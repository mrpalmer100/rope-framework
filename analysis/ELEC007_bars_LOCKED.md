# ELEC-007 locked bars — augmented-Lagrangian constrained search

The bars below were fixed before adjudicating the completed ELEC-007 run.

1. **Three-level topology certificate:** the final state passes exact polygonal minimum-separation and Gauss-linking checks at 128, 256, and 512 samples, with `d_min >= 0.060`, `||Lk|-1| <= 0.03`, adjacent linking estimates agreeing within 0.02, and adjacent distance estimates within 0.01.
2. **Physical descent:** final physical energy is at least `1e-5` below the starting physical energy.
3. **Certified accepted trajectory:** every accepted state retains `d_min >= 0.060` and `||Lk|-1| <= 0.03`; every line-search path is checked at 128 samples and every accepted endpoint at 128/256/512 samples.
4. **Constrained stationarity:** the bound- and active-constraint-projected augmented-Lagrangian gradient obeys `||P grad L|| / |E| < 0.05`.
5. **Adaptive-resolution agreement:** the final 128/256/512 topology diagnostics satisfy the agreement limits in bar 1.

No Hessian or particle-property interpretation is permitted unless all five bars pass.
