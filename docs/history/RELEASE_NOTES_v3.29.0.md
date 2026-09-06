# v3.29.0 (29 Aug 2026) -- THE WHY-WINDING ARC: THE E-LEDGER INTERPRETATION RE-PRICED TO THE BAND EDGE

**750 claims, 640/641 code-backed passing (1 documented waiver).**
Six new claims asking WHY the collapsing cell demands winding --
and answering with a re-pricing that moves the interpretive weight
of the arc's own headline result onto a committed out-of-sample
test.

## The one-paragraph version

The WHY-WINDING arc set out to explain FND-152/153's asymmetry --
the q = 4/3 branch turning its arclength into winding while
q = 5/3 stays flat -- and did its job by interrogating its own
evidence. The dispersion lattice put every measured branch near an
integer-harmonic line, so proximity cannot be the mechanism
(FND-154, RES-OPEN); the direct coupling statistic proved
structurally null (FND-155, F-INSTRUMENT); mode-resolved rotation
identified the collapse motion as a migration to the single high
harmonic +-(17,19) sitting one step below the phi-Nyquist edge
(FND-156, SEL-OPEN); and targeted resolution replication found
that content is NOT grid-stable -- it sits at whichever grid edge
is nearest and dissolves when the band opens (FND-157,
S3-F-INSTRUMENT). The re-pricing then made it exact: the
registered f_dir rise of FND-152 is carried ENTIRELY by
Nyquist-band content, with the resolved-band winding share
FALLING 0.106 -> 0.002 through the collapse and the flat
control's Nyquist band at 0.0000 throughout (FND-158, RP-FALLS,
Derived/Parseval). The confound-free 144x42 probe could not
adjudicate physical-vs-artifact -- the 4/3 deep member refused
full-bar gating while three sibling members gated cleanly on the
same grid (FND-159, NO VERDICT; grid-fragile on five
instruments). Amendment riders now sit on FND-152 and FND-153:
the rates and D bounds stand untouched; the mechanism sentence is
a statement about band-edge content whose character is OPEN. The
committed q = 5/4 FLAT prediction -- derived from the lattice,
not from any deep-end tangent -- is the arc's out-of-sample
adjudicator, queued with the resolution replication for hardware
where 144x54+ grids are feasible.

## Also in this release

- The evidence-mutation guard in tools/verify_corpus.py was found
  to be DEAD CODE (its restore block sat after the return
  statements) when a live instrument overwrote 81 analysis/
  evidence files mid-sweep and ELEC-011 failed with era-true
  numbers -- the exact incident class the guard was built
  against. All 81 files restored from the author's archive
  (hash-verified); the check moved ahead of the returns and
  annotated at its site. The offender's pass was cached this
  sweep; the repaired guard names offenders on the next cold run.
- Author grant records for FND-154..159 and the approved queue
  action shipped in analysis/.
- CITATION.cff realigned to the release version (it had lagged at
  3.27.6).
