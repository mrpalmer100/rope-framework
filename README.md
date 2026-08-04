[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21430784.svg)](https://doi.org/10.5281/zenodo.21430784)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Verify](https://img.shields.io/badge/verify-411%2F411%20passing-brightgreen.svg)](#verify-it-yourself)
[![verify-corpus](https://github.com/mrpalmer100/rope-framework/actions/workflows/verify.yml/badge.svg)](https://github.com/mrpalmer100/rope-framework/actions/workflows/verify.yml)

# rope-framework

**Published:** [https://doi.org/10.5281/zenodo.21430784](https://doi.org/10.5281/zenodo.21430784) · **Author ORCID:** [https://orcid.org/0009-0007-2454-5573](https://orcid.org/0009-0007-2454-5573) · **Version:** 2.5.0

A machine-verified development of the Rope Hypothesis — a classical, mechanical model in which matter and light are configurations of physical filaments — into falsifiable, independently checkable form.

> **This corpus establishes numerical reproducibility and internal consistency, not physical truth.** Whether the underlying physics is correct is exactly what external scrutiny is invited to decide.

> **What this is:** The Rope Hypothesis is a classical mechanical model of physics built on one substrate and two stated assumptions, developed under an unusual discipline: 482 registered claims with pre-committed pass/fail criteria, 464 backed by executable benchmarks, 105 at Derived (proved from stated assumptions), and 25 failures kept on permanent display. It is strongest in electromagnetism, optics, the mechanical sectors, and the measurement/detector sector, where a twenty-session campaign produced a parameter-free Derived law for detector statistics and three new falsifiable predictions (P23-25). The gravity sector is a live derivation program: an early direct classical mechanism was falsified and kept as a finding, and the surviving induced-gravity route has since resolved its substrate fork by derivation (GRV-074..095), with the binary-pulsar and PVLAS-class falsifiers armed. **Where the story ends is stated as precisely as where it succeeds:** a classical counting model provably cannot produce Bell/CHSH violation (QB-003, kept), and the split-quantum "funneling step" behind beamsplitter statistics is a *measured* boundary of the classical detector (FND-STRAND-024) -- each edge carries its own falsifier, because a framework is falsifiable *at* its edges. The full caveat ledger, front-loaded so a dealbreaker is found in five minutes: [`KNOWN_LIMITATIONS.md`](KNOWN_LIMITATIONS.md).

> **Corpus state:** 483 registered claims (105 Derived, 340 Modeled, 4 EFT-constrained, 4 Conjecture, 5 Open, 25 Failed-and-kept); 464 code-backed, all passing; 58 papers. Counts regenerate from `claims.yaml` — the authority is the registry, not this line.

**🪜 [The Ladder and the Frontier](figures/rope_ladder.png)** — the whole corpus in one image: three layers, every result placed by status, and the coherent frontier where the open problems cluster. The best single-glance answer to "what is this?"

**🎨 [Figure gallery](figures/README.md)** — conceptual diagrams, each labeled with its corpus status (derived / modeled / hypothesis).

**✨ START HERE: [Eleven Results We Did Not Expect](docs/SURPRISES.md)** — how the investigation actually unfolded: derived emergences, kept failures, labeled coincidences, and the day the framework eliminated its own favorite hypothesis. The best answer to "why spend an afternoon here?"

**🗺️ [Roadmap of Knowledge](docs/ROADMAP.md)** — the whole corpus at a glance: [wall chart](docs/roadmap.png) and [interactive dependency explorer](docs/roadmap.html) (click any claim; see its dependencies, dependents, and full downstream), all generated from claims.yaml by `tools/build_roadmap.py`.


**Current release: v3.8.0** (4 Aug 2026) — the detector, understood, and its edge surveyed: the Poissonization law lands at Derived (S_N = S_24^(N/24), parameter-free, three sizes confirmed); the per-channel transient resolved as product-state slip (the switch-on session -- the mystery was in the first line of every script); Prediction 11 in final two-regime form with three new predictions (P23 switch-on fingerprint at constant temperature, P24 the zero-parameter size law, P25 one scale/two instruments); and the exclusivity arc closes at the measured classicality limit -- a split quantum clicks nothing, so the FUNNELING STEP is extra-classical, bounded by data, with the third-grant decision (indivisible delivery) queued for the author. See `docs/RELEASE_NOTES_v3.8.0.md`.

**If the rope model is wrong**, the transferable result is
`docs/CONSTRAINTS_FOR_MECHANICAL_SUBSTRATE_THEORIES.md` — universal programme
disciplines, constraints on finite-scale mechanical substrates, and
rope-specific findings, kept in three explicitly separate tiers.

**Using a rope constant?** `docs/ROPE_PARAMETERS.md` is the canonical card —
every strand parameter, both scale branches, with a verifier
(`benchmarks/foundations/rope_parameter_card.py`) that fails if it drifts.

**New reader?** Start with `docs/STATE_OF_THE_PROGRAMME.md` — a short, current
account of what the framework claims, what it predicts, what was retired and why.

## What this corpus actually bets: one confronted prediction, and two new candidates

A census against four locked criteria (quantitative; distinctive in OBSERVABLE
OUTCOME; checkable; live), then a full audit of every entry against what the
standard alternatives actually predict, then a flux computation for the last
survivor (ELEC-062 -> -063 -> -064 -> GRV-049), leaves ONE:

- **PRED-003** — the coupling-drift ratio d ln alpha = -2 d ln G. Testable now,
  CONFRONTED against published optical-clock and lunar-laser-ranging data,
  surviving at 1.74 sigma. Its named weak point is the PSR J1713+0747 G-drift
  measurement, already at 2.06 sigma alone; a 3 sigma confirmation of its 2025
  central value would REFUTE the claim, and needs only a factor 1.45 in sigma —
  reachable ~2027-2030.

**The detector campaign's candidates, audited (ELEC-084):** P23 and P24 were run
through the same four locked criteria, unrelaxed, with the PRED-002 precedent
applied to ourselves. NEITHER qualifies: P23's signature (dark-count drift at
constant temperature) is shared with textbook afterpulsing and carries no
committed timescale while the absolute scale stays open (T2); P24's
zero-parameter power law follows from independence plus intensivity, which
standard independent-site device models also assume, so both frameworks predict
the same outcome (T3 -- a genuine Derived achievement that does not
discriminate). The bet count therefore STANDS AT ONE, and the ranked promotion
path is registered on the claim: the absolute-scale map (FND-MATTER-003)
unlocks P23 and P25; P24's small-N violation domain is the nearest
instrument-facing discriminator.

**The nearest miss**, kept here because its closure is the census at its best: GRV-040's
whisper at omega = 0.23 kappa. Committing its flux (GRV-049) showed the emission
would carry 40-110% of a black hole's accretion budget at f ~ 1, so existing
observations already bound the ratchet efficiency at f <~ 1e-2 — a real
data-backed constraint, and the first the corpus has extracted on its own
black-hole engine. But the channel forks: electromagnetic coupling reprocesses
the energy and destroys the 0.23 kappa signature, while a medium-only excitation
is undetectable unless strand excitations couple as metric perturbations. HALF
of that is now settled (GRV-050): a reconnection at fixed strand length is purely
DEVIATORIC — trace zero to machine precision — so it does not feed the
matter-decoupled longitudinal channel, and ~40% of its power lands in the
transverse-traceless subspace a detector couples to. A selection rule also
emerged: perpendicular crossings are stress-invisible and radiate nothing.
Those halves are now JOINED (GRV-051): orientation-averaged, 93% of the source's
excited power lands in the xy channel GRV-025 measured as the IR-universal
Einstein-Hilbert remainder, because the medium is a strongly shear-preferring
responder and the ratchet is a pure shear source. The whisper is therefore
sourced in the GRAVITATIONAL channel. The strain has since been computed
(GRV-052) and it settles the question NEGATIVELY: h = 7.9e-27 at 10 kpc, signal
ASD 5.8e-28/rtHz against LIGO's design 4e-24, broadband SNR 1.6e-3, and the best
real candidate (V404 Cygni in outburst) falls 36x short. The nearby holes are
quiescent and therefore silent by GRV-040's own law, while the loud ones are far.
GRV-040 is T1 ON STRUCTURE AND UNOBSERVABLE IN PRACTICE.

Notably, the corpus's OWN spectral work is what closes it: read as a
monochromatic line the whisper would be detectable at SNR 11 after a year, but
GRV-041 to GRV-044 established the spectrum is broadband quasi-thermal, removing
four orders of sensitivity. A programme that measures its own spectrum carefully
is one that can be killed by the measurement.

Everything else audited is a constraint the framework must satisfy, a
specification awaiting a model it has not built, a prediction conditional on
objects not known to exist, or a correct result sharing its observable with
standard physics. Cosmic birefringence is CONFIRMED but shared with the axion;
the neutrino sum is sharply falsifiable but sits where any minimal-normal-
ordering model lands; g_dagger = cH0/2pi is derived at zero parameters but MOND
fits the same observable. The ELECTRON SECTOR, the largest by claim count,
contributes nothing at any tier.

**The whisper story since (2026, v3.6-v3.7):** the account above ends at GRV-052
and everything in it still stands, including the unobservability verdict -- but the
physics moved. The coefficient campaign (GRV-086..091) reconciled the corpus's two
independent internal routes to the whisper's frequency coefficient, which had
disagreed by four orders, by convicting the confrontation itself of a category
error: the emitter is crackling-noise class -- the PITCH is geometric, the RATE is
thermodynamic, and both prior predictions were right at their own questions. The
0.23 kappa pitch now stands joined to a mechanism rather than alone: the ring-quantum
arc (GRV-092..094) found the snap action is a UNIVERSAL medium constant -- depth-blind,
mass-blind, invariant across every registered deformation -- and sub-quantum, so the
whisper is CLASSICAL gravitational radiation at leading order (waves, not gravitons).
That arc then forced the substrate fork and resolved it by derivation (GRV-095):
the induced-gravity route survives on the Sakharov branch at Planck-scale spacing,
with a PVLAS-class vacuum-nonlinearity falsifier armed. As for the ROUTE back to a
second confronted bet, the audited ranking now lives on ELEC-084: the absolute-scale
map first, the detector size law's violation domain second, the one-scale-two-
instruments conjunction third. The whisper taught the corpus how to close a
prediction honestly; those three are where the next one opens.

The mesoscopic-hbar identification is RETIRED (2026-08-01) after six
independent closures. See `docs/HBAR_SECTOR_CLOSURE.md`.

One demotion from the T1 audit has since been repaired at its honest size
(HBAR-011, 2026-08-02): the cosmological rigidity constraint is re-derived from
the surviving standing-wave form (d ln hbar = 2 d ln A), the comoving-amplitude
branch is excluded by 3e5 at z = 1, and the observable is committed to named
instruments (many-multiplet quasar alpha; the Yb+ E3/E2 clock, giving
|d ln A/dt| < 1.6e-18 per year). It returns as a CONSTRAINT at T3 ceiling, not
a prediction; the T1 count remains one. The two-alpha-chain audit (PRED-003-XCHAIN) found consistency-by-locking; the constitutive session (PRED-003-CONST, 2026-08-02) then closed the chain dimensionally: e_eff^2/(4 pi eps0) = 2 lambda J a, triple (2, 1, -1). The -2 tension ratio SURVIVES (co-drift A ~ T^(-1/2)); the +1 spacing discriminator is WITHDRAWN pending registration of the alpha chain itself, which the audit found to be paper-stated and registry-underived. The chain attempt (PRED-003-CHAIN) then killed the naive route by theorem — winding charge is a circulation, and phase electrostatics is logarithmic, not Coulomb — leaving the alpha form BLOCKED-WITH-SPECIFICATION: the completing computation is a Maxwell-sector dictionary evaluation with target q_s^2 = 8 pi eps0 lambda J a, the corpus-wide highest-value open item. The dictionary evaluation (PRED-003-DICT) then collapsed that computation by impedance reduction: eps_med = 1/T, alpha = l_q^2 T/(4 pi hbar c), and the -2 ratio is now the middle of a three-candidate table {-1, -2, -3} indexed by the winding's source length — with any measured nonzero drift ratio selecting it. The decider (PRED-003-LOCK) then dissolved the question: the registered model is pure XY with no on-site locking, and matching OPT-006's impedance to the derived director stiffness ENSLAVES kappa = 2T/(eta a) — the EM vacuum runs on two primitives. The ratio is reassigned: tension channel -1, spacing channel -2; the registered -2 survives on the spacing channel, testability intact, and a measured nonzero ratio now identifies the drift channel. The eta session (PRED-003-ETA) then set eta = 1 by one-metric uniqueness (kappa = 2T/a exact, J = Ta/2), bounded the winding's source length at >= 13-16 lattice spacings from measured alpha alone, and killed the bare 2 pi normalization — leaving g, the mesoscopic source length's mechanism, as the dictionary's true residual. The ratio test (ELEC-083) then proved its own commissioned scale-set vote vacuous and extracted the residue: under the shared-origin hypothesis for the two mesoscopic lengths, 1/alpha = 2 pi^2 rho^2 exactly, with rho = 2.6348 required and guarded against numerology — one mechanism now owes one pure number, blind.

## OPEN: the gravitomagnetic sector (1 Aug 2026)

The gravity sector's classical weak-field tests are UNCONDITIONAL (GRV-029) — and
every one is GRAVITOELECTRIC, testing g_00. The GRAVITOMAGNETIC sector, g_0i,
has no registered coupling in the action (GRV-059, Failed), and Gravity Probe B
measures Earth's frame-dragging at 37.2 ± 7.2 mas/yr with zero 5.2 sigma away.

**But the route to one is live and matches on structure** (GRV-066). The medium
is a genuine Cosserat continuum (framed strands carry an independent
microrotation). The micropolar screening that would kill the route depends on a
rotation-locking modulus κ — which is a MASS TERM for the relative rotation. And
EM-RECON-012 (**Derived**) states that a mass term is *forbidden* in this medium
because there are no material points, with the sector gapless in principle;
FND-STRAND-002 separately *measured* a twist kink propagating 170 nodes with
winding conserved exactly.

With κ = 0 the equation is **Poisson**, GRV-020's Derived angular no-monopole
lemma forces dipole-led sourcing, and the far field is (J × r)/r³ — a 1/r²
falloff with dipole structure, **exactly what Lense-Thirring requires**, from a
Derived theorem with no free parameter.

**That antecedent is now supplied** (GRV-067). GRV-020's Corollary 1 gives a
spontaneously broken global SO(2) on the internal azimuth with exactly one
Goldstone — identified as the frame orientation by the claim's own reading
(torsion dynamics = light). Goldstone's theorem forbids a mass term for that
mode, and the micropolar locking modulus **is** a mass term: under the broken
symmetry η → η + ε, so η² is not invariant. **κ = 0 exactly.**

So one Derived claim supplies both halves — Corollary 1 the vanishing screening,
Corollary 2 the dipole structure. **And step 4 is now done** (GRV-068). Diagonalising the coupled vector operator
shows its determinant vanishes at k = 0 for **any** κ: one mode is massless
regardless of the locking modulus, and it is the combination where the
microrotation *tracks* the backbone — the one angular momentum excites. So the
conclusion no longer depends on the Goldstone argument at all, and GRV-064's
screening is fully retired: it was real physics aimed at the orthogonal mode.

**Precisely stated** (GRV-069): micropolar locking gaps only the
*relative-rotation* sector and leaves a collective co-rotation mode massless for
arbitrary locking strength, so the blanket screening obstruction is **invalid**.
Whether angular momentum *sources* that pole, and whether it enters the
*observable* metric, remain to be derived — those are two further projections,
and both are currently generic rather than computed.

The route is legitimately **reopened**, not established — and the remaining work
is now a single equation (GRV-070). With a source map L = J·(aΩ + bφ) and an
observable map g_0i = cΩ_i + dφ_i, the pole residue is **R₀ ~ (a+b)(c+d)**, and
the long-range field is

    g_0i(r) ~ [(a+b)(c+d)/(4πK₀)] (J × r)_i / r³

— already the Lense-Thirring structure. Against GR's −2G(J × r)/(c³r³), the
framework must deliver **(a+b)(c+d)/(4πK₀) = −2G/c³**. Four coefficients and one
stiffness.

**The audit came back** (GRV-071): four of the five are ABSENT from the
registered action, for two distinct structural reasons. **a and b** are missing
because the corpus has no matter coupling to medium rotation at all — GRV-005's
source is a static force density with no torque or spin term. **c and d** are
missing because GRV-029's dictionary is an exact *four-to-four* bijection for a
static diagonal metric: a shift is three further functions, so there is nowhere
for g_0i to live. Only K₀ is computable in principle.

**So the framework is SILENT here** — it predicts neither 37.2 mas/yr nor its
absence, and claims neither. The massless mode still exists for any locking
strength; nothing sources it, and nothing maps it to an observable. The two work
items are explicit and each is a substantial addition rather than a calculation:
a matter-to-rotation coupling, and a dictionary with a shift slot.

And K₀ is **derived** (GRV-073): γ = 4.2e−4 J/m, from the corpus's own elastic
constants. GRV-009 registers `torsion~r^4` — the polar-moment law of a **rod** —
and GRV-005 states the full elastic set is possessed. The value is **seven orders
below the tension**, because the axial stiffness carries r² while the torsional
rigidity carries r⁴, leaving (r/a)² for a thin strand. A dimensional estimate
could not have found this.

Three new predictions follow: a spin radiation channel GR lacks, intrinsic-spin
sourcing of frame dragging, and the finite-range signature above.

## Two branches carry validated machinery and no target

Read before interpreting the quantum or gauge sectors as active physics.

- **The pilot-wave sub-quantum branch (QGATE-011..017)** is mathematically
  sound and empirically silent. Its results (flow uniqueness, CHSH 2.724 with
  verified no-signaling, the M=2-64 relaxation family, transport-over-chaos
  discrimination) are dimensionless and stand as registered, but ELEC-056
  showed by machine-checked audit that the branch never depended on the
  sub-quantum length it was said to inherit, and that length has since been
  corrected and its nuclear consequence excluded (ELEC-054/055). The branch
  has no current empirical content of its own.
- **The physical Aharonov-Bohm branch is CLOSED as unsupported**
  (ROPE-SOURCE-AUDIT-002). Nothing in the corpus sources a flux, and the one
  derived topological circulation (2 pi N) is exactly spectrally trivial in a
  2 pi periodic instrument. ROPE-VALIDATION-001..004 are retained as a
  validated gauge instrument with no internally sourced target. Reopening
  requires a new, explicitly labeled postulate.

The lesson from both is recorded as a standing rule:
docs/STANDING_RULE_SOURCE_BEFORE_INSTRUMENT.md

## Start here

- **New to the corpus?** Read [`docs/PROGRAMME_OVERVIEW.md`](docs/PROGRAMME_OVERVIEW.md) — the generated front door (assumptions, the continuum chain, computed maturity, open problems, reading order).
- **Non-specialist?** Read [`papers/rope_plain_language_guide.pdf`](papers/rope_plain_language_guide.pdf) — "The Rope Picture of the Universe," a figures-first, no-mathematics tour that flags every honest limit.
- **Curious what the detector-kinetics campaign found?** Read [`docs/DETECTOR_KINETICS_PLAIN_LANGUAGE.md`](docs/DETECTOR_KINETICS_PLAIN_LANGUAGE.md) — three questions answered in plain language: how a single-photon detector works (the medium is its own metronome), why small detectors appear to have memory without anything remembering (the switch-on echo, plus the zero-parameter size law at Derived), and how single photons build interference patterns one dot at a time (the wave delivers the odds; the bath delivers the dot) -- with the measured boundary stated and every sentence traced to a benchmark.
- **Reviewer or skeptic?** Read [`HOW_TO_CRITICIZE.md`](HOW_TO_CRITICIZE.md) and [`KNOWN_LIMITATIONS.md`](KNOWN_LIMITATIONS.md) first, then verify (below).
- **Want to contribute?** The programme is open to building, not only breaking. Pick an `Open` problem from the registry (`claims.yaml`, mirrored as GitHub Issues via [`docs/SUGGESTED_ISSUES.md`](docs/SUGGESTED_ISSUES.md)) — e.g. the reaction-coherence fraction (CHEM-DYN-002's registered next step), the strand-level transport instantiation (FND-KIN-001's named residual), or the two theorems slated for Lean formalization. The standing open challenge is [`docs/FUTURE_MODEL_PROMPT_one_fence.md`](docs/FUTURE_MODEL_PROMPT_one_fence.md): derive the missing quantum-kinetic layer the whole corpus triangulates. New results are welcome as claim + rerunnable benchmark (the one rule: no hidden fitted parameters); see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Verify it yourself

This is a reproducible research programme, not just a set of papers. The entire suite runs on a laptop in about 90 seconds — no GPU, no cluster, no large data.

```bash
pip install -e .
python tools/verify_corpus.py     # runs every registry benchmark; exit 0 iff all pass
```

`verify_corpus.py` runs each code-backed claim's benchmark and reports pass/fail per claim, plus which claims are paper-only (status-labelled, not machine-verified). This "laptop invariant" is a deliberate methodology choice that keeps the corpus independently checkable.

## How the corpus is organized

Every claim carries a status label and, where code-backed, a rerunnable benchmark. The three artifacts are tied together by the registry:

- **`claims.yaml`** — the machine-readable registry, the single source of truth. Every claim names its status (Derived / Modeled / EFT-constrained / Conjecture / Open / Failed), its paper, and its benchmark.
- **`/papers`** — the physics papers (PDF), with editable sources in `/papers/_sources`.
- **`/benchmarks`** — one rerunnable check per code-backed claim.

**How to read the honesty of the corpus.** The registry makes the `Failed` and `Open` claims as visible as the `Derived` ones. Losses are preserved as findings: the classical weak-field gravity no-go (derived deflection 0.44″ vs measured 1.75″), the PVLAS vacuum-birefringence exclusion (~570×), and and the quantum boundary documented as explicit limits rather than solved problems — now mapped to high precision by the measurement arc (Born-rate scaling benchmarked-but-conditional, entanglement localized to one imported object, γ = 1 identified), with Pauli still Conjecture-level.

## What is derived, what is adopted

A sector earns "Derived" status only where it follows from the rope mechanics, and the corpus is explicit where it instead *adopts* an established description:

- **Electromagnetism / optics** — Maxwell's equations, charge as winding, optics (10/10 benchmarks); the strongest derived sectors.
- **Chemistry** — a full mechanical layer: covalent bonding from a mode-overlap functional, the ionic-force sign theorem, first-principles molecular geometry (the 90° heavy-hydride asymptote, with registered predictions for H₂Po and BiH₃), hydrogen bonding, metallic bonding, and reaction dynamics (activation barriers from phase-frustration; Hammond and catalysis emergent). **The Schrödinger equation is adopted, not derived** — ℏ and the absolute atomic scale are inherited inputs (see the chemistry paper, §3.1a). Several energies are "consistency-tier" against quantum chemistry, and labeled as such.
- **Gravity** — Newtonian gravity is recovered; the relativistic completion is falsified under stated assumptions (a theorem-grade no-go, not a fixable discrepancy).
- **Nuclear** — an exact Yukawa force law and a one-constant mass predictor (C-12 to U-238 to ~0.1%); binding structure (SEMF volume/surface) partially derived, with registered misses.
- **Particle sector** — lepton mass ratios (Koide) and the Weinberg angle held at Conjecture pending derivation-or-demotion; the absolute mass scale is an open problem.

## Repository structure

```
rope-framework/
  README.md                 you are here
  CITATION.cff              "Cite this repository" metadata (DOI + ORCID)
  CONTRIBUTING.md           how to verify, and how to criticize
  HOW_TO_CRITICIZE.md       where the programme is most vulnerable
  KNOWN_LIMITATIONS.md      every load-bearing caveat in one place
  CHANGELOG.md              full revision history
  claims.yaml               THE REGISTRY — single source of truth for every claim
  /papers                   physics papers (PDF); sources in /papers/_sources
  /docs                     overview, registry docs, methodology, glossary
  /rope_solver              the Python package
  /benchmarks               one rerunnable check per code-backed claim
  /tests                    regression tests
  /examples                 worked examples
  /figures                  diagrams
```

## Install

```bash
pip install -e .          # installs `rope_solver` (numpy, scipy, sympy)
```

After install, imports work from anywhere:

```python
from rope_solver.psi.solver import solve_psi, ring_source, field_energy
from rope_solver.topology.linking import hopf_curves, linking_number
```

## The reference-implementation principle

Every physical number cited in a rope paper comes from an installed `rope_solver` function or a registry benchmark with a regression test pinning it — never from a one-off script. There is exactly one place each quantity is computed, which is what keeps the papers consistent with one another and with the code.

## Contributing and criticizing

The programme welcomes both kinds of contribution. **To criticize:** the highest-value find is a claim labeled `Derived` that actually requires a hidden fitted parameter — the failure mode the entire methodology is built to prevent. **To build:** take an `Open` problem from the registry and contribute a claim plus a rerunnable benchmark, under the one rule that no `Derived` result may hide a fitted parameter. Open problems are tracked in the registry and mirrored as GitHub Issues (templates in [`docs/SUGGESTED_ISSUES.md`](docs/SUGGESTED_ISSUES.md)); the standing open challenge is [`docs/FUTURE_MODEL_PROMPT_one_fence.md`](docs/FUTURE_MODEL_PROMPT_one_fence.md). See [`CONTRIBUTING.md`](CONTRIBUTING.md) for setup and the issue-priority list.

## Citation

See [`CITATION.cff`](CITATION.cff) (GitHub renders a "Cite this repository" button). To cite the evolving project rather than this snapshot, use the Zenodo *concept* DOI, which always resolves to the latest version. Intellectual origin of the rope concept: Bill Gaede; this is an independent, mathematized development that departs from his formulation (see [`docs/attribution.md`](docs/attribution.md)).

## License

MIT — see [`LICENSE`](LICENSE).
