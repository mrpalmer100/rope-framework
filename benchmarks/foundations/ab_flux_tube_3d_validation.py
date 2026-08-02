"""ROPE-VALIDATION-002: 3-D regularized AB flux-tube instrument test.

Numerical validation only. An external flux tube is imposed along the z axis
inside a 3-D toroidal trapping potential. The benchmark jointly varies grid
spacing h and regularized core width a, verifies Hermiticity and lattice gauge
invariance, and checks convergence toward the thin-core periodic holonomy
response. It does not claim that a rope carries or generates flux.
"""
from pathlib import Path
import csv, json
import numpy as np
from scipy.sparse import lil_matrix, diags, csr_matrix
from scipy.sparse.linalg import eigsh

ROOT = Path(__file__).resolve().parents[2]
BOX = 3.0
LEVELS = (17, 23, 29)
A_OVER_H = (1.5, 2.5, 3.5)
ALPHAS = (0.0, 0.25, 0.5, 1.0)
N_EIG = 5
R0 = 1.45
KR = 45.0
KZ = 35.0
SEED = 20260801


def grid(n):
    x=np.linspace(-BOX,BOX,n+2)[1:-1]
    h=float(x[1]-x[0])
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    xyz=np.column_stack([X.ravel(),Y.ravel(),Z.ravel()])
    return x,h,xyz


def vector_potential(xyz, alpha, a):
    x,y=xyz[:,0],xyz[:,1]
    den=x*x+y*y+a*a
    A=np.zeros_like(xyz)
    A[:,0]=-alpha*y/den
    A[:,1]= alpha*x/den
    return A


def build_hamiltonian(n, alpha, a, chi=None):
    x,h,xyz=grid(n); N=n**3
    A=vector_potential(xyz,alpha,a)
    H=lil_matrix((N,N),dtype=np.complex128)
    rho=np.sqrt(xyz[:,0]**2+xyz[:,1]**2)
    V=KR*(rho-R0)**2 + KZ*xyz[:,2]**2
    H.setdiag(6.0/(h*h)+V)
    def idx(i,j,k): return (i*n+j)*n+k
    # positive coordinate links, midpoint A average
    dirs=((1,0,0,0),(0,1,0,1),(0,0,1,2))
    for i in range(n):
      for j in range(n):
       for k in range(n):
        p=idx(i,j,k)
        for di,dj,dk,comp in dirs:
          ii,jj,kk=i+di,j+dj,k+dk
          if ii>=n or jj>=n or kk>=n: continue
          q=idx(ii,jj,kk)
          amid=0.5*(A[p,comp]+A[q,comp])
          U=np.exp(-1j*h*amid)
          if chi is not None:
              U=np.exp(1j*chi[p])*U*np.exp(-1j*chi[q])
          H[p,q]=-U/(h*h)
          H[q,p]=-np.conj(U)/(h*h)
    return csr_matrix(H),h,xyz


def spectrum(H,k=N_EIG):
    vals=eigsh(H,k=k,which='SA',tol=2e-7,maxiter=7000,return_eigenvectors=False)
    return np.sort(vals.real)


