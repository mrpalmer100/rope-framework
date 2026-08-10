# COMMISSION: THE B-DERIVATION AND THE SUBTRACTED EXTRACTION (EXACT-D III)

Successor to COMMISSION_EXACT_D (GRV-096) and COMMISSION_EXACT_D2
(GRV-097). Charter written and bars locked before computation. Operator
GO given 2026-08-09. Operator: Mark Palmer. Computational collaborator:
Claude (Anthropic).

## The route, and why it is not a third protocol

GRV-097 measured the two-term m-odd structure A sqrt(u) + B u^(3/2) with
B/A = 5.6 and showed no fitting protocol can separate the terms while
the lattice floors the window at 3 c q(M). But GRV-024's decomposition
already says the m-odd content is CONTINUUM physics (the lattice loop is
m^2-analytic). So both coefficients are computable from the continuum
limit of the instrument's own response: take the q -> 0 limit
analytically (no lattice floor), then descend in m numerically to
u << A/B where sqrt(u) dominates. Derive B; confront it with GRV-097's
measurement; subtract it from the lattice data; extract A clean.

## Plan

- P1 (integrity): absorption_test, absorption_verdict, exact_d_extraction,
  exact_d_ordered all PASS unmodified.
- P2 (continuum response): the continuum limit of E2_total's integrand
  (bilinear + tadpole), with the lattice trig elements replaced by their
  exact small-k forms and the h-derivative constants (V1, P2, W1, T2)
  taken from the instrument's own coeffs() at the operating point
  kt0 = 0.64. The q^2 coefficient of the xy channel taken as an exact
  small-q expansion. Momentum integrals by deterministic product
  quadrature with an explicit UV cutoff Lambda.
- P3 (m-odd isolation): evaluate the continuum q^2-coefficient on a
  dense u-grid reaching far below the lattice floor; the FD3 annihilator
  (unchanged from GRV-097, including its exact identity) extracts the
  m-odd profile; cutoff-independence of the m-odd part is a registered
  check (two Lambda values).
- P4 (confrontation): the derived B against GRV-097's measured
  4.826e-4.
- P5 (subtraction): subtract the derived B u^(3/2) from the M=96 dense
  lattice scan; re-run the SAME window and basis variants that failed
  B3 twice; re-run the FD3 profile, which must now be flat.
- P6 (the number): if P2-P5 hold, the continuum extraction also yields A
  directly; lattice-subtracted A and continuum A are two independent
  routes and must agree.

## Pre-committed bars

- B1 (integrity): all four prior benchmarks PASS unmodified. Hard gate.
- B2 (confrontation): |B_derived - 4.826e-4| / 4.826e-4 < 10%.
- B3 (cutoff independence): the m-odd profile's A and B move < 2%
  between the two registered Lambda values.
- B4 (subtraction closure): after subtracting B_derived, the lattice
  M=96 window and basis variants (the exact GRV-097 set) move the
  sqrt(u) coefficient < 10%, and the subtracted FD3 profile is flat:
  |slope| * u_max / A < 10%.
- B5 (two-route agreement): |A_lattice_subtracted - A_continuum| /
  |A_continuum| < 15%.

## Kill and honesty conditions

B2 failure registers as "the u^(3/2) amplitude is not the continuum
universal coefficient" -- a major finding kept at full strength. A
non-flat subtracted profile (B4) registers a THIRD m-odd term with its
measured exponent. No bar widens; no quadrature or cutoff is re-chosen
after first compute beyond the two registered Lambda values; every
number enters the record. If all bars pass, the resulting claim carries
D = A with the spread across B4 variants as its uncertainty, at status
Modeled, with the propagation to a (GRV-095) executed in the same claim
if the uncertainty supports the predecessor charters' 3x narrowing
standard.

## Deliverables

benchmarks/gravity/exact_d_derived.py (deterministic, CI-fast signature
test); a registered claim (proposed GRV-098); charter outcome addendum;
document propagation; release at the operator's preference.

## OUTCOME (registered 2026-08-09, GRV-098, Failed and kept)

B1 PASSED. B3 PASSED at 0.008% (A) and 0.02% (B) between Lambda = 6 and
12. B2 FAILED at 167% -- and the reconciliation explains it: the same
machinery at the lattice's q = 2 pi/96 over the lattice window
reproduces GRV-097's measured pair (B_eff 4.18e-4 within 13%, A_eff
1.05e-4 within 22%), while q-first gives (A ~ 2.0-2.2e-5, B = 1.29e-3).
THE FINDING: the q->0 and m->0 limits do not commute; the lattice
commissions measured the finite-q object; the action coefficient D is
the ordered-limit object. B4 fails by arithmetic on registered numbers;
B5 not reached. THE CLIFF: below q ~ 3e-3 the ordered-limit A
extraction destabilizes (23% under q-halving; FD3 noise-limited); the
true A is unpinned near 2e-5 or undefined. NAMED NEXT-ORDER: analytic
small-q asymptotics of the explicit, validated continuum bilinear --
pen and paper decides constant vs log vs zero. One implementation note
kept for the record: the first continuum run's u-grid violated the
m >= 3cq regime floor at its bottom; the corrected runs respect it, and
both are in the record. Benchmark: benchmarks/gravity/exact_d_derived.py.
