# Release v3.3.0 — The ribbon produced (2 August 2026)

**444 registered claims (104 Derived, 303 Modeled, 4 EFT-constrained, 4 Conjecture,
5 Open, 24 Failed-and-kept); 426 code-backed, all passing.**

One campaign, six claims, one question answered: QB-027 showed the shared ribbon
works, and nobody had shown the medium produces one. Now the corpus has.

## The production campaign (QB-028 through QB-033)

- **QB-028 — Production.** FND-STRAND-006's kink-antikink nucleation, run as a
  source: one event yields two excitations, a coherently wound connecting segment,
  free separation under the registered nucleation-silent bias, and EXACT base
  anticorrelation by conservation. The fiber question forks on one coupling.
- **QB-029 — The fork resolved by a theorem from another sector.** GRV-020's
  one-generator theorem forbids a second internal mode; FDT forbids noise without
  energy coupling (FND-STRAND-005's fibre-blindness). g_fb = 0: nothing can
  thermalize the fiber. The residual is gapped-base transport noise that
  SATURATES: a finite, separation-independent visibility, V_r ~ 0.78.
- **QB-030 — The experiment, worst case.** QB-027's measured analyzers, the
  nucleated pair, the empirical noise bank: CHSH = 2.039 +/- 0.005, an 8.6-sigma
  violation. (Also: an environment-sensitivity flag on QB-027's printed values,
  later adjudicated benign.)
- **QB-031 — The transport law derived.** The same one-generator theorem exhausts
  what transport can do to a frame: rotation about the local axis by the
  accumulated azimuth is the ONLY law available. Deriving it RAISED the number:
  CHSH = 2.234 +/- 0.005 at 52 sigma; the earlier model reclassified as the
  worst-case floor.
- **QB-032 — Orientation, from premise to parameter.** The violation as a
  function of source orientation: 2.03 (perpendicular; the floor is a buildable
  geometry) to 2.41 (any in-plane axis; a degenerate maximum from an exact
  symmetry). The whole span violates. Every point predicted before measured.
- **QB-033 — The visibility derived.** A self-consistent Gaussian closes the
  harmonic systematic from 13 to 6 percent: V_r = 0.792 from (T, kt, h) alone,
  1.6 percent from the empirical bank. The entire orientation curve is now
  computed from three engine parameters plus two theorems; the bank is a check,
  not an input.

**The headline: a Bell violation whose every number is derived from three medium
parameters** — with the chain nucleation -> holonomy -> visibility -> transport
law -> orientation fully barred, three mid-session catches owned on the record,
and one generic ingredient remaining corpus-wide (the weave-as-reservoir
derivation of the bath itself).

## Verification

`tools/verify_corpus.py --quick` passes; per-claim benchmarks pass; bars for every
session locked before computation in `analysis/`.
