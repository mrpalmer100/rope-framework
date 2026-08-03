# GRV-077 bars — LOCKED before computation (2026-08-02)

Commission: derive GRV-038's load-share premise (P1: "every strand element bears
the static support load proportional to local proper acceleration") from
registered structure. The pressing profile, the area law, and the whisper chain
all stand on it. Fork-independent (GRV-076): nothing here depends on which (a,
Sigma) branch holds.

The derivation route, stated before computing:
- The medium's stress: a strand is a DIRECTIONAL TENSION with the registered
  identity mu = T/c^2 (line energy = tension; the identity QGATE-005's additivity
  chain used). Per strand element: energy density e, LONGITUDINAL pressure
  p_par = -e (tension equals energy density with opposite sign), TRANSVERSE
  pressure p_perp = 0 (strands do not push sideways at rest).
- Static equilibrium in a static metric: covariant conservation of T^mu_nu in
  ds^2 = -alpha(x)^2 dt^2 + spatial, evaluated by machine (sympy, exact
  Christoffels, no weak-field shortcut), gives the CONTACT FORCE DENSITY a
  static medium must receive: f_j = (e + p_j) d_j ln alpha per principal
  direction.
- The expected theorem: ALONG the strand (e + p_par) = 0, so ZERO support is
  needed longitudinally; TRANSVERSE (e + p_perp) = e, so the required support is
  f_perp = e a_proper/c^2 with a_proper = c^2 grad ln alpha the proper
  acceleration -- the load-share premise EXACTLY, with a sharpening GRV-038 did
  not have: the load is TRANSVERSE-ONLY, which is precisely the component
  crossings can supply (pressing is a transverse contact force).

Premises, stated as premises:
- P1': the static (frozen-star) configuration itself -- GRV-034's dictionary
  reading of the exterior; this session derives the load GIVEN staticity, not
  staticity.
- P2': the crossing share: the transverse support is delivered by the weave's
  crossings at areal/volumetric density n_x ~ O(1)/a^3; the O(1) geometric
  factor is not derived here (it was GRV-038's K and remains its K).

Rules fixed in advance:
- R1: the conservation computation is exact and by machine on a general static
  diagonal metric; both the longitudinal null result and the transverse formula
  must come out of the same calculation with no case-by-case hand algebra.
- R2: the Rindler consequence is re-derived as a CHECK, not re-registered: with
  a_proper = c^2/s near a horizon, pressing per crossing = e/(n_x s) x c^2 --
  the K c^2/s form GRV-038 posited, now with the load factor derived.
- R3: no new horizon claims; GRV-034 consistency (the longitudinal null result
  and tension exhaustion) is NOTED, not extended.
- R4: no tier motion; GRV-038's P1 is DISCHARGED-GIVEN-STATICITY, and its claim
  text's premise ledger is updated by annotation.

Bars:
- B1: the stress tensor assembled from registered identities only (mu = T/c^2;
  transverse pressure zero), each with its source claim named.
- B2: exact static conservation by machine; the contact-force formula
  f_j = (e + p_j) d_j ln alpha reproduced from the covariant divergence.
- B3: the theorem: longitudinal support ZERO, transverse support e a_proper/c^2
  -- load proportional to local proper acceleration, transverse-only.
- B4: the Rindler check per R2.
- B5: propagation per R4; the two remaining premises (staticity P1'; the O(1)
  crossing geometry P2') named as the chain's honest residue; the deferred
  tensor-coefficient session (the fork's internal test) re-queued with reason.
