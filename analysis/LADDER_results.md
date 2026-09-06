# COMMISSION LADDER -- RESULTS (2026-09-05)
Charter analysis/LADDER_charter_LOCKED.md (+ the Leg 0 amendment and the
Leg 1 dispersion record, both before any filling). Logs analysis/ladder/.
Grade ceiling on every line: Modeled-CONDITIONAL on mode quantization
(QGATE) and the two-per-level exclusion rule (Conjecture); their
falsifiers inherited. Targets loaded once, in Leg 5.

## VERDICTS
  Q1  ** ASYM-FORM **  (shape derives in the continuum limit; the
      coefficient overshoots by R = 1.5-1.9, A-flat -> a SCALE miss;
      the discrete-grid exponent fits are NO CALL, see below)
  Q2  ** PAIR-ROUTE-SPLIT **  (the ladder's stiffness is not a constant:
      delta_top ~ A^(-0.81); P1 fails)
  Q3  ** NUN-OFF-LATTICE ** for two of three path classes, NO LOOPHOLE
      in any (no path class gives -1/2; R4's non-locality stands)

## Leg 0 -- controls
v1 NUC-022 reproduced BIT-EXACTLY (E(40,4) = 1137.068, deficit 6.9759,
   continuum E_F/3 = 12.8 at E_F = 38.4) -- but only on a CUBIC BOX of
   side 2R(A), two per (nx,ny,nz) state, m = 939.0 MeV. NUC-022's text
   says "a sphere of radius R"; the spherical Dirichlet ladder gives
   1587 and a median a_A of 32. The calibrated instrument is the one
   NUC-022 ran; the wording discrepancy is recorded for its face.
v2 dispersion: derived in Leg 1 from registered mechanics (see below);
   agreement with NUC-004's mode structure is by construction (the
   evanescent-tail mass gap kappa = 1/L).
v3 Delta_E(A, 0) = 0 exactly at every A, every dispersion.
v4 R4 reproduction: the star form returns -1/2 EXACTLY (samekh re-run).
v5 NUN reproduction: the four channel exponents (0, 0 + A^-2/3
   remainder, 0, -1/2) reproduced from the reused instrument.
v6 clean room: no target in any Leg 2-4 file.

## Leg 1 -- THE DISPERSION (derived, no Fermi-gas form)
The bundle's transverse modes at mu = T/c^2 propagate at c; NUC-004's
mode-overlap binding is the evanescent tail of a mode with mass gap
kappa = 1/L (L = 1.4 fm, the registered INPUT range). Hence
   E(k) = hbar c sqrt(k^2 + kappa^2)      (gap hbar c kappa = 141 MeV)
with the massless limit E = hbar c k carried alongside. The gap cancels
in every difference. The nucleon mass enters NOWHERE in the derived
ladder; the effective inertia at the Fermi surface is E_F/c^2 ~ 303 MeV.

## Leg 2 -- Q1 on the calibrated box (A = 16..208; N - Z = 2.. up to 0.3A)
Exponents by the locked log-log fits on the DISCRETE grid: q = 1.52 for
the derived ladders AND for the textbook control alike, m undefined
(degenerate box shells give zero deficits at several (A, N-Z), e.g. A =
56). The instrument cannot resolve the exponents even for the known
quadratic gas: NO CALL on S1/S2 by discrete fit. In the CONTINUUM LIMIT
of the same object (exact, standard) every dispersion gives q = 2 and
m = -1 with a_A,ladder = k_F E'(k_F)/6:
   textbook   12.8 MeV      derived massive 39.5 MeV     massless 44.7 MeV
Discrete medians (populated range, A >= 40): 11.0 / 34.7 / 39.4.
S1, S2 pass in the continuum; S3 is evaluated in Leg 5.

## Leg 3 -- Q2 (the ladder-built R4)
The top-level spacing delta_top(A) of the derived ladder: 42.3 (A = 16),
27.2 (40), 14.4 (56), 11.8 (80), 8.0 (120), 7.4 (140), 6.3 (208) MeV --
log-log slope -0.81 in A. Read into R4 as the mode stiffness, v0_ladder
is NOT an A-independent number; the R4 form's -1/2 is the form's (v4),
the stiffness the ladder supplies falls with A.

## Leg 4 -- Q3 (the three 1D strand-path classes, NUN's D1/D2 method)
Smearing (bilinear, amplitude 1/ell on ell sites): exponent 0 for every
class (fixed cost). Band delocalization on an open chain of ell sites:
remainder 2(1 - cos(pi/(ell+1))) ~ pi^2/ell^2, i.e. exponent -2p for
ell ~ A^p: chord -2/3 (analytic; numerical fit -0.60 from integer ell),
surface walk -4/3 (fit -1.31), space-filling -2 (fit -2.00). Chord on
the lattice; surface walk and space-filling OFF the lattice {0, -1/3,
-2/3, -1} -- new exponents with their mechanism (finite-size remainder
of a 1D band). Distance from -1/2: 0.10, 0.81, 1.49: NO LOOPHOLE.

## Leg 5 -- CONSEQUENCE (targets loaded once)
a_A(table) = 23 MeV (SEMF; the AME A-binned coefficients cluster there
from A = 40 up); v0 = 16.97 MeV with FND-071's band.
Q1: the derived ladder alone gives 34.7-39.5 (massive) / 39.4-44.7
(massless): R = 1.5-1.7 (massive) or 1.7-1.9 (massless) OVER, and A-flat
in the continuum. The label term (NUC-019's linear |N-Z| A^-1/3, D4's
required sum) adds ~13 MeV-equivalent at (40, 4) falling as 1/(N-Z) --
the sum is larger and its shape worse; per D4 that is a finding against
the label term's asymmetry content (its cost belongs elsewhere). S3
FAILS by R ~ 1.5-1.9, A-flat -> ASYM-FORM: the miss is a SCALE. Named
defendant: the ladder's inertia -- the derived dispersion carries no
nucleon mass (E_F/c^2 ~ 303 MeV at the Fermi surface where nature's
ladder carries 939), and a_A scales with E'(k_F). The textbook ladder
UNDERSHOOTS (12.8, 56 pct) and the derived one OVERSHOOTS (39.5, 170
pct): the empirical 23 sits between the massless-mode and the massive-
nucleon dispersions. That bracket is the result.
Q2: delta_top crosses 16.97 near A ~ 50 but runs 27 -> 6 MeV across the
table; P1 fails: PAIR-ROUTE-SPLIT. FND-081's chain already closes on
data; the ladder's reading of "mode stiffness" is the defendant. NUC-030
does not return to adjudication on this leg.
Q3: NUN-OFF-LATTICE (two classes), NUN-CLOSED for the chord, no
LOOPHOLE anywhere: R4's non-locality is necessary over the enumeration
NUN named as owed. NUC-030 strengthened.

## What is named
- NUC-022 rider: the instrument was a box, not a sphere (v1 finding).
- The asymmetry bracket 12.8 (nucleon-mass ladder) < 23 < 39.5 (bundle-
  mode ladder) is the sector's sharpest statement of the missing
  inertia: a dispersion with the nucleon's mass AND the bundle's
  speed is what the derived ladder lacks -- next-order, its own
  charter, zero new constants only if the mass enters through a
  registered object (the knot-count mass mechanism NUC-001).
- No claim drafted before the author reads.

## Process
One session (two budgeted). Dispersion recorded before filling; targets
in Leg 5 only; the discrete-fit weakness disclosed rather than smoothed.
