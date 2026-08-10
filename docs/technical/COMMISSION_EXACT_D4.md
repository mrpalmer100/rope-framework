# COMMISSION: THE SMALL-q ASYMPTOTICS (EXACT-D IV -- THE FORM OF D)

Successor to GRV-096/097/098. Charter written and bars locked before
computation. Operator GO 2026-08-09. Operator: Mark Palmer.
Computational collaborator: Claude (Anthropic).

## The question, sharpened by GRV-098

Is A(q -> 0) -- the ordered-limit sqrt(u) coefficient, the EH action
amplitude D -- a constant, a logarithm, or zero? The scaling analysis
locked with this charter predicts: the joint-IR region (k ~ m/c)
supports only m^(4-s) q^s with s even (no m q^2 term), and the massless
region (k >> m/c) has a scale-invariant q^2-density kappa/k whose
integral is q^2 ln(1/m) -- a running coefficient. The commission tests
that prediction against its own bars; either confirmation or refutation
is registrable.

## Plan

- P1 (integrity): all five prior benchmarks PASS unmodified (the two
  absorption instruments and the three commission benchmarks).
- P2 (the IR exponent): the bilinear-only q^2-coefficient at m = 1
  (the dimensionless F block) as Q -> 0.
- P3 (the log, two ways): (a) the radial shell density of the
  near-massless bilinear q^2-integrand, k s(k), must plateau over an
  intermediate decade; its level is kappa. (b) the direct logarithmic
  derivative d e2 / d ln u at small u and small q. The two must agree
  as d e2/d ln u = -kappa/2.
- P4 (the verdict on A): subtract the DERIVED (not fitted) log term
  from the continuum profile; the FD3 residual determines A(q) across a
  q-decade.
- P5 (lattice reconciliation): the derived log coefficient confronted
  with GRV-097's profile-linearity bound (a log adds a (16/3)(kappa/2)
  u^(-1/2) masquerade to the FD3 profile; the lattice profile's
  linearity caps it).

## Pre-committed bars

- B1 (integrity): hard gate, all five benchmarks.
- B2 (IR exponent): the bilinear q^2-coefficient at m = 1 approaches a
  constant: |F(Q) - F(Q/2)| / |F(Q)| < 2% at Q = 0.02. Confirms no
  m q^2 from the joint-IR region.
- B3 (log agreement): k s(k) has a plateau (local log-slope of s(k)
  within -1.0 +/- 0.1 over at least one decade), and
  |d e2/d ln u - (-kappa/2)| / |kappa/2| < 15%.
- B4 (form verdict): after subtracting the derived log, exactly one of:
  (i) CONSTANT -- A(q) stable to < 10% across a q-decade; or
  (ii) ZERO/LOG-DOMINATED -- |A(q)| < 3x its q-halving movement.
  An ambiguous residual (neither clean) is a Failed registration.
- B5 (lattice consistency): the derived kappa's FD3 masquerade at
  u = 0.037 is < 30% of GRV-097's measured profile span at M = 96 --
  or, if it exceeds that, the excess must itself be shown consistent
  with the lattice data by direct refit including the derived log
  (coefficient FIXED, not fitted), R^2 >= 0.99.

## Kill and honesty conditions

A failed B2 refutes the scaling analysis and registers as such. A
failed B3 means the log identification is wrong; the shell density's
actual exponent is registered. B4's two clean outcomes are both
successes of FORM adjudication; only ambiguity is failure. No bar
widens; the quadrature engine is GRV-098's validated one (a new file
must reproduce the registered integrand at a test point to 1e-12);
every number enters the record.

## Deliverables

benchmarks/gravity/exact_d_asymptotics.py; a registered claim (proposed
GRV-099); charter outcome addendum; document propagation; release at
the operator's preference.

## OUTCOME (registered 2026-08-09, GRV-099, Modeled)

B1 PASSED (five benchmarks). B2 PASSED at 0.003% (F(Q) constant; no
m q^2 from the joint-IR region). B3's premise REFUTED as the charter
allowed: the massless shell density is proportional to k, not 1/k --
the q^2 ln(1/m) channel does not exist. The actual non-analyticity is
the EVEN log, m^2 ln m: tadpole +2.47e-4 (its exact integral; the
internal control returns |A/L1| = 2e-4, pure log, validating the
four-term model), bilinear -4.08e-4, total L1 = -1.61e-4 (q-stable 4%).
B4 PASSED, verdict (ii): A(q) proportional to q -- the ordered-limit
sqrt(u) amplitude is ZERO. B5 PASSED at R^2 = 0.99963 with the derived
log FIXED: it absorbs 82-88% of GRV-097's lattice profile; residuals
collapse to A = 1.4e-5, B = 5.9e-5. THE ARC RESOLVED: protocol
dependence (GRV-096), the two-term structure (GRV-097), and the
non-commuting cliff (GRV-098) were the even-log masquerading through an
incomplete basis plus finite-q crossover. Named next-order: the
physical reading of the running m^2 ln m coefficient against GRV-095's
constant-D tension formula. Benchmark:
benchmarks/gravity/exact_d_asymptotics.py.
