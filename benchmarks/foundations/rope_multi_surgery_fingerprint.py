"""ROPE-MODE-007: repeated independent local topology surgeries.

Tests whether the low-bound-state spectral contrast tracks linked/unlinked status
across surgery location, moved strand, displacement split, width, and direction.
"""
from pathlib import Path
import csv, sys, time, json
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
# offset and width are in units of the 1024-point periodic parameter grid.
SPECS=(
    dict(name='center_B_narrow', offset=0, width=50, mode='b', tilt=0.0),
    dict(name='center_A_wide_tilt', offset=0, width=110, mode='a', tilt=0.25),
    dict(name='center_split_mid_tilt', offset=0, width=80, mode='split', tilt=-0.25),
    dict(name='left_split_narrow', offset=-48, width=50, mode='split', tilt=-0.25),
    dict(name='right_split_mid', offset=48, width=80, mode='split', tilt=0.0),
    dict(name='far_right_split_narrow', offset=96, width=50, mode='split', tilt=-0.25),
)

def lap1(n,h):
    return diags([-np.ones(n-1),2*np.ones(n),-np.ones(n-1)],[-1,0,1],format='csr')/(h*h)

def grid_for_box(box):
    n=int(round(2*box/H_TARGET))-1; h=2*box/(n+1)
    x=np.linspace(-box,box,n+2)[1:-1]
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    xyz=np.column_stack([X.ravel(),Y.ravel(),Z.ravel()])
    I=eye(n,format='csr'); L=lap1(n,h)
    H0=kron(kron(L,I),I)+kron(kron(I,L),I)+kron(kron(I,I),L)
    r=np.linalg.norm(xyz,axis=1)
    return n,h,xyz,H0,r

def polygon_length(c):
    return float(np.sum(np.linalg.norm(np.roll(c,-1,axis=0)-c,axis=1)))

def geom_moments(pts):
    p=pts-pts.mean(0); r2=float(np.mean(np.sum(p*p,axis=1)))
    Q=(p.T@p)/len(p); Q-=np.eye(3)*np.trace(Q)/3
    return r2,Q

def local_curvature(c):
    d1=(np.roll(c,-1,axis=0)-np.roll(c,1,axis=0))/2
    d2=np.roll(c,-1,axis=0)-2*c+np.roll(c,1,axis=0)
    cross=np.linalg.norm(np.cross(d1,d2),axis=1)
    return cross/np.maximum(np.linalg.norm(d1,axis=1)**3,1e-12)

def build_surgery(a,b,spec):
    n=len(a); tree=cKDTree(a); ds,ii=tree.query(b,k=1); j0=int(np.argmin(ds))
    j=(j0+int(spec['offset']))%n; i=int(tree.query(b[j],k=1)[1])
    radial=a[i]-b[j]; radial/=np.linalg.norm(radial)
    tb=b[(j+1)%n]-b[(j-1)%n]; tb/=np.linalg.norm(tb)
    ta=a[(i+1)%n]-a[(i-1)%n]; ta/=np.linalg.norm(ta)
    side=np.cross(ta,tb); side/=max(np.linalg.norm(side),1e-12)
    direction=radial+float(spec['tilt'])*side; direction/=np.linalg.norm(direction)
    inds=np.arange(n)
    db=np.minimum((inds-j)%n,(j-inds)%n); wb=np.exp(-.5*(db/float(spec['width']))**2)
    da=np.minimum((inds-i)%n,(i-inds)%n); wa=np.exp(-.5*(da/float(spec['width']))**2)
    best=None
    # Search past the topology-changing crossing until separation recovers.
    for amp in np.linspace(0.07,0.65,117):
        aa=a.copy(); bb=b.copy()
        if spec['mode']=='b': bb=b+amp*wb[:,None]*direction
        elif spec['mode']=='a': aa=a-amp*wa[:,None]*direction
        else:
            aa=a-.5*amp*wa[:,None]*direction; bb=b+.5*amp*wb[:,None]*direction
        pp=np.vstack([aa,bb]); pp-=pp.mean(0); aa=pp[:n]; bb=pp[n:]
        lk_fast=float(gauss_link(aa[::4],bb[::4]))
        d=float(np.min(cKDTree(aa).query(bb,k=1)[0]))
        if abs(lk_fast)<.03 and d>=.060:
            lk=float(gauss_link(aa,bb))
            if abs(lk)<.02:
                best=(aa,bb,float(amp),lk,d,i,j,direction)
                break
    if best is None: raise RuntimeError('surgery failed: '+spec['name'])
    return best

def tube(xyz,pts):
    d=cKDTree(pts).query(xyz,k=1,workers=-1)[0]
    return np.exp(-0.5*(d/SIGMA)**2)

