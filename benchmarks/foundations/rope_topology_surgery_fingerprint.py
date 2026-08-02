"""ROPE-MODE-006: minimally displaced topology-surgery spectral test."""
from pathlib import Path
import csv, sys, time
import numpy as np
from scipy.sparse import diags, eye, kron
from scipy.sparse.linalg import eigsh
from scipy.spatial import cKDTree

ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from benchmarks.foundations.electron_variational_remesh import Model
from benchmarks.foundations.strand_substrate import gauss_link

BOXES=(4.0,5.0); H_TARGET=0.25
ALPHA=12.0; EPS=0.30; BETA=0.50; SIGMA=0.16
N_EIG=4; OUTER_SHELL=0.50


def lap1(n,h):
    return diags([-np.ones(n-1),2*np.ones(n),-np.ones(n-1)],[-1,0,1],format='csr')/(h*h)


def grid_for_box(box):
    n=int(round(2*box/H_TARGET))-1; h=2*box/(n+1)
    x=np.linspace(-box,box,n+2)[1:-1]
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    return n,h,np.column_stack([X.ravel(),Y.ravel(),Z.ravel()])


def polygon_length(c):
    return float(np.sum(np.linalg.norm(np.roll(c,-1,axis=0)-c,axis=1)))


def geom_moments(pts):
    p=pts-pts.mean(0); r2=float(np.mean(np.sum(p*p,axis=1)))
    Q=(p.T@p)/len(p); Q-=np.eye(3)*np.trace(Q)/3
    qnorm=float(np.linalg.norm(Q)/max(r2,1e-15))
    return r2,Q,qnorm


def local_surgery(a,b):
    tree=cKDTree(a); ds,ii=tree.query(b,k=1); j=int(np.argmin(ds)); i=int(ii[j])
    direction=a[i]-b[j]; direction/=np.linalg.norm(direction)
    n=len(b); inds=np.arange(n); dd=np.minimum((inds-j)%n,(j-inds)%n)
    width=80.0; w=np.exp(-0.5*(dd/width)**2)
    best=None
    for amp in np.linspace(0.08,0.22,141):
        bu=b+amp*w[:,None]*direction[None,:]
        pts=np.vstack([a,bu]); pts-=pts.mean(0); au=pts[:len(a)]; bu=pts[len(a):]
        lk=float(gauss_link(au,bu)); d=float(np.min(cKDTree(au).query(bu,k=1)[0]))
        if abs(lk)<0.02 and d>=0.060:
            rms=float(np.sqrt(np.mean(np.sum((bu-(b+(pts.mean(0) if False else 0)))**2,axis=1))))
            best=(au,bu,amp,lk,d); break
    if best is None: raise RuntimeError('local surgery failed')
    return best


def tube(xyz,pts):
    d=cKDTree(pts).query(xyz,k=1,workers=-1)[0]
    return np.exp(-0.5*(d/SIGMA)**2)


def solve(box,kind,linked_pts,surgery_pts):
    n,h,xyz=grid_for_box(box); I=eye(n,format='csr'); L=lap1(n,h)
    H0=kron(kron(L,I),I)+kron(kron(I,L),I)+kron(kron(I,I),L)
    r=np.linalg.norm(xyz,axis=1)
    if kind=='off': t=np.zeros_like(r)
    else:
        t=tube(xyz,linked_pts if kind=='linked' else surgery_pts)
    V=-ALPHA/np.sqrt(r*r+EPS*EPS)-BETA*t
    H=H0+diags(V,0,format='csr'); t0=time.time()
    vals,vecs=eigsh(H,k=N_EIG,which='SA',tol=5e-9,maxiter=15000)
    order=np.argsort(vals); vals=vals[order]; vecs=vecs[:,order]
    prob=vecs*vecs; norm=np.maximum(prob.sum(axis=0),1e-15)
    outer=prob[r>(box-OUTER_SHELL)].sum(axis=0)/norm
    return dict(box=box,n=n,h=h,kind=kind,vals=vals,gaps=vals-vals[0],outer=outer,elapsed=time.time()-t0)


