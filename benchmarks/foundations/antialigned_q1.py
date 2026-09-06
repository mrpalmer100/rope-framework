"""ANTI-ALIGNED (ITEM 6a) Q1 + v1/v2 -- the linear internal spectrum per retained cell,
both sectors, at infinitesimal amplitude (A2 = 0.02 R2), on the 144x36 chart with the
SJ-CREDENTIALED instrument (stage-2's Leg 0 protocol: a2-pinned small-amplitude solve
with om2 FREE; the converged om2 is the linear root). Two seeds per sector as stage 2
used (aligned +0.65 Om1 / +1.2 Om1; anti-aligned -0.35 Om1 / -0.65 Om1). Cells: 3/2
(v1/v2 reproduction: +3.201 / -2.221), 4/3, 5/3, 5/4. One (cell, seed) per invocation;
checkpoint analysis/antialigned_ckpt.pkl. Charter D1: 'on a mode' = within 1e-4 of
Om1 n / N1 (the cell ladder sqrt(T) k1 n / N1). NO number from the charter's expected
outcomes is entered; the ladder is computed from the cell's own Om1.
"""
import numpy as np, pickle, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1            # noqa
from benchmarks.foundations import sparsej_instrument as SJ       # noqa
from benchmarks.foundations import truestate_stage2 as S2    # noqa

ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'antialigned_ckpt.pkl'
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
CELLS = [('3/2', 2, 3), ('4/3', 3, 4), ('5/3', 3, 5), ('5/4', 4, 5)]
SEEDS = [('aligned', +0.65), ('aligned', +1.20), ('anti', -0.35), ('anti', -0.65)]   # x Om1


def main():
    st = pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {}
    for tag, N1, N2 in CELLS:
        for sec, fac in SEEDS:
            key = f'{tag}|{sec}|{fac:+.2f}'
            if key in st and st[key].get('done'):
                continue
            T = q1.QTGrid(144, 36, N1, N2)
            G = T.G2
            W, Z, Tf, gam, om1 = G.level1()
            A2 = 0.02 * S2.R2
            ph = np.exp(1j * G.K2 * G.sgrid)[:, None] * np.exp(-1j * G.pgrid)[None, :]
            x0 = T.from_stage2(G.pack(W + A2 * ph, Z, Tf, gam, om1, fac * om1))
            sj, _ = SJ.make_instrument(T, x0, 'a2', A2, 50.0, cache=str(PAT))
            bs = SJ.BandedTorusSolver(144, 36, nglob=2)
            xn = SJ.gn_sparse(T, x0, 'a2', A2, sj, bs, rounds=60, st=st, key=key + '|solve')
            m, ok = q1.gate(T, xn, key, pin=A2)
            it = st.get(key + '|solve', {}).get('it', -1)
            done = ok or it >= 59
            if done:
                ladder = [om1 * n / N1 for n in range(1, 4 * N1 + 1)]
                near = min(ladder, key=lambda L: abs(abs(m['om2']) - L))
                st[key] = dict(done=True, gated=bool(ok), om2=float(m['om2']), om1=float(om1), rms=float(m['rms']),
                               ladder_nearest=float(near), rel=float(abs(abs(m['om2']) - near) / near))
                CKPT.write_bytes(pickle.dumps(st))
                print(f"[{key}] {'GATED' if ok else 'BUDGET'} om2 = {m['om2']:+.5f} (Om1 {om1:.5f}); nearest cell mode "
                      f"{near:.5f} ({'ON' if abs(abs(m['om2'])-near)/near < 1e-4 else 'off'} by {abs(abs(m['om2'])-near)/near:.1e})",
                      flush=True)
            else:
                print(f"[{key}] resume (round {it})", flush=True)
            return
    print("[antialigned] ALL CELLS COMPLETE -- run the Q1 verdict", flush=True)


if __name__ == '__main__':
    main()
