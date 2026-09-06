# COMMISSION CHET-2 -- RESULTS: INTERIOR-CONSTRAINED, WITH THE HARD CORE EXPLAINED AND A NEW STRUCTURAL FACT DERIVED

*Adjudicated 2026-08-11 after bar lock
(analysis/CHET2_hollow_interior_bars_LOCKED.md). Benchmark:
benchmarks/foundations/chet2_hollow_interior.py. The target ELEC-088 and
ELEC-089 named from opposite directions.*

## C1 -- the boundary condition, read geometrically

ELEC-074's first integral is r^2 F(p) = C with F(p) = p/sqrt(1+p^2) and
p = psi' the transverse slope. **A slope is the tangent of an angle.**
Writing p = tan(theta), with theta the strand tangent's tilt from the
reference axis:

    F(tan theta) = sin(theta)

so the first integral is not an algebraic curiosity but an exact
geometric statement:

    **r^2 sin(theta) = C,   i.e.   sin(theta) = C / r^2**

| r/r0 | sin θ | θ |
|---|---|---|
| 3.00 | 0.111 | 6.4 deg |
| 2.00 | 0.250 | 14.5 deg |
| 1.50 | 0.444 | 26.4 deg |
| 1.20 | 0.694 | 44.0 deg |
| 1.05 | 0.907 | 65.1 deg |
| 1.00 | 1.000 | **90 deg** |

**The hard core is the locus where the strand tangent has turned through
a full right angle.** The "divergence of p at the boundary" that ELEC-074
reported is not a pathology at all -- p = tan(theta) diverges because
theta reaches 90 degrees, which is a perfectly ordinary geometric
configuration. The apparent singularity was an artifact of the
parametrization, exactly as ELEC-073's cusp was an artifact of
truncation. **Two apparent singularities in this sector, both artifacts,
both now explained.**

## C2 -- the hollow is KINEMATIC, and therefore universal

sin(theta) = C/r^2 has no solution for r^2 < C because **sin(theta) <= 1
always**. That is a bound on an angle, not an energetic accident.

Consequence, and it is the strong form: **the hard core does not depend
on T0, on k, on the packing floors, or on any material parameter.** It
cannot be tuned away, moved, or hidden by a different parameter choice.
Any radial solution of this first integral terminates at finite radius.
The hollowness is universal for the class -- which is why ELEC-074 found
it and why no choice of constants would have concealed it.

This upgrades the hollow from "what the solution happens to do" to "what
the geometry permits".

## C3 -- what the boundary forces, and what it does not

**Forced (three exclusions, each from the boundary value):**
1. Strands **cannot pass radially through the core.** A radial crossing
   requires a tangent with a radial component, i.e. sin(theta) < 1 at
   r0, contradicting the boundary value.
2. The field **cannot be continued inward** as any radial profile of
   this class -- excluded kinematically by C2.
3. The exterior **meets r0 tangentially**; the interior is not merely
   undefined there, the solution arrives parallel to the surface.

**Therefore: strands reaching r0 run TANGENT to the core boundary.** The
core is not a hole the strands avoid, nor a body they wrap around -- it
is the surface on which the winding's strands become tangential.

**NOT determined, stated plainly per the bar:** the tangential direction
field ON that sphere is not fixed by this argument.

## THE NEW STRUCTURAL FACT: the core cannot be isotropic

Combining C3's tangency with the hairy-ball theorem: a continuous tangent
vector field on S^2 must have zeros of total index 2 (Euler
characteristic 2) -- two index-1 points, or one index-2 point.

**The core therefore has distinguished points. It cannot be spherically
symmetric.** That is a derived structural fact the corpus did not carry,
and it is a constraint on any future interior model: whatever fills the
hollow must accommodate at least two defect points (or one of index 2)
on its boundary.

It also predicts an **axis** -- a pole pair is the generic solution --
which is suggestive next to the electron's spin and next to ELEC-041's
registered 18.3:1 ASYMMETRY and 275:1 PLANARITY. That the clasp geometry
is strongly non-spherical is now a point of contact rather than a
coincidence. **The identification is still not made** (ELEC-088), and
this commission does not make it; but the two pictures have moved from
"unrelated" to "sharing a derived structural requirement".

## VERDICT: INTERIOR-CONSTRAINED

Per the pre-committed grammar, and held to it: the boundary condition
forces real properties of the interior (tangency; no radial crossing; no
smooth continuation; at least two boundary defects; non-isotropy) without
determining the configuration. Registered as a constraint, not dressed as
a solution.

## What remains, named

The tangential direction field on the core sphere. Determining it
requires either (a) an energetic principle selecting among tangent
fields with index-2 zero sets, or (b) matching to an interior model --
for which ELEC-041's clasp is now a better-motivated candidate than it
was this morning, because it is non-spherical in the way the theorem
requires.

## Assumptions used, stated where used

- **Axisymmetry**, inherited from the registered profile's own
  construction (ELEC-073/074) -- used in C3 to place the boundary
  tangent in the sphere's tangent plane.
- **Continuity of the strand tangent field** on the boundary sphere --
  used for the hairy-ball argument. A configuration with a torn tangent
  field would evade it, and would owe an account of the tear.
