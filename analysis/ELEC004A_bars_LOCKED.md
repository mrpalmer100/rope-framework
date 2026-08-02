# ELEC-004A — Linear-stability gate (locked protocol)

## Question
Is the matched-start K=8 localized state sufficiently stationary to support a meaningful internal Hessian classification, and does its tested internal spectrum contain a robust negative mode?

## Coordinate chart
The same N=14, K=8, Gaussian-tube, adiabatic Poisson curve–field model used by ELEC-003A. Centre-of-mass subtraction gauge-fixes translation, so this test does **not** count three translational zero modes. Finite-grid anisotropy also prevents an exact rotational-zero-mode claim.

## Computation
1. Load the exact ELEC-003A K=8 state.
2. Compute a central finite-difference gradient in all 97 coordinates.
3. Construct a deterministic 20-dimensional internal subspace containing the radius direction, gradient direction, low-harmonic block directions, and seeded orthogonal complements.
4. Compute the central finite-difference projected Hessian.
5. Re-evaluate the six softest projected directions at three step sizes.

## Bars
- **B1 Reference integrity:** linked and localized.
- **B2 Stationarity:** `||grad E|| / E < 0.10`.
- **B3 Robust nonnegative floor:** no negative curvature beyond tolerance, including independent step checks.
- **B4 No significant projected negative mode.**
- **B5 Positive projected internal gap above numerical zero tolerance.**

A failure of B2 blocks a physical Hessian interpretation even if some spectral bars pass.
