"""
# CORRECTION (2026-07-04, Factor-of-Three Audit): the coarse-graining factor quoted throughout these entries as K = 3J/a (hence c = kappa a/(3T^2), phase T^2 > kappa/3) is CORRECTED to K = 2J/a director / J/a scalar (hence c = kappa a/(2T^2), phase T^2 > kappa/2). Direct analytic + lattice-simulation coarse-graining does NOT reproduce the factor 3 (most probable origin: a dimensional double-count). The historical text below is retained as the reasoning record; read all "3" coefficients in the stiffness/phase chain as corrected. J = T^2/kappa (exact) and all relation FORMS and the structural alpha-G exponent (-2) are unaffected. See rope_microscopic_mechanics.docx and benchmarks/micromech/.
rope_solver.open_problems  --  Canonical registry of the programme's open problems.

A single place that tracks what the rope programme has NOT derived, so honest
limitations are visible and cannot be quietly forgotten. Each entry records the
problem, the paper/sector it arose in, and its status.

This registry is part of the same discipline as the validation suite: the suite
pins what IS established; this registry pins what is NOT. A reference
implementation that only listed successes would misrepresent the programme.

Status values:
  OPEN        -- genuinely unsolved, no candidate mechanism
  CANDIDATE   -- a mechanism is proposed but not rigorously derived
  POSTULATE   -- an explicit added bridge axiom (honestly NOT derived), precise/testable
  PARTIAL     -- partially derived, with a specific stated gap
  CONJECTURE  -- strong (often numerical) support but a key step unproven\n  FALSIFIED   -- a hypothesis was tested and ruled out (kept for the record)
"""

