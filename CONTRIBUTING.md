# Contributing / Criticizing

This is a falsifiable research programme, open to two kinds of contribution: **building**
(new derivations, benchmarks, and closed open-problems) and **criticism** (finding where it
breaks). Both are first-class, and this repository is set up to receive both. Rigorous
criticism is especially valued because the method is built to invite it — but new results
that extend the corpus are equally welcome, under the same one rule: no hidden fitted parameters.

## Before anything else

Read **HOW_TO_CRITICIZE.md** — it maps where the programme is most vulnerable, which
assumptions are load-bearing, and which benchmark failures would collapse which sectors.
Read **KNOWN_LIMITATIONS.md** for every caveat in one place.

## To set up for development

```bash
pip install -e ".[dev]"   # installs pytest + PyYAML
pytest                      # run the regression tests
```

## To verify the corpus

```bash
pip install -e .
python tools/verify_corpus.py     # ~90s on a laptop; exit 0 iff all benchmarks pass
```

## To contribute a result

New derivations and benchmarks are welcome, not only bug reports. A contribution is
accepted on the same terms every existing claim meets: a status-labelled entry in the
registry backed by a benchmark that reruns on a laptop, with **no hidden fitted
parameters** (a `Derived` claim that secretly needs a tuned constant is the one thing
the methodology exists to prevent).

**Where the open problems are.** The registry is the to-do list. Every claim with
status `Open` is an invitation; the current set includes:

- **QB-005 — amplitude interference from rope dynamics.** The one object standing
  between the model and quantum correlations (see the measurement arc, QB-007–011).
- **The strand-level transport instantiation** — FND-KIN-001's named residual: the
  1D/2D/3D defect-level mechanism is complete; instantiate it with literal
  rope_solver knots.
- **The reaction-coherence fraction** — CHEM-DYN-002's registered next step: where
  between the coherent and incoherent sharing brackets the physical system sits.
- **FND-MATTER-003 — the absolute scale**, and **GRV-012** — the standing gravity
  verdict. The hardest, and the subject of the standing challenge below.

Browse them all with `grep "status: Open" claims.yaml`, or read the issue templates in
[`docs/SUGGESTED_ISSUES.md`](docs/SUGGESTED_ISSUES.md). The single largest open target
is **[`docs/technical/FUTURE_MODEL_PROMPT_one_fence.md`](docs/technical/FUTURE_MODEL_PROMPT_one_fence.md)** —
derive the quantum-kinetic layer that four sectors triangulate (FND-BOUND-001).

**How to submit.** In order of preference:

1. **Pull request** (preferred). Fork the repo, add your claim to `claims.yaml` (use
   `tools/add_claim.py`; never hand-edit the whole file), add your benchmark under
   `benchmarks/<sector>/`, and confirm `python tools/verify_corpus.py` exits 0. Open the
   PR against `main`; CI runs the full verifier on your branch.
2. **Issue with a patch or gist**, if you can't open a PR — include the benchmark code
   and the claim text, and note which `Open` problem it addresses.
3. **Email** for anything not yet code-ready (a derivation sketch, a partial result, a
   question about scope): **palmer100@gmail.com**. Correspondence is welcome before the
   work is benchmark-ready.

A contribution that **closes** an open problem, **registers a new negative result**
(a clean falsification, kept as a finding), or **formalizes a load-bearing theorem**
(the Γ-convergence homogenization or the gravity metric-order no-go, both slated for
Lean) is worth as much as a derivation. Honorable failure has equal standing here — the
registry treats a sharp impossibility proof exactly like a success.

## To report a problem

Open an issue. The most useful issues, in order:

1. **A "Derived" claim that actually needs a hidden fitted parameter.** This is the
   failure mode the whole methodology is built to prevent — the highest-value find.
2. **A benchmark that does not reproduce**, or reproduces something other than its
   claim. Include your platform and the command you ran.
3. **A contradiction between two papers**, or between a paper and the registry
   (`claims.yaml`, the single source of truth).
4. **A load-bearing derivation you believe is wrong.** The two theorems slated for
   Lean formalization (Gamma-convergence homogenization; the gravity metric-order
   no-go) are the highest-leverage targets.

## What this project claims and does not claim

It establishes numerical reproducibility and internal consistency, **not** physical
truth. Please frame issues accordingly: "this benchmark does not support this claim"
is actionable; "the rope hypothesis is wrong" is not, unless tied to a specific
derivation or benchmark.

## Status labels

Every claim is Derived / Modeled / EFT-constrained / Conjecture / Open / Failed.
If you can't tell what status a statement has, that itself is a documentation bug —
please report it.

## Keeping the docs in step with the registry

Some hand-maintained docs (currently `KNOWN_LIMITATIONS.md` and
`docs/STATE_OF_THE_PROGRAMME.md`) carry registry-derived facts — claim counts,
the failed-and-kept count, sector maturity — that go stale as the corpus grows.
A stale fact reads as *undersell*: a smaller, less mature, more failure-heavy
programme than the one that exists.

Those facts live inside marker comments and are regenerated by a tool, so the
editorial prose around them stays hand-written and the numbers never drift:

```
<!-- BEGIN GENERATED: corpus_stats -->
...(regenerated from claims.yaml -- do not edit by hand)...
<!-- END GENERATED: corpus_stats -->
```

- `python3 tools/sync_doc_facts.py` — refresh every generated marker region.
- `python3 tools/sync_doc_facts.py --check` — CI mode for the markers only.

To add a new generated fact, register a generator in `sync_doc_facts.py` and
wrap the target region in markers.

## One freshness gate for everything

`python3 tools/check_freshness.py` (or `make freshness`) is the single command
that catches every staleness class at once, and **changes nothing** — it only
reports, then names the fixer. It runs in CI, so a stale artifact blocks the PR
rather than reaching a reviewer. It checks:

1. **Generated docs current** — `PROGRAMME_OVERVIEW`, `ROADMAP`, dependency graph
   actually re-run (fix: `make overview roadmap graph`).
2. **Marker fact-blocks current** — via `sync_doc_facts.py`.
3. **Version metadata agrees** — `CITATION.cff` == `pyproject.toml` == latest
   release note.
4. **No broken references** — every benchmark/paper in `claims.yaml` exists.
5. **Paper catalog complete** — every `papers/*.pdf` appears in `docs/PAPERS.md`.
6. **Rendered PDFs current** — no paper PDF older than its `_sources` docx.
7. **No orphaned generated docs** — a file whose header claims it is generated, but which names a generator that does not exist, is flagged as a likely stale former output (the trap that left a stale `docs/roadmap.md` behind when a generator target was renamed). Case-collision twins (`ROADMAP.md` vs `roadmap.md`) are flagged too.

When you add a paper, catalog it in `docs/PAPERS.md`; when you bump the version,
bump it in all three places; when you edit a paper's docx, re-render its PDF.
The gate will remind you if you forget.
