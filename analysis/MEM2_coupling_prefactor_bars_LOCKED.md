# COMMISSION MEM-2 -- THE COUPLING PREFACTOR ON THE REGISTERED ENGINE (BARS, LOCKED)

*Locked 2026-08-11, before computing. ELEC-094 left the electron sector's
rank-1 question: the orientation-energy SCALING is established at 3/2 by
two independent routes, but the PREFACTOR rests on a phase-overlap model
that commission constructed. This computes it on the registered engine
instead, so the confrontation stops depending on an invented number.*

## What must be used, and what may not

**MUST:** FND-STRAND-001's engine as registered and as implemented in
benchmarks/foundations/matter062_settler.py -- literal inextensible
curves (exact length projection, not stiff springs), bending KB, finite
smooth contact Ac/(1+(r/sigma)^4), no crossing axiom. Parameter values
KB = 0.6, AC = 1.0, SIG = 0.30 are the registered settings and are used
unchanged.

**MAY NOT:** any coupling model, phase-overlap ansatz, or form factor
introduced by this commission. The prefactor must come out of relaxing
strands, not out of a formula for how strands couple. If the engine
cannot produce it, the answer is UNDERSPECIFIED and the sector waits.

## The measurement

A core is represented on the engine as an ANISOTROPIC INCLUSION with an
axis -- the minimal realization of ELEC-091's structure available to a
contact-based engine: a prolate/oblate rigid inclusion whose symmetry
axis can be oriented relative to the strand families. The strands relax
around it exactly as in the registered settler run.

- **M1** Relax the ambient strands around the inclusion at several axis
  orientations relative to the mesh ([100], [110], [111] at minimum).
  Measure the relaxed total energy at each.
- **M2** Delta E_pin = E_max - E_min across orientations, normalized by
  the inclusion's own deformation energy (the same relaxation's total
  strain energy), giving a DIMENSIONLESS prefactor at that s.
- **M3** Repeat at 2-3 inclusion sizes to confirm the ratio behaves as
  ELEC-094's 3/2 law over the accessible range. Confirmation is a check,
  not a fit -- the exponent is not re-measured here.
- **M4** Combine the measured prefactor with the doubly-corroborated 3/2
  scaling and extrapolate to s = 82.6/108.0. Confront against 1e-6 eV.

## Numerical honesty requirements (pre-committed)

- The orientation differences will be SMALL. Before reporting any
  Delta E, demonstrate that it exceeds the relaxation's own convergence
  noise -- measured by re-running one orientation from a different seed
  and reporting the spread. **If the signal does not exceed the noise,
  the verdict is NOISE-LIMITED and the result is an UPPER BOUND on the
  prefactor, which is still useful and must be reported as a bound.**
- Energies must be compared at equal relaxation, not equal step count,
  if convergence differs by orientation.

## Verdict grammar (pre-committed)

- **PREFACTOR-MEASURED, PINNED**: prefactor determined, extrapolation
  above the bar. ELEC-091's spin reading FAILS; Failed-and-kept.
- **PREFACTOR-MEASURED, UNPINNED**: below the bar. ELEC-091 stands and
  the debt is finally paid.
- **NOISE-LIMITED**: only a bound. Report the bound and whether it
  suffices to decide.
- **UNDERSPECIFIED**: the engine cannot represent the structure well
  enough to answer. Say so plainly rather than substituting a model.

## Standing rule

The inclusion is a proxy for the core's anisotropy, and every conclusion
inherits that. But the COUPLING is not modelled -- it is whatever the
registered contact energetics produce. That distinction is the whole
point of this commission and must be stated in the result.
