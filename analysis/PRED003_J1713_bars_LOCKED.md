# The J1713+0747 lineage: locked bars

## Scope, stated honestly before starting
Re-timing the pulsar is NOT possible here: it requires raw TOAs, TEMPO2/PINT,
and years of noise modelling that the published analyses already performed.
What IS possible, and what PRED-003-META identified as the decisive question,
is a lineage analysis: are the three published Gdot/G values from this system
mutually consistent, what systematic does their spread imply, and what must
the next analysis deliver to decide PRED-003?

## Data (95% CL as published; halved to 1 sigma)
L1 Zhu et al. 2015 (21-yr NANOGrav):        -0.6(0.55)e-12 /yr
L2 Zhu et al. 2019 (MNRAS 482, 3249):       -0.1(0.45)e-12 /yr
L3 2025 (arXiv 2507.18188, EPTA DR2,
   J1713+0747 + J0437-4715 combined):       +0.32(0.155)e-12 /yr

## THE STATISTICAL POINT, fixed before computing
These analyses are NESTED, not independent: each uses a superset of the
earlier data. PRED-003-META described the spread as "exceeding the latest
quoted error", which applied an INDEPENDENT-sample intuition and is the wrong
test. For nested data the expected shift between analyses is
sqrt(sigma_old^2 - sigma_new^2), NOT sqrt(sigma_old^2 + sigma_new^2). B1 must
apply the correct test and correct the earlier characterization if it was
wrong.

## Locked bars
B1 NESTED CONSISTENCY: pairwise shifts against sqrt(sigma_old^2 - sigma_new^2).
   Report whether the lineage is statistically normal. CORRECT PRED-003-META
   explicitly if this overturns its "sign flipped twice" framing.
B2 THE KNOWN SYSTEMATIC: the April 2021 profile-change event disrupted this
   pulsar's timing stability (mitigation work still being published, July 2026),
   and an earlier event occurred in 2016. State how this bears on the Gdot
   measurement and whether it is an argument for or against trusting L3.
B3 THE DECISION FORECAST: compute the sigma the next analysis needs for a 3
   sigma detection at L3's central value, and estimate when timing baseline
   growth delivers it, using the Pbdot ~ T^(-5/2) scaling calibrated on the
   observed L2 -> L3 improvement.
B4 THE VERDICT FOR PRED-003, stated either way.
