# COMMISSION NUN8 -- THE GRANT-EXDYN-OVERLAP ADJUDICATION -- BARS LOCKED (2026-08-15)

Locked AFTER the grant text (FND-112) was registered and BEFORE any
overlap integral is evaluated. Grant condition 1: one session,
derivation-or-demotion armed, no re-granting on failure. The granted
form is quoted from FND-112 and may not be amended here.

## THE GRANTED FORM, quoted (fixed input)
Exchange amplitude per AYIN channel = transverse profile overlap along
the transport path; profile = CHROMO-PROFILE-CLEM (FND-111), quoted
parameters mu/sqrt(sigma) = 2.684(97), kappa_GL = 0.178(21), i.e.
alpha = xi_v/lambda from the source's lambda/xi_v = 0.27 plateau
family (Table I class); direct orientation path = d, reversed = 2d,
w2 = O(2d)/O(d); echo = reversed remainder re-entering per partner at
its own amplitude.

## THE DERIVED f(N), fixed at lock (B1)
From AYIN's registered counting dressed by the granted weights:
    f(N) = (1 + w2)/2 + w2/(N-1)
with w2 = O(2d)/O(d) and O the normalized 2D transverse overlap of two
CHROMO-PROFILE-CLEM fields at separation d:
    O(d) = Int E(x) E(x - d) d^2x / Int E(x)^2 d^2x ,
    E(x_t) prop K0( (mu^2 x_t^2 + alpha^2)^(1/2) ) .
The near-coaxial reading (FND-108, geometry shadow): the binding
fraction IS the overlap fraction, so self-consistency demands, at
each N,
    O(d_N) = f(N) = (1 + w2(d_N))/2 + w2(d_N)/(N-1)      [ONE
equation in ONE unknown d_N per N, ZERO free parameters].

## THE THREE SHADOWS, bands registered before this grant existed (B2)
- S1 (NUN4 B1): f(6) within 2 sigma of 0.865(33).
- S1 (NUN4 B2): f(infinity) within 2 sigma of 0.64(10), where
  f(inf) solves O(d) = (1 + w2(d))/2.
- S1 (NUN4 B3): f(4) within 3 sigma of 0.928(21) AND f(5) within
  3 sigma of 0.898(22).
- S2 (geometry): the solved d_N are NEAR-COAXIAL (d_N below the
  tube's characteristic transverse extent, taken as 2 lambda, the
  K0-class decay scale doubled) and O(d_N) DECLINES in N (direction
  only; magnitudes are S1's job).
- S3 (safe-volume profile): identical to NUN4 B3 by construction
  (the profile points ARE the safe-volume Table 14 points); S3 passes
  iff B3 passes. Stated so no double counting inflates the verdict.

## PARAMETER TREATMENT (B3)
alpha enters from the source's lambda/xi_v plateau. The fit family in
the source spans roughly 0.27-0.31 across smearing and 0.24-0.33
across its two determinations (2014 vs 2012-class). The CENTRAL
adjudication runs at alpha = 1/0.27 = 3.70. A sensitivity band at
alpha in [3.0, 4.2] is computed and DISPLAYED; the verdict is taken
at the central value only. No alpha is chosen after seeing f values:
this paragraph is the entire alpha policy.

## OUTCOMES, pre-committed (B4)
- PASS: all S1 bands met at central alpha AND S2 both conditions.
  Consequence: the granted form is ADJUDICATED-HELD, the window point
  ceases to be displayed-not-derived, and the k-string shortfall
  acquires its mechanism at Modeled grade with the derivation route
  (overlap integrals from a registered external profile) on the face.
- DEMOTED: any S1 band missed at central alpha, or S2 violated.
  Consequence: GRANT-EXDYN-OVERLAP is demoted per its own exposure
  statement, failure kept, no rescue, sector parks on external
  clocks with no surviving named candidate.
- NOT-SOLVABLE: the self-consistency equation has no solution d_N > 0
  for some required N. Registered as DEMOTED (the form cannot
  produce the geometry it was granted to produce).
- Mixed outcomes are resolved by the above in order; there is no
  PARTIAL at this bar (FND-107 set the stakes: pass or park).

## REFUSALS (B5)
- No amendment of the path reading, echo structure, or f(N) formula
  after any number is seen.
- No alpha selection outside the B3 policy.
- No appeal to the supplementary 2019-2025 profile series.
- No SU(N) profile rescaling invented (the N-dependence enters ONLY
  through the echo term, per the granted form; if that is too little,
  the form fails honestly).
- No softening of a DEMOTED verdict into "displayed."

## DELIVERABLE (B6)
One registered claim (FND-113) with the verdict, the solved d_N and
f(N) table, the alpha sensitivity display, the benchmark script under
benchmarks/, GRV/FND cross-annotations per outcome, CHANGELOG,
verify_corpus --quick green, re-zip.

## FAILURE MODES NAMED IN ADVANCE
- The two-number seduction, again: NUN4 executed a candidate that hit
  B1+B2 and died on B3 at 11.4 sigma. B3 is computed with the same
  care as B1.
- Solving for alpha instead of d (barred: alpha policy is fixed).
- Reading S3 as an independent pass to pad the verdict (barred at B2).
- Calling a near-miss at 2.1 sigma a pass. The bands are the bands.
