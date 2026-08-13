# EM-RECON-018-R: the areal re-solve -- RESULTS

Executed 2026-08-12 under analysis/EMRECON018R_resolve_bars_LOCKED.md.
Benchmark: benchmarks/em/emrecon018r_areal_resolve.py.

## Headline

The survival band is ROBUST to the convention correction, and the reason is
structural, not lucky: C(d0/sigma0) peaks at the knee (d0/sigma0 ~ 1.0,
C = 5.06) and the two admissible readings sit on OPPOSITE FLANKS of that
peak at nearly equal heights. Reading A (in-family touching, d0/sigma0 = 1.00)
never depended on w/a and is unchanged. Reading B moved from 1.381 (right
flank, C = 4.36) to 0.797 (left flank, C = 4.35) -- across the peak, landing
at the same curvature. The flank-crossing was verified by sweeping C over
[0.5, 3.0]: the curve is single-peaked at the knee, both readings bracket it.

## Numbers

- Corrected ratio: w/a = sqrt(4 f_c / pi) = 0.6272 at f_c = 0.309
  (sensitivity window: 0.305 at f_c = 0.073, 0.666 at f_c = 0.348).
  Factor sqrt(3) = 1.732 over the superseded 0.3621, per FND-068.
- Reading A: d0/sigma0 = 1.000, C = 5.057, threshold 0.395.
- Reading B: d0/sigma0 = 0.797 (was 1.381), C = 4.347, threshold 0.460.
- RE-SOLVED BAND: [0.395, 0.460]. Supersedes [0.40, 0.46]; numerically the
  same band to the displayed precision. The quarantine is LIFTED.
- Confrontation (FND-029 estimates, displayed and NOT adopted, unchanged
  status): m_b < 63-73 at L1 = 1 (factor-3 band ~21-220). Single-pair,
  surface-line (~22), contact-patch (~63) SURVIVE; full-section (~498) FAILS.
  Identical verdict pattern to the superseded solve.
- W1 propagation (per FND-066's a-carrying rule): every W1 value scales by
  sqrt(3). At the a values recovered from FND-066's registered W1 numbers:
  0.0362 -> 0.0627 fm (Lorentz-bound a = 0.100 fm), 0.0059 -> 0.0102 fm
  (a = 0.0163 fm), 0.0035 -> 0.0061 fm (a = 0.0097 fm). The factor-of-ten
  spread across a values is unchanged; FND-066's refusal to quote w without
  its a stands.

## Reported per B2, carried not resolved

Under the corrected (wider) strand, reading B's cross-family half-spacing
standoff sits at 0.797 contact ranges -- BELOW touching separation. The
half-spacing offset is now closer than one contact range, i.e. cross-family
strands at a/2 would sit inside each other's contact form. Whether that
invalidates reading B's routing idealization or is exactly what an
interpenetrable medium looks like is a physical question the locked bars
forbade this commission from answering. It is registered as the claim's
named open edge.

## Consequences (B5)

- EM-RECON-018: band annotation superseded by this claim; quarantine lifted.
- FND-064: the sign identity inherits the re-solved band unchanged in
  magnitude; nothing on its face moves.
- FND-065: the units bridge (0.362 -> 0.627, 0.24 orders) was already applied
  by FND-068's annotation; the corrected gap 4.6-5.2 orders stands. The
  region-I exclusion is UNAFFECTED by this re-solve.
- FND-029: the width target's band is numerically unchanged; the sharpening
  claimed by EM-RECON-018 survives the convention correction.
- FND-066: W1 values updated by sqrt(3) as above; the census's structure is
  untouched.

## What this commission did NOT do

No new f_c, no new contact form, no adjudication of reading B's sub-touching
geometry, no adoption of the FND-029 estimates, no one-medium prosecution.
