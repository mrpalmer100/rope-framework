# ELEC-005 Results — Certified Constrained Descent, Stationarity Not Yet Reached

The topology-preserving constrained variational pilot was executed from the saved ELEC-003A K=8 state.

## High-resolution diagnosis of the saved state

At 128 polygonal samples per component, the saved state has:

- minimum inter-component segment separation: **0.00916164**
- discrete Gauss linking integral: **0.01203419**

It therefore fails the new linked-manifold certificate. The apparent `|Lk| = 0.831834` at the original 24-point resolution was a coarse-resolution artifact near a strand crossing.

## Certified retraction

The nonzero K=8 Fourier coefficients were continuously retracted toward the canonical Hopf link. The largest certified retained amplitude was:

- homotopy factor `alpha = 0.833076`

The resulting state satisfied the locked separation and linking constraints before constrained descent began.

## Constrained descent

Six finite-difference projected-gradient steps were accepted. Every accepted state passed the numerical path certificate.

- starting physical energy: **16.333202416**
- final physical energy: **16.246060040**
- energy decrease: **0.087142376** (**0.5335%**)
- final RMS radius: **0.601202**
- final minimum segment separation: **0.065854**
- final linking integral: **-1.00631193**
- final projected-gradient ratio: **0.274540**

## Locked bars

- B1 higher-resolution diagnosis performed: **PASS** — the saved state is not certified linked.
- B2 certified linked manifold retained: **PASS**.
- B3 physical energy decreases: **PASS**.
- B4 projected stationarity below 0.05: **FAIL**.
- B5 every accepted state/path certified: **PASS**.

## Finding

**CERTIFIED_DESCENT_NOT_STATIONARY**

The new method successfully prevents the topology loss observed in ELEC-004A-R and permits physical-energy descent inside a numerically certified linked sector. However, the constrained gradient remains large, so a constrained stationary solution has not yet been demonstrated.

The most important new result is diagnostic: the prior saved K=8 candidate was not genuinely linked when evaluated at higher geometric resolution. A valid linked state can be recovered by homotopy retraction, and topology-preserving descent is computationally feasible from that state.

The next campaign should continue this solver with an active-constraint tangent projection or augmented-Lagrangian/SQP method, adaptive curve refinement, and a substantially longer optimization budget. Hessian classification remains premature until the constrained projected-gradient ratio is small.
