# THE tau0 PIN SESSION (codename QOF2) -- BARS LOCKED (2026-08-16)

Locked BEFORE any computation. Target: the equilibrium twist rate
tau0 of the wound conduction strand -- the single highest-leverage
numeric gate in the sector (un-gates chi_d, eta_conv, and both
EM-RECON-039 bounds simultaneously, per GRV-119).

## B1 -- THE SEARCH RAN FIRST (house rule, has paid twice), findings
     binding on this session:
1. NAME COLLISION FOUND AND ADJUDICATED: the corpus's only numeric
   "tau0" (tau0 = 1.95 w/c, ELEC-047/058/059 lineage) is a causal
   TRAVERSAL TIME in the retired hbar sector -- separation-coordinate
   units, a duration. It is NOT the lock's twist rate (rad/length).
   This session must NOT import it, and NAME_REGISTRY gains an
   addendum distinguishing tau0_lock (twist rate, EM-RECON-012
   lineage) from tau0_trav (duration, ELEC-047 lineage, retired
   sector). Any future numeric confusion between them is a
   registered failure mode.
2. THE REGISTERED GEOMETRIC RELATION (EM-RECON-012, Derived):
   gamma = 1 + 1/(r tau0)^2 = 1/sin^2(theta) EXACTLY, with r the
   winding radius. INVERTIBLE: r tau0 = 1/sqrt(gamma - 1). The
   registered gamma bracket "~2-4 for moderate twining" therefore
   PINS THE DIMENSIONLESS PRODUCT: r tau0 in [1/sqrt(3), 1].
3. REGISTERED RATIOS AVAILABLE: v_t/c = 1/sqrt(5) (FND-MATTER-047);
   k/T0 = 2 in registered use across 12+ claims including Derived
   ones (FND-REL-002/004) and confirmed at the f = 1 limit by
   FND-063; c^2 = T0/mu.
4. NOT REGISTERED: tau0 in absolute units (requires r in metres --
   the mesh/winding radius numeric, which the scale ladder holds at
   brackets); the gyration-to-winding radius ratio beta =
   sqrt(I/mu)/r (an O(1) geometric property of the strand
   cross-section and winding, never constructed by the registry --
   checked before idealizing, per standing rule 2).

## B2 -- PRE-COMMITTED OUTCOMES (exhaustive)
- PINNED: tau0 in absolute units from registered inputs alone.
  (Expected unreachable: r is bracketed, not pinned. If reached,
  every input's provenance must be cited at verdict level.)
- DIMENSIONLESSLY PINNED: the combinations the DOWNSTREAM closed
  forms actually need (chi_d, sin^2 chi_d, eta_conv, L_az/L_tr) are
  functions of DIMENSIONLESS products only; if those products pin or
  bracket from registered inputs, the gates fall WITHOUT an absolute
  tau0. This outcome is admissible and, if reached, must state each
  residual gate (expected: beta) with its status.
- BRACKETED: numeric brackets on the downstream quantities, each
  bracket edge carrying its provenance.
- UNPINNABLE-WITHOUT: named inputs; session registers the shape of
  the obstruction.

## B3 -- REFUSALS
- NO fitting to any experiment (PVLAS, LARES, anything). If a
  desired value would "fix" an exclusion, that is the alpha-shopping
  the audit loop forbids; the derivation must be blind to targets.
- NO new primitive: beta is NOT invented a number. If beta gates the
  result, it is NAMED, bracketed only if a registered construction
  brackets it, else left symbolic.
- NO touching the scale ladder (FND-110's single-anchor ruling), the
  hbar sector's retired numerics, or any absolute-length grant.
- The k/T0 = 2 input is carried WITH ITS GRADE: it is registered
  use, not a Derived pin; every downstream number inherits that
  qualifier on its face.
- Titles are not verdicts; failures registered and kept.

## B4 -- MACHINE CONTENT PLANNED
sympy, benchmarks/em/tau0_pin_qof2.py:
1. Invert the Derived gamma relation; verify r tau0 = 1/sqrt(gamma-1)
   exactly; evaluate the bracket at gamma = 2 and 4.
2. Reduce tan(2 chi_d) to dimensionless registered ratios:
   substitute lambda/I = v_t^2, k_s/mu = (k/T0) c^2, and exhibit
   tan(2 chi_d) = 2 (v_t^2/c^2) beta (gamma tau0 r) / (k/T0 - v_t^2/c^2)
   = (2/9) beta gamma/sqrt(gamma-1) at the registered ratios.
3. Evaluate gamma/sqrt(gamma-1) on the bracket; propagate to
   sin^2(chi_d), eta_conv = sin^2(2 chi_d)/2, and the L_az/L_tr
   bound, carrying beta symbolic; also report the beta = 1 reference
   point EXPLICITLY LABELED as reference, not derivation.
4. Monotonicity audit: which direction each downstream quantity
   moves in gamma and beta, so the brackets are honest intervals.
