# COMMISSION AYIN-2 -- RESULTS: FEASIBLE. TWO ROUTES PRESERVE THE PHYSICS, ONE IS REJECTED, AND THE BOTTLENECK IS REFORMULABLE RATHER THAN MERELY LARGE

*Adjudicated 2026-08-11 after bar lock
(analysis/AYIN2_embedded_solver_bars_LOCKED.md). Benchmark:
benchmarks/foundations/ayin2_embedded_solver.py. The reviewer's ELEC-098,
run before provisioning a 30-100x brute-force job. No C_pin value is
produced or quoted, per the bar.*

## R1 -- symmetry-compatible far-field boundary: **PASSES**

The contaminating artifact ELEC-097 identified is the FREE SURFACE: once
the inclusion protrudes past the strand grid, the O_h environment
ELEC-096's harmonic classifies is simply absent, so the angular data
measure box geometry.

**Periodic boundary conditions on a cubic cell of side L = N a fix
exactly that.** The three strand families lie along the cube axes and
are commensurate with the cell for any integer N, so the periodic image
lattice is itself cubic and the symmetry group of the periodic system is
**O_h -- precisely the group the harmonic is built on.** PBC restores the
symmetry the free box destroys.

**New artifact, stated honestly:** the inclusion now interacts with its
periodic images. But that artifact is CONTROLLED -- it decays with L and
extrapolates in 1/L -- where the free-surface artifact is uncontrolled
AND orientation-dependent, since the protrusion differs by axis. That
orientation dependence is very likely what produced ELEC-097's sign flip.

**Physics preserved:** PBC changes the domain, not the mechanics.
Inextensibility, bending and contact are all local or along-strand and
are unaffected by identifying faces. **And critically, PBC removes the
nrings >= s requirement entirely**, since there is no free surface for
the inclusion to protrude through -- which was the cost driver that made
the box grow with s.

## R2 -- Green-function / embedding: **FAILS on physics**

An embedding treatment requires the exterior response to be LINEAR so it
can be folded into a kernel. The registered mechanics do not supply that:

- inextensibility is an exact constraint enforced by projection -- a
  nonlinear, NONLOCAL operation along each whole strand, not a linear
  response;
- the contact kernel Ac/(1+(r/sigma)^4) is manifestly nonlinear;
- **a stiff-spring linearization was already tried and REJECTED** in the
  settler work as numerically outside the inextensible regime (10 percent
  stretch, audit-caught).

A Green-function exterior would linearize precisely the constraint the
corpus insisted on keeping exact. **Per the bar, that is reported as a
failure however attractive the cost saving** -- it would be a different
calculation wearing the same name.

## R3 -- perturbative anisotropy: **PASSES, conditionally**

At a relaxed configuration the energy is stationary with respect to
strand displacements. So rotating the inclusion changes the relaxed
energy, to FIRST order, by the change in interaction energy evaluated on
the UNCHANGED strand configuration -- the relaxation's own response
enters only at SECOND order (Hellmann-Feynman).

**One relaxation can therefore serve many orientations:** 9 relaxations
become 1 relaxation plus 9 energy evaluations, and an evaluation costs
about one relaxation step. The saving approaches the full orientation
count.

**Limit, stated:** first order captures the anisotropy only if the
relaxation response is not itself strongly orientation-dependent. That
requires a control -- one fully relaxed orientation compared against its
perturbative estimate. A single run, not a programme.

## VERDICT: FEASIBLE

R1 and R3 attack the two INDEPENDENT cost drivers and neither changes
FND-STRAND-001:

| driver | fix | effect |
|---|---|---|
| box must grow with s (nrings >= s) | R1, PBC | requirement removed; O_h restored |
| one relaxation per orientation | R3, perturbative | N relaxations -> 1 + N evaluations |

**The reviewer's instinct is vindicated: the bottleneck is reformulable,
not merely large.** Spending 30-100x on brute force before trying this
would have been the wrong call.

## The chartered next brick, now well-posed

**Re-run the C_pin extraction under PBC with the perturbative orientation
scan**, with three preconditions inherited from this arc:
1. the order-4 projection estimator (ELEC-097), not max-minus-min;
2. the 3/2 exponent as FIXED INPUT (ELEC-096, the reviewer's point about
   exponent-prefactor compensation);
3. a noise floor and a 1/L image-artifact extrapolation, both measured
   BEFORE any signal is read -- the ordering ELEC-097 violated and logged.

If that still fails, the brute-force case is then genuinely justified,
and this audit is what justifies it rather than impatience.

## Attribution

The three routes are the reviewer's, framed exactly as they proposed.
Their judgement that this audit should precede provisioning was correct:
one of their routes is rejected on physics grounds that only a check
would have surfaced, and two survive and compose.
