# Known Limitations of the Rope Programme

A single place for every load-bearing caveat, so a reader never has to hunt for them.
This document is deliberately front-loaded: if any of these is a dealbreaker for you,
you have found it in under five minutes.

*Revised against the current registry.*
<!-- BEGIN GENERATED: corpus_stats -->
*600 registered claims, 558 code-backed and passing, 120 Derived, 38 registered Failed and kept.*
<!-- END GENERATED: corpus_stats -->


## THE PHOTON SECTOR AT HIGH ENERGY — UNRESOLVED (adopted openly, 2026-08-11)

**This is the programme's most serious open failure, and it is registered here
rather than left inside an unadjudicated fork. Author's decision (route (c),
FND-059/060 recommendation).**

**The statement.** Ultra-high-energy photons are routinely observed — LHAASO's
Galactic PeV gamma rays at ~1.4×10¹⁵ eV, arriving from sources distributed
across the sky. **The registered medium cannot host them.** The requirement is:

    transverse coherence sampled at ≤ ħc/E_obs = 1.41e-22 m

which is five orders below the mesh spacing and three below the *measured*
strand thickness. No registered length meets it.

**The correct diagnosis is ANISOTROPY, not a Nyquist cutoff (FND-061).** An
earlier reading — that light hits a short-wavelength cutoff at the mesh spacing
— was an overreach and is withdrawn. EM-RECON-025's registered light branch is
ω² = (T₀/μ)q², *continuum* in q with no Brillouin cutoff; the crossings couple
strands (gapping the optical branch) rather than sampling the wave. The
continuum direction is *along* a strand. Transverse coherence is still sampled
at the crossing spacing a, so the accessible wavevector region is a slab, and
PeV photons could propagate only within arcseconds of one of three strand axes
— an accessible solid-angle fraction of ~10⁻⁹. That contradicts **FND-REL-002
(Derived: the wave sector is forced to Lorentz-invariant, hence isotropic,
form)** and the observed all-sky source distribution independently.

**Four escapes were prosecuted and all four closed:**
- the loaded continuum (FND-058): removes the lattice, not the strands;
- the collective mode (FND-059): anisotropic, contradicts a Derived claim;
- any operator-shaped fix (FND-060): closed as a *class* — ω²(k) is periodic
  for arbitrary coupling range and Gershgorin bounds the disordered case, so
  E_max ~ ħc/a always. **The ceiling is discreteness, not the
  nearest-neighbour approximation.**
- tuning a length: blocked because both registered lengths are
  electron-anchored — d_c through ELEC-021's Λ = E_inf·d_c (GRV-094,
  fork-invariant) and a through the spent m_e calibration T₀a = 2.6065e-14 J.
  Driving a to the required value raises T₀ by 10⁵ and Σ_vac by 10¹⁵,
  destroying the Lorentz bound that currently clears at 6.1×. Shrinking d_c
  does not help at all — the constraint falls on the spacing *between* strands.

**Scope, stated precisely.** The transverse-wave mechanics are **not** refuted.
The collective mode exists, propagates, carries exactly two polarizations, and
supports the derived couplings; **every result at accessible energies stands
untouched.** The failure is at one end of one axis, by a stated number.

**What a fix must supply:** isotropy at high k. A finer constituent spacing
would do it; so might any structure that removes the preferred strand
directions at short wavelength. The remaining candidates each cost a new
primitive — strand substructure below the measured d_c (which must also explain
why the electron anchor cannot see it), or a second carrier for the PeV quanta
(owing two polarizations and a coupling). Neither is adopted.

**Process note, on the record.** This contradiction was registered in
FND-REL-004 with its escape left UNADJUDICATED across two claims while work
continued on top of it, and FND-MATTER-049's reopening tripwire is recorded as
having FIRED at 10¹¹× without halting further vacuum-facing work. That was a
process failure. The house rule added in consequence: **a registered
contradiction whose escape is unrun is a blocking item, not a footnote.**


## The vacuum stiffness tower (conditional, floors without ceiling)

Everything vacuum-facing above Σ_eff — Σ_vac, the moved M-point, the mesh pair
(a, T₀) — hangs on **FND-037's quadratic-nonlinearity form (Conjecture)** at the
FND-040 floors (κ_pack ≥ 50 / 250). One resolved measurement of long-distance
Casimir-scaling violations confronts the whole tower; the current lattice bound
(Bali 2000, ≤5%) gives only κ_pack ≥ 12.5 (FND-047), so the floors are held by
Conjecture, not data. There is **no ceiling** (the old 1–100 window retired as
grammar, FND-042).

