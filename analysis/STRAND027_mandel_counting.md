# FND-STRAND-027 — the Mandel counting formula from threshold nucleation

Date: 2026-08-04. Commission: Phase A's third and final derivation.
Target: photon-count statistics — the standard-list item — derived from
the corpus's own detector, with the classical/nonclassical boundary
placed exactly.

## T1 — the conditional-Poisson foundation (registered, cited)

In steady state the registered detector clicks as a memoryless Poisson
process at every size: FND-STRAND-021 (equilibrium-prepared escape is
exponential at the stationary Kramers rate) and FND-STRAND-020 (the
aggregate at any size is the Poissonization of independent channels).
Conditional on a FIXED drive, the click record over a counting window T
is therefore Poisson with mean lambda(I) T.

## T2 — linear response, with its domain stated

The registered single-site rate law (the Born-rate structure of the
measurement chain: threshold nucleation in the weak-field limit) gives
the WEAK-DRIVE regime: the click rate responds linearly to the drive's
channel energy, lambda(t) = c I(t), for illumination weak compared to
the barrier scale. DOMAIN, honest: this is continuous weak illumination
modulating the thermally assisted rate — the OPPOSITE regime from
FND-STRAND-024's single-packet cliff. Same detector, two regimes:
continuous classical beams live here; single-quantum packets live under
Grant 3. Both are used below, and their consistency is T5.

## T3 — the formula

For drive fluctuating slowly relative to the bath correlation time
(the detector is Markovian in steady state per 021, so lambda tracks
I(t)), the click record is a Cox (doubly stochastic Poisson) process,
and the count over window T is:

    P(m) = <  (eta W)^m exp(-eta W) / m!  >_W ,   W = integral_T I dt

— MANDEL'S SEMICLASSICAL COUNTING FORMULA, with eta the detector
constant absorbing c and collection efficiency, and the average over
the drive's intensity fluctuations. Derived here from threshold
nucleation, not postulated.

## T4 — consequences, and the classical boundary placed

(i) COHERENT (constant I): P(m) Poisson. (ii) THERMAL single-mode with
T much less than the coherence time (W exponential): P(m)
Bose-Einstein (geometric). (iii) THE MANDEL Q PARAMETER:
Q = eta Var(W)/<W> >= 0 for EVERY classical drive — the semiclassical
theory can be Poissonian or super-Poissonian, NEVER sub-Poissonian.
The classical boundary of photon counting is therefore Q = 0, the
counting twin of T4's g2 = 1 row in FND-STRAND-026: sub-Poissonian
counting requires integer quanta (Grant 3: Fock n thins to Binomial,
Q = -eta' < 0), exactly as sub-unity g2 does.

## T5 — the correspondence theorem (the two routes commute)

The corpus now owns TWO derivations of counting statistics: the Cox
route (this claim: classical intensity into a linear-response
nucleation detector) and the Grant-3 route (FND-STRAND-025: integer
quanta, multinomially thinned). THEOREM: on the classical sources they
share, they agree EXACTLY —
- Coherent: constant-I Cox gives Poisson(eta W); Poisson quanta thinned
  give Poisson(eta lambda). Identical.
- Thermal: exponential-W Cox gives geometric; geometric quantum number
  thinned binomially is AGAIN geometric (thinning invariance of the
  geometric family). Identical, including the mean.
The semiclassical and granular descriptions of classical light are the
same theory viewed at two grains — which is precisely why classical
optics never needed photons, and why photon counting alone (absent
sub-Poissonian sources) never proved them. The framework reproduces
that historical fact as a theorem about itself.

## Status, scope, ledger

- The Mandel formula (T1-T3) is Derived from registered detector claims
  plus the stated weak-drive linear-response domain — no grant needed.
  The nonclassical rows (Q < 0) are Derived conditional on Grant 3, as
  FND-STRAND-025/026 already carry.
- Benchmark: Cox Monte Carlo against closed forms (Poisson; Bose-
  Einstein; Q >= 0 across classical ensembles including gamma and
  lognormal drives); the Grant-3 cross-check (thinned geometric =
  geometric); Fock Q < 0.
- PHASE A CLOSES: beamsplitter correlations (025), antibunching (026),
  and photon-count statistics (027) are done at derivation cost. Next
  on the roadmap: the source sector (Phase B, simulation budget), the
  HOM 50%-visibility pin (Phase C), plain delayed choice as a derived
  non-paradox (Phase D), with the eraser scoped to QB-003's edge.
- Absolute scale untouched (FND-MATTER-003).
