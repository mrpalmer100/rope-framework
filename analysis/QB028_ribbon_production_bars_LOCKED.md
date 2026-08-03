# QB-028 bars — LOCKED before computation (2026-08-02)

Commission: the shared ribbon is QB-027's premise (severing it collapses the
violation to the sub-classical wall); nobody has shown the medium PRODUCES one.
Candidate mechanism (Mark's pointer): FND-STRAND-006's kink-antikink pair nucleating
in a single strand's twist field — two excitations that are features of one object by
construction, with the inter-kink segment as the candidate ribbon (the umbilical
remnant of the nucleation, free to grow in the driven regime).

The load-bearing unknown, identified in advance from the corpus's own theorems:
BASE VERSUS FIBER. QB-013/QB-020 prove shared provenance plus conserved charge pins
correlations at the -1/3 wall; only the spinor FIBER reaches -1. Winding
anticorrelation is base-level. FND-STRAND-005's fibre-blindness (the drive provably
does not see a 2 pi frame twist) means the nucleation energetics do not obviously
imprint fiber correlation. The session must measure whether the segment CARRIES
fiber coherence between the cores, and at what cost in noise.

Scope, stated honestly: S3 (the end-to-end QB-027 rerun with the measured pair
replacing the ribbon-by-fiat) is named next-order, not run today — it is only worth
running if S1/S2 survive. Today runs S1/S2 on FND-STRAND-006's own Langevin engine.

Model commitments, fixed in advance:
- The twist (base) field: FND-STRAND-006's engine verbatim (overdamped sine-Gordon,
  kt = w^2 = 0.64, T = 0.4, N = 96 extended as needed, tilt h above threshold).
- The fiber: a frame phase psi per site transported along the strand with gradient
  stiffness K_f (frame elasticity), fibre-blind to the drive per FND-STRAND-005 B2
  (no h-coupling), with bath coupling g_fb an EXPLICIT UNKNOWN swept over
  {1.0 (fully thermal), 0.1, 0.0 (decoupled)} — the corpus registers no fiber-bath
  coupling, and the sweep converts the ignorance into a requirement rather than a
  choice. K_f = 1 fixed; only ratios matter at exponent level.
- 1D analytic control: for a thermal XY chain, <cos(psi_i - psi_j)> =
  exp(-|i-j| g_fb T/(2 K_f)) — the measured decay must match this within 15% where
  g_fb > 0, or the simulation is not trusted.

Verdict rules, fixed in advance:
- R1 (base): winding anticorrelation of the nucleated pair must be EXACT (integer
  conservation); anything else is a bug, not physics.
- R2 (the kill-bar): if at g_fb = 1 the core-to-core fiber coherence length is
  below 10 kink widths, the UNPROTECTED thermal segment is registered as DEAD as
  QB-027's ribbon at laboratory separations. This does not kill the premise; it
  kills this candidate's naive branch and converts the premise into a
  specification: the ribbon works iff the fiber is (near-)decoupled from the bath.
- R3 (the surviving branch): at g_fb = 0 the coherence must persist across the
  full separation for the candidate to remain live; partial decay at g_fb = 0
  would indicate an intrinsic dephasing channel and be registered as adverse.
- R4 (no promotion): whatever survives, the shared ribbon remains a premise until
  S3 runs; today's best outcome is PREMISE SHARPENED (production mechanism live
  under a named decoupling condition), not premise derived.
- R5: the confinement cross-reference (PRED-003-CHAIN's log interaction) is cited
  where separation energetics appear; no new claims about it.

Bars:
- B1: nucleation reproduced on the registered engine; cores identified; pair
  separated under sustained tilt to >= 40 sites; base winding anticorrelation
  verified exact (rule R1).
- B2: fiber transport implemented per the model commitments; the analytic control
  passed at g_fb = 1 (rule: 15%).
- B3 (S1): core-to-core fiber coherence C(d) measured versus separation at
  g_fb in {1.0, 0.1, 0.0}; coherence lengths extracted; R2/R3 adjudicated
  mechanically.
- B4 (S2): a pi/2 frame rotation imposed at one core after separation; propagation
  of the constraint to the far core measured through the segment at each g_fb —
  the ribbon's defining bookkeeping function, tested dynamically.
- B5: the requirement stated quantitatively: for a ribbon at separation d, the
  fiber-bath coupling must satisfy g_fb < 2 K_f/(T d) — the production premise
  converted into one inequality with named unknowns.
- B6: verdict per R2-R4; S3 (the end-to-end rerun) and the fiber-bath coupling's
  strand-level derivation named as next-orders; FND-025/026 (the shared object
  works; the two-particle boundary) cited as the lineage this session extends.
