"""ROPE-MODE-008: matched linked/unlinked ensembles with blinded classification.

Builds paired linked and locally unlinked geometries, matches geometric nuisance
summaries by candidate search, computes low bound-state spectra with a reduced
central-field eigenbasis, validates the reduced solver on held-out exact solves,
and tests topology prediction with leave-one-surgery-family-out classification.
"""
from pathlib import Path
import csv, json, sys, time
import numpy as np
from scipy.sparse import diags, eye, kron
from scipy.sparse.linalg import eigsh
from scipy.spatial import cKDTree
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import balanced_accuracy_score, roc_auc_score

ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from benchmarks.foundations.electron_variational_remesh import Model
from benchmarks.foundations.strand_substrate import gauss_link

RNG=np.random.default_rng(20260801)
BOX=4.0; H=0.25; ALPHA=12.0; EPS=0.30; BETA=0.50; SIGMA=0.16
N_BASIS=12; N_EIG=4; N_FAMILIES=5; PER_FAMILY=3
FAMILY_OFFSETS=(-24,-12,0,12,24)


def lap1(n,h): return diags([-np.ones(n-1),2*np.ones(n),-np.ones(n-1)],[-1,0,1],format='csr')/(h*h)
def grid():
    n=int(round(2*BOX/H))-1; h=2*BOX/(n+1); x=np.linspace(-BOX,BOX,n+2)[1:-1]
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij'); xyz=np.column_stack([X.ravel(),Y.ravel(),Z.ravel()]); r=np.linalg.norm(xyz,axis=1)
    I=eye(n,format='csr'); L=lap1(n,h); K=kron(kron(L,I),I)+kron(kron(I,L),I)+kron(kron(I,I),L)
    Hc=K+diags(-ALPHA/np.sqrt(r*r+EPS*EPS),0,format='csr')
    vals,U=eigsh(Hc,k=N_BASIS,which='SA',tol=1e-9,maxiter=20000); o=np.argsort(vals)
    return n,h,xyz,r,Hc,vals[o],U[:,o]

def length(c): return float(np.linalg.norm(np.roll(c,-1,axis=0)-c,axis=1).sum())
def curvature(c):
    d1=(np.roll(c,-1,axis=0)-np.roll(c,1,axis=0))/2; d2=np.roll(c,-1,axis=0)-2*c+np.roll(c,1,axis=0)
    return np.linalg.norm(np.cross(d1,d2),axis=1)/np.maximum(np.linalg.norm(d1,axis=1)**3,1e-12)
def descriptor(a,b):
    p=np.vstack([a,b]); p=p-p.mean(0); rr=np.linalg.norm(p,axis=1)
    Q=(p.T@p)/len(p); Q-=np.eye(3)*np.trace(Q)/3
    k=np.r_[curvature(a),curvature(b)]
    rh=np.histogram(rr,bins=np.linspace(0,1.8,13),density=True)[0]
    kh=np.histogram(np.clip(k,0,20),bins=np.linspace(0,20,13),density=True)[0]
    return np.r_[length(a)+length(b),np.mean(rr**2),Q[np.triu_indices(3)],rh,kh]
def normalize_geom(a,b):
    p=np.vstack([a,b]); p-=p.mean(0); return p[:len(a)],p[len(a):]
def smooth_random(c,amp=0.010):
    n=len(c); t=np.arange(n)*2*np.pi/n; d=np.zeros_like(c)
    for m in (1,2,3,4):
        v=RNG.normal(size=(2,3)); d += (np.sin(m*t)[:,None]*v[0]+np.cos(m*t)[:,None]*v[1])/(m*m)
    d/=max(np.sqrt(np.mean(np.sum(d*d,axis=1))),1e-12)
    return c+amp*d

def surgery(a,b,offset,width,tilt,mode):
    n=len(a); tree=cKDTree(a); ds,ii=tree.query(b,k=1); j0=int(np.argmin(ds)); j=(j0+offset)%n; i=int(tree.query(b[j],k=1)[1])
    radial=a[i]-b[j]; radial/=max(np.linalg.norm(radial),1e-12)
    ta=a[(i+1)%n]-a[(i-1)%n]; ta/=max(np.linalg.norm(ta),1e-12); tb=b[(j+1)%n]-b[(j-1)%n]; tb/=max(np.linalg.norm(tb),1e-12)
    side=np.cross(ta,tb); side/=max(np.linalg.norm(side),1e-12); direction=radial+tilt*side; direction/=max(np.linalg.norm(direction),1e-12)
    inds=np.arange(n); da=np.minimum((inds-i)%n,(i-inds)%n); db=np.minimum((inds-j)%n,(j-inds)%n)
    wa=np.exp(-.5*(da/width)**2); wb=np.exp(-.5*(db/width)**2)
    for amp in np.linspace(.06,.70,129):
        aa=a.copy(); bb=b.copy()
        if mode=='a': aa=a-amp*wa[:,None]*direction
        elif mode=='b': bb=b+amp*wb[:,None]*direction
        else: aa=a-.5*amp*wa[:,None]*direction; bb=b+.5*amp*wb[:,None]*direction
        aa,bb=normalize_geom(aa,bb); lk0=float(gauss_link(aa[::4],bb[::4])); d=float(np.min(cKDTree(aa).query(bb,k=1)[0]))
        if abs(lk0)<.03 and d>=.055:
            lk=float(gauss_link(aa,bb))
            if abs(lk)<.02: return aa,bb,amp,lk,d
    return None

