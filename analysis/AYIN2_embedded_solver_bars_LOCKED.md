# COMMISSION AYIN-2 -- EMBEDDED-CORE SOLVER FEASIBILITY (BARS, LOCKED)

*Locked 2026-08-11, before assessing. The reviewer's ELEC-098: can the
C_pin calculation be reformulated with infinite-medium or
symmetry-preserving boundary treatment WITHOUT changing the registered
strand physics? Run before provisioning a 30-100x brute-force job.*

## The non-negotiable constraint

Any reformulation must preserve FND-STRAND-001 EXACTLY: literal
inextensible curves (exact length projection, not stiff springs),
bending, finite smooth contact Ac/(1+(r/sigma)^4), no crossing axiom.
**A method that linearizes, softens, or coarse-grains the registered
mechanics is not a cheaper version of the calculation -- it is a
different calculation**, and must be reported as failing this audit even
if it is numerically attractive.

## The three routes, assessed separately

- **R1 SYMMETRY-COMPATIBLE FAR-FIELD BOUNDARY.** Does a boundary
  treatment exist that restores the O_h environment the free-surface box
  destroys? Assess specifically whether periodic boundary conditions on
  a cubic cell are compatible with the three-family weave, and what NEW
  artifact they introduce in place of the free surface.
- **R2 GREEN-FUNCTION / EMBEDDING.** Relax only the near-core region and
  handle the exterior analytically. Assess against the registered
  physics: a Green-function treatment presumes LINEAR response of the
  exterior. Determine whether the registered mechanics supply that, and
  say plainly if they do not.
- **R3 PERTURBATIVE ANISOTROPY.** Compute the orientation dependence as
  an energy correction rather than relaxing a full box per orientation.
  Determine at what order the relaxation contributes, and therefore
  whether one relaxation can serve many orientations.

## Verdict grammar (pre-committed)

- **FEASIBLE**: at least one route preserves the registered physics and
  materially reduces cost. Specify it and the expected saving.
- **PARTIAL**: a route reduces cost but only for part of the problem.
  State which part and what remains.
- **INFEASIBLE**: no route preserves the physics. The brute-force case
  is then justified and this audit is what justifies it.

## Standing rules

- Cost savings claimed must be arithmetic, not impressions.
- If a route is attractive but changes the physics, it is reported as
  FAILING, with the change named. The audit exists to prevent a cheap
  wrong calculation from displacing an expensive right one.
- No C_pin value may be quoted from this commission under any route.
  This is a feasibility audit, not the measurement.
