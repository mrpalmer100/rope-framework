# COMMISSION C1 -- THE FINE-CEILING EXHIBITION ON THE SHIN ENGINE: BARS, LOCKED BEFORE COMPUTING

Locked 2026-08-13, before any spectrum is computed. Purpose: the
certificate named by FND-098 and owed by FND-099's ruling -- exhibit
that FND-060's band-ceiling theorem TRANSFERS to the wound fine mesh,
i.e. that the fine transverse operator's ceiling is S x c/a_f with S
an O(1) structural factor large enough that the label gap clears the
1.4 PeV anchor at the registered window edge. RIDE-ALONG: the 1/N
composition consistency reading armed by FND-099.

## The certificate condition, pre-committed

At the window edge a_f = lambda/4, hbar c/a_f = (4/2pi) x 1.4 PeV, so
the gap clears the anchor iff the structural factor satisfies

    S >= pi/2 = 1.5708.

C1-CERTIFIED iff S >= pi/2 on the ADJUDICATING wound member (f = 1/5,
the SHIN6 isotropy-capable case, at the derived angles) AND on the
straight control, with the sampling stability bar passed. Any lower S
is C1-FAILED, kept, and certificate C2 (a >2.2 PeV photon) remains
the label gap's only firming route. m = 1 throughout (conservative;
larger m only helps).

## Instrument, inherited VERBATIM from SHIN6 (no retuning)

benchmarks/foundations/shin6_3d_bloch.py: the 18-neighbour
central-spring vector lattice with the g = 2 shell weighting (the
null-isotropy calibration, locked addendum 4 of the SHIN6 arc), the
two-level derived winding (psi1 = arcsin(1/sqrt(3)), psi2 from
FND-088), KX = 0.08, transverse projectors, and the straight-medium
normalization: c_eff measured from the acoustic slope at kk = 0.05 on
the straight cell -- the SAME self-normalization SHIN6 used, so S is
a pure ratio and engine units cancel.

## Measurement, locked

- M1: omega_max = the maximum eigenfrequency of the dynamical matrix
  over the Brillouin zone, computed on a uniform k-grid over
  [-pi, pi]^3 (lattice units, a_f = 1), grid 9^3, all bands (the
  ceiling is a property of the full operator, not only the
  photon-weighted bands: a label excitation need not be transverse-
  polarized).
- M2: S = omega_max / (c_eff / a_f) with c_eff from the straight-
  medium normalization above.
- M3 STABILITY: the grid is refined 9^3 -> 13^3; STABLE iff S changes
  by <= 2 percent. UNSTABLE is registrable and kept (no certificate).
- Cases: straight control (P = 1), wound f = 1/3, f = 1/4 (context),
  wound f = 1/5 (ADJUDICATING, per SHIN6's own designation). The
  certificate reads the adjudicating member; context members are
  reported in full per the full-table rule.

## Reference disclosure (guard)

Pre-lock scoping, disclosed so the landing cannot be dressed as
discovery: the textbook 1D nearest-neighbour chain has S = 2
(E_max = 2 hbar c/a, the figure FND-REL-004 already carries), and a
3D 18-neighbour stencil is expected to land S in the low single
digits -- ABOVE pi/2. The certificate is therefore EXPECTED to fire;
the session's value is converting that expectation into an exhibited
number on the validated instrument, with the wound geometry (which
could in principle soften the ceiling) actually checked rather than
assumed. If winding drops S below pi/2, that is exactly the finding
the conditionally-closed status exists to catch.

## RIDE-ALONG: the 1/N composition reading (verbatim, no computation)

Question (armed by FND-099): does FND-053's factorization
b_k(N) = (k-1) x 1/(N-1) survive the label moving to the sub-strand?
Method: read FND-053's two factors verbatim and record, for each,
whether it depends on WHICH object carries the label or only on the
label GROUP Z_N. Verdict grammar: SURVIVES (neither factor names the
carrier) / TAXED (a factor depends on the coarse-strand carrier;
FND-099 returns to adjudication) / AMBIGUOUS (a factor's carrier
dependence cannot be determined verbatim; escalate to the desk).

## Discipline

No re-binning of S's bar after numbers exist; no additional stencils
or weightings; adverse outcomes (C1-FAILED, UNSTABLE, TAXED)
pre-authorized and kept. This commission certifies or fails a
condition; it does not touch FND-099's ruling, GRANT-N2, or the
k-string bands.

## Deliverables

benchmarks/foundations/c1_fine_ceiling.py;
analysis/C1_fine_ceiling_results.md; claim via tools/add_claim.py;
annotations to FND-099, FND-098, FND-056, FND-060, FND-053;
CHANGELOG; HANDOFF; verify_corpus --quick; re-zip; present_files.
