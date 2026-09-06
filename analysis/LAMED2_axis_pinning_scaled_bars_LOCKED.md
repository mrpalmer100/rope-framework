# COMMISSION LAMED-2 -- THE AXIS-PINNING EXPERIMENT, SCALED (BARS, LOCKED)

*Locked 2026-08-11, before computing. The reviewer's protocol adopted with
attribution and with one correction, run at tractable core sizes with an
extrapolation to the physical one.*

## The reviewer's protocol, and the correction

**As proposed:** rotate the same relaxed core through many orientations
relative to the microscopic mesh, minimize all other degrees of freedom,
measure Delta E_pin = E_max - E_min, refine, extrapolate.

**THE CORRECTION, stated because the result would otherwise be vacuous:**
the reviewer proposes extrapolating "under refinement". The mesh spacing
a is NOT a numerical discretization -- it is the registered physical
strand spacing. Refining a away computes the pinning of a continuum,
which is zero by construction and answers nothing. Therefore:

- numerical refinement (angular sampling, relaxation convergence, box
  padding) is done at FIXED physical a, and must be shown not to move
  the answer;
- the EXTRAPOLATION is in the physical ratio s = r0/a, from tractable
  values to the registered s = 82.6-108.0.

## Why an extrapolation is admissible here

ELEC-093 measured the core's form-factor envelope falling as a power law
with n = 1.4615 (sharp-edge signature, 3/2). A power law extrapolates
over a decade with controlled error; an exponential would not need to.
The extrapolation's exponent is therefore ITSELF a check against
ELEC-093, and the two must be reported together.

## The computation

- **L1** Build a minimal anisotropic core proxy: ELEC-091's structure --
  azimuthal boundary circulation with two polar defects on a sphere of
  radius r0 -- embedded in the registered three-family mesh of spacing a.
  The proxy's construction is stated in full; it is NOT the registered
  electron and the claim must say so.
- **L2** For each of several s = r0/a, scan the axis orientation over the
  mesh's symmetry-inequivalent directions, relax, and record
  Delta E_pin / E_core.
- **L3** Fit Delta E_pin/E vs s on log-log AND semi-log; report both
  residuals; extrapolate the winner to s = 82.6 and 108.0.
- **L4** Confront against the 1e-6 eV degeneracy bar carried from
  ELEC-092.

## Verdict grammar (pre-committed)

- **UNPINNED**: extrapolated Delta E_pin below the bar. ELEC-091's spin
  resolution stands.
- **PINNED**: at or above the bar. ELEC-091's two-orientations reading
  of spin FAILS; registered Failed-and-kept without rescue here.
- **PROXY-LIMITED**: the scan resolves no orientation dependence above
  numerical noise at any tractable s, so no exponent can be fitted. Then
  the experiment BOUNDS the pinning rather than measuring it, and the
  bound is what is registered.

## Standing rules

- The proxy is a proxy. Every conclusion inherits that and must say so.
- If numerical noise exceeds the signal, that is PROXY-LIMITED and may
  not be reported as UNPINNED -- absence of a resolvable signal is not a
  measurement of zero.
