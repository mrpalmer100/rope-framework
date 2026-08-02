"""ROPE-VALIDATION-003: excluded-core 3-D Aharonov--Bohm validation.

Numerical instrument test only. The wavefunction lives on a Cartesian 3-D
annular domain with a cylindrical core removed. Outside the excluded core the
connection is flat; its only physical content is the imposed holonomy around
the inaccessible axis. Distributed-link and twisted-cut gauges are compared.
No claim is made that a rope supplies or dynamically generates the flux.
"""
from pathlib import Path
import csv, json
import numpy as np
from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.linalg import eigsh

ROOT = Path(__file__).resolve().parents[2]
BOX = 3.0
LEVELS = (15, 19, 23)
CORE_RADII = (0.45, 0.75)
ALPHAS = (0.0, 0.25, 0.5, 1.0)
N_EIG = 4
R0 = 1.45
KR = 45.0
KZ = 35.0
SEED = 20260801


def make_domain(n, r_core):
    x = np.linspace(-BOX, BOX, n + 2)[1:-1]
    h = float(x[1] - x[0])
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    rho = np.sqrt(X*X + Y*Y)
    mask = rho > r_core
    coords = np.column_stack([X[mask], Y[mask], Z[mask]])
    ijk = np.argwhere(mask)
    lookup = {tuple(v): p for p, v in enumerate(ijk)}
    return x, h, coords, ijk, lookup


def principal_angle(d):
    return np.angle(np.exp(1j*d))


def build_hamiltonian(n, r_core, alpha, gauge='distributed', chi=None):
    x, h, xyz, ijk, lookup = make_domain(n, r_core)
    N = len(xyz)
    phi = np.arctan2(xyz[:,1], xyz[:,0])
    rho = np.sqrt(xyz[:,0]**2 + xyz[:,1]**2)
    V = KR*(rho-R0)**2 + KZ*xyz[:,2]**2
    H = lil_matrix((N, N), dtype=np.complex128)
    H.setdiag(6.0/(h*h) + V)
    dirs = ((1,0,0),(0,1,0),(0,0,1))
    for p, (i,j,k) in enumerate(ijk):
        for di,dj,dk in dirs:
            q = lookup.get((i+di,j+dj,k+dk))
            if q is None:
                continue
            raw = phi[q] - phi[p]
            wrapped = principal_angle(raw)
            if gauge == 'distributed':
                U = np.exp(-1j*alpha*wrapped)
            elif gauge == 'cut':
                m = int(np.rint((raw-wrapped)/(2*np.pi)))
                U = np.exp(1j*2*np.pi*alpha*m)
            else:
                raise ValueError(gauge)
            if chi is not None:
                U = np.exp(1j*chi[p])*U*np.exp(-1j*chi[q])
            H[p,q] = -U/(h*h)
            H[q,p] = -np.conj(U)/(h*h)
    return csr_matrix(H), h, xyz


def spectrum(H, k=N_EIG):
    vals = eigsh(H, k=k, which='SA', tol=1e-9, maxiter=12000,
                 return_eigenvectors=False)
    return np.sort(vals.real)


