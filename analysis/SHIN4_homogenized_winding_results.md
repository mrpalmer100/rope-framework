# COMMISSIONS SHIN3/SHIN4 -- TIGHT AND HOMOGENIZED WINDING: RESULTS

Executed 2026-08-12 under analysis/SHIN3_tight_winding_bars_LOCKED.md
and analysis/SHIN4_homogenized_winding_bars_LOCKED.md. Benchmarks:
benchmarks/foundations/shin3_tight_winding.py (SHIN4 block appended).

## SHIN3: G1 PASS, G2 FAIL (Failed-and-kept)

G1: the constructibility window is NON-EMPTY at both kappa readings
(psi >= 24 deg at kappa50, >= 19 deg at kappa250; Lorentz spend
1/sin^2 within margin; coverage annulus over 10 percent).
G2: every locked pitch ~ lambda member FAILS -- pitch matching the
wavelength is the RESONANT (Bragg) regime: spread improves toward the
bar as pitch approaches lambda (0.80 -> 0.076) but group transport
collapses (0.03-0.15) and the wave hybridizes (pw weight 0.18-0.31).
The diagnosis sharpens the requirement one final step: homogenization
needs pitch WELL BELOW the wavelength, p <= lambda/4.

## SHIN4: PASS at (P1, P2) = (3, 4), |k| = 2 pi/24

Control valid (straight spread 0.45 at the same wavelength). Wound:
- B2 phase-speed spread 0.0036 (bar 0.05) -- isotropic to 0.4 percent;
- B1 min group speed 0.856 (bar 0.3);
- B3 group-angle error 0.3 deg (bar 15);
- plane-wave weight 0.92: the propagating mode IS the plane wave.
Isotropic speed factor 0.790 (the direction-averaged stiffness),
absorbed by the tension compensation already priced in G1's window.

## The completed structural statement

The photon sector's repair candidate now reads, in full: fine strands
(redistribution: zero Lorentz cost, FND-083), OVER-RESOLVED so
a_f <= lambda_PeV/4 (free: redistribution is m-independent), wound at
two levels with pitch between a_f and lambda/4 and pitch angles inside
the G1 window. In that regime the medium is transparent, isotropic,
and straight-propagating at the short wavelength by measurement on a
validated instrument, while the coarse anchor physics is untouched.
Loose winding (FND-084) and resonant winding (SHIN3) are both
registered exclusions bracketing the passing regime from above.

## Owed at Derived grade regardless (carried onto the grant)

FND-REL-002's re-derivation on wound carriers; the 3D two-polarization
instrument; the bending cost (kb unscaled); provenance of m, n_sub,
and both pitches (all currently chosen-to-work, not derived).
