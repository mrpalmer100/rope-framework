# ELEC-008 locked bars — adaptive direct-curve representation

1. Final topology certificate passes at 128/256/512 polygonal samples: `d_min >= 0.060`, `||Lk|-1| <= 0.03`, inter-resolution distance agreement <= 0.01, and linking agreement <= 0.02.
2. Final physical energy is below the campaign's initial physical energy by at least `1e-5`.
3. Every accepted optimization state remains inside the hard certified linked sector.
4. Every adaptive remesh remains certified and changes physical energy by less than 1.5%.
5. At least eight constrained line-search steps are accepted across the refinement stages.
6. Final projected physical-gradient ratio is below 0.05.

The Poisson curve-field physical energy, hard separation floor, and linking tolerances are unchanged. No bending, twist, or curvature term is introduced.
