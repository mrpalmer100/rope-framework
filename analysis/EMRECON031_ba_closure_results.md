# COMMISSION EM-RECON-031 -- THE b/a CLOSURE: RESULTS (FAILED, KEPT)

Executed 2026-08-13 under analysis/EMRECON031_ba_closure_bars_LOCKED.md.
Benchmark: benchmarks/em/emrecon031_ba_closure.py. Inputs exactly as
locked: c4 = T0/8, exponential profiles, g* = 2, full quartic
cross-energy, bands +-25 percent.

## Verdict (locked grammar): FAIL-BOTH

- M1: d0/xi = 6.157 at the locked amplitude, zero free parameters.
  Deviation 353 percent from the nuclear target (1.36) and 269
  percent from the chemical target (1.67). Far outside the log-weak
  honesty band; not a near-miss.
- M2 sensitivity (disclosure): d0/xi = 2.21 at g = 1, rising
  monotonically to 6.16 at g = 2; NO MINIMUM exists at g = 2.5 or 3
  (the quartic renormalization overwhelms the attraction entirely).
  No amplitude in the locked sweep [1, 3] passes either target.

## What failed, precisely (the diagnostic value)

The full quartic cross-energy at the saturation amplitude does NOT
reproduce the registered compact model. The mechanism is the term
the bars disclosed at lock: the g1^3 g2 cross-terms decay at the
SAME exponential rate as the quadratic attraction and, at amplitude
g* = 2, renormalize it downward so strongly that equilibrium is
pushed to ~6 healing lengths (and beyond g ~ 2.3, abolished). The
compact model -a e^{-d/xi} + b e^{-2d/xi} implicitly dropped those
terms; EM-RECON-009's b/a ~ 2 consistency window lives inside that
truncation. At least one of the following is therefore wrong, and
this commission cannot say which from registered structure alone:
(i) the saturation-amplitude identification (the operating strain of
real bound modes may sit well below the Kerr onset -- the one
modeling step this commission locked, now convicted at its locked
value); (ii) the 1D exponential idealization at quartic order (3D
profile geometry may suppress the same-rate cross-terms); (iii) the
compact model's truncation, which the registered consistency window
inherited.

## What does NOT fall

- c4 = T0/8 and k/T0 = 2: untouched. The medium value was
  adjudicated (FND-027) on the speed relation and stability, not on
  this closure; the vibrational FORM check (16 percent, parameter-
  free) also stands, as it is amplitude-independent by its exact
  curvature identity.
- EM-RECON-008's unification finding: intact. The three-plus-one
  observables still hang on the same coefficient; what failed is a
  specific route from the fixed coefficient to the spacings.
- EM-RECON-009's honest flags: VINDICATED. It called the b/a check
  log-weak and the prefactors profile-dependent; the first serious
  attempt to compute those prefactors from an idealization shows the
  profile dependence is not a detail but the whole question.

## Status consequences

EM-RECON-008 REMAINS OPEN, and its Open status is now sharpened
rather than stale: the missing input is no longer the coefficient
(fixed) but the OPERATING AMPLITUDE AND PROFILE of bound modes at
quartic order -- a genuinely new, precisely located gap. The board-
scan framing ("the blocker quietly died") is corrected on the
record: the coefficient blocker died; a second blocker stood behind
it and is now named.

## Named next-orders (none owed by this commission)

A successor needs one of: a registered determination of the
operating strain of bound modes (would re-run this benchmark at that
g, one line); a 2D/3D profile computation of the same cross-terms
(new instrument, medium session); or an independent measurement
route to b/a (the Kerr window remains the clean one: vacuum optical
nonlinearity measures c4 directly and bypasses profiles entirely).
The ferro magnitude and absolute Yukawa range remain open as scoped.
