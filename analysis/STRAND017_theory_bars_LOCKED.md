# FND-STRAND-017 — the theory session: deterministic finite-N escape
# Bars locked before any derivation is checked or any run is made

Date: 2026-08-03. Commission: FND-STRAND-016's pre-committed consequence.
Brief: the smallest box's non-exponential escape is invisible to
temperature, drive intensity, and every measured early-state covariate.
Decide between the three named framings — (a) phase-pattern frailty,
(b) recurrence-structured deterministic first-passage, (c) spectral
reshaping — and derive the discriminating observable BEFORE any fourth
instrument. This session's product is a theory with its own falsification
experiment attached, run tonight under pre-registered grammar.

## T1 — the amplitude-freezing claim (derivation + numerical check)

CLAIM to be established: pre-escape, the chain sits near phi = 0 with
small fluctuations, so the back-reaction on each weave mode is O(c phi) —
the mode AMPLITUDES (actions) are conserved to leading order over the
entire pre-escape epoch, and the weave evolves as an almost-free
quasi-periodic drive with FROZEN amplitudes and winding phases.

If T1 holds, it PROVES the exclusion triangle rather than merely
surviving it: kinetic temperature and total drive intensity are functions
of the (frozen) amplitudes alone, hence flat BY THEOREM, and framing (c)
— spectral reshaping — is impossible at leading order, killed
analytically rather than instrumentally.

Numerical check bar (committed): evolve 16 fresh walkers (generator 121)
to t = 2000; per-mode energy drift statistic D := median over walkers of
the RELATIVE drift of the per-mode energy vector (L1 norm of change /
total). PASS: D <= 0.10 (amplitudes frozen to 10%). FAIL: D > 0.10 —
T1 falls, framing (c) revives, and the session stops there and says so.

## T2 — the reduction (derivation, no bar; consequences carried to T3)

If T1 holds: conditioned on the amplitude vector, the escape time is a
DETERMINISTIC function of the initial PHASE VECTOR alone (384 phases).
Framings (a) and (b) UNIFY: "phase-pattern frailty" and
"recurrence-structured first-passage" are one picture — the waiting time
is the hitting time of an ignition region under quasi-periodic winding,
and the falling population hazard is the generic signature of
hitting-time distributions of measure-preserving flows (early hitters
start near the ignition set; late hitters wind from far).

## T3 — the discriminating experiment (pre-registered, run tonight)

Design: 64 matched TRIPLES at the standard operating point (N = 24,
h = 0.55, T = 0.40, c0 = 0.35, window 36000):
- ORIGINAL: thermal draw (generators 111, 112; 32 walkers each).
- AMP-SCRAMBLED: same walker, per-mode PHASES kept, per-mode energies
  REDRAWN thermal (scramble generators 211, 212).
- PHASE-SCRAMBLED: same walker, per-mode ENERGIES kept, per-mode phases
  REDRAWN uniform (scramble generators 311, 312).
Convention (fixed): q = (sqrt(2E)/omega) cos theta, p = sqrt(2E) sin theta.

Statistics: rho_amp := Spearman(t_esc original, t_esc amp-scrambled);
rho_phase := Spearman(t_esc original, t_esc phase-scrambled), n = 64.
(Budget priced per the standing rule: SE ~ 0.125 at n = 64, adequate to
separate the committed thresholds.)

GRAMMAR, all outcomes fixed:
- PHASE-DETERMINISM (the theory's prediction): rho_amp >= 0.40 AND
  rho_phase <= 0.20 — fate survives an amplitude redraw and dies with a
  phase redraw. Framings (a)+(b) confirmed as one; PROMOTABLE.
- AMPLITUDE-DETERMINISM: reversed pattern — the theory is refuted in its
  specific form; amplitudes carry fate after all (and the earlier weak
  covariates must be re-examined); registered at full volume.
- CHAOTIC SENSITIVITY: both rho <= 0.20 — fate survives NEITHER redraw;
  escape depends sensitively on the full microstate; the deterministic-
  hitting picture fails in its simple form and the non-exponentiality
  needs a different origin; registered at full volume.
- ROBUST: both rho >= 0.40 — fate survives both redraws (would contradict
  the covariate record); anomaly, instrument audit.
- INTERMEDIATE: anything else; as measured.

## Promotion criterion

PROMOTE the deterministic phase-winding picture iff T1 passes AND T3
lands PHASE-DETERMINISM. Consequence grammar if promoted: the smallest
box's "aging" is neither aging nor frailty in the stochastic sense — it
is the hitting-time statistics of a quasi-periodic drive; Prediction 11's
fork RESOLVES toward STATIC DIVERSITY (an individual small detector does
not drift; an ensemble shows reproducible first-click diversity set by
initial phase configuration), stated at Modeled with the absolute-scale
caveat. If not promoted: the failing limb names the follow-up.

## Honesty clauses

- The scramble experiment's grammar, generators, convention, n, and all
  thresholds are fixed above before any triple is run.
- T1's check precedes T3; a T1 FAIL stops the session (no cherry-picking
  a favorable experiment after a failed premise).
- Status ceiling: Modeled. Absolute scale untouched (FND-MATTER-003).
