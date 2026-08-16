# COMMISSION CURRENT-AS-SPIN (session codename RESH2) -- BARS LOCKED (2026-08-16)

Locked BEFORE any computation. Charter: STRATEGIC_TARGETS standing
item E.4 (v3.26.32 cut). The author's question: what specifically
makes conduction ropes SPIN rather than merely vibrate. Two halves,
both to be answered from registered structure only.

## REGISTERED PARTS LIST (complete, fixed at lock; nothing else admitted)
- EM-RECON-012 (Derived): the twist-stretch lock, delta_tau =
  -gamma tau0 eps with gamma = 1/sin^2(theta) exact; the penalty is
  GRADIENT-order; the longitudinal sector is gapless.
- EM-RECON-023 (Modeled): the coupled screw-stretch stiffness matrix
  [[lambda, c_L],[c_L, k_s]], entrywise q-independent, both
  eigenbranches omega = c q exactly; azimuth-blindness dV/dphi = 0
  IDENTICALLY at crossings; twist reaches crossings only through the
  lock chain, higher-order-in-g.
- EM-RECON-026 (Modeled): the O(g) q-linear crossing coupling for
  the displacement/stretch content (condition TH1 on the face).
- FND-MATTER-047 (Modeled): torsional stiffness priced, torsion
  speed v_t/c = 1/sqrt(5).
- GG-006 (Derived): winding is charge (handedness = linking).
- EM-014 lineage (screw realization): rotation-to-axial coupling
  exact (tan(alpha) per rotation); power = torque x angular rate.

## THE TWO QUESTIONS, fixed at lock (B1)
(a) TORQUE INJECTION: does an EMF-class longitudinal strain gradient
    eps(z) on a wound strand force azimuthal rotation through the
    Derived lock at a derivable rate? The deliverable is the
    torque-balance allocation steady-EMF -> steady rotation rate.
(b) SPIN PERSISTENCE: quantify the leak asymmetry -- transverse
    vibration leaks at every crossing at O(g); azimuth escapes only
    via the lock chain (dV/dphi = 0 identically). The deliverable is
    a quantitative asymmetry statement, not a slogan.

## PRE-COMMITTED OUTCOMES (B2, per the charter, exhaustive)
- DERIVED-RATE: the steady rotation rate follows from registered
  inputs alone, both the injection side and the dissipation side.
- RATE-UNDERDETERMINED: the injection side derives but the balance
  cannot close because a required input is unregistered; the missing
  input must be NAMED, with its owning session identified.
- Either way, the asymmetry in (b) is quantified: a closed form in
  registered quantities, with any numeric gating named.

## REFUSALS (B3)
- NO new coupling registered; the drive is the registered EMF-strain
  reading only (along-rope strain gradient, EM-RECON-001 mapping).
- NO computation of the suppression ORDER of the lock chain's
  crossing transfer: that is the vertex session's obligation (3)
  per GRV-118, explicitly not owed here. If the torque balance needs
  it, the outcome is RATE-UNDERDETERMINED naming exactly that.
- NO touching GRV-118's verdict, EM-RECON-023's photon kill, or the
  GRV-113/114 gravitomagnetic objects.
- Adjacency discipline (charter): this session computes NOTHING the
  vertex session owns; shared parts are cited, not re-derived.
- Titles are not verdicts; cited claims read at verdict level.
- Failures registered and kept; no silent edits.

## MACHINE CONTENT PLANNED (B4)
sympy only, benchmarks/em/current_as_spin_resh2.py:
1. From the registered lock energy (lambda/2)(delta_tau +
   gamma tau0 eps)^2, derive the generalized torque density on the
   azimuthal coordinate phi (tau = phi') under an imposed strain
   gradient. Exact symbol algebra; no numbers invented.
2. Verify that with dV/dphi = 0 in the bulk (registered exactness),
   a steady drive gives angular ACCELERATION unless balanced -- i.e.
   exhibit the torque-balance equation and identify which
   coefficient is registered and which is not.
3. Diagonalize [[lambda, c_L],[c_L, k_s]] with c_L = lambda gamma
   tau0 read off the SAME lock energy; compute the stretch fraction
   sin^2(chi) of the twist-dominant eigenbranch (the only registered
   leak path for azimuth) and the exact zero for the pure-twist
   component at O(g). Report the asymmetry as
   leak_az / leak_transverse = sin^2(chi) x (chain factor), the
   chain factor being the vertex session's unowned order.
4. Gating: gamma carried as the registered bracket ~2-4 (moderate
   twining); tau0 numeric NOT registered -- if a number requires it,
   the gate is named, not filled.
