# QGATE-016 — Direct trajectory-mixing / Born-relaxation correlation: bars locked before data

**Locked:** 2026-07-29, before executing the registered benchmark.

## Question

Does a direct measure of trajectory instability explain the Born-relaxation strength observed in QGATE-015 better than raw mode count alone?

## Protocol

- Reuse exactly the QGATE-015 nested mode families `M = 1, 2, 4, 8, 16, 32, 64` and seeds `17, 29, 43`.
- Reuse QGATE-015's 1,200-step, total-time `T=4` guidance integration and its recorded endpoint H and L1 reductions.
- For each seed/mode state, launch 256 reference trajectories from the same ground-state density used for the nonequilibrium ensemble.
- Pair each reference trajectory with a displacement of `delta0 = 1e-6` in a seeded random direction.
- Evolve both trajectories with the identical midpoint guidance solver and hard-wall reflection.
- Every 20 integration steps, measure pair separation and renormalize the perturbed trajectory back to `delta0` around its reference partner.
- Define the finite-time trajectory-divergence exponent

  `lambda_FT = (1/T) sum_k ln(delta_k/delta0)`.

  This is a direct finite-separation mixing/instability diagnostic for the implemented flow; it is not claimed to be a rigorous asymptotic Lyapunov exponent of the continuum system.

## Pre-committed bars

1. **Integrable control:** the median one-mode exponent must satisfy `|lambda_FT| < 0.05`.
2. **Multimode instability:** at least five of the six multimode counts must have median `lambda_FT` at least `0.05` above the one-mode median.
3. **Relaxation association:** pooled Spearman correlation across all 21 seed/mode runs between `lambda_FT` and H reduction must exceed `+0.30`.
4. **Independent meter:** pooled Spearman correlation between `lambda_FT` and L1 reduction must exceed `+0.30`.
5. **Explanatory improvement:** the absolute pooled correlation of `lambda_FT` with H reduction must exceed the absolute pooled correlation of `log2(M)` with H reduction.

## Interpretation locked before data

- Passing all bars supports the limited statement that stronger direct trajectory instability is associated with stronger coarse-grained Born relaxation in this tested family.
- Failure of bars 3–5 means FTLE-style local separation is not the controlling variable, even if multimode flows are more unstable than the control; the next candidates would be nodal encounters, global transport entropy, or cell-to-cell mixing.
- No outcome proves causality, universal Born attraction, or a rope-level derivation of the configuration-space guidance law.
