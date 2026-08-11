# COMMISSION HE-2 -- RESULTS: BRIDGE-LANDS; EM-016's LEDGER EMPTIES, AND EM-020 IS CORRECTED

*Adjudicated 2026-08-11 after bar lock
(analysis/HE2_sigma_bridge_bars_LOCKED.md). Benchmark:
benchmarks/em/he2_sigma_bridge.py. The bar authorised correcting EM-020
in advance, and it is corrected.*

## H1 -- definitional identity

EM-RECON-014 defines SIGMA = T0 n_L and calls it "the network's vacuum
TENSION DENSITY". That is a definition in registered quantities, not an
independent constant: the mesh HAS a line density (spacing a, three
strand families), so n_L = 1/a^2 per family and 3/a^2 in total. Both
readings computed, neither chosen by hand:

| kappa | a [m] | T0 [J/m] | T0/a^2 | 3T0/a^2 |
|---|---|---|---|---|
| 50 | 1.630e-17 | 1599 | 6.02e36 | 1.80e37 |
| 250 | 9.533e-18 | 2734 | 3.01e37 | 9.02e37 |

**Sigma_EM's own definition, evaluated on the registered mesh, gives
6.0e36 - 9.0e37 J/m^3.** No new constant is required.

## H2 -- what the 1e25 actually is (the decisive check)

Read from EM-RECON-014's own source rather than inferred from the quoted
value. The source derives SIGMA >= eps0 E_S^2 / g*^2 from the
requirement that any classical rope quartic have its onset at or above
the Schwinger scale, giving 4e24 - 1.5e25 J/m^3, and then adds:
"EQUALITY = the identification, in which case ATLAS has MEASURED SIGMA."

**The 1e25 is a LOWER BOUND, saturated by an assumed equality. It was
never a measurement** -- and the assumption behind the equality is
exactly what QGATE-007 withdrew (unpolarized light-by-light carries no
structure information; the rate is degenerate with normalization).

**Therefore the "10.6-order gap" is not a discrepancy between two
quantities. It is the distance between a lower bound and the actual
value -- and a value eleven orders ABOVE a lower bound SATISFIES it.**

## H3 -- consistency under substitution

Nonlinearity onset E* = g* sqrt(SIGMA/eps0), all eight combinations of
{kappa floor} x {n_L convention} x {g* in [1,2]}: every one clears the
Schwinger requirement by 5-6 orders (E*/E_S = 6.2e5 to 4.8e6). The
weaker laser bound (SIGMA > ~1e15) clears by 21 orders.

**Independent cross-check, and it is the strongest evidence here:**
FND-031's downstream sweep already computed E_crit = 2.0e23 V/m under
the PINNED Sigma and registered it as 1.5e5x above Schwinger --
the same order as the values above. **The corpus had already run the EM
nonlinearity confrontation on the pinned Sigma family** without anyone
noticing that this discharged the EM sector's calibration blocker.

## VERDICT: BRIDGE-LANDS

Sigma_EM is not a free constant. It is T0 n_L on the registered mesh,
its value follows from the pinned chain, and the number that made it
look independent was a bound saturated by a withdrawn assumption.

## What EM-020 got right and wrong (required by the bar, by name)

**RIGHT, and it remains valuable:** that the quoted values differ by
10.6 orders; that Sigma_EM's ATLAS pin is superseded; that prior
statements conflating the two were ambiguous; and that the relabel could
not honestly proceed before the object was identified. Insisting on that
sequence is what made this commission possible.

**WRONG:** the DIFFERENT-OBJECTS verdict. EM-020 compared quoted VALUES
and inferred distinct quantities. It should have compared DEFINITIONS
and asked what kind of number the 1e25 was -- which its own bar had
gestured at but did not require. They are the same physical quantity;
one quoted figure was a bound. The verdict is corrected here.

The methodological lesson, which is the more transferable half: **a
numerical gap between two quantities is evidence of distinct objects
only if both numbers are of the same epistemic kind.** Comparing a bound
to a value and concluding "different objects" is a category error, and
it is now on the record as one this corpus made and caught within the
same session.

## Consequences

- **EM-016's blocker (i) discharges BY DERIVATION.** Its ledger, which
  stood at four this morning, is EMPTY.
- **The approved relabel is no longer needed.** It was the fallback for
  a constant that turned out not to be free. Nothing is relabelled;
  nothing needs to be.
- **EM-016's GRADE is now a live question, and this commission does not
  touch it.** Grading is the author's. What can be said is that all four
  registered obstacles are discharged by derivation (EM-017, EM-018,
  EM-019, and this claim), with the honest residuals recorded in each:
  EM-019's coefficient is matched rather than independently derived and
  its uniqueness assumes locality; and Sigma_EM's value inherits the
  kappa_pack floor spread and every conditionality of the pinned chain,
  which is a real conditionality and travels with any upgrade.
