# ELEC-003A — Matched-start basis convergence

## Question
Was ELEC-003's independent-start K=4→5 radius miss caused by incomplete optimization / basin mismatch, or by persistent high-frequency instability?

## Locked protocol
1. Relax one K=4 configuration for 220 optimization iterations.
2. Project that exact coefficient vector into K=5, K=6, and K=8 by zero-padding newly admitted Fourier coefficients; add no new perturbation.
3. At each stage, run the same 220-iteration optimizer, same N=14 grid, a=0.24 tube width, common Poisson curve-field energy, topology guard, and numerical tolerances.
4. Record total energy, R_rms, linking number, accepted updates, and per-mode coefficient amplitudes.

## Locked bars
- B1: topology, monotone descent, and finite localization persist at every K.
- B2: final energy is non-increasing along the matched K=4→5→6→8 sequence.
- B3: K=6 and K=8 radii differ by <10%.
- B4: the two highest K=8 mode amplitudes are each <25% of the largest low-mode amplitude.

## Outcome
All four bars passed. The matched radii were 0.607733, 0.602846, 0.591627, and 0.593648 for K=4,5,6,8. Adjacent shifts were 0.81%, 1.88%, and 0.34%. Final energies decreased from 16.621601 to 16.284581. At K=8 the two newly highest modes had amplitudes 0.0047 and 0.0055, only 1.10% of the largest low-mode scale.

## Interpretation
The ELEC-003 K=4→5 failure was numerical: independent starts and shorter optimization sampled unequal states. Under exact matched projection and longer optimization, practical Fourier-basis convergence is recovered. This remains a finite-grid, reduced-curve-basis result—not a continuum theorem or electron identification.
