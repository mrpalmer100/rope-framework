# ELEC-051 — The lattice-width literature adjudication: locked bars (before computation)

## Commission
ELEC-050 predicted the flux-tube width R_pred = 0.342 fm (uniform-density
cylinder radius from Sigma = T_tube/(pi R^2)) against the corpus band
0.35-0.5 fm, and named a literature reading as the free adjudicator. The
reading is done (2026-07-31); the sources and the conversion are computed here.

## Sources logged (B1, fixed before computation)
S1. Baker, Cea, Chelnokov, Cosmai, Papa, EPJ C 85, 29 (2025) [2409.20168]:
    FULL QCD, 2+1 HISQ at physical masses. Width w ~ 0.5 fm by the definition
    w = sqrt(int x^2 E dx / int E dx) (E-weighted RMS), constant over
    d = 0.5-1.06 fm; sqrt(sigma_eff) ~ 0.4 GeV; fitted profile
    E ~ E3 + E8 with E3 ~ sech^2(sqrt(gH0/2) x), E8 ~ (sqrt3/2a) sech^2(a sqrt(gH0)/2 x),
    sqrt(gH0) ~ 1.0 GeV, alpha ~ 1.
S2. Verzichelli et al., PoS LATTICE2025 [2603.05323] + [2601.19520]:
    (2+1)d SU(2). INTRINSIC (exponential-tail) width lambda sqrt(sigma) =
    0.244(4) -> lambda ~ 0.109 fm at QCD sqrt(sigma) = 0.44 GeV. Different
    theory and different definition; logged for the definition spread, not
    for adjudication.
S3. Clem-fit penetration lengths in SU(3) pure gauge (Cea et al. 2012/2017,
    Baker et al. 2019): lambda ~ 0.17-0.19 fm. Definition: exponential decay
    scale, not RMS.

## Locked bars
B2 (the conversion instrument). From S1's fitted profile (both Abelian
   components, sqrt(gH0) = 1.0 GeV, alpha = 1), compute numerically:
   (i) the E-weighted RMS width w_E; VALIDATION: it must land within 25% of
   the paper's ~0.5 fm or the profile reconstruction is wrong and the
   adjudication is void;
   (ii) the ENERGY-weighted (E^2) uniform-equivalent radius
   R_eq = sqrt(2 <x^2>_{E^2}) -- the quantity NUCQ-003's mass-density
   n = 3 pi (R/a)^2 actually requires.

B3 (THE ADJUDICATION). Compare R_eq to R_pred = 0.342 fm and to the corpus
   band 0.35-0.5 fm. Verdicts available: SUPPORTS (within ~15%), CONSISTENT
   (within the band), TENSION (outside the band). Whatever it is, quote it
   with the conversion's model-dependence stated.

B4 (registry update). Restate the T0 band at the adjudicated width and file
   the modern-literature annotation on NUCQ-003 (superseding the bare
   0.35-0.5 band with the definition-resolved values).

B5 (honesty). The conversion is profile-model dependent (sech^2 assumed;
   Clem would differ), the E8 parameters are approximate (alpha ~ 1 from the
   text, exact Table-4 values not extracted), and S2 is a different gauge
   theory in a different dimension. All three limits stated in the output.
