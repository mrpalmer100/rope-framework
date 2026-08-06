# FND-MATTER-040 — the scale closure: the pipeline run, and the redundant equation says NO

Date: 2026-08-04. Commission: execute the FND-MATTER-039 pipeline with the
author's calibration decision received ("spend it on m_e, run the closure").
Benchmark: `benchmarks/foundations/matter040_scale_closure.py` (all bars pass).

## Bars (restated from MATTER039, locked before any number was computed)

1. Step order fixed: a from R2 → T0 from R5 → l_q from R1 → Step 4 grammar.
2. The one calibration is spent on the electron mass; the ring identification
   for the electron (L = 3.141 mesh units) is GIVEN material, not on trial.
3. Bands propagated honestly: sqrt(D) ∈ [0.1, 10] on a; ZPE factor ∈ [1, 3].
4. Step-4 grammar as pre-drafted: l_q/a of order 1–100 reconciles the two
   registered action areas; a ratio outside it with bands propagated is a
   REGISTERED TENSION, and the mismatch's size fingerprints the culprit.
5. Every step inherits Modeled; FND-MATTER-003 remains OPEN unless the
   confrontation RECONCILES; a tension does not close it.

## The run

| Step | Result |
|---|---|
| 1. a (gravity route) | 1.293e-34 m (8 l_P), band ×/÷10 |
| 2. T0 (m_e spent) | 2.016e20 J/m |
| 3. l_q (no freedom) | 3.792e-24 m |
| 4. l_q/a | **2.93e10**, full band [9.3e9, 1.6e11] |

**Verdict, by the pre-drafted grammar: REGISTERED TENSION.** The band's low
edge clears the reconciliation window by 8.0 orders of magnitude. No permitted
combination of the dictionary factor and the zero-point lever brings the
gravity route and the matter route into the same universe of scales. This is
the first time the scale question had a way to say no, and it said no.

## The fingerprint — the tension names its own culprit

The mismatch is not diffuse. Four independent registered T0 anchors cluster
within a factor 49 of one another:

| Anchor | T0 (J/m) | Closure T0 / anchor |
|---|---|---|
| R1 quantum area (fork-invariant, 2.65e-28 m²) | 119 | 1.7e18 |
| Lattice-anchored (QCD flux tube, ELEC-081) | 1203 | 1.7e17 |
| Σ-route branch | 1700 | 1.2e17 |
| GRV-074 rigidity quantification (mid) | 5847 | 3.4e16 |

The closure's T0 sits ~17 orders above the entire cluster. Since Step 2 is
just m_e c² = T0 L a, and m_e is measured, the 17 orders live entirely in the
choice of a — i.e., in R2's identification of the induced-gravity cutoff with
THE mesh scale. And the registry already holds the escape hatch, written a
month before this run: the G-investigation conjecture explicitly reserved that
a_grav need NOT equal the inter-rope mesh spacing ("a network generically has
distinct micro-scales"), and flagged that a future independent pin of the mesh
would make agreement or disagreement with 1.6e-35 m "a sharp consistency
test." Tonight that test ran, and it disagreed by 17–18 orders. The tension
lands exactly on the pre-registered reservation: **the gravitational
micro-scale and the matter mesh scale are not the same length.** Note the 17
orders is the SAME lever GRV-093 identified as the fork's n_q lever — one
geometric ratio, now measured from a second direction.

## What survives, sharpened: the EM cluster

Removing R2 from the mesh-scale role leaves a coherent picture the run itself
corroborates:

- The four T0 anchors above are mutually consistent within ~50x, built in
  four different sectors (EM lattice data, the Σ branch, the hbar relation,
  the gravity rigidity bookkeeping) across months.
- **The blind-mass diagnostic (no calibration spent):** the EM branch's own
  card values (a = 1e-16 m, T0 = 1203 J/m) predict a ring mode mass of
  4.62 m_e — factor 4.6 from the measured electron mass, just outside the
  honest ZPE bar of 2–3. Registered as a whisper, not a win: the corpus's
  whisper playbook applies (name it, band it, do not promote it).
- n_q lands inside the snap band on the EM branch (1.4–4.1e-4 vs 1.1–4.6e-4,
  the original GRV-093 pass) and MISSES below it on the closure branch
  (2.4–7.1e-5, with the h-scaling ambiguity flagged) — a second, independent
  vote in the same direction as the fingerprint.

## The ELEC-084 unlock, executed branch-conditionally

With the naive dictionary (time unit a/c) flagged:

| Branch | P23 epoch (s) | P25 location (Hz) | ħc/a |
|---|---|---|---|
| EM (a = 1e-16 m) | 5.8e-23 | 3.0e24 | 1.97 GeV |
| Closure (a = 8 l_P) | 7.6e-41 | 2.3e42 | 1.5e18 GeV |

On the EM branch the switch-on epoch is tens of yoctoseconds — the P23
discriminating branch is then unobservable against device effects, which
retroactively RATIFIES ELEC-084's T2 demotion of P23 rather than reversing
it. P25's spectral scale lands at ~2 GeV, numerically adjacent to the nucleon
scale; noted, not claimed. Conversions remain branch-conditional until the
tension resolves.

## Status discipline

- Everything here is Modeled. Nothing is promoted.
- FND-MATTER-003 (absolute scale) remains **OPEN**: the confrontation
  adjudicated a tension, not a reconciliation. The open problem is now
  sharper: it is no longer "what is a" but "which of the two registered
  micro-scales is the mesh, and what physical relation spans the 17 orders
  between them."
- FND-MATTER-005's irreducibility theorem stands, untouched.
- The calibration is SPENT. Any future use of m_e as a fit target must cite
  this file and justify a second spend under a new bars session.

## Next bricks, ranked

1. **The two-scale session:** promote or kill the "a_grav ≠ a_mesh" reading —
   does the induced-gravity derivation (GRV-025/029/095) survive with the
   cutoff decoupled from the mesh, and what registered quantity, if any,
   relates the two lengths? (The 17-order lever appearing in both this run
   and the n_q fork is the thread.)
2. **The whisper session:** the 4.6x blind mass. One factor of ~4.6 between
   the EM branch and the electron mass, with the ZPE lever honestly blocked
   at FND-MATTER-003 — a bars-locked attempt to price the gap's geometry
   (ropelength convention, core energy, ZPE sign) without touching m_e.
3. Re-run the closure with a = 1e-16 m as the PRIMARY route (spending the
   calibration nowhere) and let R2 output a_grav as the derived quantity —
   the inverted pipeline, one afternoon.
