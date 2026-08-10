# COMMISSION: THE a = 8 PLANCK LENGTHS RE-DERIVATION (EXACT-D VI)

Successor to GRV-100. Charter written and bars locked before
computation. Operator GO 2026-08-09. Operator: Mark Palmer.
Computational collaborator: Claude (Anthropic).

## The chain under audit

GRV-075: a_Sak = sqrt(16 pi zeta) l_P with zeta = chi_2 / sqrt(kt0),
chi_2 = 0.967 from GRV-021's 1D machinery at M = 96 (total-energy
convention). GRV-100 amended the doctrine: the 3D covariant coefficient
is the even-log channel, scheme-borne, slope L1 = -1.61e-4 per site.
Two questions decide what survives: (1) is chi_2 intensive or extensive
(a factor of M hiding in zeta moves a by sqrt(M)); (2) what does the
chain give when the covariant coefficient replaces zeta x dictionary in
the same convention.

## Pre-committed bars

- B1 (integrity): all eight prior benchmarks PASS unmodified (the six
  commission/instrument benchmarks plus induced_elasticity and
  band_coefficient_units). Hard gate.
- B2 (reproduction): GRV-075's registered numbers reproduce on its own
  benchmark unmodified: chi_2 = 0.967 +/- 0.02, zeta = 1.209 +/- 0.02,
  a_Sak in [7, 9] l_P. Hard gate.
- B3 (extensivity): chi_2 recomputed with GRV-021's own zp_energy at
  M = 96 and M = 192, same protocol. Verdict bands, pre-set:
  |chi_2(192)/chi_2(96) - 2| < 0.1 -> EXTENSIVE: the registered zeta
  carries the ring size; an erratum is registered on GRV-075 and the
  intensive coefficient is zeta_int = chi_2 / (M sqrt(kt0)).
  |ratio - 1| < 0.1 -> INTENSIVE: no erratum; the surrogate misled.
  Anything else -> registered as unresolved with the numbers.
- B4 (the covariant chain): a_cov = sqrt(16 pi C) l_P with C the 3D
  covariant per-site coefficient in the matched convention
  (per-site, per-fractional-modulation-squared, q^2-coefficient,
  lattice units): C = |L1| |ln u0| over the locked scheme window
  u0 in [1/4, 4], with the geometric dictionary O(1) allowance [1/3, 3]
  folded in as a stated systematic. The full a-window and the sign
  structure (fraction of the scheme window with no real a) are
  registered.
- B5 (cascade adjudication, classes pre-set):
  (i) the F-Lor exclusion flips only if the a-window reaches the
  1e-16 m class; (ii) the PLANCK-CLASS statement survives iff the
  window lies within [1e-2, 1e2] l_P; (iii) the "8 l_P within a factor
  of ten" headline survives iff the window overlaps [0.8, 80] l_P;
  (iv) each of the 13 F-Sak-carrying claims is classed exclusion or
  precision and adjudicated accordingly.

## Kill and honesty conditions

No bar widens. B3's erratum outcome, if it fires, attaches to the
bookkeeping, not to GRV-021's response computation (which is correct at
its own convention). The re-derivation does not manufacture a
principle: if the sign structure leaves half the scheme window without
a real a, that is registered as the sharpest available statement of
GRV-100's open principle, not resolved by fiat. Every number enters the
record.

## Deliverables

benchmarks/gravity/exact_d_scale.py; a registered claim (proposed
GRV-101); erratum pointer on GRV-075 if B3 fires; charter outcome
addendum; document propagation; release at the operator's preference.

## OUTCOME (registered 2026-08-09, GRV-101, Modeled; erratum on GRV-075)

B1/B2 PASSED: eight benchmarks green; the registered chain (chi_2 =
0.967, zeta = 1.209, a = 7.8 l_P) reproduces exactly before correction.
B3 FIRED: chi_2(192)/chi_2(96) = 2.035 -- EXTENSIVE. The registered
zeta carries sqrt(96); the intensive coefficient is zeta_int = 0.01259
and the corrected 1D chain selects a = 0.80 l_P. B4: the covariant
chain gives real a only on u0 > 1 (positivity selects the half-line
ABOVE the band gap -- the first physically motivated candidate for
GRV-100's open principle), window (0, 0.18] l_P; the measured
dictionary ratio sits at or below GRV-095's bracket floor. B5: F-Lor
exclusion survives strengthened; the PLANCK-CLASS statement survives on
both chains (and is stronger: 0.80 l_P is nearer l_P than 7.8 was);
the '8 l_P within a factor of ten' headline FAILS, replaced by 'at or
below one Planck length'; the sub-Planck reading is registered plainly;
precision-class F-Sak descendants flagged for their own traces.
Benchmark: benchmarks/gravity/exact_d_scale.py.
