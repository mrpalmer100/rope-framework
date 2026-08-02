[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21430784.svg)](https://doi.org/10.5281/zenodo.21430784)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Verify](https://img.shields.io/badge/verify-384%2F384%20passing-brightgreen.svg)](#verify-it-yourself)
[![verify-corpus](https://github.com/mrpalmer100/rope-framework/actions/workflows/verify.yml/badge.svg)](https://github.com/mrpalmer100/rope-framework/actions/workflows/verify.yml)

# rope-framework

**Published:** [https://doi.org/10.5281/zenodo.21430784](https://doi.org/10.5281/zenodo.21430784) · **Author ORCID:** [https://orcid.org/0009-0007-2454-5573](https://orcid.org/0009-0007-2454-5573) · **Version:** 2.5.0

A machine-verified development of the Rope Hypothesis — a classical, mechanical model in which matter and light are configurations of physical filaments — into falsifiable, independently checkable form.

> **This corpus establishes numerical reproducibility and internal consistency, not physical truth.** Whether the underlying physics is correct is exactly what external scrutiny is invited to decide.

> **Scope (read first):** The Rope Hypothesis is a *classical, configuration-counting* model. It is strongest in electromagnetism, optics, and the mechanical sectors; its classical weak-field gravity is **falsified under stated assumptions** (kept as a finding, not hidden); and it **provably does not reproduce quantum entanglement** in its present form (a counting model cannot produce Bell/CHSH violation; QB-003 Failed, QB-005 negative). The measurement arc (QB-007–011) maps this boundary in detail — single-particle statistics reproduced or cornered, the detector angle fixed at γ = 1, the residual gap localized to configuration-space guidance — without crossing it; a future non-classical rope structure is not claimed impossible. Nothing is hidden — see [`KNOWN_LIMITATIONS.md`](KNOWN_LIMITATIONS.md).

> **Corpus state:** 402 registered claims (104 Derived, 262 Modeled, 4 EFT-constrained, 4 Conjecture, 5 Open, 23 Failed-and-kept); 384 code-backed, all passing; 58 papers. Counts regenerate from `claims.yaml` — the authority is the registry, not this line.

**🪜 [The Ladder and the Frontier](figures/rope_ladder.png)** — the whole corpus in one image: three layers, every result placed by status, and the coherent frontier where the open problems cluster. The best single-glance answer to "what is this?"

**🎨 [Figure gallery](figures/README.md)** — conceptual diagrams, each labeled with its corpus status (derived / modeled / hypothesis).

**✨ START HERE: [Eleven Results We Did Not Expect](docs/SURPRISES.md)** — how the investigation actually unfolded: derived emergences, kept failures, labeled coincidences, and the day the framework eliminated its own favorite hypothesis. The best answer to "why spend an afternoon here?"

**🗺️ [Roadmap of Knowledge](docs/ROADMAP.md)** — the whole corpus at a glance: [wall chart](docs/roadmap.png) and [interactive dependency explorer](docs/roadmap.html) (click any claim; see its dependencies, dependents, and full downstream), all generated from claims.yaml by `tools/build_roadmap.py`.


**Current release: v3.1.0** (1 Aug 2026) — see `docs/RELEASE_NOTES_v3.1.0.md`.

**If the rope model is wrong**, the transferable result is
`docs/CONSTRAINTS_FOR_MECHANICAL_SUBSTRATE_THEORIES.md` — universal programme
disciplines, constraints on finite-scale mechanical substrates, and
rope-specific findings, kept in three explicitly separate tiers.

**New reader?** Start with `docs/STATE_OF_THE_PROGRAMME.md` — a short, current
account of what the framework claims, what it predicts, what was retired and why.

## What this corpus actually bets: one prediction

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

**The nearest miss**, and the corpus's clearest route back to a second: GRV-040's
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

The mesoscopic-hbar identification is RETIRED (2026-08-01) after six
independent closures. See `docs/HBAR_SECTOR_CLOSURE.md`.

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
