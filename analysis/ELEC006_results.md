# ELEC-006 Results — Extended Certified Descent Does Not Reach Stationarity

ELEC-006 extended the topology-preserving solver from ELEC-005 using active-constraint tangent projection, limited-memory BFGS directions, deterministic steepest-descent fallback, adaptive 128/256-point curve certification, and certified Armijo line searches.

## Campaign

The solver was run as three deterministic four-step stages, restarting the quasi-Newton memory between stages while carrying forward the accepted state. This produced **12 accepted constrained steps**, twice the accepted-step depth of ELEC-005.

- campaign starting energy: **16.246060040**
- final energy: **16.172284192**
- total energy decrease: **0.073775848** (**0.4541%**)
- final RMS radius: **0.586069**
- final minimum segment separation: **0.06591359**
- final `Lk` at 128 points: **-1.00676822**
- final `Lk` at 256 points: **-1.00344345**
- final feasible projected-gradient ratio: **0.4362766**

All accepted states remained above the separation floor and in the unit-linked sector. The 128- and 256-point certificates remained mutually consistent.

## Locked bars

- B1 adaptive topology certificate: **PASS**.
- B2 path certification for accepted steps: **PASS**.
- B3 physical energy descent: **PASS**.
- B4 at least 12 accepted constrained steps: **PASS**.
- B5 feasible projected stationarity below 0.05: **FAIL**.

## Finding

**EXTENDED_CERTIFIED_DESCENT_NOT_STATIONARY**

The stronger constrained method preserves topology and continues to lower the physical energy, but the feasible projected-gradient residual does not trend toward zero. It fluctuates between approximately 0.34 and 0.46 and ends at 0.4363, well above the locked 0.05 threshold.

This makes simple optimizer under-running a less plausible explanation for the missing stationary point. Within the tested K=8 representation and current Poisson curve-field functional, the linked configuration continues to possess substantial feasible descent directions even after 12 certified steps.

The result does not prove nonexistence of a linked stationary solution. It does show that active-projected L-BFGS descent, adaptive geometric certification, and a doubled accepted-step campaign do not establish one. The next scientifically productive test should alter the variational representation or functional rather than merely increasing line-search depth: for example, direct polygonal degrees of freedom with remeshing, a smooth thickness/ropelength constraint, or an additional curvature/twist stabilizing term preregistered independently of the observed failure.
