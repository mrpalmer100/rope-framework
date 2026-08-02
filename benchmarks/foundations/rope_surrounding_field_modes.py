"""ROPE-MODE-003: 3-D scalar field modes around a certified linked rope.

The linked rope is held fixed and enters as an embedded tubular potential in a
three-dimensional scalar eigenproblem. A softened central attraction is kept so
that bound states exist. The benchmark asks whether the surrounding field—not
a field confined to the curve—has converged, localized modes with recognizable
angular families, and whether those families survive a modest rope coupling.

This is a numerical structural gate, not a derivation of atomic spectroscopy.
"""
from pathlib import Path
import csv, sys
import numpy as np
from scipy.sparse import diags, eye, kron
from scipy.sparse.linalg import eigsh
from scipy.spatial import cKDTree
from scipy.special import sph_harm_y

ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from benchmarks.foundations.electron_variational_remesh import Model

LEVELS=(23,29)
BETAS=(0.0,0.25,0.5,1.0)
ALPHA=2.0
BOX=3.0
EPS=0.12
SIGMA=0.10
N_EIG=18
CONV_TOL=0.08
LOC_TOL=0.85
PURITY_TOL=0.55


def real_ylm(l,m,theta,phi):
    y=sph_harm_y(l,m,theta,phi)
    if m<0: return np.sqrt(2)*(-1)**m*y.imag
    if m==0: return y.real
    return np.sqrt(2)*(-1)**m*y.real


def lap1(n,h):
    return diags([-np.ones(n-1),2*np.ones(n),-np.ones(n-1)],[-1,0,1],format='csr')/(h*h)


def angular_scores(vecs,xyz,lmax=3,nrad=7):
    r=np.linalg.norm(xyz,axis=1)
    theta=np.arccos(np.clip(xyz[:,2]/np.maximum(r,1e-12),-1,1))
    phi=np.mod(np.arctan2(xyz[:,1],xyz[:,0]),2*np.pi)
    centers=np.linspace(0.15,2.4,nrad); width=0.42
    scores=np.zeros((vecs.shape[1],lmax+1))
    for l in range(lmax+1):
        cols=[]
        for rc in centers:
            radial=np.exp(-0.5*((r-rc)/width)**2)
            for m in range(-l,l+1): cols.append(radial*real_ylm(l,m,theta,phi))
        B=np.column_stack(cols)
        Q,_=np.linalg.qr(B,mode='reduced')
        scores[:,l]=np.sum((Q.T@vecs)**2,axis=0)/np.maximum(np.sum(vecs*vecs,axis=0),1e-15)
    return scores


def solve(n,beta,rope_pts):
    x=np.linspace(-BOX,BOX,n+2)[1:-1]; h=x[1]-x[0]
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij'); xyz=np.column_stack([X.ravel(),Y.ravel(),Z.ravel()])
    L=lap1(n,h); I=eye(n,format='csr')
    H0=kron(kron(L,I),I)+kron(kron(I,L),I)+kron(kron(I,I),L)
    r=np.linalg.norm(xyz,axis=1)
    dc=cKDTree(rope_pts).query(xyz,k=1,workers=-1)[0]
    V=-ALPHA/np.sqrt(r*r+EPS*EPS)-beta*np.exp(-0.5*(dc/SIGMA)**2)
    H=H0+diags(V,0,format='csr')
    vals,vecs=eigsh(H,k=N_EIG,which='SA',tol=2e-7,maxiter=5000)
    order=np.argsort(vals); vals=vals[order]; vecs=vecs[:,order]
    prob=vecs*vecs
    localized=np.sum(prob[r<2.2],axis=0)/np.maximum(np.sum(prob,axis=0),1e-15)
    scores=angular_scores(vecs,xyz)
    return vals,localized,scores,h


def clusters(vals,tol=0.04):
    out=[]; cur=[0]
    for i in range(1,len(vals)):
        scale=max(abs(vals[i]),abs(vals[i-1]),0.25)
        if abs(vals[i]-vals[i-1])/scale<tol: cur.append(i)
        else: out.append(cur); cur=[i]
    out.append(cur); return [len(q) for q in out]