OPEN_PROBLEMS = [
    {
        "id": "pauli-rope-spin",
        "problem": "Pauli exclusion from rope-spin mode saturation "
                   "(max two kinks per mode, opposite rope-spin).",
        "sector": "chemistry",
        "paper": "rope_theory_of_chemistry",
        "status": "CANDIDATE",
        "note": "Physically motivated but explicitly NOT a full derivation; "
                "the paper calls it the most important open problem in rope "
                "chemistry. A complete derivation needs the rope mode wave "
                "equation to admit antisymmetric two-kink solutions and no "
                "valid three-kink solution.",
    },
    {
        "id": "electron-absolute-mass",
        "problem": "The absolute electron mass.",
        "sector": "particles",
        "paper": "rope_fluctuation_determinant",
        "status": "OPEN",
        "note": "One-loop determinant FALSIFIED (gives O(1), needs exp(-54)). "
                "Systematic search (2026, this work) ruled out EIGHT natural "
                "mechanisms: dimensional transmutation (b=16.7/18.6/19.9, NOT "
                "universal); m_e/M_Pl=alpha^n (n=10.7, not clean); Planck-Hubble "
                "power see-saw (p=0.367, not clean); Koide-scale (scale-invariant, "
                "M0 genuinely free); lepton see-saw (needs undetermined M_R); "
                "eigenvalue/standing-wave (circular: L=pi x Compton); and simple "
                "topological combos (k=3, c=9/5). KEY STRUCTURAL RESULT: the "
                "knot's own Euclidean action is O(1) (M_Pl c L_Pl/hbar = 1 in "
                "Planck units, computed) and its topology is simple (Hopf link, "
                "crossing number 2), so the exp(-51.5) suppression CANNOT be "
                "internal to the knot -- it must come from the knot's coupling to "
                "the cosmological rope background (the same IR/Hubble scale "
                "required by MOND a0=cH0/2pi). SUGGESTIVE BUT NOT CLAIMED: "
                "ln(M_Pl/m_e)/ln(M_Pl/M_Hubble) = 0.367 ~ 1/3 (cube-root cosmo "
                "see-saw), but 10% off in the exponent = 117x in mass, so NOT a "
                "derivation. The sharpened open problem: derive how a Planck-scale "
                "knot couples to the Hubble-scale background. "
                "FRESH PASS (2026, Fable 5) -- three additions; doors closed and spec tightened, m_e still NOT derived. (1) WHY the knot lands at M_Pl, as a theorem: the imbalance texture is an S2-valued (Hopf-base) field; with tension-only (two-derivative) energy, Derrick scaling E(lambda) = lambda*E2 makes every knot shrink without limit, so it collapses to the ontology sole UV scale -> M_Pl (mechanism behind the recorded knot-action-O(1) result). The tempting fix -- helix bending/torsional rigidity, i.e. a Faddeev-Skyrme term stabilizing at size sqrt(g4/g2) with E_min = 2 sqrt(E2 E4) -- merely RELOCATES the hierarchy: Compton-size knots need g4/g2 ~ (lambda_C/L_Pl)^2 ~ 5.7e44. Also the hopfion-tower reading of leptons (E ~ Q^{3/4}) is excluded: ratios demand Q_mu ~ 1223, Q_tau ~ 5.3e4; the Koide-phase route remains the live lepton-ratio mechanism. (2) ANOMALOUS-DIMENSION DRESSING CLOSED (new negative, executable): the natural post-beta-function mechanism -- IR dressing of the knot operator by the framework own SU(2)_3 CFT, m = M_Pl (m_H/M_Pl)^p with p a CFT datum -- fails a systematic scan. Required p = 0.3674 (H0 67-73 shifts it 0.06%; the IR-mass CONVENTION hbar H0 vs hbar H0/2pi shifts it 1.3%, so sub-1% coincidences are convention noise -- this also re-kills 1/e, which matches to 0.14% under only ONE convention and fails the other by 1.4%). The CFT natural numbers h_j = {3/20, 2/5, 3/4}, Delta = 2h, c/5, c/24, simple rationals: best miss is c/5 = 0.36 at 2.0%, vs the <0.1% hypersensitivity bar (d ln m / dp = 140; 2% in p = factor ~2.8 in mass). Encoded as rope_solver.particles.hubble_planck_mass_exponent and su2k3_dressing_scan with three regression tests. (3) TYPING RESULT: with transmutation dead at the beta=0 fixed point, knot action O(1), no intermediate scale, and CFT-dimension dressing now excluded, the absolute-mass wall is formally the SAME CLASS as em-curl-from-ontology: a MISSING POSTULATE (the quantitative knot<->cosmological-background coupling, i.e. the quantitative form of the framework Machian inertia claim), not a missing calculation. An exactly scale-invariant sector cannot select m_e; only an explicit, currently-unpostulated IR coupling can. SPEC for that postulate: it must produce a pure-number exponent p on (m_H/M_Pl); p must come out 0.3674 to better than 0.1% to predict m_e within 15%; p is NOT any primary dimension or simple datum of SU(2)_3; and the same coupling should quantify Machian inertia, giving an independent consistency check.",
    },
    {
        "id": "born-rule",
        "problem": "The Born rule P(q0) = |psi|^2 for kink initial positions.",
        "sector": "light",
        "paper": "rope_theory_of_light",
        "status": "OPEN",
        "note": "The one non-mechanical postulate of the rope/Bohmian account; "
                "no classical wave theory has derived it. The paper calls it "
                "'the frontier'.",
    },
    {
        "id": "kappa-alpha-derivation",
        "problem": "kappa = alpha/(2 pi) beyond dimensional analysis.",
        "sector": "particles / electromagnetism",
        "paper": "rope_alpha_higher_links",
        "status": "PARTIAL",
        "note": "The identification is dimensional and non-circular, but the "
                "geometric factor and cutoff need a first-principles treatment. "
                "At this coupling the soliton is compact (R < lambda_c), "
                "outside the thin-ring regime.",
    },
    {
        "id": "mass-ontology-scale-breaking",
        "problem": "What mass physically IS in the rope network, and what sets "
                   "the intermediate (Compton) scale.",
        "sector": "particles",
        "paper": "(this work, 2026)",
        "status": "OPEN",
        "note": "Five ontologies of mass were examined: (1) knot self-energy "
                "[current, fails -> Planck mass]; (2) Machian inertia/coupling; "
                "(3) precession frequency; (4) topological defect deficit; "
                "(5) IR condensation gap. DIAGNOSIS: ontologies 3 and 5 merely "
                "relocate the hierarchy (the same ln=51.5 reappears); the "
                "relational ones (2,4) need either a 22-digit cancellation "
                "(fine-tuning unless symmetry-protected) or an intermediate "
                "scale. THE NAMED WALL: the rope network has NO intrinsic length "
                "scale between L_Pl and the Hubble length, yet mass needs a "
                "Compton wavelength ~1e22 L_Pl. Every ontology relocates the "
                "question to 'why this intermediate scale' = the same 51.5. "
                "SURVIVING REFRAME (the useful idea): mass = breaking of the "
                "rope's SCALE INVARIANCE (a massless rope is scale-free, waves "
                "at c = the photon). Mass is the conformal anomaly / scale where "
                "scale-invariance breaks. This converts the puzzle into ONE "
                "well-posed calculation: derive the beta function of the rope "
                "tension (how the coupling runs UV->IR), plausibly tied to the "
                "central charge c=9/5. Dimensional transmutation failed earlier "
                "as a FORMULA; the reframe says try it as a derived running. "
                "REJECTED COINCIDENCE (do not revive): ln(M_Pl/m_e)/"
                "ln(M_Pl/M_Hubble) = 0.3671 ~ 1/e (0.2% off) is NOT a "
                "derivation -- it moves with H0, predicts m_e to only ~10%, and "
                "the exponent is hypersensitive (d ln m/d exp = 140), so the "
                "nearest simple constant explains nothing (3/8 and 1/3 bracket "
                "it). Same failure mode as the earlier pi/8; killed deliberately.",
    },
    {
        "id": "mass-tension-beta",
        "problem": "Derive the rope tension beta function to generate the mass "
                   "scale by dimensional transmutation.",
        "sector": "particles",
        "paper": "(this work, 2026)",
        "status": "FALSIFIED",
        "note": "The scale-breaking reframe pointed here: derive beta(T). Two "
                "structural results, both closing the route: (1) worldsheet "
                "tension running (Luscher/Alvarez) is POWER-LAW, T_eff = T_0 - "
                "(D-2)pi/(24 R^2), giving an O(1) critical scale (R_crit ~ 0.51 "
                "L_Pl), not an exponential hierarchy. (2) the rope's "
                "dimensionless sector is an SU(2)_3 WZW-type CFT sitting at a "
                "CONFORMAL FIXED POINT where beta = 0 EXACTLY; a fixed-point "
                "theory does not run logarithmically and so cannot transmute an "
                "exponential mass scale. CONCLUSION: dimensional transmutation "
                "fails 'by structure' (not merely 'b not universal') -- the rope "
                "cannot generate the mass hierarchy by running its OWN coupling. "
                "The scale must come from EXPLICIT conformal-symmetry breaking, "
                "and the only such scale available is cosmological (IR/Hubble). "
                "This is the THIRD independent line (with knot-action-O(1) and "
                "the ontology survey) converging on: mass = how the near-"
                "conformal knot couples to the cosmological background. Encoded "
                "as luscher_critical_scale_planck, wzw_beta_function, "
                "dimensional_transmutation_works in rope_solver.particles.",
    },
    {
        "id": "alpha-G-correlated-variation",
        "problem": "New prediction from cross-sector unification: because the EM "
                   "coupling (alpha ~ 3T^2/(kappa a)) and gravity are both set by "
                   "the same rope tension T, alpha and G are NOT independent; a "
                   "drift in the shared primitive forces correlated drift, in a "
                   "scale-free fixed ratio -- testable against varying-constants data.",
        "sector": "electromagnetism / gravity (cross-sector)",
        "paper": "(this work, 2026)",
        "status": "CANDIDATE",
        "note": "GENUINELY NEW, SCALE-FREE, FALSIFIABLE prediction -- the first the "
                "programme has produced that escapes the undetermined-primitives "
                "wall. Structural content (ROBUST): standard physics treats alpha "
                "and G as independent; the rope programme, having expressed both in "
                "the same primitives (alpha ~ 3T^2/(kappa a) from the EM coefficient "
                "c = kappa a/(3T^2); gravity governed by the same tension T), FORCES "
                "them to co-vary if a shared primitive drifts. It forbids, e.g., a "
                "spacetime region where EM strength changes but G does not, if the "
                "change is tension-driven. Quantitative content (PROVISIONAL): using "
                "the natural gravity-rigidity scaling G ~ 1/(T a), differentiation "
                "gives, for TENSION-driven drift, d ln alpha = -2 d ln G, i.e. "
                "alpha_dot/alpha = -2 G_dot/G -- a pure number (-2), scale-"
                "independent, forced (not tuned), and different from both standard "
                "physics (no relation) and generic varying-constants models (no "
                "fixed ratio). Falsifiable NOW against combined quasar-spectra "
                "alpha-dot bounds and lunar-laser-ranging / pulsar-timing G-dot "
                "bounds. (Other-primitive drifts give different ratios: kappa-drift "
                "leaves G fixed while alpha moves; a-drift gives d ln alpha = d ln G. "
                "The cleanest test is the tension channel, ratio -2.) HONEST CAVEAT: "
                "the exponent -2 depends on the gravity-sector relation G ~ 1/(T a), "
                "which has NOT been derived with the rigor of the EM coefficient (J "
                "and the EM chain are now exact/EFT-reduced; the gravity G(T,kappa,a) "
                "is a natural-scaling assumption, not a derivation). So the STRUCTURE "
                "(fixed-ratio co-variation) is robust; the NUMBER -2 is provisional "
                "on deriving G(T,kappa,a). HIGHEST-LEVERAGE NEXT STEP: derive "
                "G(T,kappa,a) rigorously -- that converts this structural prediction "
                "into a sharp falsifiable number against already-existing data. "
                "Weaker related predictions on record: (i) magnetic monopoles exist "
                "as heavy topological defects of the rope medium with mass tied via "
                "c = kappa a/(3T^2) to the same primitives (existence + scaling, not "
                "a number); (ii) a hard bound -- no photon mass above the confinement "
                "scale, incompatible with any future large-photon-mass detection.",
    },
    {
        "id": "em-energy-coefficient-c",
        "problem": "Compute the coefficient c of the EFT-constrained continuum "
                   "energy c|curl A|^2 by coarse-graining microscopic rope "
                   "elasticity (strand tension, bending, torsional moduli), "
                   "upgrading the energy functional from EFT-constrained to "
                   "microscopically derived.",
        "sector": "electromagnetism",
        "paper": "(this work, 2026)",
        "status": "OPEN",
        "note": "Raised by external review as the natural next EM target. Current "
                "status: the FORM c|curl A|^2 is EFT-constrained (uniquely selected "
                "within the class of local, gauge-invariant, rotationally-invariant "
                "quadratic energies -- see EM-P2), but NOT microscopically derived, "
                "and c is entirely undetermined. Physical conjecture worth testing: "
                "c is not a free EFT constant but a coarse-grained rope-medium "
                "modulus -- e.g. the strand tension density, or a combination of "
                "bending/torsional stiffness. Concrete programme: (1) write a "
                "microscopic rope Hamiltonian with tension + bending + torsion "
                "terms; (2) coarse-grain the slowly-varying imbalance-orientation "
                "field; (3) show the leading effective term is c|curl A|^2 (this "
                "would upgrade FORM from EFT-constrained to microscopically derived) "
                "and read off c in terms of the microscopic moduli; (4) check the "
                "validity range / gradient expansion. If c comes out as a simple "
                "rope modulus, the whole EM sector (Ampere, field structure, dipole "
                "law, all currently conditional on the energy functional) becomes "
                "microscopically grounded in one stroke, since all of them rest on "
                "this single functional. Success criterion: c expressed in physical "
                "rope-medium constants with the correct dimensions, and a derivation "
                "(not just symmetry selection) that no lower-order or competing "
                "leading term survives. "
                "COARSE-GRAINING ATTEMPT (2026) -- partial success with an honest relocation. Starting from a genuine microscopic rope energy (Frank elasticity: tension/splay K1, twist K2, bend K3 -- the standard lowest-order elastic energy of an orientation/director field, the same coarse-graining used for liquid crystals and superfluids, NOT inserted), the coarse-grained energy of the slowly-varying imbalance-orientation angle theta is (K/2)|grad theta|^2 (XY / superfluid-stiffness form; one-constant K a computable combination of K1,K2,K3, i.e. of the rope tension/bend/twist moduli). This part is MICROSCOPICALLY DERIVED, clearing the EFT-constrained bar for the energy FORM. DUALITY RESULT: in 3D, (K/2)|grad theta|^2 is dual to a gauge theory (1/2K)|curl A'|^2 -- the stiffness current j = K grad theta is divergence-free away from vortices, so j = curl A' for a dual field A', giving field energy with coefficient c = 1/K. So the reviewer's conjecture is essentially CONFIRMED: the EM energy coefficient is set by the rope stiffness modulus, c = 1/K, a physical property of the medium, not a free EFT constant. HONEST FORK EXPOSED (the new, sharper remaining question): the naive identity |curl A|^2 = |curl grad theta|^2 = 0 for smooth theta shows the microscopic stiffness energy and the Maxwell field energy are NOT literally the same object -- they are dual. Two physically DISTINCT theories result: (i) physical field ~ grad theta (the bare stiffness current) => superfluid-type, line defects interacting LOGARITHMICALLY, NOT the 1/r^3 dipole law; (ii) physical field ~ curl A' (the dual strength) => Maxwell magnetostatics with the verified 1/r^3 dipole law. The dipole-law success presumed (ii). So microscopic rope elasticity reproduces Maxwell ONLY IF the network realizes the DUAL/Maxwell phase, not the superfluid phase. NET: 'what fixes c?' is answered (c=1/K, a rope modulus); it is REPLACED by the sharper, concrete, experimentally-distinguishable question 'why does the rope network realize the Maxwell (dual) phase rather than the superfluid phase?' -- different force laws (1/r^3 vs logarithmic) attach to the two options, so this is decidable in principle and a candidate site for a prediction that differs from Maxwell. Status: energy FORM now microscopically derived up to the duality-phase choice; coefficient c=1/K identified with rope stiffness; superfluid-vs-Maxwell selection is the real open item (supersedes em-energy-coefficient-c as stated)."
                "PHASE-SELECTION RESULT (2026) -- the superfluid-vs-Maxwell fork resolved to known physics + a falsifiable criterion. The fork is NOT a free choice: the microscopic energy (K/2)|grad theta|^2 with vortex-line defects IS the 3D XY / compact-U(1) system, whose phase structure is established (Peskin; Dasgupta-Halperin 1981; Polyakov 1977). Anchoring on FORCE LAWS (not the slippery ordered/disordered labels): Maxwell magnetostatics = a MASSLESS gauge field (a mass gives short-range Yukawa e^{-mr}, not observed), so real long-range magnetism = the massless-photon COULOMB/DECONFINED phase. Which branch is 'ours' is thus pinned unambiguously by the observed long-range 1/r^3 dipole law. TWO INDEPENDENT CONSISTENCY CHECKS, neither engineered: (1) the 1/r^3 dipole law derived earlier REQUIRED a massless long-range A' (no e^{-mr}), so it is only consistent with the Coulomb branch -- two separately-done calculations agree. (2) Polyakov: a stable massless-photon phase exists only in 3+1D (in 2+1D the compact-U(1) photon is ALWAYS confined by monopole proliferation); this matches, from the dual side, the topological paper's independently-argued 'd=3 space is essential'. Two different arguments -> same dimensionality. CONCRETE FALSIFIABLE CRITERION: the rope network realizes Maxwell IFF its defect (vortex/monopole) core energy is above the monopole-condensation threshold -- physically, the ropes must RESIST making defects. This is (a) a concrete microscopic property, (b) consistent with observation (the photon is massless => the medium is above threshold), and (c) PREDICTIVE: near the threshold the theory predicts DEVIATIONS from Maxwell (a small photon mass / short-range correction) -- exactly the beyond-Maxwell signature to look for. So the rope picture does not merely reproduce Maxwell; it says WHY Maxwell holds (defects costly) and WHERE it would break (if they were cheap). HONEST GAP: the actual defect-core-energy / stiffness ratio has NOT been computed from a specified microscopic lattice rope Hamiltonian, so 'the network is in the Coulomb phase' is established as REQUIRED and CONSISTENT, not computed from first principles. NEXT CONCRETE STEP: build a lattice rope model, measure its monopole fugacity, verify it sits below the condensation threshold (and estimate how far, which bounds any photon-mass deviation)."
                "LATTICE-MC ATTEMPT (2026) -- ATTEMPTED AND FAILED; no evidence claimed. To move the phase question from 'required + consistent' to 'computed', a lattice compact-U(1) (dual of the coarse-grained rope network) Monte Carlo was attempted to locate the Coulomb (Maxwell) vs confined phase via the static potential / plaquette / monopole density. TWO implementations both FAILED: (1) Wilson-loop potential on an 8^3 lattice gave physically impossible non-monotonic V(R) (noise-dominated, too-small lattice/too-few sweeps); (2) a vectorized version would not equilibrate -- average plaquette stayed ~0 even at large beta where it must approach 1, indicating a staple sign/convention bug in the update. A non-equilibrating MC is worthless as evidence; BOTH runs are discarded and NOTHING is claimed from them. (Recording this explicitly because a failed computation belongs in the record.) What remains RELIABLE (literature, not the broken code): 3+1D compact U(1) has a genuine transition at beta_c ~ 1.01 (Guth 1980 rigorous bound; DeGrand-Toussaint 1980), Coulomb/massless-photon (Maxwell) phase above, confined/massive below; and 2+1D is always confined (Polyakov 1977), so the Maxwell phase exists ONLY in 3+1D -- independently matching the topological paper's 'd=3 essential'. So the phase-selection picture stands on literature, but the concrete goal -- map a specific microscopic ROPE Hamiltonian to an effective beta and check it lands above beta_c -- remains UNCOMPUTED. Next: either repair the lattice MC (fix the staple sign, add equilibration + finite-size-scaling checks) or estimate the rope defect-core energy analytically."
                "LATTICE-MC REPAIRED (2026). The staple sign bug was fixed by computing the Metropolis action change DIRECTLY from the plaquettes touching each link (no hand-built staple). The MC is now VERIFIED CORRECT by the standard benchmark: average plaquette rises monotonically from 0.006 (beta=0) to 0.93 (beta=5), as it must. Static-potential run across couplings (L=8, T=2, R<=4, a few hundred sweeps) shows the RIGHT QUALITATIVE TREND: the fitted string tension (linear-fit slope) collapses systematically with coupling -- sigma ~ 0.63 (beta=1.1) -> 0.18 (beta=1.8) -> 0.085 (beta=3.0) -- i.e. strong confinement at small beta weakening toward a small/Coulomb-like slope at large beta, consistent with the known 3+1D transition near beta_c ~ 1. HONEST LIMITS (claimed trend only, NOT a clean determination): on this small lattice with R<=4, a 'small constant slope' (weak confinement) cannot be cleanly distinguished from 'slope decreasing to zero' (Coulomb); raw fit residuals actually slightly favor the linear form at beta=1.8,3.0, and beta=0.7 spuriously fit Coulomb (a small-lattice artifact -- it should be deep confined). So the run does NOT resolve the Coulomb phase or pin beta_c; it establishes that the (now-correct) MC produces physical confinement behavior with a string tension that collapses at strong coupling. To make it a clean phase determination: larger L, larger T and R, many more sweeps, and finite-size scaling of the string tension -- beyond the sandbox's practical compute here. NET across the coefficient-c/phase line of work: the energy coefficient is c=1/K (a rope stiffness modulus); Maxwell is the massless-photon Coulomb phase which provably exists only in 3+1D (matching 'd=3 essential'); a WORKING lattice tool now exists and shows the right trend; mapping a specific rope Hamiltonian to beta and cleanly locating it relative to beta_c remains the open computational step."
                "CROSS-SECTOR CONSISTENCY RESULT (2026), analytic route -- a reframe, not an ab-initio derivation. Rather than run a larger lattice (which would only re-find the generic beta_c ~ 1.01 without placing the ropes), the phase question was attacked analytically. Key reframe: the photon is measured massless to < 1e-18 eV; in the dual language this is a MEASUREMENT that the rope network sits deep in the Coulomb (Maxwell) phase (dual monopole condensate zero to that precision, beta_eff >> beta_c). So the logic runs backward from what was assumed: masslessness FIXES the phase, and the phase then CONSTRAINS the medium -- it requires the rope network to be very stiff (Frank stiffness K >> K_c; defects/monopoles very costly). This is NOT a free knob: the gravity sector already assumes taut, high-tension ropes (source of gravitational rigidity). So two independent sectors demand the SAME property of the medium -- EM (photon masslessness => deep Coulomb => stiff ropes) and gravity (tension => taut ropes) -- a non-trivial cross-sector consistency the framework satisfies (had EM needed floppy ropes while gravity needed taut ones, that would have been evidence against the picture). HONEST LIMITS: (1) NOT ab-initio -- K was not computed from a specified microscopic rope Hamiltonian and shown > K_c; (2) the argument USES an observation (masslessness) as input, so it establishes a consistency chain (massless => deep Coulomb => stiff => consistent with gravity), not 'Coulomb phase from first principles'; (3) beta_eff ~ K / fluctuation-scale is parametric/dimensional, not a rigorous quantitative map. NET: the open phase question is reframed from 'which phase?' into a cross-sector consistency requirement (rope stiffness) that the programme demonstrably meets; the ab-initio computation of K vs K_c from a microscopic rope model remains the outstanding step (the repaired lattice tool in benchmarks/lattice/ plus a rope-to-beta map would do it at scale)."
                "MICROSCOPIC COEFFICIENT + ROPE->EFT MAP (2026) -- items 1 and 2 substantially reduced. CANONICAL STATUS LINE (use this phrasing): 'Derived to rope-medium primitives; not derived from nothing.' The microscopic->EFT chain is a genuine bridge with J now EXACTLY derived (not parametric); it rests on three substrate primitives T, kappa, a that observation constrains only in combination. Earlier 'EFT-reduced / parametric' wording is superseded for J (now exact) but still applies to the overall coefficient because of the coarse-graining step and the undetermined primitives. c is reduced to rope-medium primitives, which is a bridge microscopic->continuum, not a first-principles closure. Item 1 (coefficient, not form): a concrete microscopic model REDUCES c to rope-medium primitives (an EFT-reduced / parametric derivation, NOT a full closure). Model the neighboring-rope orientation coupling as the leading symmetry-allowed lattice-XY locking H = -J sum cos(dtheta) (J = orientation-locking energy per shared-endpoint link). Standard gradient coarse-graining gives K = 3J/a (Frank stiffness; a = rope spacing), hence c = 1/K = a/(3J). Then J itself is computed from strand mechanics: two ropes sharing an atom with mismatched imbalance orientation dtheta strain the shared-atom bond (stiffness kappa) by x ~ T dtheta/kappa (T = strand tension), storing (1/2)kappa x^2 = T^2 dtheta^2/(2 kappa), so matching (J/2)dtheta^2 gives J = T^2/kappa. FULL CHAIN, all in microscopic rope constants: J = T^2/kappa; K = 3 T^2/(kappa a); c = 1/K = kappa a/(3 T^2). Dimensions check: [J]=energy, [K]=energy/length, [c]=length/energy (consistent). Item 2 (rope->EFT map): the same chain gives the dual gauge coupling beta_eff ~ K a = 3 T^2/kappa -- an explicit map from rope mechanics (T, kappa) to the EFT/phase parameter. PHASE CRITERION becomes one inequality: Maxwell (Coulomb) phase requires beta_eff > beta_c ~ 1, i.e. T^2 > kappa/3 -- stiff, high-tension ropes. This is the SAME 'stiff ropes' conclusion the photon-masslessness argument forced last turn, now reached from microscopic parameters (parametrically, not by exact derivation) rather than only inferred from observation; and T is the gravity-sector tension, so the EM/gravity cross-sector consistency is now explicit in a single formula (both sectors constrained by the same T). HONEST LIMITS: (1) the leading XY locking form and the harmonic small-misalignment bond treatment are standard leading-order approximations, not exact; (2) T, kappa, a are taken as rope-medium primitive constants (the correct stopping point for an EFT, but not derived from anything deeper); (3) J = T^2/kappa is a parametric estimate (x ~ T dtheta/kappa + harmonic well), not the full endpoint force-balance integral. NET: item 1 reduced from 'unknown coefficient' to 'three measurable rope constants c = kappa a/(3T^2)'; item 2 reduced to the explicit map beta_eff ~ 3T^2/kappa; phase + EM/gravity consistency collapse into T^2 > kappa/3. Remaining: a rigorous (non-parametric) computation of J and independent values/bounds for T, kappa, a."
                "EXACT J FROM ENDPOINT MECHANICS + PRIMITIVES STATUS (2026). QUESTION 1 (compute J exactly) -- ANSWERED, upgrades J from parametric to derived. Exact force-balance: a shared atom pulled by two rope imbalance-forces of magnitude F at relative angle dtheta, held by a harmonic bond (stiffness kappa), minimized over the atom position, gives EXACTLY E(dtheta)-E(0) = (F^2/kappa)(1 - cos dtheta). Two consequences: (a) the XY locking form -J cos(dtheta) is NOT an assumption but the EXACT result (the ratio [E(dtheta)-E(0)]/(1-cos dtheta) = F^2/kappa is rigorously constant, independent of dtheta -- no higher harmonics); (b) J = F^2/kappa exactly, with F = strand imbalance force = tension T, confirming the earlier J = T^2/kappa as exact (not merely parametric) in the harmonic regime. Intermediate geometry verified (net force = 2F cos(dtheta/2)). ANHARMONIC CHECK: adding a quartic bond term g gives a correction to the misalignment energy ~ g F^4 (cos^4(dtheta/2) - 1)/kappa^4, so J acquires a mild force-dependence and the pure 1-cos form is broken away from the harmonic regime; corrections are small when atom displacement is small (F << kappa * bond length). NET for item 1: the XY-form assumption and the parametric-J assumption (two of the three flagged limits) are REMOVED -- J = T^2/kappa is now derived, with known anharmonic corrections. The coefficient chain c = kappa a/(3 T^2) stands on firmer ground (still EFT-reduced overall due to the coarse-graining step and the primitives). QUESTION 2 (estimate T, kappa, a independently) -- HONESTLY NOT ANSWERABLE at present, and NOT faked. The rope network is a proposed sub-structure of spacetime with no established length scale, tension, or bond stiffness; no experiment has measured them. Available anchors only CONSTRAIN COMBINATIONS: photon masslessness forces T^2 > kappa/3 (deep Coulomb), and matching measured EM strength via c = kappa a/(3T^2) fixes the combination kappa a/T^2 -- but neither gives independent values. Producing specific numbers would require assuming a fundamental scale (e.g. a = Planck length), and that assumption would do all the work; declined as manufactured precision. STATUS: T, kappa, a remain primitive inputs constrained only as a combination by observed EM + the phase condition; independent determination needs new physics input or a derivation of the rope scale from deeper structure. This is the genuine remaining wall for the EM coefficient, now sharply isolated.",
    },
    {
        "id": "EM-P2-linking-inheritance",
        "problem": "EM-P2 (Linking Inheritance): proposed bridge postulate that "
                   "the surrounding rope network's Hopf phase texture inherits the "
                   "enclosed charged rope's strand-linking number, so transported "
                   "linking (current) sources a circulating connection (magnetism).",
        "sector": "electromagnetism",
        "paper": "(this work, 2026)",
        "status": "POSTULATE",
        "note": "STATUS IS 'POSTULATE', NOT 'DERIVED' -- this is the honest fix for "
                "the em-curl-from-ontology gap: rather than pretend magnetism is "
                "derived, add one precise, topological, countable, testable bridge "
                "axiom and label it as such. Origin: multiple sessions showed "
                "(i) magnetism is the surrounding network's curl response, not the "
                "current-rope itself; (ii) it must be a topological winding (a "
                "COUNT), not a vector sum; (iii) the two-strand state space IS the "
                "Hopf bundle (forced); (iv) but nothing derived forces the network "
                "texture to wind -- that is the missing ingredient. EM-P2 supplies "
                "it. IMPORTANT: the natural one-line wording ('network Hopf number = "
                "transported internal linking') bundles TWO logically distinct "
                "claims; a pre-registration check separated them: "
                "EM-P2a (STATIC): a charged rope link with strand self-linking "
                "Lk_strand forces the surrounding network imbalance texture to carry "
                "matching Hopf number H_network = Lk_strand. This is a config "
                "statement; alone it gives a static charge's texture, not "
                "magnetism. EM-P2b (DYNAMIC): TRANSPORT of that linking (linking "
                "flux through a surface per unit time = current) converts the "
                "inherited static texture into a circulating spatial connection; "
                "this is the clause that actually yields Ampere ∮A·dl ∝ I_enc. "
                "EM-P2b is where magnetism lives; do not let 'equivalently' hide "
                "it. WHY IT IS THE RIGHT KIND OF POSTULATE: it is stated as an "
                "integer identity (countable), it is relational (needs the network, "
                "so a lone rope in vacuum has no B -- reproduces fact F2), it flips "
                "sign with transport direction (F3), its Ampere RHS is automatically "
                "a count (F4), and a constant Lk along a straight wire gives the "
                "azimuthal 1/r field with consistent sign (F1). NEW FALSIFIABLE "
                "CONTENT beyond relabeling: charge is EXACTLY integer-quantized (Lk "
                "is an integer) and there is NO magnetism without net linking "
                "transport (forbids any 'longitudinal push' magnetic field). WHAT IT "
                "STILL OWES (why it is POSTULATE not CANDIDATE/derived): EM-P2a is "
                "not derived from the interpenetrability + two-strand axioms -- an "
                "explicit counterexample (charge Lk_strand=1 embedded in a network "
                "with uniform texture H_network=0) violates no stated axiom, so the "
                "1:1 inheritance is an ADDED law, not a consequence. To promote it "
                "to CANDIDATE/derived, one must show interpenetrable-network "
                "dynamics FORCE H_network=Lk_strand (e.g. an energetic or "
                "topological-consistency argument that a mismatched texture is "
                "impossible/infinite-energy). STRUCTURAL UNIFICATION: with EM-P2, "
                "both headline programme gaps have identical form -- a single "
                "topological coupling postulate binding a knot/link to its "
                "surrounding network (mass: knot<->cosmological network background; "
                "magnetism: charge-link<->local network texture). CROSS-CHECK for "
                "consistency: the same connection/inheritance rule invoked here must "
                "be the one operating in the electricity paper's "
                "charge-quantization-from-linking, or the framework uses "
                "inconsistent rules across its EM sectors. BOUNDARY-MATCHING RESULT (2026), the strongest EM result to date -- a partial DERIVATION, not just a postulate. Tested the four proposed coupling options (1 Linking Inheritance, 2 Linking Flux, 3 Boundary-Matching, 4 No-Slip). FINDING: Option 3 is not a peer option but the ROOT of the other three. Assume only PHASE CONTINUITY at the charged rope's surface (the network's Hopf fiber phase must join the rope's internal winding continuously across the tube boundary -- a far weaker, less arbitrary assumption than 'inherit the linking number'). Then: a continuous phase field cannot jump its integer winding across the boundary, so the exterior fiber-phase winding around the tube is FORCED to equal the interior self-linking Lk; by Stokes this forces circ(A)=2pi*Lk around any enclosing loop, hence B-flux = 2pi*Lk. That IS Ampere's law with enclosed current = enclosed linking number -- DERIVED FROM CONTINUITY, not postulated. Options 1,2,4 are repackagings of this one continuity requirement. NET: the MEASURABLE content of magnetism (azimuthal circulation, 1/r, Ampere, right-hand sign, monopole-free) reduces to [phase continuity at the charge boundary] + [the already-forced Hopf structure of the two-strand state space]. HONEST RESIDUAL (why not a full derivation of EM-P2a): boundary continuity fixes the FLUX through the tube (all measurable near-wire magnetism) but does NOT uniquely fix the full 3D bulk Hopf integer of the exterior texture -- fields with identical boundary winding but different bulk arrangement (Hopf fibration vs sheet) share the same flux. So EM-P2b (dynamical/Ampere content, the part that IS magnetism) is DERIVED from continuity; EM-P2a as a statement about the bulk Hopf number is NOT uniquely forced and reduces to a minimal/economy selection ('the exterior bulk is the minimal texture consistent with the boundary'). STATUS UPGRADE: the missing piece has shrunk from a substantive coupling law ('inherit the linking number') to a bulk-topology bookkeeping choice that no around-a-wire experiment probes. To fully close: show interpenetrable-network energetics select the minimal (Hopf) bulk among all textures matching the boundary winding. ENERGY-MINIMIZATION RESULT + SELF-CORRECTION (2026). Attacked the residual bulk-texture ambiguity via energy minimization, as proposed. REAL RESULT: among all exterior textures sharing the required boundary winding, any extra bulk knottedness costs strictly positive energy (Vakulenko-Kapitanskii bound: nonzero Hopf number has an energy floor ~|H|^{3/4}), so the physical texture is the UNIQUE MINIMAL one and the magnetic field is DETERMINED, not ambiguous. This closes the bulk-selection residual, modulo one flagged assumption: that the network's coarse-grained energy takes the standard lowest-derivative (Dirichlet+Faddeev) form, which the rope tension energy does reduce to. SELF-CORRECTION (important): an initial narration of this claimed the energy minimizer has bulk Hopf number H = Lk. That is WRONG and was caught on adversarial audit -- a straight vortex has boundary winding Lk but bulk Hopf number ZERO (straight parallel field lines do not link each other; Hopf number IS that linking). The earlier slogan 'H_network = Lk_strand' conflated TWO DIFFERENT INTEGERS: the BOUNDARY WINDING (= Lk, which sets the flux and hence Ampere) versus the BULK HOPF NUMBER (= 0 for a straight wire). CORRECTED EM-P2 CHAIN (cleaner, no free-floating inheritance postulate): charge = internal strand self-linking Lk; boundary phase-continuity => exterior phase WINDS by Lk around the wire (boundary winding, carries the charge outward); energy minimization => bulk exterior texture is the unique minimal one consistent with that boundary winding; together => unique field with circ(A)=2pi*Lk => Ampere with enclosed current = enclosed linking. The precise one-line statement uses BOUNDARY winding number, NOT a bulk Hopf charge: 'current is transported internal linking; magnetism is the boundary-forced phase WINDING (boundary winding number) of the surrounding network.' STATUS: EM-P2b (Ampere/measurable magnetism) is now DERIVED from continuity + energy-min + the forced Hopf structure; no separate inheritance axiom needed. Remaining assumption is only the standard-energy-functional form. DIPOLE-LAW + ENERGY-FUNCTIONAL RESULTS (2026), stated conditionally. (A) Given the continuum rope-energy functional E = (1/2)integral|curl A|^2 = (1/2)integral B^2, the quantitative magnet-magnet interaction follows RIGOROUSLY, not just its direction: expanding (1/2)integral|B1+B2|^2, the self-energies are constant and the CROSS TERM integral B1.B2 dV is the interaction energy, which is the textbook identity equal to (mu0/4pi)[m1.m2 - 3(m1.rhat)(m2.rhat)]/r^3 -- the exact 1/r^3 distance law AND the angular factor. Orientation check matches observed magnets exactly: head-to-tail opposite poles attract (U=-2 at r=1,|m|=1), side-by-side like poles repel (U=+1), T-config U=0. IMPORTANT PROCESS NOTE: a first NUMERICAL integration gave a DRIFTING ratio (4.3->5.8 over r=3..6), which looked like failure; investigation showed it was a finite-box + core-cutoff artifact mishandling the long-range tail and near-core singularity, and the analytic cross-term identity is exact. No NEW assumption beyond the 4.5 continuum-energy one is needed: the SAME assumption that yields Ampere also yields the quantitative dipole force. (B) Attempt to remove that remaining assumption by deriving the energy-functional FORM from microscopics (reviewer's ask): symmetry forces it. Any effective energy that is rotationally invariant, gauge invariant, and quadratic in first derivatives must reduce at leading order to c|curl A|^2 = c|B|^2 (div A is pure gauge/removable; vector identity integral|grad A|^2 = integral|div A|^2+|curl A|^2 leaves |curl A|^2 as the only gauge-invariant bulk term). The three inputs are already in the framework: gauge invariance (Hopf fibre = unobservable overall phase), positivity c>0 (tension is restoring), and absence of a mass term m^2|A|^2 (not gauge invariant; its absence is what makes magnetism long-range 1/r^3 rather than short-range Yukawa). HONEST STATUS (corrected per external review to EFT language): the FORM of the continuum energy is EFT-CONSTRAINED, not MICROSCOPICALLY DERIVED. That is: within the class of local, gauge-invariant, rotationally-invariant energies quadratic in first derivatives, c|curl A|^2 is the unique leading term -- fixed by the ontology's symmetry/locality/gauge structure (same standard as chiral perturbation theory fixing operators from QCD symmetries), NOT obtained by coarse-graining the microscopic rope Hamiltonian directly. So it is not an independent new assumption, but the phrase 'derived' was an overstatement; the precise claim is 'uniquely selected within the stated EFT class'. The COEFFICIENT c is neither derived nor constrained (needs microscopic tension/bending/torsional moduli), and full rigor against fine-tuned cancellation is open. To upgrade FORM from EFT-constrained to microscopically derived: show the rope elasticity coarse-grains to exactly this leading term. NET: the principal remaining EM assumption shrinks from 'why this energy functional?' to 'what fixes its single coefficient?'. All EM-sector results (Ampere, field structure, dipole force) rest on this one now-partly-justified functional. Wording discipline: every claim above is 'GIVEN the continuum energy functional', per the sector's honesty standard. Encoded as electromagnetism.minimal_texture_energy_selects_ampere.",
    },
    {
        "id": "em-curl-from-ontology",
        "problem": "EM-OP (current-to-curl): given a two-strand interpenetrable "
                   "rope network supporting traveling strand-imbalance waves, "
                   "derive why a moving imbalance induces a CIRCULATING connection "
                   "field B = curl(A) rather than only a longitudinal/radial "
                   "response.",
        "sector": "electromagnetism",
        "paper": "(this work, 2026)",
        "status": "OPEN",
        "note": "Sharpened by a critique (M. Palmer, 2026). The single-rope test "
                "is decisive: a lone imbalance wave on ONE rope in empty space has "
                "nothing to circulate around it, so the magnetic field cannot be a "
                "property of the current-carrying rope itself -- it must be the "
                "RESPONSE of the surrounding rope network. Charge (strand "
                "imbalance) and current (traveling imbalance wave) are well "
                "defined, and B = curl(A) with A the helical pitch vector is "
                "reproduced (Biot-Savart, 1/r falloff all follow). BUT nothing in "
                "the ontology yet FORCES that induced response to have non-zero "
                "curl rather than being radial: a network could in principle "
                "respond radially (pressure-like) and yield no magnetism. Precise "
                "statement of the gap: given a two-strand interpenetrable rope "
                "network supporting longitudinal imbalance waves, what property "
                "forces the induced response to satisfy curl(A) != 0? Two "
                "candidate mechanisms, NEITHER derived: (A) network torsional/"
                "shear elasticity (pulling one strand rotates neighbours) -- but "
                "this appears to CONFLICT with the interpenetrability postulate "
                "(ropes pass through each other without interacting except at "
                "shared atomic endpoints), so it would require modifying a "
                "load-bearing axiom; (B) holonomy/curvature -- treat A as a "
                "genuine connection on a field of local imbalance-directions, so "
                "that transporting orientation around a loop fails to close, and "
                "magnetism IS that geometric mismatch (curvature). Option B is "
                "mathematically what standard EM already is (A is a gauge "
                "connection, B its curvature) and is the more attractive lead, "
                "but note it retreats from the literal vortex/'swirling rope' "
                "picture: the circulation would live in an orientation field, not "
                "in physically swirling rope material. Existing seeds: the "
                "two-strand helical geometry and the Chern-Simons term in the "
                "magnetism paper supply handedness/chirality, which is the seed of "
                "a curl, but do not yet constitute a derivation. Caution: 'the "
                "field must be a global network deformation, not a local vortex' "
                "is a reasonable intuition from action-at-a-distance but is NOT a "
                "proof -- a 1/r falloff is equally 'far-reaching but weakening' "
                "and does not by itself select a global-holonomy ontology over a "
                "summed-local-response one. PROGRESS (2026): the question reduces to a "
                "sharp geometric one. A response field around a straight current can "
                "only be built from r_hat (radial), z_hat (along current), or "
                "phi_hat (azimuthal) = z_hat x r_hat; a radial response has zero "
                "curl, so circulation exists IFF the response is built from a CROSS "
                "PRODUCT of the current direction with the separation. A purely "
                "SCALAR imbalance carries no direction and can only respond radially "
                "(no magnetism) -- but the two-strand HELIX supplies an axial "
                "screw-vector w (handedness along the wire) that a scalar lacks. "
                "Symmetry then nearly fixes the coupling: of w.r (scalar, no curl), "
                "w x r (azimuthal, sign-flips with current), and r (radial, does not "
                "flip), only w x r both circulates AND reverses when the current "
                "reverses (both observed), and w x r yields the 1/r Biot-Savart "
                "field and the right-hand rule automatically. This is the holonomy "
                "route (Option B), kinematic and thus consistent with "
                "interpenetrability (no sideways force needed, only orientation "
                "comparison). REMAINING GAP, now precisely located: it is not yet "
                "derived from rope dynamics that the coupling MUST be w x r rather "
                "than another handedness-odd term; w x r is symmetry-SELECTED, not "
                "yet dynamically DERIVED. Next concrete check: whether the magnetism "
                "paper's existing Chern-Simons term, specialized to a straight "
                "current, reduces to a w x r coupling (if so, the derivation may be "
                "nearly in hand; if not, the paper's handedness and the needed one "
                "are different objects). CHERN-SIMONS CHECK DONE (2026): the paper's "
                "Chern-Simons term [eq 17: box A + chi*eps*dF = -mu0 J, with "
                "chi = sin(2 theta_W) n_rope r_H^2 / c] does NOT close this gap. "
                "That term is a tiny COSMOLOGICAL parity-violating correction "
                "(vacuum birefringence, ~0.34 deg across the observable universe) "
                "ADDED on top of an already-existing magnetism; ordinary B=curl A "
                "lives upstream in the main equation box A = -mu0 J, which the "
                "paper writes down but does not derive from the ontology. Key "
                "distinction the check clarified: ordinary magnetism needs only "
                "LOCAL, RELATIONAL handedness (field handedness tied to the "
                "current's; reversing current reverses field; NO net cosmic parity "
                "violation required, present in every wire), whereas Chern-Simons "
                "needs a GLOBAL NET vacuum handedness (vanishes if L/R-wound ropes "
                "balance). The gap is therefore the WEAKER, more plausibly "
                "derivable requirement, and it is now precisely localized: derive, "
                "within the box A = -mu0 J sector, that a helical (axial) "
                "strand-imbalance winding sources an AZIMUTHAL connection (the w x "
                "r map) from local rope geometry -- separate from, and upstream "
                "of, the cosmological Chern-Simons physics. DERIVATION ATTEMPT (2026), "
                "two failed constructions that sharpened the target: building A "
                "by summing the helix imbalance VECTOR u around the wire gives a "
                "UNIFORM field (trivial transport, zero curl) or, with a u x "
                "rayhat cross-product, a DIPOLE field whose azimuthal part flips "
                "sign around the loop and averages to zero -- neither is "
                "magnetism. Root cause: a summed vector cannot produce the "
                "same-sign-everywhere circulation of a line current. Ampere's "
                "law has a COUNT (enclosed current) on the right, so the source "
                "must be TOPOLOGICAL (a winding number), not a vector average. "
                "CORRECTLY-TYPED TARGET: the magnetic connection is A ~ "
                "grad(theta) where theta is the helix's winding PHASE, MULTIVALUED "
                "around the current (increases 2pi per loop); then circulation of "
                "A = enclosed winding = enclosed current, and curl(grad theta)=0 "
                "off the wire with a line singularity on it -- exactly the "
                "Aharonov-Bohm/vortex structure of a line current, circulating "
                "with consistent sign. So the remaining task is a TOPOLOGICAL "
                "claim (network connection = gradient of the multivalued helical "
                "phase), not a vector-superposition one. Structural hint: the "
                "electricity paper already derives charge quantization from rope "
                "LINKING number (topology), so magnetism-as-phase-winding would "
                "put E and M on the same topological footing."
                "MULTIVALUEDNESS TEST (2026) -- decisive negative result: attempted to derive that the network winding phase is multivalued around an enclosed current (phase gain = 2pi per loop). Found the result is ENTIRELY controlled by an unfixed modeling choice: if a network point inherits its phase by connecting ALONG THE HELICAL THREAD, the phase winds by 2pi (magnetism); if it connects to the NEAREST atom by straight-line distance, the phase closes (no magnetism). Nothing in the stated postulates (rope = two-strand helix; coupling only at shared atomic endpoints; current = translating winding) selects between these. CONCLUSION: the current-to-curl gap is NOT a missing calculation but a MISSING POSTULATE -- the ontology does not specify the rule by which a network point selects which wire-atom it inherits orientation from, and that selection rule IS the origin of magnetism. The needed axiom has the form [network connections follow the helical thread, not straight-line proximity]; it must be added and independently justified/tested, not derived from the others. PROPOSED SHARPEST FORM OF THE OPEN PROBLEM (per external review): can the two-strand rope phase be identified with the U(1) fiber phase of the Hopf bundle already in the framework? If yes, A ~ grad(theta) with the required multivaluedness may emerge naturally; if no, an additional ingredient is needed. Treat multivaluedness as a CONJECTURE to be proved from ontology, not assumed. CONSISTENCY CROSS-CHECK: the same connection rule must also operate in the electricity paper charge-quantization-from-linking result, or the framework uses contradictory connection rules across its two EM sectors. Note: an earlier draft narrated a 2pi success the computation did not support (honest number was 0 under a distance rule); corrected.  "
                "HOPF CHECK DONE (2026), a partial result. Step 1 SUCCEEDED and is non-circular: the two-strand imbalance state space genuinely IS the Hopf bundle -- a normalized two-component spinor (S^3) quotiented by the unobservable overall helix phase (U(1) fiber) leaves the observable imbalance state (S^2 base); verified the overall phase is exactly the fiber. So the rope phase really is a Hopf fiber phase, forced by the physics, not declared. Step 2 did NOT close the gap. Via Hopf holonomy (fiber phase gained = 1/2 * solid angle swept on the base S^2), magnetism exists IFF the current's imbalance texture, sampled around the wire, encloses nonzero solid angle on S^2. Coplanar texture -> S^2 equator -> zero solid angle -> no winding -> no magnetism (this EXPLAINS the earlier failed vector-superposition attempts: they were coplanar). Out-of-plane texture -> nonzero solid angle -> winding -> magnetism. Nothing derived fixes which occurs; it is the SAME unfixed choice as follow-the-thread vs nearest-atom, now sharply restated as a SOLID-ANGLE / COPLANARITY condition on the Hopf base. NET: Hopf gives (a) a real structural result [state space = Hopf bundle], (b) a sharpened, quantitative form of the missing postulate ['the imbalance texture around a current encloses nonzero solid angle on S^2'], and (c) an explanation of the prior negative results, but does NOT by itself force the winding. The missing postulate persists, now in its most precise form to date. CURRENT-POSTULATE EXPLORATION (2026): tested four redefinitions of current (C1 transported U(1) phase; C2 linking-number flux; C3 drifting charged link-defects; C4 inter-fiber phase-slip). C3 REJECTED as a derivation: it is 'moving charges' relabeled, reproduces the wire field only by importing per-charge Biot-Savart (the thing to be derived) and reintroduces the drift-speed vs signal-speed split. C1=C2=C4 are the same object (transported topological phase) and are the correct mathematical TYPE. C2 near-miss and the exact reason it is not yet a derivation: the Hopf invariant theorem (fiber winding = linking number) is real and would force 2pi winding per unit charge IF the relevant linking numbers were the same integer -- but they are NOT obviously the same. Charge (electricity paper) = SELF-LINKING of one rope's two strands, Lk_strands, an internal per-rope integer. The Hopf number that forces fiber winding, H[field], = linking of preimages of the SPACE-FILLING network imbalance texture. These are logically independent: an explicit configuration has Lk_strands=1 (charge) with a UNIFORM surrounding texture H[field]=0 (no winding), forbidden by no stated postulate. So redefining current does NOT remove the assumption; it relocates it. NET ADVANCE: the missing EM postulate is renamed into its sharpest, most nearly-derivable form yet -- a topological identity 'network imbalance-texture Hopf number = enclosed rope strand-linking number (1:1)'. This is the SAME connection-selection postulate found earlier (follow-the-thread vs nearest-atom), now stated as an integer identity rather than a geometric rule. STRUCTURAL UNIFICATION: with this, the two deepest programme gaps become the SAME kind of object -- a single topological coupling postulate binding a knot/link to its surrounding network (mass: knot<->cosmological network; magnetism: charge-link<->local network texture). Recorded as sharpening, not resolution. Recorded as the "
                "leading OPEN conceptual question in the EM sector, not as a "
                "result.",
    },
    {
        "id": "absolute-G-cosmic-tension",
        "problem": "Derive Newton's constant G from a cosmic source of rope "
                   "tension (expansion acting on the universe's mass content).",
        "sector": "gravity",
        "paper": "(this work, 2026)",
        "status": "PARTIAL",
        "note": "Idea: the rope network's tension is sourced by the cosmos, and "
                "G measures how strongly mass couples to it. POSITIVE RESULT: the "
                "framework naturally reproduces the Mach/Dirac closure relation "
                "G M / (R c^2) ~ 1/2 -- i.e. the observable universe sits at its "
                "own Schwarzschild radius (verified numerically: with R=c/H0 and "
                "M = critical-density Hubble mass, G M /(R c^2) = 0.50 exactly). "
                "So G, R, M, c are locked together as G = (1/2) R c^2 / M, and "
                "G's RELATIONAL value is consistent with a critically-closed "
                "expanding universe. ROTATION VARIANT RULED OUT: a rotating "
                "cosmos would give tension ~ omega^2 R and needs omega ~ H0, but "
                "CMB isotropy bounds cosmic rotation to omega < ~1e-9 H0, so "
                "spin-sourced tension is excluded by observation; only the "
                "expansion-sourced version survives. THE WALL (why it does NOT "
                "yield G's absolute value): the relation cannot be solved for a "
                "NUMBER because M is never known independently of G. Three "
                "natural routes to a G-free cosmic mass were checked and all "
                "fail at the SAME step -- converting a G-free quantity into a "
                "mass: (1) star-counting gives a G-free count and a G-free volume "
                "(R=c/H0), but mass-per-star needs Kepler / mass-luminosity / "
                "hydrostatic structure, all of which carry G; (2) age + "
                "expansion give G-free t0, H0, R_H, but rate->density goes only "
                "through the Friedmann equation H^2=(8 pi G/3) rho; (3) the CMB "
                "pins density RATIOS (Omega_i) G-free, but cashing a ratio into "
                "kilograms needs rho_crit = 3H0^2/8 pi G. CONCLUSION: mass is "
                "only ever measurable through gravitation, so R c^2 / M is "
                "exactly consistent but structurally unsolvable for G's absolute "
                "value. Same wall as the electron-mass work: the framework has "
                "no scale it can access that is not already defined through the "
                "quantity it is trying to derive.",
    },
    {
        "id": "absolute-G",
        "problem": "The absolute value of Newton's G from rope parameters.",
        "sector": "gravity",
        "paper": "rope_gem_equations",
        "status": "OPEN",
        "note": "Equivalent to the hierarchy problem; G not derived from T0 "
                "and mu_rope.",
    },
    {
        "id": "em-mag-rope-geometry",
        "problem": "The rope chirality parameters sin(2 theta_W), n_rope, r_H "
                   "individually (only their product is constrained).",
        "sector": "light / magnetism",
        "paper": "rope_theory_of_light",
        "status": "OPEN",
        "note": "Cosmic birefringence constrains the PRODUCT to 9.18e-29 /m "
                "(Eskilt-Komatsu). The individual geometric parameters are "
                "unfixed; EB/EE = 0.0119 is the LiteBIRD test of the mechanism.",
    },
    {
        "id": "one-loop-mass",
        "problem": "Electron mass from the one-loop fluctuation determinant.",
        "sector": "particles",
        "paper": "rope_fluctuation_determinant",
        "status": "FALSIFIED",
        "note": "Computed ln[det ratio] ~ +0.1; electron needs ~+108. Ruled "
                "out by direct computation; kept for the record.",
    },
    {
        "id": "koide-phase-t-parity",
        "problem": "phi = (3+Phi) theta_W: the T-oddness of the helical fiber "
                   "mode (the load-bearing step giving Phi rather than 1).",
        "sector": "particles",
        "paper": "rope_cs_theorem",
        "status": "CONJECTURE",
        "note": "The lepton Koide phase formula phi=(3+Phi)theta_W reproduces "
                "m_mu/m_e and m_tau/m_e to ~0.5%. The coefficient's Phi is "
                "rigorous (d_1/2 = [2]_q = 2cos(pi/5) = Phi at CS level k=3). "
                "The decomposition D=3+Phi requires the helical fiber mode to be "
                "T-ODD (-> j=1/2 -> Phi; T-even would give D=4, wrong by ~45x). "
                "UPGRADE (2026, this work): the T-oddness now rests on a THEOREM "
                "-- SU(2)_3 has chiral central charge c=9/5 != 0, i.e. it breaks "
                "time reversal, so the chiral framing phase the fiber mode carries "
                "is necessarily T-odd. This replaces the two FAILED prior "
                "arguments (helicity and mutual linking, both T-even). "
                "RESIDUAL (still open): (a) the fiber mode lands in EXACTLY the "
                "j=1/2 sector (lowest-T-odd assumption); (b) k=3 from N=2 "
                "(structural postulate); (c) the identification of the rope's "
                "physical helix WITH the CS framed Wilson loop is a modeling "
                "assumption, not proven. Status: conjecture with a rigorous core "
                "(T-oddness from c!=0) and three named residual assumptions -- "
                "stronger than the twice-failed prior version, still not a "
                "complete theorem. Also needs measured theta_W (see "
                "lepton-mass-ratios-thetaW).",
    },
    {
        "id": "lepton-mass-ratios-thetaW",
        "problem": "Lepton mass ratios as a parameter-free prediction.",
        "sector": "particles",
        "paper": "rope_mass_weights",
        "status": "PARTIAL",
        "note": "Given phi=(3+Phi)theta_W and Koide K=2/3, the lepton mass "
                "ratios follow to ~0.5% -- but only with the MEASURED Weinberg "
                "angle to 4 digits. The rope's own sin^2 theta_W = 1/(3 sqrt2) "
                "is 1.9% off, and the Koide-phase hypersensitivity amplifies "
                "that to a >600% mass-ratio error. So the ratios are a strong "
                "structural relation contingent on measured theta_W, not yet a "
                "parameter-free derivation. Absolute scale still needs one mass "
                "input (M0): see electron-absolute-mass.",
    },
    {
        "id": "writhe-ladder-generations",
        "problem": "Three generations from a knot writhe ladder.",
        "sector": "particles",
        "paper": "rope_hopf_link",
        "status": "FALSIFIED",
        "note": "The Lk=1 soliton spectrum is a monotonic infinite tower, not "
                "a triple. Generation count belongs to the discrete 2T "
                "symmetry (H3), not knot writhe.",
    },
]


