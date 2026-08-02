# ELEC-007 results — augmented-Lagrangian / SQP-style constrained search

## Protocol

ELEC-007 starts from the actually executed continuation state saved by ELEC-006 (`E=16.152913943`). The physical Poisson curve-field objective and K=8 Fourier representation are unchanged. The new solver adds:

- a buffered separation inequality with target `d_min >= 0.066`;
- a Powell-Hestenes-Rockafellar augmented-Lagrangian multiplier update;
- an SQP-style linearized tangent correction near the active separation constraint;
- trust-region control and Armijo merit-function backtracking;
- hard pathwise topology certification at 128 samples;
- adaptive accepted-endpoint certification at 128, 256, and 512 samples.

The hard feasibility floor remains `d_min >= 0.060`; the buffered target is an optimization constraint, not a change to the physical energy.

## Observed run

Five constrained steps were accepted.

| quantity | start | final |
|---|---:|---:|
| physical energy | 16.152913943 | 16.137416994 |
| RMS radius | 0.583045 | 0.581394 |
| adaptive minimum separation | 0.06579395 | 0.06578210 |
| Gauss linking, 128 samples | — | -1.00763139 |
| Gauss linking, 256 samples | — | -1.00386185 |
| Gauss linking, 512 samples | -1.00201217 | -1.00194220 |
| projected augmented-Lagrangian gradient / energy | — | 0.2597405 |
| final multiplier | 0 | 0.0545076 |
| penalty parameter | 50 | 50 |

Physical energy fell by `0.015496949` (`0.09594%`). Every accepted path and endpoint remained in the certified unit-linked sector.

## Locked-bar adjudication

- B1 final 128/256/512 certificate: **PASS**
- B2 physical energy decreases: **PASS**
- B3 all accepted states remain certified: **PASS**
- B4 constrained stationarity below 0.05: **FAIL**
- B5 three-level certificate agreement: **PASS**

## Finding

**AUGLAG_CERTIFIED_DESCENT_NOT_STATIONARY**

The augmented-Lagrangian/SQP-style method preserves topology and continues to lower the unchanged physical energy, but the constrained residual remains `0.2597405`, more than five times the locked stationarity ceiling. This is lower than the immediately preceding ELEC-006 continuation residual (`0.2709513`) but is not close enough to support a stationary-soliton or Hessian claim.

The result is a kept negative result. It does not prove nonexistence of a linked stationary state. It does show that changing from projected L-BFGS descent to a buffered augmented-Lagrangian/SQP-style treatment, while adding 512-point endpoint certification, does not by itself resolve the stationarity debt in the current K=8 Fourier representation.

## Next-order decision

Further repetitions of the same finite-dimensional representation are now low-value. The clean next controlled change is to replace the global K=8 Fourier chart with direct periodic spline or polygonal degrees of freedom plus adaptive remeshing, while retaining the same physical objective and hard topology certificates. Only after representation independence should a curvature or twist stabilizer be introduced.