- **The mesoscopic source length g = l_q/a ≈ 83–108 is UNEXPLAINED.** It is the
  corpus's single remaining mesoscopic unknown (five former questions collapse
  to it, FND-044). Its best-shaped candidate mechanism — the defect-log energy
  budget — is **excluded structurally** (FND-045, Failed-and-kept: the
  electron's own rest energy exhausts its logarithm at ~7 cells; a rescue must
  derive a budget of 2.2–3.2 m_ec² blind).
- **The softening mechanism is claimed N-UNIVERSAL (FND-050, author's grant,
  2026-08-11) — and the corpus therefore owes a computation it has not done.**
  The derivations (FND-037/040) contain no reference to the number of colours,
  so the corpus declines to assert an N-dependence its own derivations do not
  exhibit. The price is real and chosen: k-strings are bundles of k unit
  windings, so the SU(N≥4) sine-law data measures inter-tube binding, and the
  framework must compute the bundle-binding relation from the derived −1/8 and
  confront its (N, k) form against sine-vs-Casimir. If that computation lands
  against the data, this grant is what makes it a falsification of the corpus
  rather than someone else's problem. Retreating to the SU(3) scope afterwards
  would be bar-shopping and is refused in advance. Running start, not evidence:
  the qualitative bundle prediction (σ_k < kσ_1) holds on every dataset row.
  Calibrations (Σ_eff and everything conditional on it) remain SU(3)-anchored.

## The quantum boundary (the deepest limitation)

The framework is classical, but it is **not** a pure configuration-counting
scheme: its native arithmetic is the Hopf/spinor (quaternion) machinery, with
modes, winding, and geometric structure, and it is that non-counting structure
that derives the Tsirelson bound and demonstrates a Bell violation (below). What
*is* limited is a specific **local counting reading** of measurement, which Bell's
theorem caps at CHSH = 2 no matter how it is built (QB-006). With that distinction
kept straight, several quantum facts are **adopted, not derived**, or **open**:

- **The Schrodinger equation is ADOPTED**, not derived. It is used as the effective
  continuum description of network modes; hbar, the electron mass, and hence the
  absolute atomic scale (Bohr radius, Rydberg, every eV in the chemistry paper) are
  inherited as inputs, not predicted. (Chemistry paper, Section 3.1a.)
- **The Born rule is OPEN -- now as a three-part decomposition (QB-007/008).** Dot
  indivisibility is derived from integer topology; the single-site |psi|^2 rate law is
  derived-in-structure (threshold nucleation, weak-field limit); the irreducible core is
  spacelike winner-take-all (classical models pinned at g2 >= 1 vs measured ~0.18), whose
  only escape is cornered to instantaneous constraint propagation in the mesh frame
  (K_L/K_T >= 1.9e8 demanded; Conjecture -- demonstrated SUFFICIENT for g2 ~ 0 in a
  conservation toy, QB-009, with CHSH still failing: sufficiency, not truth). Amplitude interference remains unproduced by a
  counting model (QB-005); a documented boundary, sharpened, not solved.
- **Quantum entanglement: the ceiling is DERIVED and a Bell violation is DEMONSTRATED;
  the honest gap is narrower than "retired."** The framework derives the Tsirelson bound
  2√2 as a theorem, with the corpus-native singlet saturating it (QB-019/020, Derived), and
  a complete Bell experiment run from a nucleated pair gives a genuine violation (CHSH =
  2.039 to 2.234 above the classical bound of 2; QB-030/031, Modeled). What a
  configuration-counting model provably **cannot** do on its own is produce those
  correlations from ropes-in-physical-space alone (QB-003 Failed; QB-005 negative; the
  identical-race benchmark gives S = 1.42 in physical space vs 2.83 only when the
  configuration-space guidance object is imported by hand). The residual gap is therefore
  precise: the guidance flow across the wall is **added, not yet derived from the ropes** --
  the same status pilot-wave (Bohmian) theories give it. A future rope-native derivation is
  not claimed impossible; none is claimed to exist.
- **Pauli exclusion is INCOMPLETE** (Conjecture-level spin-mode-saturation proposal); the
  contact core supplies a mechanical steric repulsion that partially routes around it.
- **The nuclear binding table has a real but unexplained residual.** The classical
  model now predicts atomic masses across the table (light nuclei through U-238), with He-4 used as
  the single calibration constant rather than standing as a failure, and the heavy-table
  gap has been narrowed to about a percent with derived classical physics. What remains
  open is the residual itself: it is a coordination-dependent term of roughly the right
  magnitude whose origin is not yet derived. Notably, the sector's long-inherited
  explanation -- that the residual is a kinetic/zero-point (hbar) omission -- was computed
  and **refuted** (NUC-010, Failed and kept: the derived Fermi-gas term makes the model
  2.25x worse; NUC-023 confirmed this collectively). The residual is real and does *not*
  scale like kinetic energy; naming its mechanism is the open problem.

