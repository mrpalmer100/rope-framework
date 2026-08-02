# ELEC-003 — Resolution and Stability Campaign

## Question

Is ELEC-002's localized linked attractor robust to practical grid refinement, Fourier-basis enlargement, Gaussian tube-width variation, out-of-basis perturbations, and repeated re-perturbation?

## Locked practical bars

1. All runs preserve the linked sector, descend monotonically by more than 2.5%, and remain localized in `0.4 < R_rms < 2.0`.
2. Grid convergence: the `N=14` and `N=16` radii differ by less than 8%.
3. Basis convergence: the `K=4` and `K=5` radii differ by less than 10%.
4. Tube-width robustness: adjacent-radius changes remain below 25% over `a = 0.18, 0.24, 0.30, 0.36`.
5. Out-of-basis/re-perturbation stability: three successive relaxed radii have CV below 12% and stay linked.

## Result

- **Bar 1 PASS:** all 15 runs remained linked, descended monotonically, and stayed localized.
- **Bar 2 PASS:** `N=14 -> 16` radius difference = **2.00%**.
- **Bar 3 FAIL:** `K=4 -> 5` radius difference = **14.77%**, above the locked 10% threshold.
- **Bar 4 PASS:** maximum adjacent tube-width radius jump = **19.71%**.
- **Bar 5 PASS:** repeated out-of-basis/re-perturbation radius CV = **3.67%**.

The localized object is robust across grid resolution, regularization width, and repeated perturbation in this practical campaign. However, the attractor radius has not converged with Fourier-basis size: adding the fifth harmonic shifted the independently optimized radius from 0.681 to 0.790. This failure is retained rather than softened.

## Interpretation

ELEC-003 strengthens the existence of a localized topological basin but does **not** establish a basis-independent continuum object. The most productive next step is a focused basis-convergence campaign using matched initial conditions, longer optimization, and `K = 4, 5, 6, 8` to distinguish incomplete optimization from a genuine high-mode instability.

No identification with the physical electron, electron mass, spin, or magnetic moment is made.
