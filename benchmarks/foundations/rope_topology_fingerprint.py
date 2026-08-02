"""ROPE-MODE-004: topology-specific spectral fingerprint in 3-D bound states.

Tests whether a certified Hopf-linked tubular perturbation leaves a measurable,
converged spectral fingerprint beyond matched unlinked and spherically averaged
controls.  The central field creates ordinary bound states; the rope is a
small perturbation whose causal contribution is isolated by controls.
"""
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

BOXES=(3.0,4.0)
H_TARGET=0.25
ALPHA=12.0
EPS=0.30
BETA=0.50
SIGMA=0.16
N_EIG=12
OUTER_SHELL=0.50
BOUNDARY_TOL=0.01
DOMAIN_TOL=0.03
EFFECT_SIGMA=3.0


def lap1(n,h):
    return diags([-np.ones(n-1),2*np.ones(n),-np.ones(n-1)],[-1,0,1],format='csr')/(h*h)


def grid_for_box(box):
    n=int(round(2*box/H_TARGET))-1
    h=2*box/(n+1)
    x=np.linspace(-box,box,n+2)[1:-1]
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    return n,h,np.column_stack([X.ravel(),Y.ravel(),Z.ravel()])


def make_unlinked(a,b):
    # Preserve both curve shapes and lengths exactly; translate one component
    # until Gauss linking is numerically zero and the tubes are disjoint.
    best=None
    for shift in np.linspace(0.4,3.0,27):
        bu=b+np.array([shift,0.0,0.0])
        pts=np.vstack([a,bu]); pts-=pts.mean(0)
        au=pts[:len(a)]; bu=pts[len(a):]
        lk=gauss_link(au,bu)
        d=np.min(cKDTree(au).query(bu,k=1)[0])
        if abs(lk)<0.02 and d>0.12:
            best=(au,bu,shift,lk,d); break
    if best is None: raise RuntimeError('could not construct unlinked control')
    return best


def tube_profiles(xyz, linked_pts, unlinked_pts):
    dl=cKDTree(linked_pts).query(xyz,k=1,workers=-1)[0]
    du=cKDTree(unlinked_pts).query(xyz,k=1,workers=-1)[0]
    tl=np.exp(-0.5*(dl/SIGMA)**2)
    tu=np.exp(-0.5*(du/SIGMA)**2)
    # Spherical average of the linked tube profile on this grid.
    r=np.linalg.norm(xyz,axis=1)
    bins=np.linspace(0,r.max()+1e-12,120)
    idx=np.clip(np.digitize(r,bins)-1,0,len(bins)-2)
    sums=np.bincount(idx,weights=tl,minlength=len(bins)-1)
    cnt=np.bincount(idx,minlength=len(bins)-1)
    means=sums/np.maximum(cnt,1)
    ts=means[idx]
    # Match integrated perturbation strength across controls.
    target=tl.sum()
    for arr in (tu,ts): arr*=target/max(arr.sum(),1e-15)
    return tl,tu,ts,r


def solve(box, kind, linked_pts, unlinked_pts):
    n,h,xyz=grid_for_box(box)
    I=eye(n,format='csr'); L=lap1(n,h)
    H0=kron(kron(L,I),I)+kron(kron(I,L),I)+kron(kron(I,I),L)
    tl,tu,ts,r=tube_profiles(xyz,linked_pts,unlinked_pts)
    tube={'off':np.zeros_like(r),'linked':tl,'unlinked':tu,'spherical':ts}[kind]
    V=-ALPHA/np.sqrt(r*r+EPS*EPS)-BETA*tube
    H=H0+diags(V,0,format='csr')
    t0=time.time()
    vals,vecs=eigsh(H,k=N_EIG,which='SA',tol=5e-8,maxiter=10000)
    order=np.argsort(vals); vals=vals[order]; vecs=vecs[:,order]
    prob=vecs*vecs; norm=np.maximum(prob.sum(axis=0),1e-15)
    outer=prob[r>(box-OUTER_SHELL)].sum(axis=0)/norm
    inner=prob[r<2.2].sum(axis=0)/norm
    return dict(box=box,n=n,h=h,kind=kind,vals=vals,gaps=vals-vals[0],outer=outer,inner=inner,elapsed=time.time()-t0)


