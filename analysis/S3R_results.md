# S3R RESULTS -- ** S3R-ARTIFACT-CONFIRMED ** (2026-08-29)
# Under analysis/S3R_charter_LOCKED.md (locked before any 144x54
# number). Driver benchmarks/foundations/s3r_replication.py; state
# analysis/s3r_ckpt.pkl. Ships in the NEXT release.

## THE FOUR SOLVES (all a2-pinned, stage-1 full bars, the
## SJ-CREDENTIALED instrument, s = 144 throughout)

  member       RMS       clos     A2 (pin)    Om2      wsNyq
  5/3 prev   7.83e-11  1.9e-11  0.0051481   4.32661  6.7e-09
  5/3 deep   7.95e-11  1.9e-11  0.0051922   4.32661* 7.5e-09
  4/3 prev   3.94e-11  1.2e-07  0.0050380   2.22672  5.1e-08
  4/3 deep   4.35e-09  3.1e-07  0.0050464   2.22702  4.8e-08
  (*deep Om2 from its gate line; both 5/3 members on the flat
   value.) No refusals; no confirmation debt anywhere. Peak RSS
  2.70-2.73 GB throughout -- the C4 daylight held in production.

## S3R-CRED: PASS (rendered before any 4/3 spectrum existed)
5/3 tangent top mode (|m|,|n|) = (2,1) ON THE BEAT LADDER, with
the k = 2, 3 harmonics in descending order ((4,2) 0.157x2,
(6,3) 0.076). The flat cell at 144x54 is as unremarkable as at
every prior grid.

## THE LOCKED LINES (rendered once, on the gated 4/3 pair)

  F17_54                       = 0.0000
    vs PHYSICAL line 0.4662 (0.5 x the FND-161 baseline): FAILS
    vs ARTIFACT line 0.05:                                FIRES
  DOM54 = (m,n) = (-/+1, +/-1), NOT the (17,19) band
  HIBAND54 over the FULL headroom [19, 27]         = 0.0000
    vs RELOCATED line 0.10:                          FAILS

## VERDICT: ** S3R-ARTIFACT-CONFIRMED **

The 4/3 deep-pair winding demand exists at NO resolvable band
beyond the 144x36 grid. The FND-161 loophole is CLOSED: the
content did not relocate to [22, 27] -- the full-headroom band
mass is zero to four decimals. The 144x54 tangent is the same
smooth low-mode diagonal ladder seen at 42 ((1,1) 0.191x2,
(2,2) 0.101x2, (3,3) 0.075x2, (4,4) 0.055x2), now resolved with
50 percent more phi headroom and unchanged. Grid-refinement
convergence of the tangent to smooth content is now shown at TWO
independent refinements (36 -> 42, FND-161; 36 -> 54, here), with
the s-reduction confound absent by construction and the flat-cell
control credentialed in the same run.

## LOCKED CONSEQUENCES (now standing, per the charter)
1. The artifact call is FINAL for the FND-150..153 interpretation
   re-pricing: the proposal RIPENS TO A CHARTERED COMMISSION over
   the interpretation (rates and D bounds untouched).
2. The q = 5/4 column proceeds as next queue item with the
   artifact-final prior. The committed q = 5/4 FLAT dispersion
   prediction stands as committed, untouched by this charter.

## REGISTERED (author's grant WITH SCOPE RIDER 2026-08-30; see
## analysis/S3R_grant_record.md)
  FND-162 (REGISTERED, scope rider in note): S3R-ARTIFACT-CONFIRMED -- full stage-3
      replication at 144x54 (s = 144 throughout, four a2-pinned
      full-bar members, S3R-CRED beat-ladder pass): F17_54 =
      0.0000 and HIBAND54[19..27] = 0.0000 on the 4/3 deep-pair
      tangent. The n = 17 winding demand exists at no resolvable
      band beyond 144x36; with FND-161 this establishes
      two-refinement convergence to smooth tangent content. The
      artifact call is final for the FND-150..153 interpretation
      re-pricing. Evidence: analysis/S3R_charter_LOCKED.md, this
      document, analysis/s3r_ckpt.pkl,
      benchmarks/foundations/s3r_replication.py.

## INSTRUMENT LEDGER ADDITION
  FAULT-10 (LATENT, caught before firing, this session): the
  pattern cache key lacked the CELL (n2); the 4/3 members would
  have silently reused the 5/3-measured 144x54:a2 pattern. Key now
  grid + pin_mode + cell; annotated at make_instrument. No number
  was contaminated.
  [SJ-OPT 2026-08-29b] (this march): factor memo streams as .npy
  (pickle.dumps of the whole factor was OOM-reaped at 144x54);
  supersedes the SJ_MEMO=1 sizing note in
  SPARSEJ_credential_results.md for 54-class grids.

## STANDING
Registry advanced to FND-162 (753 claims) with the author's grant
and scope rider on record. Failures kept. Nothing beyond the locked lines was
computed on the 4/3 spectrum.
