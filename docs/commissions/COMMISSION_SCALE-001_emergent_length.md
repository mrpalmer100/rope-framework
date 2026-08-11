# COMMISSION SCALE-001 — the Emergent Mesoscopic Length Audit

*Chartered 2026-08-11, post-v3.17.0. Origin: the corpus's own ranked
next-order (the ambient/collective g-charter, FND-045/047), sharpened by
an external reviewer whose framing is adopted with attribution: the
question is not "find a formula that gives 90" but "what already-licensed
collective property of the ambient weave generates a stable dimensionless
correlation length of order 10^2 cells WITHOUT that number being
inserted?"*

## Status of this document

CHARTER ONLY. No mechanism has been evaluated. The target range is
SEALED (see the blinding protocol). Nothing in this file may cite,
paraphrase, or approximate the target value.

## What is being asked

FND-044 collapsed five formerly independent questions -- the L1
area-selection question (GRV-093), the vacuum packing kappa_pack, the
amplitude selection (ELEC-054), lambda's normalization, and the locking
softness -- onto ONE unknown: g = l_q/a, with N = 2g^2, lambda =
g^2/(4 pi), and A = 2.6348 l_q all slaved to it. FND-045 excluded the
first mechanism class (the single-defect energy-budget log) structurally.

THE HONEST FRAMING, adopted from the review and stated on the charter's
face: that collapse is a CONSOLIDATION, not yet an explanation. If no
registered collective property produces a stable scale in the sealed
range, the corpus learns that its one-number compression bought
bookkeeping rather than understanding -- and that is a first-class
outcome of this commission, not a failure of it.

## The blinding protocol (the commission's distinguishing feature)

The corpus has never run a blind-target audit in this sector. The
review's proposal is adopted and made mechanical:

1. **SEAL.** The target range is computed by
   `tools/scale001_seal.py --seal`, which writes a SHA-256 commitment of
   the range to `analysis/SCALE001_TARGET.sealed` and prints nothing
   else. The plaintext range is NOT written to disk in this repo at
   charter time and is not restated in any Phase 1 or Phase 2 document.
2. **PHASE 1 (classes).** The mechanism classes are enumerated and
   frozen in this charter, before any evaluation.
3. **PHASE 2 (scaling laws).** For each class, its scaling law is
   derived in terms of registered quantities and written to
   `analysis/SCALE001_PHASE2_laws.md` — WITH NO NUMBER EVALUATED. Each
   law must be expressed as g_class = f(registered inputs) with every
   input's claim ID given. A class whose law cannot be written without
   free parameters is registered UNDERSPECIFIED and does not proceed.
4. **LOCK.** Phase 2 is hashed and committed (`--lock`) before any
   evaluation. After this point the laws may not be edited.
5. **PHASE 3 (evaluation).** Every locked law is evaluated ONCE, all
   results displayed, and only then is the seal opened (`--unseal`)
   and the comparison made.
6. **DISCLOSURE.** The verdict reports how many classes were locked,
   how many were evaluable, and the full table — hits and misses alike.
   The look-elsewhere rate is computed from the number of locked
   classes against the log-width of the target range, and stated.

The protocol's purpose is precise: it makes "a mechanism landed" mean
something, because the mechanism could not have been chosen to land.

## Phase 1 — the mechanism classes, FROZEN

