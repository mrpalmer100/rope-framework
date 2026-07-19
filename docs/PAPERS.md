# Rope Hypothesis — Paper Index

Master list of the Rope Hypothesis corpus. Credit for the core Rope Hypothesis is due to **Bill Gaede**; this programme develops and formalises it.

---

## ⭐ Read First: Scope and Conclusion

**The Rope Hypothesis is a CLASSICAL, MECHANICAL model of physics.** It gives strong, visualisable, object-level accounts of electromagnetism, gravity, optics, and related classical domains. **In its present configuration-counting form it does not reproduce quantum entanglement** — and this is a *proven boundary of that form*, not a hidden gap: a model that determines outcomes by counting configurations yields classical (CHSH ≤ 2) correlations and cannot produce the amplitude interference that Bell-violating measurements require. Entanglement is **retired as an ambition and preserved as a documented boundary finding.** Nothing is deleted; the negative results are kept as evidence of honest method.

- **Scope and Limits of the Rope Hypothesis** 📄 — the programme's own conclusion; start here.
  `rope_capstone.js` -> `docs/rope_scope_and_limits.docx`

The corpus is organised in three tiers: **(1) In-domain** classical results (the strength); **(2) The Classical Boundary** — the quantum-foundations, non-local-dynamics, and measurement/Born papers, retained as rigorous demonstrations of *where and why* the model ends; **(3) The Conclusion** (this capstone).

---


**Status legend (honest tiers):**  
📄 **Bundled** — full document ships in `docs/` as `.docx`+`.pdf`; content present and verifiable.  
🔧 **Code-backed** — no standalone document ships, but the result rests on live computation in `rope_solver`, `benchmarks`, or `tests` that runs in this package and can be regenerated into a paper.  
📝 **Index tier** — no document ships. **No `.js` build scripts ship in this release at all**, so these are not regenerable from the package. The tier has three honest sub-states:  
 ⊘ **superseded** — an already-bundled paper covers this; the old title is retained only for traceability.  
 🔧⚠ **reconstructable** — shipping `rope_solver` code backs the result, so a document *could* be built (as the phase-2 papers were), but none exists yet.  
 📝 **planned** — title only; no shipped content and no backing code in this release.


## Foundations & Ontology

> **Note:** the three quantum papers below (Measurement Problem, Non-Local Dynamics, Quantum Foundations) constitute **Tier 2 — The Classical Boundary**. They are retained as findings that *locate and prove the rope model's limit at entanglement*, not as successful explanations of it. See the capstone (Scope and Limits) for the full conclusion.


- **The Measurement Problem for the Rope Medium** 📄
  `rope_born.js` -> `docs/rope_measurement_born_problem.docx`  
  *NEGATIVE RESULT: config-entropy counting (S=k ln|C|) gives the triangle wave (π−θ)/π, NOT Born cos²(θ/2) — counting is not interference. Rope model reproduces only classical (CHSH≤2) correlations as formulated; falsified as a complete theory of entanglement pending an amplitude-interference measurement rule. Includes a disclosed, numerically-caught error.*

- **Dynamics of Non-Local Rope Correlations** 📄
  `rope_nonlocal.js` -> `docs/rope_nonlocal_dynamics.docx`  
  *PARTIAL RESULT: local model falsified; non-local update reproduces −cos(a−b) + Tsirelson + no-signalling, but the conditional is imposed; whole viability reduces to one angle map (gamma=1). Honestly reported as open.*

- **Renormalization and Effective Field Theory of the Rope Medium** 📄
  `rope_eft_rg.js` -> `docs/rope_renormalization_eft.docx`  
  *Justifies the coarse-grained form (stiffness marginal, higher-gradient irrelevant); locates the massless photon in 4D compact-U(1); one-loop stiffness stable in the stiff regime. Global flow-to-compact-U(1) left open.*

- **Microscopic Mechanics of the Rope Medium: From Endpoint Locking to Continuum Stiffness** 📄

