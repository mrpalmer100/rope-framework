# COMMISSION CASIMIR-PLATE (F3) -- RESULTS (2026-09-05)
Executed under analysis/CASIMIR_PLATE_charter_LOCKED.md (+A1, the Leg 0
piston calibration). Leg 0 logs and scripts: analysis/casimir/.

## VERDICT (Leg 1, 2026-09-05): CAS-BC-OPEN -- HALTED at Leg 1; DISCHARGED the same day by E-RECON (EM-023, granted). Legs 2-5 licensed under A2/A3; running locally.

## Leg 0 -- controls (instrument calibrated)
v1 The FND-089 supercell reproduces SHIN6 (min group speed 0.791, both
   polarizations, PASS) -- re-run in this campaign's PEV-IDENT Leg 0.
v2/v3 Scalar piston controls, after Amendment A1: Dirichlet p_F =
   4.002, K = pi^2/1440 to 0.01 pct (both Richardson extrapolants);
   Neumann p_F = 4.002, K = pi^2/1440 to 0.00 pct. A1 recorded two
   properties the charter's piston lacked: the far-slab geometric
   factor g(d, L) = 1 + (d/(L-d))^3 - 2(2d/L)^3 (0.787 at the top
   rung), and the plate's effective position (Dirichlet d_eff = d + 1;
   Neumann d_eff = d).
v4 In-plane convergence 3e-6 at W = 1024 -> 2048 (a 64 x 64 grid was
   non-convergent at 74 pct and rejected). v5 L-spread 1.2e-3 (D) /
   2.4e-5 (N) on the normalized piston. v6 clean room: hbar and the
   experimental values appear in no executed file; pi^2/1440 appears
   only in the control leg as the charter permits.

## Leg 1 -- THE PLATE, DERIVED (reading only): the dictionary does not
## fix it
"Perfect conductor: tangential E = 0" was mapped through the registered
dictionary. The registry holds TWO Derived-class identifications of E:
  (a) EM-016 (the field-tensor dictionary): E_i = F_i0 = -grad phi -
      dA/dt = "static tension/twist gradient plus orientation-transport
      rate", A the coarse-grained orientation connection (GG-001).
      Tangential E = 0 then pins the transverse ORIENTATION-TRANSPORT
      RATE at the plate: for the collective transverse displacement s
      (EM-RECON-025's carrier, orientation = tilt = ds/dz) this is a
      condition on d/dt(ds/dz) -- NEUMANN-class on s (d_eff = d).
  (b) EM-RECON-026 (the Magnus identification, q-linear force):
      E = rho kappa_0 (v_medium x zhat). Tangential E = 0 pins the
      medium VELOCITY at the plate: DIRICHLET-class on s (d_eff = d+1).
The two conditions differ by one derivative order and by one lattice
unit of plate position; for the wound two-band vector medium they are
not the same problem. Worse for the dictionary than for this
commission: for a transverse plane wave along z polarized in x, (a)
gives E_z ~ d/dt(ds_x/dz) (a longitudinal E) while (b) gives E in the
plane (v x zhat) -- the two identifications do not agree on the
polarization of E for light. No registered object reconciles them (no
"conductor", "mirror" or "pinned boundary" exists in the EM/OPT/FND-REL
registry as a mechanical boundary condition; OPT-010's dielectric
mirror is an index-contrast object, not a plate condition).
CENSUS (as far as derivable): the longitudinal carrier IS constrained
under either reading through the -grad phi half (phi = the twist-
tension channel, EM-018: tangential gradient zero -> phi constant along
the plate); the transverse bands are constrained under both readings
but by DIFFERENT conditions. Per D2 the commission HALTS.

## What is registered from the halt (draft for the author's grant)
- CAS-BC-OPEN as a NAMED DEBT on EM-016's face: "a conductor is not yet
  a dictionary object" -- sharpened to: the registry's two Derived
  identifications of E (EM-016's Faraday half via the orientation
  connection; EM-RECON-026's Magnus form via the medium velocity) do
  not agree on the boundary condition a conductor imposes, nor on the
  polarization of E for a transverse plane wave. Reconciling them is
  a prerequisite for ANY conductor-boundary computation in the corpus
  (Casimir, reflection, cavity modes), and is the true next-order.
- The calibrated piston instrument (A1) is durable: once the plate
  condition is fixed, Legs 2-5 run as chartered at zero re-derivation.
- FINE-GATE's Q2 ledger: the Casimir per-mode action remains the
  relation that would close the a_f gate -- now behind the dictionary
  debt rather than behind computation.

## Not run (by the charter's own halt rule)
Legs 2-5: no wound spectrum, no readings (i)-(iii), no exponent, no
coefficient, no CAS-PIN / GAP / OVER, no thermal term. FND-132's
mechanical identity and Prediction 32 are untouched.

## Process
One session (three budgeted). The halt fired at the reading leg
exactly as D2 pre-committed; the controls' two calibration findings
are recorded as A1 before Leg 1 so they carry to the resumed run.
