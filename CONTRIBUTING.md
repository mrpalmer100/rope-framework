# Contributing / Criticizing

This is a falsifiable research programme. Rigorous criticism is the most valuable
contribution you can make, and this repository is set up to receive it.

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