- **A Γ-Convergence Derivation for the Rope Medium** 📄  

- **Topological Defects in the Rope Medium** 📄  

- **Topology of Defects in Three Dimensions** 📄  

- **The Microscopic Origin of Defect Cores in the Rope Medium** 📄  
  `rope_defcore.js` -> `docs/rope_defect_cores.docx`  
  *Derives the continuum cutoff the defect sector put in by hand. The discrete vortex core is FINITE and universal: E_core = E - piK ln(L/2) -> 5.448 K (size-independent), so the continuum's short-distance divergence is an artefact. Matching fixes a_eff ~ 0.18 spacings; per-bond energy bounded by (1/2)K pi^2 (max angle diff = pi). E = piK ln(L/2)+5.448K reproduces measured energy, no free parameters. Energy concentration, not a Ginzburg-Landau core. Reproducible: benchmarks/micromech/defect_cores.py (5/5).*

- **Topology and Gauge Geometry Underlying the Rope Programme** 📄  
  `rope_gauge.js` -> `docs/rope_gauge_geometry.docx`  
  *The mathematical Rosetta Stone: the corpus's recurring objects (bundle, connection A, curvature F=dA, winding, linking, Hopf, Chern, homotopy) are ONE geometric structure. KEYSTONE computed: Hopf invariant = linking of preimage fibers, via the SAME routine as electric charge. Gauge invariance shown forced, not added. Includes unifying diagram, dependency map, glossary, and rope->math dictionary. Mathematics kept strictly separate from ontology (Part IX). Reproducible: benchmarks/topology/gauge_geometry.py (5/5).*
  `rope_defect_topology_3d.js` -> `docs/rope_defect_topology_3d.docx`  
  *Completes the (planar) defect paper. Vortex-line tension πK ln(R/a) per length; homotopy taxonomy of S¹ defects (line defects & loops EXIST; walls π₀=0 and monopoles π₂=0 do NOT -- monopole exclusion as theorem); defect-loop linking = integer Gauss invariant, the SAME routine the knot sector uses (|Lk|=1 linked, 0 unlinked), conserved under reconnection; loop self-energy grows with size. EM-flux-tube relation stated as OPEN. Reproducible: benchmarks/micromech/defect_topology_3d.py (5/5). Classical.*
  `rope_defect_theory.js` -> `docs/rope_defect_theory.docx`  
  *Completes the vortex regime the homogenization derivation DEFERRED, on the same (K/2)∫|∇θ|² functional. Vortex energy πK ln(R/a) (coefficient confirmed: slope 3.151 vs π); integer conserved winding charge; pair energy 2πK ln(d/a) -> 2D Coulomb / BKT; reconnection conserves charge. Reproducible: benchmarks/micromech/defect_theory.py (5/5). Classical.*

- **The Parameter Count of the Rope Medium** 📄  
  `rope_parameter_count.js` -> `docs/rope_parameter_count.docx`  
  *Three primitives {T,κ,a} carry exactly ONE dimensionless coupling Π=κ a/T (two are unit conventions); Lorentz invariance fixes the line density μ=T/c² but is orthogonal to Π; and the VALUE of Π is provably not fixable by dimensional analysis, Lorentz invariance, or lattice dispersion (Lorentz violation ~(ka)²/24 bounds the scale a, not Π). One irreducible free parameter, with an impossibility proof. Reproducible: benchmarks/micromech/parameter_count.py.*
  `rope_homogenization_theorem.js` -> `docs/rope_homogenization_theorem.docx`  
  *Rigorous Γ-convergence of the discrete endpoint-locking energy to the continuum stiffness (K/2)∫|∇θ|², K=J/a scalar / 2J/a director. Both Γ-inequalities established (within cited standard analysis) on vortex-free fields; O(a²) rate; vortex counterexample shows the hypothesis is necessary. Upgrades the programme's central coarse-graining step from heuristic to a structured Γ-convergence derivation. Reproducible: benchmarks/micromech/gamma_convergence.py.*
  `rope_micromech.js` -> `docs/rope_microscopic_mechanics.docx`  
  *Contains the Factor-of-Three Audit: corrects K=3T²/(κ a) to K=T²/(κ a) (scalar) or 2T²/(κ a) (director).*

