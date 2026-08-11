# Commission NU — the downstream re-evaluation sweep at the pinned Sigma: locked bars

*Locked 2026-08-10, before any computation. Follows Commission MU (FND-030
draft), which pinned Sigma to the lattice band 3.61–3.70e35 J/m^3 and demoted
the 5.10e35 registration to historical.*

## Commission
Commission MU's B5(d) itemized the downstream bill: four registered claim
groups conditioned numerically on Sigma = 5.1e35. This session pays it. The
sweep is a RE-EVALUATION, not a re-derivation: each item's registered formula
is re-run at the pinned band, and the verdict for each is one of
UNCHANGED / SHIFTED (number moves, conclusion stands) / FLIPPED (a registered
verdict reverses) / DEAD (the item was load-bearing on 5.1e35 itself).
A FLIPPED or DEAD verdict must be reported with the same prominence as a
survival.

## The sweep list, fixed in advance (nothing added or dropped after computing)
S1 QGATE-009's invoice, all six confrontations re-run at Sigma = 3.61–3.70e35:
   (1) rho_vac = Sigma/c^2 and its multiple of nuclear density (the fence);
   (2) wave-speed identity (expected magnitude-blind, confirm);
   (3) the Schwinger diagnosis: E_crit = sqrt(Sigma/eps0) vs the Schwinger
       field — does the "five orders above" separation that made the
       matter-sector-QED debt coherent survive at the smaller Sigma?
   (4) the tension chain at the working point (M-point already lattice-based:
       confirm T0 = Sigma a^2/3 closes);
   (5) the mesh birefringence suppression Delta_n ~ 5e-34 rescaled by 1/Sigma —
       does "ten orders below any polarimetry" survive?
   (6) the proton-to-vacuum energy-density ratio (was ~12%) — recompute; if it
       crosses O(1) the perturbative-hierarchy question sharpens and must be
       flagged.
S2 EM-RECON-029 P29 (the one-number lock) and EM-RECON-027's kappa_0 bound:
   kappa_0 = c/sqrt(eps0 Sigma) evaluated at the band; the vacuum density
   floor rho >= 4.5e7 kg/m^3 statement re-checked; the registered
   kappa_0 <= ~26–50 band replaced or confirmed.
S3 ELEC-049 Ledger B: w = 5.78e-17 m was conditional on Sigma = 5.1e35.
   Re-derive w at the pinned band and at the M-point; state whether any
   claim re-based onto Ledger B (ELEC-044/045/046/047 re-basings) changes
   verdict. Note: those chains are already dead — the question is whether the
   deaths WEAKEN, which must be reported if so.
S4 QGATE-008's conditional chain ("if collective reconnection and
   Sigma >= 5.1e35, then hbar = W_collective"): the antecedent's Sigma clause
   now fails at the pinned band. State what this does to the chain's status —
   noting the chain was already killed by ELEC-047 on the recruitment side —
   and whether the QGATE-018 threshold-test conclusion (PVLAS excludes
   Sigma-small) still holds at 3.6e35, i.e. confirm the pinned band is still
   on the large-Sigma side of the PVLAS threshold.

## Locked bars
B1 Every S-item reports its verdict class (UNCHANGED/SHIFTED/FLIPPED/DEAD)
   with the old number, the new number at both band edges, and the registered
   inequality it faces.
B2 THE HEADLINE RISK, named before computing: S1(3). At Sigma = 3.6e35,
   E_crit = sqrt(Sigma/eps0) drops by sqrt(5.1/3.6) ~ 1.19 — if this brings
   mesh nonlinearity back within reach of any registered field scale, the
   coherence of the matter-sector-QED debt is damaged and must be said. The
   bar: E_crit must remain >= 100x the Schwinger field for the "mesh linear
   through all known fields" statement to stand as registered.
B3 S1(6): if the proton/vacuum ratio exceeds 30%, the perturbative-hierarchy
   flag escalates from "question filed" to "named tension"; if it exceeds
   100%, FLIPPED and the gravity sector inherits an immediate obligation.
B4 A verifier: the sweep's arithmetic goes into a benchmark script that fails
   if any registered input drifts, extending mu_sigma_provenance.py.
B5 HONESTY: the sweep evaluates at BOTH band edges (3.61 and 3.70e35) and
   carries the band's known model dependence (R_eq^-2 scaling) so any future
   width re-measurement can be propagated by inspection. No downstream claim
   may be marked UNCHANGED unless both edges leave its inequality intact.
