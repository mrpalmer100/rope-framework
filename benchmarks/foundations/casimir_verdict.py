"""CASIMIR-PLATE Legs 3-5: readings from the checkpoint, exponent/coefficient, verdict.
Run ONCE in the session after the local ladder completes. Targets (pi^2/240) load in Leg 5 only."""
import numpy as np, pickle, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
st = pickle.loads((ROOT/'analysis'/'casimir_plate_ckpt.pkl').read_bytes())
m = st['meta']; R, L = m['rungs'], m['L']; K = st['k']
def g(d,L): return 1+(d/(L-d))**3-2*(2*d/L)**3
def piston(fun):
    out={}
    for d in R:
        tot=0.0; wsum=0.0
        for i,rec in K.items():
            if rec['W']==0: continue
            e = fun(rec['om'][d]) + fun(rec['om'][L-d]) - 2*fun(rec['om'][L//2])
            tot += e*rec['W']; wsum += rec['W']
        out[d] = tot/(2*np.pi)**2 / g(d+1, L+2)
    return out
E2 = piston(lambda om: 0.5*np.sum(om))                       # reading (ii), S = 1
E3 = piston(lambda om: np.sum(np.log(np.maximum(om,1e-12)))) # reading (iii), k_B T_w = 1
k0 = [rec for rec in K.values() if rec['W']==0]
E1 = {d: 0.5*(np.sum(k0[0]['om'][d])+np.sum(k0[0]['om'][L-d])-2*np.sum(k0[0]['om'][L//2]))/g(d+1,L+2) for d in R} if k0 else None
def fit(E, name):
    ds=np.array(R)+1.0; Es=np.array([E[d] for d in R])
    pE=-np.polyfit(np.log(ds[-3:]),np.log(np.abs(Es[-3:])),1)[0]
    Kc=np.abs(Es)*ds**(np.round(pE)); r1=(4*Kc[-1]-Kc[-2])/3; r2=(4*Kc[-2]-Kc[-3])/3
    print(f"{name}: E(d)={[f'{e:.3e}' for e in Es]} sign {np.sign(Es[-1]):+.0f}  p_E={pE:.3f} (force p={pE+1:.3f})  K={np.round(Kc,6)}  Richardson {r1:.6f}/{r2:.6f}")
    return pE+1, r1, r2, np.sign(Es[-1])
print("LEG 3 -- readings"); p2,r21,r22,s2 = fit(E2,"(ii) standing-wave action"); p3,_,_,_ = fit(E3,"(iii) warm-weave (log-sum)")
if E1: fit(E1,"(i) coherent winding (k_par=0 slice)")
print("\nLEG 5 -- targets loaded once"); K2_target = 2*np.pi**2/1440   # two polarizations x pi^2/1440 (energy coefficient; force pi^2/240)
print(f"  two-polarization energy coefficient pi^2/720 = {K2_target:.6f}; measured (ii) Richardson {r21:.6f}/{r22:.6f} -> ratio {r21/K2_target:.3f}/{r22/K2_target:.3f}")
inwin = 3.9 <= p2 <= 4.1
if not inwin: print("  VERDICT: CAS-SHAPE-FAIL candidate (p not 4 under reading (ii)); check (i)/(iii) before rendering")
elif abs(r21/K2_target-1) <= 0.01 or abs(r22/K2_target-1) <= 0.01: print("  VERDICT: CAS-FORM (p=4, K_2 = pi^2/240-class within 1%); sub-verdict PIN/GAP/OVER needs S_1(a_f) vs S_req -- next step")
else: print(f"  VERDICT: p=4 but K/K_2 = {r21/K2_target:.3f}: CAS-CHANNEL-KILL if the excess traces to the longitudinal carrier (K_tot/K_2 - 1 > 0.03), else NO CALL")
