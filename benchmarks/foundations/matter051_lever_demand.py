"""FND-MATTER-051: the lever session, part 1 -- the demand, the
renormalization pose, and the shared sub-quantum building block.
Bars locked BEFORE computing (analysis/MATTER051_lever_demand_results.md):
(1) NO NEW CALIBRATION. The ~25 percent lever size is a REGISTERED
measurement (FND-MATTER-009); converting it into lambda's required value is
unit conversion, not fitting. The campaign's spend count stays at one.
(2) INSTRUMENT for the raw zero-point term, stated: 1D transverse
mode-density (continuum) form on the knot's ropelength L*a, omega = c k,
E_raw = (La/2 pi) integral hbar c k dk to k_max = 1/a, i.e. E_raw =
hbar c La/(4 pi a^2). The discrete count is REPORTED alongside it: a ring
of ropelength pi a supports of order ONE transverse mode below the mesh
cutoff, so discrete counting is ill-conditioned and the continuum form is
the committed instrument. The Casimir caveat is carried on the claim's
face: the PHYSICAL Delta E_zp is a with/without difference, so the raw
term is an UPPER SCALE, not the physical value -- which is exactly why
lambda exists.
(3) NUMEROLOGY GUARD: any numeric agreement found must be DECOMPOSED into
shared vs distinct registered factors before registration, registers at
WHISPER grade at most, and registers only if the shared factor is a
registered structure (not a digit coincidence).
(4) FND-MATTER-050 REMAINS OPEN. This session poses and prices; it does
not close. The closure criterion it must leave behind is a derivation
target stated in one sentence.
"""
import numpy as np

HBAR, C = 1.054571817e-34, 2.99792458e8
ALPHA, ME = 1 / 137.036, 9.1093837015e-31
A_M, T0_M = 6.0056e-17, 434.0
L_RING = 3.141
LEVER_MEASURED = 0.25            # FND-MATTER-009's registered size
BETA, RINGF, H_CORE = 35.4, 0.23, 1.87e-19


def main():
    La = L_RING * A_M
    tension_term = T0_M * La                      # = m_e c^2 by construction
    N_discrete = La / (np.pi * A_M)               # ~ 1.0: the ring is pi cells
    E_raw = HBAR * C * La / (4 * np.pi * A_M**2)  # committed continuum form
    E_single = 0.5 * HBAR * C * np.pi / La        # the one discrete mode
    ratio_raw = E_raw / tension_term
    print(f"THE RAW TERM (committed continuum instrument):")
    print(f"  discrete picture: N = {N_discrete:.2f} -- the ring supports of")
    print(f"  order ONE transverse mode below the mesh cutoff (a finding in")
    print(f"  itself: the electron knot is a cell-scale object, so its 'mode")
    print(f"  tower' is a single rung); single-mode energy = "
          f"{E_single/tension_term:.0f}x rest energy.")
    print(f"  continuum form: E_zp_raw / (T0 L a) = {ratio_raw:.0f} -- the")
    print(f"  corpus's own miniature hierarchy problem, quantified: the naive")
    print(f"  one-loop zero-point term at the knot scale is ~{ratio_raw:.0f}x")
    print("  the electron rest energy. The Casimir caveat is carried: this is")
    print("  the UPPER SCALE the renormalization must suppress, which is why")
    print("  lambda exists at all.")

    lam = LEVER_MEASURED * tension_term / E_raw
    print(f"THE DEMAND (registered 25 percent converted, no new calibration):")
    print(f"  lambda = 0.25 / {ratio_raw:.0f} = {lam:.3e}")

    # Structural decomposition using the registered hbar relation
    # (hbar c = T0 l_q^2 / (4 pi alpha)):
    #   lambda = 0.25 * T0 La / E_raw = 0.25 * 4 pi a^2 T0/(hbar c)
    #          = 0.25 * (4 pi)^2 alpha * (a/l_q)^2
    lq2 = 4 * np.pi * ALPHA * HBAR * C / T0_M
    lam_clean = LEVER_MEASURED * 4 * np.pi * A_M**2 * T0_M / (HBAR * C)
    lam_reg = LEVER_MEASURED * (4 * np.pi) * (4 * np.pi * ALPHA) * A_M**2 / lq2
    print(f"  structural form: lambda = 0.25 * 4 pi a^2 T0/(hbar c) "
          f"= {lam_clean:.3e}")
    print(f"  with the REGISTERED hbar relation: lambda = "
          f"0.25 (4 pi)^2 alpha (a/l_q)^2 = {lam_reg:.3e}")
    assert abs(lam_reg / lam - 1) < 0.01 and abs(lam_clean / lam - 1) < 0.01

    # The shared building block with n_q
    nq = {chi: 4 * np.pi * ALPHA * (3 * BETA / (RINGF * chi))
          * (A_M * H_CORE / lq2) for chi in (1.0, 3.0)}
    ratio_band = (lam / nq[1.0], lam / nq[3.0])
    print("THE DECOMPOSITION (numerology guard applied):")
    print("  lambda   = [4 pi alpha a/l_q^2] x [pi a]  (times 0.25 x 4)")
    print("  n_q      = [4 pi alpha a/l_q^2] x [(3b/0.23chi) h]")
    print("  SHARED CORE: 4 pi alpha a / l_q^2 -- a REGISTERED structure (the")
    print("  quantum-area ratio), not a digit coincidence. DISTINCT parts:")
    print("  a cell length (pi a) vs the snap-height stack -- both cell-scale.")
    print(f"  lambda/n_q = {ratio_band[0]:.2f} (chi=1) .. {ratio_band[1]:.2f} (chi=3)")
    assert 1 < ratio_band[0] < 10 and ratio_band[1] < 10
    print("  WHISPER REGISTERED (grade capped by bar): the mass sector's")
    print("  zero-point suppression and the gravity sector's snap fraction")
    print("  are the SAME dimensionless building block -- (cell area)/(quantum")
    print("  area) -- times O(few) cell geometry. One medium, one sub-quantum")
    print("  fraction, two sectors reading it.")

    print("THE CLOSURE CRITERION LEFT FOR FND-MATTER-050 (one sentence):")
    print("  derive that the EXPRESSED fraction of the raw determinant equals")
    print("  the cell-to-quantum area ratio (equivalently: why the medium")
    print("  expresses one quantum area's worth of zero-point weight per")
    print("  cell), with the 0.25's O(1) geometry computed, not measured.")
    print("  FND-MATTER-050 REMAINS OPEN; spend count remains ONE.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
