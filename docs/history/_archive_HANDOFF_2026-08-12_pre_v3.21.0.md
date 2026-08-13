# HANDOFF — Rope Framework, next session

*Written 2026-08-11 at the close of the v3.20.0/BET arc; touched 2026-08-12 (annotation repair, EM-RECON-018 re-solve). Everything a fresh
session needs, in reading order. The corpus zip is
`rope-framework-github.zip`; unpack it and work in `rope/`.*

---

## 0. Ninety-second orientation

The Rope Framework is Mark Palmer's object-based physics programme
(GitHub: mrpalmer100/rope-framework), building physics from mechanical
strands rather than fields. It runs as a registry of claims
(`claims.yaml`, 592 registered) each carrying a status grade, a
benchmark, and its provenance. **The registry is the authority.**

**House discipline, non-negotiable:**
- Bars locked in `analysis/*_LOCKED.md` BEFORE computing. Always.
- Failures register as `Failed-and-kept`, never rescued, never quietly
  re-scoped. Bar-shopping is refused by rule.
- No post-hoc refitting; no O(1) rescues argued after a miss.
- Every session ends with: claim registered via `tools/add_claim.py`,
  annotations appended to affected claims, CHANGELOG entry,
  `tools/verify_corpus.py --quick`, re-zip, `present_files`.
- Em dashes are forbidden in file content (use `--`).
- Premise adoptions ("grants") are MARK'S CALL, not Claude's. Name the
  grant, price it, and leave it for him.

**GEOMETRIC RESEMBLANCE IS NOT PHYSICAL IDENTIFICATION (added 2026-08-11).**
Before identifying a newly derived geometric structure with an
already-derived observable, require a DEPENDENCY PATH from one to the
other. A structure that merely looks like the observable is not evidence.
Worked example, kept because it cost a full arc: ELEC-090/091 derived a
core axis with two poles and two orientations -- visually a perfect match
for spin. ELEC-099 then measured the weave to pin that axis at ordinary
strength, and ELEC-100's dependency trace showed the corpus's actual
spin results (QB-020/025/026/031, GRV-045) predate the axis by many
sessions and never referenced it. The resemblance was total and the
identification was empty.

- **NEW, learned expensively this arc (FND-056):** "no derivation
  mentions X, so none is disturbed" is an INVALID audit argument. A
  derivation need not mention a degree of freedom to depend on HOW MANY
  there are. Counting is the channel, and this corpus kills on counts.

---

## 1. State of the corpus

**Release:** v3.20.8 (the full 2026-08-12 arc: re-solve, NUN/SAMEKH/adoption, AYIN/PE/TSADE, CI repair) atop the BET arc (FND-063..070).
**Registry:** 628 claims -- 120 Derived, 455 Modeled, 38 Failed-and-kept,
7 Open, 4 Conjecture, 4 EFT-constrained.
(Counts regenerate from claims.yaml -- trust `tools/sync_doc_facts.py`.)

**Read these first, in order:**
1. Section 2a below -- the BET arc, because four of its eight claims
   correct or retract earlier ones and two correct each other.
2. `KNOWN_LIMITATIONS.md`.
3. `docs/history/RELEASE_NOTES_v3.20.0.md`.
4. `docs/STATE_OF_THE_PROGRAMME.md`.

---

## 2a. THE BET ARC (FND-063..070, 2026-08-11) -- READ BEFORE REUSING ANY c4, w, OR f_c NUMBER

Eight commissions on the quartic coefficient, the constituent width, and
Rank-1 g. **No new number was produced.** What it produced is a cleaner
registry and one exact result. Net ledger:

**STANDS:**
- **FND-063/064** -- the master functional
  `c4_eff = [k(K_c + f k)/(K_c + k) - T0]/8`, with EM-RECON-009's
  `(k-T0)/8` at f -> 1 and FND-040's `-T0/8` at f -> 0, K_c -> 0, both
  EXACT. The localised sign condition and EM-RECON-013's core-survival
  condition are THE SAME INEQUALITY. This is the arc's one durable result.
