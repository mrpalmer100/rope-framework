"""CASIMIR-PLATE Leg 0, controls v2/v3 (+v4/v5): scalar linear-dispersion lattice chain,
piston geometry, Dirichlet / Neumann plates. ZP-CONV: carried modes, E_mode = (1/2) omega
(hbar = 1 as the control's unit; the charter permits pi^2/1440 in this leg). E per area:
piston(d) = E_slab(d) + E_slab(L-d) - 2 E_slab(L/2). In-plane: fine W x W k grid, vectorized."""
import numpy as np, json
def kpar2_grid(W):
    k = 2*np.pi*(np.arange(W)+0.5)/W          # midpoint grid (avoids the k=0 corner bias)
    kx, ky = np.meshgrid(k, k, indexing='ij')
    return (4*np.sin(kx/2)**2 + 4*np.sin(ky/2)**2).ravel()
def E_slab(n, kp2, bc):
    kz = np.pi*np.arange(1,n+1)/(n+1) if bc=='D' else np.pi*np.arange(0,n)/n
    ez = 4*np.sin(kz/2)**2
    e = 0.0
    for z in ez: e += 0.5*np.sum(np.sqrt(z + kp2))
    return e/len(kp2)
def piston(d, L, kp2, bc): return E_slab(d,kp2,bc) + E_slab(L-d,kp2,bc) - 2*E_slab(L//2,kp2,bc)
out={}
for bc in ('D','N'):
    W=1024; kp2=kpar2_grid(W); kp2b=kpar2_grid(2*W)
    rows=[]
    for d in (8,16,32,64):
        L=4*64; E=piston(d,L,kp2,bc)
        rows.append([d,E])
    Etop2 = piston(64,4*64,kp2b,bc); v4 = abs(Etop2-rows[-1][1])/abs(rows[-1][1])
    ds=np.array([r[0] for r in rows]); Es=np.array([r[1] for r in rows])
    pE = -np.polyfit(np.log(ds[-3:]), np.log(np.abs(Es[-3:])), 1)[0]
    K = np.abs(Es)*ds**3; r1=(4*K[-1]-K[-2])/3; r2=(4*K[-2]-K[-3])/3
    Lchk=[piston(16,LL,kp2,bc) for LL in (3*64,4*64,6*64)]; v5=(max(Lchk)-min(Lchk))/abs(np.mean(Lchk))
    out[bc]=dict(rows=rows,pE=float(pE),pF=float(pE+1),K=K.tolist(),rich=(float(r1),float(r2)),v4=float(v4),v5=float(v5),sign=float(np.sign(Es[-1])))
    print(f"[{bc}] E(d): {[round(e,7) for e in Es]}  sign {np.sign(Es[-1]):+.0f}")
    print(f"     p_E = {pE:.3f} (force p = {pE+1:.3f}; window [3.9,4.1])   K d^3 = {np.round(K,6)}   Richardson {r1:.6f}/{r2:.6f}   target pi^2/1440 = {np.pi**2/1440:.6f}")
    print(f"     v4 (W 1024->2048) {v4:.1e}   v5 L-spread {v5:.1e}")
json.dump(out, open('analysis/casimir/leg0_scalar_piston.json','w'), indent=1)
