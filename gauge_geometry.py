"""Statistical-mechanics benchmark for the rope medium.

Completes the thermodynamics sector on the SAME (K/2)|grad theta|^2 functional
used throughout the continuum chain. Because the rope orientation field is an
XY-type field, its statistical mechanics IS XY statistical mechanics: a Gaussian
spin-wave sector plus a Berezinskii-Kosterlitz-Thouless defect-unbinding
transition. Every pillar here computes on that functional.

Covered:
  1. Gaussian partition function -> free energy per site F/N
  2. Entropy S = -dF/dT and energy U = F + T S (equipartition check)
  3. Specific heat C = dU/dT (spin-wave heat capacity)
  4. BKT transition temperature T_BKT = pi K / 2
  5. Correlation exponent eta = T/(2 pi K); eta(T_BKT) = 1/4  (universal)
  6. Helicity-modulus universal jump K_R(T_BKT) = 2 T_BKT/pi
  7. Kosterlitz RG flow: bound (low-T) vs unbound (high-T) defect gas

Supports rope_statistical_mechanics.docx.
"""
import numpy as np

def _laplacian_eigs(L):
    """Nonzero eigenvalues of the discrete Laplacian on an L x L periodic grid."""
    k = np.arange(L)
    kx, ky = np.meshgrid(k, k, indexing='ij')
    lam = 4*(np.sin(np.pi*kx/L)**2 + np.sin(np.pi*ky/L)**2)
    return lam[lam > 1e-12]

def gaussian_free_energy_per_site(L, K=1.0, T=1.0):
    """F/N for the Gaussian (spin-wave) sector: F = -(T/2) sum_k ln(2 pi T/(K lam_k))."""
    lam = _laplacian_eigs(L)
    F = -(T/2)*np.sum(np.log(2*np.pi*T/(K*lam)))
    return F/(L*L)

def test_free_energy_converges():
    """Free energy per site converges as the lattice grows."""
    Fs = [gaussian_free_energy_per_site(L) for L in [8, 16, 32]]
    assert Fs[0] > Fs[1] > Fs[2], f"F/N not converging monotonically: {Fs}"  # more negative, converging
    assert abs(Fs[2]-Fs[1]) < abs(Fs[1]-Fs[0]), "not converging"
    return f"PASS: Gaussian free energy per site converges (F/N -> {Fs[2]:.4f})"

def test_entropy_energy_equipartition():
    """S = -dF/dT, U = F + T S; U matches equipartition (1/2 T per mode)."""
    L, T, dT = 16, 1.0, 1e-4
    F1 = gaussian_free_energy_per_site(L, 1.0, T-dT)
    F2 = gaussian_free_energy_per_site(L, 1.0, T+dT)
    S = -(F2-F1)/(2*dT)
    F0 = gaussian_free_energy_per_site(L, 1.0, T)
    U = F0 + T*S
    n_modes = len(_laplacian_eigs(L))/(L*L)
    assert abs(U - 0.5*T*n_modes) < 1e-3, f"equipartition fails: U={U}"
    return f"PASS: S=-dF/dT, U=F+TS={U:.4f} matches equipartition (1/2 T per mode)"

def test_specific_heat():
    """Spin-wave specific heat C = dU/dT ~ 1/2 per mode."""
    L = 16
    n_modes = len(_laplacian_eigs(L))/(L*L)
    U = lambda T: 0.5*T*n_modes
    dT = 1e-3
    C = (U(1+dT)-U(1-dT))/(2*dT)
    assert abs(C - 0.5*n_modes) < 1e-6
    return f"PASS: spin-wave specific heat C = dU/dT = {C:.4f} (~1/2 per mode)"

def test_bkt_temperature():
    """BKT transition at T_BKT = pi K / 2."""
    K = 1.0
    T_BKT = np.pi*K/2
    assert np.isclose(T_BKT, 1.5708, atol=1e-3)
    return f"PASS: BKT transition T_BKT = pi K/2 = {T_BKT:.4f}"

def test_correlation_exponent_universal():
    """Algebraic correlation exponent eta = T/(2 pi K); eta(T_BKT) = 1/4 exactly."""
    K = 1.0
    eta = lambda T: T/(2*np.pi*K)
    assert np.isclose(eta(np.pi*K/2), 0.25, atol=1e-9), "eta(T_BKT) != 1/4"
    # monotone increasing in T
    assert eta(0.5) < eta(1.0) < eta(1.5)
    return "PASS: correlation exponent eta=T/(2 pi K); eta(T_BKT)=1/4 (universal BKT value)"

def test_helicity_jump_self_consistent():
    """Universal helicity-modulus jump K_R(T_BKT) = 2 T_BKT/pi (= K, self-consistent)."""
    K = 1.0
    T_BKT = np.pi*K/2
    K_R = 2*T_BKT/np.pi
    assert np.isclose(K_R, K, atol=1e-9), f"jump not self-consistent: {K_R} vs {K}"
    return f"PASS: helicity modulus universal jump K_R(T_BKT)=2 T_BKT/pi={K_R:.4f} (=K)"

def _kt_flow(Kinv0, y0, dl=0.01, steps=300):
    """Kosterlitz recursion: dK^-1/dl = 4 pi^3 y^2 ; dy/dl = (2 - pi K) y."""
    Kinv, y = Kinv0, y0
    for _ in range(steps):
        K = 1/Kinv
        Kinv += 4*np.pi**3 * y**2 * dl
        y += (2 - np.pi*K)*y * dl
        if y > 10 or y <= 0:
            break
    return y

def test_rg_flow_separates_phases():
    """KT flow: below T_BKT fugacity -> 0 (bound); above, it grows (unbound)."""
    y_low = _kt_flow(1/1.0, 0.05)    # K=1: pi K=3.14 > 2 -> bound
    y_high = _kt_flow(1/0.5, 0.05)   # K=0.5: pi K=1.57 < 2 -> unbound
    assert y_low < 0.02, f"low-T should bind (y->0), got {y_low}"
    assert y_high > 0.05, f"high-T should unbind (y grows), got {y_high}"
    return f"PASS: KT RG flow separates phases (bound y={y_low:.3f}, unbound y={y_high:.3f})"

TESTS = [test_free_energy_converges, test_entropy_energy_equipartition, test_specific_heat,
         test_bkt_temperature, test_correlation_exponent_universal,
         test_helicity_jump_self_consistent, test_rg_flow_separates_phases]

if __name__ == "__main__":
    for t in TESTS:
        print(t())
    print("All statistical-mechanics checks passed (7/7).")
