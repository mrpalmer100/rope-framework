# COMMISSION KOIDE-WEINBERG (ITEM 6d) -- RESULTS (2026-09-05)
Charter: analysis/ITEM6_charters_LOCKED.md, section 6d (locked before any
sensitivity was computed; comparison point 0.23122 locked; low-Q^2 value
displayed only). Files: analysis/koide/.

## VERDICTS
  EW-001:  ** EW-DEMOTE **
  PM-001:  ** PM-DEMOTE **
  Joint:   the pair is resolved by the demotions; the KNOWN_LIMITATIONS
           inconsistency ("succeeds with the measured angle, fails with
           the model's own") is CLOSED -- it was a fit to the input.

## Controls
v1 PM-001's construction (rope_solver.particles, byte-identical: sqrt m_k
   ~ 1 + sqrt2 cos(phi + 2 pi k/3), phi = (3 + Phi) theta_W): with 0.23122,
   mu/e = 205.81 (206.77, 0.5 pct), tau/e = 3463 (3477, 0.4 pct); with
   1/(3 sqrt2), mu/e = 1605. Reproduced.
v2 EW-001: 1/(3 sqrt2) = 0.23570 vs 0.23122 -> 1.94 pct. Reproduced.
   (Display only: vs the low-Q^2 effective angle ~0.238 -> 0.97 pct; NOT
   adjudicated against, per the lock.)
v3 Clean room: the Q1 files carry the symbol s2 only (grep-verified).

## Q1 -- SENSITIVITY (exact algebra, then numbers once)
d phi / d ln(sin^2 theta_W) = sqrt(s2) (7 + sqrt5) / (4 sqrt(1 - s2))
= 1.266 rad at the measured angle; chained through the Koide cosines,
    d ln(m_mu/m_e) / d ln(sin^2 theta_W) = 71.0
(symbolic pair derivatives 71.0 / 64.7 / -6.2 for mu-e / tau-e / tau-mu;
finite-difference cross-check agrees). A 1.94 pct change in the input
moves mu/e by a factor 7.8. Threshold 10: EXCEEDED sevenfold. The
relation is a fit to the input angle, not a prediction.

## Q3 -- DEPENDENCY PATHS (choice points named)
EW-001 (the three papers read: rope_weinberg_angle, rope_two_axioms_
weinberg, rope_hopf_weinberg): the chain is "three dimensions supply the
3, two strands supply the sqrt2, giving 1/(3 sqrt2)". Choice points:
  (1) the COMBINATION rule -- why 1/(3 x sqrt2) rather than 1/3^2,
      1/sqrt6, sqrt2/3, 1/(3 + sqrt2), ...: the two-axioms paper itself
      states "NOT CLAIMED: that these inputs uniquely force 1/(3 sqrt2).
      Uniqueness is Open";
  (2) the QUANTITY -- why sin^2 theta_W carries the geometric number
      rather than sin, tan^2, or the coupling ratio g'/g;
  (3) the READING of "three dimensions -> 3" and "two strands -> sqrt2"
      as multiplicative factors (the Hopf route "makes the origin more
      transparent" but supplies no forcing mechanism, by its own text).
  Three choice points; the chain does not reach the number without them.
  EW-DEMOTE: Conjecture -> kept coincidence with the choice points on its
  face. The number is 1.9 pct from one renormalization point and 1.0 pct
  from another, which is what a coincidence at the 1-2 pct level looks
  like; running/threshold effects are not invoked.
PM-001: the chain is Koide's empirical parametrization (external, not a
rope object) + phi = C theta_W + C = 3 d_0 + d_1/2 at k = 3. Choice
points: (1) the identification phi = C theta_W (why the Koide phase is
the Weinberg angle times a coefficient); (2) the "3 + 1 T-parity mode
count" behind C, stated as CONJECTURAL in the construction's own
docstring (d_1/2 = Phi is the rigorous part); (3) the Koide form itself
is imported. Plus the Q1 sensitivity of 71. PM-DEMOTE on both grounds.
PM-003 (Derived: the lepton problem is a 3-level excitation spectrum) is
the standing context and is untouched -- it says a relation AMONG levels
is the right kind of tool; it does not say this relation is it.

## Consequences (drafts for the author's grant)
- EW-001 -> status "kept coincidence"; PM-001 -> "kept coincidence";
  PM-002 (Failed) stands as the pinned failure. The Koide relation's
  corpus status: "an observed relation among measured masses, not a
  rope result."
- KNOWN_LIMITATIONS: the coupled-inconsistency entry closes; the
  electroweak sector's "weak link" sentence becomes "no derived
  Weinberg angle; the geometric estimate is a kept coincidence."
- The predictions ledger's structural entry citing EW-001 is annotated.
- No new geometry proposed (D3); a derivation attempt, if wanted, is its
  own charter.
