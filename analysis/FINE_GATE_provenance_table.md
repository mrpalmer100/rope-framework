# FINE-GATE Leg 1 -- THE PROVENANCE TABLE (frozen 2026-09-05, durable)
Rows per charter D1 (closed list). Clean rule D2: alpha-CLEAN iff no leaf
is alpha or a quantity computed from alpha; m_e-loading does not
disqualify; the LHAASO anchor is a measured leaf (makes the row a CEILING
suspended on m).

| length | defining relation | chain to leaves | leaf class | alpha? | m_e? | LHAASO? | kind |
|---|---|---|---|---|---|---|---|
| a (M-point) | T0 a = m_e c^2/L with T0 = Sigma a^2/3 | m_e (calibration, spent), Sigma (lattice-anchored, FND-030/ELEC-081), L (derived count), c | measured+lattice+derived | NO | YES | no | VALUE (coarse) |
| w (strand width) | w/a = 1/sqrt3 (branch-independent) | a | derived ratio | NO | YES (via a) | no | VALUE (coarse) |
| a_f (fine ceiling) | a_f <= lambda/4 at E = m x 1.4 PeV (FND-083/086/087) | h, c, LHAASO 1.4 PeV, m (underived) | constant+measured+unknown | NO | no | YES | CEILING on m |
| p (pitch) | p = a_f at worst case (FND-125) | a_f | ratio | NO | no | YES | CEILING |
| R_1 | sqrt2/(2 pi) a_f (FND-088 angle, FND-125 corrected) | a_f, sin^2 psi_1 = 1/3 (isotropy) | ratio | NO | no | YES | RATIO of a_f |
| R_2 | 0.09396 a_f (FND-125 corrected) | a_f, psi_2 | ratio | NO | no | YES | RATIO of a_f |
| r_s (bound) | r_s <= 0.1874 a_f (FND-131 rod identity at k_f/T0_f = 9) | a_f, k/T0 = 2 (coarse, chain-internal input), FND-126 anchor | ratio | NO | no | YES | CEILING/RATIO |
| r_s (derive-point) | 0.2496 a_f (FND-122, frame-drag equality) | a_f, GRV chain (chi bound from polarimetry) | ratio | NO | no | YES | RATIO (conditional) |
| l_chi | bound parasitic on w (GRV-113) | w, polarimetry ceiling | ratio+measured | NO | YES | no | BOUND |
| R* (chain) | R* = J/(pi^2 mu q^2 c); ln x* = pi^2; R* = x* x solver unit | J (closure), mu = T0/c^2 (M-point), q (winding charge), x* = e^(pi^2) | derived | NO (chain-internal; alpha is its OUTPUT) | YES | no | VALUE in solver units |
| r_min (W solver) | numerical regulator | -- | -- | -- | -- | -- | NOT A LENGTH (r_min -> 0 on real solutions; ruled out by LEAD-RAD/D-E-COMPLETE) |
| 0.407 fm (ELEC-052/081) | R_eq from published lattice flux-tube points | lattice data (anc_data), fit | measured (lattice) | NO | no | no | VALUE -- a LATTICE flux-tube radius that anchors Sigma; NOT a registered electron core scale |
| hollow-core r0 (ELEC-074/075/090) | hard core at 1.7 pct of a strand | w | ratio | NO | YES (via w) | no | VALUE, with ELEC-075's verdict on its face: the hard core IS the continuum failing -- not a physical regulator |
| (LEAD-RAD's cited core value) | V Phase 2 LEAD-2 | CODATA alpha | -- | YES | -- | -- | LOADED (the row LEAD-RAD excluded; listed for completeness) |

FINDINGS FROM THE TABLE
- Alpha-clean fine VALUE: NONE. Every fine length is a ceiling on m or a
  ratio of a_f (FND-110's suspension, confirmed row by row).
- Alpha-clean fine CEILING: YES -- a_f (and p, R_1, R_2, r_s with it),
  all descending only through h, c, the LHAASO anchor and the unknown m.
- Alpha-clean coarse VALUES exist (a, w, r0 = 0.017 w) but are coarse,
  m_e-loaded, and -- for r0 -- flagged as a continuum failure; the
  charter's Q1 forms concern fine lengths; the coarse values enter Q3
  only as the M* >= x* floor (any registered r_core <= the solver's unit).
- v3 completeness: every length in ROPE_PARAMETERS section 6 (r_s, the
  a_f-scaled stiffnesses, the twist density -- a rate, not a length) is
  covered; no row added.
