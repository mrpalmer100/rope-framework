# ELEC-067 — Can matter use the fast channel? Locked bars

## Commission
ELEC-066 Amendment 1 left one sharp question: the longitudinal sector decouples
from matter at LINEAR order exactly (EM-RECON-011), so any use of it by a matter
configuration must be nonlinear, or the decoupling must be shown not to apply to
a self-coupled object. Neither had been done. But EM-RECON-011 leg (2) already
records the answer's first half: the first coupling IS a cubic vertex,
((k - T0)/2) u' psi'^2, sympy-verified. This session asks whether that vertex is
USABLE.

## What is fixed before computing
- The vertex, from EM-RECON-011: strain eps = sqrt((1+u')^2 + psi'^2) - 1, no
  quadratic u'-psi' mixing, first coupling ((k-T0)/2) u' psi'^2.
- The inextensible limit: QB-008 corners the fast channel onto the
  INSTANTANEOUS-CONSTRAINT limb, which is the ideal limit of P-VOL. In that
  limit the longitudinal sector has no propagating dynamics -- it is a
  CONSTRAINT field solving an elliptic equation sourced by the transverse
  sector.

## Locked bars
B1 RE-DERIVE THE VERTEX independently (sympy, from the strain expression) rather
   than citing it. Confirm no quadratic mixing and the cubic coefficient.
B2 THE NO-GO CHECK, and it must be run first because it could end the session:
   the vertex coefficient is (k - T0)/2. IF the medium satisfies k = T0 the
   vertex VANISHES IDENTICALLY and matter cannot use the channel at cubic order
   at all. Determine whether the corpus forces k = T0, forbids it, or leaves it
   free. Report whichever it is.
B3 THE CONSTRAINT STRUCTURE: in the inextensible limit, derive the equation the
   longitudinal field obeys and state explicitly whether its response is
   instantaneous and what sources it.
B4 THE MAGNITUDE: for a localized transverse configuration of amplitude A and
   scale R, compute the induced longitudinal strain and the dimensionless
   coupling. State what would have to be true for it to maintain internal
   coherence.
B5 HONESTY: this is a STRUCTURAL question about a vertex, not an electron model.
   No result here licenses any claim about the electron's size, mass or form
   factor. Say so.
