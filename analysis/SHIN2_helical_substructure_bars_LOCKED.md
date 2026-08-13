# COMMISSION SHIN2 -- THE HELICAL-SUBSTRUCTURE ACCEPTANCE TEST: BARS, LOCKED BEFORE COMPUTING

Locked 2026-08-12, before any computation. Charter: the C1+C2
acceptance computation priced in docs/T3_PHOTON_REPAIR_PRICING.md.
This commission TESTS the candidate; it adopts nothing. If every bar
passes, the candidate goes to the desk as GRANT-CANDIDATE-SUBSTRUCTURE
with its price sheet; any failure is registered and kept.

## The candidate, stated once

Fundamental strands finer than the registered coarse strand by
sqrt(n_sub), n_sub ~ 4.6e9 (kappa250) to 1.3e10 (kappa50) per coarse
cell, carrying the SAME total tension (redistribution: T0_f = T0/n_sub,
mu_f = mu/n_sub), wound helically (possibly hierarchically) within
the coarse strand. The m_e anchor reads the coarse envelope.

## Acceptance tests, all four locked with pass bars

A1 REDISTRIBUTION INVARIANCE (exact arithmetic). Under the
redistribution map, verify symbolically/numerically: (i) wave speed
c^2 = T/mu invariant; (ii) energy density Sigma per volume invariant;
(iii) the FND-040 Lorentz margins (6.1x / 10.5x) invariant. PASS:
all three exact. FAIL: any drift.

A2 THE CEILING (arithmetic). Fine-mesh ceiling E_max ~ hbar c / a_f,
a_f = a / sqrt(n_sub), at both live (a, kappa) readings. PASS:
E_max >= 1.4 PeV at the priced n_sub. FAIL: short at any reading.

A3 DIRECTION COVERAGE (the decisive computation). FND-059's locked
bar was accessible sky fraction >= 10 percent; the same bar binds
here. Compute the tangent-direction coverage of the fine-strand
field on the unit sphere within the required acceptance half-angle
theta_req = 2.7e-5 rad (the tighter of FND-059's pair) for:
- W0: straight three-family (the control; must reproduce ~1e-9).
- W1: single-level helices, three families, pitch angle psi swept
  over (0, pi/2); coverage is bands around three circles.
- W2: two-level (helix-on-helix) winding, pitch angles (psi1, psi2)
  swept; tangents precess over 2D tori on the sphere.
PASS: any registered-geometry member of W1 or W2 reaches >= 10
percent coverage. FAIL: no member does. The sweep grid is locked at
psi in {5, 15, 30, 45, 60, 75, 85} degrees per level; no post-hoc
grid additions.

A4 ACCESSIBLE-ENERGY INVARIANCE (condition check plus named risk).
At wavelengths far above the pitch, the wound structure must present
the coarse medium unchanged. Two locked checks:
- A4a: the effective-medium speed is volumetric (T per area over mu
  per volume), invariant under winding by A1's arithmetic. PASS if
  A1 passes.
- A4b THE GUIDED-PATH RISK, displayed and confronted: a disturbance
  guided ALONG a wound carrier travels arclength, giving axial speed
  c sin(psi_eff) < c. The candidate survives only if the coarse
  light mode is the COLLECTIVE medium mode (EM-RECON-025's
  registered branch), not a guided single-carrier mode. Locked test:
  compute the arclength retardation factor at every swept psi and
  report it next to the A3-passing members; if every A3-passing
  member requires sin(psi_eff) < 0.99 for its guided modes, the
  tension between coverage and guided-speed is REGISTERED ON THE
  FACE with the collective-mode assignment as the named escape --
  reported, not resolved, per the resemblance rule.

## Discipline clauses

- No bar-shopping: theta_req, the 10 percent bar, and the psi grid
  are final. Adverse outcomes pre-authorized at every test.
- Nothing here identifies the fine strand with any registered object;
  n_sub, the pitch, and the hierarchy depth remain UNDERIVED
  parameters on the price sheet.
- The stale-number tripwires and the light-carrier phrasing caution
  carry (the collective transverse pair is light; no topological
  mode is identified with the photon here).
- If all four pass: GRANT-CANDIDATE-SUBSTRUCTURE is drafted with the
  full price (one primitive family, three underived parameters, the
  A4b tension if present) and placed on the desk. The author decides.
