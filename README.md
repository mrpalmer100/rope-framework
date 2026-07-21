[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21430784.svg)](https://doi.org/10.5281/zenodo.21430784)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Verify](https://img.shields.io/badge/verify-124%2F124%20passing-brightgreen.svg)](#verify-it-yourself)
[![verify-corpus](https://github.com/mrpalmer100/rope-framework/actions/workflows/verify.yml/badge.svg)](https://github.com/mrpalmer100/rope-framework/actions/workflows/verify.yml)

# rope-framework

**Published:** [https://doi.org/10.5281/zenodo.21430784](https://doi.org/10.5281/zenodo.21430784) · **Author ORCID:** [https://orcid.org/0009-0007-2454-5573](https://orcid.org/0009-0007-2454-5573) · **Version:** 2.2.3

A machine-verified development of the Rope Hypothesis — a classical, mechanical model in which matter and light are configurations of physical filaments — into falsifiable, independently checkable form.

> **This corpus establishes numerical reproducibility and internal consistency, not physical truth.** Whether the underlying physics is correct is exactly what external scrutiny is invited to decide.

> **Scope (read first):** The Rope Hypothesis is a *classical, configuration-counting* model. It is strongest in electromagnetism, optics, and the mechanical sectors; its classical weak-field gravity is **falsified under stated assumptions** (kept as a finding, not hidden); and it **provably does not reproduce quantum entanglement** in its present form (a counting model cannot produce amplitude interference; a future non-classical rope structure is not claimed impossible). Nothing is hidden — see [`KNOWN_LIMITATIONS.md`](KNOWN_LIMITATIONS.md).

> **Corpus state:** 139 registered claims (69 Derived, 46 Modeled, 4 EFT-constrained, 4 Conjecture, 9 Open, 7 Failed-and-kept); 124 code-backed, all passing; 57 papers. Counts regenerate from `claims.yaml` — the authority is the registry, not this line.

## Start here

- **New to the corpus?** Read [`docs/PROGRAMME_OVERVIEW.md`](docs/PROGRAMME_OVERVIEW.md) — the generated front door (assumptions, the continuum chain, computed maturity, open problems, reading order).
- **Non-specialist?** Read [`papers/rope_plain_language_guide.pdf`](papers/rope_plain_language_guide.pdf) — "The Rope Picture of the Universe," a figures-first, no-mathematics tour that flags every honest limit.
- **Reviewer or skeptic?** Read [`HOW_TO_CRITICIZE.md`](HOW_TO_CRITICIZE.md) and [`KNOWN_LIMITATIONS.md`](KNOWN_LIMITATIONS.md) first, then verify (below).

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

**How to read the honesty of the corpus.** The registry makes the `Failed` and `Open` claims as visible as the `Derived` ones. Losses are preserved as findings: the classical weak-field gravity no-go (derived deflection 0.44″ vs measured 1.75″), the PVLAS vacuum-birefringence exclusion (~570×), and the quantum boundary (Born rule, entanglement, Pauli) documented as explicit limits rather than solved problems.

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

Rigorous criticism is the most valuable contribution. See [`CONTRIBUTING.md`](CONTRIBUTING.md). The highest-value find is a claim labeled `Derived` that actually requires a hidden fitted parameter — the failure mode the entire methodology is built to prevent. Open problems are tracked in the registry and mirrored as GitHub Issues (templates in [`docs/SUGGESTED_ISSUES.md`](docs/SUGGESTED_ISSUES.md)).

## Citation

See [`CITATION.cff`](CITATION.cff) (GitHub renders a "Cite this repository" button). To cite the evolving project rather than this snapshot, use the Zenodo *concept* DOI, which always resolves to the latest version. Intellectual origin of the rope concept: Bill Gaede; this is an independent, mathematized development that departs from his formulation (see [`docs/attribution.md`](docs/attribution.md)).

## License

MIT — see [`LICENSE`](LICENSE).
