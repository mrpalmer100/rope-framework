# Release Notes — v3.20.0 (2026-08-11): What an Electron Looks Like

This release began with a plain question — *what does an electron actually
look like?* — and ended thirteen commissions later with a derived core
structure, a measured negative result, and an attractive interpretation
falsified by the framework's own mechanics. It also closes the
electromagnetic sector's central assembly and discloses the photon
sector's high-energy failure.

**613 registered claims** (120 Derived, 440 Modeled, 38 Failed-and-kept,
7 Open, 4 Conjecture, 4 EFT-constrained).

---

## Part I — The electron core: derived, measured, and one story falsified

The corpus could say what the electron *is* — a dynamical winding of the
internal azimuth, hollow, with a hard core — but not what the core looked
like. Thirteen commissions later it can.

**The boundary is explained (`ELEC-090`).** The exact profile's first
integral r²F(p) = C reads **r² sin θ = C** once the slope p = ψ′ is written
as tan θ — so F is the *sine of the strand tilt*, and the hard core is
simply where the tangent reaches **90°**. The reported divergence at r₀ was
a parametrization artifact, the second apparent singularity in this sector
to dissolve on inspection. The hollow is **kinematic** (sin θ ≤ 1), hence
independent of every material parameter and untunable.

**The core has structure (`ELEC-090`, `ELEC-091`).** Strands arrive
*tangent* to the boundary, so by the hairy-ball theorem the tangent field's
zeros total index 2 — the core **cannot be isotropic**. Matching to the
exterior winding then fixes that field as **azimuthal with exactly two
polar defects**, independently reproducing index 2 by a route not built to
produce it.

**The axis looked exactly like spin — and an external reviewer proposed
testing that rather than believing it.** The test worked:

- `ELEC-096`: the weave's point group is **O_h, not SO(3)**, so pinning is
  allowed at order 4 in K(n) = Σnᵢ⁴ − 3/5. Symmetry protection excluded;
  orientation averaging unregistered.
- `ELEC-099`: the pinning is **measured** under cubic periodic boundaries
  on the registered strand engine — anisotropy fraction **0.21**, **166×**
  the noise floor, **R² = 0.71** on an angular form fixed in advance and
  never fitted. Null projection machine-zero; global-rotation control
  passed; all controls run *before* orientation labels were read.
- `ELEC-100`: a dependency trace showed the corpus's spin machinery —
  Tsirelson, the half-angle junction law, Stern-Gerlach, the transport law
  — **predates the axis by many sessions and never referenced it.**

**Verdict: an interpretation died, not a mechanism.** Retired: *the axis's
two orientations are the electron's two spin states*. Kept: the axis, which
was derived from topology without reference to spin. Spin lives where it
always lived — in GRV-020's internal azimuth and the Hopf/Pauli-quaternion
machinery.

**Methodological result, now house discipline:** *geometric resemblance is
not physical identification — require a dependency path.* The axis had two
poles, an axis, two orientations. The resemblance was total and the
identification was empty.

---

## Part II — The field-tensor dictionary closes

`EM-016`, the complete mapping from mechanical state to electromagnetic
field tensor, carried four explicit debts. All four fell in one day, each
to a theorem with its defeater named **before** the attempt:

- **(iv) uniqueness** (`EM-017`): any assignment reproducing the same
  forces gives the same (E, B) pointwise. The duality rotation, pre-named
  as the defeater, fails both arithmetically and structurally — charge is
  winding and no monopole is registered.
- **(iii) φ's channel** (`EM-018`): transverse excluded by a computed
  Helmholtz argument, screw excluded structurally (it *is* the charge), and
  the longitudinal channel's gaplessness — derived elsewhere for an
  unrelated reason — is exactly what Coulomb requires.
- **(ii) the inertial term** (`EM-019`): the *same shift symmetry that
  forbids a mass term permits the inertial one*, because a gauge label's
  rate of change is observable even when the label is not.
- **(i) Σ** (`EM-021`): not a free constant but T₀·n_L on the registered
  mesh. The figure that made it look independent was a **lower bound
  saturated by an assumed equality** whose warrant had been withdrawn.

**Graded Derived** (`EM-022`, the author's act, registered separately from
its own evidence) with three conditionalities on its face and **a falsifier
armed**: if the κ_pack floors move, the grade returns to adjudication.

---

## Part III — The photon sector, disclosed

Ultra-high-energy photons (LHAASO's Galactic PeV gamma rays) cannot be
carried by the medium as currently specified. Four escapes were prosecuted
and all four closed — one on the corpus's *own* Derived isotropy theorem,
one as an entire operator class. An external reviewer then corrected the
diagnosis (`FND-061`): the problem is **anisotropy, not a Nyquist cutoff**,
which widens the demand from "find an impossibly small length" to "supply
isotropy at high k."

**Route (c) adopted** (`FND-062`, the author's act): registered openly in
`KNOWN_LIMITATIONS.md`, first section. The transverse-wave mechanics are
**not** refuted — every result at accessible energies stands.

---

## Part IV — Everything else

- **`FND-051`–`FND-053`, `GRV-103`:** four independent commissions each
  found the ontology missing a **carrier** rather than a number.
- **`FND-054`/`FND-055`:** GRANT-N2 adopted and its acceptance test paid —
  antisymmetric-Casimir binding derived identically, zero fitted
  coefficients — then `FND-056`'s audit found dynamical labels give the
  light carrier 2N polarizations against a measured 2.
- **`NUC-026`/`NUC-027`:** the nuclear residual classifier returned DIFFUSE
  with five priced channels; NUC-024's A-independent pairing form refuted
  at 6.6σ.

---

## Corrections made and kept

Seven self-corrections are registered rather than quietly patched,
**several against claims from the same session**:

- `EM-020`'s DIFFERENT-OBJECTS verdict, corrected within the hour. *Lesson:
  a numerical gap is evidence of distinct objects only if both numbers are
  of the same epistemic kind.*
- A stale-value error caught by the author. *Lesson: a claim's blocker text
  ages independently of the claims that would discharge it.*
- `ELEC-094`'s proxy extrapolation, withdrawn when the registered engine
  contradicted its trend.
- `ELEC-097`'s procedural failure — an adequacy check run *after* the scan
  it invalidated.
- A process failure accepted on the record: the photon contradiction sat
  with its escape unadjudicated while work continued. **New house rule: a
  registered contradiction whose escape is unrun is a blocking item.**

---

## Method

Every result was produced under pre-registered bars: hypotheses, thresholds,
defeaters and verdict grammars locked in `analysis/*_LOCKED.md` **before**
any number was computed. Failures register as `Failed-and-kept` and are
never rescued or quietly re-scoped.

## Verification

```
python3 tools/verify_corpus.py            # full: runs every backing benchmark
python3 tools/verify_corpus.py --quick    # structure and existence checks
```

## The queue after this release

1. **The mesoscopic scale g (`FND-044`)** — rank 1. Carries a protocol rule
   from this arc: *do not search for something that numerically resembles
   g; require a dependency path from an existing collective mechanism
   before looking at the target value.*
2. **The NUC-021 1/√A dilution derivation** — three registered misses share
   one demand.
3. **The reconnection rate** — missing in three independent contexts.
4. **On the author's desk:** GRANT-CANDIDATE-ROT, GRANT-N2-GAP, the κ
   rename.

## Acknowledgement

Several of this release's sharpest results came from an external reviewer:
the axis-pinning test, the fixed-input discipline, the blinding order, the
global-rotation control, the perturbative control that failed, the
dependency audit that resolved the arc — and the judgement to stop.