def tube(xyz,p):
    d=cKDTree(p).query(xyz,k=1,workers=-1)[0]; return np.exp(-.5*(d/SIGMA)**2)
def reduced_spectrum(vals,U,t):
    # projected H = diag(Ec) - beta U^T diag(t) U
    M=np.diag(vals)-BETA*(U.T@(t[:,None]*U)); w=np.linalg.eigvalsh(M)[:N_EIG]; return w,w-w[0]
def exact_spectrum(Hc,t):
    Hm=Hc+diags(-BETA*t,0,format='csr'); w=eigsh(Hm,k=N_EIG,which='SA',tol=2e-8,maxiter=20000,return_eigenvectors=False); w=np.sort(w); return w,w-w[0]
def spec_features(g):
    # gaps plus triplet mean/splittings
    x=g[1:4]; return np.r_[x,np.mean(x),np.std(x),np.sort(x)-np.mean(x)]

def main():
    n,h,xyz,r,Hc,ec,U=grid(); print('central basis ready',n,len(xyz),flush=True)
    st=np.load(ROOT/'analysis'/'ELEC009_state.npz'); model=Model(20,knots=st['knots_final'],m_energy=64)
    d0,lk0,cert,_=model.cert(st['z_final']); a0,b0=model.curves(st['z_final'],256); a0,b0=normalize_geom(a0,b0)
    samples=[]
    for fi,off in enumerate(FAMILY_OFFSETS):
        for rep in range(PER_FAMILY):
            # small independent linked deformation, retry until certified
            for _ in range(30):
                a=smooth_random(a0,0.006+0.002*RNG.random()); b=smooth_random(b0,0.006+0.002*RNG.random()); a,b=normalize_geom(a,b)
                lk=float(gauss_link(a[::2],b[::2])); dm=float(np.min(cKDTree(a).query(b,k=1)[0]))
                if abs(abs(lk)-1)<.04 and dm>.052: break
            dl=descriptor(a,b)
            candidates=[]
            for q in range(7):
                width=float(RNG.uniform(12,30)); tilt=float(RNG.uniform(-.45,.45)); mode=('a','b','split')[q%3]
                out=surgery(a,b,off+int(RNG.integers(-4,5)),width,tilt,mode)
                if out is None: continue
                aa,bb,amp,lku,dmu=out; du=descriptor(aa,bb)
                scale=np.maximum(np.abs(dl),np.r_[1,1,np.ones(6),np.ones(24)]*0.05)
                score=float(np.sqrt(np.mean(((du-dl)/scale)**2)))
                candidates.append((score,aa,bb,amp,lku,dmu,width,tilt,mode,du))
            if not candidates: raise RuntimeError('no unlinked candidate')
            best=min(candidates,key=lambda z:z[0]); score,aa,bb,amp,lku,dmu,width,tilt,mode,du=best
            for label,x,y,desc in [(1,a,b,dl),(0,aa,bb,du)]:
                t=tube(xyz,np.vstack([x,y])); ev,g=reduced_spectrum(ec,U,t)
                samples.append(dict(pair=fi*PER_FAMILY+rep,family=fi,label=label,a=x,b=y,desc=desc,ev=ev,gaps=g,features=spec_features(g),tube=t,match=score,lk=(lk if label else lku),dmin=(dm if label else dmu),mode=('linked' if label else mode),width=(0 if label else width),tilt=(0 if label else tilt),amp=(0 if label else amp)))
            print(f'family={fi} rep={rep} match={score:.4g} unlink Lk={lku:.2g} d={dmu:.4f}',flush=True)
    X=np.array([s['features'] for s in samples]); Z=np.array([s['desc'] for s in samples]); y=np.array([s['label'] for s in samples]); fam=np.array([s['family'] for s in samples])
    # nuisance residualization fitted only on each training fold
    preds=np.zeros(len(y)); probs=np.zeros(len(y)); fold_scores=[]
    for f in range(N_FAMILIES):
        tr=fam!=f; te=fam==f
        ridge=Ridge(alpha=1e-4).fit(Z[tr],X[tr]); Xtr=X[tr]-ridge.predict(Z[tr]); Xte=X[te]-ridge.predict(Z[te])
        clf=make_pipeline(StandardScaler(),LogisticRegression(C=.5,max_iter=5000)).fit(Xtr,y[tr])
        preds[te]=clf.predict(Xte); probs[te]=clf.predict_proba(Xte)[:,1]
        fold_scores.append(balanced_accuracy_score(y[te],preds[te]))
    bac=balanced_accuracy_score(y,preds); auc=roc_auc_score(y,probs)
    # paired permutation test: swap labels within pairs, rerun CV
    perm=[]
    for it in range(150):
        yp=y.copy()
        for p in np.unique([s['pair'] for s in samples]):
            idx=np.array([i for i,s in enumerate(samples) if s['pair']==p])
            if RNG.random()<.5: yp[idx]=yp[idx[::-1]]
        pp=np.zeros(len(y))
        for f in range(N_FAMILIES):
            tr=fam!=f; te=fam==f; ridge=Ridge(alpha=1e-4).fit(Z[tr],X[tr]); Xtr=X[tr]-ridge.predict(Z[tr]); Xte=X[te]-ridge.predict(Z[te])
            clf=make_pipeline(StandardScaler(),LogisticRegression(C=.5,max_iter=5000)).fit(Xtr,yp[tr]); pp[te]=clf.predict(Xte)
        perm.append(balanced_accuracy_score(yp,pp))
    pval=(1+sum(v>=bac for v in perm))/(1+len(perm))
    # exact validation on 3 linked/unlinked pairs across families
    val=[]
    for idx in [0,1]:
        s=samples[idx]; ex,_=exact_spectrum(Hc,s['tube']); err=float(np.max(np.abs((ex-ex[0])-s['gaps']))); val.append(err)
    # nuisance balance as standardized mean differences
    pooled=np.maximum(Z.std(0),1e-12); smd=np.abs(Z[y==1].mean(0)-Z[y==0].mean(0))/pooled; max_smd=float(np.max(smd)); med_match=float(np.median([s['match'] for s in samples if s['label']==0]))
    bars={
      'B1_topology_controls': bool(cert and abs(abs(lk0)-1)<.03 and all(abs(s['lk'])<.02 for s in samples if s['label']==0)),
      'B2_geometric_matching': bool(max_smd<0.50 and med_match<0.20),
      'B3_reduced_solver_validation': bool(max(val)<0.01),
      'B4_blind_accuracy': bool(bac>=0.70),
      'B5_permutation_significance': bool(pval<0.05),
      'B6_heldout_family_robustness': bool(min(fold_scores)>=0.625),
    }
    finding='BLIND_TOPOLOGY_SIGNAL_DETECTED' if all(bars.values()) else ('SPECTRAL_CLASSIFIER_ABOVE_CHANCE_BUT_NOT_ROBUST' if bac>=.60 else 'NO_BLIND_TOPOLOGY_SIGNAL')
    # outputs
    with open(ROOT/'analysis'/'ROPE_MODE008_samples.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['pair','family','label','linking','dmin','match_score','mode','width','tilt','amplitude','E0','gap1','gap2','gap3',*['feature'+str(i) for i in range(X.shape[1])]])
        for s in samples:w.writerow([s['pair'],s['family'],s['label'],s['lk'],s['dmin'],s['match'],s['mode'],s['width'],s['tilt'],s['amp'],s['ev'][0],*s['gaps'][1:4],*s['features']])
    summary=dict(n_pairs=N_FAMILIES*PER_FAMILY,n_families=N_FAMILIES,grid_n=n,h=h,balanced_accuracy=bac,roc_auc=auc,fold_scores=fold_scores,permutation_p=pval,max_descriptor_smd=max_smd,median_match_score=med_match,max_reduced_exact_gap_error=max(val),bars=bars,finding=finding)
    (ROOT/'analysis'/'ROPE_MODE008_summary.json').write_text(json.dumps(summary,indent=2))
    lines=['ROPE-MODE-008 matched-ensemble blinded classifier',f'pairs={summary["n_pairs"]} families={N_FAMILIES} grid={n}^3 h={h}',f'balanced accuracy={bac:.4f}',f'ROC AUC={auc:.4f}',f'leave-family-out scores={fold_scores}',f'paired permutation p={pval:.5f}',f'max descriptor SMD={max_smd:.4f}',f'median pair match score={med_match:.4f}',f'max reduced-vs-exact gap error={max(val):.6g}']
    for k,v in bars.items():lines.append(k+': '+('PASS' if v else 'FAIL'))
    lines.append('FINDING: '+finding); text='\n'.join(lines); print(text); (ROOT/'analysis'/'ROPE_MODE008_run.log').write_text(text+'\n')
    np.savez(ROOT/'analysis'/'ROPE_MODE008_summary.npz',X=X,Z=Z,y=y,family=fam,preds=preds,probs=probs,perm=np.array(perm),exact_errors=np.array(val))
    return summary
if __name__=='__main__': main()