def run():
    st=np.load(ROOT/'analysis'/'ELEC009_state.npz'); model=Model(20,knots=st['knots_final'],m_energy=64)
    d,lk,cert,_=model.cert(st['z_final']); a,b=model.curves(st['z_final'],1024)
    linked=np.vstack([a,b]); linked-=linked.mean(0); a=linked[:len(a)]; b=linked[len(a):]
    au,bu,amp,lku,du=local_surgery(a,b); surgery=np.vstack([au,bu])
    # geometry matching diagnostics
    rms=float(np.sqrt(np.mean(np.sum((surgery-linked)**2,axis=1))))
    L0=polygon_length(a)+polygon_length(b); L1=polygon_length(au)+polygon_length(bu); lrel=abs(L1-L0)/L0
    r20,Q0,q0=geom_moments(linked); r21,Q1,q1=geom_moments(surgery)
    r2rel=abs(r21-r20)/r20; qrel=np.linalg.norm(Q1-Q0)/max(np.linalg.norm(Q0),1e-15)
    print(f'linked cert={cert} dmin={d:.8f} Lk={lk:.8f}; surgery amp={amp:.5f} Lk={lku:.8g} dmin={du:.8f}',flush=True)
    print(f'geometry rms={rms:.8f} length_rel={lrel:.6g} r2_rel={r2rel:.6g} quadrupole_rel={qrel:.6g}',flush=True)
    results={}; rows=[]
    for box in BOXES:
        for kind in ('off','linked','surgery'):
            q=solve(box,kind,linked,surgery); results[(box,kind)]=q
            print(f"box={box:g} n={q['n']} {kind:7s} E0={q['vals'][0]:.9f} max_outer={np.max(q['outer']):.3g} time={q['elapsed']:.1f}s",flush=True)
            for k in range(N_EIG): rows.append((box,q['n'],q['h'],kind,k,q['vals'][k],q['gaps'][k],q['outer'][k]))
    coarse,fine=BOXES
    dom={k:np.abs(results[(fine,k)]['gaps']-results[(coarse,k)]['gaps']) for k in ('off','linked','surgery')}
    gl=results[(fine,'linked')]['gaps']; gs=results[(fine,'surgery')]['gaps']; topo=gl-gs
    unc=dom['linked']+dom['surgery']; sig=np.abs(topo)>3*np.maximum(unc,1e-6); sig_modes=np.where(sig[1:])[0]+1
    rel_dom=max(float(np.max(dom[k][1:]/np.maximum(np.abs(results[(fine,k)]['gaps'][1:]),0.25))) for k in dom)
    tc=results[(coarse,'linked')]['gaps']-results[(coarse,'surgery')]['gaps']
    stable=[np.sign(tc[i])==np.sign(topo[i]) and abs(tc[i]-topo[i])<max(0.5*abs(topo[i]),1e-5) for i in sig_modes]
    B1=bool(cert and d>=.060 and abs(abs(lk)-1)<.03 and abs(lku)<.02 and du>=.060)
    B2=bool(rms<.05 and lrel<.01 and r2rel<.02 and qrel<.08)
    B3=all(np.max(results[(fine,k)]['outer'])<.001 for k in ('off','linked','surgery'))
    B4=rel_dom<.01
    B5=len(sig_modes)>=2
    B6=bool(len(sig_modes)>0 and all(stable))
    finding='MINIMALLY_MATCHED_TOPOLOGY_FINGERPRINT_DETECTED' if all((B1,B2,B3,B4,B5,B6)) else 'NO_MINIMALLY_MATCHED_TOPOLOGY_FINGERPRINT'
    with open(ROOT/'analysis'/'ROPE_MODE006_spectrum.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['box','grid_n','h','control','mode','eigenvalue','excitation_gap','outer_shell_probability']); w.writerows(rows)
    with open(ROOT/'analysis'/'ROPE_MODE006_contrasts.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['mode','linked_minus_surgery','combined_domain_uncertainty','significant_3sigma','coarse_contrast'])
        for i in range(N_EIG): w.writerow([i,topo[i],unc[i],bool(sig[i]),tc[i]])
    lines=['ROPE-MODE-006 local topology-surgery fingerprint',f'linked certified={cert} dmin={d:.8f} Lk={lk:.8f}',f'surgery amplitude={amp:.6f} Lk={lku:.8g} dmin={du:.8f}',f'geometry rms={rms:.8g} length_rel={lrel:.8g} radial_moment_rel={r2rel:.8g} quadrupole_rel={qrel:.8g}',f'alpha={ALPHA} eps={EPS} beta={BETA} sigma={SIGMA} boxes={BOXES} h={H_TARGET}',f'max outer probability={max(np.max(results[(fine,k)]["outer"]) for k in ("off","linked","surgery")):.8g}',f'worst relative gap drift={rel_dom:.8g}',f'3sigma contrast modes={sig_modes.tolist()}']
    for nm,v in [('B1 topology controls certified',B1),('B2 geometry matched',B2),('B3 boundary leakage',B3),('B4 domain-converged gaps',B4),('B5 topology contrast significant',B5),('B6 contrast stable',B6)]: lines.append(nm+': '+('PASS' if v else 'FAIL'))
    lines.append('FINDING: '+finding); text='\n'.join(lines); print(text)
    (ROOT/'analysis'/'ROPE_MODE006_run.log').write_text(text+'\n')
    np.savez(ROOT/'analysis'/'ROPE_MODE006_summary.npz',boxes=np.array(BOXES),dmin=d,lk=lk,lku=lku,amp=amp,rms=rms,length_rel=lrel,r2_rel=r2rel,quadrupole_rel=qrel,contrast=topo,uncertainty=unc,significant=sig)
    return finding

if __name__=='__main__': run()
