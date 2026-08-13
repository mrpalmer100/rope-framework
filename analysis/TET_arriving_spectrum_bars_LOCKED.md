# COMMISSION TET -- THE ARRIVING-WAVENUMBER SPECTRUM: BARS, LOCKED BEFORE COMPUTING

Locked 2026-08-12, before any number is computed. The computation four
sealed demands converge on, run under the fresh GRANT-THRESHOLD
(FND-080): g = [0.395, 0.460] is now FIXED, so every confrontation
below is parameter-free once a spectrum is chosen -- which is why the
spectrum enumeration must be closed here, first.

## The four sealed demands (quoted per FND-079's requirement)

D1 (FND-074): the reconnection window family [0.082, 0.265] x ka must
   contain the granted g.
D2 (FND-075 robust): effective ka in [2.19, 2.38] for the C4 mesoscopic
   landing robust across both density readings.
D3 (FND-075 any-landing): effective ka in [1.8, 2.9]; outside converts
   C4 to a clean miss, by FND-075's own pre-registered statement.
D4 (NUC-030/FND-071, DATA-SIDE): the effective reconnection probability
   p_eff must land in the sealed band [8.3e-4, 8.6e-3], priced from the
   measured v0 before any of this machinery existed. D4 is the
   discriminator with external teeth: a spectrum failing D4 beyond L1
   is EXCLUDED as a spectrum, because v0 is data.

## Method, fixed at lock

For each locked spectrum, compute p_eff(g) = <p(g, ka)> over the
spectrum's weight, exactly (FND-072's closed form, no small-x
approximation), across the granted g band. Confront: (i) p_eff vs D4's
band; (ii) g_C4 = 1/(2 p_eff) and 1/(3 p_eff) vs the sealed mesoscopic
range [82.6, 108.0] (regenerated from the seal procedure at run time);
(iii) the effective ka (exact inversion of p_eff at each g) vs D2/D3.
D1 is implied by D4 + the granted g and is checked for the record.

## The spectrum enumeration, CLOSED AT LOCK

S1 SEGMENT FUNDAMENTAL: all weight at ka = pi (FND-REL-005's registered
   hard-pinning harmonics, lowest mode; QOPH's R1).
S2 STEP-KINK ON SEGMENT HARMONICS: a topological displacement step
   (the generic kink class; the KIN machinery registers kinks as the
   athermal drivers, FND-071) decomposed on the pinned harmonics
   k_n = n pi / a with the step's universal weight |c_n|^2 ~ 1/n^2;
   p_eff = sum n^-2 p(g, n pi) / sum n^-2, exact form summed.
S3 TRANSIT (incumbent): all weight at ka = 1 (FND-071's attempt
   kinematics). Carried, not privileged.
S4 KINK CONTINUUM (unpinned reading): Lorentzian displacement spectrum
   rho(k) ~ 1/(k^2 + kappa^2), kappa = 1/w_vac = 1.594/a, on the free
   strand -- the reading in which crossings do NOT pin the arriving
   modes. Closed-form average.
No spectrum outside S1-S4 may be introduced after lock. The choice
between the pinned (S1/S2) and unpinned (S4) readings is physical
(does the crossing's own pinning shape what arrives?) and is NOT made
here: all are evaluated and D4 adjudicates with data.

## Guard disclosures

G1: pre-lock scoping estimated the outcomes at order level (S3 and S4
    high in p_eff; S1/S2 near the sealed band; the mesoscopic landing
    strained). Disclosed. The grammar below was written before the
    benchmark, and the seal-tool target is regenerated at run time.
G2: the kink profile forms in S2/S4 are GENERIC CLASSES (step and
    Lorentzian), not claim-specific registered profiles; a verbatim
    sweep of the FND-KIN family for a registered profile is OWED and
    named as a follow-up. If a registered profile exists and differs,
    re-solve is owed, exactly as EM-RECON-018's precedent.
G3: disclosed-target integrity as in RESH/MEM.

## Verdict grammar, pre-committed

Per spectrum: D4-EXCLUDED (p_eff outside the sealed band beyond L1);
D4-MARGINAL (outside within L1); D4-PASS (inside).
Overall:
- CHAIN-CLOSES + C4-LANDS: some D4-PASS spectrum also lands g_C4 in the
  sealed mesoscopic range at either density reading (robust if both).
- CHAIN-CLOSES + C4-MISSES: at least one D4-PASS spectrum exists (the
  granted g reproduces the nuclear v0 window through derived spectra --
  the reconnection chain closes end-to-end, conditional on grant +
  spectrum class), but no D4-PASS spectrum lands g_C4; C4 converts per
  D3's pre-registered statement, and FND-044's residual stands with a
  fourth evaluated miss.
- CHAIN-BREAKS: no spectrum passes D4; the grant's exposure fires and
  FND-080 returns to adjudication.

## Adverse outcomes pre-authorized

All three, including the one that fires the day-old grant. No rescue,
no re-weighting after numbers, no spectrum added post hoc.

## Deliverables

benchmarks/foundations/tet_arriving_spectrum.py;
analysis/TET_arriving_spectrum_results.md; claim via tools/add_claim.py;
annotations to FND-080, FND-075, FND-074, NUC-030, FND-044, FND-051.
