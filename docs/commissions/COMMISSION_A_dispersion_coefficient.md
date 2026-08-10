# COMMISSION A: THE DISPERSION COEFFICIENT

## The question
Compute, from the strand engine, the coefficient beta of the leading lattice
correction to the transverse (photon-sector) dispersion:

    omega^2 = c^2 k^2 [1 - beta (k a)^2 + O((ka)^4)]

The corpus currently holds two claims in unexamined tension:

- FND-REL-002: the matter-coupled transverse sector is EXACTLY Lorentz
  invariant (emergent LI, exact).
- FND-MATTER-005: the absolute mesh scale a is fixed by MEASUREMENT via the
  (ka)^2 Lorentz-violation dispersion signal.

Both cannot be fully true. This commission decides which.

## Why this is high stakes
If beta = 0 identically, the measurement route in FND-MATTER-005 is VOID and
the M-point (FND-MATTER-044) is the framework's only possible pin, with no
independent falsifier. FND-MATTER-005's "normal fundamental constant with a
defined measurement route" framing must be amended.

If beta = O(1), then a = 6.0e-17 m implies a dispersion scale of order
hbar*c/a ~ 3 GeV. Astrophysical time-of-flight constraints on quadratic
Lorentz violation sit many orders of magnitude above this. The corpus would
be either already falsified in the photon sector or owed a derivation of
strong suppression.

Both outcomes reorganize the sector. There is no boring answer.

## Pre-committed bars (locked before computation)
- B1: beta must be computed symbolically or numerically from the registered
  transverse wave operator on the discrete weave, with no reference to any
  observational bound during the derivation. The observational comparison is
  run only after beta is fixed.
- B2: if beta = 0 at O((ka)^2), the computation must continue to the first
  nonvanishing order and report it, with its coefficient.
- B3: any claimed exact cancellation must be exhibited as an identity
  (sympy-grade), not a numerical near-zero. A numerical residual below 1e-10
  with no identity is registered as "consistent with zero, identity not
  found" and the claim stays Modeled.
- B4: the observational confrontation uses published bounds cited by name
  and number. No bound is characterized from memory; each is web-verified or
  taken from a cited source in the session.

## Seal
The answering session must derive beta BEFORE being shown any statement of
what value would be convenient. This document's "Why this is high stakes"
section is the contamination risk; a clean run hands the session only the
question section and the bars, and supplies the stakes section afterward.

## Stopping rule
One derivation, one audit pass, one observational confrontation. If the
derivation and audit disagree, one reconciliation session. No further
attempts; register the disagreement if unresolved.

## Registrable outcomes (all acceptable)
1. beta = 0 by identity: FND-MATTER-005's measurement route is amended to
   void; the exactness of FND-REL-002 is strengthened; the M-point becomes
   the sole pin, stated plainly.
2. beta != 0: confront bounds. If excluded, register the falsification of
   the a = 6.0e-17 m + O(1)-dispersion combination at full volume and open
   the suppression question as a named problem.
3. Underdetermined by current commitments: register per the GRV-006 style.

## Depends on
FND-REL-001, FND-REL-002, FND-MATTER-005, FND-MATTER-044, FND-STRAND series
(engine), GRV-029 (metric dictionary, for the operator's registered form).
