# ROPE-VALIDATION-002 — 3-D regularized AB flux-tube instrument test

ROPE-VALIDATION-002 3-D regularized AB flux-tube instrument test  
3-D imposed-flux solver validation only; flux is external and not derived from rope dynamics  
levels=(17, 23, 29) a/h=(1.5, 2.5, 3.5) alphas=(0.0, 0.25, 0.5, 1.0) eigs=5  
max Hermiticity error=0  
max gauge spectrum error=8.17124e-13  
fixed-core gap drift=0.115905  
a/h=1.50 half-flux response=0.1185 period closure=2.28333 max gap drift=0.109929  
a/h=2.50 half-flux response=0.0990929 period closure=2.1373 max gap drift=0.201657  
a/h=3.50 half-flux response=0.0787204 period closure=1.96558 max gap drift=0.250129  
B1_hermitian: PASS  
B2_lattice_gauge_invariance: PASS  
B3_nontrivial_flux_response: PASS  
B4_joint_h_a_convergence: FAIL  
B5_fixed_core_crosscheck: FAIL  
B6_thin_core_periodicity_trend: FAIL  
FINDING: AB_3D_FLUX_TUBE_VALIDATION_INCOMPLETE  
NOTE: Finite regularized cores contain real magnetic field and need not have exact unit-flux periodicity. The validation target is gauge invariance, joint h/a stability, nonzero holonomy response, and convergence toward periodic behavior as the resolved core narrows.

## Interpretation

This validates a three-dimensional complex lattice-gauge solver with an externally imposed regularized flux tube. It does not show that a rope supplies flux, fixes its strength, or dynamically generates holonomy.
