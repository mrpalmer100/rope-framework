# COMMISSION SHIN -- CAN THE OPERATOR ITSELF MOVE THE CEILING? (BARS, LOCKED)

*Locked 2026-08-11, before any evaluation. Proposal 3 from the fix menu:
attack the DISPERSION RELATION rather than the length. FND-REL-004's
ceiling came from the nearest-neighbour transverse operator; if the true
operator differs at high k, the ceiling may move. This commission tests
that -- and is required to test it GENERALLY, not by proposing one
alternative operator and checking it.*

## What must be established (the general question, not a model)

FND-REL-004 used ONE operator (nearest-neighbour tension plus a discrete
bending channel). The escape only works if SOME admissible operator on
the registered mesh gives a band ceiling above 1.4e15 eV. The commission
must therefore bound the ceiling over the whole ADMISSIBLE CLASS, not
exhibit one failure.

**Admissible class (fixed here):** any translation-invariant linear
transverse dynamics on the registered mesh of spacing a, with couplings
of arbitrary range, built from the registered constants (T0, mu, B, and
the crossing stiffness kappa_lock). Disordered (non-translation-invariant)
couplings are covered separately by the operator-norm bound below.

## The two computations required

- **C1 PERIODICITY:** for any translation-invariant lattice dynamics,
  omega^2(k) is periodic with period 2pi/a, hence attains a finite
  maximum. Establish whether long-range coupling evades this. (If it does
  not, no finite- or infinite-range modification helps, and the escape is
  closed for the whole class at once.)
- **C2 OPERATOR NORM:** bound omega_max for ANY coupling arrangement,
  ordered or disordered, by the Gershgorin/operator-norm bound
  omega_max^2 <= (sum of |couplings|)/mu, and express the result in
  registered constants. State what coupling magnitude would be REQUIRED
  to reach the anchor energy, and compare it to the registered values.

## Bars (pre-committed)

- **ESCAPE-OPEN** iff some admissible operator reaches
  E_max > 1.4e15 eV using registered constants without altering a.
- **ESCAPE-CLOSED-BY-THEOREM** iff the class is bounded above by a
  ceiling of order hbar c / a irrespective of the operator's details --
  in which case the finding is stronger than FND-REL-004's, since it
  removes ALL operator-shaped hopes at once rather than one.
- The required coupling enhancement factor must be computed and stated
  whichever way it lands.

## Disclosure

If the escape closes, the commission must say plainly that proposals 1
and 2 (strand substructure; a different carrier) and route (c) are what
remain, and must NOT propose a new primitive itself -- naming is the
author's, per the standing rule.
