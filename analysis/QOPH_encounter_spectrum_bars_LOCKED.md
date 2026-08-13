# COMMISSION QOPH -- THE ENCOUNTER SPECTRUM: BARS, LOCKED BEFORE COMPUTING

Locked 2026-08-12, before any number is computed. Owner of the C3 tension
per FND-073. Chartered from the HANDOFF queue ("also owed: the
encounter-spectrum derivation").

## Question

FND-072's exact form p(g, ka) = g^2/(2(g^2 + 4(ka)^2)) was evaluated at
the single locked scale ka = 1 (FND-071's transit kinematics). The
demanded contrast window [0.082, 0.265] inherits that choice, and FND-073
registered the C3 tension against the survival floor g >= [0.395, 0.460]
as disjoint by 1.49x AT ka = 1. QOPH asks: what encounter scale (or
spectrum) does the REGISTERED structure itself supply, and what does the
demanded window become under it?

## Exact scaling law, fixed at lock (from the closed form, no computation)

At fixed p, x = g/(2ka) is fixed, so g_demanded is EXACTLY linear in ka.
The window under any ka is [0.082, 0.265] x ka. This is algebra on
FND-072's registered form, stated here so route evaluation is arithmetic,
not modeling.

## Route classification, CLOSED AT LOCK (all evaluated, none selected by outcome)

R1: SEGMENT NORMAL MODES. Crossings bound strand segments of length a;
    admissible standing wavenumbers k_n = n pi / a. Characteristic
    encounter scale = the fundamental, ka = pi. Registered basis:
    EM-RECON-025's crossing coupling localizes relative displacement at
    crossings; FND-REL-005's g -> infinity limit pins modes at segment
    harmonics (registered, quoted verbatim from the claim face).
R2: KINK LOCALIZATION WIDTH. The only registered length localizing a
    disturbance transversely on a strand is the strand width;
    vacuum-mesh w/a = 0.6272 (FND-068 convention, EM-RECON-030 re-solve,
    quarantine lifted). Characteristic ka = a/w = 1.594.
R3: TRANSIT KINEMATICS (incumbent). FND-071's attempt scale k = 1/a,
    ka = 1. Carried as the baseline, not privileged.

No route outside R1-R3 may be introduced after lock. If a route cannot
be posed amplitude-free it returns UNDERSPECIFIED for that route
(SCALE-001 discipline; athermality theorem forbids any occupancy weight,
so no thermal spectrum is admissible and equal-weight averaging over
harmonics is REFUSED as an unlocked choice -- each route reports its
characteristic scale only).

## Verdict grammar, pre-committed

- RESOLVED: two or more routes produce a demanded window overlapping the
  survival floor [0.395, 0.460], and no evaluated route excludes overlap
  by more than the L1-class conversion band (factor 3, direction-neutral,
  per FND-029's L1 convention).
- SHARPENED-TENSION: all routes leave the windows disjoint beyond the
  L1 band. NUC-030's adjudication path arms.
- UNDERDETERMINED: routes disagree such that overlap depends on route
  selection. The spread goes on the face; no route is selected; the
  C3 tension remains assigned, with the spread as its new statement.

## Guard disclosures (noticed BEFORE lock, displayed so refusal is auditable)

G1: ka = a/w = 1.594 was noticed pre-lock to move the window's top edge
    to approximately 0.42, adjacent to the survival floor. The route is
    evaluated because it is one of the three registered localization
    scales, NOT because of this adjacency. Adoption on proximity is
    refused; only the pre-committed grammar decides.
G2: a 1/p adjacency to FND-044's mesoscopic range was noticed pre-lock.
    It is OUT OF SCOPE for QOPH and reserved for a separate commission
    (RESH) under the scale001 seal. QOPH's outputs may not be steered
    toward it and QOPH does not open the sealed target.

## Adverse outcomes pre-authorized

SHARPENED-TENSION and UNDERDETERMINED are acceptable results and will be
registered without rescue. No re-scoping after numbers appear.

## Deliverables

benchmarks/foundations/qoph_encounter_spectrum.py (machine check of the
scaling law, the three windows, and the overlap verdicts);
analysis/QOPH_encounter_spectrum_results.md; claim registered via
tools/add_claim.py; annotations to FND-072, FND-073, NUC-030, FND-071.
