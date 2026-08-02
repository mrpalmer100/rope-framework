# ELEC-002 — Self-consistent curve–field localization gate

## Question

Does the same curve–field energy functional that gives the sourced Hopf-radius
minimum also support a finite, topologically charged attractor when the curve
and its Poisson field are evolved self-consistently?

This is an existence and consistency test only. It does not identify the
configuration with the physical electron.

## Protocol

For every trial curve, the benchmark rebuilds a Gaussian tube source on a 3-D
grid, solves Poisson's equation for the field, and evaluates one common energy:

`E[C,psi] = T0 L[C] + (kappa/2) integral |grad psi|^2 dV`.

The field is minimized exactly for each curve update, while the curve descends
in a finite Fourier basis. Proposed steps are accepted only when this common
energy falls and the initial linking sector is preserved.

## Bars locked before data

1. **Topology:** all five perturbed candidates finish with `||Lk|-1| < 0.20`.
2. **Common-action descent:** energy falls by more than 5% in every trial and
   accepted energy histories are monotone.
3. **Localization:** every final combined RMS radius lies in `0.4 < R_rms < 2.0`.
4. **Common attractor:** final-radius coefficient of variation is below 15%.
5. **Control:** an initially unlinked pair remains `|Lk| < 0.15` under the same
   numerical protocol.

## Result

| Bar | Result |
|---|---|
| B1 topology | PASS: `|Lk| = 0.801–1.192` |
| B2 common energy | PASS: `9.2–16.1%` reduction, monotone |
| B3 localization | PASS: `R_rms = 0.621–0.670` |
| B4 common attractor | PASS: radius CV `3.20%` |
| B5 unlink control | PASS: `|Lk| = 0.0000` |

## Interpretation

Within the registered grid and reduced Fourier basis, the common Poisson
curve–field functional supports a finite localized attractor in the unit-linked
sector. This resolves ELEC-001's specific inconsistency: the expanded attractor
was a property of the pairwise flexible-curve proxy, not of the sourced-field
functional when used consistently for both statics and dynamics.

## Boundaries

The result is **Modeled**, not Derived. It is limited by grid resolution,
Gaussian tube regularization, adiabatic field relaxation, and a finite Fourier
basis. It does not yet establish unrestricted 3-D stability, relativistic
propagation, spin-1/2 behavior, electric charge normalization, electron mass,
or magnetic moment.

The next gate should be **ELEC-003: full-resolution stability and basis/grid
convergence**, including out-of-basis perturbations and a post-convergence
re-perturbation test.