## Gravity

- **Frame dragging: structure derived, magnitude not yet derivable.** The twist sector
  supplies a gravitomagnetic mode with the exact Lense-Thirring form — a locking mass term
  is symmetry-forbidden (kappa = 0 by Goldstone, GRV-067), the mode is massless for any
  modulus (GRV-068), and the far field has the required 1/r² falloff and dipole angular
  structure with no free parameter (GRV-066). What is **not** yet available is the amplitude:
  the registered strand action lacks a matter-to-rotation coupling and a metric shift-slot,
  so the sector "can predict neither 37.2 mas/yr nor its absence and should claim neither"
  (GRV-071). The source-audit failure that opened this line is kept (GRV-059); the work since
  converted it from "the sector is missing" to "the form is derived, the magnitude is the
  open frontier." A limitation of degree (no number yet), not of kind (the structure matches).
- **Strong-field / black holes are a Modeled extrapolation, not a proof.** The horizon
  mechanism, the derived Newton constant, and the reconnection thermodynamics (GRV-034..095)
  are a controlled expansion certified as such (GRV-048), but every result there is Modeled
  or conditional, not Derived.

## Electromagnetism / optics

- **The PVLAS vacuum-birefringence identification is EXCLUDED** by roughly 570x; absorbed
  by raising a bound on an input (SIGMA), with the surviving falsifiable content a
  sign/ratio discriminator against QED. One rescue postulate was refused on principle.
- **London dispersion is NOT derived** (zero-point, hbar-scaling; quantum-boundary class).


## Gauge-holonomy branch closure

- **The physical Aharonov--Bohm branch is CLOSED under the current framework.** The numerical instrument is validated, but no undriven rope mechanism supplies a nontrivial target phase. Static handedness supplies orientation only; screw current requires prescribed rotation; the continuity and Maxwell-like models require an inserted pump/current. More sharply, the only derived topological phase is `2 pi N`, which is spectrally identical to zero in the validated AB spectrum. This is registered as `INTEGER_WINDING_HOLONOMY_SPECTRALLY_TRIVIAL` / `NO_UNDRIVEN_NONTRIVIAL_PERSISTENT_HOLONOMY` (ROPE-SOURCE-AUDIT-002). Any fractional coupling, offset flux, persistent compact phase, or explicit linking action would be a new postulate and must be labeled accordingly.

## Particle sector

- **Lepton mass ratios (Koide) and the Weinberg angle are CONJECTURES** -- numerical
  coincidences (~1%) held pending a derivation-or-demotion, not claimed as results.
- **The absolute atomic scale is CLOSED BY MEASUREMENT, not derived (FND-MATTER-003).**
  Both originally-missing inputs are now determined -- the rope count N by the coverage
  threshold (FND-MATTER-004) and the absolute mesh scale a fixed by measurement at the
  M-point (a = 6.0e-17 m, FND-MATTER-044), exactly as the irreducibility theorem said it
  must be (FND-MATTER-005). The scale is therefore pinned but measurement-fixed, not derived
  from more primitive quantities; a remains a fundamental constant of the framework.

## Chemistry (open edges within a strong sector)

- **Metallic bonding** cohesion is a consistent ~2.8x low (order-right, declared shortfall).
- **The hydrogen-bond F/O ordering is a registered MISS**, reclassified as short-range
  (overlap/Pauli) structure after three knob-free correction attempts failed to flip it.
- **Reaction barriers** are bracketed, not pinned: the coherence fraction that would close
  the bracket to a point prediction is underived.
- **Hybridization mixing coefficients are ADOPTED**, not derived (the mechanics-first layer
  gives the 90-degree fixed point; the sp3 opening is the adopted layer).

## Methodological limitations

- This corpus establishes **numerical reproducibility and internal consistency, not physical
  truth.** Agreement with data in the derived sectors demonstrates the mechanical account's
  reach; in sectors where quantum mechanics predicts the same numbers, agreement does not
  discriminate rope from QM (labeled "consistency-tier" throughout).
- The generator (AI-derived) and much of the verification grew up in the same process; the
  registered highest-priority mitigation is external adversarial review.

## The complete failed-and-kept ledger

<!-- BEGIN GENERATED: corpus_stats -->
*600 registered claims, 558 code-backed and passing, 120 Derived, 38 registered Failed and kept.*
<!-- END GENERATED: corpus_stats -->

Every one of those Failed claims is kept on permanent display below with its lesson,
grouped by sector. (If the count above ever exceeds the entries listed, the ledger has
fallen behind the registry — run `tools/sync_doc_facts.py --check`.)

