# COMMISSION DYNAMO (codename MEM3) -- BARS LOCKED (2026-08-16)

Locked BEFORE any computation. Chartered from the author's question:
what causes planetary/stellar magnetic fields in the rope model?
THE QUESTION, made commission-shaped: does transported winding in a
rotating, convecting conductor close a SELF-EXCITING circulation
loop from registered structure alone?

## REGISTERED PARTS LIST (fixed at lock)
- EM-RECON-026 (Modeled, TH1 on face): E = rho kappa_0 (v_medium x
  zhat); the q-linear Magnus force; the Lorentz split F = q(E +
  v_defect x B'); a static winding sources azimuthal mesh flow
  v_theta = q kappa_0/(2 pi r).
- GG-006 (Derived) / EM-014 lineage: winding is charge; current is
  transported winding realized as the screw; torque x rate = V x I.
- The Gaede reconciliation (registered note, EM sector): B is
  curl-of-pitch mesh circulation; the permanent-magnet account --
  aligned spinning atoms sweep the network into circulation, field
  without transport current; the Ampere force SIGN derived by the
  jump-rope gap rule (benchmarks/em/force_sign_derivation.py).
- EM-RECON-039/GRV-119/EM-RECON-040 (this week): current is spin;
  persistence quantified (leak = n_x g sin^2(chi_d) C26, sin^2 in
  [0.043, 0.055] at reference); injection Gamma_inj = lambda gamma
  tau0 E0.
- GRV-104/105 (Modeled, granted): rotation sources twist, beta_J=1.
- GRV-020 (Derived): angular no-monopole -- dipole-led sourcing.

## THE LOOP UNDER TEST (B1, fixed)
L1: mesh circulation exerts q-linear force on windings in a moving
    conductor (EM-RECON-026) -> EMF-class drive.
L2: the drive transports winding / spins conduction ropes
    (EM-014 screw; EM-RECON-039 injection; persistence per QOF2).
L3: transported winding sweeps the mesh into circulation
    (curl-of-pitch; v_theta = q kappa_0/(2 pi r); Gaede swing-wave).
L4: SIGN/FEEDBACK: does the induced circulation REINFORCE the
    pattern that induced it (jump-rope sign rule), and under WHAT
    flow class does the loop have nonzero gain?

## PRE-COMMITTED OUTCOMES (B2, exhaustive)
- LOOP-CLOSES-STRUCTURALLY: every link registered and composable,
  sign consistent; the gain criterion derived in FORM with all
  numeric gates named. (This outcome does NOT claim field
  magnitudes or that Earth/Sun numbers are reproduced.)
- LOOP-OPEN-AT: a named link fails verbatim reading or sign check.
- SCOPE-BLOCKED: the plasma question (unbound charge vs bound
  conduction ropes) blocks the stellar case; if it blocks only the
  Sun and not Earth, the split verdict is stated.

## MANDATORY NULL TEST (B3)
RIGID ROTATION: compute whether v = Omega x r alone drives a closed-
loop EMF through L1. If the curl vanishes, register the null AS A
RESULT (rotation alone cannot self-excite; convection required) --
this is the anti-dynamo-flavored check that keeps the commission
honest, and its empirical resonance (bodies with rotation but no
convection lack fields) may be DISPLAYED but not registered as a
confrontation.

## REFUSALS (B4)
- NO field-strength numerics: kappa_0 is gated on SIGMA (registered
  bound only); no Earth/Sun magnitude claim, no geodynamo data
  confrontation.
- NO touching the gravitomagnetic grants (GRV-110/113/114, condition
  4); frame dragging is a SEPARATE charter written only if this
  loop closes, and nothing here pre-computes it.
- The plasma scope question is FLAGGED where it binds, not resolved.
- TH1 (effective-medium, wavelengths >> a) carried on the face of
  every L1/L3 statement.
- Titles are not verdicts; numeric gates named, not filled.

## MACHINE CONTENT PLANNED (B5)
sympy, benchmarks/em/dynamo_mem3.py:
1. L1 composition: E = rho kappa_0 (v x zhat) for (a) rigid rotation
   v = Omega x r -- compute curl(E) exactly (the null test); (b) a
   poloidal convective component u_c -- show curl(E) != 0.
2. L3: verify the winding-sourced azimuthal flow and the jump-rope
   sign compose with L1's drive to REINFORCE co-rotating transport
   loops (sign propagation through the full cycle, symbolic).
3. The gain/loss criterion: per-cycle gain ~ rho kappa_0^2 u_c /
   (2 pi L) class vs the registered leak n_x g sin^2(chi_d) C26;
   define R_rope = gain/loss and exhibit the self-excitation
   threshold R_rope > 1 in closed form with gates {SIGMA->kappa_0,
   u_c, L, n_x, g, C26, beta}.