- **FND-065** -- FND-029's nuclear import excludes the eta-satisfying
  region by 3.3 orders, so FND-MATTER-063's zero-point consistency
  problem is unconditional given the import. The sign itself is OPEN.
- **FND-066** -- w carries THREE objects in TWO roles (vacuum-mesh strand
  vs flux-tube constituent). "Determine w" is not yet well-posed.
- **FND-068** -- f_c is AREAL, so EM-RECON-018's coverage relation is
  `pi w^2/(4a^2) = f_c` and **w/a = 0.6272, not 0.3621**.
  The owed re-solve is EXECUTED (EM-RECON-030, 2026-08-12): band robust at
  [0.395, 0.460], m_b < 63-73 stands, W1 scales by sqrt(3). Quarantine
  LIFTED; quote with EM-RECON-030's provenance. Its open edge: reading B's
  sub-touching standoff (0.797 contact ranges).
- **FND-070 Q1** -- GRV-035's percolation (bond survival, p_c = 0.2488)
  is NOT FND-MATTER-038's coverage percolation (areal, f_c = 0.309).

**RETRACTED WITHIN THE ARC:**
- FND-063's acquisition target (K_c is derived in form -- EM-RECON-017).
- FND-067's route identity (an artefact of the 3 pi conflation).
- **FND-069 in full except its C6 check** -- the K_c chain places
  **MATTER** at the coverage threshold, NOT the vacuum. There is no
  "critical vacuum" commitment; correlation-length mechanisms for g are
  LIVE candidates again.

**g IS EXACTLY WHERE FND-051 LEFT IT.** SCALE-001's ledger is 3 evaluable
/ 5 UNDERSPECIFIED, UNDERSPECIFIED-DOMINANT stands. C6's retirement is
narrowed to a single ground (amplitude circularity).

### The arc's operating lesson, which is the real handoff

**Four of the arc's errors share one root: proposing on a PARAPHRASE or a
FACE VALUE instead of opening the cited claim verbatim.** The bars caught
every one, but three of the four were caught a commission late. Specific
vectors found:
- EM-RECON-013's superseded face value for K_c (annotation not read).
- FND-029 described as undischarged when it had executed.
- ELEC-048's paraphrase attaching the symbol `f_c` to GRV-035's
  bond-collapse statement -- read through without opening GRV-035.

**STANDING RULE ADDED: before writing a law, a bar, or a next-order that
leans on a claim, OPEN THAT CLAIM AND READ ITS TITLE, NOTE, AND EVERY
BRACKETED ANNOTATION VERBATIM.** Quoting a neighbour's summary of a claim
is not reading the claim. This is HANDOFF section 6's stale-value
tripwire generalised from numbers to statements.

## 2b. THE EM DICTIONARY IS CLOSED (do not re-open its debts)

