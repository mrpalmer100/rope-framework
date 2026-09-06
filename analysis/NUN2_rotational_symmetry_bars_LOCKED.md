# COMMISSION NUN-2 -- DOES THE THREE-FAMILY WEAVE NECESSARILY BREAK ROTATIONAL SYMMETRY? (BARS, LOCKED)

*Locked 2026-08-11, before computing. An external reviewer identified this
as the question to inspect BEFORE the expensive coupling calculation, and
they are right: if the answer is that pinning must vanish by symmetry, the
prefactor commission is unnecessary; if it must not, the prefactor
commission is decisive. Either way this is cheaper and should come first.*

## The reviewer's framing, adopted

If the electron axis is unpinned, that requires one of three
QUALITATIVELY DIFFERENT mechanisms, and the bar forbids letting them
blur together after the number is known:

- **(A) EXACT CANCELLATION / SYMMETRY PROTECTION:** C_pin = 0 identically,
  by a mechanical or topological identity.
- **(B) STRONG DERIVED SUPPRESSION:** C_pin small but nonzero, with a
  derived reason for its smallness.
- **(C) EMERGENT ROTATIONAL RESTORATION or ORIENTATION AVERAGING:** the
  pinning exists microscopically but is averaged away, e.g. by the
  core's own rotation (ELEC-068's dynamical branch, L* = c/omega).

Each is a different physical claim. The commission must say which, if
any, the registered structure supports, and must not present one as
another.

## The computation

- **N1 THE SYMMETRY GROUP.** Determine the point group of the registered
  three-family weave and whether it contains the full rotation group.
  If it does not, an orientation-dependent energy is GENERICALLY allowed
  and (A) requires a further identity, not merely the lattice symmetry.
- **N2 THE LOWEST ALLOWED ANISOTROPY.** For an axis n embedded in that
  point group, determine the lowest-order rotationally-invariant-breaking
  polynomial in n permitted by the symmetry -- i.e. the leading cubic
  harmonic. Its ORDER is what controls how strongly the pinning is
  suppressed for a nearly-isotropic object, and it is fixed by group
  theory alone, with no dynamics and no proxy.
- **N3 THE DYNAMICAL AVERAGE (mechanism C).** ELEC-068 registers that the
  electron has NO static branch and exists only as a rotating
  configuration. Determine whether rotation about an axis averages the
  N2 harmonic to zero, and if so under what condition on the rotation.

## Verdict grammar (pre-committed)

- **SYMMETRY-FORBIDDEN**: the leading anisotropy vanishes identically.
  Mechanism (A); the prefactor commission is unnecessary.
- **SYMMETRY-ALLOWED, ORDER n**: the anisotropy is permitted at order n.
  The prefactor commission is then decisive and its target order is
  known in advance -- which the reviewer's protocol requires.
- **AVERAGED**: allowed statically, but killed by the registered
  dynamics. Mechanism (C), and the condition must be stated.

## Standing rules

- The 3/2 SCALING is treated as FIXED INPUT and is not re-derived here.
  The reviewer's point is adopted: re-deriving an exponent alongside a
  prefactor lets the two compensate.
- No coupling model, no fitted normalization, no proxy. This is a
  symmetry computation or it is nothing.
