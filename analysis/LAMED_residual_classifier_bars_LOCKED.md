# COMMISSION LAMED -- THE NUCLEAR RESIDUAL CLASSIFIER: BARS (LOCKED BEFORE COMPUTING)

*Locked 2026-08-11, before any residual is evaluated. The queue's brick:
blind correlation of the remaining few-MeV binding residual against
rope-native structural descriptors, tested strictly out of sample. The
obvious Fermi-gas explanation was already falsified (NUC-010) and stays
falsified; nothing here reopens it.*

## The registered baseline model (fixed here, no refitting permitted)

B_rope(A, Z) = a_V A - a_S A^(2/3) - a_C Z^2 A^(-1/3) - a_A (N-Z)^2 / A

- Geometry chain at the CORRECTED registered values (NUC-018): saturation
  spacing d0 = 2.026 fm (NUC-017), surface ratio a_S/a_V = 1.34 (NUC-015/016
  sphere value), a_C = 0.6 * 1.44 / (r0_over_d0 * d0) with
  r0_over_d0 = (3/(4 pi sqrt(2)))^(1/3) -- all derived, none fitted here.
- a_V calibrated ONCE on Ca-40 (the registered calibration convention,
  NUC-005/018). One constant, fixed before residuals exist.
- Asymmetry a_A = 19.85 MeV, the registered derived value (NUC-A kinetic
  16.6 + NUC-B quadratic-overlap potential 3.25; zero new constants).
- PAIRING IS EXCLUDED FROM THE BASELINE deliberately: NUC-024's derived
  term is A-independent where nature falls as 1/sqrt(A) (registered
  mismatch), so pairing parity remains an admissible DESCRIPTOR below
  rather than a subtracted term. Stated so the choice is auditable.

## Data and scope (fixed)

AME2012 evaluated masses (masstable package data file, mass excesses in
MeV; B = Z*7.28897 + N*8.07132 - Delta). Scope: A >= 12, measured table
only -- the registered classical-drop applicability domain (He-4 and
lighter declared inapplicable by NUC-005). Residual R = B_exp - B_rope
in MeV, total (not per nucleon).

## Descriptors (CLOSED list, each with its license; nothing added after lock)

- D1 SHELL: valence distance s = min|Z - m| + min|N - m| over the magic
  set {2, 8, 20, 28, 50, 82, 126}. Licensed by the queue's "shell
  occupancy". MANDATORY DISCLOSURE, on the face: the magic numbers are
  an EXTERNAL empirical structure; a D1 hit LOCATES the residual at the
  declared quantum boundary, it does not derive it.
- D2 PAIRING PARITY: delta = +1 (even-even), 0 (odd A), -1 (odd-odd).
  Licensed by NUC-024's isolated channel.
- D3 CURVATURE: A^(1/3), the droplet curvature term absent from the
  registered functional. Licensed by the queue's "curvature".
- D4 LINKING DENSITY: Z/A, charge windings per nucleon (GG-006 charge =
  winding). Licensed by the queue's "knot/link density".
- D5 ALPHA GEOMETRY: indicator (A mod 4 = 0 and N = Z). Licensed by
  NUC-009's alpha-cluster construction.
- D6 ISOSPIN QUARTIC: (N-Z)^4 / A^3, the next order past the registered
  quadratic. Licensed by NUC-020's exponent finding.
- D7 RECONNECTION CONFIGURATION COUNT: UNDERSPECIFIED -- no registered
  computable form exists for a bond-arrangement multiplicity; declared,
  not improvised. (Same acquisition-target grammar as FND-051.)

## Protocol (pre-committed)

1. Random 50/50 train/test split, seed 3141, drawn before any residual is
   inspected; split is descriptor-blind and residual-blind by construction.
2. OLS of R on [1, D1..D6] on train. Report: each descriptor's UNIVARIATE
   out-of-sample R^2 on test, and the JOINT model's out-of-sample R^2.
3. SWAP TEST: refit on test, score on train; retained coefficients
   (|t| > 3 on train) must keep sign.
4. PERMUTATION: 1000 refits with R permuted within train, scored on test;
   the joint out-of-sample R^2's null distribution and p-value reported.

## Bars (pre-committed)

- A descriptor is a FINDING iff univariate out-of-sample R^2 >= 0.5.
- The JOINT model is a FINDING iff out-of-sample R^2 >= 0.6 AND the swap
  test passes AND permutation p < 0.01.
- Verdict grammar: STRUCTURE-FOUND (named descriptors) / DIFFUSE (signal
  below bars) / NULL (nothing beats permutation). Whatever lands is
  reported with the full table, hits and misses alike.
- No descriptor may be transformed, thresholded, or recombined after this
  lock. No residual may be inspected before the split is drawn.
