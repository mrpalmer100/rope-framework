# COMMISSION EM-RECON-032 -- THE WOUND-BUNDLE EFFECTIVE c4: BARS, LOCKED BEFORE COMPUTING

Locked 2026-08-13, before any number is evaluated. Purpose: compute
the effective quartic (extensibility) coefficient of a coarse strand
that is, per GRANT-SUBSTRUCTURE-TIGHT (FND-087), a two-level wound
bundle at the REGISTERED derived angles -- no free parameters -- and
re-run EM-RECON-031's failed closure at whatever coarse c4 survives.
This targets EM-RECON-031's suspect (ii): the homogeneous-strand
idealization behind c4 = (k - T0)/8.

## The mechanical model, fixed at lock (scope honest)

- STIFF-HELIX PROJECTION MODEL: when the coarse strand elongates by
  strain eps (the transverse-field elongation eps = sqrt(1+g^2) - 1
  of EM-RECON-009), each winding level transmits to its fibers the
  PROJECTED strain: eps_fiber = s x eps with
  s = sin^2(psi1) x sin^2(psi2), the two levels compounding
  multiplicatively (level-2 lives in level-1's local frame). Fiber
  arc-length factors appear identically in the linear and quadratic
  terms and cancel in every ratio used below.
- Radius held fixed (the STIFFEST transmission); free-radius
  unwinding only LOWERS s. Therefore s is an UPPER bound on
  transmission and every "required fine stiffness" derived from 1/s
  is a LOWER bound. Disclosed.
- Bending and torsion EXCLUDED: kb is separately priced (SHIN7) and
  torsional stiffness enters no registered quartic; this commission
  prices the EXTENSIBILITY channel only, same as EM-RECON-009.
- Angles, registered, no freedom: sin^2(psi1) = 1/3 (FND-088);
  sin^2(psi2) = (15 + 2 sqrt(30))/35.

## The reading question, enumerated at lock (the real adjudicand)

The medium constant k/T0 = 2 (FND-027) was fitted to COARSE
observables (spacings). Under substructure it can be read two ways:
- READING-COARSE: k/T0 = 2 is the coarse-EFFECTIVE ratio (where the
  measurements live). Then the coarse c4 = T0/8 stands by
  definition, and the fine ratio is DERIVED from the transmission:
  k_f/T0_f = (k/T0)_coarse / s.
- READING-FINE: k/T0 = 2 is the fine-level material ratio. Then the
  coarse effective ratio is k_eff/T_eff = 2 s and the coarse quartic
  is c4_eff = (2 s - 1)/8 x T_eff.
ADJUDICATION RULE, pre-committed: EM-RECON-009's stability theorem
(a repulsive core exists iff effective c4 > 0; matter exists) is the
judge. A reading whose coarse c4_eff <= 0 is EXCLUDED BY REGISTERED
PHYSICS PLUS THE EXISTENCE OF MATTER. If exactly one reading
survives, it is ADOPTED AS DERIVED-BY-EXCLUSION (this is a logical
exclusion, not an author's grant: no new premise, only registered
statements confronted). If both survive, the ambiguity is reported
to the desk.

## Measurements, locked

- M1: s from the registered angles (exact).
- M2: c4_eff under READING-FINE = (2 s - 1)/8 (sign is the verdict).
- M3: required fine stiffness for core existence: (k_f/T0_f)_min =
  1/s (lower bound per the stiff-helix disclosure).
- M4: derived fine ratio under READING-COARSE: k_f/T0_f = 2/s;
  CONSISTENCY CHECK: 2/s >= 1/s must hold (trivially true) --
  reported as the margin 2/s vs 1/s.
- M5: THE CLOSURE RE-RUN at the surviving reading's coarse c4, with
  EM-RECON-031's benchmark, amplitude, sweep, and +-25 percent bands
  INHERITED UNCHANGED (no re-locking, no band motion). If the
  surviving c4 equals T0/8, the re-run is executed anyway as a
  confirmation and its verdict is expected to inherit EM-RECON-031's
  FAIL; that expectation is disclosed here, before computing.

## Verdict grammar, pre-committed

- READING EXCLUDED / READING DERIVED-BY-EXCLUSION (name which).
- CLOSURE: RESCUED (bands pass under a renormalized c4) /
  UNCHANGED-FAIL (surviving c4 = T0/8, EM-RECON-031's verdict
  inherited) / DOUBLY-FAILED (renormalized c4 also misses).
- BYPRODUCTS registered regardless: the derived fine stiffness ratio
  and the core-existence demand on any future fine-level
  determination (a falsifier: any independent measurement of
  k_f/T0_f below 1/s contradicts the existence of the extensibility
  core on a wound bundle under the stiff-helix bound).

## Guards

- G-A: all inputs registered (angles, k/T0 = 2, the stability
  theorem); zero continuous freedom anywhere; the model class
  (projection-only, fixed radius) is locked and its bias direction
  disclosed (s is an upper bound on transmission).
- G-B: pre-lock scoping disclosed: s = (1/3)(0.7416) ~ 0.247, so
  2 s ~ 0.49 < 1 -- READING-FINE is EXPECTED to be excluded (its
  coarse quartic would be negative, abolishing the core and matter
  with it), and READING-COARSE is expected to survive with
  k_f/T0_f ~ 8. The expected overall verdict is therefore
  READING-COARSE DERIVED-BY-EXCLUSION plus UNCHANGED-FAIL on the
  closure. Disclosed in full so the landing cannot be dressed as
  discovery; the grammar binds regardless, and the session's value
  is the derived fine ratio, the falsifier, and the refutation on
  the record of the "winding rescues the closure" candidate this
  commission was asked to test.
- G-C: adverse and null outcomes pre-authorized; no model additions
  after numbers exist.

## Deliverables

benchmarks/em/emrecon032_wound_c4.py;
analysis/EMRECON032_wound_c4_results.md; claim via
tools/add_claim.py; annotations to EM-RECON-031, EM-RECON-009,
FND-087, FND-027; CHANGELOG; HANDOFF; verify_corpus --quick; re-zip;
present_files. The v3.25.0 release cut follows.
