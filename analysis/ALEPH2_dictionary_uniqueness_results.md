# COMMISSION ALEPH-2 -- RESULTS: UNIQUENESS-DERIVED; ONE OF FOUR BLOCKERS RETIRES

*Adjudicated 2026-08-11 after bar lock
(analysis/ALEPH2_dictionary_uniqueness_bars_LOCKED.md). Benchmark:
benchmarks/em/aleph2_dictionary_uniqueness.py. EM-016's grade is
UNCHANGED and this document says so twice.*

## The theorem

**Statement.** Let a mechanical assignment be any map from the rope's
mechanical state to fields (E', B'). If two assignments predict the same
force on every test winding at every point and every velocity, they are
the same assignment up to a gauge transformation of the potentials and
the single global calibration constant already registered as an input.

**Proof, in the corpus's own registered inputs.**

1. *E is determined.* By the operational definition already in
   registered use (E = force per winding, EM-015/EM-RECON-024), a static
   test winding at a point returns E there directly. Verified
   numerically: exact recovery.
2. *B is determined.* By EM-013's Derived Lorentz law, a moving winding
   returns F/q - E = v x B. Three linearly independent test velocities
   give nine equations for three unknowns with the cross-product
   matrices spanning the space; B is recovered exactly (residual
   3.8e-16). **There is no velocity-degeneracy** -- this was checked by
   explicit inversion, as the locked bar required, not asserted.
3. *F_munu is determined* pointwise from (E, B), and by EM-003's
   Derived dF = 0 the potentials follow from F via the Poincare lemma,
   which fixes (phi, A) up to gauge -- and gauge freedom is registered
   as physical phase-convention arbitrariness (GG-004), i.e. it changes
   no observable by construction.

**The duality escape, checked rather than assumed.** The locked bar
named the E/B rotation as the freedom that would DEFEAT the claim. It is
computed symbolically and it is NOT a symmetry here: the static term
alone shifts by q(E cos t + B sin t - E), non-zero for any t != 0. And
the registered structural reason is stronger than the arithmetic: charge
is WINDING (GG-006, EM-001) and windings are the only registered
charge -- the corpus has no magnetic monopole, so a duality rotation
would map electric sources into magnetic ones the registry cannot
represent. The rotation is not available in this ontology.

## VERDICT: UNIQUENESS-DERIVED -- blocker (iv) discharged

EM-016's status ledger drops from four blockers to three. The dictionary
is not a choice presented as a mapping: given the registered charge
definition and the registered force law, **it is the only assignment
consistent with the observables.**

## EM-016's GRADE IS UNCHANGED, and here is why

Modeled it remains, on the three blockers that are NOT in this
commission's scope and were not argued around:

- **(i) SIGMA's absolute value is an input** -- measured/bounded
  (EM-RECON-014, ATLAS/PVLAS-confronted), not derived. This is the one
  freedom the theorem above explicitly leaves open, so discharging (iv)
  makes (i) MORE conspicuous, not less: the dictionary is unique up to
  exactly one number the corpus does not derive.
- **(ii) EM-010's inertial term is assumed.**
- **(iii) phi's channel identification (EM-RECON-011) is Modeled** --
  the twist-tension channel, transmitted via the twist-stretch lock.

Upgrading on a partial discharge would be bar-shopping and is refused.

## What this changes downstream

The README's electromagnetism paragraph can now say something sharper
and still true: the dictionary is *unique* given the registered charge
and force law, and Modeled because of one undetermined calibration
constant and two mechanical assumptions -- rather than the flat "Modeled,
not Derived" which reads as though the mapping might be arbitrary. It is
not arbitrary; it is pinned up to a scale.

## Named next-orders (the remaining three, priced)

- **(iii) is the tractable one:** derive phi's channel identification
  from the twist sector rather than modelling it. If it falls, EM-016
  drops to two blockers, both of which are honest inputs rather than
  soft identifications.
- **(i) is a calibration** and may be irreducible -- the corpus should
  decide whether it regards SIGMA as an input on the same footing as the
  m_e calibration, in which case it should be labelled as such rather
  than as a blocker.
- **(ii)** needs EM-010's inertial term derived from the strand engine.
