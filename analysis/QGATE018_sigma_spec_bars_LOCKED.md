# QGATE-018 — Specifying the Sigma experiment: locked bars

## Commission
Sigma is the corpus's ONE remaining free scale (FND-017), with two registered
candidates 28% apart, and QGATE-007/010 is its named external arbiter. That
arbiter is still a NAME rather than a specification: no sensitivity requirement,
no discrimination calculation, no statement of what would separate the branches.
This session writes the specification.

## What must be computed, fixed before writing anything
S1 THE SIGNAL. Under the Sigma-large branch QGATE-009 records the mesh's own
   birefringence falling to Delta_n ~ 5e-34, ten orders below the QED/matter
   signal of 2.5e-23 at 2.5 T. The mesh nonlinearity weakens with stiffness, so
   take Delta_n_mesh ~ 1/Sigma and state the assumption.
S2 THE DISCRIMINATION. Compute the DIFFERENCE in Delta_n between the two
   registered candidates. That difference -- not the signal -- is what an
   experiment must resolve to decide Sigma.
S3 THE COMPARISON. PVLAS reached (12 +/- 17)e-23. VMB@CERN's design goal is
   ~1e-25, a thousandfold gain.

## Locked bars
B1 Report the mesh Delta_n for both candidates and their difference.
B2 Report the sensitivity needed to SEE the mesh at all, and to DISCRIMINATE
   the candidates, each as a factor over PVLAS and over VMB@CERN's goal.
B3 THE VERDICT, and it must be stated whichever way it falls: if the required
   sensitivity is unreachable, then QGATE-007 is NOT a decider for Sigma's
   VALUE and the corpus must stop describing it as one. Distinguish clearly
   between what the axis CAN test (a branch/threshold) and what it cannot (the
   value).
B4 IF IT CANNOT DECIDE THE VALUE: say what would, or report that nothing in the
   corpus or in reach does.
B5 HONESTY: the 1/Sigma scaling is an assumption; state how the verdict changes
   under other plausible scalings.
