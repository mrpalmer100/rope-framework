# COMMISSION CASIMIR-PLATE (F3) -- RESULTS (2026-09-05)
Charter analysis/CASIMIR_PLATE_charter_LOCKED.md with A1 (piston calibration),
A2 (plate condition from E-RECON / EM-023), A3 (implementation), A4 (budget),
A5 (v4 discharged). Leg 1 halted on CAS-BC-OPEN and was lifted the same day
(EM-023). Legs 2-4 ran on the author's laptop (49 k-points, ~8.5 h; checkpoint
analysis/casimir_plate_ckpt.pkl); Legs 3-5 in casimir_verdict.py, run once.

## INSTRUMENT FAULT 12 (found at the verdict, disclosed first)
The laptop patch that halved the angular nodes (A4) left the weight array at
the full angle count, so the flattened weights were paired with the wrong
nodes: sum W = 0.036 instead of pi k_c^2 = 1.240. The spectra are correct
(one per k-point); only the quadrature weights were wrong. Found by the
cross-check sum W; weights recomputed from each node's radius and the
Gauss-Legendre rule (exact, no re-solve), checkpoint annotated, the first
verdict run (analysis/casimir/verdict.log) kept as the faulted run, the
corrected run (verdict_corrected.log) is the run of record. Ledger entry 12.

## VERDICT: ** CAS-SHAPE-FAIL ** by the locked fit -- explicitly PRE-ASYMPTOTIC,
## with the coefficient structure of CAS-CHANNEL-KILL already visible
Reading (ii), the locked statistic (log-log slope over the top three rungs):
force exponent p = 4.26, outside [3.9, 4.1]. Rung-by-rung: 4.56 (10->20),
4.30 (20->30), 4.18 (30->40), falling monotonically toward 4 from above and
not there within the chartered ladder. The GR54 lesson applies: this reads
"not yet the d^-4 law at d <= 40", not "not a d^-4 law".

## What was measured (reading (ii), E = (1/2) S sum omega, S = 1; d_eff = d + 1)
   d      E(d)          K d_eff^3      local p_F
   10   -3.988e-5       0.05308
   20   -3.985e-6       0.03691          4.56
   30   -1.101e-6       0.03280          4.30
   40   -4.522e-7       0.03117          4.18
ATTRACTIVE at every rung (the sign control: pass). K is converging from
above (successive changes 0.016, 0.004, 0.0016; ratio ~0.3; Aitken asymptote
~0.0305; Richardson 0.0306 / 0.0314). Against the two-polarization Casimir
coefficient pi^2/720 = 0.01371 (S_eff = hbar), the wound medium gives
K / K_2 = 2.23-2.29, i.e. about 4.5 scalar-polarization units (pi^2/1440
each) where electromagnetism has 2. The natural accounting: the two
transverse bands supply ~2 units and the longitudinal carrier, constrained
at k_par != 0 (A2) and three times faster (c_L,f = 3.00 c_T, FND-126),
supplies ~3 (Casimir energy scales with the mode speed): 2 + 3 = 5 units =
0.0343, against the measured 0.031 still converging. This is the
CAS-CHANNEL-KILL structure (K_tot / K_2 - 1 = 1.2 >> 0.03 with the excess
traced to the longitudinal carrier). It is NOT rendered: the sub-verdicts
are licensed only under a p in window, and p is 4.26 pre-asymptotic.
Reading (iii) (warm-weave log-sum): p_F = 3.56, local 3.57 / 3.53 / 3.61
(the classical d^-3 law would be 3; also pre-asymptotic), K d^3 rising.
Reading (i) (k_par = 0 coherent-winding slice): p_F = 2.89, local 2.47 ->
3.07: a different, slower law; the plate does not act on the winding family
as a Casimir force. Plate orientation (111): UNREACHED (A3).

## Controls
v1 SHIN6 reproduced; v2/v3 scalar controls p = 4.002 and K = pi^2/1440 to
0.01 pct after A1; v4 discharged (A5: the as-run quadrature reproduces the
scalar control to 0.2 pct at every rung); v5 L-spread on the normalized
piston; v6 clean room (hbar, the experimental values and pi^2/240 appear
only in Leg 5 and the control leg).

## What this establishes
1. The wound mesh with the derived plate condition (tangential displacement
   pinned, EM-023) produces an ATTRACTIVE plate force from its carried modes
   alone, with no zero-point continuation and no subtraction by hand
   (ZP-CONV). The sign is a result.
2. Its d-dependence approaches the d^-4 law from above; at d = 40 the local
   exponent is 4.18. The asymptotic regime is beyond the ladder.
3. The magnitude is 2.2-2.3 times the two-polarization EM coefficient in the
   S = 1 unit, converging from above, with the excess accounted for by the
   longitudinal carrier the derived plate condition constrains. If the
   asymptote holds, the verdict is CAS-CHANNEL-KILL: the wound mesh's
   plates are not electromagnetic plates -- the tension channel feels the
   conductor too. Whether S_eff can then be pinned (CAS-PIN) becomes a
   question about the transverse bands alone; OPEN.
4. The coherent-winding reading is a different, slower law: the plate does
   not act on the winding family as a Casimir force.

## Named next-order (its own charter; the GR54-X precedent)
A CAS-X extension: rungs d = 60 and 80 at L = 240 with the same instrument
(cost ~2 x this run per rung), verdict forms carrying CAS-ASYMPTOTIC (p in
window on the extended top three, K converged to 3 pct) and CAS-STILL-
TRANSIENT, with CHANNEL-KILL and the PIN / GAP / OVER sub-verdicts licensed
only under CAS-ASYMPTOTIC; plus a channel-resolved reading (transverse bands
vs longitudinal, by eigenvector projection on the same spectra) so the 2 + 3
accounting is measured, not inferred. Cheaper first step: a d = 50 rung at
L = 150 (local exponent 4.18 -> ~4.1 expected).

## Consequences for the desk
- FINE-GATE Q2: the Casimir per-mode action is still the relation that would
  close the a_f gate; it is now behind an extension run, not behind the
  dictionary. CAS-PIN not reached.
- No claim drafted before the author reads; the sign result and the
  pre-asymptotic exponent are the registrable content.
- Prediction 32 / FND-132 untouched.

## Process
Verdict computed once under the locked forms; the pre-asymptotic reading is
stated alongside the letter of the verdict, as GR54's amendment requires,
rather than substituted for it.
