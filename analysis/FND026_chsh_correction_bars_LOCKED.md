# FND-026 — The two-particle boundary FELL, and I reported it twice as standing. Locked bars

## The error
FND-024 and FND-025 both stated that "CHSH still fails at S = 1.42 < 2, the
two-particle boundary kept", citing QB-009. That was QB-009's status and it was
SUPERSEDED. QB-027 -- the corpus's 200th registered claim -- reports
CHSH = 2.66 +/- 0.01 from engine-measured hardware.

## Why it happened
I searched the corpus (which found QB-023 and QB-010) but did NOT run
tools/forward_check.py on QB-009 before quoting its verdict. The tool exists for
exactly this, was built today, and I skipped it twice in consecutive claims.

## Locked bars
B1 State the correction and the magnitude of the error.
B2 Report what QB-027 actually did, including whether any analytic response law
   was used.
B3 THE SHORTFALL FROM TSIRELSON: is it a failure or a verification? Check the
   visibility arithmetic.
B4 THE CONTROL: what does severed bookkeeping give on identical hardware?
B5 WHAT THIS DOES TO FND-024 AND FND-025's conclusions, and what genuinely
   remains open.
