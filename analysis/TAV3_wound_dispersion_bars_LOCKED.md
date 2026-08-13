# COMMISSION TAV3 -- THE WOUND-CARRIER DISPERSION CHECK: BARS, LOCKED BEFORE COMPUTING

Locked 2026-08-12, before any computation. The owed successor to
SHIN2 (FND-083). Charter: test whether a medium of hierarchically
wound fine carriers supports SHORT-WAVELENGTH transverse propagation
that is (i) transmitted, (ii) straight-line at speed ~c, and
(iii) direction-independent -- FND-REL-002's isotropy demand as the
acceptance bar. The author has pre-authorized adoption of
GRANT-CANDIDATE-SUBSTRUCTURE IF AND ONLY IF this check passes; a
failure is registered, kept, and NOT adopted.

## The physical question, stated honestly

SHIN2 established coverage geometry. What it did not establish: at
wavelengths near the fine spacing a_f, the wound medium is
INHOMOGENEOUS at scales between a_f and the pitch (the local fiber
axis rotates with position). A short wave crossing such a medium can
be scattered, slowed, guided, or transmitted cleanly. Timing data
(LIV bounds: PeV photons arrive with negligible energy-dependent
delay) additionally excludes the guided-path reading (0.008c) --
transport must be THROUGH the medium, near c, straight.

## The instrument (Modeled-grade engine test, 2D)

A 2D mass-spring lattice, N x N nodes, out-of-plane displacement
(scalar transverse field):
- Strong along-fiber coupling K_par (tension channel) along a LOCAL
  fiber direction that ROTATES with position: angle
  phi(x, y) = 2 pi (x / P1) + 2 pi (y / P2), the two-level winding
  proxy (two incommensurate rotation periods P1 = 24 a_f,
  P2 = 60 a_f, declared here at lock).
- Weak crossing coupling K_x = 0.08 K_par isotropic to the four
  neighbors (the registered crossing channel, s/a-class).
- Implementation: each node couples to its 8 neighbors with weight
  K_x + K_par cos^2(theta_nb - phi(x, y)), theta_nb the bond angle;
  row-sum normalized so the homogeneous long-wave speed is 1.
- CONTROL W0: phi = 0 everywhere (straight fibers) -- must show the
  strong anisotropy the conviction requires (validates instrument).

## Measurements and bars, locked

- M1 TRANSMISSION: Gaussian pulse, carrier wavelength lambda = 6 a_f
  (short: one fine cell is beyond a discrete lattice's reach; 6 a_f
  is the shortest clean carrier the discretization supports, declared
  at lock), launched in 8 directions (every 45 deg, plus the two
  winding-symmetry-breaking diagonals). Transmitted energy fraction
  through a slab of thickness 4 max(P1, P2) after steady passage.
  BAR: >= 0.5 in every direction.
- M2 SPEED ISOTROPY: group arrival time of the pulse centroid across
  the slab per direction; speed spread
  (max - min) / mean <= 0.05 across the 8 directions.
  BAR: <= 0.05 (a 5 percent engine-level bar; the physical
  FND-REL-002 demand is far tighter and is NOT claimed met by this
  test -- this bar detects order-unity anisotropy, the failure mode
  the conviction alleges).
- M3 STRAIGHTNESS: transverse centroid drift of the pulse at exit
  <= 0.1 of the slab thickness, every direction.
- W0 CONTROL: the straight-fiber medium must FAIL M1 or M2 for
  off-axis directions (transmission or speed collapsing off-axis),
  reproducing the slab obstruction. If the control does not fail,
  the instrument cannot see the disease and the commission returns
  INSTRUMENT-INVALID (kept).

## Verdict grammar, pre-authorized

- PASS (all of M1-M3 at the wound medium AND the control failing as
  required): the check passes; GRANT-CANDIDATE-SUBSTRUCTURE is
  ADOPTED per the author's pre-authorization, as a separate author's
  act with the price sheet on its face.
- FAIL any bar: registered Failed-and-kept; NO adoption; the
  candidate returns to the desk with the failing mode named.
- INSTRUMENT-INVALID: no adoption, no conviction; successor owed.

## Discipline clauses

- No bar-shopping: P1, P2, K_x/K_par, lambda, the direction set, and
  every threshold above are final.
- Honest scope carried onto any claim: 2D scalar proxy; two
  polarizations, 3D winding, and the true PeV-scale ratios are NOT
  simulated; a PASS upgrades the candidate's dispersion status from
  unexamined to engine-supported, nothing more. FND-REL-002's full
  re-derivation remains owed at Derived grade regardless of outcome.
- The A4b conditionality (light = collective branch) and the three
  underived parameters carry onto the grant text verbatim if adopted.
