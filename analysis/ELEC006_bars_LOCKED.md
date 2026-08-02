# ELEC-006 Locked Bars — Extended Certified Constrained Solver

The campaign continues from the final certified ELEC-005 state. The physical energy functional and K=8 parameterization are unchanged.

1. **Adaptive topology certificate:** every accepted endpoint must satisfy `d_min >= 0.06`, `||Lk|-1| <= 0.03`, and agreement between 128- and 256-point polygonal evaluations (`|ΔLk| <= 0.02`, `|Δd_min| <= 0.01`).
2. **Path certification:** every accepted line-search path must remain inside the 128-point certified linked sector, with the endpoint rechecked at 256 points.
3. **Physical descent:** final physical energy must be below the ELEC-005 final energy.
4. **Extended run:** at least 12 accepted constrained steps must be completed using deterministic four-step restarts of the active-projected L-BFGS solver.
5. **Constrained stationarity:** the feasible projected-gradient ratio must satisfy `||P_T ∇E|| / |E| < 0.05`.

No Hessian or particle interpretation is allowed unless all five bars pass.
