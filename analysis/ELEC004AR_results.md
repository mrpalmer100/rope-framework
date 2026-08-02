# ELEC-004A-R results

The deterministic repair did **not** reach a stationary linked state. The first accepted L-BFGS-B step lowered the physical energy but left the linked topological basin.

| Quantity | Start | After first accepted step |
|---|---:|---:|
| Physical energy | 16.284581491 | 16.245606456 |
| RMS radius | 0.593648 | 0.589354 |
| `|Lk|` | 0.831834 | 0.141802 |
| Relative gradient | 0.377383 | 0.427763 |

The final relative-gradient checks were stable across the smaller stencil:

- h=5e-5: 0.4277627
- h=1e-4: 0.4277625
- h=2e-4: 0.4277627

## Locked bars
- B1 linked/localized basin retention: **FAIL** — localization remains, but `|Lk|` collapses to 0.142.
- B2 physical-energy nonincrease: **PASS**.
- B3 relative gradient below 0.02: **FAIL**.
- B4 step-robust relative gradient below 0.03: **FAIL**.

## Interpretation
The ELEC-003A configuration is not merely an incompletely optimized minimum that can be repaired by ordinary deterministic descent. In the present discretized coordinate chart, the lower-energy direction immediately points out of the linked sector. A short-range inter-strand separation barrier did not preserve the numerical linking invariant, indicating that the current topology protection is inadequate (and possibly that the coarse linking estimator/curve sampling is too fragile near the almost-touching strands).

This does **not** prove that no linked stationary solution exists. It shows that the current candidate is not demonstrably a local minimum of the unconstrained common energy. The next-order problem is therefore a genuinely topology-preserving variational formulation—e.g. a certified non-crossing constraint, higher curve resolution, and a constrained optimizer—rather than another unconstrained Hessian calculation.
