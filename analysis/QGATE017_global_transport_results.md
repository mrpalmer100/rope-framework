# QGATE-017 — Global transport results

The preregistered 10x10 cell-transition campaign was run over the same 21 seed/mode states as QGATE-015 and QGATE-016.

## Median transport diagnostics by mode count

| Modes | Transition entropy | Cross-cell fraction | Spectral gap | H reduction | L1 reduction |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.000 | 0.000 | 0.000 | 0.0% | 0.0% |
| 2 | 0.186 | 0.361 | 0.033 | 55.5% | 20.7% |
| 4 | 0.548 | 0.856 | 0.099 | 76.2% | 52.6% |
| 8 | 0.591 | 0.880 | 0.152 | 87.1% | 66.2% |
| 16 | 0.713 | 0.944 | 0.270 | 85.0% | 64.0% |
| 32 | 0.758 | 0.947 | 0.239 | 87.9% | 65.7% |
| 64 | 0.768 | 0.917 | 0.207 | 68.3% | 56.6% |

## Pooled rank correlations across all 21 runs

- Transition entropy vs H reduction: **Spearman +0.615**
- Transition entropy vs L1 reduction: **Spearman +0.680**
- Cross-cell fraction vs H reduction: **Spearman +0.782**
- Cross-cell fraction vs L1 reduction: **Spearman +0.806**
- Spectral gap vs H reduction: **Spearman +0.767**
- Spectral gap vs L1 reduction: **Spearman +0.782**

For comparison, QGATE-016's local finite-separation exponent correlated with H reduction at **+0.573**. Both cross-cell transport and the empirical transfer gap outperform that local-chaos diagnostic.

## Locked-bar verdict

All six preregistered bars pass:

1. The stationary one-mode control has exactly zero entropy, cross-cell motion, and spectral gap.
2. All six multimode families exceed the control transport thresholds.
3. Transition entropy correlates positively with H reduction.
4. Transition entropy independently correlates with L1 reduction.
5. Global transport outperforms the QGATE-016 FTLE correlation.
6. The empirical spectral gap positively corroborates H relaxation.

## Interpretation

The result supports the limited statement that **global transport through configuration space predicts coarse-grained Born relaxation better than local trajectory separation in this tested family**. The 64-mode case is especially diagnostic: it has the largest local FTLE but reduced endpoint relaxation, while its cross-cell fraction and transfer gap also fall from their 16–32-mode maxima. This resolves the nonmonotonicity in the direction predicted by a global-mixing mechanism.

The result does not establish causality, universal attraction, or a rope-level derivation of the guidance law. The transition operator is finite-grid and time-aggregated; grid-resolution, lag-time, independent phase ensembles, and nodal-encounter robustness remain next-order tests.
