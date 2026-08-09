# Task prompt for a dedicated construction effort (e.g. Fable 5): derive the rope mode-overlap coupling

You are being asked to solve one specific, self-contained physics-modeling problem.
Read the whole brief before starting. The single most important rule is at the end
(the anti-fitting rule); a solution that violates it is worthless even if every
number matches.

## Background you need (self-contained)

A speculative classical model ("the Rope Hypothesis") represents each atom as a
localized standing-wave / vortex pattern of an underlying elastic network of
strands under tension. Two neighbouring atoms' patterns overlap in the region
between them. The model claims — but has never derived — that the energy of this
overlap is what produces: covalent bond strengths, nuclear binding energies, and
ferromagnetic spin alignment. It is currently only named, never written as a
formula. Your job is to write that formula, derived from the network mechanics,
and prove it is not fitted.

The network primitives you may build from (and ONLY these, plus standard
continuum mechanics):
- a strand tension T [N] (longitudinal stress along a strand),
- a linear mass density mu [kg/m],
- a per-length phase/torsional stiffness lambda (resistance to twisting the
  two-strand helix),
- a helical pitch vector field and its gradient,
- each atom modeled as a network mode field psi_i(x) (a localized standing
  vortex/torsion pattern) with an orientation (its moment axis) and a sense.

## What you must produce

A concrete functional **E_overlap[psi_1, psi_2]** = the interaction energy of two
atoms' mode fields as a function of separation r and relative orientation, derived
from the network elastic energy of two OVERLAPPING mode patterns (e.g. the elastic
+ torsional energy density integrated over the overlap region). It must be written
in closed form (or as a well-defined integral) in terms of the primitives above,
with NO free parameter whose only job is to select a sign or match a target.

## Hard requirements (each is checkable)

1. **Long-range limit — must MATCH an already-computed result.** When the two mode
   fields barely overlap, E_overlap must reduce to the known swirl-field/dipolar
   strain term: in 2D, two vortices of sense s_i,s_j at separation d contribute
   E_field = (1/2pi) * s_i * s_j * ln(L/d) (L = system scale). Equivalently the
   3D magnetostatic dipole tensor [m_i.m_j - 3(m_i.n)(m_j.n)]/r^3. Your functional's
   large-r tail MUST agree with this. (This is the consistency anchor; it is
   already validated separately, so you cannot get it wrong.)

2. **Scale — must FALL OUT, not be inserted.** At atomic separation (~2-3 Angstrom)
   the coupling must come out order 0.1 eV (the exchange/bond scale that beats room
   temperature ~0.025 eV). You may use realistic values of T, mu, lambda; you may
   NOT insert a prefactor chosen to hit 0.1 eV.

3. **Sign from mechanics, not choice.** Whether the short-range coupling favors
   aligned (ferro) or anti-aligned (antiferro) neighbours must follow from the
   geometry of how two mode patterns elastically mesh — not from a sign you pick.

## The anti-fitting validation harness — THE MOST IMPORTANT PART

A functional that reproduces the magnetic sign but is fitted to do so is a
FAILURE. To prove it is derived, the SAME functional, with the SAME constants and
NO per-case retuning, must independently reproduce two facts it was not built for:

- **Chemistry check:** the sigma > pi bond-strength ordering — head-on (axial)
  mode overlap must come out STRONGER than side-on (lateral) overlap, purely from
  the orientation dependence of E_overlap.
- **Nuclear check:** the binding-energy-per-nucleon trend that RISES to a peak near
  iron-56 (total binding ~492 MeV for Fe-56) and then DECLINES — i.e. overlap
  energy maximized at an optimal packing density, then falling as patterns
  over-crowd. The trend/peak location is what matters, not exact MeV.
- **Magnetism check:** for a given lattice geometry, E_overlap + the long-range
  field term (req. 1) must combine to give the observed magnetic order.

You must run all three checks with one frozen functional and report all three
outputs together. If you retune anything between checks, you have failed.

## Deliverables

1. The derivation of E_overlap from the network elastic energy, step by step.
2. The closed-form / integral functional, with every constant traced to T, mu,
   lambda, or geometry.
3. A single program that: (a) verifies the long-range limit matches req. 1
   numerically; (b) evaluates the atomic-scale magnitude (req. 2); (c) runs the
   three harness checks with ONE frozen functional and prints all outputs.
4. An explicit honesty statement: which results fell out vs. which required
   assumptions, and every place a constant or sign could have been chosen.

## If you cannot derive it

Say so plainly. A correct "here is exactly where the derivation blocks, and why"
is a valuable result. A fitted functional dressed as a derivation is not — it will
be caught by the harness and rejected. Do not invent a formula that only reproduces
the one target you were aiming at.
