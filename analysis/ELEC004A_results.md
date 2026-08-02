# ELEC-004A — Linear-stability results

## Outcome: FAILED, KEPT — reference state is not stationary enough

The ELEC-003A K=8 state remains linked and localized:

- `E = 16.284581491`
- `R_rms = 0.593648`
- `|Lk| = 0.831834`

However, the full 97-coordinate finite-difference gradient has

- `||grad E|| = 6.10289`
- `||grad E|| / E = 0.374765`

which is far above the locked 0.10 stationarity ceiling. Therefore the state produced by the stochastic monotone optimizer is a low-energy localized configuration, but not a sufficiently converged stationary point for a valid Hessian stability claim.

The 20-dimensional projected Hessian returned one nominal negative eigenvalue (`-16.6974`), but direct curvature checks along that eigenvector at three independent step sizes were positive (`27.3238`, `26.9753`, `13.0030`). This disagreement is exactly what is expected when the expansion point has a large residual gradient and finite-difference mixed derivatives are contaminated by nonquadratic drift. It is **not** registered as a physical instability.

## Locked bars

- B1 linked/localized reference: **PASS**
- B2 near-stationary gradient: **FAIL**
- B3 no robust negative mode: **FAIL / inconclusive**
- B4 projected spectrum nonnegative: **FAIL / inconclusive**
- B5 finite positive projected gap: **PASS** (`4.53269`)

## Interpretation
ELEC-004A cannot yet adjudicate linear stability. The failure identifies a precise optimization debt: ELEC-003A established practical basis convergence in energy and radius, but its stochastic optimizer did not drive the 97-dimensional gradient near zero.

## Required next order
Run **ELEC-004A-R**, a deterministic stationarity repair:

1. start from the saved K=8 state;
2. switch from SPSA-style stochastic descent to an explicit finite-difference gradient optimizer such as L-BFGS-B;
3. preserve the topology guard;
4. require `||grad E||/E < 0.02` before recomputing the Hessian;
5. only then classify negative, zero, and positive modes.
