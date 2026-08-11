# COMMISSION TSADE -- RESULTS: FORK-INHERITED; THE LABEL GAP IS NOT A NEW QUESTION

*Evaluated 2026-08-11 after bar lock
(analysis/TSADE_label_gap_bars_LOCKED.md). Benchmark:
benchmarks/foundations/tsade_label_gap.py. Bar locked before computing:
E_gap > 1.4e15 eV, the LHAASO photon anchor the corpus already carries.*

## The full candidate table (all reported, above and below the bar alike)

| candidate | kappa=50 | kappa=250 | clears 1.4e15 eV? |
|---|---|---|---|
| G1 T0 a (locking/calibration energy) | 1.63e5 eV | 1.63e5 eV | no |
| G2 hbar c / a (mesh spacing quantum) | 1.21e10 | 2.07e10 | no |
| G3 hbar c / d_c (strand thickness) | 1.06e12 | 1.06e12 | no |
| G4 hbar c / a_disp (dispersive scale) | 2.12e20 | 2.12e20 | **YES**, by 2e5x |
| G5 sqrt(T0 hbar c) (confinement scale) | 4.44e7 | 5.80e7 | no |

Four of five candidates fall BELOW the bar -- some far below. The
confinement reading G5, the one the naive expectation favoured (derive
the gap from the tube sector, as FND-056 suggested), lands at ~50 MeV,
seven orders short. The QCD intuition does not transfer: the corpus's
tube tension is anchored to hadronic physics, and hadronic scales are
nowhere near PeV.

## VERDICT: FORK-INHERITED (per the pre-committed grammar)

The candidates do not scatter -- they split cleanly along a fork the
corpus already owes: **the three-pin coverage-vs-dispersive fork**
(FND-MATTER-068; FND-REL-004 Amendment 3), which EM-RECON-025 already
carries as a MANDATORY condition of the light carrier (its registered
cost 1: the collective mode inherits the lattice dispersion, so
a_disp <= 9.3e-28 m while the coverage scale sits at 6.0e-17 m).

- On the COVERAGE reading of a, every registered gap candidate is below
  the observed photon spectrum: labels would be excitable where we look,
  and FND-056's census disturbance stands unrepaired.
- On the DISPERSIVE reading, the gap clears by five orders and the
  disturbance closes with room to spare.

**So the label-gap question is not new physics. It is the three-pin fork
wearing a new hat.** The same fork that already decides whether the
collective mode can be light at all now also decides whether that mode
has the right number of states.

## Consequences

1. **GRANT-N2-GAP is NOT NEEDED as a separate grant** on the dispersive
   branch -- the gap is a consequence of a length the corpus already
   must fix. It IS needed (or the census disturbance is fatal) on the
   coverage branch. The author's second decision therefore collapses
   into a decision the corpus already owed, which is a strict
   simplification of the ledger.
2. **The fork's stakes rise sharply.** It was already load-bearing for
   the light carrier's existence; it is now load-bearing for the light
   carrier's state count as well. Two independent obligations, one
   unresolved length.
3. **The derivation attempt FAILED in its intended form** and this is
   reported as a failure, not spun: the commission set out to derive the
   gap from the tube/confinement machinery (FND-056's named
   next-order), and G5 misses by seven orders. What replaced it -- the
   fork inheritance -- is a better result than the one sought, but it is
   not the one sought.

## Demand registered

The three-pin fork must be resolved. It now carries: the M-point's a
(coverage), the photon's dispersion bound (dispersive), the light
carrier's viability (EM-RECON-025 cost 1), and -- new here -- the label
sector's excitability and hence the photon state count. Any commission
that resolves it discharges four obligations at once. It is, by this
result, the corpus's highest-leverage open question.
