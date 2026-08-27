# The Rope Programme — Overview

*The front door to the corpus. This document is **generated** from `claims.yaml` and the computed roadmap by `tools/build_overview.py`, so its statistics, maturity table, and open-problems list stay in sync with the corpus by construction.*

Programme credit: the core Rope Hypothesis is due to Bill Gaede; this corpus develops and formalises it.

---

## What this programme is

The Rope Hypothesis is a speculative classical model in which interactions are carried by physical strands under tension. This corpus develops its **classical continuum sector** into a reproducible research programme: a coherent chain from microscopic mechanics up through electromagnetism, optics, and thermodynamics, with every principal claim assigned a status and, wherever possible, backed by an executable benchmark.

The programme's discipline is its defining feature: **derived results, empirical inputs, and open problems are kept strictly separate**, corrections and negative results are preserved as visibly as successes, and the mathematics is kept distinct from the ontology it proposes.

## Corpus at a glance (generated)

- **Bundled papers:** 64
- **Reproducible benchmarks:** 629
- **Registered claims:** 0 (0 code-backed and machine-verified)
- **Claim status distribution:** 

Verify it yourself in one command: `make verify` (runs every benchmark the registry references) or `python tools/verify_corpus.py`.

## The classical continuum chain (the strongest core)

The programme's spine is a single geometric structure developed level by level. Each link is a Mature, benchmark-backed sector:

```
Microscopic Mechanics
      -> Homogenization (Gamma-convergence)
            -> Effective Field Theory
                  -> Electromagnetism
                        -> Classical Optics -> Interface Optics
      -> Defect Theory (2D + 3D)  [shares the same functional]
      -> Statistical Mechanics    [BKT = defect-gas unbinding]
  All unified by: Gauge Geometry (bundle -> connection -> curvature -> topology)
```
The gauge-geometry paper is the mathematical reference showing these are one structure; the machine-readable dependency graph (`docs/dependency_graph.txt`) encodes the links claim by claim.

## Sector maturity (computed)

Maturity is **computed** from each sector's claim statuses and benchmark coverage, not hand-assigned. Readiness is cross-checked against it; there are currently no readiness-vs-evidence flags.

| Sector | Computed maturity | Claims | Derived | Benchmarked |
|---|---|---:|---:|---:|

## Suggested reading order

For a first read of the corpus:

1. **This overview** — assumptions, scope, maturity, open problems.
2. **Topology and Gauge Geometry Underlying the Rope Programme** — the mathematical backbone; why bundles, connections, curvature, and topology recur.
3. **Microscopic Mechanics** — the endpoint mechanics the chain starts from.
4. **A Gamma-Convergence Derivation for the Rope Medium** (homogenization) — how the discrete model becomes the continuum functional.
5. **Electromagnetism** and **Classical Optics** — the strongest, most self-contained physical sectors.
6. **Scope and Limits** — what the programme does not claim, especially the quantum boundary.

## Open problems and boundaries (generated)

The programme marks where it does not (yet) claim to explain nature. These are surfaced directly from the registry:

## How to evaluate this corpus

- **Dependency graph:** `docs/dependency_graph.txt` — what rests on what.
- **Claim registry:** `claims.yaml` — every claim's status, paper, and benchmark.
- **Computed roadmap:** `docs/ROADMAP.md` — sector maturity, auto-flagged if any readiness outruns its evidence.
- **One-command verification:** `make verify` — runs every code-backed claim's benchmark.
- **Heartbeat:** `make heartbeat` — the core validation runs (currently 75/75 + 10/10 + 6/6).

The programme's strongest posture is not any single prediction; it is that the classical core can be independently audited, sector by sector and claim by claim, and that its boundaries are stated rather than blurred.

