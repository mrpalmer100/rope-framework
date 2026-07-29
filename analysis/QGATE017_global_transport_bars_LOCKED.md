# QGATE-017 — Global transport / Born-relaxation correlation: bars locked before data

**Locked:** 2026-07-29, before executing the registered benchmark.

## Question

Does global cell-to-cell transport explain the nonmonotonic Born-relaxation strength in QGATE-015 better than the local trajectory-separation diagnostic of QGATE-016?

## Protocol

- Reuse exactly the QGATE-015 nested mode families `M = 1, 2, 4, 8, 16, 32, 64` and seeds `17, 29, 43`.
- Reuse total time `T=4`, 1,200 midpoint steps, hard-wall reflection, the same mode pool, coefficient streams, and ground-state launch density.
- Launch 1,000 trajectories for each seed/mode state.
- Partition the box into a fixed `10 x 10` grid and sample cell membership every 20 integration steps.
- Aggregate lag-one cell transitions into a count matrix `C_ij` and row-normalize it to `P_ij` on visited origin cells.
- Record three direct global-transport diagnostics:
  1. **Normalized transition entropy**: occupancy-weighted `H(J|I)/ln(N_active)`, zero for deterministic self-cell motion and larger when each origin distributes trajectories broadly.
  2. **Cross-cell fraction**: fraction of sampled transitions with destination cell different from origin cell.
  3. **Transfer spectral gap**: `1 - |lambda_2|` of the empirical row-stochastic operator restricted to its largest recurrent communicating component. This is an empirical finite-grid mixing diagnostic, not a continuum theorem.
- Correlate each diagnostic with the already-recorded QGATE-015 H and L1 reductions over all 21 seed/mode runs.

## Pre-committed bars

1. **Stationary control:** one-mode medians must satisfy transition entropy `< 0.02`, cross-cell fraction `< 0.02`, and spectral gap `< 0.02`.
2. **Multimode transport:** at least five of six multimode families must exceed the one-mode median transition entropy by `0.05` and cross-cell fraction by `0.05`.
3. **Relaxation association:** pooled Spearman correlation between transition entropy and H reduction must exceed `+0.30`.
4. **Independent meter:** pooled Spearman correlation between transition entropy and L1 reduction must exceed `+0.30`.
5. **Global-over-local test:** at least one global diagnostic must correlate with H reduction more strongly in absolute value than QGATE-016's FTLE correlation `0.573`.
6. **Spectral corroboration:** the empirical spectral gap must correlate positively (`rho > 0`) with H reduction. Failure is retained because a finite-grid, time-aggregated operator may not be the right transport representation.

## Interpretation locked before data

- Passing bars 1–5 supports the limited statement that global cell-to-cell transport is a better predictor of coarse-grained Born relaxation than local pair separation in this tested family.
- Passing bars 1–4 but failing bar 5 means global transport accompanies relaxation without yet resolving the controlling variable.
- Failure of the spectral bar alone does not erase transport evidence; it diagnoses the limitations of a time-aggregated finite-grid transfer operator.
- No outcome proves causality, universal attraction to Born equilibrium, or a rope-level derivation of the guidance law.
