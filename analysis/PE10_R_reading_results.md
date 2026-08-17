# THE R READING (PE10) -- RESULTS (2026-08-16)

A reading session on FND-124's named next-order (1). Verification
arithmetic inline (four checks, machine-exact).

VERDICT: R-DERIVED + NAMED CORRECTION TO FND-124.

## The reading
The registered closed forms kappa = (pi/p) sin 2psi and
tau = (2pi/p) cos^2 psi are, JOINTLY, exactly the standard Frenet
helix under the psi-from-axis convention (kappa = sin^2 psi / R,
tau = sin psi cos psi / R) if and only if
    R = p tan(psi) / (2 pi).
All four registered values reproduce machine-exactly. At the
worst-case pitch p = a_f:
    R_1 = 0.11254 a_f   (level 1, psi_1 = 35.2644 deg)
    R_2 = 0.26959 a_f   (level 2, psi_2 = 59.4444 deg)
The winding radii were derivable from registered structure all
along; the parametrization is fixed by the kappa+tau PAIR.

## NAMED CORRECTION (to FND-124, the day's twelfth catch)
FND-124's "R-GAP" finding -- "both natural conventions checked,
they disagree" -- was an OPERATOR ANALYSIS ERROR: the stage-1 check
tested the two closed forms SEPARATELY against single-convention
guesses instead of solving the joint system. The joint system is
consistent and unique. The R-gap portion of FND-124 is corrected by
name; its rigidity demand and the Bloch-L charter SURVIVE
untouched, and the charter's input list now CLOSES.

## Consequence for BLOCH-L: inputs complete
Angles/pitch (registered), rod inputs (granted, tripwire), mu_f
(forced), R_1/R_2 (derived above). The commission is runnable.
DISPLAY, heavily caveated and not spent: a one-line load-path
estimate at the derived R suggests the bending and stretch paths
are COMPARABLE near the derive-point -- if right, Bloch-L is
decisive rather than confirmatory, and the rigidity demand is a
live check, not a formality. The estimate uses uncontrolled O(1)
factors and decides nothing.

## REFUSALS
Clean-room held (targets absent from the reading); the display
estimate not spent; condition 4 unchanged.