def run():
    st=np.load(ROOT/'analysis'/'ELEC009_state.npz')
    model=Model(20,knots=st['knots_final'],m_energy=64)
    d,lk,cert,_=model.cert(st['z_final'])
    rope_pts=np.vstack(model.curves(st['z_final'],768))
    rows=[]; summary=[]; cache={}
    for beta in BETAS:
        for n in LEVELS:
            vals,loc,scores,h=solve(n,beta,rope_pts); cache[(beta,n)]=(vals,loc,scores,h)
            dom=np.argmax(scores,axis=1); purity=np.max(scores,axis=1)
            for k in range(N_EIG):
                rows.append((beta,n,h,k,vals[k],loc[k],dom[k],purity[k],*scores[k]))
        vf=cache[(beta,LEVELS[-1])][0]; vc=cache[(beta,LEVELS[0])][0]
        # compare excitation gaps, which are more stable than absolute finite-box energies
        gf=vf-vf[0]; gc=vc-vc[0]
        conv=float(np.max(np.abs(gf[1:10]-gc[1:10])/np.maximum(np.abs(gf[1:10]),0.25)))
        loc=cache[(beta,LEVELS[-1])][1]; scores=cache[(beta,LEVELS[-1])][2]
        dom=np.argmax(scores,axis=1); pur=np.max(scores,axis=1)
        summary.append((beta,conv,clusters(vf[:12]),dom[:12].tolist(),pur[:12].tolist(),float(np.mean(loc[:12]))))

    B1=bool(cert and d>=0.060 and abs(abs(lk)-1)<=0.03)
    B2=max(s[1] for s in summary)<CONV_TOL
    B3=all(s[5]>=LOC_TOL for s in summary)
    # central baseline should have identifiable l=0 and l=1 families among low modes
    base=summary[0]; B4=(0 in base[3][:6] and base[3][:6].count(1)>=2 and np.mean(base[4][:6])>=PURITY_TOL)
    # modest rope coupling should preserve identifiable angular character, rather than destroy it
    modest=[s for s in summary if 0< s[0] <=0.5]
    B5=all(np.mean(s[4][:8])>=0.45 and 0 in s[3][:8] and 1 in s[3][:8] for s in modest)
    finding='SURROUNDING_3D_FIELD_SUPPORTS_ROBUST_ANGULAR_MODE_FAMILIES' if all((B1,B2,B3,B4,B5)) else 'SURROUNDING_3D_FIELD_GATE_NOT_YET_PASSED'

    with open(ROOT/'analysis'/'ROPE_MODE003_spectrum.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['beta','grid_n','h','mode','eigenvalue','localized_fraction','dominant_l','purity','score_l0','score_l1','score_l2','score_l3']); w.writerows(rows)
    out=['ROPE-MODE-003 surrounding 3-D scalar-field spectrum',f'certified={cert} dmin={d:.8f} Lk512={lk:.8f}',f'alpha={ALPHA} eps={EPS} sigma={SIGMA} box={BOX} grids={LEVELS}']
    for beta,conv,cl,dom,pur,loc in summary:
        out.append(f'beta={beta:g} gap_conv={conv:.6g} clusters={cl} dominant_l={dom} mean_purity={np.mean(pur):.4f} mean_localized={loc:.4f}')
    for name,b in [('B1 certified linked rope',B1),('B2 grid-converged low excitation gaps',B2),('B3 low modes localized inside analysis volume',B3),('B4 central baseline has identifiable s/p angular families',B4),('B5 angular families survive modest rope coupling',B5)]: out.append(name+': '+('PASS' if b else 'FAIL'))
    out.append('FINDING: '+finding)
    text='\n'.join(out); print(text)
    (ROOT/'analysis'/'ROPE_MODE003_run.log').write_text(text+'\n')
    np.savez(ROOT/'analysis'/'ROPE_MODE003_summary.npz',betas=np.array(BETAS),levels=np.array(LEVELS),dmin=d,lk=lk)
    return finding,summary

if __name__=='__main__': run()
