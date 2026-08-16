# COMMISSION FRAME-DRAG-RATIO (NUN-GRV13) -- BARS LOCKED (2026-08-16)

Locked BEFORE any computation. Charter:
docs/commissions/COMMISSION_FRAMEDRAG_ratio.md (cut at v3.26.37 on
EM-RECON-041's verdict). Target: GRV-062's open G-free question --
does the framework give gravitomagnetic/gravitoelectric =
J sin^2(theta)/(Mc)?

## B1 -- CONDITIONS READ AND BINDING (quoted at verdict level)
- GRV-104 conditions: beta_J audit ran and PINNED (GRV-105,
  beta_J = 1, clean-room attested). Satisfied.
- GRV-110 condition 4 / GRV-115 framing, BINDING ON THIS SESSION:
  "UNTIL lambda IS DERIVED OR INDEPENDENTLY BOUNDED, NO LARES-CLASS
  RESULT MAY BE ADVERTISED AS A KILL TEST -- ONE-PARAMETER
  MEASUREMENT IS THE HONEST FRAMING." lambda's magnitude is
  UNDERIVED; GRV-113 caps only its MESH-CHIRALITY channel
  (chi <= 2.49e-19), which is a different operator channel and does
  NOT pin the gravitomagnetic amplitude. Consequence fixed at lock:
  this session may derive STRUCTURE (angular form, J-scaling,
  radial law, parameter count) and must express any amplitude
  through the granted lambda, never around it.
- GRV-005: the mass-monopole leg -- static force balance, Poisson
  forced, 1/r conditioning field. G inverse-measured (GRV-006).
- GRV-020 (Derived): dipole-led sourcing forced for neutral static
  rotating bodies.

## B2 -- OUTCOME GRAMMAR, finalized at lock (exhaustive)
- RATIO-REPRODUCED: J sin^2(theta)/(Mc) with NO free parameter.
  (Reachable only if lambda cancels between sectors; the monopole
  rides strain and the dipole rides L_C3, so cancellation would
  itself be a derivation and must be exhibited, not assumed.)
- RATIO-REPRODUCED-IN-FORM / ONE-PARAMETER-AMPLITUDE: the ratio's
  STRUCTURE (linearity in J at beta_J = 1; sin^2(theta); the radial
  law; zero additional freedom) derives exactly, and the amplitude
  is Lambda x J sin^2(theta)/(Mc) with Lambda ONE dimensionless
  underived constant (the granted lambda in GR-calibrated units),
  Lense-Thirring at Lambda = 1. This is the grant's own
  "one-parameter measurement" framing landing on GRV-062's target.
- RATIO-OFF-BY (named factor): a STRUCTURAL mismatch (wrong angular
  form, wrong J-power, wrong radial law, or extra freedom beyond
  Lambda). The framework dies or is wounded with a number/shape.
- RATIO-BLOCKED-AT (named leg): a required registered input missing.

## B3 -- REFUSALS
- NO LARES/GP-B numbers, NO kill-test language (condition 4).
- NO derivation or estimation of lambda's magnitude; Lambda is
  carried symbolic. Any 'natural value' talk REFUSED.
- NO EM-sector constants (kappa_0, C26, g) in any gravitational
  leg; the dynamo precedent supplies COMPOSITION DISCIPLINE only.
- NO touching GRV-113's cap or re-deriving GRV-105's pin.
- The GR comparison target (J sin^2 theta/(Mc)) is quoted from
  GRV-062's registered reduction, not re-derived from GR here.
- Titles are not verdicts; clean-room on the target value: the
  derivation legs run before the comparison leg is opened.

## B4 -- MACHINE CONTENT PLANNED
sympy, benchmarks/gravity/framedrag_ratio_nungrv13.py:
1. MONOPOLE LEG (GRV-005 class): Poisson with point mass source;
   potential Phi = -C_m M / r; C_m carries the calibrated (inverse-
   measured) strength. Verify 1/r.
2. DIPOLE LEG (L_C3 class): the shift potential sourced by the
   twist dipole of a rotating body; twist dipole moment d = beta_J J
   = J exactly (GRV-105); solve the same elliptic operator with a
   dipole source: u_t,phi = C_d J sin(theta)/r^2 class. Verify
   dipole solution EXACTLY (Laplacian check), extract sin(theta)
   and 1/r^2; form the metric-slot ratio and verify the sin^2 theta
   and the G-cancellation STRUCTURE question honestly: exhibit
   where C_d/C_m does and does not cancel.
3. PARAMETER COUNT: show the ratio is Lambda x J sin^2(theta)/(Mc)
   with Lambda = (C_d/C_m) x (calibration factors), ONE constant,
   and that beta_J = 1 leaves no second slot.
4. NULL CHECKS: monopole term of the twist source vanishes (GRV-020
   verified on the ansatz); J -> -J flips the ratio's sign (parity
   of frame dragging).
