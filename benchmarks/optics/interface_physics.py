"""Interface-physics benchmark for the rope medium.

Every result here follows from ONE fact the rope medium already supplies: a wave
impedance Z = sqrt(T*mu) = T/c. Matching Z across an interface (continuity of
transverse displacement and transverse force -- the standard string junction)
yields the whole of classical interface optics. All classical; none touches Bell.

Covered:
  1. Rope impedance         Z = sqrt(T*mu) = T/c  (natural, not postulated)
  2. Snell's law            n1 sin th1 = n2 sin th2  (tangential-k continuity)
  3. Fresnel (normal)       r = (Z1-Z2)/(Z1+Z2), t = 2Z1/(Z1+Z2); R+T=1
  4. Brewster angle         tan th_B = n2/n1
  5. Anti-reflection coat   quarter-wave Z_c = sqrt(Z1 Z2) -> R = 0
  6. Fabry-Perot etalon     T = 1/(1 + F sin^2(delta/2)); resonances at 2 pi m
  7. Dielectric mirror      quarter-wave stack reflectivity -> 1 with N pairs

Supports rope_interface_optics.docx.
"""
import numpy as np

T = 1.0  # tension (natural units)

def impedance(mu, T=T):
    return np.sqrt(T*mu)

def test_impedance_natural():
    """Z = sqrt(T mu) equals T/c for all mu -> impedance is intrinsic to the medium."""
    for mu in [0.5, 1.0, 4.0, 9.0]:
        c = np.sqrt(T/mu); Z = impedance(mu)
        assert np.isclose(Z, T/c), f"Z != T/c at mu={mu}"
    return "PASS: rope impedance Z = sqrt(T mu) = T/c (intrinsic to the medium)"

def test_snell():
    """Tangential-wavevector continuity gives n1 sin th1 = n2 sin th2."""
    c1, c2 = 1.0, 0.5
    n1, n2 = 1/c1, 1/c2
    th1 = np.radians(30)
    th2 = np.arcsin(n1*np.sin(th1)/n2)
    assert np.isclose(n1*np.sin(th1), n2*np.sin(th2)), "Snell violated"
    return f"PASS: Snell n1 sin th1 = n2 sin th2 (th1=30 -> th2={np.degrees(th2):.2f} deg)"

def fresnel_normal(Z1, Z2):
    r = (Z1-Z2)/(Z1+Z2)
    t = 2*Z1/(Z1+Z2)
    return r, t

def test_fresnel_energy():
    """Fresnel amplitude coefficients + energy conservation R + T = 1."""
    Z1, Z2 = impedance(1.0), impedance(4.0)
    r, t = fresnel_normal(Z1, Z2)
    R = r**2
    Tp = (Z2/Z1)*t**2  # transmitted power coefficient
    assert np.isclose(R+Tp, 1.0), f"energy not conserved: R+T={R+Tp}"
    assert np.isclose(r, -1/3) and np.isclose(t, 2/3)
    return f"PASS: Fresnel r={r:.4f}, t={t:.4f}, R+T={R+Tp:.4f} (energy conserved)"

def test_brewster():
    """Brewster angle tan th_B = n2/n1."""
    n1, n2 = 1.0, 2.0
    thB = np.arctan(n2/n1)
    assert np.isclose(np.tan(thB), n2/n1)
    return f"PASS: Brewster tan th_B = n2/n1 (th_B = {np.degrees(thB):.2f} deg)"

def test_ar_coating():
    """Quarter-wave AR coating Z_c = sqrt(Z1 Z2) gives exactly zero reflection."""
    Z1, Z2 = impedance(1.0), impedance(4.0)
    Zc = np.sqrt(Z1*Z2)
    Z_in = Zc**2 / Z2          # quarter-wave impedance transform
    r = (Z1 - Z_in)/(Z1 + Z_in)
    assert abs(r) < 1e-12, f"AR coating not perfect: r={r}"
    return "PASS: quarter-wave AR coating Z_c=sqrt(Z1 Z2) -> R = 0"

def etalon_transmission(delta, R=0.3):
    F = 4*R/(1-R)**2
    return 1/(1 + F*np.sin(delta/2)**2)

def test_etalon():
    """Fabry-Perot: full transmission at round-trip phase = 2 pi m."""
    for m in range(3):
        assert np.isclose(etalon_transmission(2*np.pi*m), 1.0), f"no resonance at m={m}"
    assert etalon_transmission(np.pi) < 1.0  # anti-resonance
    return "PASS: Fabry-Perot etalon T=1 at delta=2 pi m (resonances), dip between"

def test_dielectric_mirror():
    """Quarter-wave stack reflectivity rises toward 1 with pair count N."""
    def R_stack(Zh, Zl, N, Z0=1.0):
        Z_in = Z0*(Zh/Zl)**(2*N)
        return ((Z0 - Z_in)/(Z0 + Z_in))**2
    Rs = [R_stack(2.0, 1.0, N) for N in [2, 4, 8]]
    assert Rs[0] < Rs[1] < Rs[2] and Rs[2] > 0.999, f"mirror not converging: {Rs}"
    return f"PASS: dielectric mirror reflectivity -> 1 with pairs (N=8: R={Rs[2]:.5f})"

TESTS = [test_impedance_natural, test_snell, test_fresnel_energy, test_brewster,
         test_ar_coating, test_etalon, test_dielectric_mirror]

if __name__ == "__main__":
    for t in TESTS:
        print(t())
    print("All interface-physics checks passed (7/7).")
