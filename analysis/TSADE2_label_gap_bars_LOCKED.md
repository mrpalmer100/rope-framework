# COMMISSION TSADE2 -- THE LABEL GAP RE-RUN ON POST-SHIN LENGTHS: BARS, LOCKED BEFORE COMPUTING

Locked 2026-08-13, before any energy is evaluated. Tier: DESK-SERVICE
(prices GRANT-N2-GAP, on the author's desk since FND-058 returned it).
Successor to TSADE (FND-057) and QOF (FND-058), both of which predate
the photon-sector resolution: GRANT-SUBSTRUCTURE-TIGHT (FND-087)
registered material lengths that did not exist when TSADE's candidate
list closed. This commission MAY NOT adopt or refuse GRANT-N2-GAP, may
not narrow GRANT-N2, and may not weaken FND-056's disturbance finding.
The deliverable is a priced decision, or the grant's dissolution into
a derivation, for the author.

## The bar, carried verbatim from TSADE

E_gap must EXCEED 1.4 PeV = 1.4e15 eV, the registered LHAASO photon
anchor. Evaluated at m = 1 (conservative: FND-087's soft falsifier
only forces m UP, and a larger m raises every fine-scale candidate).

## Conventions, fixed at lock (the borderline decider)

- E(L) = hbar c / L exactly, TSADE's convention, hbar c = 1.97327e-7
  eV m. FND-060's theorem states the ceiling as hbar c / a UP TO AN
  O(1) STRUCTURAL FACTOR; therefore the verdict grammar carries an
  AT-BAND cell: CLEARS iff E >= 1.4e15 eV exactly; AT-BAND iff E in
  [1.4e15/pi, 1.4e15 * pi] but below clearing; MISSES below that.
  An AT-BAND candidate can neither close nor confirm the disturbance
  on its own; it reports the O(1) question it hangs on.
- lambda(E) = 2 pi hbar c / E (the photon wavelength at the anchor):
  lambda(1.4 PeV) = 8.855e-22 m; lambda/4 = 2.214e-22 m.

## The label-carrier assignment, ENUMERATED AT LOCK, BOTH EVALUATED

GRANT-N2's text ("STRANDS carry one of N labels") predates FND-087,
under which the vacuum strand IS a bundle of n_sub sub-strands. Two
readings, neither privileged, no registered statement selects one:

- L-STRAND: the label is a property of the coarse strand. Candidate
  scales are the coarse registered lengths (TSADE's table stands).
- L-SUB: the label is a property of the sub-strand (the coarse
  strand's label constituted by its sub-strands, colour-like).
  Candidate scales are the fine registered lengths.

## Candidates (CLOSED list)

Carried verbatim from TSADE, values reproduced not recomputed
(analysis/TSADE_label_gap_results.md): G1 T0 a; G2 hbar c/a; G3
hbar c/d_c; G4 hbar c/a_disp (cleared, but killed as unregistered by
FND-058 -- carried for completeness, not available); G5 sqrt(T0
hbar c). All L-STRAND.

New, from FND-087's registered windows (all L-SUB):
- G6 hbar c / a_f AT THE WINDOW EDGE a_f = lambda/4 (the adopted
  bound is a_f <= lambda/4, so this is the candidate's LOWER bound;
  the true a_f can only be smaller and the gap only larger).
- G7 hbar c / p at the pitch window edge p = lambda/4 (same lower-
  bound logic; a_f < p <= lambda/4).
- G8 the fine locking energy T0_f a_f = (T0/n_sub) a_f, REPORT ONLY:
  n_sub is underived (FND-087's price), so G8 is a window, not a
  number. May inform, may not decide.
- G6' THE CONSISTENCY READING, dependency path stated at lock: by
  FND-060's ceiling theorem applied at the FINE level, the fine mesh
  can carry a photon of energy E only if its ceiling ~ hbar c/a_f
  (up to the same O(1)) is at least E. The substructure was adopted
  TO carry the m x 1.4 PeV photon (FND-087's stated purpose). If the
  adoption is consistent, then hbar c/a_f >= m x 1.4 PeV / O(1), and
  any excitation whose minimum size is the sub-strand scale --
  including a label excitation under L-SUB -- costs at least the
  carried photon energy up to the same O(1). This is a DERIVATION
  ROUTE (the gap from the carrier's own consistency), not a new
  length; it stands or falls with FND-060's theorem transferring to
  the fine mesh, which is the route's named condition.

## Verdict grammar, pre-committed

Per assignment, then overall:
- DERIVED (at an assignment): a registered candidate CLEARS and the
  label mechanism selects it on stated grounds.
- CONDITIONALLY-DERIVED: clears only via a named condition (e.g.
  G6' via FND-060-at-fine-level, or an AT-BAND candidate plus a
  favorable O(1)); the condition and what would certify it are
  named.
- UNDERIVABLE (at an assignment): every available candidate misses.
Overall:
- DISSOLVED: both assignments reach DERIVED or CONDITIONALLY-DERIVED
  with the same condition class -- GRANT-N2-GAP is unneeded up to
  the named conditions; the author is handed a certificate list
  instead of a grant.
- ASSIGNMENT-SPLIT: the assignments disagree -- the grant decision
  reduces to the assignment question plus any conditions; both are
  named for the author.
- UNDERIVABLE-STILL: both assignments miss; GRANT-N2-GAP stands as
  the only route at its FND-056 price.

## Guards

- G-A: the m = 1 floor and the lower-bound status of G6/G7 are
  disclosed; candidates may only be evaluated at their registered
  window edges, never at interior points chosen after seeing the
  bar.
- G-B: pre-lock scoping disclosed: hbar c/(lambda/4) = (4/2pi) x
  1.4 PeV = 0.891 PeV, which is AT-BAND (inside a factor pi of the
  bar), not clearing -- so the arithmetic outcome at the window edge
  is FORESEEN to hang on the O(1) and on G6'. Disclosed so the
  landing cannot be dressed as discovery; the grammar binds
  regardless.
- G-C: no candidate additions, no rescaling, mandatory full-table
  disclosure above and below the bar alike; adverse outcomes
  (UNDERIVABLE-STILL) pre-authorized and registrable without rescue.
- G-D: resemblance is not identification -- an energy landing near
  the anchor is arithmetic; the label mechanism's selection of a
  candidate needs stated grounds.

## Deliverables

benchmarks/foundations/tsade2_label_gap_rerun.py;
analysis/TSADE2_label_gap_results.md; claim via tools/add_claim.py;
annotations to FND-056, FND-057, FND-058, FND-054, FND-087;
CHANGELOG; HANDOFF; verify_corpus --quick; re-zip; present_files.
