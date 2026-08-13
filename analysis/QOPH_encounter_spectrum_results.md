# COMMISSION QOPH -- THE ENCOUNTER SPECTRUM: RESULTS

Executed 2026-08-12 under analysis/QOPH_encounter_spectrum_bars_LOCKED.md.
Benchmark: benchmarks/foundations/qoph_encounter_spectrum.py.

## Verdict (locked grammar): RESOLVED

The C3 tension is an artifact of the ka = 1 evaluation choice. Both
mode-based registered encounter scales produce demanded windows that
OVERLAP the survival floor, and the incumbent transit scale sits within
the L1 conversion band of it. No evaluated route excludes overlap.

## The routes, all three evaluated (closed at lock, none selected by outcome)

The exact scaling law g_demanded = g_demanded(ka=1) x ka was verified
against FND-072's closed form to 1e-12 before any window moved.

| route | ka | demanded g window | vs survival [0.395, 0.460] |
|---|---|---|---|
| R1 segment fundamental | pi | [0.256, 0.831] | OVERLAP (floor fully inside) |
| R2 kink width a/w | 1.594 | [0.130, 0.422] | OVERLAP (marginal, top edge) |
| R3 transit (incumbent) | 1.000 | [0.082, 0.265] | disjoint by 1.49x, WITHIN L1 |

Joint windows where overlap exists:
- R1: g in [0.395, 0.460], p there [1.97e-03, 2.67e-03] (mid-band).
- R2: g in [0.395, 0.422], p there [7.56e-03, 8.60e-03] (band's top edge).

## What this does and does not establish

DOES: the reconnection demand and matter-stability survival are
COMPATIBLE constraints on the same per-pair ratio under either of the
two registered mode-based encounter scales. FND-073's C3 debt is
discharged: the tension no longer forces a choice between the NUC-030
adoption and the survival band. The NUC-030 falsifier does NOT fire.

DOES NOT: select an encounter scale. The three routes span pi in ka and
the corpus registers no dynamics that privileges one. The demanded
window is now honestly a FAMILY, [0.082, 0.265] x ka with
ka in [1, pi], and any future g determination must be confronted against
the family, not against a chosen member. The route selection is itself
a named acquisition: a derivation of which wavenumbers actually arrive
at a crossing (the true spectrum, not a characteristic scale) would
collapse the family to a window again.

## Displayed, NOT adopted (resemblance rule; FND-070 discipline)

The overlap windows sit AT the survival floor: a single contrast
g ~ 0.40-0.46 would simultaneously satisfy reconnection and place matter
at its own survival threshold -- an echo of EM-RECON-017's registered
placement of matter AT the coverage threshold (FND-070's corrected
reading). Whether these are the same marginality is a question with no
dependency path yet. Displayed so the refusal is auditable; adopting it
on resonance would be exactly the error the house rules name.

## Guard disclosure follow-through

G1 (the a/w adjacency noticed pre-lock): R2 was evaluated as one of
three locked routes and its overlap is the MARGINAL one; the verdict
does not rest on it (R1 overlaps robustly). The pre-lock noticing did
not select the outcome.
G2: the mesoscopic 1/p adjacency was not touched. The scale001 seal was
not opened. Reserved for RESH.