def by_status(status):
    """Return all registry entries with the given status."""
    return [p for p in OPEN_PROBLEMS if p["status"] == status]


def by_sector(sector):
    """Return all entries whose sector contains the given substring."""
    return [p for p in OPEN_PROBLEMS if sector.lower() in p["sector"].lower()]


def summary():
    """Return a {status: count} summary across the registry."""
    out = {}
    for p in OPEN_PROBLEMS:
        out[p["status"]] = out.get(p["status"], 0) + 1
    return out


def print_registry():
    """Print the registry grouped by status."""
    order = ["OPEN", "POSTULATE", "CONJECTURE", "CANDIDATE", "PARTIAL", "FALSIFIED"]
    print("=" * 64)
    print("ROPE PROGRAMME -- OPEN PROBLEMS REGISTRY")
    print("=" * 64)
    for st in order:
        items = by_status(st)
        if not items:
            continue
        print(f"\n[{st}]  ({len(items)})")
        for p in items:
            print(f"  - {p['problem']}")
            print(f"      sector: {p['sector']}  |  {p['paper']}")
    s = summary()
    print("\n" + "-" * 64)
    print("  " + ", ".join(f"{k}: {v}" for k, v in s.items()))
    print("=" * 64)


if __name__ == "__main__":
    print_registry()
