"""ROPE-MODE-002: central-field standing-wave gate on certified linked rope.

This benchmark tests the smallest honest extension of ROPE-MODE-001: a scalar
wave living on each closed rope component is coupled to a softened central
attraction.  The geometry, topology certificate, and rope Laplacian are kept
fixed.  No atomic-spectrum fitting is performed.

Because this is a field-on-curve test rather than a full nonlinear atom solver,
its conclusion is limited: it asks whether a central field alone reorganizes
ordinary 1-D harmonics into robust s/p/d-like multiplets.
"""
from pathlib import Path
import csv, sys
import numpy as np
from scipy.linalg import eigh
from scipy.special import sph_harm_y

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from benchmarks.foundations.electron_variational_remesh import Model

LEVELS=(128,256,512)
ALPHAS=(0.0,0.1,0.3,1.0,3.0,10.0)
EPS_FRAC=0.15
N_EIG=18
CONV_TOL=0.01
DEG_TOL=0.02
ROBUST_FRAC=0.80


def assemble(curve, alpha, eps):
    x=np.asarray(curve,float); n=len(x)
    ell=np.linalg.norm(np.roll(x,-1,axis=0)-x,axis=1)
    K=np.zeros((n,n)); M=np.zeros((n,n)); V=np.zeros((n,n))
    pot=-alpha/np.sqrt(np.sum(x*x,axis=1)+eps*eps)
    for i,h in enumerate(ell):
        j=(i+1)%n
        ke=np.array([[1.,-1.],[-1.,1.]])/h
        me=h*np.array([[2.,1.],[1.,2.]])/6.
        # linearly interpolated nodal potential, mass-lumped locally for stability
        ve=0.5*(pot[i]+pot[j])*me
        ix=np.ix_([i,j],[i,j]); K[ix]+=ke; M[ix]+=me; V[ix]+=ve
    H=K+V
    vals,vecs=eigh(H,M,subset_by_index=[0,min(n-1,N_EIG-1)])
    return vals,vecs,M,ell.sum(),pot


def real_sph_basis(curve,lmax=2):
    x=np.asarray(curve,float); r=np.linalg.norm(x,axis=1)
    theta=np.arccos(np.clip(x[:,2]/np.maximum(r,1e-15),-1,1))
    phi=np.arctan2(x[:,1],x[:,0])%(2*np.pi)
    blocks=[]
    for l in range(lmax+1):
        cols=[]
        for m in range(-l,l+1):
            y=sph_harm_y(l,m,theta,phi)
            if m<0: col=np.sqrt(2)*(-1)**m*y.imag
            elif m==0: col=y.real
            else: col=np.sqrt(2)*(-1)**m*y.real
            cols.append(np.asarray(col,float))
        blocks.append(np.column_stack(cols))
    return blocks


def projection_scores(vecs,M,blocks):
    scores=np.zeros((vecs.shape[1],len(blocks)))
    for l,B in enumerate(blocks):
        G=B.T@M@B
        Gi=np.linalg.pinv(G,rcond=1e-10)
        for k in range(vecs.shape[1]):
            v=vecs[:,k]; den=float(v.T@M@v)
            c=B.T@M@v
            scores[k,l]=float(c.T@Gi@c/max(den,1e-15))
    return scores


def clusters(vals,tol=DEG_TOL):
    vals=np.asarray(vals)
    out=[]; cur=[0]
    for i in range(1,len(vals)):
        scale=max(abs(vals[i]),abs(vals[i-1]),1.0)
        if abs(vals[i]-vals[i-1])/scale < tol: cur.append(i)
        else: out.append(cur); cur=[i]
    out.append(cur); return out


