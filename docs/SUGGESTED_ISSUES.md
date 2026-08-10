# Suggested GitHub Issues (open problems as research questions)

*Generated from `claims.yaml` -- do not edit by hand. Regenerate with
`python3 tools/build_suggested_issues.py` (run by `make` / checked by
`tools/check_freshness.py`).*

Every claim currently at status **Open** or **Conjecture** -- the programme's live
open frontier. Paste a block below as a new Issue. Suggested labels:
`open-problem`, `conjecture`, `derivation-wanted`, `help-wanted`.


---

### [EM-RECON-008] The repulsive-core residual is located precisely and confirmed irreducible at quadratic or...

**Status:** Open  
**Benchmark:** `benchmarks/em/repulsive_core_residual.py`  
**Depends on:** EM-RECON-005, EM-RECON-006, FND-MATTER-004  

Went after the repulsive-core residual (the equilibrium-spacing gap in the mode-overlap functional, EM-RECON-005/006). ATTEMPTED ROUTE: the interpenetrability threshold (FND-MATTER-004) LOOKED like it supplies a parameter-free hard core (ropes cannot overlap past coverage f_c -> hard wall). RETRACTED after checking the...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [FND-MATTER-001] REFRAMED via Gaede's atom: atomic size is a standing-wave WAVELENGTH (decoupled from mesh ...

**Status:** Open  
**Paper:** rope_microscopic_mechanics  
**Depends on:** FND-REL-003  

Consequence of FND-REL-003 (mesh spacing a << 1e-16 m, far finer than atomic ~1e-10 m). READING A ('atom = single rope-endpoint node', which would make rope spacing = interatomic spacing) is REFUTED -- that scale is Lorentz-excluded. The corpus's endpoint-locking result J=T^2/kappa is a COARSE-GRAINED homogenization, s...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [FND-MATTER-049] [REOPENED, applied at merge 2026-08-09 from the review-session record (SYNC_STATE, Commiss...

**Status:** Open  
**Paper:** falsifiable_predictions  
**Benchmark:** `benchmarks/foundations/matter049_open_claim_terminus.py`  
**Depends on:** FND-MATTER-003, FND-MATTER-044, FND-MATTER-048, FND-MATTER-005  

A registry-hygiene brick that turned out to have a conscience clause, and the clause is the reason the session was worth running. Closing an Open claim is the most self-serving edit a programme can make, so the bars made it hard on purpose: the claim could only close if every named input had a determination AND every d...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [FND-MATTER-050] [REVERTED TO HONEST FORM + PREDICTION GRANTED (FND-MATTER-064/065, 2026-08-09): the ~25 pe...

**Status:** Open  
**Paper:** rope_matter_mass  
**Depends on:** FND-MATTER-009, FND-MATTER-049  

An open problem rescued from an accounting shortcut. For months the lever was 'blocked at FND-MATTER-003' in a dozen registration texts, which was convenient shorthand and quietly false: 003 was about the atomic scale's two missing inputs, and the zero-point coefficient was neither of them. The borrowing was harmless w...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [GRV-012] STANDING ADVERSE VERDICT (stated plainly): on current commitments, rope weak-field gravity...

**Status:** Open  
**Paper:** rope_gravity  
**Benchmark:** `benchmarks/gravity/anisotropic_defect_field.py`  
**Depends on:** GRV-011, GRV-010, GRV-009, GRV-008  

The tensor-structure campaign's conclusion, registered at full strength because burying it would poison everything else. THE CHAIN: (1) the isotropic sector is exhausted -- every constructed mechanism gives gamma in [-1, 0] (GRV-009: -4/7; GRV-010: -1/2; pure channels: -1/2, 0, -1); (2) the anisotropic route (GRV-011) ...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [NUC-003] Fractional quark sub-knots are CONSISTENT with integer charge quantization (confined, sum ...

**Status:** Open  
**Paper:** rope_nuclear_physics  
**Depends on:** GG-006, EM-001, FND-008  

CONSISTENCY CHECK run before adopting the nuclear paper. The paper models quarks as sub-knots with fractional winding (+2/3,-1/3). SURFACE conflict with the corpus's integer charge quantization (FND-008, EM-001, GG-006, all Derived). RESOLUTION (passes): the fractional pieces are CONFINED (unstable alone) and only exis...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [ELEC-066] THE DYNAMICAL-ELECTRON CONJECTURE: THE SECTOR'S STRONGEST NO-GO SILENTLY ASSUMES A STATIC ...

**Status:** Conjecture  
**Depends on:** ELEC-057, ELEC-058, ELEC-043, ELEC-041, ELEC-036, ELEC-054, PM-005  

Filed as a conjecture with nothing computed, because it is worth recording and worth not overstating. It originated in conversation rather than at a benchmark, and the corpus should be able to tell the difference between the two forever after. WHAT MAKES IT WORTH REGISTERING is not the intuition that the electron is dy...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [EW-001] Weinberg angle sin2thetaW = 1/(3sqrt2) = 0.2357 from winding/Hopf geometry

**Status:** Conjecture  
**Paper:** rope_weinberg_angle  

~1.94% from measured 0.23122; the 'soft external input' that breaks PM-001.

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [NUC-002] Strong nuclear force identified as rope-bundle contact force at nuclear scale (atomic cont...

**Status:** Conjecture  
**Paper:** rope_nuclear_physics  
**Depends on:** NUC-001  

The paper's central proposal: the strong force IS the rope-bundle contact force that creates chemical contact at atomic scales (1e-10 m, eV), operating at nuclear scale (1e-15 m, MeV) -- 1e5x smaller, correspondingly greater energy. Quark confinement follows from fractional sub-knots being unstable alone (see NUC-003)....

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

### [PM-001] Lepton mass ratios via Koide phase (3+Phi)=4.618 to ~1% WITH measured sin2thetaW

**Status:** Conjecture  
**Paper:** rope_lepton_masses  

CONDITIONAL: with the model's own sin2thetaW=1/(3sqrt2) it FAILS (mu/e~1605). [STRUCTURAL CONTEXT (PM-003): the lepton mass problem is a 3-level knot EXCITATION spectrum, not composite counting -- which is why a Koide-type RELATION AMONG LEVELS (this claim) is the relevant kind of tool. The knot-count mass mechanism th...

*Falsification / resolution welcome. See HOW_TO_CRITICIZE.md.*

---

*10 open-frontier claims (6 Open, 4 Conjecture) as of the current registry.*