def run():
    rng=np.random.default_rng(SEED)
    rows=[]; herm=[]; gauge=[]; cache={}
    for n in LEVELS:
      _,h,xyz=grid(n)
      chi=rng.uniform(-np.pi,np.pi,n**3)
      for ratio in A_OVER_H:
       a=ratio*h
       for alpha in ALPHAS:
        H,_,_=build_hamiltonian(n,alpha,a)
        vals=spectrum(H)
        Hg,_,_=build_hamiltonian(n,alpha,a,chi=chi)
        vg=spectrum(Hg)
        he=float(np.linalg.norm((H-H.getH()).data)/max(np.linalg.norm(H.data),1e-30))
        ge=float(np.max(np.abs(vals-vg)))
        herm.append(he); gauge.append(ge); cache[(n,ratio,alpha)]=vals
        gaps=vals-vals[0]
        for mode,v,g in zip(range(N_EIG),vals,gaps):
            rows.append(dict(n=n,h=h,a_over_h=ratio,a=a,alpha=alpha,mode=mode,eigenvalue=float(v),gap=float(g)))

    # diagnostics at each ratio: flux response and period closure, plus h convergence
    diagnostics=[]
    for ratio in A_OVER_H:
      responses=[]; closures=[]; gap_drifts=[]
      for n in LEVELS:
        e0=cache[(n,ratio,0.0)]; eh=cache[(n,ratio,0.5)]; e1=cache[(n,ratio,1.0)]
        responses.append(float(eh[0]-e0[0]))
        closures.append(float(np.max(np.abs((e1-e1[0])-(e0-e0[0])))))
      for n0,n1 in zip(LEVELS[:-1],LEVELS[1:]):
        g0=cache[(n0,ratio,0.5)]-cache[(n0,ratio,0.5)][0]
        g1=cache[(n1,ratio,0.5)]-cache[(n1,ratio,0.5)][0]
        gap_drifts.append(float(np.max(np.abs(g1[1:]-g0[1:])/np.maximum(np.abs(g1[1:]),0.25))))
      diagnostics.append(dict(a_over_h=ratio,half_flux_response_finest=responses[-1],period_closure_finest=closures[-1],max_gap_drift=max(gap_drifts),responses=responses,closures=closures))

    # Fixed physical core convergence cross-check: interpolate by nearest a across levels.
    target_a=0.45
    fixed=[]
    for n in LEVELS:
      _,h,_=grid(n); ratio=min(A_OVER_H,key=lambda r:abs(r*h-target_a))
      vals=cache[(n,ratio,0.5)]; fixed.append((n,h,ratio,ratio*h,vals-vals[0]))
    fixed_drift=max(float(np.max(np.abs(fixed[i+1][4][1:]-fixed[i][4][1:])/np.maximum(np.abs(fixed[i+1][4][1:]),0.25))) for i in range(len(fixed)-1))

    max_herm=max(herm); max_gauge=max(gauge)
    finest=[d for d in diagnostics if d['a_over_h']==A_OVER_H[0]][0]
    # Thin-core trend: closure should improve as a/h decreases at finest n.
    closures_finest=[d['period_closure_finest'] for d in diagnostics]
    thin_trend=closures_finest[0] <= closures_finest[-1]
    bars={
      'B1_hermitian': max_herm<1e-12,
      'B2_lattice_gauge_invariance': max_gauge<2e-7,
      'B3_nontrivial_flux_response': finest['half_flux_response_finest']>0.05,
      'B4_joint_h_a_convergence': max(d['max_gap_drift'] for d in diagnostics)<0.08,
      'B5_fixed_core_crosscheck': fixed_drift<0.08,
      'B6_thin_core_periodicity_trend': bool(thin_trend and closures_finest[0]<0.08),
    }
    finding='AB_3D_FLUX_TUBE_INSTRUMENT_VALIDATED' if all(bars.values()) else 'AB_3D_FLUX_TUBE_VALIDATION_INCOMPLETE'
    summary={
      'scope':'3-D imposed-flux solver validation only; flux is external and not derived from rope dynamics',
      'box':BOX,'levels':LEVELS,'a_over_h':A_OVER_H,'alphas':ALPHAS,'n_eig':N_EIG,
      'max_hermiticity_error':max_herm,'max_gauge_spectrum_error':max_gauge,
      'diagnostics':diagnostics,'fixed_physical_core_target':target_a,'fixed_core_gap_drift':fixed_drift,
      'bars':{k:bool(v) for k,v in bars.items()},'finding':finding,
      'technical_note':'Finite regularized cores contain real magnetic field and need not have exact unit-flux periodicity. The validation target is gauge invariance, joint h/a stability, nonzero holonomy response, and convergence toward periodic behavior as the resolved core narrows.'
    }
    out=ROOT/'analysis'; out.mkdir(exist_ok=True)
    with open(out/'ROPE_VALIDATION002_spectrum.csv','w',newline='') as f:
      w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    (out/'ROPE_VALIDATION002_summary.json').write_text(json.dumps(summary,indent=2))
    lines=['ROPE-VALIDATION-002 3-D regularized AB flux-tube instrument test',summary['scope'],
           f'levels={LEVELS} a/h={A_OVER_H} alphas={ALPHAS} eigs={N_EIG}',
           f'max Hermiticity error={max_herm:.6g}',f'max gauge spectrum error={max_gauge:.6g}',
           f'fixed-core gap drift={fixed_drift:.6g}']
    for d in diagnostics:
      lines.append(f"a/h={d['a_over_h']:.2f} half-flux response={d['half_flux_response_finest']:.6g} period closure={d['period_closure_finest']:.6g} max gap drift={d['max_gap_drift']:.6g}")
    lines += [k+': '+('PASS' if v else 'FAIL') for k,v in bars.items()]
    lines += ['FINDING: '+finding,'NOTE: '+summary['technical_note']]
    text='\n'.join(lines); print(text)
    (out/'ROPE_VALIDATION002_run.log').write_text(text+'\n')
    (out/'ROPE_VALIDATION002_results.md').write_text('# ROPE-VALIDATION-002 — 3-D regularized AB flux-tube instrument test\n\n'+text.replace('\n','  \n')+'\n\n## Interpretation\n\nThis validates a three-dimensional complex lattice-gauge solver with an externally imposed regularized flux tube. It does not show that a rope supplies flux, fixes its strength, or dynamically generates holonomy.\n')
    return summary

if __name__=='__main__': run()
