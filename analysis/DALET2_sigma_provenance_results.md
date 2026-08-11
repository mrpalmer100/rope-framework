# COMMISSION DALET-2 -- RESULTS: DIFFERENT-OBJECTS. A NAMING COLLISION, AND THE RELABEL MUST CHANGE SHAPE

*Adjudicated 2026-08-11 after bar lock
(analysis/DALET2_sigma_provenance_bars_LOCKED.md). Benchmark:
benchmarks/em/dalet2_sigma_provenance.py. Triggered by the author's
challenge to a stale session estimate.*

## The stale-value error, logged first

An earlier estimate in this session described Sigma as undecided, with
"two candidates 28 percent apart" and an unreachable arbiter, and put
the odds of a derivation at 10-15 percent. That reading was formed from
EM-016's blocker text and the older EM-RECON-014/015 claims WITHOUT
checking the FND-030 series -- which had already run a Sigma provenance
audit (FND-030, Commission MU), pinned the quantity, paid the downstream
bill (FND-031), confronted an out-of-sample prediction on the Sigma axis
(FND-032), and re-scoped the pinned object (FND-034). The author caught
it. Logged as exactly the stale-value class HANDOFF section 6 warns
about, and the warning is thereby earned rather than theoretical.

## Q1 -- SAME OBJECT? **NO.**

| quantity | value | provenance |
|---|---|---|
| EM-RECON-014's SIGMA (EM-016 blocker (i)) | ~1e25 J/m^3 | SIGMA = T0 n_L, calibrated by ATLAS light-by-light |
| FND-030's pinned Sigma_eff (FND-034 scope) | 3.61e35 J/m^3 | lattice tube data, re-scoped to measured tube tension density |

**10.6 orders apart.** And the vacuum-mesh construction sits with the
pinned one, not with the EM one: T0/a^2 gives 6.0e36 (kappa=50) and
3.0e37 (kappa=250), while Sigma_vac = 3T0/a^2 gives 1.8e37 / 9.0e37 --
all within a small factor of the pinned 3.6e35 scale's family, and all
~11-12 orders ABOVE the EM SIGMA. Reproducing the EM SIGMA would need a
line density 6e11-3e12 times SPARSER than one strand per cell face.
**No registered conversion spans that gap.**

**VERDICT: DIFFERENT-OBJECTS.** Two distinct quantities wear the letter
Sigma -- a naming collision of exactly the class already queued for
kappa, and the second such collision the corpus has found.

## Q2 -- what EM-016's blocker (i) actually is

EM-RECON-014's SIGMA is an EFFECTIVE EM-sector scale: the constant in
the field-strain calibration g = E sqrt(eps0/SIGMA), read off a
photon-photon measurement. It is not the vacuum stiffness the FND-030
series pinned from lattice tube data.

**And its only quoted determination has been withdrawn.** QGATE-007
showed unpolarized light-by-light carries no structure information --
the angular distribution is identical between Euler-Heisenberg and the
rope structure to numerical precision, with only the total rate
differing and the rate degenerate with normalization. The ATLAS pin
snapped. So EM-016's blocker (i) currently rests on a superseded
calibration, which is worse than the blocker text suggests, not better.

## Consequences for the relabel (the author has approved it; its SHAPE changes)

The relabel as previously framed -- "declare SIGMA a calibration input
on the same footing as m_e" -- was framed against the WRONG Sigma. Two
things must happen instead, and only the second is the approved act:

1. **DISAMBIGUATION (a correction, not a decision).** The two Sigmas
   must be distinguished by name throughout. This commission proposes
   the distinction be recorded as: **Sigma_eff** (the pinned lattice
   tube tension density, FND-030/034) and **Sigma_EM** (the effective
   field-strain calibration constant, EM-RECON-014). Naming is
   editorial; the DISTINCTION is a finding and is registered here.
2. **THE RELABEL, correctly scoped.** EM-016's blocker (i) concerns
   Sigma_EM. The BET-2 audit's three tests were applied to it and
   passed (sets a scale not a form; no chain derives it; the
   discriminating prediction is a SIGMA-independent ratio) -- those
   tests remain valid because BET-2 read EM-RECON-014, i.e. the right
   object. So the relabel stands, but its statement must name Sigma_EM
   and must disclose that the constant's quoted value rests on a
   superseded pin.

## The revised difficulty estimate for deriving Sigma_EM

Better than the stale estimate implied, and for a specific reason: the
FND-030 series demonstrates the corpus CAN pin a Sigma-class quantity by
provenance audit plus lattice anchoring rather than by an unreachable
polarimetry experiment. Sigma_EM has not had that treatment. Whether a
registered chain connects Sigma_EM to Sigma_eff is now an OPEN and
tractable question -- and if one exists, blocker (i) discharges by
derivation rather than by relabelling.

**That question is not answered here** (the bar confined this commission
to identity and provenance), and it should be asked before the relabel
is treated as final. Recommended as the next brick: attempt the
Sigma_EM <-> Sigma_eff bridge. If it lands, EM-016 has no blockers left.
