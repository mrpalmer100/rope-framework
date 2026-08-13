# EM-RECON-018-R: re-solve under the corrected areal convention -- BARS, LOCKED BEFORE COMPUTING

Locked 2026-08-12, before any number in this commission was computed.

## Charter

FND-068 corrected the coverage convention (f_c is AREAL per FND-MATTER-038's
own construction; a plane is pierced only by the family normal to it) but did
NOT re-solve EM-RECON-018. This commission executes the owed re-solve. Nothing
else: no new f_c, no new contact form, no new standoff readings beyond the two
EM-RECON-018 enumerated.

## Bars

B1 (convention, fixed, not adjustable): the coverage relation is
    pi w^2 / (4 a^2) = f_c, so w/a = sqrt(4 f_c / pi). f_c = 0.309 registered
    (FND-MATTER-038), sensitivity window 0.073-0.348 reported as before.

B2 (readings, enumerated and carried, never selected): reading A (in-family
    touching, d0/sigma0 = 1.00, unchanged by the convention) and reading B
    (cross-family half-spacing, d0/sigma0 = 1/(2 w/a), which MOVES). Both
    thresholds computed with EM-RECON-017's registered C(d0/sigma0) machinery,
    reused verbatim (same integrand, same second difference). The band is the
    envelope of both. If reading B lands at d0/sigma0 < 1 the geometric
    interpretation question is REPORTED, not resolved, and the reading is
    still carried.

B3 (confrontation sealed): the FND-029 displayed estimates (EB = 4.716,
    T0 a = 0.16268, the four contact geometries) are confronted only AFTER
    the band is fixed, with the same not-adopted status EM-RECON-018 gave
    them. L1 = 1 with the factor-3 band noted.

B4 (adverse outcomes pre-authorized): if the corrected band excludes
    geometries that previously survived, or narrows survival to implausible
    geometries, that verdict is registered as-is. No rescue, no bar-shopping.

B5 (propagation duty): the claim must annotate EM-RECON-018 (band superseded),
    and must STATE the consequences for FND-064 (sign identity inherits the
    new band), FND-065 (units bridge 0.627 already applied there; gap number
    re-checked), FND-066 (W1 value updates), and FND-029 (width target moves).
    Annotations appended where numbers on a claim's face change.

B6 (house): no em dashes in file content; benchmark script under
    benchmarks/em/; verify_corpus --quick before re-zip.
