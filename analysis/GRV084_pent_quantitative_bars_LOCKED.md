# GRV-084 bars — LOCKED before computation (2026-08-02)

Commission (the chain's last premise): make P-ENT quantitative -- convert
energy-per-bit to temperature with the two-state O(1) measured, not assumed.

The route, recorded before computing:
- B1 (exact thermodynamics, by machine): the crossing as a two-state system with
  gap W: Z = 1 + exp(-W/T); broken fraction f = 1/(1 + exp(W/T)); entropy
  S(f) = -f ln f - (1-f) ln(1-f); and the inversion T = W/ln((1-f)/f) -- the
  temperature of a bit population is the gap over the log-odds of its
  occupation. All sympy-verified, including dE = T dS along the curve.
- B2 (the measurement): the operating broken fraction f* of the near-horizon
  shell is MEASURABLE on GRV-081's engine -- the accretion run (sub-threshold
  pulse, blueshift capture) and the crossing run each leave a fired shell whose
  mean broken fraction is read off the s field. The two-state O(1) is then
  L* = ln((1-f*)/f*), computed per regime, with the spread reported.
- B3 (compatibility): GRV-037's measured metastability (the intact branch holds
  up to T_c ~ 1 in engine units, with engine barriers O(1)) is checked for
  ORDER-OF-MAGNITUDE consistency with the two-state reading (the bit becomes
  unusable when T approaches W over an O(1) log) -- a compatibility note, not a
  precision bar, and said so.
- B4 (the assembled chain, quantitative): T_res(sigma) = N(sigma) h / L* with
  L* measured -- every factor now has a provenance: N h from the lift-over
  theorem (GRV-083), e_bit ~ barrier measured (GRV-082), L* measured (tonight).
  The residual premise is named: P-EQ, that the shell's bit population
  equilibrates (the two-state formula is an equilibrium statement; the engine's
  shell is driven). P-ENT moves to DISCHARGED-AS-MEASURED-COEFFICIENT-GIVEN-P-EQ.

Rules fixed in advance:
- R1: f* is extracted mechanically -- mean(1 - s) over cells with s < 0.999 --
  from runs at GRV-081's registered parameters, no tuning.
- R2: if the two regimes' L* differ by more than a factor 2, the coefficient is
  reported as a RANGE and the claim's title says range, not value.
- R3: no flux, no spectrum, no absolute-temperature evaluation (h, K, n_x stay
  unevaluated); the deliverable is the measured log-odds coefficient and the
  fully-labelled chain.