- **Quantum Foundations of the Rope Model: A Non-Local Hidden-Variable Framework** 📄
  `rope_quantum.js` -> `docs/rope_theory_of_quantum_foundations.docx`

*Backing module(s): `rope_solver.geometry / topology`* 🔧

- **Thermodynamics and Statistical Mechanics of the Rope Medium** 📄
  `rope_thermodynamics.js` → `docs/rope_theory_of_thermodynamics.docx`
- **The Rope Hypothesis — Ontology (Part I)** 📝 *planned* — title only; no shipped content or code in this release
  `rope_ontology_v2.js`
- **The Weinberg Angle from Three Dimensions and Two Strands** 📄
  `rope_two_axioms.js`
- **Particles as Rope Knots** 📝 *planned* — title only; no shipped content or code in this release
  `rope_knots.js`
- **The Nonlinear Rope Action** 📝 *planned* — title only; no shipped content or code in this release
  `rope_nonlinear.js`
- **The Effective Field Theory of the Rope Medium** ⊘ *superseded* — superseded by **Renormalization and EFT of the Rope Medium** (bundled)
  `rope_eft_v2.js`
- **Rope Bundle Theory** 📝 *planned* — title only; no shipped content or code in this release
  `rope_bundle_paper.js`
- **The Effective Metric from the Rope Action** ⊘ *superseded* — superseded by **Gravity in the Rope Framework** (bundled)
  `rope_metric.js`

## Electromagnetism

- **Optics in the Rope Framework** 📄

- **Classical Optics in the Rope Framework** 📄  

- **Optical Boundary Conditions and Interface Physics in the Rope Framework** 📄  
  `rope_interface_optics.js` -> `docs/rope_interface_optics.docx`  
  *One intrinsic impedance Z=√(Tμ)=T/c; four boundary types (free/aperture/fixed/impedance). Snell (wavefront continuity), Fresnel (r=(Z₁−Z₂)/(Z₁+Z₂), R+T=1), Brewster (tanθ_B=n₂/n₁), AR coatings (R=0), Fabry–Pérot, dielectric mirrors (R→1), Poynting flux. All reproducible: benchmarks/optics/interface_physics.py (7/7). Classical; explains physically why optics stops short of the quantum boundary.*
  `rope_classical_optics.js` -> `docs/rope_classical_optics.docx`  
  *One wave equation (ω=ck, c²=T/μ), eight boundary-condition solutions: non-dispersive propagation, Huygens, single-slit diffraction (sinθ=λ/a), two-slit interference, standing waves (ωₙ=nπc/L), cavities (f₁=c/2L), waveguide cutoff (πc/a), fibre TIR (arcsin n₂/n₁). All reproducible: benchmarks/optics/classical_optics.py (8/8). Entirely classical; does not touch the quantum boundary.*
  `rope_optics.js` -> `docs/rope_optics.docx`  
  *Classical interference & diffraction as genuine rope-wave superposition (two-slit law I∝1+cos(2πΔ/λ), obstacle/needle diffraction). Single-photon interference is the documented quantum boundary (needs amplitude interference; g²<1 closes the weak-wave escape).*

*Backing module(s): `rope_solver.electromagnetism`* 🔧

- **Electricity in the Rope Framework** 📄  
  *Charge = linking number (|Lk|=0.999≈1, topological quantisation); ε₀, Z₀=376.74Ω, 1/α=137.06 from structure; Maxwell from Bianchi + Chern–Weil + d=3. Classical in-domain; α value not derived from nothing.*
  `rope_electricity_paper.js`
- **Magnetism in the Rope Framework** 📄
  `rope_magnetism_paper.js` → `docs/rope_theory_of_magnetism.docx`
