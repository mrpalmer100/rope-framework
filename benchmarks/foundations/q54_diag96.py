"""Q54 DIAGNOSTIC (not the chartered column): does the q = 5/4
injection catch at 96x36 on the DENSE registered instrument?
Discriminates cell-physics vs instrument/grid for the 144x36
guard-floor deadlock (see the Q54 session record). Identical
ladder mechanics to run_q rung 1; identical guard. Resumable."""
import numpy as np, pickle, sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1     # noqa

FRACS = (0.15, 0.3, 0.55, 0.8)


def main():
    st = q1.load()
    d = st.setdefault('q54-diag96', {})
    T = q1.QTGrid(96, 36, 4, 5)
    A2 = q1.WAYPOINTS[0]
    xw = None
    for frac in FRACS:
        kk = f'done-{frac}'
        if kk in d:
            xw = np.asarray(d[kk], float)
            continue
        sub = frac * A2
        seed = q1.ramp_seed(T, sub) if xw is None else xw
        print(f"  [diag96 5/4] sub-pin {sub:.7f}", flush=True)
        xw, _ = q1.gn_lean(T, seed, 'a2', sub, rounds=10, st=st,
                           key=f'q54d96-sub{frac}', stop_rms=1e-5)
        _, c2 = T.modes(T.geom(xw)[2])
        d[kk] = xw
        d[f'ratio-{frac}'] = float(abs(c2) / sub)
        q1.save(st)
        print(f"  [diag96 5/4] rung {frac} done: |A2|/pin = "
              f"{abs(c2)/sub:.3f}  RMS {T.field_rms(xw):.1e}",
              flush=True)
    if 'final' not in d:
        xn, _ = q1.gn_lean(T, xw, 'a2', A2, rounds=40, st=st,
                           key='q54d96-final')
        m, ok = q1.gate(T, xn, 'diag96 5/4 waypoint', pin=A2)
        d['final'] = {k: v for k, v in m.items()}
        d['gated'] = bool(ok)
        q1.save(st)
        print(f"  [diag96 5/4] waypoint {'GATED' if ok else 'not gated'}"
              f": |A2| {m['A2']:.7f} (pin {A2:.7f}) RMS {m['rms']:.1e}",
              flush=True)


if __name__ == '__main__':
    main()
