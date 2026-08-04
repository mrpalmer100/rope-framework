# FND-STRAND-023 — exclusivity at the thermal point: bars locked first

Date: 2026-08-04. Commission: FND-STRAND-022's named redesign. The
question, restated with 022's finding in hand: at the REGISTERED thermal
operating point, where the bath supplies the concentration mechanism,
does one quantum's worth of injected signal energy fund at most one
click — and is that exclusivity attributable to the signal's finiteness
(scarcity of concentrations) rather than to the medium's generic
reluctance to multi-seed?

## The model, committed

Registered composite verbatim (kt = 0.64, K = 16, c0 = 0.35, dt = 0.02),
N = 96, T = 0.40 (the thermal point), base tilt h = 0.30 (the registered
silent tilt), window W = 2000 units. Signal: the delocalized fundamental
mode, pphi_n += A cos(2 pi n/N), E_sig = A^2 N/4 — one extended coherent
excitation over every site, as in 022.

## Observables (the 022 persistence rule, executed)

FIRE: at least one cluster of sites with phi > pi present at BOTH
t_first + 25 AND t_first + 50 (t_first = first instantaneous crossing).
n_ev := min(cluster count at +25, cluster count at +50) — merging can
only reduce, transients vanish. All bars consume FIRE and n_ev only;
instantaneous crossings alone decide nothing.

## Calibrations, procedures committed with bracket pricing (lesson 4)

E50 := signal energy at P(FIRE) = 0.5 in W. ONSET PRE-ESTIMATE, on the
face: at h = 0.30 the thermal barrier is a few units and injection
offsets it, so E50 is expected at order 1-10 units; the committed grid
E_sig in {1, 2, 4, 8, 16} (S = 24/point, generators 191-195) BRACKETS
that estimate by construction on both sides. Linear interpolation between
bracketing points; if unbracketed despite the pricing, the session stops
and says so (no ad-hoc extension this time — the grid was priced).

h' (the rate-matched thermal comparator): from {0.40, 0.45, 0.50} at
S = 24 each (generators 196-198), the point whose P(FIRE) is nearest
0.5 is the comparator; reported, not interpolated.

## B0 — the baseline

No injection, h = 0.30, S = 48 (generator 190): P(FIRE) <= 0.10. FAIL ->
the window is re-locked shorter in an addendum before anything else.

## B1 — exclusivity at one quantum

At E_sig = E50 (S = 48, generators 201-202): m_sig := P(n_ev >= 2 | FIRE).
- EXCLUSIVE: m_sig <= 0.15.
- NOT EXCLUSIVE: m_sig >= 0.40.
- INTERMEDIATE: as measured.

## B2 — attribution (the comparator's job)

m_th := P(n_ev >= 2 | FIRE) on the h' comparator ensemble (S = 48,
generators 203-204, no injection).
- ATTRIBUTED: B1 EXCLUSIVE and m_sig <= 0.5 x m_th — the signal-driven
  channel is MORE exclusive than rate-matched thermal clicking; the
  finiteness of the shared quantum is doing work.
- GENERIC: B1 EXCLUSIVE but m_th also <= 0.15 — the medium rarely
  multi-seeds at this size/window regardless; exclusivity is real but
  not attributable to signal finiteness on this design; registered
  EXCLUSIVE-MECHANISM-UNRESOLVED.
- As measured otherwise.

## B3 — the two-quanta alibi (mandatory, as 022 taught)

At E_sig = 2.5 x E50 (S = 48, generators 205-206):
P(n_ev >= 2 | FIRE) >= max(0.25, 2 x m_sig). Multis MUST appear when the
energy budget allows, or the persistence instrument is the suspect and
an audit voids B1 (pre-stated).

## Promotion criterion

PROMOTE "one quantum, one click at the thermal point" iff B0 passes, B1
EXCLUSIVE, B3 alibi holds. B2 sets the mechanism language: ATTRIBUTED
promotes the scarcity-of-concentrations reading; GENERIC promotes only
the phenomenon with the mechanism explicitly open. Consequence if
promoted with ATTRIBUTED: Prediction 14 gains its exclusivity clause
with mechanism; the plain-double-slit wave-plus-dot account completes.
Refutations and voids registered at full volume per house rule.

## Honesty clauses

- Model, observables, calibration procedures with pricing, generators,
  thresholds: all fixed above. Which-path/delayed-choice/eraser remain
  out of scope.
- Status ceiling: Modeled. Absolute scale untouched (FND-MATTER-003).
