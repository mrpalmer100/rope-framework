# QB-032 bars — LOCKED before computation (2026-08-02)

Commission (QB-031's cheapest next-order): convert P1' (isotropic source
orientation) from premise to PARAMETER by computing the Bell violation as a
function of the source's strand-axis orientation n relative to the settings plane.

The analytic structure, locked before simulating:
- Per trial the derived transport applies R_n(delta) with FIXED axis n. Averaging
  over the delta bank (symmetric, so the sin term vanishes) gives the effective
  linear map M(n) = cbar I + (1 - cbar) n n^T, with cbar = <cos delta>.
- First-order prediction per orientation: E(x, y) ~ -k x.M(n).y with the response
  slope k fixed by the perfect-ribbon reference (k = S_perfect/(2 sqrt 2)); the
  predicted CHSH is the max CHSH combination of the four x.M(n).y values times k.
- Checkpoints the curve must hit: n perpendicular to the settings plane (n = y-hat)
  reduces M to cbar I on in-plane vectors -- the QB-030 worst case realized
  geometrically; the isotropic average of M(n) over n reproduces QB-031's
  ((1 + 2 cbar)/3) I.

Rules fixed in advance:
- R1: run order -- the analytic prediction S_pred(n) for every orientation is
  computed and printed BEFORE its Monte Carlo value.
- R2: the MC must match first order within 10% per orientation (QB-031's rule,
  inherited; its measured deviation was 3.9%).
- R3: whatever the curve's shape, both endpoints are adjudicated: the
  perpendicular orientation must land near QB-030's floor and the isotropic
  reference near QB-031's 2.234, or the interpolation is not trusted.
- R4: no tier motion; the deliverable is the CURVE S(n) -- a lab-geometry dial --
  and P1' is thereafter a parameter, not a premise.

Bars:
- B1: the effective-map identity M(n) = cbar I + (1 - cbar) n n^T verified
  symbolically (delta-symmetry kills the sin term; isotropic average recovers
  QB-031's scalar).
- B2: analytic S_pred(n) computed for the orientation set {y-hat, z-hat, x-hat,
  (x+z)/sqrt2, (x+y)/sqrt2} plus the isotropic reference, before any MC (rule R1).
- B3: MC at M = 100000 per pair per orientation; R2/R3 adjudicated; no-signaling
  < 0.015 everywhere.
- B4: the curve's extremes identified and stated (which orientation maximizes the
  violation, and its value); the P1'-to-parameter conversion recorded.
