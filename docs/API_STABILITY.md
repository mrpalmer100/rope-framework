# API stability and versioning policy (from 2.0)

`rope_solver` 2.0 marks the transition from "implementation of individual papers"
to a **reference implementation** with stability guarantees. Published results
cite this package by version and by benchmark ID; those citations must stay valid.

## What 2.0 freezes

- **Public APIs.** The signatures of public functions (those without a leading
  underscore, listed in [`API.md`](API.md)) are stable. Within 2.x they may gain
  optional keyword arguments with defaults, but existing call signatures and
  return types do not change.
- **Benchmark numbering.** The IDs in [`BENCHMARKS.md`](BENCHMARKS.md) (G-001,
  EM-002, P-004, ...) are frozen. An ID always refers to the same quantity. New
  benchmarks get new IDs; existing IDs are never renumbered or repurposed.
- **Regression philosophy.** Every cited number is produced by an installed
  function with a regression test pinning it. The three-command heartbeat
  (validation / physics+EM / reproduction) is the contract; CI runs it on every
  change.
- **Reproducibility of published results.** A result computed with 2.x is
  reproducible with any later 2.y (y >= x). The committed `benchmark_results/`
  capture the expected outputs.

## Versioning (semantic, from 2.0)

| Change | Version bump | Example |
|---|---|---|
| New module, new benchmark ID, new optional kwarg, new prediction | **minor** (2.0 -> 2.1) | adding a nuclear-physics module |
| Bug fix that does not change a published number | **patch** (2.1.0 -> 2.1.1) | docstring fix, internal refactor |
| Bug fix that DOES change a published number | **minor**, with the change documented in CHANGELOG and the affected benchmark IDs listed | correcting a solver convention |
| Removing/renaming a public function, renumbering a benchmark, changing a return type | **major** (2.x -> 3.0) | only with strong justification |

## What this enables

After 2.0, a paper can say "computed with rope_solver 2.x, benchmark G-002" and
that statement remains precise and reproducible as the package evolves to 2.1,
2.2, and beyond — without breaking earlier papers. Future physics is added; the
foundation under prior results does not move.

## What is explicitly NOT guaranteed

- **Physical correctness.** Stability of the API is not a claim that the physics
  is right. The package establishes numerical reproducibility, not physical
  truth. See the [open-problems registry](roadmap.md) for what is unsolved,
  conjectural, or falsified.
- **Private functions** (leading underscore) and internal implementation details
  may change at any time.