**Electromagnetism / cosmology**
- **EM-011**: cosmological alpha-variation falsifies the strong (local density-tracking) form of the rope-density hypothesis for the EM coupling.

**Gravity**
- **GRV-009**: per-strand STRAIN conditioning gives the wrong sign of spatial curvature (Cassini-excluded).
- **GRV-010**: mode-bath conditioning gives γ = -1/2 universally (Cassini-dead).
- **GRV-059**: the stationary mass-current source-and-form audit returned nothing (no matter-to-rotation coupling in the action). Kept as the failure that opened the frame-dragging line; the twist route since derived the *form* of Lense-Thirring though not yet its magnitude (see the gravity section above).

**Particle / lepton sector**
- **PM-002**: lepton ratios with the model's own Weinberg angle.
- **PM-004**: the lepton mass spectrum does not fall out of the knot/soliton excitation physics without tuning; lepton masses are irreducible inputs.

**Nuclear**
- **NUC-010**: the kinetic/zero-point diagnosis is refuted -- the named omission makes the model 2.25x worse when computed.
- **NUCQ-003**: the structural strand count is derived, the escape closes, and the mesoscopic-hbar picture is refuted.

**Quantum boundary**
- **QB-003**: the *local configuration-counting* reading of measurement cannot reproduce CHSH — theorem-forced, since Bell caps any local mechanism at 2 (QB-006). Kept as a finding; the framework's non-local Hopf/spinor structure later derives Tsirelson (QB-020) and demonstrates a violation (QB-030). Not a statement that the framework is a mere counting scheme.
- **QB-004**: one-loop fluctuation mass mechanism (log-det ≈ -1.29 vs electron ≈ 108).
- **THM-006**: the layer-separation theorem -- the programme's failures concentrate at the dynamical (Layer III) frontier.

**Electron-structure search (the ELEC candidate chain)**
- **ELEC-001**: stable localised electron-candidate search, first gate -- attractor expands past the locked localization window.
- **ELEC-003**: resolution/stability campaign -- misses the locked Fourier-basis convergence bar.
- **ELEC-004A**: linear-stability gate -- residual gradient too large to classify the Hessian.
- **ELEC-004A-R**: deterministic stationarity repair -- the first step leaves the linked basin.
- **ELEC-006**: extended topology-preserving variation -- certified descent without constrained stationarity.
- **ELEC-007**: augmented-Lagrangian linked-sector search -- same, no stationarity.
- **ELEC-008**: adaptive direct-spline representation does not establish constrained stationarity.
- **ELEC-009**: variational remeshing fails the strict numerical-consistency gate.

**Atomic-shell mode search (the ROPE-MODE chain)**
- **ROPE-MODE-001**: certified rope modes are ordinary closed-string harmonics (shell gate fails).
- **ROPE-MODE-002**: central-field standing waves do not form robust atomic orbital multiplets.
- **ROPE-MODE-003**: a surrounding 3-D field yields angular families but fails the localization gate.
- **ROPE-MODE-005**: the resolved-tube spectrum is a single level -- the shell question is premature at the certified geometry.

**Strand kinetics / holonomy**
- **FND-STRAND-017**: the phase-winding picture is killed at its own first checkpoint -- the weave is an internally mixing thermal network.
- **ROPE-SOURCE-AUDIT-002**: undriven closed-rope circulation sources no nontrivial observable holonomy; integer winding is AB-spectrally trivial.

## The one fence (cross-sector synthesis)

The four hardest residuals above -- the gravitomagnetic (frame-dragging) magnitude, the
nuclear shell/pairing tier, light-isotope masses, and dispersion forces -- were registered
independently, in four sectors, over months. (Weak-field gravity is not among them: the metric, γ = 1, the exact
1.751″ deflection, and the SPARC relation are all derived; the open gravity item is the
frame-dragging *magnitude*, not the sector. And the nuclear residual is now narrow: the
classical semi-empirical mass formula is derived across all five terms, leaving only the
genuinely quantum shell/pairing structure at a few MeV RMS -- not the classical mass table,
which is closed.) Their terminal diagnoses name the same missing
layer: quantum zero-point / shell structure (FND-BOUND-001). The classical programme's boundary is one boundary. It is located from four
directions and crossed from none; constructing the quantum layer requires hbar (underived)
and the absolute mesh scale (measurement-fixed at the M-point, not derived -- FND-MATTER-003/044).
A standing research directive for
crossing this fence -- with pre-committed acceptance tests and the discipline required --
is maintained at docs/technical/FUTURE_MODEL_PROMPT_one_fence.md.