def solve(grid,kind,pts):
    n,h,xyz,H0,r=grid
    t=np.zeros_like(r) if kind=='off' else tube(xyz,pts)
    V=-ALPHA/np.sqrt(r*r+EPS*EPS)-BETA*t
    H=H0+diags(V,0,format='csr'); t0=time.time()
    vals,vecs=eigsh(H,k=N_EIG,which='SA',tol=5e-9,maxiter=15000)
    order=np.argsort(vals); vals=vals[order]; vecs=vecs[:,order]
    prob=vecs*vecs; norm=np.maximum(prob.sum(axis=0),1e-15)
    outer=prob[r>(grid[0]*0 + (xyz[:,0].max()+h)-OUTER_SHELL)].sum(axis=0)/norm
    return dict(vals=vals,gaps=vals-vals[0],outer=outer,elapsed=time.time()-t0,n=n,h=h)

def run():
    st=np.load(ROOT/'analysis'/'ELEC009_state.npz'); model=Model(20,knots=st['knots_final'],m_energy=64)
    d,lk,cert,_=model.cert(st['z_final']); a,b=model.curves(st['z_final'],1024)
    linked=np.vstack([a,b]); linked-=linked.mean(0); a=linked[:len(a)]; b=linked[len(a):]
    L0=polygon_length(a)+polygon_length(b); r20,Q0=geom_moments(linked)
    ka0,kb0=local_curvature(a),local_curvature(b)
    surgeries=[]
    for spec in SPECS:
        aa,bb,amp,lku,du,i,j,direction=build_surgery(a,b,spec); pts=np.vstack([aa,bb])
        rms=float(np.sqrt(np.mean(np.sum((pts-linked)**2,axis=1))))
        L1=polygon_length(aa)+polygon_length(bb); r21,Q1=geom_moments(pts)
        lrel=abs(L1-L0)/L0; r2rel=abs(r21-r20)/r20; qrel=np.linalg.norm(Q1-Q0)/max(np.linalg.norm(Q0),1e-15)
        ka1,kb1=local_curvature(aa),local_curvature(bb)
        # local curvature change around the actual surgery centres
        win=80; inds=np.arange(len(a)); ma=np.minimum((inds-i)%len(a),(i-inds)%len(a))<win; mb=np.minimum((inds-j)%len(a),(j-inds)%len(a))<win
        curv=float(np.sqrt(np.mean((ka1[ma]-ka0[ma])**2)+np.mean((kb1[mb]-kb0[mb])**2)))
        surgeries.append(dict(spec=spec,aa=aa,bb=bb,pts=pts,amp=amp,lk=lku,dmin=du,rms=rms,length_rel=lrel,r2_rel=r2rel,q_rel=qrel,curv_change=curv,i=i,j=j))
        print(f"{spec['name']}: amp={amp:.4f} Lk={lku:.3g} d={du:.6f} rms={rms:.5f} Lrel={lrel:.4g} Qrel={qrel:.4g} dK={curv:.4g}",flush=True)

    grids={box:grid_for_box(box) for box in BOXES}; results={}; rows=[]
    for box in BOXES:
        q=solve(grids[box],'off',None); results[(box,'off')]=q
        q=solve(grids[box],'linked',linked); results[(box,'linked')]=q
        print(f"box={box:g} off/linked complete",flush=True)
        for s in surgeries:
            q=solve(grids[box],s['spec']['name'],s['pts']); results[(box,s['spec']['name'])]=q
            print(f"box={box:g} {s['spec']['name']} E0={q['vals'][0]:.8f} outer={np.max(q['outer']):.2g} t={q['elapsed']:.1f}s",flush=True)
        for name in ['off','linked']+[s['spec']['name'] for s in surgeries]:
            q=results[(box,name)]
            for k in range(N_EIG): rows.append([box,q['n'],q['h'],name,k,q['vals'][k],q['gaps'][k],q['outer'][k]])

    coarse,fine=BOXES; gl=results[(fine,'linked')]['gaps']
    contrasts=[]
    for s in surgeries:
        name=s['spec']['name']; gs=results[(fine,name)]['gaps']; topo=gl-gs
        dl=np.abs(results[(fine,'linked')]['gaps']-results[(coarse,'linked')]['gaps'])
        ds=np.abs(results[(fine,name)]['gaps']-results[(coarse,name)]['gaps']); unc=dl+ds
        tc=results[(coarse,'linked')]['gaps']-results[(coarse,name)]['gaps']
        sig=np.abs(topo)>3*np.maximum(unc,1e-6)
        stable=np.array([np.sign(tc[k])==np.sign(topo[k]) and abs(tc[k]-topo[k])<max(.5*abs(topo[k]),1e-5) for k in range(N_EIG)])
        contrasts.append((s,topo,unc,tc,sig,stable))

    C=np.array([x[1][1:] for x in contrasts])
    signs=np.sign(C); majority=[]
    for m in range(3):
        nz=signs[:,m]; majority.append(int(max(np.sum(nz>0),np.sum(nz<0))))
    sig_counts=[int(sum(x[4][m] for x in contrasts)) for m in range(1,4)]
    stable_counts=[int(sum(x[5][m] for x in contrasts)) for m in range(1,4)]
    # Correlations quantify whether magnitude is dominated by nuisance geometry metrics.
    metrics=np.array([[x[0]['rms'],x[0]['length_rel'],x[0]['r2_rel'],x[0]['q_rel'],x[0]['curv_change'],abs(x[0]['spec']['offset']),x[0]['spec']['tilt']] for x in contrasts])
    corrs=np.zeros((metrics.shape[1],3))
    for j in range(metrics.shape[1]):
        for m in range(3):
            corrs[j,m]=np.corrcoef(metrics[:,j],C[:,m])[0,1] if np.std(metrics[:,j])>0 and np.std(C[:,m])>0 else 0

    max_outer=max(np.max(results[(fine,name)]['outer']) for name in ['off','linked']+[s['spec']['name'] for s in surgeries])
    max_rel_drift=0
    for name in ['off','linked']+[s['spec']['name'] for s in surgeries]:
        drift=np.abs(results[(fine,name)]['gaps'][1:]-results[(coarse,name)]['gaps'][1:])/np.maximum(abs(results[(fine,name)]['gaps'][1:]),.25)
        max_rel_drift=max(max_rel_drift,float(np.max(drift)))
    geometry_pass=all(s['rms']<.09 and s['length_rel']<.02 and s['r2_rel']<.03 and s['q_rel']<.10 and abs(s['lk'])<.02 and s['dmin']>=.060 for s in surgeries)
    B1=bool(cert and abs(abs(lk)-1)<.03 and geometry_pass)
    B2=max_outer<.001; B3=max_rel_drift<.01
    B4=all(c==len(surgeries) for c in majority)
    B5=all(c>=5 for c in sig_counts)
    B6=all(c>=5 for c in stable_counts)
    # With only six surgeries, correlations above 0.70 are too large to claim
    # independence from nuisance geometry. This is deliberately conservative.
    B7=float(np.max(np.abs(corrs)))<.70
    finding='LINKING_NUMBER_TRACKING_ISOLATED' if all((B1,B2,B3,B4,B5,B6,B7)) else 'REPEATED_SURGERIES_DO_NOT_ISOLATE_LINKING_NUMBER'

    with open(ROOT/'analysis'/'ROPE_MODE007_spectrum.csv','w',newline='') as f:
        w=csv.writer(f);w.writerow(['box','grid_n','h','control','mode','eigenvalue','excitation_gap','outer_shell_probability']);w.writerows(rows)
    with open(ROOT/'analysis'/'ROPE_MODE007_surgeries.csv','w',newline='') as f:
        w=csv.writer(f);w.writerow(['name','offset','width','mode','tilt','amplitude','linking','dmin','rms','length_rel','r2_rel','quadrupole_rel','local_curvature_change'])
        for s in surgeries:
            z=s['spec'];w.writerow([z['name'],z['offset'],z['width'],z['mode'],z['tilt'],s['amp'],s['lk'],s['dmin'],s['rms'],s['length_rel'],s['r2_rel'],s['q_rel'],s['curv_change']])
    with open(ROOT/'analysis'/'ROPE_MODE007_contrasts.csv','w',newline='') as f:
        w=csv.writer(f);w.writerow(['surgery','mode','linked_minus_unlinked','combined_domain_uncertainty','significant_3sigma','coarse_contrast','domain_stable'])
        for s,c,u,tc,sg,stb in contrasts:
            for k in range(N_EIG): w.writerow([s['spec']['name'],k,c[k],u[k],bool(sg[k]),tc[k],bool(stb[k])])
    with open(ROOT/'analysis'/'ROPE_MODE007_correlations.csv','w',newline='') as f:
        w=csv.writer(f);w.writerow(['metric','mode1_r','mode2_r','mode3_r'])
        for name,row in zip(['rms','length_rel','r2_rel','quadrupole_rel','curvature_change','abs_offset','tilt'],corrs):w.writerow([name,*row])

    lines=['ROPE-MODE-007 repeated independent local surgeries',f'linked certified={cert} dmin={d:.8f} Lk={lk:.8f}',f'surgeries={len(surgeries)} boxes={BOXES} h={H_TARGET}',f'max outer probability={max_outer:.8g}',f'worst relative gap drift={max_rel_drift:.8g}',f'majority same-sign counts modes1-3={majority}',f'3sigma counts modes1-3={sig_counts}',f'domain-stable counts modes1-3={stable_counts}',f'max absolute nuisance correlation={float(np.max(np.abs(corrs))):.6g}']
    for nm,v in [('B1 topology and geometry controls',B1),('B2 boundary leakage',B2),('B3 domain convergence',B3),('B4 universal sign consistency',B4),('B5 significance consistency',B5),('B6 domain stability',B6),('B7 weak nuisance correlations',B7)]:lines.append(nm+': '+('PASS' if v else 'FAIL'))
    lines.append('FINDING: '+finding);text='\n'.join(lines);print(text)
    (ROOT/'analysis'/'ROPE_MODE007_run.log').write_text(text+'\n')
    np.savez(ROOT/'analysis'/'ROPE_MODE007_summary.npz',contrasts=C,metrics=metrics,correlations=corrs,majority=np.array(majority),sig_counts=np.array(sig_counts),stable_counts=np.array(stable_counts),max_outer=max_outer,max_rel_drift=max_rel_drift)
    return finding

if __name__=='__main__':run()
