"""Commission MU — the Sigma provenance audit, mechanically verified.

Verifies:
  V1. The one-relation identity: both registered Sigma candidates are
      Sigma = 3*T_tube/(n*a^2) at the Lorentz bound, same T_tube, different n.
      T_tube agrees across the three registered chains to < 0.5%; the candidate
      ratio equals the inverse strand-count ratio to < 1%.
  V2. The forward re-derivation: the surviving strand counts (ELEC-052 n=156,
      ELEC-081 n=152) reproduce the lattice-anchored Sigma band 3.6-3.7e35 to
      < 1%, and n_t=111 reproduces 5.1e35 to < 1%.
  V3. The exclusion: n_t=111's forward tube radius (0.343 fm) sits +17-19%
      below the measured R_eq = 0.402-0.407 fm — the structural exclusion is
      one-signed (ELEC-052 B2), independent of the reconnection-chain kill.

Fails loudly if the registry numbers drift.
"""
import math

A = 1e-16                      # Lorentz-bound spacing, m (FND-MATTER-005)
CAND_SIGMA_ROUTE = 5.10e35     # QGATE-005 Arm 2 / QGATE-007 (J/m^3)
CAND_LATTICE = (3.606e35, 3.70e35)  # ELEC-052 (3.60e35), ELEC-081 (3.70e35)

CHAINS = {                     # (n, T0 J/m) -> T_tube = n*T0
    "sigma_route (QGATE-009)": (111, 1700 / 1.005),
    "lattice ELEC-052": (156, 1201),
    "lattice ELEC-081": (152, 1234),
}


def sigma(n, t_tube, a=A):
    return 3 * t_tube / (n * a ** 2)


def main():
    t_tubes = {k: n * t0 for k, (n, t0) in CHAINS.items()}
    ref = t_tubes["lattice ELEC-052"]
    for k, v in t_tubes.items():
        dev = abs(v / ref - 1)
        print(f"V1 T_tube[{k}] = {v:.4e} J/m  (dev {dev*100:.2f}%)")
        assert dev < 0.005, f"T_tube chain drift: {k}"

    ratio_cand = CAND_SIGMA_ROUTE / CAND_LATTICE[0]
    ratio_n = 156 / 111
    print(f"V1 candidate ratio {ratio_cand:.4f} vs n-ratio {ratio_n:.4f}")
    assert abs(ratio_cand / ratio_n - 1) < 0.01, "one-relation identity broken"

    t_tube = ref
    checks = [(111, CAND_SIGMA_ROUTE), (156, CAND_LATTICE[0]), (152, CAND_LATTICE[1])]
    for n, target in checks:
        got = sigma(n, t_tube)
        dev = abs(got / target - 1)
        print(f"V2 n={n}: Sigma = {got:.3e} vs registered {target:.3e} (dev {dev*100:.2f}%)")
        assert dev < 0.01, f"forward re-derivation drift at n={n}"

    # V3: R_tube = a*sqrt(n/(3*pi))  (NUCQ-003 relation)
    r111 = A * math.sqrt(111 / (3 * math.pi)) * 1e15  # fm
    for r_meas in (0.402, 0.407):
        excess = r_meas / r111 - 1
        print(f"V3 R(n=111) = {r111:.3f} fm vs measured {r_meas} fm (+{excess*100:.1f}%)")
        assert excess > 0.15, "structural exclusion no longer one-signed"

    print("\nALL CHECKS PASS — the two Sigma candidates are one relation at two n's;")
    print("the surviving strand count pins Sigma to the lattice band 3.61-3.70e35 J/m^3.")


if __name__ == "__main__":
    main()
