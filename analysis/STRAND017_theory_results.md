# FND-STRAND-017 — the theory session: T1 FAILED; the session stops here

Bars: analysis/STRAND017_theory_bars_LOCKED.md. Per those bars, a T1 FAIL
stops the session — the pre-registered T3 scramble experiment was NOT run,
and by the bars' own clause may not be run tonight (no cherry-picking a
favorable experiment after a failed premise).

## T1 — the amplitude-freezing claim: FAILED, decisively

The claim: pre-escape, the weave modes' amplitudes are conserved to
leading order (an almost-free quasi-periodic drive), which would have
proven the exclusion triangle by theorem and reduced escape to a
deterministic function of the initial phase vector.

The check (generator 121, 16 walkers, t = 2000, bar D <= 0.10): among the
six walkers still alive at t = 2000, the relative L1 reallocation of the
per-mode energy vector is 0.86-0.96 — the mode energies have reorganized
by ~90%, NINE TIMES over the bar. (Escaped walkers read ~3000 due to
post-escape pumping; the committed statistic over all walkers reads 3023;
the alive-only reading is 0.92; both readings FAIL by an order of
magnitude, so the verdict carries no ambiguity from that design wrinkle,
which is nonetheless noted.)

## What the failure teaches (the session's actual product)

The premise was wrong in an instructive direction: the weave is NOT a
bundle of independent oscillators wearing thermal amplitudes — it is an
INTERNALLY MIXING THERMAL NETWORK. Each site's K modes couple through the
shared chain coordinate, the spectrum is dense (spacing ~0.06), and by
t ~ 2000 the microstate has substantially forgotten its initial mode-energy
pattern.

This REFRAMES the exclusion triangle rather than deepening the mystery:
- Temperature flat (015) and total drive intensity flat (016) are what an
  EQUILIBRIUM-STATIC AGGREGATE over a mixing microstate looks like. The
  instruments measured conserved-in-distribution quantities of a bath
  behaving like a genuine bath.
- But a mixing bath with a FINITE mixing time is exactly a NON-MARKOVIAN
  bath on times shorter than that mixing time — and the measured hazard
  fall lives at t ~ 100-4000, plausibly commensurate with the mixing
  timescale the T1 check just exposed (order 10^3 at N = 24).

REFINED CANDIDATE, named for the next session (not adjudicated tonight):
SLOW-MIXING MEMORY — the escape hazard falls while the bath still
remembers its initial microstate and plateaus once mixing completes. This
makes two sharp, cheap predictions with pre-committable grammar:
(1) the mode-energy autocorrelation time tau_mix at N = 24 is of the same
    order as the hazard-fall window (measurable from short runs);
(2) the hazard becomes CONSTANT beyond a few tau_mix — testable partly on
    the ARCHIVED census (hazard beyond q90) and cleanly with one
    long-window run.
And a size consequence for free: tau_mix should shrink with N (more chain
channels mixing the modes), which would explain why the non-exponential
structure is a SMALL-box phenomenon — connecting this arc back to the
STRAND-012 crossover.

## Status of the three original framings after tonight

- (a)+(b) phase-winding determinism: the unified picture is KILLED in its
  premise (amplitudes are not frozen); whether a weaker phase-memory
  survives inside the mixing picture is subsumed into the slow-mixing
  candidate.
- (c) spectral reshaping: the T1 data show the spectrum DOES churn (per-
  mode energies reorganize ~90%) — but churn at equilibrium is not
  systematic reshaping; (c) is reframed into the mixing picture rather
  than revived as a distinct mechanism.

## Ledger

- T1 FAILED against its own pre-committed bar by 9x; the session stopped
  at its own stop-clause; T3 was not run.
- Registered status: FAILED-AND-KEPT — the corpus keeps its dead theories
  on display, and this one died usefully: the exclusion triangle now has
  a candidate EXPLANATION (equilibrium-static aggregates over a mixing
  microstate) instead of a paradox, and the mystery has a timescale to
  chase instead of a ghost.
- NEXT-ORDER, fully specified: the SLOW-MIXING SESSION — measure tau_mix
  (mode-energy autocorrelation), test the hazard plateau (archived census
  tail + one long-window run), and the N-scaling of tau_mix; blind bars,
  budget and window priced per the standing rules.
- Status: Failed (kept). Absolute scale untouched (FND-MATTER-003).
