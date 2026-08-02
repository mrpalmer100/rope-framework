"""ROPE-VALIDATION-001: imposed Aharonov--Bohm holonomy instrument test.

This is deliberately NOT a rope-physics claim.  It validates the complex
Hermitian lattice-gauge eigensolver against the exactly soluble quantum ring.
The imposed phase theta is external.  Passing means the numerical instrument
can represent global phase transport, gauge invariance, flux periodicity, and
the equivalence of link-gauge and twisted-boundary implementations.
"""
from pathlib import Path
import csv, json
import numpy as np
from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.linalg import eigsh

ROOT = Path(__file__).resolve().parents[2]
LEVELS = (48, 96, 192, 384)
RADIUS = 1.0
ALPHAS = np.linspace(0.0, 1.0, 17)   # theta/(2 pi), includes one full period
N_EIG = 12
SEED = 20260801


def covariant_ring(n, alpha, chi=None):
    """Return -D_A^2 on a periodic ring using oriented link variables.

    Link U_j transports from j+1 to j in the hopping term.  A uniform gauge
    has U_j=exp(-i*theta/n), theta=2*pi*alpha.  Under psi' = G psi,
    U'_j = exp(i chi_j) U_j exp(-i chi_{j+1}), so H'=G H G^dagger.
    """
    L = 2*np.pi*RADIUS
    h = L/n
    theta = 2*np.pi*alpha
    U = np.full(n, np.exp(-1j*theta/n), dtype=np.complex128)
    if chi is not None:
        chi = np.asarray(chi)
        U = np.exp(1j*chi) * U * np.exp(-1j*np.roll(chi, -1))
    H = lil_matrix((n,n), dtype=np.complex128)
    for j in range(n):
        jp=(j+1)%n
        H[j,j] += 2.0/(h*h)
        H[j,jp] += -U[j]/(h*h)
        H[jp,j] += -np.conj(U[j])/(h*h)
    return csr_matrix(H), h


def twisted_ring(n, alpha):
    """Same holonomy in a gauge with zero internal links and a boundary twist."""
    L=2*np.pi*RADIUS; h=L/n; theta=2*np.pi*alpha
    H=lil_matrix((n,n),dtype=np.complex128)
    for j in range(n): H[j,j]=2.0/(h*h)
    for j in range(n-1):
        H[j,j+1]=-1.0/(h*h); H[j+1,j]=-1.0/(h*h)
    # This boundary link has total Wilson phase exp(-i theta).
    H[n-1,0]=-np.exp(-1j*theta)/(h*h)
    H[0,n-1]=-np.exp(1j*theta)/(h*h)
    return csr_matrix(H),h


def spectrum(H,k=N_EIG):
    # For small matrices dense eigvalsh is more accurate and deterministic.
    vals=np.linalg.eigvalsh(H.toarray())
    return np.sort(vals.real)[:k]


def exact_lattice(n,alpha,k=N_EIG):
    h=2*np.pi*RADIUS/n
    # One representative from each of the n lattice momentum classes.
    m=np.arange(n)
    vals=4.0*np.sin(np.pi*(m-alpha)/n)**2/(h*h)
    return np.sort(vals)[:k]


def continuum(alpha,k=N_EIG):
    m=np.arange(-100,101)
    vals=(m-alpha)**2/(RADIUS*RADIUS)
    return np.sort(vals)[:k]


