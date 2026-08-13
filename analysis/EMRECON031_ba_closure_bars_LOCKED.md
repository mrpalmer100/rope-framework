# COMMISSION EM-RECON-031 -- THE b/a CLOSURE: BARS, LOCKED BEFORE COMPUTING

Locked 2026-08-13, before any integral is evaluated. Purpose: the
forward confrontation EM-RECON-008 (Open) has awaited -- its missing
coefficient was fixed after it was filed (c4 = (k - T0)/8 exact per
EM-RECON-009; k/T0 = 2 adjudicated as the corpus's ONE registered
medium value per FND-027 bar 2), and EM-RECON-009 left exactly one
uncomputed piece: the mode-profile prefactor b/a it flagged
honestly. With the coefficient fixed, b/a is COMPUTABLE from
registered structure and the equilibrium spacing ratio d0/xi becomes
a ZERO-FREE-PARAMETER number confronting two measured ratios.

## Scope, fixed at lock

IN: the two-mode equilibrium spacing d0/xi computed from the full
registered energy (quadratic mode-overlap attraction + quartic
extensibility repulsion), confronted against the two measured
ratios EM-RECON-009 registered: NUCLEAR d0/L = 1.9 fm / 1.4 fm =
1.36 and CHEMICAL bond/healing = 0.74 A / 0.443 A = 1.67.
OUT (disclosed, remaining open): the FERROMAGNETIC magnitude (no
registered map from c4 to a ferro number exists; inventing one would
be the fitting EM-RECON-008 warned against) and the ABSOLUTE Yukawa
range L (needs the nuclear mode mass, i.e. the operating amplitude
in physical units -- the RATIO is what this commission predicts).

## Inputs, all registered, none free

- c4 = (k - T0)/8 with k/T0 = 2 (adjudicated): c4 = T0/8. NO other
  value may be evaluated.
- Mode profiles: exponential, |grad psi_i|(x) = g exp(-|x -+ d/2|/xi)
  (the registered mode-overlap class; 1D transverse line integrals,
  the same idealization EM-RECON-005/006/009 used).
- Operating amplitude: g = g* = sqrt(4 T0/(k - T0)) = 2.0000 at
  k/T0 = 2 -- the SATURATION STRAIN already registered as the Kerr
  onset (k_independent_windows window 3), i.e. the strain at which
  the quartic correction equals the quadratic term. The core
  condition: a mode develops its repulsive core where its own
  nonlinearity saturates. This identification is the commission's
  one modeling step and is STATED AT LOCK, before any number exists;
  a sensitivity sweep over g in [1, 3] is mandatory disclosure
  either way.
- Energy, FULL, no model-form truncation: E(d) =
  -(T0/2) I_cross2(d) + c4 [4 I_31(d) + 6 I_22(d) + 4 I_13(d)],
  where I_cross2 = INT g1 g2 dx and I_pq = INT g1^p g2^q dx, all
  exact/numeric on the locked profiles. NOTE DISCLOSED AT LOCK: the
  registered compact model (-a e^{-d/xi} + b e^{-2d/xi}) kept only
  the g1^2 g2^2 quartic term; the g1^3 g2 terms decay at the SAME
  rate as the attraction and renormalize it. This commission
  computes the full E(d) and finds the minimum directly, so the
  truncation question is bypassed, not adjudicated.

## Measurement and verdict bands, pre-committed

- M1: d0/xi = argmin E(d)/xi at g = 2, c4 = T0/8. NO-MINIMUM is a
  registrable outcome (FAIL, kept).
- M2: sensitivity d0/xi over g in [1, 3] (disclosure, not verdict).
- BANDS (final, the registered log-weak honesty level ~20-25
  percent): per target, PASS iff |d0/xi - target|/target <= 0.25.
  Overall: PASS-BOTH / PASS-ONE (name which) / FAIL-BOTH /
  NO-MINIMUM. PASS-BOTH converts EM-RECON-008's joint-resolution
  promise into a measured fact at zero free parameters; PASS-ONE or
  worse is kept and EM-RECON-008's Open stands for the missed
  sector(s).

## Guards

- G-A: targets in context (1.36, 1.67; the needed-b/a figures 1.94
  and 2.66 from EM-RECON-009). Protection: every input above is
  registered with its provenance named; the amplitude identification
  is locked before computing; bands final; no re-runs at other g or
  k/T0.
- G-B: log-weakness cuts BOTH ways and is disclosed: d0/xi depends
  logarithmically on prefactors, which makes PASS easier and the
  discriminating power low. The verdict therefore claims FORM-level
  consistency at the registered honesty level, not a sharp
  determination -- same grammar as the registered 16 percent
  vibrational check.
- G-C: this commission touches EM-RECON-008's status only as far as
  the verdict licenses; the ferro sector and absolute L remain open
  regardless of outcome; adverse outcomes pre-authorized.

## Deliverables

benchmarks/em/emrecon031_ba_closure.py;
analysis/EMRECON031_ba_closure_results.md; claim via
tools/add_claim.py; annotations to EM-RECON-008, EM-RECON-009,
FND-027, NUC-004; CHANGELOG; HANDOFF; verify_corpus --quick; re-zip;
present_files. The v3.25.0 release cut follows this session.
