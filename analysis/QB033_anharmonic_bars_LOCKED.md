# QB-033 bars — LOCKED before computation (2026-08-02)

Commission: the anharmonic V_r correction (QB-029's 14 percent systematic), plus the
QB-027 pinned-tolerance repair adjudicated. No new Monte Carlo; the session is
theory-versus-existing-measurement.

The method, fixed in advance:
- SELF-CONSISTENT GAUSSIAN (variational): around the tilted minimum phi_0 =
  arcsin(h), the Gaussian-averaged curvature is m_eff^2 = cos(phi_0) exp(-s2/2)
  with s2 the on-site variance, itself the lattice sum at m_eff^2:
  s2 = (T/N) Sum_k 1/(m_eff^2 + 2 kt (1 - cos k)). Solve the fixed point by
  iteration; the saturated difference variance is var_sat = 2 s2 and the derived
  visibility V_SCGA = exp(-var_sat/2).
- The empirical truth is already banked: QB-030's 25536-sample bank gives
  <cos delta> = 0.780, i.e. var_emp = -2 ln(0.780) = 0.497.

Verdict rules, fixed in advance:
- R1: the SCGA prediction is computed and printed BEFORE the comparison.
- R2: bars -- var within 8 percent of empirical and V within 5 percent. If SCGA
  lands outside, the residual is registered as the two-loop correction's size, not
  absorbed; the harmonic-versus-SCGA improvement is reported either way.
- R3: propagation is FIRST-ORDER ARITHMETIC ONLY (no rerun): the derived cbar
  updates V' = (1 + 2 cbar)/3 and the QB-032 curve's endpoints; shifts are
  reported against the existing MC values, which already used the EMPIRICAL bank
  and therefore do not move -- the session's product is that the visibility is now
  DERIVED from (T, kt, h) rather than only measured.
- R4 (hygiene): the QB-027 repair is adjudicated on its actual content: the
  registered benchmark already asserts same-run self-consistency (|S - S_det| <
  0.03), so the environment sensitivity affects PRINTED MAGNITUDES only. If that
  adjudication holds, the repair is a documentation fix (annotation), not a code
  change; if inspection finds an assertion pinned to a historical magnitude, the
  code is repaired.

Bars:
- B1: SCGA fixed point converged (successive iterates < 1e-10); prediction stated.
- B2: var_SCGA vs var_emp within 8 percent (R2); harmonic gap and SCGA gap both
  reported.
- B3: V_SCGA vs empirical 0.780 within 5 percent; V_r now carries the label
  DERIVED (T, kt, h) at the stated accuracy.
- B4: first-order propagation table (V', floor, ceiling, isotropic) from the
  derived cbar next to the empirical-bank MC values.
- B5: QB-027 adjudication per R4, with the outcome registered.