- **Maxwell's Equations from the Vortex Rope Model** 📄
  `rope_maxwell.js` → `docs/rope_maxwell_equations.docx`
- **Maxwell's Equations from Hopf Bundle Topology** 📄
  `rope_topo_maxwell.js` → `docs/rope_topological_maxwell.docx`
- **Light in the Rope Framework** ⊘ *superseded* — superseded by **Optics in the Rope Framework** (bundled)
  `rope_light_paper.js`
- **The Electric Potential as Rope Tension** 📄
  `rope_a0.js`
- **The Alpha Coefficient in Rope Bundle Theory** 📄
  `rope_alpha_paper.js`
- **The Coupling Identification and Higher Links** ⊘ *superseded* — superseded by **Higher Rope Links** + **The Alpha Coefficient** (bundled)
  `rope_alpha_links.js`

## Gravity & Relativity

- **Gravity in the Rope Framework** 📄
  `rope_gravity.js` -> `docs/rope_gravity.docx`  
  *Classical result: rope effective metric = isotropic Schwarzschild (weak field); PPN γ=β=1; light deflection 1.751″, Mercury 43.0″/century, Shapiro γ=1, Nordtvedt η=0, all computed from the metric. Weak-field/PPN only; no strong-field or quantum-gravity claim.*

*Backing module(s): `rope_solver.gravity`* 🔧

- **Rope Cosmology: Cosmology of an Interpenetrating Rope Medium** 📄
  `rope_cosmology.js` → `docs/rope_theory_of_cosmology.docx`
- **General Relativity in the Rope Framework** ⊘ *superseded* — weak-field metric/PPN content is in **Gravity in the Rope Framework** (bundled)
  `rope_gr_paper.js`
- **Special Relativity in the Rope Framework** 📝 *planned* — title only; no shipped content or code in this release
  `rope_sr_paper.js`
- **Gravitoelectromagnetism from the Vortex Rope Model** 📝 *planned* — no shipped content or backing function (earlier 'reconstructable' tag was over-generous; corrected on code audit)
  `rope_gem.js`
- **The Rope Orientation Quadrupole and Tensor Gravitational Waves** ⊘ *superseded* — folded into the gravitational-wave polarisation entry
  `rope_gw.js`
- **Gravitational Wave Polarisation as a Test of the Rope Hypothesis** 📝 *planned* — title only; no shipped content or code in this release
  `rope_ligo_paper.js`
- **Newton to MOND via Rope Winding Coherence** 📝 *planned* — no shipped content or backing function (earlier 'reconstructable' tag was over-generous; corrected on code audit)
  `rope_mond.js`
- **The Rope Model and the Radial Acceleration Relation** 📝 *planned* — no shipped content or backing function (earlier 'reconstructable' tag was over-generous; corrected on code audit)
  `rope_rar_paper.js`
- **Rope Tension from Energy Density** 📝 *planned* — no shipped content or backing function (earlier 'reconstructable' tag was over-generous; corrected on code audit)
  `rope_T_u_paper.js`
- **The Effective Rope Density n_rope** ⊘ *superseded* — duplicate of **Rope Tension from Energy Density**
  `rope_n_rope_paper.js`
- **A Phenomenological Rope Tension Model for Galaxy Rotation Curves** 📝 *planned* — no shipped content or backing function (earlier 'reconstructable' tag was over-generous; corrected on code audit)
  `preprint.js`

## Particle Masses & Mixing

*Backing module(s): `rope_solver.particles`* 🔧

- **Lepton Masses from Rope Topology** 📄
  `rope_masses_paper.js`
- **Mass Weights of Standard Model Particles** 📄
  `rope_mass_weights.js`
- **Neutrino Mass Ratios in the Rope Hypothesis** 📄
  `rope_neutrino_paper.js`
- **Correction: Neutrino Mass Hierarchy Ratio from the Brannen Formula** 📄
  `rope_neutrino_corrected.js`
- **The Origin of the Brannen Neutrino Offset (π/12)** 📄
  `rope_pi12.js`
