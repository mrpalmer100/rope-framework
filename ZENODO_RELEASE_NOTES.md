# Rope Solver Corpus — Release Notes

**Version 2.2.1 · 130 registered claims · 116 rerunnable benchmarks (all passing)**

## What this is

A machine-verified research corpus developing Bill Gaede's Rope Hypothesis into
falsifiable, independently checkable form. Every claim carries a status label
(Derived / Modeled / EFT-constrained / Conjecture / Open / Failed) and, where
code-backed, a benchmark any reader can rerun. The corpus establishes numerical
reproducibility and internal consistency — **not** physical truth. Whether the
underlying physics is correct is exactly what external scrutiny is invited to decide.

## Verify it yourself (one command, ~90 seconds, commodity hardware)

```bash
pip install -e .
python tools/verify_corpus.py     # runs every registry benchmark; exit 0 iff all pass
```

No GPU, no cluster, no large data. Every benchmark runs on a laptop in seconds;
this "laptop invariant" is a deliberate methodology choice that keeps the corpus
independently checkable.

## How to read the honesty of the corpus

The value here is not that the model succeeds everywhere — it doesn't. The value
is that successes and failures are labeled by the same standard and kept side by
side. Two kinds of entries deserve a reader's first attention:

### Kept losses (7 Failed claims, preserved as findings)

These are results the framework was corrected by, retained rather than hidden:
- **EM-011**: Cosmological alpha-variation test FALSIFIES the strong (local density-tracking) form of the rope-density hypothesis for the EM coupling
- **GRV-009**: FAILED CANDIDATE: per-strand STRAIN conditioning -- fully specified by session primitives (k, P-VOL, torsion~r^4) with zero freedom -- gives gamma = -
- **GRV-010**: FAILED: mode-bath conditioning -- after correcting my own posed estimates (mean strain relaxes; no inertia renormalization in the elastic Lagrangian; 
- **PM-002**: Lepton ratios with the model's own Weinberg angle
- **PM-004**: The lepton mass spectrum does NOT fall out of the corpus knot/soliton excitation physics without tuning; lepton masses are irreducible inputs (negativ
- **QB-003**: Present counting form does not reproduce quantum entanglement
- **QB-004**: One-loop fluctuation mass mechanism (log-det ≈ -1.29 vs electron ≈108)

The classical gravity no-go (weak-field deflection 0.44 vs measured 1.75 arcsec)
and the PVLAS vacuum-birefringence exclusion (naive identification excluded ~570x)
are the load-bearing examples: the audit sided against the theory, on the record.

### Open frontiers (8 Open + 4 Conjecture claims)

Named, not buried — the honest edge of the programme, including the atomic-scale
derivation (blocked on declared missing inputs), amplitude interference, and
several numerical coincidences (Koide, Weinberg angle) held at Conjecture pending
derivation-or-demotion.

## Status distribution

| Status | Count | Meaning |
|--------|-------|---------|
| Derived | 69 | follows from stated mechanics |
| Modeled | 39 | reproduces data with declared inputs |
| EFT-constrained | 3 | bounded by effective-theory limits |
| Conjecture | 4 | proposed, not derived |
| Open | 8 | registered unsolved problem |
| Failed | 7 | falsified, kept as a finding |

## Where to start

1. `docs/PROGRAMME_OVERVIEW.md` — generated front door (assumptions, maturity, reading order)
2. `claims.yaml` — the machine-readable registry (the authority for every count)
3. `CHANGELOG.md` — the full revision history, including every registered correction
3b. `KNOWN_LIMITATIONS.md` — every load-bearing caveat in one place
3c. `HOW_TO_CRITICIZE.md` — a map of where the programme is most vulnerable (read this if you are a reviewer)
4. `docs/rope_plain_language_guide.docx` — **"The Rope Picture of the Universe"**, a figures-first, no-mathematics tour of the whole framework; the best entry point for a non-specialist reader
5. `docs/rope_theory_of_chemistry.docx` — the most complete single sector (start with its one-page roadmap)


## Scope of this release

This is a **versioned research snapshot**, not a claim of peer-reviewed acceptance. It
records the state of an ongoing, self-directed research programme at one point in time,
with every claim labeled by status and every code-backed claim independently rerunnable.
Publication here asserts reproducibility and internal consistency; it does **not** assert
that the underlying physics is correct. That question is exactly what external scrutiny
is invited to decide. Subsequent versions (v2.2.1, v2.3, ...) will be published as
separate snapshots so the scientific history is preserved rather than overwritten.

See `KNOWN_LIMITATIONS.md` for every load-bearing caveat and `HOW_TO_CRITICIZE.md` for a
map of where the programme is most vulnerable.

## Citation

**DOI (this version):** https://doi.org/10.5281/zenodo.21430784  
**Author:** Mark Palmer (https://orcid.org/0009-0007-2454-5573)  
To cite the evolving project rather than this snapshot, use the Zenodo *concept* DOI ("Cite all versions" on the record page), which always resolves to the latest release.


See `CITATION.cff`. Intellectual origin of the rope concept: Bill Gaede; this is an
independent, mathematized development that departs from his formulation (see
`docs/attribution.md`).
