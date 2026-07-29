# QGATE-015 — Born relaxation across mode count

## Registered result
Using three fixed coefficient seeds and a nested energy-ordered sweep over M = 1, 2, 4, 8, 16, 32, 64, the timestep-converged 1,200-step campaign produced:

| Modes | Median H reduction | Median L1 reduction |
|---:|---:|---:|
| 1 | 0.0% | 0.0% |
| 2 | 55.5% | 20.7% |
| 4 | 76.2% | 52.6% |
| 8 | 87.1% | 66.2% |
| 16 | 85.0% | 64.0% |
| 32 | 87.9% | 65.7% |
| 64 | 68.3% | 56.6% |

All five registered bars pass. Six of six multimode counts exceed the 50% median-H threshold; M = 4 through 64 also exceed 50% in median L1. The Spearman correlation between log2(M) and median H reduction is positive but modest (rho = 0.371), because relaxation saturates and then weakens at M=64 rather than increasing monotonically.

## Interpretation
The result strengthens QGATE-014 from a single 16-mode existence demonstration to robustness across a 2-to-64-mode family. It does not show that raw mode count is the sole control parameter. The non-monotonic high-mode behavior points toward flow-specific mixing or chaos measures as the more fundamental predictor.

## Numerical audit
The initial 800-step pilot failed at M=64. A disclosed timestep refinement to 1,200 steps restored strong relaxation for all three M=64 seeds. Therefore the campaign also establishes a numerical requirement: mode-count comparisons must be timestep-converged as the maximum modal frequency rises.