EM-016's four registered debts are ALL discharged and the claim is graded
Derived (EM-022, author's act, 2026-08-11):
- (iv) uniqueness -> EM-017; (iii) phi's channel -> EM-018;
  (ii) the inertial term's form -> EM-019; (i) SIGMA -> EM-021.
THREE CONDITIONALITIES travel with the grade and must not be dropped when
quoting it: SIGMA inherits the kappa_pack floor spread held by FND-037's
Conjecture-grade form (6.0e36-9.0e37 J/m^3); EM-019's coefficient is
matched to EM-RECON-025, not independently derived; EM-019's uniqueness
assumes locality.
FALSIFIER ARMED: if the floors move materially or FND-037's form is
refuted, EM-016's grade RETURNS TO ADJUDICATION. FND-037 is annotated
accordingly -- work there is now grade-load-bearing.


## 2c. THE ELECTRON CORE ARC (closed 2026-08-11 -- do not reopen for interpretation)

Thirteen commissions, ELEC-088 through ELEC-100. Reached a natural
stopping point; an external reviewer advised against ELEC-101 and that
advice is recorded as binding for the next session.

**What was derived and stands:**
- the core is HOLLOW with a hard boundary at r0 -- and ELEC-090 explained
  it: the first integral reads r^2 sin(theta) = C, so the boundary is
  simply where the strand tilt reaches 90 degrees. KINEMATIC, hence
  independent of every material parameter.
- strands reach r0 TANGENT; hairy-ball forces zeros of total index 2, so
  the core cannot be isotropic (ELEC-090).
- matching the exterior winding fixes the boundary field as AZIMUTHAL
  with exactly two polar defects, independently reproducing index 2
  (ELEC-091).
- the weave's point group is O_h, so pinning is allowed at order 4 in
  K(n) = sum_i n_i^4 - 3/5 (ELEC-096).
- the pinning is MEASURED under PBC on the registered engine: anisotropy
  fraction 0.21, 166x the noise floor, R^2 = 0.71 on the pre-fixed
  harmonic, null and rotation controls passed (ELEC-099).

**What was retired:** the suggestion that the axis's two orientations are
the electron's two spin states (ELEC-100). Spin lives in GRV-020's
internal azimuth and the Hopf/Pauli-quaternion machinery, and the
dependency trace shows it never touched the axis.

**Do NOT charter:** tumbling (violates source-before-instrument -- six
things unregistered), or a campaign to decide what the axis represents.
Three possibilities are recorded on ELEC-091 as possibilities.

**Genuine open work in this sector, if returning:** ELEC-088's
unadjudicated tension between the field-winding electron (GRV-020,
Derived) and the clasp-and-loop geometry (ELEC-041/042, Modeled).
ELEC-090's non-isotropy requirement made the clasp a better-motivated
candidate for the hollow's interior than it was.

## 3. THE PHOTON SECTOR -- read this before touching the wave sector

**The one inequality:**

    a <= hbar c / E_obs = 1.41e-22 m

Five orders below the mesh spacing, three below the measured strand
thickness. The observed 1.4 PeV Galactic photons (LHAASO) cannot exist
on the registered mesh.

**SCOPE CORRECTION (FND-061), read before anything else in this section:**
FND-060 bounded the nearest-neighbour LATTICE displacement field.
EM-RECON-025's registered LIGHT branch is omega^2 = (T0/mu) q^2 --
continuum in q, non-periodic, NO Brillouin cutoff; crossings couple
(gapping the optical branch) rather than sample. So the problem is NOT a
Nyquist cutoff on light. **It is ANISOTROPY**: the continuum direction
is along a strand, transverse coherence is still sampled at a, and the
resulting slab is what FND-059 closed on FND-REL-002's Derived isotropy.
The demand is therefore **"supply isotropy at high k"** -- transverse
coherence sampled at <= 1.41e-22 m, a constraint on the spacing BETWEEN
strands, not on any length along one. Wider target than a bare
substructure length.

**What is CLOSED, and do not re-attempt without reading the claim:**
- The loaded-continuum escape (FND-058): removes the lattice, not the
  strands.
- The collective-mode escape (FND-059): anisotropic, contradicts a
  Derived claim.
- **Any operator-shaped fix (FND-060): closed as a CLASS.**
  omega^2(k) is periodic with period 2pi/a for arbitrary coupling range;
  Gershgorin bounds the disordered case; E_max ~ hbar c/a always. The
  ceiling is DISCRETENESS, not the nearest-neighbour approximation.
  **Any fix must change a LENGTH; no fix can change the dynamics.**

**Why no length is free:** both registered lengths are electron-anchored
by different routes -- d_c through ELEC-021's Lambda = E_inf d_c
(GRV-094, fork-invariant) and a through the spent m_e calibration
T0 a = 2.6065e-14 J. Driving a to 1.41e-22 m raises T0 by 1e5 and
Sigma_vac by 1e15, destroying the Lorentz bound that currently clears at
6.1x. Shrinking d_c does NOT help at all -- the ceiling tracks a.

**What remains (author's to name, none adopted):**
1. Strand substructure 8.3 orders below the measured d_c -- a new
   primitive that must also explain why the electron anchor cannot see it.
2. A second carrier: the PeV quanta are not collective mesh modes.
   Owes two polarizations and a coupling.
3. Route (c): ADOPTED 2026-08-11 (FND-062, author's decision). The
   limitation is now registered openly in KNOWN_LIMITATIONS. This does
   NOT concede the framework is wrong at high energy and does NOT
   abandon the fix -- candidates 1 and 2 remain live and unpriced by
   preference.

**Scope, so no session over-reads:** the transverse-wave mechanics are
NOT refuted. The collective mode exists, propagates, carries two
polarizations and the derived couplings, and every result at accessible
energies stands. The failure is one end of one axis, by a stated number.

---

## 4. ON THE AUTHOR'S DESK (nothing adopted; standing rule)

1. **(DECIDED 2026-08-11, FND-062: route (c) adopted -- limitation
   disclosed.)** The wave sector's remaining work is unblocked to the
   extent that the corpus now builds openly on a stated limitation
   rather than on an unadjudicated fork.
2. **GRANT-CANDIDATE-ROT** (GRV-103): tau = beta_J J, matter's angular
   momentum as strand twist. Buys frame-dragging's absent source by
   elimination; beta_J's derivation target is GRV-073's gamma. Exposure:
   GRV-057's ladder (5.2 / 20 / ~500 sigma). Refusing makes GRV-059's
   Failed permanent -- the audit certifies no derivation exists to wait
   for.
3. **GRANT-N2-GAP** (FND-056; live again after FND-058 unpinned it): a
   confinement-like gap on the label sector. Closes four disturbances
   including the light carrier's state count.
4. **The kappa rename**, queued since PRED-003-ETA: three objects wear
   the name (locking modulus [J/m^2], the gravity sector's surface
   gravity, ELEC-021's Coulomb coefficient [J m]). Registry-wide sweep
   owed.
5. **(DECIDED 2026-08-12, NUC-030: GRANT-CANDIDATE-COH adopted as the
   R4 channel separation.)** Diagonal cost -> asymmetry (surface -1/3),
   off-diagonal hybridization -> pairing (-1/2). Conditional on QGATE
   quantization and the reconnection rate; FALSIFIER ARMED at
   v0 = 16.97 MeV -- any future reconnection-rate or vertex derivation
   must hit it or the adoption returns to adjudication. Surviving open
   items in the sector: asymmetry shape (state counting), asymmetry
   magnitude coefficient, v0's derivation.
6. **ZENODO_RELEASE_NOTES.md** still frozen at the v2.2.1 era.

---

## 5. The ranked queue

1. **The mesoscopic scale g (FND-044)** -- RANK 1.
   **PROTOCOL RULE, carried from the electron-axis arc and binding on
   the next g commission: do NOT search for something that numerically
   resembles g. Require a DEPENDENCY PATH from an existing collective
   mechanism to the mesoscopic scale BEFORE looking at the target
   value.** The sealed-target machinery (tools/scale001_seal.py) already
   prevents tuning TO the number; this rule prevents the subtler failure
   of proposing a mechanism BECAUSE it lands near the number. It
   combines source-before-instrument with the resemblance rule in
   section 0.
   The corpus's oldest
   load-bearing residual, five former questions collapsed into one
   number (g = l_q/a ~ 82.6-108.0), and SCALE-001 (FND-051) found five
   of eight collective channels cannot even be POSED in registered
   inputs. An external reviewer's advice at the close of the electron
   arc: return here rather than asking the newly discovered axis to
   explain something else. Rank-1.
2. **(EXECUTED 2026-08-12, NUC-028.)** The NUC-021 1/sqrt(A) dilution ran
   blind: no registered channel produces -1/2; only a non-local coherent
   amplitude does (root-extensivity is not a geometric exponent -- the
   boundary theorem now covers scale as well as shape). Priced, ABSORBED
   in the smooth surface (staggering is the sole instrument), and
   converted to GRANT-CANDIDATE-COH on the author's desk. One edge: the
   asymmetry misses (A^-0.37 measured) may dilute by the surface channel
   instead -- NUC-027's three-way consolidation is a hypothesis.
2. **THE ONE-MEDIUM PROSECUTION -- the registry's decisive question
   (FND-073, TSADE, 2026-08-12).** The w determination returned
   CONDITIONALLY-DETERMINED: under one-medium, w = [0.0395, 0.0528] fm,
   a = [6.30e-17, 8.41e-17] m, Lorentz bound satisfied (1.11x unaimed),
   n_t = 111 LIVE inside the computed hbar census [47, 198]. One
   registered conflict forces the adjudication: one-medium and
   FND-040's kappa_pack-floor a readings cannot both stand. One
   prosecution, five payoffs (tube census, m_b, the FND-072 chain's a,
   W1's value, the kappa_pack question) -- or the T0 chain loses its
   underwriting identity. Charter outline in FND-073's results: state
   what one-medium FORBIDS, find the registered claim nearest to
   violating it, confront. Also owed to this chain: the
   encounter-spectrum derivation (owns FND-072/073's C3 tension, 1.49x
   at ka = 1). By five commissions'
   testimony, the registry's most-wanted acquisition: registering a rate
   or cross-section re-opens all three against laws already locked.
3. **The Born joint-outcome gate** -- untouched this arc. Can the
   derived global conservation/topological structure produce joint
   detection probabilities without importing a configuration-space
   guidance object? A decisive negative is valuable.
4. **The nuclear residual's other channels** (NUC-026): isospin quartic
   (coefficient ~-47, the largest), curvature (~+6 MeV).

**Running externally:** the lattice-precision push, now TWO entries --
FND-047's adjoint/fundamental decision table (0.5-1 percent decides the
kappa_pack floor) and FND-055's SU(6) k-string determination (decides
GRANT-N2's exclusion statistic outright; the measurement largely exists
and needs only sharpening).

---

## 6. Live cautions

**The timing lesson, accepted on the record.** The photon existence kill
sat registered in FND-REL-004 with its escape UNADJUDICATED across two
claims while the arc continued, and FND-MATTER-049's reopening tripwire
is recorded as having FIRED at 1e11x without halting further
vacuum-facing work. A registered contradiction whose escape is unrun is
a blocking item, not a footnote. Prosecute forks before building on top
of them.

**The counting lesson (FND-056).** See section 0.

**The stale-value class.** Before using any number from a claim's face,
check its bracketed annotations for corrections. The tripwire that keeps
catching these: read the neighbouring registrations before reusing a
code path. (This arc added one: NUC-026 round 1 locked the NUC-018 chain
the registry itself ranks worst.)

**The light carrier phrasing.** Light is the COLLECTIVE TRANSVERSE
Goldstone pair; the screw/torsion mode carries CHARGE (winding). Stale
phrasing survives in older documents -- do not propagate it.

---

## 7. First message to paste into the new session

> Continuing the Rope Framework. Corpus attached
> (`rope-framework-github.zip`, v3.20.8, 628 claims). Read `HANDOFF.md`
> first (sections 1-2 and the CHANGELOG 3.20.1-3.20.8 entries cover the
> 2026-08-12 arc), then `KNOWN_LIMITATIONS.md`.
>
> The photon-sector limitation is DISCLOSED (route (c), FND-062). The
> pairing channel separation is ADOPTED (NUC-030) with its falsifier
> armed at v0 = 16.97 MeV; the reconnection chain is derived in form
> down to the contrast g (FND-072); the w determination is
> CONDITIONALLY-DETERMINED (FND-073). Live grants: GRANT-CANDIDATE-ROT
> and GRANT-N2-GAP. The registry's decisive question is THE ONE-MEDIUM
> PROSECUTION (charter outline in FND-073's results); also owed: the
> encounter-spectrum derivation (owns the C3 tension) and Rank-1 g
> under the dependency-path protocol.
>
> Standard house discipline throughout.
