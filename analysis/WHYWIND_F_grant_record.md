# GRANT RECORD -- WHYWIND-F (author's grant, 2026-08-29)
# Granted in the handoff-review session. REGISTRATION NOT YET TAKEN:
# this session holds only the session artifacts (no claims.yaml, no
# tools/add_claim.py). The working session executes the insert via
# the canonical tool in a verified process-quiet window. Nothing is
# registered until then.

## DECISION
WHYWIND-F GRANTED as drafted in
WHYWIND_draft_registration_addendum.md, with the inserting session
completing the one drafting gap noted there: the 5/3 deep control's
gate line ("[gate line pending at drafting]") is filled from the
close-out section of WHYWIND_probe42_results.md.

## CLAIM TEXT (for the canonical inserter)
144x42 confound-free probe: NO VERDICT -- the probe could not
render (P42 lines never armed). p42|4/3|prev gated at full bar in
11 rounds (RMS 6.8e-09; om2 2.22712, above Om1/2), but
p42|4/3|deep REFUSED under two bounded attempts (f32 limit cycle
at 2.3e-07; f64 endgame slid off constraints: A2 -> 0.0050447
off-pin, clos -> 6.8e-05). CONTRAST CREDENTIAL: the optional 5/3
control pair gated effortlessly on the SAME grid and solver
(prev: RMS 4.57e-09, clos 1.49e-10, om2 drift 0.03 pct; deep:
gate line per the results doc close-out). FINDING: the q = 4/3
deep-end state is grid-fragile on five independent instruments
(enumerated in WHYWIND_probe42_results.md); the FND-150..153
deep-end interpretation carries the hardened rider (WHYWIND-E);
artifact-vs-physical remains OPEN pending hardware where 144x54+
is feasible. Instrument ledger kept: phase-C disk-backed
factorization (OOM fix); per-dtype resumable Jacobian; bounded
f64 endgame; stale-jac disk cleanup.
Evidence: analysis/WHYWIND_probe42_bars_LOCKED.md,
analysis/WHYWIND_probe42_results.md,
benchmarks/foundations/whywind_probe42.py,
analysis/whywind_probe42_ckpt.pkl.

## STANDING
Author's grants so far: WHYWIND-A..F (separate records) and the
FND-152/153 hardened rider. The QUEUE ACTION is the last item on
the desk.
