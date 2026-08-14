# MEASUREMENT PROPOSAL: SU(3) ADJOINT STATIC POTENTIAL AT HALF-PERCENT PRECISION, 0.5-1.0 fm

*A technically routine, quarter-century-overdue lattice measurement
that decides a registered theoretical constant. Self-contained; no
acceptance of the sponsoring framework is required to perform or to
use it. Contact: Mark Palmer (rope-framework repository).*

## The measurement

Compute the SU(3) pure-gauge static potential for the ADJOINT
representation (optionally sextet and 15a as cross-checks) against
the FUNDAMENTAL, in 4d, at source separations r = 0.5-1.0 fm, with
combined statistical-plus-systematic precision of 0.5 percent or
better on the relative Casimir-scaling deviation

    delta(r) = [V_adj(r) - (C_adj/C_f) V_f(r)] / [(C_adj/C_f) V_f(r)],
    C_adj/C_f = 9/4,

continuum-extrapolated (three or more spacings). The window is
screening-safe: adjoint string breaking sits near 1.2 fm and the
gluelump channel is separable by standard variational methods.

## Status of the field (verified 2026-08)

The best existing primary bound is Bali, PRD 62, 114503 (2000):
violations <= 5 percent to 1 fm, continuum-extrapolated,
anisotropic Wilson action. A literature sweep (this repository,
FND-105) confirms NO tighter admissible SU(3) 4d determination has
been published in the twenty-six years since. Deldar (PRD 62,
034509) sits at 5-15 percent; the precision work since has gone to
G2 and to 2+1 dimensions. Sub-percent precision here is unclaimed
territory reachable with 2000-era methodology on 2026-era machines.

## Methodology pointer (nothing exotic required)

- Pure-gauge SU(3), Wilson or improved action; L ~ 2-2.5 fm boxes.
- Adjoint Wilson/Polyakov correlators via multilevel (Luscher-Weisz)
  variance reduction -- the adjoint signal decays with ~(9/4) sigma,
  and multilevel is what makes the 1 fm range affordable; HYP or
  gradient-flow smearing for the static lines.
- Variational basis including the gluelump-pair channel to isolate
  the unbroken-string state near the top of the window.
- Three-plus spacings, a^2-extrapolation; quote delta(r) with full
  error budget across the window.

Resource scale: a modest modern GPU allocation; weeks, not years.

## What each precision tier buys (pre-committed, PRD-independent)

| precision e on delta | consequence in the sponsoring framework   |
|----------------------|-------------------------------------------|
| 5 percent (existing) | floor kappa_pack >= 12.5 (current state)  |
| 1.25 percent         | decides/excludes the kappa = 50 reading   |
| 0.5 percent          | floor 125; strong-form discrimination     |
| 0.25 percent         | full test: both readings adjudicated      |

The framework's two pre-registered predictions are delta = -1.25
percent (kappa_pack = 50) and delta = -0.25 percent (kappa_pack =
250), both NEGATIVE (softened below exact Casimir scaling). The
complete verdict grammar, including the kill conditions the
framework accepts against itself and a sign clause under which a
resolved POSITIVE deviation falsifies the derived mechanism
outright, is pre-registered with no adjustment permitted:
analysis/TET3_adjoint_bands_PREREGISTERED.md. Whatever this
measurement finds, it decides something -- for Casimir-scaling
phenomenology generally, and against fixed, published numbers for
this framework specifically.

## Why it is worth a group's time independent of any framework

A sub-percent continuum determination of adjoint Casimir scaling in
the confining window is a standing gap in the confinement
literature: it discriminates among stochastic-vacuum, center-vortex,
and flux-tube pictures at a level the 2000 data cannot, and it has
been cited as the missing measurement by multiple confinement
reviews. The framework attached to this proposal simply happens to
be the party that pre-committed exact numbers to it.
