# ELEC-049 — The w adjudication: locked bars (before computation)

## Commission
ELEC-048 registered a factor-4.97 two-ledger discrepancy in the strand spacing:
Ledger B, w = 5.78e-17 m (from Sigma = 5.1e35, QGATE-007/009, HBAR-005), vs
Ledger A, w = 2.87e-16 m (nuclear-density spacing, used by ELEC-044..048).
This session adjudicates by PEDIGREE: trace every input of each ledger to its
registration, mark which inputs died with the reconnection route, and decide.

## Pre-trace findings (recorded before bars, governing their design)
- Ledger B is a one-parameter closed set: {Sigma, rho = Sigma/c^2,
  w = sqrt(T0/(c^2 rho)), T0 = Sigma w^2} -- identities, one independent input.
- T0's support: T0 = T_tube / n_structural with T_tube a MEASURED hadronic
  tension (QGATE-009: n_t T0 / T_tube = 1.005) and NUCQ-003 pinning the
  STRUCTURAL count at n >= 115 from lattice flux-tube width, explicitly
  non-circular. NUCQ-002 distinguished the structural role (survives) from the
  coherence role (died with the reconnection route).
- Ledger A's source: ELEC-039's "nuclear vacuum" was one of five counting
  HYPOTHESES; ELEC-040 used nuclear-density spacing as a COMPARISON value.
  No claim registers rho_vac = nuclear as the medium.

## Locked bars
B1 (identity audit). Verify Ledger B's closure numerically: from Sigma = 5.1e35
   alone, recover rho = 5.67e18, w = 5.78e-17, T0 = 1.70e3 to < 1%. Confirms
   one independent input, so the adjudication reduces to that input's pedigree.

B2 (pedigree verdict). Enumerate Ledger B's independent inputs: tension
   additivity (registered derivation), measured T_tube (external data,
   reconstructed here from the registered closure ratio), structural
   n >= 115 (NUCQ-003, lattice, non-circular), Lorentz bound a <= 1e-16 m
   (FND-MATTER-005). PASS if NONE of these is a killed claim (the kill list:
   W = 1.80 T D^2/c, coherence n_t = 111, D/w = 19, pre-correlation). Also
   compute the lattice-floor correction: T0 <= T_tube/115, report the shift
   from the registered 1.70e3 and its propagation into w (annotation owed on
   QGATE-009 if > 1%).

B3 (Ledger A adjudication). Registry search: does ANY claim register nuclear
   density as the medium's density? Expected none. If none, Ledger A is
   declared a PROMOTION ERROR: ELEC-044 (this auditor) promoted ELEC-040's
   comparison value into a medium parameter. Fifth self-catch of the arc,
   filed as corrections on ELEC-044..048 re-basing their numbers to Ledger B
   -- with ELEC-048's B2 column already showing every verdict SURVIVES the
   re-basing (deaths strengthen ~25x; nothing flips).

B4 (the adjudicated value and its condition). w := 5.78e-17 m is canonical BY
   ELIMINATION, conditional on Sigma = 5.1e35 -- which is itself a registered
   PREDICTION of {additivity + Lorentz + structural n}, with the experimental
   arbiter (VMB@CERN-class polarimetry, inverted payoff per QGATE-007) still
   standing. The output states the conditionality verbatim.

B5 (honesty). Adjudication-by-pedigree selects the surviving ledger; it does
   not derive w from first principles. The absolute scale still rests on the
   measured hadronic tension plus the Lorentz bound, and dies or lives with
   Sigma's experimental test.