Adopted from the review's list, with the registry pointer that licenses
each (a class with no registered carrier is inadmissible by the
corpus's own channel-exhaustion rule, FND-MATTER-047):

- **C1 collective mode localization length** — the ambient weave's
  transverse Goldstone pair (EM-RECON-025) in a disordered crossing
  lattice; localization from crossing-strength disorder.
- **C2 correlation length near a mechanical instability** — proximity
  to the stability boundary the core coefficient defines
  (EM-RECON-009: k > T0 required for stable matter); a diverging
  length as k/T0 approaches its bound.
- **C3 bundle/recruitment coherence length** — the Casimir recruitment
  structure (FND-037) read as a coherence scale rather than a packing
  factor.
- **C4 reconnection mean-free path** — the reconnection sector's
  registered rates; the distance a strand travels between topology
  changes.
- **C5 topological screening length** — BKT-class screening on the
  registered stiffness (THM-004/005: T_BKT = pi K/2), i.e. the
  vortex-unbinding correlation length. NOTE the standing scope
  problem: the vacuum sector registers no temperature (flagged out of
  scope in FND-042's bars); this class must EITHER supply a registered
  effective temperature or be registered UNDERSPECIFIED. It may not
  import one.
- **C6 nonlinear strain localization** — the derived negative quartic
  (FND-040) as a self-focusing/soliton width.
- **C7 percolation / coordination length of the ambient weave** — the
  coverage-threshold machinery (FND-MATTER-004) read as a percolation
  correlation length.
- **C8 an eigenvalue of the full lattice dynamical operator** — the
  spectral route: a length from the dynamical matrix's spectrum rather
  than any single-defect energy budget. (The review's own emphasis,
  and the direction FND-045's structural exclusion points.)

No class may be added after this charter is filed. A class may be
withdrawn only as UNDERSPECIFIED, with its reason on the record.

## Admissibility and anti-fitting rules

1. **No inserted number.** A law containing a free O(10^2) factor, or
   an exponent chosen to land, is inadmissible. Exponents must come
   from the mechanism.
2. **Registered carriers only.** Each class cites the claims that
   license it. No new primitive is adopted by this commission; if a
   class requires one, that is a GRANT and goes to the author
   (standing rule), not into the evaluation.
3. **Scaling before magnitude.** A class earns evaluation only if its
   law is written in registered inputs at Phase 2.
4. **The kappa_pack coupling is mandatory disclosure.** Because
   kappa_pack = (g/43.0)^6 (FND-042), any successful class does not
   merely explain g -- it MEASURES the vacuum packing, and must say
   so, with the implied kappa_pack computed and confronted against the
   FND-040 floors and the FND-047 lattice bound.
5. **Drift filters apply.** Any class producing g must be checked
   against the registered ELEC-082/PRED-003-CONST drift conditions.

## Verdict grammar (pre-committed)

- **DERIVED-CANDIDATE**: exactly one locked class lands in the sealed
  range with no free parameters, passes the drift filters, and its
  implied kappa_pack is consistent with the floors. Registered
  Modeled, with the look-elsewhere rate stated and a blind
  out-of-sample demand attached before any promotion.
- **MULTIPLE LANDINGS**: more than one class lands — reported as
  WEAK, with the look-elsewhere rate doing the talking; no selection
  among them without an independent discriminator.
- **NULL (the consolidation verdict)**: no locked class lands. The
  registered finding is that no already-licensed collective property
  of the weave generates the scale, i.e. the one-number compression is
  bookkeeping and the missing physics is not in the enumerated classes.
  Registered Failed-and-kept with the inverted demand per class.
- **UNDERSPECIFIED-DOMINANT**: if a majority of classes cannot be
  written in registered inputs, that is itself the finding — the
  ontology does not yet contain enough structure to pose the question,
  which is a sharper statement than a miss.

## What this commission may not do

It may not adopt a grant, promote any claim, alter kappa_pack's floors,
or touch the SU(3)-vs-N-universality scope question (separately on the
author's desk). It may not reopen the static-electron variational
programme (the review's explicit non-priority, adopted).

## Sequence context

SCALE-001 is brick 1 of the reviewer's sequence as adjusted: (1)
SCALE-001; (2) the nuclear residual classifier (blind structural
correlation); (3) the frame-dragging COUPLING-PROVENANCE audit — note
that GRV-071 already found four of five coefficients absent from the
registered action for structural reasons, so "derive the coefficient"
is not yet runnable and the honest prior question is whether a
matter-to-rotation coupling can be derived or must be granted (author's
call); (4) the Born joint-outcome gate. The lattice-precision push
(FND-047's decision table) runs externally throughout.
