# ROPE-MODE-001 results — discrete modes, but ordinary string harmonics

The benchmark linearized the simplest constant-tension wave operator on each of the two closed components of the certified ELEC-009 linked geometry. A periodic finite-element stiffness and mass matrix was assembled directly from the nonuniform polygonal arclength mesh. The constant displacement mode was removed, and the nearly degenerate sine/cosine pairs were averaged.

## Numerical result

- Certified reference: `d_min = 0.06195531`, `Lk512 = -1.00225398`.
- Maximum 256→512 frequency change: `0.0775%`.
- Strand 0 paired frequency ratios: `1.000000, 2.000049, 3.000194, 4.000486, 5.000972`.
- Strand 1 paired frequency ratios: `1.000000, 2.000059, 3.000236, 4.000589, 5.001179`.
- Ordinary harmonic fit: `R^2 = 0.99999997`, RMS error `2.29e-4`.
- Best atomic-shell template: `1 - 1/n^2`, `R^2 = 0.45724718`, RMS error `0.823954`.
- Observed scalar multiplicity per harmonic: four (two sine/cosine modes on each of two components).
- Atomic shell capacities for `n=1..5`: `2, 8, 18, 32, 50`.

## Locked bars

- B1 certified linked reference: **PASS**
- B2 mesh-converged frequencies: **PASS**
- B3 ordinary harmonic law: **PASS**
- B4 atomic-shell template beats harmonic law: **FAIL**
- B5 atomic-shell degeneracy reproduced: **FAIL**

## Finding

**DISCRETE_MODES_BUT_ORDINARY_STRING_HARMONICS**

The core standing-wave intuition is partly correct: a closed rope necessarily has a robust discrete normal-mode spectrum. In the present simplest dynamics, however, that spectrum is almost exactly the integer harmonic sequence of a closed string. It does not reproduce hydrogenic shell spacing or atomic shell multiplicities.

This does not exclude a more elaborate atom-scale rope model. It shows that geometry plus constant tension alone is insufficient. Any shell interpretation would require additional dynamics—such as a central interaction, field coupling, rotational/angular structure, nonlinear mode locking, or fermionic degrees of freedom—and those additions must make new quantitative predictions rather than being chosen after the fact.