- **Neutrino Mixing Angles from the Rope Framework (PMNS)** 📄
  `rope_pmns.js`
- **A Numerical Bridge: Pion Mass, QCD String Tension, and the Lepton Sector** 📄
  `rope_pion_lepton.js`

## Electroweak & Chern-Simons

*Backing module(s): `rope_solver.particles / topology`* 🔧

- **The Rope Winding Angle as the Weinberg Angle** 📄
  `rope_weinberg_paper.js`
- **The Weinberg Angle from Hopf Bundle Geometry** 📄
  `rope_hopf_weinberg.js`
- **Parity Violation and the Weak Force in the Rope Framework** 📝 *planned* — no shipped content or backing function (earlier 'reconstructable' tag was over-generous; corrected on code audit)
  `rope_weak.js`
- **Level 4: The Dirac Equation from Two-Strand Rope Mechanics** 📝 *planned* — title only; no shipped content or code in this release
  `rope_dirac_paper.js`
- **φ = (3+Φ)θ_W: A Complete Theorem** 📝 *planned* — title only; no shipped content or code in this release
  `rope_cs_theorem.js`
- **The Koide Phase from T-Parity in SU(2)₃ Chern-Simons Theory** 📝 *planned* — title only; no shipped content or code in this release
  `rope_cs_proof.js`
- **The Electron Knot in SU(2)₃ Chern-Simons Theory** 📝 *planned* — title only; no shipped content or code in this release
  `rope_cs_step4.js`
- **Derivation of the Koide Phase from Chern-Simons Topology** 📝 *planned* — title only; no shipped content or code in this release
  `rope_phi_braid_paper.js`
- **Correcting the Chiral Linking Lemma** 📝 *planned* — title only; no shipped content or code in this release
  `rope_chiral_lemma.js`
- **The Holonomy-Momentum Lemma** 📝 *planned* — title only; no shipped content or code in this release
  `rope_casimir_lemma.js`
- **Berry Holonomy and Color Holonomy in the Rope Framework** 📄
  `rope_holonomy.js`

## Solitons & Knot Spectrum

- **Higher Rope Links and the Charge–Linking Correspondence** 📄  
  `rope_higher_links.js` -> `docs/rope_higher_links.docx`  
  *Torus links Lk=2,3 conserve linking number under relaxation (1.983, 2.951); integer charge quantisation from integer Lk. Reproduced.*

*Backing module(s): `rope_solver.relaxation / spectrum / psi`* 🔧

- **Hopf-Link Solutions and the Rope Soliton Spectrum** 📄
  `rope_hopf.js`
- **Self-Consistent Rope Solitons** 📄
  `rope_soliton.js`
- **Full-Field Rope Solitons** 📄
  `rope_fullfield.js`
- **Numerical Relaxation of Fully Flexible Hopf Links** 📄
  `rope_flexible.js`
- **Quantum Fluctuations Around Rope Knots** 📄
  `rope_det.js`
- **Quantum Rope Perturbation Theory** 📄  
  *NEGATIVE RESULT: one-loop fluctuation log-det ≈ −1.29 (O(1), no negative modes) vs electron requirement ≈108 — falsifies the one-loop mass mechanism by ~80×. Kept as a finding.*
  `rope_qpt_paper.js`
- **Phase Coherence and Decoherence in the Rope Network** 📄
  `rope_coherence.js`

## Chemistry, Nuclear & Black Holes
- **Nuclear Physics in the Rope Framework** ✅ *shipped* — strong force as rope-bundle contact (atomic contact scaled ~1e5); quarks as confined fractional sub-knots summing to integer winding; nuclear binding as rope-mode overlap (Fe-56 peak); alpha/beta/gamma decay mechanisms. Atomic masses reproduced <0.1% from nucleon-knot count minus binding (NUC-001). Claims NUC-001/002/003; benchmark benchmarks/em/atomic_mass_from_nucleons.py.
  `docs/rope_nuclear_physics.docx`
