# Suggested GitHub Issues (open problems as research questions)

Paste each block below as a new Issue. Labeled by status and linked to claim IDs so the
issue tracker mirrors the open frontier of the programme. Suggested labels: `open-problem`,
`conjecture`, `derivation-wanted`, `help-wanted`.


---

### [FND-013] EM flux tubes as defect lines vs smooth winding

**Status:** Open  
**Paper:** rope_defect_topology_3d  
**Depends on:** FND-011, EM-001  

Stated open bridge, not claimed; would require settling core singular-vs-smooth....

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [EM-RECON-008] The repulsive-core residual is located precisely and confirmed irreducible at quadratic order

**Status:** Open  
**Paper:** None  
**Benchmark:** `benchmarks/em/repulsive_core_residual.py`  
**Depends on:** EM-RECON-005, EM-RECON-006, FND-MATTER-004  

Went after the repulsive-core residual (the equilibrium-spacing gap in the mode-overlap functional, EM-RECON-005/006). ATTEMPTED ROUTE: the interpenetrability threshold (FND-MATTER-004) LOOKED like it supplies a parameter-free hard core (ropes cannot overlap past coverage f_c -> hard wall). RETRACTED after checking the actual postulate (magnetism paper 2.1): 'bundle density determines the local fi...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [EM-RECON-015] OPEN

**Status:** Open  
**Paper:** None  
**Benchmark:** `benchmarks/em/field_strain_calibration.py`  
**Depends on:** EM-RECON-014  

A genuine consistency problem the field<->strain calibration creates, computed and registered rather than buried. If SIGMA ~ 1e25 J/m^3 (the ATLAS-scale identification), the rope network's rest-tension energy corresponds to SIGMA/c^2 ~ 1.7e8 kg/m^3 pervading all space -- five orders denser than lead. Were this to gravitate normally, the universe would have collapsed immediately; it manifestly does...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [GRV-012] STANDING ADVERSE VERDICT

**Status:** Open  
**Paper:** rope_gravity  
**Benchmark:** `benchmarks/gravity/anisotropic_defect_field.py`  
**Depends on:** GRV-011, GRV-010, GRV-009, GRV-008  

The tensor-structure campaign's conclusion, registered at full strength because burying it would poison everything else. THE CHAIN: (1) the isotropic sector is exhausted -- every constructed mechanism gives gamma in [-1, 0] (GRV-009: -4/7; GRV-010: -1/2; pure channels: -1/2, 0, -1); (2) the anisotropic route (GRV-011) produced the exact tidal theorem but also the RANGE OBSTRUCTION: elastic conditi...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [GRV-014] CONJECTURE

**Status:** Conjecture  
**Paper:** rope_gravity  
**Benchmark:** `benchmarks/gravity/quantum_completion_audit.py`  
**Depends on:** GRV-013, GRV-012, GRV-007, GRV-006, FND-REL-002, NUC-005  

Mark asked: is it possible that quantum effects -- outside the documented scope -- account for the missing arcsecond, given that Newton is classically accounted for? Audited with full care, because this sits exactly on the line between honest scope refinement and a rescue in better clothes. THE KEY DISTINCTION, kept explicit: in GR itself the 1.75 arcsec is classical, so 'bending is quantum in nat...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [PM-001] Lepton mass ratios via Koide phase

**Status:** Conjecture  
**Paper:** rope_lepton_masses  

CONDITIONAL: with the model's own sin2thetaW=1/(3sqrt2) it FAILS (mu/e~1605). [STRUCTURAL CONTEXT (PM-003): the lepton mass problem is a 3-level knot EXCITATION spectrum, not composite counting -- which is why a Koide-type RELATION AMONG LEVELS (this claim) is the relevant kind of tool. The knot-count mass mechanism that works for nuclei (NUC-001) provably cannot apply here, since all leptons shar...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [FND-MATTER-001] REFRAMED via Gaede's atom

**Status:** Open  
**Paper:** rope_microscopic_mechanics  
**Depends on:** FND-REL-003  

Consequence of FND-REL-003 (mesh spacing a << 1e-16 m, far finer than atomic ~1e-10 m). READING A ('atom = single rope-endpoint node', which would make rope spacing = interatomic spacing) is REFUTED -- that scale is Lorentz-excluded. The corpus's endpoint-locking result J=T^2/kappa is a COARSE-GRAINED homogenization, so 'endpoint' is an effective node, consistent with READING B ('atom = extended c...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [FND-MATTER-003] Derivation of the atomic scale is BLOCKED

**Status:** Open  
**Paper:** rope_microscopic_mechanics  
**Depends on:** FND-MATTER-002  

Attempted to push the R~a*sqrt(N) consistency window (FND-MATTER-002) toward an actual derivation of the Bohr radius. HONEST RESULT: blocked, and the attempt located exactly why. A derivation needs, independently of a0: (I) the absolute microstructure scale a -- but the corpus leaves a a FREE parameter (only a Lorentz bound a<~1e-16 m exists, no value); and (II) the rope count N -- for which the n...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [EW-001] Weinberg angle sin2thetaW = 1/

**Status:** Conjecture  
**Paper:** rope_weinberg_angle  

~1.94% from measured 0.23122; the 'soft external input' that breaks PM-001....

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [QB-005] Amplitude interference from rope dynamics

**Status:** Open  
**Paper:** rope_scope_and_limits  

The genuinely open quantum frontier; do not overclaim. [AUDIT NOTE: this open problem is motivated BY the failure of QB-003 (the counting form does not reproduce entanglement); that is a conceptual motivation, not a derivation dependency, so the raw depends_on was cleared to avoid resting an Open claim on a Failed one.] [DIRECTION (QB-006): interference is native to rope wave modes (linear superpo...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [NUC-002] Strong nuclear force identified as rope-bundle contact force at nuclear scale

**Status:** Conjecture  
**Paper:** rope_nuclear_physics  
**Depends on:** NUC-001  

The paper's central proposal: the strong force IS the rope-bundle contact force that creates chemical contact at atomic scales (1e-10 m, eV), operating at nuclear scale (1e-15 m, MeV) -- 1e5x smaller, correspondingly greater energy. Quark confinement follows from fractional sub-knots being unstable alone (see NUC-003). QUALITATIVE identification with a scaling story; the paper lists the quantitati...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [NUC-003] Fractional quark sub-knots are CONSISTENT with integer charge quantization

**Status:** Open  
**Paper:** rope_nuclear_physics  
**Depends on:** GG-006, EM-001, FND-008  

CONSISTENCY CHECK run before adopting the nuclear paper. The paper models quarks as sub-knots with fractional winding (+2/3,-1/3). SURFACE conflict with the corpus's integer charge quantization (FND-008, EM-001, GG-006, all Derived). RESOLUTION (passes): the fractional pieces are CONFINED (unstable alone) and only exist bound into configurations whose TOTAL winding is integer -- verified arithmeti...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*
