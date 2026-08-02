# ROPE-VALIDATION-001 — Imposed AB holonomy instrument test

ROPE-VALIDATION-001 imposed Aharonov--Bohm holonomy instrument test  
solver validation only; imposed flux is not derived from rope dynamics  
levels=(48, 96, 192, 384) flux_samples=17 eigs=12  
max Hermiticity error=0  
max exact-lattice spectral error=1.17195e-11  
max gauge-transformation spectral error=1.69049e-11  
max link-vs-twist spectral error=1.82971e-11  
max alpha->alpha+1 periodicity error=1.71024e-11  
max alpha->-alpha reversal error=0  
finest first-8 continuum error=0.00571076  
ground-state half-flux response=0.249999  
period closure error=3.14893e-12  
B1_hermitian: PASS  
B2_exact_lattice_solution: PASS  
B3_gauge_invariance: PASS  
B4_twisted_boundary_equivalence: PASS  
B5_flux_periodicity: PASS  
B6_flux_reversal_symmetry: PASS  
B7_continuum_convergence: PASS  
B8_nontrivial_holonomy_response: PASS  
FINDING: AB_HOLONOMY_INSTRUMENT_VALIDATED  
NOTE: This exact ring benchmark has no regularized Biot-Savart core a. A future 3-D flux-tube benchmark must sweep a and h jointly.

## Interpretation

This validates the numerical representation of an externally imposed global phase on an exactly soluble ring. It is not evidence that a rope carries flux, fixes the coupling, or dynamically generates holonomy.
