# PRED-003 widened confrontation — locked bars (before any combination)

## Commission
The first confrontation used one measurement per side. This widens to every
independent determination retrievable, tests whether each family is internally
consistent, and re-runs the relation against the combination.

## Data logged before computing (retrieved 2026-08-01)
ALPHA-DOT/ALPHA (per yr):
 A1 1.0(1.1)e-18   Yb+ E3/E2, PTB (Filzinger et al. 2023)  [tightest]
 A2 1.8(2.5)e-19   same programme, supplemental linear-drift fit
 A3 -1.7(2.5)e-17  Al+/Hg+ (Rosenband et al., revised sensitivity)
 A4 -5.8(6.9)e-17  Dy (Leefer et al.)
 A5 7.2(4.7)e-17   Yb+/Cs (Godun et al. 2014)
 A6 -0.7(2.1)e-17  Godun et al. 2014 combination [OVERLAPS A3-A5: excluded
                   from the combination to avoid double counting]
GDOT/G (per yr; 95% CL values halved to 1 sigma where the source states 95%):
 G1 7.1(7.6)e-14   LLR, Hofmann & Muller 2018
 G2 4(9)e-13       LLR, Williams, Turyshev & Boggs 2004 [supersedes into G1's
                   lineage: reported, excluded from the combination]
 G3 -0.6(0.55)e-12 PSR J1713+0747, Zhu et al. 2015 (95% -> 1 sigma)
 G4 -0.1(0.45)e-12 PSR J1713+0747, Zhu et al. 2019 (95% -> 1 sigma)
 G5 0.32(0.155)e-12 PSR J1713+0747 + J0437-4715, 2025 (95% -> 1 sigma)
 G6 -7(12)e-12     PSR J1738+0333 (95% -> 1 sigma)
 NOTE, fixed here: G3, G4 and G5 share the SAME pulsar and are NOT independent.
 The combination uses G5 (latest) as the pulsar representative and reports the
 others as a lineage consistency check.

## Locked bars
B1 INTERNAL CONSISTENCY of each family, by chi-square against a common mean.
   If a family is internally inconsistent, say so and do not combine it
   silently.
B2 THE COMBINATION: inverse-variance weighted means of the independent
   subsets, with the overlap exclusions above applied as stated.
B3 THE TEST re-run on the combination, per method and combined.
B4 THE 2025 PULSAR CENTRAL VALUE. G5 sits ~2 sigma from zero. Compute what the
   relation implies for alpha-dot IF that central value is real, and report the
   resulting tension against the clock bound. THIS MUST BE REPORTED WHETHER OR
   NOT IT IS UNFAVOURABLE.
B5 HONESTY: the same null-vs-null caveat applies to the combination. State
   which measurement is doing the work and what would change the verdict.
