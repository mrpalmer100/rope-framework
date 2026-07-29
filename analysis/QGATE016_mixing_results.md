# QGATE-016 — Direct trajectory instability versus Born relaxation

## Locked question

Does a finite-time trajectory-divergence measure explain the strength of coarse-grained Born relaxation in the QGATE-015 mode-count family better than raw mode count?

The protocol and five bars were written to `analysis/QGATE016_mixing_bars_LOCKED.md` before execution.

## Results

| Modes | Median finite-time exponent |
|---:|---:|
| 1 | ~0.000 |
| 2 | 3.839 |
| 4 | 6.212 |
| 8 | 9.752 |
| 16 | 21.478 |
| 32 | 47.674 |
| 64 | 91.101 |

Pooled across all 21 seed/mode runs:

- Spearman(`lambda_FT`, H reduction) = **+0.573**.
- Spearman(`lambda_FT`, L1 reduction) = **+0.639**.
- Spearman(`log2 M`, H reduction) = **+0.606**.
- All six multimode families have median `lambda_FT` more than 0.05 above the stationary control.

## Locked-bar outcome

1. Integrable control near zero: **PASS**.
2. At least five multimode families unstable: **PASS (6/6)**.
3. FTLE-H correlation above +0.30: **PASS**.
4. FTLE-L1 correlation above +0.30: **PASS**.
5. FTLE explains H reduction better than raw mode count: **FAIL** (`0.573 < 0.606`).

The benchmark is green because it mechanically reproduces this preregistered outcome vector, including the failed fifth bar; it does not rewrite the bar after seeing the result.

## Interpretation

The direct trajectory-instability measure cleanly separates the stationary control from every multimode flow and is positively associated with both relaxation meters. However, it does not explain the nonmonotonic relaxation pattern better than mode count. In particular, the 64-mode cases have the largest local separation exponents while relaxing less strongly than the 8–32-mode cases.

Therefore local exponential separation is **associated with** Born relaxation but is **not sufficient to control its strength** in this family. The next direct observable should be global transport rather than local instability: nodal encounter rate, cell-to-cell transition entropy, or a mixing matrix/spectral-gap measure.

## Numerical scope

The reported quantity is a finite-separation, finite-time diagnostic under the implemented clipped guidance field and periodic renormalization. A small convergence check preserved the ordering but showed that absolute exponent magnitudes shift with timestep, especially at lower multimode counts. The claim is therefore about control separation and rank association, not continuum-accurate absolute Lyapunov values.
