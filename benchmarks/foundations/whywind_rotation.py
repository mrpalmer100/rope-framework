"""WHY-WINDING BRICK 2a -- mode-resolved sector rotation.
Executed under analysis/WHYWIND_rotation_bars_LOCKED.md.
Read-only on analysis/qsweep_stage2c_ckpt.pkl.
"""
import pathlib
import pickle
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations.qsweep_stage1 import QTGrid          # noqa: E402
from benchmarks.foundations.whywind_coupling import probe        # noqa: E402

CK = pathlib.Path('analysis/qsweep_stage2c_ckpt.pkl')
LINES = {
    '4/3': dict(cell=(3, 4), fire=[(2, 6)], ctrl=(2, 7)),
    '5/3': dict(cell=(3, 5), fire=[(2, 9), (3, 12)], ctrl=(2, 10)),
}


def run_cell(q, states, meas):
    n1, n2 = LINES[q]['cell']
    T = QTGrid(144, 36, n1, n2)
    X = [np.asarray(s) for s in states]
    rows = []
    for i in range(len(meas)):
        x, xn = X[i + 1], X[i + 2]
        t = (xn - x) / np.linalg.norm(xn - x)
        rec = dict(A2=float(meas[i]['A2']), fdir=float(meas[i]['fdir']))
        for tag, nm in ([('fire%d' % k, nm) for k, nm in
                         enumerate(LINES[q]['fire'])]
                        + [('ctrl', LINES[q]['ctrl'])]):
            vals = [abs(probe(T, nm[0], nm[1], quad) @ t) for quad in 'cs']
            rec[tag] = float(np.sqrt(np.mean(np.square(vals))))
        # display only: total pt share of the tangent (FND-152 kin)
        rec['pt_share'] = float(np.linalg.norm(t[T.N:2 * T.N]))
        rows.append(rec)
    return rows


def main():
    st = pickle.loads(CK.read_bytes())
    out = {}
    for q in ('4/3', '5/3'):
        out[q] = run_cell(q, st['prof-%s' % q]['states'],
                          st['prof-%s' % q]['meas'])
        print(f"\n== q = {q} kappa table (tangent of arc pair i)")
        hdr = ['A2', 'fdir'] + [k for k in out[q][0]
                                if k.startswith('fire')] \
            + ['ctrl', 'pt_share']
        print('   ' + '  '.join(f'{h:>9s}' for h in hdr))
        for r in out[q]:
            print('   ' + '  '.join(f'{r[h]:9.5f}' if h != 'A2'
                                    else f'{r[h]:9.6f}' for h in hdr))

    r43, r53 = out['4/3'], out['5/3']
    span43 = [r['fire0'] for r in r43[-8:]]
    span53 = [max(r['fire0'], r['fire1']) for r in r53[-8:]]
    m43, m53 = float(np.median(span43)), float(np.median(span53))
    R1 = m43 >= 10 * m53
    mc = float(np.median([r['ctrl'] for r in r43[-8:]]))
    R2 = m43 >= 5 * mc
    f43 = np.array([r['fire0'] for r in r43])
    fd43 = np.array([r['fdir'] for r in r43])
    rho43 = float(np.corrcoef(f43, fd43)[0, 1])
    f53 = np.array([max(r['fire0'], r['fire1']) for r in r53])
    fd53 = np.array([r['fdir'] for r in r53])
    rho53 = float(np.corrcoef(f53, fd53)[0, 1])
    rng = (f53.max() - f53.min()) < 0.2 * (f43.max() - f43.min())
    R3 = rho43 >= 0.7 and (rho53 < 0.5 or rng)
    print('\n== VERDICT BLOCK ==')
    print(f'R1 contrast: median kappa 4/3 fire {m43:.5f} vs 10x 5/3 '
          f'1:1 {10*m53:.5f}  -> {"PASS" if R1 else "FAIL"}')
    print(f'R2 within-cell: {m43:.5f} vs 5x ctrl {5*mc:.5f}  -> '
          f'{"PASS" if R2 else "FAIL"}')
    print(f'R3 co-movement: r(4/3)={rho43:.3f} (>=0.7); r(5/3)='
          f'{rho53:.3f} (<0.5) or range ratio ({rng})  -> '
          f'{"PASS" if R3 else "FAIL"}')
    v = 'SEL-CONFIRMED' if (R1 and R2 and R3) else 'SEL-OPEN'
    print(f'\n**** VERDICT: {v} ****')


if __name__ == '__main__':
    main()
