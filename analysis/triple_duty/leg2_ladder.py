"""TRIPLE-DUTY Leg 2 (R2): the BLOCH-L anchor solve as a function of s (level-1 angle),
registered inputs otherwise (S2, p = a_f, KT0 = 2, kb = 0), one rung per invocation.
Ladder locked at charter: s in {0.20,0.25,0.30,0.35,0.40,0.45,0.50} (1/3 NOT on it).
Bar v3: FND-126's 0.5 pct reading-window drift (24p vs 48p) per rung."""
import sys, json, pathlib, numpy as np
sys.path.insert(0,'benchmarks/foundations')
import blochl_longitudinal as B
from scipy.optimize import fsolve
LADDER = [0.20,0.25,0.30,0.35,0.40,0.45,0.50]
OUT = pathlib.Path('analysis/triple_duty/leg2_ladder.json')
res = json.loads(OUT.read_text()) if OUT.exists() else {}
todo = [s for s in LADDER if str(s) not in res]
if not todo: print("LADDER COMPLETE"); sys.exit(0)
s = todo[0]
B.S1 = s; B.PSI1 = np.arcsin(np.sqrt(s)); B.C1 = np.sqrt(s); B.ST1 = np.sqrt(1-B.C1**2)
B.KAP1 = (np.pi/B.PPHYS)*2*B.C1*B.ST1
def resid(x, kb):
    rr = B.branch(max(x[0],1e-6), x[1], kb, 6, 24)
    return [rr['T'][0]**2 - 1.0, rr['L'][0]**2 - B.KT0]
kf, T = fsolve(resid, [9.0, 1.5], args=(0.0,))
r24 = B.branch(kf, T, 0.0, 6, 24); r48 = B.branch(kf, T, 0.0, 6, 48)
drift = abs(r48['L'][0]-r24['L'][0])/r24['L'][0]
conv = drift <= 0.005
M = T - 1.0/(1.0-s)
res[str(s)] = dict(kf=float(kf), T=float(T), drift=float(drift), converged=bool(conv), M=float(M), Mrel=float(M/(1/(1-s))))
OUT.write_text(json.dumps(res, indent=1))
print(f"rung s={s}: k_f/T0_f={kf:.5f}  T_fibre/T0_f={T:.5f}  1/(1-s)={1/(1-s):.5f}  M(s)={M:+.5f} ({M/(1/(1-s))*100:+.2f}%)  drift={drift*100:.3f}% [{'converged' if conv else 'UNREACHED'}]")
