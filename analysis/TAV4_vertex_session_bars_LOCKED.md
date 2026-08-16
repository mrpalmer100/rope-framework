# THE TWIST-TO-CARRIER VERTEX SESSION (codename TAV4) -- BARS LOCKED (2026-08-16)

Locked BEFORE any computation. Charter provenance: GRV-118's three
enumerated obligations, standing item E.1; run ADJACENT to
CURRENT-AS-SPIN (RESH2, EM-RECON-039) under shared bars discipline
per the E.4 charter's adjacency clause. Parts list identical to
RESH2's; nothing re-derived, everything cited at verdict level.

## THE THREE OBLIGATIONS, fixed at lock (B1, verbatim from GRV-118)
(V1) EMISSION from time-varying tau into the mixed branches.
(V2) LOCK CONVERSION EFFICIENCY.
(V3) CROSSING TRANSFER RATE at the registered coupling.

## REGISTERED PARTS LIST (fixed; identical to RESH2's, plus GRV-104/105)
- EM-RECON-012 (Derived): the lock, c_L = lambda gamma tau0
  (gradient-order, read off the lock energy at RESH2).
- EM-RECON-023 (Modeled): stiffness matrix [[lambda, c_L],[c_L, k_s]],
  entrywise constant; both eigenbranches omega = c_i q exactly;
  dV/dphi = 0 identically at crossings.
- EM-RECON-026 (Modeled): the O(g) q-linear crossing coupling for
  stretch/displacement content; condition TH1 on the face.
- FND-MATTER-047 (Modeled): torsional stiffness priced; v_t/c = 1/sqrt(5).
- GRV-104/105: J = twist at beta_J = 1; propagation pin
  gamma_grav = 4.21e-4 J/m. Source side ONLY; no lambda, no g_0i.
- EM-RECON-039 (Modeled, this session's sibling): Gamma_inj derived;
  eta_chain named as the missing input this session must price or
  declare unpriceable.

## PRE-COMMITTED OUTCOMES (B2, exhaustive per obligation)
- V1: PARTITION-DERIVED (the twist source's emitted power splits
  between the two eigenbranches in a closed form in the mixing
  structure) / SOURCE-UNDERDETERMINED (a required source moment is
  unregistered; name it).
- V2: EFFICIENCY-DERIVED (the stretch content available at crossings
  per unit emitted energy, closed form in registered symbols) /
  EFFICIENCY-UNDERDETERMINED (name the missing input).
- V3: ORDER-DETERMINED -- the leading power of g AND the geometric
  factor of the azimuth-to-neighbor transfer, stated exactly; this
  either CONFIRMS EM-RECON-023's display-level "higher-order-in-g"
  as literally higher powers of g, or REFINES it to same-order-in-g
  with geometric (mixing-angle) suppression -- either refinement is
  admissible and must be stated plainly, with 023 annotated not
  overwritten / ORDER-UNDERDETERMINED (name what blocks).
- eta_chain: PRICED (closed form, numeric gates named) /
  UNPRICEABLE-WITHOUT (named inputs).

## TRIPWIRES AND REFUSALS (B3)
- THE MASS-TERM TRIPWIRE: if any step generates an azimuthal MASS
  term (energy ~ phi^2 rather than gradients), STOP and register the
  conflict with EM-RECON-023's m_gamma = 0 exactness -- do not
  paper over. Pre-committed check: every derived crossing-induced
  azimuthal coupling must be gradient-order or field-of-stretch.
- NO touching the photon kill (state count), the GRV-113 cap,
  condition 4, or the GRV-114 grant.
- NO observational or LARES-class quantity advertised.
- NO new coupling registered; the crossing channel is EM-RECON-026's
  q-linear coupling ONLY.
- Numeric gates named, not filled: tau0 (no registered numeric),
  the crossing density n_x, and the O(g) coefficient's SI value are
  all expected gates; closed forms are the deliverable.
- Titles are not verdicts; failures registered and kept.

## MACHINE CONTENT PLANNED (B4)
sympy only, benchmarks/em/vertex_session_tav4.py:
1. The GENERALIZED eigenproblem K v = c^2 M v with M = diag(I, mu)
   (inertia matters for the dynamical mixing; RESH2's stiffness-only
   chi is superseded for dynamics by the M-weighted angle, disclosed).
2. V1: project a localized time-varying twist source tau(t) onto the
   two eigenbranches; emitted power partition in closed form.
3. V2: stretch content of each branch's unit-energy wave; the
   conversion efficiency as the energy-weighted stretch fraction.
4. V3: the transfer per crossing of each branch through the O(g)
   stretch coupling; leading order in g stated exactly; the induced
   azimuthal coupling inspected against the mass-term tripwire.
5. eta_chain assembled: drain per unit length = n_x x (per-crossing
   transfer), closed form; Omega = Gamma_inj/eta_chain propagated
   from EM-RECON-039; gates named.
