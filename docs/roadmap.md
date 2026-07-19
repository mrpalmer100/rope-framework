# The Rope Programme — Computed Sector Roadmap

*Maturity is computed by `tools/build_roadmap.py` from the status and benchmark
coverage of each sector's claims in `claims.yaml`. It is not hand-assigned, so it
cannot drift from the corpus. Readiness labels are cross-checked against computed
maturity; mismatches are flagged below.*

| Sector | Computed maturity | Stated readiness | Claims | Basis |
|---|---|---|---:|---|
| Microscopic Mechanics & Foundations | **Mature** | Ready for expert review | 24 | 19/24 derived/EFT, 21/24 benchmark-backed |
| Renormalization / EFT | **Mature** | Ready for expert review | 1 | 1/1 derived/EFT, 1/1 benchmark-backed |
| Electromagnetism | **Developing** | Ready for expert review | 35 | 16/35 solid, 35/35 benchmarked |
| Classical Optics | **Mature** | Ready for expert review | 10 | 10/10 derived/EFT, 10/10 benchmark-backed |
| Thermodynamics | **Mature** | Ready for expert review | 5 | 4/5 derived/EFT, 4/5 benchmark-backed |
| Condensed-Matter Analogues | **Developing** | Conditional (analogue-level) | 1 | 0/1 solid, 0/1 benchmarked |
| Gravity (weak field) | **Developing** | Developing (weak-field metric matched, not derived; needs more benchmark-backed claims) | 20 | 9/20 solid, 20/20 benchmarked |
| Solitons & Knot Spectrum | **Mature** | Ready with caveats (not identified with particles) | 1 | 1/1 derived/EFT, 1/1 benchmark-backed |
| Electroweak (Weinberg angle) | **Exploratory** | Exploratory (conjectural) | 1 | 1/1 conjectural |
| Particle Masses | **Developing** | Internal / open problem | 5 | 2/5 solid, 3/5 benchmarked |
| Gauge Geometry (unification) | **Mature** | Ready for expert review | 6 | 5/6 derived/EFT, 4/6 benchmark-backed |
| Quantum Boundary (Bell) | **Mature (boundary)** | Ready (documented boundary / negative result) | 6 | 2 derived + 2 failed/1 open, documented limit |

## ⚠ Readiness-vs-evidence flags

These sectors state an external readiness that the computed maturity does not yet fully support. This is a prompt to either add benchmark backing or soften the readiness label — not a claim the physics is wrong.

- **Electromagnetism**: stated *Ready for expert review*, but computed *Developing* (16/35 solid, 35/35 benchmarked). Add benchmark-backed claims or relabel.

### How maturity is computed (auditable rules)
- **Mature (boundary)**: ≥half claims Failed/Open *with* ≥1 solid result — a documented limit (e.g. the Bell/quantum boundary). A strong negative result.
- **Mature**: ≥2/3 claims Derived/EFT-constrained *and* ≥half benchmark-backed.
- **Conceptually strong, thin backing**: ≥half solid statuses but <half benchmark-backed — a flag to add executable backing.
- **Exploratory**: ≥half claims Conjecture.

