# COMMISSION AYIN -- GRANT-N2's ACCEPTANCE TEST: BARS (LOCKED BEFORE COMPUTING)

*Locked 2026-08-11, after the author's adoption of GRANT-N2 and BEFORE any
(N, k) number is evaluated. The test FND-053 pre-built: does the granted
label primitive deliver b_k(N), and does it discriminate sine from Casimir
at O(1/N^2)? The grant is adopted; this commission may not widen it, may
not add a second primitive, and may not rescue a miss.*

## The granted primitive (as adopted, stated exactly)

Strands carry one of N labels. A unit winding is label-carrying; a
k-string is k unit windings (FND-048 bundles, GG-006 additive winding).
Inter-tube attraction arises from LABEL EXCHANGE between tube pairs. One
primitive, one coupling; nothing else is granted.

## The derivation's required shape (fixed before computing)

b_k = C(k,2) * v(N) / k, where v(N) is the per-pair binding fraction
supplied by label combinatorics alone. Two statistics are pre-named and
BOTH must be computed and reported:

- **A FREE LABELS:** each tube's label independent and uniform over N.
- **B EXCLUSION LABELS:** the bundle's tubes carry DISTINCT labels (the
  antisymmetric/Pauli-class reading of winding exclusion).

v(N) must come from counting exchange channels against available label
partners. No coefficient may be fitted; if a statistic requires one, it
registers UNDERSPECIFIED.

## Bars

- SHAPE: a statistic PASSES shape iff its b_k is proportional to (k-1)
  and falls as 1/N at large N (both required, checked symbolically).
- MAGNITUDE: evaluated at SU(4)/SU(6)/SU(8), k = 2, 3 against the
  registered record: antisymmetric-Casimir b = (k-1)/(N-1) and the sine
  law, with SU(6) k=2 sine-consistent at ~2 percent and sitting +8.3
  percent above Casimir (FND-047's admissible record).
- DISCRIMINATION: the demand's teeth. A statistic that reproduces one law
  EXACTLY must say so, and the corpus then owns that law's fate.
- MANDATORY DISCLOSURE: FND-040's derived softening applies on top of any
  bundle result (single-source violations are negative). Its direction
  relative to whichever law is landed on MUST be reported, whichever way
  it cuts.

## Verdict grammar (pre-committed, four ways)

- **DERIVES-SINE**: a statistic lands the sine law. The grant is
  vindicated against the data that motivated it.
- **DERIVES-CASIMIR**: a statistic lands antisymmetric-Casimir exactly.
  The 1/N structure is DERIVED (the grant's stated purpose achieved) but
  the corpus is then committed to Casimir against sine-favoring data --
  registered as a partial success with a live exposure, NOT as a win.
- **DERIVES-NEITHER**: shape or magnitude misses both laws. The grant
  bought nothing; registered Failed-and-kept and the author informed
  that the primitive did not pay.
- **UNDERSPECIFIED**: the combinatorics cannot be written without a free
  parameter.

No retreat, no reweighting, no post-hoc statistic. Whichever cell fires
is registered at full volume.