def run():
    st=np.load(ROOT/'analysis'/'ELEC009_state.npz')
    model=Model(20,knots=st['knots_final'],m_energy=64)
    d,lk,cert,_=model.cert(st['z_final'])
    a,b=model.curves(st['z_final'],1024)
    linked_pts=np.vstack([a,b])
    au,bu,shift,lku,du=make_unlinked(a,b)
    unlinked_pts=np.vstack([au,bu])
    print(f'linked cert={cert} dmin={d:.8f} Lk={lk:.8f}; unlinked shift={shift:.3f} Lk={lku:.6f} dmin~={du:.6f}',flush=True)
    results={}; rows=[]
    for box in BOXES:
        for kind in ('off','linked','unlinked','spherical'):
            q=solve(box,kind,linked_pts,unlinked_pts); results[(box,kind)]=q
            print(f"box={box:g} n={q['n']} {kind:9s} E0={q['vals'][0]:.8f} outer12={np.max(q['outer']):.4g} time={q['elapsed']:.1f}s",flush=True)
            for k in range(N_EIG): rows.append((box,q['n'],q['h'],kind,k,q['vals'][k],q['gaps'][k],q['outer'][k],q['inner'][k]))
    coarse,fine=BOXES
    # Domain uncertainty estimated from excitation-gap drift for each control.
    domain={}
    for kind in ('off','linked','unlinked','spherical'):
        a0=results[(coarse,kind)]['gaps']; a1=results[(fine,kind)]['gaps']
        domain[kind]=np.abs(a1-a0)
    vf={k:results[(fine,k)]['gaps'] for k in ('off','linked','unlinked','spherical')}
    shifts={k:vf[k]-vf['off'] for k in ('linked','unlinked','spherical')}
    topo=shifts['linked']-shifts['unlinked']
    anis=shifts['linked']-shifts['spherical']
    uncertainty=domain['linked']+domain['unlinked']
    significant=np.abs(topo)>EFFECT_SIGMA*np.maximum(uncertainty,1e-5)
    # Exclude ground gap mode 0; count low excited states with robust topology contrast.
    sig_modes=np.where(significant[1:]+False)[0]+1
    B1=bool(cert and d>=0.060 and abs(abs(lk)-1)<0.03 and abs(lku)<0.02)
    B2=all(np.max(results[(fine,k)]['outer'][:N_EIG])<BOUNDARY_TOL for k in ('off','linked','unlinked','spherical'))
    rel_domain=max(float(np.max(domain[k][1:]/np.maximum(np.abs(vf[k][1:]),0.25))) for k in domain)
    B3=rel_domain<DOMAIN_TOL
    max_effect=float(np.max(np.abs(shifts['linked'][1:])))
    B4=max_effect>1e-4
    B5=len(sig_modes)>=2
    # Require topology contrast to survive in sign and magnitude between both boxes.
    tc=(results[(coarse,'linked')]['gaps']-results[(coarse,'off')]['gaps'])-(results[(coarse,'unlinked')]['gaps']-results[(coarse,'off')]['gaps'])
    stable=[]
    for i in sig_modes:
        stable.append(np.sign(tc[i])==np.sign(topo[i]) and abs(tc[i]-topo[i])<max(0.5*abs(topo[i]),3e-4))
    B6=bool(sig_modes.size and all(stable))
    finding='TOPOLOGY_SPECIFIC_SPECTRAL_FINGERPRINT_DETECTED' if all((B1,B2,B3,B4,B5,B6)) else 'NO_CONVERGED_TOPOLOGY_SPECIFIC_FINGERPRINT'

    with open(ROOT/'analysis'/'ROPE_MODE004_spectrum.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['box','grid_n','h','control','mode','eigenvalue','excitation_gap','outer_shell_probability','r_lt_2p2_probability']); w.writerows(rows)
    with open(ROOT/'analysis'/'ROPE_MODE004_contrasts.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['mode','linked_shift','unlinked_shift','spherical_shift','linked_minus_unlinked','linked_minus_spherical','domain_uncertainty','significant_3sigma'])
        for i in range(N_EIG): w.writerow([i,shifts['linked'][i],shifts['unlinked'][i],shifts['spherical'][i],topo[i],anis[i],uncertainty[i],bool(significant[i])])
    lines=['ROPE-MODE-004 topology fingerprint',f'linked certified={cert} dmin={d:.8f} Lk={lk:.8f}',f'unlinked Lk={lku:.8f} translation={shift:.4f} approximate dmin={du:.8f}',f'alpha={ALPHA} eps={EPS} beta={BETA} sigma={SIGMA} boxes={BOXES} h_target={H_TARGET}',f'max outer-shell probability={max(np.max(results[(fine,k)]["outer"]) for k in ("off","linked","unlinked","spherical")):.6g}',f'worst relative domain gap drift={rel_domain:.6g}',f'max linked-vs-off gap shift={max_effect:.6g}',f'3sigma topology-specific modes={sig_modes.tolist()}']
    for name,bv in [('B1 topology controls certified',B1),('B2 bound-state boundary leakage',B2),('B3 domain-converged excitation gaps',B3),('B4 rope perturbation measurable',B4),('B5 linked-unlinked contrast exceeds numerical uncertainty',B5),('B6 topology contrast stable across domains',B6)]: lines.append(name+': '+('PASS' if bv else 'FAIL'))
    lines.append('FINDING: '+finding)
    text='\n'.join(lines); print(text)
    (ROOT/'analysis'/'ROPE_MODE004_run.log').write_text(text+'\n')
    np.savez(ROOT/'analysis'/'ROPE_MODE004_summary.npz',boxes=np.array(BOXES),alpha=ALPHA,eps=EPS,beta=BETA,sigma=SIGMA,dmin=d,lk=lk,lku=lku,topology_contrast=topo,uncertainty=uncertainty,significant=significant)
    return finding

if __name__=='__main__': run()
