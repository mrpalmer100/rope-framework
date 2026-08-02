# ELEC-005 — Topology-Preserving Constrained Variational Solver (Locked Bars)

## Question
Can the common Poisson curve–field energy be descended while remaining inside a numerically certified linked manifold, and does that constrained descent reach first-order stationarity?

## Protocol
- Begin from the saved ELEC-003A K=8 state.
- Re-evaluate topology using a 128-vertex polygonal representation rather than the original 24-point diagnostic.
- If the saved state is not certified, retract its nonzero Fourier coefficients continuously toward the canonical Hopf link until both constraints are met.
- Require exact polygonal inter-component segment separation `d_min >= 0.06`.
- Require the high-resolution discrete Gauss integral to satisfy `||Lk|-1| <= 0.03`.
- Use an explicit central finite-difference energy gradient.
- Apply box projection and a trust-region/backtracking line search.
- Numerically certify the full proposed path at interpolation points before accepting any energy-descending step.

## Locked bars
1. **Diagnostic:** the saved K=8 state is independently classified by the higher-resolution certificate.
2. **Topology preservation:** every accepted state remains within the certified linked manifold.
3. **Variational descent:** physical energy decreases from the certified starting state.
4. **Projected stationarity:** final projected-gradient ratio is below 0.05.
5. **Line-search certification:** every accepted step passes separation and linking checks along its sampled path.

This is a finite-resolution numerical certificate, not a continuum proof of topology preservation.
