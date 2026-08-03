# PRED-003-CONST bars — LOCKED before computation (2026-08-02)

Commission (reviewer-refined): derive the constitutive relation e_eff^2(T, a, kappa, ...)
with ALL logarithmic derivatives (p_T, p_a, p_kappa), not the scalar p.

Pre-computation reconnaissance findings that the bars must adjudicate (recorded now so
they cannot be softened after the algebra):
- The expression alpha ~ 2 T^2/(kappa a) appears in the predictions paper's P6 with the
  phrase "whose chain is derived to rope-medium primitives", but NO registry claim or
  benchmark derives it. EM-002b explicitly registers alpha as a consistency relation
  (measured Z0 and e as inputs), NOT a derivation. FND-001 supplies only J = T^2/kappa.
- Units from FND-001's own benchmark: J is an energy per link, coarse-grained stiffness
  K = J/a [J/m]; hence kappa = T^2/J has units [J/m^2]. Then 2 T^2/(kappa a) has units
  J/m — a TENSION, not a dimensionless number. The literal paper expression is
  dimensionally open.

Rules fixed in advance:
- R1: The XCHAIN identity e^2 = 4 pi^2 eps0 T^3 A^2/(kappa a) is INADMISSIBLE as a
  derivation route — it contains A and is the answer in costume. Refused by name.
- R2: No closure of the paper expression may be selected by numerics against measured
  alpha (that is tuning). Closure selection must be structural, and its premises stated
  as premises.
- R3: Honorable failure is registrable: if no closure is forced, the session registers
  the enumeration and the block.
- R4: All unfavorable findings (provenance gap in the sole T1; dimensional openness of
  its alpha expression) are registered at full volume regardless of how the derivation
  lands. No tier motion in either direction this session.
- R5: Every downstream consequence (PRED-003's -2; XCHAIN's boundary conditions;
  ELEC-082's kills) must be RE-VERIFIED end-to-end symbolically under whatever
  constitutive form results — favourable or not, channel by channel.

Bars:
- B1 (provenance, machine-checked): scan claims.yaml and benchmarks/ for any derivation
  of 2 T^2/(kappa a) outside the PRED-003 lineage. Expected: none. Register the gap.
- B2 (dimensional audit): with kappa = T^2/J and J an energy [FND-001 benchmark],
  verify [2 T^2/(kappa a)] = J/m for this convention (and record the alternative
  kappa ~ J*m convention's failure too). The literal expression is not dimensionless.
- B3 (closure theorem): under the paper's OWN primitive statement — alpha a function of
  (T, kappa, a) only, closed by hbar*c and medium lengths proportional to a — show the
  dimensionless closure is UNIQUE up to a pure number: alpha = 2*lambda*T^2*a/(kappa
  hbar c). Closures involving A are excluded BY THE PRIMITIVE STATEMENT (a premise,
  recorded as such, not a proof). Equivalently, via alpha's definition:
      e_eff^2/(4 pi eps0) = 2*lambda*T^2*a/kappa = 2*lambda*J*a,
  the constitutive relation, with triple (p_T, p_a, p_kappa) = (2, 1, -1) FORCED and
  the pure number lambda open.
- B4 (consequences, per R5): (i) the two chains FUSE into one — the XCHAIN locking
  relation becomes an identity and the E1 branch (drift-inert coupling) is EXCLUDED
  under the closure; (ii) PRED-003's tension-channel ratio re-derived end-to-end: does
  -2 survive, and on what co-drift condition; (iii) the amplitude boundary conditions
  updated: expected BC2' A ~ T^(-1/2), BC3' A ~ a^1; (iv) the amplitude formula
  A^2 = 4*lambda*T*a/(pi*kappa*alpha) stated, with its calibration-closure declared
  (it reproduces ELEC-054's readback identically — no numeric content today).
- B5 (ELEC-082 re-grade under the triple): M2/M4/M5 against BC2'/BC3'; M5's
  hbar-exponent test against the updated requirement (hbar ~ T^0 under tension drift);
  the pure-number class against both. Report whichever way each falls, including any
  kill whose load-bearing channel MOVES.
- B6 (status): the closure is CONDITIONAL on the paper's primitive statement and on the
  unregistered chain being what the paper says it is. Modeled, no tier motion, and the
  claim must state that registering the actual chain (or refuting the primitive
  statement) is the outstanding obligation.
