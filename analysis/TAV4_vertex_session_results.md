# THE TWIST-TO-CARRIER VERTEX SESSION (TAV4) -- RESULTS (2026-08-16)

Bars: analysis/TAV4_vertex_session_bars_LOCKED.md (locked first).
Benchmark: benchmarks/em/vertex_session_tav4.py (sympy-exact; one
symbolic identity verified exactly at rational points after a sympy
branch-ordering artifact, disclosed below; all assertions pass).
All three GRV-118 obligations DISCHARGED at their pre-committed
positive outcomes. eta_chain PRICED in closed form; numeric gates
named. One registered display-level statement REFINED (EM-RECON-023
annotated, not overwritten).

## THE DYNAMICAL MIXING ANGLE (supersedes RESH2's stiffness-only chi
   for dynamics, disclosed)

The generalized problem K v = c^2 M v, M = diag(I, mu), gives

    tan(2 chi_d) = 2 sqrt(I mu) lambda gamma tau0 / (I k_s - lambda mu)

with both branch speeds exactly linear (omega = c q, entrywise
q-independence re-confirmed). chi_d -> RESH2's chi at I = mu; the
closed forms below hold in chi_d.

## V1 -- EMISSION PARTITION: PARTITION-DERIVED

A localized time-varying twist source (the GRV-104 identity supplies
the source: J = twist at beta_J = 1, no lambda, no g_0i) drives the
twist coordinate. Its emitted power splits:

    P_twist-branch : P_stretch-branch = cos^2(chi_d) : sin^2(chi_d)

verified exactly (ordering-agnostic rational-point identity; the
fully symbolic trigsimp is beyond sympy and the failure of the FIRST
symbolic check is disclosed as instrument, not physics -- the
numeric probe agreed to all digits, 14.1795... = 14.1795...).
Most of a spinning source's output stays on the slow twist-dominant
branch; the fast stretch branch takes the sin^2 remainder.

## V2 -- LOCK CONVERSION EFFICIENCY: EFFICIENCY-DERIVED, closed form

Stretch energy fractions: sin^2(chi_d) (twist branch), cos^2(chi_d)
(stretch branch); completeness verified (sum = 1). The total
crossing-available fraction of the source's emitted energy:

    eta_conv = cos^2 sin^2 + sin^2 cos^2 = sin^2(2 chi_d) / 2

exact (machine identity True). Small-mixing: eta_conv ~ 2 chi_d^2.
The efficiency is bounded at 1/2 (chi_d = pi/4, degenerate stiffness)
and quadratically small in the physically indicated weak-lock regime.

## V3 -- CROSSING TRANSFER RATE: ORDER-DETERMINED, and a REFINEMENT

Per crossing, through the registered q-linear coupling
(EM-RECON-026), the twist-dominant branch transfers

    T = g * sin^2(chi_d) * C26        [leading order g^1]

THE ORDER STATEMENT, the session's headline: the azimuth-to-neighbor
transfer is FIRST order in g. It is NOT higher powers of g. The
suppression is GEOMETRIC -- the sin^2(chi_d) mixing factor -- not
parametric. EM-RECON-023's display-level phrase "higher-order-in-g
chain" is hereby REFINED per the pre-committed grammar: the chain
adds a mixing angle, not a power of g. 023 is annotated, not
overwritten; its exactness results (dV/dphi = 0, m_gamma = 0) are
untouched and indeed re-verified:

MASS-TERM TRIPWIRE: PASSED. The induced azimuthal coupling enters
only through the branch's stretch GRADIENT content; the crossing
energy has d/dphi = d/du = 0 identically (gradients only). No
azimuthal mass term is generated at any step. m_gamma = 0 intact.

## eta_chain: PRICED

    eta_chain = n_x * g * sin^2(chi_d) * C26
    Omega     = lambda gamma tau0 E0 / eta_chain      (EM-RECON-039 closed)

GATES, named not filled: tau0 (no registered numeric); n_x (crossing
density); C26's SI value (rho kappa_0 class, gated on SIGMA per
EM-RECON-027); g. Four gates, all pre-existing registry gates -- the
session added NO new unknowns; it arranged the registered ones into
two closed forms.

## THE ECONOMY, completed

One identity, dV/dphi = 0, now audited across all three of its
duties with the same angle: it protects m_gamma = 0 (exactly, mass
term impossible), it throttles twist radiation (to first order in g
times sin^2(2 chi_d)/2 conversion), and it preserves current (leak
bounded by sin^2(chi_d) per RESH2, now with the dynamical angle).
The sector status line updates: STRUCTURALLY UNSUPPRESSED AT THE
SOURCE, REGISTERED-VIA-LOCK IN PROPAGATION, DYNAMICALLY DERIVED AT
LEADING ORDER WITH FOUR NAMED NUMERIC GATES.

## REFUSALS HONORED
No observational/LARES quantity; photon kill untouched; GRV-113 cap
and condition 4 untouched; no new coupling; the one instrument
artifact disclosed with its numeric adjudication.
