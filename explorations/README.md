# explorations/ — plausibility sketches and model-building notes

**Nothing in this directory is a validated result.** These are exploratory
notes: plausibility checks, tuned consistency windows, and model-building
sketches kept for future reference. They are deliberately SEPARATE from:

- the validated papers in `docs/`,
- the registered claims in `claims.yaml` (which carry explicit status labels),
- the benchmark suite in `benchmarks/` and `validation/`.

Each file here states its own assumptions and honest limits inline. Do not cite
anything in this directory as a derivation or a result. Where an exploration
connects to a registered claim, it references the claim id (e.g. FND-MATTER-002,
FND-MATTER-003) so the validated status is easy to look up.

## Contents
- `atom_scale_plausibility.md` / `.py` — hydrogen atom size & mass-ratio
  plausibility under an explicit, tuned assumption set (rope count N,
  microstructure scale a). Ballpark-consistent with the Bohr radius and mass
  ratios; NOT a derivation (see FND-MATTER-003 for the blocking obstruction).
