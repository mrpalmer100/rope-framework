"""SPARSE-J C4 -- MEMORY CEILING (charter: analysis/SPARSEJ_charter_LOCKED.md).

Bar: peak RSS of one FULL solve round (jacobian + factor + solve +
line search) at 144x54 <= 3.0 GB, measured; reported alongside the
same measurement at 144x36 and 144x42. State at 54/42: the retained
144x36 member prolongated along phi by Fourier interpolation (pt
unwrapped for winding) -- a MEMORY measurement only; no solve claims
from prolongated states (charter S3 rule extended to C4 by the same
logic). Run one grid per invocation: python3 sparsej_c4.py <NP>.
Memo writes disabled for the round measurement (resume scaffolding,
not the solve); the with-memo figure is reported separately.
"""
import numpy as np, pickle, pathlib, sys, time, resource, os, threading

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1           # noqa
from benchmarks.foundations import sparsej_instrument as SJ      # noqa

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'   # shared cache file
S2C = ROOT / 'analysis' / 'qsweep_stage2c_ckpt.pkl'
OUT = pathlib.Path('/tmp/sjc4_results.pkl')


def peak_rss_gb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6


class RssWatch(threading.Thread):
    """/proc sampler -- ru_maxrss can miss short mmap spikes."""
    def __init__(self):
        super().__init__(daemon=True); self.peak = 0.0; self.go = True
    def run(self):
        while self.go:
            with open('/proc/self/status') as f:
                for ln in f:
                    if ln.startswith('VmRSS'):
                        self.peak = max(self.peak,
                                        int(ln.split()[1]) / 1e6)
            time.sleep(0.05)


def prolongate(x, NS, NP0, NP1):
    """Fourier refinement along phi; pt unwrapped (winding trend
    removed, interpolated, re-added)."""
    N0, N1 = NS * NP0, NS * NP1
    out = np.empty(3 * N1 + 2)
    out[-2:] = x[-2:]
    for f in range(3):
        F = x[f * N0:(f + 1) * N0].reshape(NS, NP0)
        if f == 1:                                   # pt: angle field
            Fu = np.unwrap(F, axis=1)
            k = np.round((Fu[:, -1] - Fu[:, 0]) /
                         (2 * np.pi) * NP0 / (NP0 - 1))
            trend = (np.arange(NP0)[None, :] / NP0) * 2 * np.pi * k[:, None]
            G = _fint(Fu - trend, NP1) + \
                (np.arange(NP1)[None, :] / NP1) * 2 * np.pi * k[:, None]
        else:
            G = _fint(F, NP1)
        out[f * N1:(f + 1) * N1] = G.ravel()
    return out


def _fint(F, NP1):
    NP0 = F.shape[1]
    C = np.fft.rfft(F, axis=1)
    C1 = np.zeros((F.shape[0], NP1 // 2 + 1), complex)
    C1[:, :C.shape[1]] = C
    return np.fft.irfft(C1, n=NP1, axis=1) * (NP1 / NP0)


def main(NP1):
    watch = RssWatch(); watch.start()
    T = q1.QTGrid(144, NP1, 3, 4)
    rec = pickle.loads(S2C.read_bytes())['prof-4/3']
    x36_0 = np.asarray(rec['states'][0], float)
    x36_1 = np.asarray(rec['states'][1], float)
    if NP1 == 36:
        x0, x1 = x36_0, x36_1
    else:
        x0, x1 = prolongate(x36_0, 144, 36, NP1), \
                 prolongate(x36_1, 144, 36, NP1)
    t = (x1 - x0); t /= np.linalg.norm(t)
    aux = (x1, t, 0.08)
    x = x1 + 0.08 * t

    tt = time.time()
    sj, _ = SJ.make_instrument(T, x, 'arc', aux, 50.0, cache=str(PAT))
    t_pat = time.time() - tt
    bs = SJ.BandedTorusSolver(144, NP1, nglob=2)
    print(f'[c4 {144}x{NP1}] pattern+instrument {t_pat:.0f}s  '
          f'RSS {watch.peak:.2f} GB', flush=True)

    base = watch.peak
    tt = time.time()
    # ---- ONE FULL SOLVE ROUND (gn_sparse round body, memo off) ----
    fx = float(np.linalg.norm(T.wres(x, 'arc', aux, 50.0)))
    J, r0 = sj(x, 'arc', aux, 50.0)
    t_jac = time.time() - tt
    d2 = np.maximum(np.asarray(J.power(2).sum(axis=0)).ravel(), 1e-12)
    tt = time.time()
    bs.factor(J, 1e-4, d2)
    t_fac = time.time() - tt
    dx = bs.solve(J.T @ r0)
    nd = float(np.linalg.norm(dx))
    if nd > 0.05:
        dx = dx * (0.05 / nd)
    acc, f2b = False, None
    for a_ in (1.0, 0.5, 0.25, 0.1, 0.03):
        f2 = float(np.linalg.norm(T.wres(x + a_ * dx, 'arc', aux, 50.0)))
        if f2 < fx:
            acc, f2b = True, f2
            break
    watch.go = False
    res = dict(grid=f'144x{NP1}', peak_proc=watch.peak,
               peak_ru=peak_rss_gb(), t_pattern=t_pat, t_jac=t_jac,
               t_factor=t_fac, wres0=fx, wres1=f2b, accepted=acc,
               n=x.size, nnz=int(J.nnz))
    d = pickle.loads(OUT.read_bytes()) if OUT.exists() else {}
    d[f'144x{NP1}'] = res
    OUT.write_bytes(pickle.dumps(d))
    print(f"[c4 144x{NP1}] ROUND: jac {t_jac:.0f}s factor {t_fac:.0f}s "
          f"wres {fx:.2e} -> {f2b if f2b else float('nan'):.2e} "
          f"acc {acc}", flush=True)
    print(f"[c4 144x{NP1}] PEAK RSS {watch.peak:.3f} GB (/proc)  "
          f"{peak_rss_gb():.3f} GB (ru_maxrss)  "
          f"[bar 3.0 GB at 144x54]", flush=True)


if __name__ == '__main__':
    main(int(sys.argv[1]))
