# QB-029 bars — LOCKED before computation (2026-08-02)

Commission (QB-028's load-bearing next-order): derive the fiber-bath coupling at
strand level — does fibre-blindness extend from the drive to the bath?

The structure found in reconnaissance, recorded before computing:
- GRV-020 (Derived, the one-generator theorem): the internal symmetry group of the
  two-strand rope has exactly ONE Goldstone, and topology allocates it to
  electromagnetism. A SECOND independent gapless internal field is excluded.
- Consequence for QB-028's branch (A): the fiber CANNOT be an independent dynamical
  thermal mode of the medium. If it were, it would be a second internal Goldstone
  (if gapless) or a new registered field (if gapped) — neither exists in the corpus.
  Fluctuation-dissipation then has NO independent fiber channel to thermalize:
  a bath cannot dephase a variable that has no energy coupling, and FND-STRAND-005
  B2 proved the frame twist carries no channel energy.
- Therefore the fiber must be a HOLONOMY: a frame relation transported along the
  strand by the base twist field (the corpus-native reading, since torsion IS the
  one internal mode). Its core-to-core fluctuations are inherited from the BASE
  field between the cores — and the base in the pair's interior is GAPPED (pinned
  at the sine-Gordon minimum), so the inherited noise should SATURATE with
  separation instead of growing: a finite VISIBILITY, not decoherence.

Premises, stated as premises:
- P1: the QB fiber, realized on strands, is frame holonomy riding the base twist
  (transport reading), not a new medium field. Supported by GRV-020 + FND-STRAND-005
  B2; not independently proven here.
- P2: the interior of the nucleated pair sits in the tilted sine-Gordon minimum
  with curvature m^2 = sqrt(1 - h^2) at h = 0.30 (harmonic treatment of the pinned
  fluctuations; anharmonic corrections uncontrolled at T = 0.4 and flagged).

Verdict rules, fixed in advance:
- R1: the lattice measurement decides between SATURATION (gapped transport noise;
  finite separation-independent visibility) and GROWTH (Goldstone-like; QB-028's
  thermal death re-enters through the base). Both outcomes registrable; the massless
  control must show growth or the instrument is not trusted.
- R2: the analytic lattice-sum prediction for the saturated variance is computed
  BEFORE the measurement in the run order and the match bar is 20% (harmonic
  prediction against the full nonlinear simulation; P2's flag prices the gap).
- R3: no promotion of QB-027's ribbon; the output is a derived g_fb verdict plus a
  measured visibility, handed to S3 as a quantitative input.

Bars:
- B1 (the exclusion): GRV-020 cited; branch (A) — the independent thermal fiber
  mode, the g_fb = 1 reading of QB-028 — excluded structurally. The FDT argument
  stated: damping requires energy coupling; the frame has none (FND-STRAND-005 B2).
- B2 (the prediction): the exact lattice sum for the pinned field's difference
  variance, var(d) = (2T/N) Sum_k (1 - cos kd)/(m^2 + 2 kt (1 - cos k)), computed
  at the engine's parameters; its saturation value and the implied visibility
  V = exp(-var_sat/2) stated in advance of the measurement.
- B3 (the measurement): the pinned sine-Gordon field at h = 0.30 (registered
  nucleation-silent) evolved and sampled; var(phi_i - phi_j) versus d compared to
  the prediction (rule R2); the massless control run and required to GROW.
- B4 (the pair check): the same statistics sampled in the interior of an actual
  QB-028 nucleated pair (one seed, looser 30% bar) — the plateau must behave as the
  pinned field does.
- B5 (verdict per R1/R3): g_fb = 0 in the FDT sense; the residual is a finite,
  separation-independent ribbon visibility V_r (measured); QB-028's inequality is
  satisfied at ALL separations on the holonomy reading; S3 becomes quantitative
  with V_r as input, and the analogy to QB-027's analyzer-visibility arithmetic is
  NOTED, not claimed.
