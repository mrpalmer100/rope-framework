# ELEC-065 — The dependency sweep: what inherited a changed premise? Locked bars

## Commission
Two errors of the SAME TYPE surfaced today: HBAR-010 inherited HBAR-006's
retired relation and was classified as surviving (caught by ELEC-064), and
ELEC-062's census scoped itself to one file and missed a paper (caught by
ELEC-063). Both are "something upstream changed and nothing downstream
noticed". This sweeps for the rest mechanically.

## The universe, fixed before computing
Every claim whose standing changed today: closed, retired, falsified,
superseded, demoted, unanchored, corrected, or narrowed. Identified by
annotation tag, not by memory.

## Locked bars
B1 Build the transitive DESCENDANT set of every changed claim -- every claim
   that depends on one, directly or at any depth.
B2 FLAG the descendants that do NOT already carry an annotation referencing the
   change. These are the unnoticed inheritances, and they are the sweep's
   product.
B3 TRIAGE each flagged claim by whether the change is load-bearing for it:
   INHERITS (the changed premise is used), SURVIVES (independent of what
   changed), or UNCLEAR (needs reading). No claim may be marked SURVIVES
   without a stated reason.
B4 Report the count and the worst cases. If the sweep finds nothing, say so --
   a null sweep is a real result and means today's corrections were complete.
B5 Any claim found INHERITING must be annotated in this session, not deferred.
