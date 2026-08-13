# COMMISSION PE -- THE BRANCHING RATIO p, DERIVED BLIND: BARS, LOCKED BEFORE COMPUTING

Locked 2026-08-12, before any number in this commission was computed.

## Charter

FND-071 reduced the reconnection acquisition to one dimensionless branching
ratio p per crossing encounter, with a sealed target band p in
[8.3e-04, 8.6e-03] armed from NUC-030's v0. This commission derives p from
registered structure, blind: the derivation and every input are fixed by
these bars before the resulting number is compared with the band.

## The realization (fixed at lock)

Reconnection = INTER-STRAND TRANSFER at a single crossing. Registered
basis: EM-RECON-025's two-strand stiffness matrix couples RELATIVE
displacement at the crossing with strength s/a; the symmetric (acoustic)
combination passes the crossing free (gapless by symmetry protection, the
claim's own derived structure), the antisymmetric (optical) combination
scatters off the crossing as a point pinning of dimensionless contrast g
(Commission G's registered transfer relation, cos(qa) = cos(ka) +
(g/2ka) sin(ka), defines g). This realization is AMPLITUDE-FREE, which
matters: SCALE-001 certifies no non-circular amplitude is registered, so
any amplitude-dependent p would be unposeable. Scattering probabilities
are ratios of quadratic functionals and the unregistered amplitude
cancels identically.

## Bars

B1 (the exchange definition): p = probability that a disturbance incident
    on strand 1 exits on strand 2, in EITHER direction (transmitted-onto-2
    plus reflected-onto-2). Both terms count: connectivity has moved to
    the partner. Locked before computing; not adjusted after.

B2 (the evaluation scale): ka = 1, from FND-071's own attempt kinematics
    (nu = c/a, hence omega = c/a and k = 1/a: the encounter's own scale,
    not chosen for the answer). A sweep over ka in [0.3, 3] is REPORTED
    for sensitivity and may not be used to select a value.

B3 (the contrast inventory, registered only): g's floor is Commission G's
    G3 registration, g >= O(1e-2). The wider material-ratio band is
    FND-029's E_x/(T0 a) in [0.019, 87]. Both carried; no value of g is
    selected. If the derivation returns p(g), the sealed p-band is
    INVERTED to a demanded g-window and confronted with this inventory.

B4 (verdict grammar, locked):
      CLOSED-HIT     the registered inventory PINS g and p lands in band;
      CONSISTENT-UNDERDETERMINED  the demanded g-window lies strictly
                     inside the registered inventory (the chain is
                     consistent; the acquisition moves down one rung,
                     from p to g);
      MISS           the demanded g-window and the registered inventory
                     are disjoint: the NUC-030 falsifier FIRES and the
                     adoption returns to adjudication.
    No fourth verdict may be invented after the numbers are seen.

B5 (derivation checks): the one-crossing scattering must be solved
    symbolically (unitarity |t|^2 + |r|^2 = 1 in the antisymmetric
    channel, verified exactly) and numerically; the symmetric channel's
    free passage must be exhibited, not assumed, from the registered
    matrix structure.

B6 (athermality and causality inherited): no thermal factor may appear
    (FND-071 Q2a); the scattering is local to one crossing (ELEC-043
    honoured by construction).

B7 (adverse outcomes pre-authorized): MISS is an acceptable outcome and
    fires the falsifier exactly as NUC-030 demands. No rescue, no
    bar-shopping, no re-scoping of the band.

B8 (house): no em dashes in file content; benchmark under
    benchmarks/foundations/; verify before re-zip.
