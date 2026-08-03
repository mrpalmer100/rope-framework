# PRED-003-XCHAIN bars — LOCKED before computation (2026-08-02)

Commission: HBAR-011's named next-order. The corpus carries two alpha chains:
  CHAIN 1 (PRED-003, paper P6): alpha ~ 2 T^2/(kappa a), derived to rope primitives
    (locking energy J = T^2/kappa exact in the harmonic regime).
  CHAIN 2 (HBAR-011): alpha = e^2/(4 pi eps0 hbar c) with hbar = pi T A^2/(2c)
    (the surviving standing-wave form), giving alpha = e^2/(2 pi^2 eps0 T A^2).
If they disagree, one of the corpus's two best surviving structures is wrong.

Rules fixed in advance:
- R1: Whatever the verdict, PRED-003's tier does not move UP on this audit; a
  consistency result hands boundary conditions to ELEC-054, it does not promote
  anything. If the chains CONFLICT, the conflict is registered at full strength
  against whichever chain has the weaker provenance, stated explicitly.
- R2: The charge-coupling question must be branched, not assumed: (E1) e^2/(eps0 c)
  drift-inert (the topological-charge reading, GG-006-adjacent but NOT identical to
  it — linking quantizes charge, it does not derive the coupling magnitude; flagged);
  (E2) e^2 ~ T^p with p free, reported generally.
- R3: All algebra symbolic (sympy), no numerics invented; any numeric statement must
  reduce to registered values or be declared calibration-closed.
- R4: The a-vs-w identification must be checked: chain 1's "a" and the ambient
  spacing w = 5.78e-17 m are DIFFERENT registered lengths. Report whether either
  chain's content depends on conflating them.

Bars:
- B1 (static): Derive the joint identity the two chains impose,
  kappa a = 4 pi^2 eps0 T^3 A^2 / e^2, and test whether it can FAIL numerically at
  present calibration. Expected and must be stated honestly if so: with A read back
  from measured hbar (ELEC-054) and chain 1 calibrated to measured alpha, the
  identity reduces to e^2 = e^2 — calibration-closed, ZERO static content. Prove it
  symbolically; do not dress a tautology as a check.
- B2 (drift, E1 branch): Derive the general drift-consistency condition. Expected
  form: d ln kappa + d ln a = 3 d ln T + 2 d ln A. Verify symbolically that under it
  the two chains give IDENTICAL d ln alpha for arbitrary drifts.
- B3 (channels): PRED-003's two channels re-derived under the joint corpus:
  tension channel (kappa, a fixed) must force d ln A = -(3/2) d ln T with the -2
  ratio surviving; spacing channel (T, kappa fixed) must force d ln A = (1/2) d ln a
  with the +1 ratio surviving. Both verified symbolically, including the G ~ 1/(Ta)
  form (still ASSUMED, carried as such).
- B4 (E2 branch): general p: tension-channel condition d ln A = (p-3)/2 d ln T,
  reported without choosing p.
- B5 (verdict): apply R1 mechanically. If B1-B3 pass, the registered outcome is
  CONSISTENT-BY-LOCKING: one identity, two channel-conditional amplitude scalings
  handed to ELEC-054 as boundary conditions, PRED-003 annotated (its provisional
  list gains the amplitude co-drift condition), tier unchanged.
