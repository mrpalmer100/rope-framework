# COMMISSION E: THE TARGET-SIDE AUDIT

## The question
FND-MATTER-060 closed the mechanism side of the lambda campaign and named,
explicitly and unverified, the one remaining place a directional factor
could live: the TARGET. The MATTER055 target (lambda = 1.156e-5 mean) is
built from dE_zp/L and the registered conditioning table. If that
construction converts through T0 or Sigma anywhere, then FND-MATTER-059's
genuine per-direction partition (the 3 in T0 = Sigma a^2/3, Derived) could
enter the target ONCE, legitimately, moving it by a factor of 3 in either
direction, and the 2.08x mechanism verdict would be re-adjudicated against
a moved target.

Task: trace the MATTER055 target construction line by line from the
benchmark source (matter055_ambient_zero_point.py) and the conditioning
table's provenance, and determine whether T0 or Sigma appears in the
chain, and if so, in which unit of account.

## The asymmetry, enforced
060 stated the seal requirement and the reason: the failure mode being
guarded against is A TARGET ADJUSTED TO MEET A CONSTRUCTION. Therefore the
session running this audit must have the MECHANISM SEALED OUT: it receives
the target construction, the 059 provenance result, and the 060 bookkeeping
method. It must NOT receive the mechanism's value (5.552e-6), the gap
(2.08x), or any statement of which direction a factor would need to move
the target to close it.

## Pre-committed bars
- B1 (asked first, target-free): does T0 or Sigma appear anywhere in the
  dE_zp/L chain or the conditioning-table entries feeding the target? A
  yes/no dependency fact, wrong wherever it lands.
- B2: if yes, apply the 060 unit-of-account method at each appearance: is
  the quantity a ratio in which the partition cancels (060's case), or a
  single conversion in which the 3 enters once (059's case)? The method is
  mechanical; judgment calls are flagged, not resolved.
- B3: if the audit moves the target, the new target is registered WITHOUT
  any comparison to the mechanism in the same session. Re-adjudication of
  the 2.08x verdict, if warranted, is a separate session receiving both
  sealed halves.
- B4: the conditioning table itself is not re-derived or re-fitted here.
  Its registered values are inputs; only their conversion path is audited.

## Stopping rule
One trace, one unit-of-account pass, one registration. If B1 answers no,
the commission closes in one session with a short negative claim: the
target is T0/Sigma-free, the 2.08x verdict is final for this mechanism
family, and the directional partition has no remaining entry point in the
lambda sector.

## Registrable outcomes (all acceptable)
1. No conversion through T0/Sigma: the lambda campaign's negative is
   final-final; a clean closure claim.
2. Conversion found, 3 enters once: target moves; separate re-adjudication
   session commissioned with both sides sealed.
3. Conversion found, ambiguous unit of account: the ambiguity registered as
   the finding, resolved (if at all) by a further target-blind settler in
   the 059 style.

## Depends on
FND-MATTER-055, FND-MATTER-059, FND-MATTER-060, FND-017, the matter055
benchmark source, the conditioning table's registered provenance.