def main():
    rng=np.random.default_rng(SEED)
    rows=[]
    exact_errors=[]; twist_errors=[]; gauge_errors=[]; herm_errors=[]
    periodic_errors=[]; reversal_errors=[]
    cache={}
    for n in LEVELS:
        chi=rng.uniform(-np.pi,np.pi,n)
        for alpha in ALPHAS:
            H,h=covariant_ring(n,float(alpha))
            vals=spectrum(H)
            cache[(n,float(alpha))]=vals
            ex=exact_lattice(n,float(alpha))
            cont=continuum(float(alpha))
            Ht,_=twisted_ring(n,float(alpha)); vt=spectrum(Ht)
            Hg,_=covariant_ring(n,float(alpha),chi=chi); vg=spectrum(Hg)
            herm=float(np.linalg.norm((H-H.getH()).toarray(),ord='fro')/max(np.linalg.norm(H.toarray(),ord='fro'),1e-30))
            ee=float(np.max(np.abs(vals-ex)))
            te=float(np.max(np.abs(vals-vt)))
            ge=float(np.max(np.abs(vals-vg)))
            exact_errors.append(ee); twist_errors.append(te); gauge_errors.append(ge); herm_errors.append(herm)
            for mode,(v,e,c) in enumerate(zip(vals,ex,cont)):
                rows.append(dict(n=n,h=h,alpha=float(alpha),theta=float(2*np.pi*alpha),mode=mode,eigenvalue=float(v),exact_lattice=float(e),continuum=float(c),abs_exact_error=float(abs(v-e)),abs_continuum_error=float(abs(v-c))))
        # periodicity and reversal on same mesh
        for alpha in ALPHAS:
            v=cache[(n,float(alpha))]
            # alpha+1 computed directly to avoid relying on endpoint only
            vp=spectrum(covariant_ring(n,float(alpha+1.0))[0])
            vm=spectrum(covariant_ring(n,float(-alpha))[0])
            periodic_errors.append(float(np.max(np.abs(v-vp))))
            reversal_errors.append(float(np.max(np.abs(v-vm))))

    # continuum convergence: compare low spectrum at alpha values away from crossings too
    conv=[]
    for alpha in (0.0,0.125,0.25,0.375,0.5):
        c=continuum(alpha)
        errs=[]
        for n in LEVELS:
            vals=spectrum(covariant_ring(n,alpha)[0])
            errs.append(float(np.max(np.abs(vals[:8]-c[:8]))))
        conv.append((alpha,*errs))
    max_finest_cont=max(x[-1] for x in conv)
    monotone=all(all(row[i+1] <= row[i]*(1+1e-10) for i in range(1,len(row)-1)) for row in conv)

    # Nontrivial holonomy response: the ground state rises to alpha=1/2 and returns.
    nf=LEVELS[-1]
    e0=cache[(nf,0.0)][0]; ehalf=cache[(nf,0.5)][0]; e1=cache[(nf,1.0)][0]
    response=float(ehalf-e0)

    bars={
      'B1_hermitian': max(herm_errors)<1e-13,
      'B2_exact_lattice_solution': max(exact_errors)<2e-10,
      'B3_gauge_invariance': max(gauge_errors)<2e-10,
      'B4_twisted_boundary_equivalence': max(twist_errors)<2e-10,
      'B5_flux_periodicity': max(periodic_errors)<2e-10,
      'B6_flux_reversal_symmetry': max(reversal_errors)<2e-10,
      'B7_continuum_convergence': bool(monotone and max_finest_cont<0.01),
      'B8_nontrivial_holonomy_response': bool(response>0.20 and abs(e1-e0)<2e-10),
    }
    finding='AB_HOLONOMY_INSTRUMENT_VALIDATED' if all(bars.values()) else 'AB_HOLONOMY_VALIDATION_FAILED'
    summary={
      'scope':'solver validation only; imposed flux is not derived from rope dynamics',
      'levels':LEVELS,'n_flux_samples':len(ALPHAS),'n_eigenvalues':N_EIG,
      'max_hermiticity_error':max(herm_errors),
      'max_exact_lattice_error':max(exact_errors),
      'max_gauge_spectrum_error':max(gauge_errors),
      'max_twisted_boundary_error':max(twist_errors),
      'max_flux_periodicity_error':max(periodic_errors),
      'max_flux_reversal_error':max(reversal_errors),
      'finest_max_continuum_error_first8':max_finest_cont,
      'ground_state_half_flux_response':response,
      'ground_state_period_closure_error':float(abs(e1-e0)),
      'bars':{k:bool(v) for k,v in bars.items()},'finding':finding,
      'technical_note':'This exact ring benchmark has no regularized Biot-Savart core a. A future 3-D flux-tube benchmark must sweep a and h jointly.'
    }
    out=ROOT/'analysis'; out.mkdir(exist_ok=True)
    with open(out/'ROPE_VALIDATION001_spectrum.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    with open(out/'ROPE_VALIDATION001_convergence.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['alpha']+[f'max_abs_error_N{n}' for n in LEVELS]); w.writerows(conv)
    (out/'ROPE_VALIDATION001_summary.json').write_text(json.dumps(summary,indent=2))
    lines=['ROPE-VALIDATION-001 imposed Aharonov--Bohm holonomy instrument test',summary['scope'],
           f"levels={LEVELS} flux_samples={len(ALPHAS)} eigs={N_EIG}",
           f"max Hermiticity error={summary['max_hermiticity_error']:.6g}",
           f"max exact-lattice spectral error={summary['max_exact_lattice_error']:.6g}",
           f"max gauge-transformation spectral error={summary['max_gauge_spectrum_error']:.6g}",
           f"max link-vs-twist spectral error={summary['max_twisted_boundary_error']:.6g}",
           f"max alpha->alpha+1 periodicity error={summary['max_flux_periodicity_error']:.6g}",
           f"max alpha->-alpha reversal error={summary['max_flux_reversal_error']:.6g}",
           f"finest first-8 continuum error={summary['finest_max_continuum_error_first8']:.6g}",
           f"ground-state half-flux response={response:.6g}",
           f"period closure error={abs(e1-e0):.6g}"]
    lines += [k+': '+('PASS' if v else 'FAIL') for k,v in bars.items()]
    lines += ['FINDING: '+finding,'NOTE: '+summary['technical_note']]
    text='\n'.join(lines)
    print(text)
    (out/'ROPE_VALIDATION001_run.log').write_text(text+'\n')
    (out/'ROPE_VALIDATION001_results.md').write_text('# ROPE-VALIDATION-001 — Imposed AB holonomy instrument test\n\n'+text.replace('\n','  \n')+'\n\n## Interpretation\n\nThis validates the numerical representation of an externally imposed global phase on an exactly soluble ring. It is not evidence that a rope carries flux, fixes the coupling, or dynamically generates holonomy.\n')
    return summary

if __name__=='__main__': main()