- **Chemistry in the Rope Framework** ✅ *shipped* — atomic structure, bonding, and molecular geometry from rope network modes. Hydrogen rope-mode equation identical to the hydrogen Schrödinger equation (Eₙ=−13.6/n² eV, orbital shapes); shell filling 2n²; covalent/ionic/metallic/H-bonding; sp/sp²/sp³ hybridisation; electronegativity as nuclear tension; a proposed Pauli mechanism. Honest three-level scope (clean / needs-rope-math / open). Shell-counting reproduced by benchmarks/em/periodic_shell_counting.py (claim CHEM-STRUCT-001).
  `docs/rope_theory_of_chemistry.docx`


- **Nuclear Physics in the Rope Framework** 📝 *planned* — title only; no shipped content or code in this release
  `rope_nuclear_paper.js`
- **Black Holes in the Rope Framework** 📝 *planned* — title only; no shipped content or code in this release
  `rope_blackhole_v2.js`

## Predictions, Audits & Methods

- **Master Claim-Status Registry** 📄
  `rope_registry.js` -> `docs/rope_claim_status_registry.docx`  
  *One canonical table of every principal claim in the external set: Status (Derived/EFT-constrained/Modeled/Failed/Open), Paper, Dependency, Corrected?, External test? Classical claims all Derived/Modeled; Failed/Open entries are all quantum-boundary.*

- **Condensed-Matter Analogues of the Rope Medium: Near-Term Tabletop Tests** 📄
  `rope_condmat.js` -> `docs/rope_theory_of_condensed_matter.docx`

- **Falsifiable Predictions of the Rope Hypothesis** 📄
  `predictions_paper.js` → `docs/falsifiable_predictions.docx`
- **The Three-Way Consistency Check** 📝 *planned* — title only; no shipped content or code in this release
  `rope_3way_paper.js`
- **Rope Framework Consistency Audit** 📝 *planned* — title only; no shipped content or code in this release
  `rope_audit.js`
- **Computational Rope Theory** 📝 *planned* — title only; no shipped content or code in this release
  `rope_comp.js`
- **A Computational Toolkit for Rope Solitons** 📝 *planned* — title only; no shipped content or code in this release
  `rope_methods.js`

## Reference

- **The Rope Picture of the Universe (Plain-Language Guide)** 📄
  `rope_plainlanguage.js` → `docs/rope_plain_language_guide.docx`
- **The Rope Hypothesis — Glossary** 📝 *planned* — title only; no shipped content or code in this release
  `rope_glossary_v3.js`
- **Rope Hypothesis Glossary — Addendum** 📝 *planned* — title only; no shipped content or code in this release
  `rope_glossary_update.js`

---

**Corpus status (this release):** 82 titles across 9 sectors. **49 bundled** — full `.docx`+`.pdf` present and verifiable; these are the finished documents in this package. The remaining 35 carry no document, and **no `.js` build scripts ship in this release**, so none are regenerable from the package as shipped. They divide honestly into **7 superseded** (each covered by a bundled paper; retained only for traceability) and **28 planned** (title only, no shipped content or backing code). An earlier interim tier called ‘reconstructable’ is now empty: every title with shipping computational backing was either built into a bundled paper or, where a code audit found the backing insufficient, honestly moved to superseded or planned. This replaces any earlier implication that the non-bundled titles are regenerable from shipped build scripts — they are not.


*Titles auto-extracted from build scripts. Superseded early versions (black holes, EFT, ontology, glossary v1/v2) have been removed; only current versions are listed.*

---

**Machine-readable companions (new):** `claims.yaml` is the machine-readable claim registry (id / status / paper / benchmark / depends_on) consumed by `tools/verify_corpus.py` (one-command verification: runs every referenced benchmark) and `tools/build_depgraph.py` (emits `docs/dependency_graph.dot` / `.txt`). Run `make verify` or `python tools/verify_corpus.py` to reproduce every code-backed claim; see `docs/dependency_graph.txt` for what depends on what.
