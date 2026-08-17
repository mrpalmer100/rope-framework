# COMMISSION BLOCH-L -- CHARTER AND BARS (LOCKED 2026-08-16, v3.26.69)

The computation that decides whether k/T0 = 2 is a theorem. Chartered
at FND-124, inputs closed at FND-125, resonance window locked here.
This document is self-contained: a fresh session can run the
commission from this file plus the registry.

## 0. THE QUESTION (three equivalent registered forms, FND-123)
Is r_s = 0.2496 a_f  <=>  is c_L,f = 2.844 c  <=>  is the
coarse->fine stiffness mapping (FND-117's factorization) dynamically
exact? Bloch-L answers in the SPEED form.

## 1. CLEAN-ROOM SEALS (binding on every build leg)
The values 2.844 c, r_s = 0.2496 a_f, and 8.091 are SEALED: they may
not appear in, motivate, or tune any part of the build. They enter
only at the pre-registered outcome sheet (section 6). The KBSAT
derive-point may not steer (FND-121 condition 3).

## 2. INSTRUMENT
FND-089's triply-controlled Bloch machinery (supercell), which
passed its transverse-sector controls on THIS medium. The three
controls are INHERITED and must be re-run for the longitudinal
build: (i) the straight-configuration control (must reproduce the
registered straight-medium longitudinal behavior); (ii) the
instrument-validity control from FND-084's lesson (the time-domain
instrument was retired for cause -- Bloch/supercell only); (iii) the
polarization-identification control (the read mode must be
identified as the LONGITUDINAL branch by its eigenvector, not by
ordering or continuity assumptions).

## 3. INPUTS (all sourced; no free parameters)
- Winding: two levels, psi_1 = 35.2644 deg, psi_2 = 59.4444 deg
  (FND-088, derived); worst-case pitch p = a_f (FND-091 convention).
- Radii: R_1 = 0.11254 a_f, R_2 = 0.26959 a_f (FND-125, derived
  from the joint kappa+tau system; the psi-from-axis Frenet
  realization is the registered one).
- Fiber (the granted rod, FND-118): one modulus; kb = 0.126 T0_f
  a_f^2 (FND-121, KBSAT -- TRIPWIRE NOTED: any independent kb
  arrival below the ceiling supersedes the grant and re-opens this
  input); axial k_f follows from the rod identity k_f = 4 kb/r_s^2
  with r_s LEFT SYMBOLIC in the build (the output determines it;
  pre-inserting a value would violate the seals).
- Mass: mu_f = T0_f / c^2 (FORCED by the SHIN transverse-c
  invariant; FND-123 leg B).
- Tension: T0_f = T0 / n_sub (redistribution, FND-083); note the
  n_sub cancellation class (GRV-128) -- the commission should
  verify n_sub cancels from c_L,f as it did from lambda.

## 4. THE READING WINDOW (locked by the resonance-avoidance check)
Read the longitudinal branch at lambda = 24 p and lambda = 48 p:
24-48x from FND-085's excluded resonance (p ~ lambda), 3-8x deeper
than FND-086's validated transverse homogenization point
(lambda/p in [6, 8]). CONVERGENCE BAR: |c_L(24p) - c_L(48p)|/c_L
<= 0.5%, else STOP and register REGIME-NOT-REACHED (no reading).

## 5. THE INTERNAL KILL CONDITION (fires before any target
comparison; FND-124's rigidity demand)
The axial transmission must land AT OR ABOVE the static
stretch-projection value. Below it, the wound structure cannot
carry the registered coarse sqrt(2) c channel floor and the fine
structure CONFLICTS WITH THE CORPUS'S OWN FLOOR -- registered as
RIGIDITY-DEMAND-FIRED regardless of what the speed would otherwise
imply. (The FND-125 caveated display suggests the bending and
stretch load paths are comparable at order one near the
derive-point, so this check is LIVE, not a formality.)

## 6. THE PRE-REGISTERED OUTCOME SHEET (targets unsealed here only)
Convert the read speed via r_s/a_f = 0.7099 c / c_L,f (FND-123):
- c_L,f = 2.844 c (within the convergence bar's resolution)
  -> r_s = 0.2496 a_f -> k/T0 = 2 DERIVES: FND-114 upgrades
  ADOPTED-ADJUDICATED -> DERIVED; the alpha chain's inheritance
  rider strengthens programme-wide; the FND-117 factorization is
  certified dynamically exact.
- any other value above the rigidity threshold -> the implied r_s
  lands in the FND-122 CONFLICT region (off-point in
  (0, 0.3529 a_f]) or, for c_L,f < 2.390 c (r_s > 0.3529 a_f),
  FIRES EM-RECON-032's falsifier (core existence).
- below the stretch-projection transmission -> section 5 fires
  FIRST (internal inconsistency, adjudication of the SHIN
  structure or the floor).
NO NULL REGION EXISTS.

## 7. HOUSE RULES BINDING ON THE RUNNING SESSION
Bars may add detail but not weaken seals, window, or sheet; failures
registered and kept; corrections named; every factor sourced; the
claim registers whichever outcome fires, at full volume; doc sync
(KNOWN_LIMITATIONS + README status line) owed in the SAME release
as the verdict; release note + sync_doc_facts.py per the standing
release rules.

## 8. WHY THIS COMMISSION MATTERS (for the fresh session's context)
k/T0 = 2 is the corpus's most load-bearing adopted constant
(FND-114 rider on the alpha chain and beyond). This computation is
the first with the registered standing to convert it to a theorem
-- or to send the SHIN angles to adjudication -- with every outcome
pre-registered and no way to leave empty-handed.
