# HANDOFF — Rope Framework, next session

*Written 2026-08-11 at the close of the v3.18.0 arc. Everything a fresh
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
- **NEW, learned expensively this arc (FND-056):** "no derivation
  mentions X, so none is disturbed" is an INVALID audit argument. A
  derivation need not mention a degree of freedom to depend on HOW MANY
  there are. Counting is the channel, and this corpus kills on counts.

---

## 1. State of the corpus

**Release:** v3.19.0 (cut 2026-08-11), "The Dictionary Closes, The Photon Sector Opens."
**Registry:** 592 claims -- 116 Derived, 423 Modeled, 38 Failed-and-kept,
7 Open, 4 Conjecture, 4 EFT-constrained.
(Counts regenerate from claims.yaml -- trust `tools/sync_doc_facts.py`,
not this line.)

**Read these first, in order:**
1. `docs/history/RELEASE_NOTES_v3.19.0.md` -- the arc just completed (EM dictionary closed; photon sector disclosed).
2. `KNOWN_LIMITATIONS.md` -- the dealbreakers, front-loaded by design.
3. `analysis/SHIN_operator_ceiling_results.md` -- the photon sector's
   current position, and the one inequality (section 3 below).
4. `docs/STATE_OF_THE_PROGRAMME.md`.
5. `papers/rope_formulas.pdf` -- the formula compendium.

---

## 2. What just happened (eleven commissions)

**The pattern, and it is the arc's real content:** four independent
commissions, none aimed at the others, each found the ontology missing a
CARRIER rather than a number.

- **FND-051 (SCALE-001):** the first blind-target audit.
  UNDERSPECIFIED-DOMINANT -- five of eight collective channels cannot be
  POSED in registered inputs; three writable laws all miss low. The
  FND-044 one-number compression is bookkeeping on today's registry.
- **FND-052 (KAF):** the FND-050 grant's owed computation. UNBOUND-
  PREDICTED -- binding needs x > 4/(k^2+k+1), an order of magnitude
  above the licensed strain domain. Exposure clause fired.
- **FND-053 (SAMEKH):** WHY, by group theory. The demand factorizes,
  b_k(N) = (k-1) x 1/(N-1); the second factor needs Z_N and the medium
  is Z-charged (GG-006). Derivation branch CERTIFIED CLOSED.
- **FND-054 (GRANT-N2, author's):** strands carry one of N labels;
  attraction by label exchange.
- **FND-055 (AYIN):** the acceptance test PAID -- exclusion statistic
  gives v = 2/(N-1), hence b_k = (k-1)/(N-1), antisymmetric-Casimir
  IDENTICALLY, zero fitted coefficients. Partial success with live
  exposure: the corpus now OWNS Casimir against sine-favouring data.
- **FND-056 (PE):** the owed label-blindness audit, and it did NOT pass
  cheap. Dynamical labels give the light carrier 2N polarizations
  against a measured 2 -- a kill by the corpus's own EM-RECON-022/023
  criterion. Grant re-priced: two primitives, one coupling, one scale.
- **FND-057 (TSADE):** the gap clears only on the dispersive side of the
  three-pin fork. Intended tube/confinement derivation FAILED by seven
  orders.
- **FND-058 (QOF):** the fork's sole escape adjudicated. Necessity and
  motivation PASS; consistency FAILS -- removing the lattice does not
  remove the strands.
- **FND-059 (RESH):** the last escape given its best case and closed on
  FND-REL-002's own Derived isotropy (PeV photons confined to arcsecond
  cones about three axes).
- **FND-060 (SHIN):** the cheap fix closed as a CLASS -- see section 3.
- **GRV-103 (NUN):** frame-dragging provenance. GRANT-REQUIRED by
  elimination; twist is the only surviving carrier and lacks only its
  source.
- **NUC-026 (LAMED) / NUC-027 (MEM):** the nuclear residual classifier
  (DIFFUSE, 0.581 vs a 0.6 bar, five priced channels) and the pairing
  confrontation (NUC-024's A-independent form REFUTED at 6.6 sigma).

---

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
5. **ZENODO_RELEASE_NOTES.md** still frozen at the v2.2.1 era.

---

## 5. The ranked queue

1. **The NUC-021 1/sqrt(A) dilution derivation** -- the cheapest real
   physics available. Three registered misses (asymmetry magnitude,
   asymmetry exponents, pairing scaling) share ONE demand: the fixed
   cross-sublattice cost of one misplaced label must dilute as
   1/sqrt(A), i.e. the odd nucleon delocalizes. Derive it once, confront
   all three.
2. **The reconnection rate** -- missing in THREE independent contexts
   (FND-051's C4, FND-053's S2, NUC-026's D7). By three commissions'
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
> (`rope-framework-github.zip`, v3.19.0, 600 claims). Read `HANDOFF.md`
> first, then `docs/history/RELEASE_NOTES_v3.19.0.md`, then `RELEASE_NOTES_v3.18.0.md` (+ its addendum) and
> `KNOWN_LIMITATIONS.md`.
>
> The photon-sector limitation is DISCLOSED (route (c), FND-062); the
> live grants are GRANT-CANDIDATE-ROT and GRANT-N2-GAP. Rank-1 physics
> brick is the NUC-021 1/sqrt(A) dilution derivation.
>
> Standard house discipline throughout.
