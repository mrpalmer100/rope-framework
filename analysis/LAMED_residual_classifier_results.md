# COMMISSION LAMED -- RESULTS: DIFFUSE, WITH THE CHANNELS NAMED

*Two rounds, both as-run. Bars: analysis/LAMED_residual_classifier_bars_LOCKED.md
plus analysis/LAMED_round2_addendum_LOCKED.md. Benchmark:
benchmarks/nuclear/lamed_residual_classifier.py. Data: AME2012 evaluated
masses, 2398 nuclides A >= 12.*

## Round 1 (as locked, as run): the baseline was the finding

The corrected-BOTH NUC-018 variant produced a residual of rms 110 MeV
(8.1 percent of binding, mean -91), out-of-sample dominated by a smooth
A^(1/3) term (univariate R^2 = 0.874). Verdict under the grammar:
STRUCTURE-FOUND -- but the structure is BASELINE MISCALIBRATION, stated at
full volume: this round measured, across the full table, what NUC-018's own
note registered on seven nuclei (the corrected-both variant degrades). The
stale-value tripwire caught the chain one commission late; the round stands
as a table-scale confirmation of NUC-018's internal ranking, not as
residual physics.

## Round 2 (registry-best baseline, per NUC-018's own table): the chartered question

Baseline: d0 = 2.026, ratio 1.108, a_C = 0.772, a_V = 15.987 (Ca-40, once),
a_A = 19.85 derived. Residual: mean -6.4 MeV, rms 13.7 MeV -- the few-MeV
regime the queue chartered.

| Descriptor | univariate oos R^2 | joint coef (train) | t | sign-stable |
|---|---|---|---|---|
| D1 shell (valence distance) | 0.017 | -0.152 MeV/unit | -5.1 | yes |
| D2 pairing parity | 0.011 | +1.41 MeV | +4.5 | yes |
| D3 curvature A^(1/3) | 0.002 | +5.97 | +18.7 | yes |
| D4 linking density Z/A | 0.294 | +64.1 | +7.8 | yes |
| D5 alpha geometry | 0.007 | +3.5 | +1.3 (not retained) | yes |
| D6 isospin quartic | 0.460 | -46.8 | -25.3 | yes |

Joint out-of-sample R^2 = 0.581 vs the pre-committed 0.6. Swap test PASS.
Permutation: null max 0.126 over 1000 draws, p < 0.001. No univariate
descriptor reaches 0.5.

## VERDICT: DIFFUSE (per the pre-committed grammar; the bar is the bar)

The residual is real, statistically unambiguous, and MULTI-CHANNEL: no
single rope-native descriptor owns it, and the joint model falls 0.019
short of the pre-committed threshold. That near-miss is reported as a
near-miss, not promoted.

## What the channels say (the commission's usable content)

1. **The macroscopic channels dominate.** D6 (isospin quartic, negative:
   the derived quadratic asymmetry under-prices high-isospin cost -- the
   registered a_A lacks a surface-symmetry/quartic companion) and D3/D4
   (curvature and linking density: the droplet functional is missing its
   next geometric orders). The bulk of the few-MeV residual is SMOOTH
   physics adjacent to already-derived terms -- reachable by the same
   methods that derived a_A, and now sized: ~6 MeV rms of the 13.7.
2. **Pairing recovered out of sample at +1.41 MeV** (even-even vs odd-odd,
   sign-stable, t = 4.5): the A-averaged magnitude of the empirical
   12/sqrt(A) term. This answers NUC-024's mismatch constructively -- the
   table wants ~1.4 MeV on average, and NUC-024's A-independent derived
   term should be confronted against exactly that number.
3. **Shell structure is present but weak through this proxy** (-0.15 MeV
   per valence unit, t = -5): the linear magic-distance descriptor
   captures the declared quantum boundary faintly; the shell channel is
   real but needs a registered occupancy structure, not a distance proxy.
4. **D7 (reconnection configuration count) remains UNDERSPECIFIED** -- the
   same acquisition-target grammar as FND-051: no registered computable
   form exists.

## Inverted demands / named next-orders

- Derive the surface-symmetry (or quartic) isospin correction by the
  NUC-A/B method; the classifier prices it at coefficient ~-47 on
  (N-Z)^4/A^3 out of sample, a pre-sized target.
- Derive the curvature term (A^(1/3), coefficient ~+6 MeV) from the same
  droplet geometry that produced the surface term.
- Confront NUC-024's derived pairing magnitude against the out-of-sample
  +1.41 MeV measured here.
- The Fermi-gas explanation stays falsified (NUC-010, untouched): nothing
  in this commission reopens it.
