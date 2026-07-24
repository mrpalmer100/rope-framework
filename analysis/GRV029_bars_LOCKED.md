# GRV-029 pre-committed bars — LOCKED before any computation (v2.2.7 cycle)

Candidate theorem: THE PHYSICAL ONE-METRIC DERIVATION. Limbs:
(a) COUNTING: the gapless transverse mode's wave operator carries exactly the
    coefficient functions (mu, T_x, T_y, T_z); a static metric diag(-a^2, b_a^2)
    carries exactly (a, b_x, b_y, b_z). Claim: the map is an exact bijection on
    positive functions — the photon sector is one-metric BY COUNTING.
(b) EXCLUSIVITY: the only operator direction leaving the metric image is the gap
    coefficient (deviation = phi, screened per GRV-028); all other off-metric
    content is gapped-sector and couples to the gapless channel at O((omega/m)^2)
    (slaving / omega-hierarchy).
(c) IDENTIFICATION: the induced EH dynamics (GRV-025) and the light-propagation
    metric are built by the SAME dictionary from the SAME (T, mu) fields; the
    verifier reruns the tensor instrument with the conditioning-generated
    (physical-basis, fully nonlinear dictionary) coupling and must land the EH
    pattern.

BARS (PASS/FAIL fixed now; no post-hoc adjustment):
B1 (dictionary bijection, sympy): exact symbolic solve of
    mu = B/a, T_c = a*B/b_c^2 for (a, b_c); round-trip residual must simplify
    to 0 EXACTLY; Jacobian nonzero on the positive cone. PASS iff exact.
B2 (constraint identification, sympy): the one-metric condition on the 5th
    operator field is EXACTLY the gap-lock: on-site coefficient tracks
    sqrt(mu * T_x T_y T_z) (isotropic: T^{3/2} mu^{1/2}, GRV-026's lock; whose
    deviation phi is GRV-028's screened scalar). PASS iff symbolic identity.
B3 (omega-hierarchy, engine): two-band chain, gapless branch protected +
    gapped branch (gap m0). (i) protection: with coupling on, the gapless
    branch's lowest omega^2 / m0^2 < 1e-8; (ii) a static pure gap-sector
    distortion shifts gapless transmission/dispersion with exponent
    p = dln(effect)/dln(omega) in [1.8, 2.2] over >= one decade;
    (iii) suppression at omega = 0.1 m0 vs an equal-amplitude (T, mu)
    modulation >= 30x. FAIL if p outside [1.5, 2.5] or suppression < 10x.
B4 (instrument extension): closed-form PT extended with the alpha (mass/time)
    channel must validate vs exact diagonalization at M = 8 to < 0.5% on all
    tested directions including alpha-mixed (GRV-025's validation bar). FAIL
    blocks all downstream verdicts (audit before execution).
B5 (the verifier, m-odd q^2 on the extended instrument):
    (i) covariant-basis calibration reproduces the EH pattern (spatial ratios
        < 0.2, GRV-025's locked bar);
    (ii) FIFTH parameter-free covariance fingerprint: |K_{alpha z}/K_{alpha x}|
        < 0.05 (R^(1) = q^2(h_x + h_y) has no z);
    (iii) physical-basis (T_a, mu) channels through the FULL NONLINEAR
        dictionary match the covariant pull-back prediction: every nonzero
        channel within 0.2 relative; predicted-zero combinations < 0.1 of the
        dominant channel. M-stability drift < 0.15 between the two lattice
        sizes run.
    FAIL iff any nonzero-channel ratio > 0.5 or a predicted zero > 0.3 —
    registered as a negative per house rules; kill verdicts trigger an
    instrument audit BEFORE execution.

HONESTY PRE-REGISTRATION: the q^2-coefficient of the second-order zero-point
response is bilinear in the FIRST-ORDER operator fields (the family's
second-order fields drop in the q^2 differencing: uniform part is q-independent,
cos(2qz) part has zero diagonal). Therefore B5(iii) is an INSTRUMENT/DICTIONARY
consistency verification, not an independent dynamical test; the physical
content of the summit lives in B1+B2 (exact structure), B3 (slaving), and
GRV-028 (screening). This is stated before running so the claim cannot
oversell its verifier. If B5 nonetheless fails, the dictionary or the
derivation chain is wrong and the theorem does not stand.
