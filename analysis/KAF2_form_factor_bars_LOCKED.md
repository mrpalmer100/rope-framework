# COMMISSION KAF-2 -- THE CORE'S FORM FACTOR AT THE MESH SCALE (BARS, LOCKED)

*Locked 2026-08-11, before computing. ELEC-092 narrowed the electron's
spin-degeneracy question to one determinable number: the asymptotic
behaviour of ELEC-074's core form factor at the reciprocal-lattice
wavevector G = 2 pi/a. The two regimes differ by 218 orders and there is
no middle ground. This commission computes it.*

## What is being transformed (fixed before computing)

ELEC-074's exact solution, in closed form:

    p(x) = x^-2 / sqrt(1 - x^-4),   x = r/r0 >= 1,   p = 0 for x < 1

p is the transverse slope; the physical density whose Fourier transform
sets the coupling to the lattice is the ENERGY DENSITY, which in the
registered lab parametrization is

    e(x) = sqrt(1 + p(x)^2) - 1

(the same density ELEC-074 integrated to get its finite energy). The
transform is the 3D radially symmetric one:

    S(q) = (4 pi / q) * integral_0^inf  e(r) sin(q r) r dr

evaluated at q = G = 2 pi/a, i.e. at q r0 = 2 pi g with g = r0/a.

## The question, stated so it cannot be fudged

As q r0 -> infinity, does |S(q)| fall

- **EXPONENTIALLY** (smooth regime) -- the spin question closes, ELEC-091
  stands, degeneracy safe by ~200 orders; or
- as a **POWER LAW** (sharp regime) -- then the EXPONENT must be
  extracted numerically, not assumed, and confronted. ELEC-092's
  illustrative exponent 4 is INADMISSIBLE as an input here.

## Method (pre-committed)

1. Compute S(q) numerically over a wide range of q r0, with the
   oscillatory integral handled by a method whose convergence is
   demonstrated (report the check).
2. Fit log|S| against log(q r0) AND against q r0. Whichever is linear
   over the asymptotic range is the regime. Report BOTH fits and their
   residuals -- the discrimination must be visible, not asserted.
3. If power law, extract the exponent by regression over the asymptotic
   decade and state its uncertainty.
4. Evaluate at the registered g = 82.6 and 108.0 and confront against
   the 1e-6 eV bar carried over from ELEC-092.

## Verdict grammar (pre-committed)

- **SMOOTH**: exponential falloff. The debt is PAID, ELEC-091's
  resolution stands, spin degeneracy is safe.
- **SHARP-SAFE**: power law, but the exponent is large enough that the
  pinning still clears the bar. Report the margin.
- **SHARP-FATAL**: power law with the pinning above the bar. **ELEC-091's
  charge-fixes-spin resolution FAILS and the two-orientations reading of
  spin fails with it.** Registered Failed-and-kept, no rescue attempted
  in this commission.

## Standing rules

- The exponent is measured, never chosen.
- If the numerics are ambiguous the verdict is UNDERSPECIFIED; a noisy
  fit may not be rounded toward a convenient regime.
- Whatever lands is registered, including against ELEC-091, which is one
  commission old and this session's own work.