def run():
    state=np.load(ROOT/'analysis'/'ELEC009_state.npz')
    z=state['z_final']; knots=state['knots_final']
    model=Model(20,knots=knots,m_energy=64)
    d,lk,cert,certvals=model.cert(z)
    radii=[]
    for c in model.curves(z,512): radii.extend(np.linalg.norm(c,axis=1))
    eps=EPS_FRAC*float(np.median(radii))

    rows=[]; summaries=[]; mesh_cache={}
    for Mlev in LEVELS:
        mesh_cache[Mlev]=model.curves(z,Mlev)
    for alpha in ALPHAS:
        per=[]
        for Mlev in LEVELS:
            strand_data=[]
            for s,c in enumerate(mesh_cache[Mlev]):
                vals,vecs,Mass,L,pot=assemble(c,alpha,eps)
                scores=projection_scores(vecs,Mass,real_sph_basis(c,2))
                dom=np.argmax(scores,axis=1)
                strand_data.append((vals,scores,dom))
                for k,v in enumerate(vals):
                    rows.append((alpha,Mlev,s,k,v,dom[k],scores[k,0],scores[k,1],scores[k,2],L,float(pot.min()),float(pot.max())))
            if Mlev==512: per=strand_data
        # convergence 256->512
        conv=[]
        for s in range(2):
            v256=assemble(mesh_cache[256][s],alpha,eps)[0]
            v512=per[s][0]
            conv.extend(np.abs(v512-v256)/np.maximum(np.abs(v512),1.0))
        maxconv=float(np.max(conv))
        # pooled first 9 levels after each strand ground state; inspect cluster sizes
        cs=[]; labels=[]; purities=[]
        for s,(vals,scores,dom) in enumerate(per):
            cset=clusters(vals[:9])
            cs.append([len(q) for q in cset])
            labels.append(dom[:9].tolist())
            purities.append(np.max(scores[:9],axis=1).tolist())
        # Exact atomic spatial target is 1,3,5 for s,p,d. Require on both strands.
        mult_ok=all(x[:3]==[1,3,5] for x in cs)
        class_ok=all(lab[:9]==[0]+[1]*3+[2]*5 for lab in labels)
        pure_ok=all(np.mean(np.asarray(p)>=0.5)>=ROBUST_FRAC for p in purities)
        summaries.append((alpha,maxconv,cs,labels,purities,mult_ok,class_ok,pure_ok))

    B1=bool(cert and d>=0.060 and abs(abs(lk)-1)<=0.03)
    B2=max(s[1] for s in summaries)<CONV_TOL
    central=[s for s in summaries if s[0]>0]
    B3=any(s[5] for s in central)
    B4=any(s[6] and s[7] for s in central)
    B5=False
    # robustness means same successful multiplet/classification across >=3 adjacent nonzero alphas
    for i in range(len(central)-2):
        grp=central[i:i+3]
        if all(s[5] and s[6] and s[7] for s in grp): B5=True
    finding='CENTRAL_FIELD_GENERATES_ROBUST_ORBITAL_MULTIPLETS' if all((B1,B2,B3,B4,B5)) else 'CENTRAL_FIELD_DOES_NOT_GENERATE_ATOMIC_MULTIPLETS'

    with open(ROOT/'analysis'/'ROPE_MODE002_spectrum.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['alpha','samples','strand','mode','eigenvalue','dominant_l','score_l0','score_l1','score_l2','length','potential_min','potential_max']); w.writerows(rows)
    out=['ROPE-MODE-002 central-field spectrum',f'certified={cert} dmin={d:.8f} Lk512={lk:.8f} eps={eps:.8f}']
    for alpha,maxconv,cs,labels,purities,mult_ok,class_ok,pure_ok in summaries:
        out.append(f'alpha={alpha:g} maxconv={maxconv:.6g} clusters={cs} dominant_l={labels} mean_purity={[round(float(np.mean(p)),4) for p in purities]} multiplet={mult_ok} class={class_ok} purity={pure_ok}')
    for name,b in [('B1 certified linked reference',B1),('B2 mesh-converged central-field spectrum',B2),('B3 1/3/5 multiplets emerge',B3),('B4 multiplets classify as s/p/d',B4),('B5 structure robust across coupling sweep',B5)]: out.append(name+': '+('PASS' if b else 'FAIL'))
    out.append('FINDING: '+finding)
    text='\n'.join(out); print(text)
    (ROOT/'analysis'/'ROPE_MODE002_run.log').write_text(text+'\n')
    np.savez(ROOT/'analysis'/'ROPE_MODE002_summary.npz',alphas=np.array(ALPHAS),eps=eps,dmin=d,lk=lk)
    return finding,summaries

if __name__=='__main__': run()
