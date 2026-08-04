# FND-STRAND-028 — delayed choice derived as a non-paradox

Date: 2026-08-04. Commission: the roadmap's Phase D (plain Wheeler
delayed choice, no entanglement — the entangled eraser stays fenced at
QB-003). The claim: in the wave-plus-whole-delivery ontology, Wheeler's
paradox does not arise, choice-timing invariance is a one-line theorem,
and the quantitative duality relation V^2 + D^2 = 1 follows as
arithmetic.

## The setup, and where the paradox lived

Mach-Zehnder: a quantum enters splitter BS1; arms a and b with relative
phase phi; the experimenter chooses — possibly AFTER the quantum has
passed BS1 — whether the recombining splitter BS2 is present (wave
configuration: interference fringes) or absent (path configuration:
50/50 clicks on the arm detectors). Wheeler's framing: the photon "must
decide at BS1" whether to be a wave (both arms) or a particle (one
arm), so a late choice appears to reach back and fix that decision.

The paradox is a paradox FOR TRAJECTORY ONTOLOGIES. It requires a
variable — "which arm the particle took" — that exists at BS1 and that
the later choice could retroactively determine.

## T1 — the ontology has no such variable (the dissolution)

In this framework, propagation is untouched by Grant 3: the torsional
wave takes BOTH arms, every time, in every configuration. Nothing
decides anything at BS1 because there is nothing to decide: no
trajectory variable exists at any time. The only event in the story is
ABSORPTION, and Grant 3 acts there: the quantum is delivered whole to
exactly one channel, with Born weights given by the channel energies of
the apparatus AS CONFIGURED AT ABSORPTION TIME.

## T2 — choice-timing invariance (the theorem, one line)

Since delivery happens at absorption, click statistics depend ONLY on
the channel-energy configuration at absorption. The choice (insert or
remove BS2) fixes that configuration; WHEN the choice is made — before
emission, mid-flight, a nanosecond before absorption — is irrelevant
provided it precedes absorption, because the wave it reconfigures has
not yet been absorbed. Predicted statistics for early and delayed
choice are IDENTICAL, with zero retrocausality, matching the
experimental record (delayed-choice implementations find no dependence
on choice timing). What the late choice determines is the future
disposition of a wave still in flight — ordinary causation, running
forward.

Wave configuration (BS2 in): output channel energies
E_c = E cos^2(phi/2), E_d = E sin^2(phi/2); Grant 3 gives fringes with
visibility V = 1. Path configuration (BS2 out): arm channel energies
E/2 each; one click, 50/50 — "which-path statistics" WITHOUT a
which-path fact: delivery-to-one-arm-detector is not
travel-down-one-arm. The particle-like record is detector bookkeeping,
as the whole campaign established.

## T3 — the duality relation as arithmetic (the bonus)

Make the choice CONTINUOUS: BS2 present with reflectivity R (R = 1/2
is the full wave configuration; R = 0 removes it). The output channel
energies are

  E_c/E = R + (1-2R)... [worked form]  computed exactly in the
  benchmark from the two-arm amplitudes: with arm amplitudes
  sqrt(E/2) each and phase phi, port c receives
  E_c(phi) = E [ 1/2 + sqrt(R(1-R)) cos phi ].

Fringe visibility: V = 2 sqrt(R(1-R)). Path distinguishability (the
best arm-attribution the port statistics allow): D = |1 - 2R|. Then

  V^2 + D^2 = 4R(1-R) + (1-2R)^2 = 1   EXACTLY, for every R.

The Englert-Greenberger-Yasin duality relation — usually presented as a
deep quantum complementarity bound — is HERE a two-line algebraic
identity about how a fixed energy budget partitions between an
interfering and a non-interfering component at a partial recombiner.
Complementarity, in this ontology, is energy bookkeeping.

## Scope, honesty, status

- PLAIN delayed choice only. The delayed-choice QUANTUM ERASER uses
  entangled pairs and erasure correlations that are CHSH-adjacent;
  QB-003's no-go fences it, and this claim does not touch it.
- The dissolution is only as good as the ontology's two commitments:
  waves always both arms (propagation sector), delivery whole at
  absorption (Grant 3). Both are registered; the claim is Derived
  conditional on Grant 3.
- Benchmark: exact port energies vs phi and R; Monte Carlo Grant-3
  sampling with EARLY vs DELAYED configuration choice (identical
  distributions, KS-level); V(R) and D(R) measured from sampled
  statistics; V^2 + D^2 = 1 across R; wave config matches cos^2; path
  config 50/50 with zero coincidences.
- Absolute scale untouched (FND-MATTER-003).