def run():
    rng = np.random.default_rng(SEED)
    rows=[]; cache={}; herm=[]
    # Main spectral matrix only.
    for r_core in CORE_RADII:
        for n in LEVELS:
            for alpha in ALPHAS:
                H,h,xyz=build_hamiltonian(n,r_core,alpha,'distributed')
                vals=spectrum(H)
                if alpha == 0.25 and n == LEVELS[-1]:
                    herm.append(float(np.linalg.norm((H-H.getH()).data)/max(np.linalg.norm(H.data),1e-30)))
                cache[(r_core,n,alpha)] = vals
                gaps=vals-vals[0]
                for mode,(v,g) in enumerate(zip(vals,gaps)):
                    rows.append(dict(n=n,h=h,r_core=r_core,r_core_over_h=r_core/h,
                                     alpha=alpha,mode=mode,eigenvalue=float(v),gap=float(g)))

    # Expensive equivalence checks only at the finest grid, where they are strongest.
    gauge_err=[]; cut_err=[]; reversal_err=[]
    for r_core in CORE_RADII:
        n=LEVELS[-1]
        _,_,xyz,_,_=make_domain(n,r_core)
        chi=rng.uniform(-np.pi,np.pi,len(xyz))
        H,_,_=build_hamiltonian(n,r_core,0.25,'distributed')
        base=cache[(r_core,n,0.25)]
        Hg,_,_=build_hamiltonian(n,r_core,0.25,'distributed',chi=chi)
        Hc,_,_=build_hamiltonian(n,r_core,0.25,'cut')
        Hm,_,_=build_hamiltonian(n,r_core,-0.25,'distributed')
        gauge_err.append(float(np.max(np.abs(base-spectrum(Hg)))))
        cut_err.append(float(np.max(np.abs(base-spectrum(Hc)))))
        reversal_err.append(float(np.max(np.abs(base-spectrum(Hm)))))

    diagnostics=[]
    for r_core in CORE_RADII:
        grid_drifts=[]; closures=[]; responses=[]
        for n in LEVELS:
            e0=cache[(r_core,n,0.0)]; eh=cache[(r_core,n,0.5)]; e1=cache[(r_core,n,1.0)]
            closures.append(float(np.max(np.abs((e1-e1[0])-(e0-e0[0])))))
            responses.append(float(eh[0]-e0[0]))
        for n0,n1 in zip(LEVELS[:-1],LEVELS[1:]):
            for alpha in (0.25,0.5):
                g0=cache[(r_core,n0,alpha)]-cache[(r_core,n0,alpha)][0]
                g1=cache[(r_core,n1,alpha)]-cache[(r_core,n1,alpha)][0]
                grid_drifts.append(float(np.max(np.abs(g1[1:]-g0[1:]) /
                                                np.maximum(np.abs(g1[1:]),0.25))))
        diagnostics.append(dict(r_core=r_core,
                                half_flux_response_finest=responses[-1],
                                period_closure_finest=closures[-1],
                                max_grid_gap_drift=max(grid_drifts),
                                responses=responses,closures=closures))

    max_herm=max(herm); max_gauge=max(gauge_err); max_cut=max(cut_err)
    max_reverse=max(reversal_err)
    max_period=max(d['period_closure_finest'] for d in diagnostics)
    max_grid=max(d['max_grid_gap_drift'] for d in diagnostics)
    min_response=min(abs(d['half_flux_response_finest']) for d in diagnostics)
    bars={
      'B1_hermitian': max_herm < 1e-12,
      'B2_arbitrary_gauge_invariance': max_gauge < 1e-6,
      'B3_distributed_cut_equivalence': max_cut < 1e-6,
      'B4_unit_flux_periodicity': max_period < 1e-6,
      'B5_flux_reversal_symmetry': max_reverse < 1e-6,
      'B6_nontrivial_half_flux_response': min_response > 0.05,
      'B7_grid_convergence': max_grid < 0.10,
    }
    finding='AB_3D_EXCLUDED_CORE_INSTRUMENT_VALIDATED' if all(bars.values()) else 'AB_3D_EXCLUDED_CORE_VALIDATION_INCOMPLETE'
    summary={
      'scope':'3-D excluded-core AB solver validation only; holonomy is imposed externally and not derived from rope dynamics',
      'box':BOX,'levels':LEVELS,'core_radii':CORE_RADII,'alphas':ALPHAS,'n_eig':N_EIG,
      'max_hermiticity_error':max_herm,'max_arbitrary_gauge_spectrum_error':max_gauge,
      'max_distributed_cut_spectrum_error':max_cut,'max_flux_reversal_error':max_reverse,
      'diagnostics':diagnostics,'bars':{k:bool(v) for k,v in bars.items()},'finding':finding,
      'technical_note':'The cylindrical core is excluded from the wavefunction domain. Link phases implement a flat connection outside the core, so unit-flux periodicity and cut-gauge equivalence are exact lattice tests rather than thin-core extrapolations.'
    }
    out=ROOT/'analysis'; out.mkdir(exist_ok=True)
    with open(out/'ROPE_VALIDATION003_spectrum.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    (out/'ROPE_VALIDATION003_summary.json').write_text(json.dumps(summary,indent=2))
    lines=['ROPE-VALIDATION-003 3-D excluded-core Aharonov--Bohm instrument test',summary['scope'],
           f'levels={LEVELS} core radii={CORE_RADII} alphas={ALPHAS} eigs={N_EIG}',
           f'max Hermiticity error={max_herm:.6g}',
           f'max arbitrary-gauge spectrum error={max_gauge:.6g}',
           f'max distributed-vs-cut spectrum error={max_cut:.6g}',
           f'max flux-reversal error={max_reverse:.6g}']
    for d in diagnostics:
        lines.append(f"r_core={d['r_core']:.3f} half-flux response={d['half_flux_response_finest']:.6g} period closure={d['period_closure_finest']:.6g} max gap drift={d['max_grid_gap_drift']:.6g}")
    lines += [k+': '+('PASS' if v else 'FAIL') for k,v in bars.items()]
    lines += ['FINDING: '+finding,'NOTE: '+summary['technical_note']]
    text='\n'.join(lines); print(text)
    (out/'ROPE_VALIDATION003_run.log').write_text(text+'\n')
    (out/'ROPE_VALIDATION003_results.md').write_text(
      '# ROPE-VALIDATION-003 — 3-D excluded-core Aharonov–Bohm instrument test\n\n'+
      text.replace('\n','  \n')+
      '\n\n## Interpretation\n\nThis validates a three-dimensional multiply connected lattice-gauge solver with an externally imposed holonomy. It does not show that a rope carries flux, fixes its strength, or generates the phase dynamically.\n')
    return summary

if __name__=='__main__': run()
