"""Q54 v-bar B -- the v5 ramp control (charter:
analysis/Q54_charter_LOCKED.md), resumable across reap windows.
Each completed ladder stage's OUTPUT state persists under its own
key so restarts advance instead of replaying."""
import numpy as np, pickle, sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1     # noqa

FRACS = (0.15, 0.3, 0.55, 0.8)


def main():
    st = q1.load()
    vb = st.setdefault('q54-vbarB', {})
    T = q1.QTGrid(96, 36, 2, 3)
    A2 = q1.WAYPOINTS[0]

    xw = None
    for frac in FRACS:
        kk = f'done-{frac}'
        if kk in vb:
            xw = np.asarray(vb[kk], float)
            continue
        sub = frac * A2
        seed = q1.ramp_seed(T, sub) if xw is None else xw
        xw, _ = q1.gn_lean(T, seed, 'a2', sub, rounds=10, st=st,
                           key=f'q54v5-sub{frac}')
        vb[kk] = xw
        q1.save(st)
        print(f"[vbarB] sub-pin {frac} done (RMS "
              f"{T.field_rms(xw):.1e})", flush=True)

    if 'done-final' not in vb:
        xn, _ = q1.gn_lean(T, xw, 'a2', A2, rounds=40, st=st,
                           key='q54v5-final')
        m, ok = q1.gate(T, xn, 'Q54 v-bar B control', pin=A2)
        if ok:
            vb['done-final'] = xn
            vb['metrics'] = {k: v for k, v in m.items() if k != 'x'}
            q1.save(st)
            print(f"[vbarB] ** PASS ** RMS {m['rms']:.2e} clos "
                  f"{m['clos']:.2e} A2 {m['A2']:.7f} (pin "
                  f"{A2:.7f})", flush=True)
        else:
            q1.save(st)
            print(f"[vbarB] not gated this chunk (RMS {m['rms']:.1e} "
                  f"clos {m['clos']:.1e}) -- resume", flush=True)
    else:
        print("[vbarB] already PASS", flush=True)


if __name__ == '__main__':
    main()
