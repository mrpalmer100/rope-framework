# FND-STRAND-021 — the per-channel shape: the switch-on hypothesis
# Bars locked before any run

Date: 2026-08-03. Commission: the question FND-STRAND-020 cleanly isolated
— why does the per-channel hazard fall? The arc's clues, assembled: the
composite is always initialized in a PRODUCT STATE (weave thermal, chain
exactly cold and uncorrelated with it), which is not the equilibrium of
the coupled system. Statistical mechanics calls the consequence "initial
slip": for a time of order the correlation-building epoch, the coordinate
feels non-stationary effective forcing even though every stationary
aggregate (temperature, instantaneous force intensity) reads flat — which
is EXACTLY the signature 015/016 measured. The hypothesis:

  THE PER-CHANNEL TRANSIENT IS A SWITCH-ON EFFECT. The falling hazard is
  the product-state slip decaying into the stationary Kramers rate; the
  plateau IS the equilibrium rate; a system prepared in the true
  metastable equilibrium has NO transient — constant, memoryless escape
  from t = 0.

This is decisively testable: change nothing but the preparation.

## The preparation, defined exactly

Metastable-well equilibrium at the standard operating point (N = 24,
h = 0.55, T = 0.40, c0 = 0.35, K = 16, dt = 0.02, window 36000):
- Chain: linearize about the uniform well minimum phi_0 = asin(h). Draw
  lattice phonons thermally: normal-mode coordinates ~ N(0, T/omega_m^2)
  with omega_m^2 = cos(phi_0) + 2 kt (1 - cos k_m), momenta ~ N(0, T);
  transform to site coordinates; phi = phi_0 + fluctuation.
- Weave: shifted-oscillator equilibrium — qs ~ N(0, T)/omega per mode,
  p ~ N(0, T)^{1/2} scaling as standard, then q = qs + c phi_n / omega^2
  (the counter-term form makes the bare chain potential the equilibrium
  weight, so this is the correct dressed draw at the drawn phi).
- The quadratic-well draw is an approximation at T/DeltaE ~ 0.2; its
  residual is acknowledged in advance and the bars' tolerances are set
  accordingly. Walkers whose draw escapes immediately are part of the
  ensemble and are kept and reported.
Generators: 161-164, 32 walkers each (n = 128). Censoring clause: > 2%
invalidates. Chunked checkpointing pre-authorized.

## B1 — flatness of the equilibrium-prepared hazard

R_eq := lambda[q50,q90]/lambda[q25,q50] on the equilibrium-prepared
ensemble (STRAND-013 estimator, this ensemble's own quantiles).
- CONSTANT: R_eq in [0.75, 1.33] — the transient is gone; the shape was
  preparation, not physics of the well.
- STILL-FALLING: R_eq <= 0.60 — the transient survives equilibrium
  preparation; the switch-on hypothesis is REFUTED and the shape is
  intrinsic; registered at full volume.
- INTERMEDIATE: otherwise; as measured (the quadratic-prep residual is
  the pre-named suspect at this outcome, and a better-prep follow-up is
  the next-order rather than a verdict).

## B2 — the level closure

If B1 lands CONSTANT: the single fitted rate lambda_eq (ln-survival slope
over [q25, q90]) must match the product-state ensemble's LATE rate — the
registered plateau lambda_3 = 4.06e-4 from the pooled n = 512 reference
([q90, q98] window, STRAND-018) — within a factor 2.
- CLOSED: within factor 2 — the plateau IS the equilibrium rate.
- OPEN: outside — flat but at the wrong level; registered; the level
  residual named.

## B3 — memorylessness (only if B1 CONSTANT)

Shape check: r^2 of the ln-survival fit over [q25, q90] >= 0.95 — the
equilibrium ensemble escapes exponentially.

## Promotion criterion

PROMOTE the switch-on mechanism iff B1 CONSTANT and B2 CLOSED (B3
reported; a B3 failure with B1/B2 passing is registered as a shape
residual, not a block). Consequence grammar if promoted, at full volume:
- The per-channel shape question is ANSWERED: the falling hazard is
  product-state slip; the plateau is the stationary Kramers rate whose
  clock STRAND-010 promoted.
- PREDICTION 11, refined a final step: the non-Poisson dark-count
  transient is a SWITCH-ON phenomenon — it appears after a quench
  (power-up, reset, sudden isolation) and lasts the correlation-building
  epoch; in steady state, even SMALL detectors click Poisson at the
  plateau rate. Together with STRAND-020: dark-count survival =
  (per-channel switch-on curve)^(channel count) after a quench, pure
  exponential in steady state — an experimentally crisp two-regime
  statement.
If REFUTED: the shape is intrinsic to the well dynamics; the named
next-order is the per-channel spectral theory (the 017-successor in its
harder form).

## Honesty clauses

- Preparation recipe, generators, estimator, windows, and every threshold
  fixed above. The registered plateau number is used as registered.
- Status ceiling: Modeled. Absolute scale untouched (FND-MATTER-003).
