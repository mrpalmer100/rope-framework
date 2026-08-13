# COMMISSION TAV3B -- THE WOUND-CARRIER BLOCH CHECK: BARS, LOCKED BEFORE COMPUTING

Locked 2026-08-12 after TAV3's time-domain instrument returned
INSTRUMENT-INVALID (no clean propagation in its own control; verdict
taken, engine retired for this question). Same physical question,
deterministic instrument: Bloch eigenanalysis of the wound supercell.
The author's adoption pre-authorization carries over unchanged: adopt
on PASS, register-and-keep on FAIL.

## Instrument

Scalar transverse field on a 2D lattice; supercell P1 x P2 = 24 x 60
sites with local fiber angle phi(x,y) = 2 pi x/P1 + 2 pi y/P2; bond
weights K_x + K_par cos^2(theta_nb - phi), K_x/K_par = 0.08, eight
neighbors, metric-weighted diagonals, global normalization set so the
STRAIGHT medium's along-fiber phase speed at small k is 1.
Dynamical matrix D(k) for Bloch vector k; eigenvalues omega^2.
CONTROL W0: phi = 0, same machinery.

## Measurements and bars, locked

At |k| = 2 pi / 6 (the locked short wavelength), 8 directions
(45-degree set):
- B1 PROPAGATION: in every direction, at least one Bloch band with
  real omega and group speed |d omega/d k| >= 0.3 exists within the
  transverse acoustic band family. BAR: all 8 directions.
- B2 SPEED ISOTROPY: taking per direction the band maximizing group
  speed within the acoustic family, phase-speed spread
  (max - min)/mean <= 0.05.
- B3 STRAIGHTNESS: angle between group velocity (finite-difference
  gradient of omega over k) and k <= 15 degrees in every direction.
- W0 CONTROL: the straight medium at the same |k| must show
  order-unity direction dependence (phase-speed spread > 0.3) or a
  direction with no propagating acoustic mode. Required for
  instrument validity.

## Verdict grammar, pre-authorized
PASS (B1-B3 + valid control) -> adoption per the author's standing
authorization, as a recorded author's act with the full price sheet.
FAIL any bar -> Failed-and-kept, no adoption.
Control invalid -> INSTRUMENT-INVALID again, no adoption, question
returns to the desk as blocked-on-instrument.

## Discipline
No bar-shopping; thresholds final. Honest scope carries: 2D scalar
proxy at engine ratios, not PeV ratios; FND-REL-002's Derived-grade
re-derivation remains owed regardless of outcome.
