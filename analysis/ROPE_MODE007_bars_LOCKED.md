# ROPE-MODE-007 locked bars

The purpose of this benchmark is to test whether the low-mode spectral shift follows linked versus unlinked status across multiple independent local surgeries, rather than the details of a particular deformation.

- **B1 — topology and geometry controls:** the reference remains certified linked; all six controls are numerically unlinked, preserve minimum separation `>= 0.060`, and remain within the locked geometry-matching tolerances.
- **B2 — boundary leakage:** maximum outer-shell probability across all controls and four modes is `< 0.001` on the larger domain.
- **B3 — domain convergence:** worst relative excitation-gap drift from box half-width 4 to 5 is `< 0.01`.
- **B4 — universal sign consistency:** each of the three excited-mode linked-minus-unlinked contrasts has the same sign for all six surgeries.
- **B5 — significance consistency:** each excited mode exceeds three times combined domain uncertainty in at least five of six surgeries.
- **B6 — domain stability:** each excited-mode contrast retains sign and approximate magnitude from box 4 to box 5 in at least five of six surgeries.
- **B7 — weak nuisance correlations:** no tested nuisance metric has absolute Pearson correlation `>= 0.70` with any excited-mode contrast. With only six surgeries this is a conservative isolation gate, not a definitive causal test.

The topology-only interpretation passes only if all seven bars pass.
