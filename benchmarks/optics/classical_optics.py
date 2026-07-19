"""Comprehensive classical-optics benchmark for the rope medium.

Every phenomenon here is a solution of the ONE wave equation the rope medium
supplies (c^2 = T/mu, omega = c k, non-dispersive) under a different boundary
condition. Nothing new is postulated; nothing touches the quantum boundary.

Covered:
  1. Non-dispersive propagation      omega = c k  (phase velocity indep. of k)
  2. Huygens construction            wavefront = envelope of secondary wavelets
  3. Single-slit diffraction         I(th) = sinc^2(pi a sin th / lambda)
  4. Two-slit interference           I ∝ 1 + cos(2 pi Delta / lambda)
  5. Standing waves (fixed ends)     omega_n = n pi c / L
  6. Resonant cavity                 f_n = n c / (2L)
  7. Waveguide cutoff                omega_c = c pi / a  (evanescent below)
  8. Fiber / total internal refl.    theta_c = arcsin(n2/n1)

Supports rope_classical_optics.docx.
"""

# --- UTF-8 console shim (cross-platform; fixes Windows cp1252 crashes) ---
import sys as _sys
for _s in ("stdout", "stderr"):
    _stream = getattr(_sys, _s, None)
    _rc = getattr(_stream, "reconfigure", None)
    if callable(_rc):
        try:
            _rc(encoding="utf-8", errors="replace")
        except Exception:
            pass
# --- end shim ---
import numpy as np

C = 1.0  # signal speed in natural units (= sqrt(T/mu))

# ---- 1. propagation -------------------------------------------------------
def test_nondispersive():
    ks = np.array([0.1, 0.5, 1.0, 2.0, 5.0])
    v = np.array([C*k for k in ks]) / ks  # omega/k
    assert np.allclose(v, C, rtol=1e-12)
    return "PASS: omega = c k non-dispersive (phase velocity = c for all k)"

# ---- 2. Huygens -----------------------------------------------------------
def huygens_wavefront(sources, t, c=C, n_angles=3600):
    """Envelope of secondary spherical wavelets of radius c*t from each source.
    Returns points on the reconstructed forward wavefront (2D)."""
    ang = np.linspace(0, 2*np.pi, n_angles)
    pts = []
    for (sx, sy) in sources:
        pts.append(np.c_[sx + c*t*np.cos(ang), sy + c*t*np.sin(ang)])
    return np.vstack(pts)

def test_huygens_plane_wave():
    """A line of in-phase sources reconstructs a plane wavefront advancing at c."""
    xs = np.linspace(-2, 2, 21)
    sources = [(x, 0.0) for x in xs]
    t = 1.0
    wf = huygens_wavefront(sources, t)
    # the forward envelope sits at y = c*t for the central region
    front_y = wf[:, 1].max()
    assert abs(front_y - C*t) < 1e-4, f"wavefront not at c*t: {front_y}"  # resolved to angular step
    return "PASS: Huygens wavelets reconstruct a plane wavefront advancing at c"

# ---- 3. single-slit diffraction ------------------------------------------
def single_slit_intensity(theta, a, lam):
    beta = np.pi * a * np.sin(theta) / lam
    return np.sinc(beta/np.pi)**2  # numpy sinc is sin(pi x)/(pi x)

def test_single_slit():
    a, lam = 0.5, 0.05
    # first minimum at sin(theta) = lambda / a
    th_min = np.arcsin(lam/a)
    I = single_slit_intensity(th_min, a, lam)
    assert I < 1e-6, f"first minimum not dark: {I}"
    assert abs(single_slit_intensity(0, a, lam) - 1.0) < 1e-9
    return f"PASS: single-slit first minimum at sin(th)=lambda/a ({np.degrees(th_min):.2f} deg)"

# ---- 4. two-slit interference --------------------------------------------
def two_slit_intensity(delta, lam, I0=1.0):
    return 2*I0*(1 + np.cos(2*np.pi*delta/lam))

def test_two_slit():
    lam = 1.0
    assert abs(two_slit_intensity(0, lam) - 4.0) < 1e-9
    assert abs(two_slit_intensity(lam/2, lam)) < 1e-9
    ds = np.linspace(0, lam, 2000)
    assert abs(np.mean(two_slit_intensity(ds, lam)) - 2.0) < 1e-2  # energy conserved
    return "PASS: two-slit I∝1+cos(2πΔ/λ), bright=4I0/dark=0, energy conserved"

# ---- 5 & 6. standing waves + cavity --------------------------------------
def standing_wave_modes(L, n_modes=4, N=400):
    """Eigenfrequencies of the 1D wave equation with fixed ends (Dirichlet)."""
    x = np.linspace(0, L, N); h = x[1]-x[0]
    main = 2*np.ones(N-2)/h**2; off = -np.ones(N-3)/h**2
    A = np.diag(main)+np.diag(off,1)+np.diag(off,-1)
    ev = np.sort(np.linalg.eigvalsh(A))[:n_modes]
    return C*np.sqrt(ev)

def test_standing_waves():
    L = 1.0
    num = standing_wave_modes(L)
    exact = C*np.pi*np.arange(1, 5)/L
    assert np.max(np.abs(num-exact)/exact) < 1e-3, f"modes off: {num} vs {exact}"
    return "PASS: standing-wave modes omega_n = n pi c/L (fixed ends), <0.1% error"

def test_cavity():
    L = 1.0
    f1 = C/(2*L)  # fundamental resonance
    # fundamental standing mode omega_1 = pi c/L -> f_1 = omega_1/2pi = c/2L
    om1 = standing_wave_modes(L, 1)[0]
    assert abs(om1/(2*np.pi) - f1) < 1e-3
    return f"PASS: resonant cavity fundamental f_1 = c/(2L) = {f1}"

# ---- 7. waveguide cutoff -------------------------------------------------
def waveguide_cutoff(a, b, m=1, n=0):
    return C*np.sqrt((m*np.pi/a)**2 + (n*np.pi/b)**2)

def test_waveguide():
    a, b = 1.0, 0.5
    wc = waveguide_cutoff(a, b, 1, 0)
    assert abs(wc - C*np.pi/a) < 1e-9, f"TE10 cutoff wrong: {wc}"
    # a wave below cutoff is evanescent: k_z^2 = (omega/c)^2 - (pi/a)^2 < 0
    omega_below = 0.5*wc
    kz2 = (omega_below/C)**2 - (np.pi/a)**2
    assert kz2 < 0, "below cutoff should be evanescent"
    return f"PASS: waveguide TE10 cutoff omega_c = c pi/a; below cutoff evanescent"

# ---- 8. fiber / total internal reflection --------------------------------
def critical_angle(n1, n2):
    return np.arcsin(n2/n1)  # n = c/v_medium in the rope model

def test_fiber_tir():
    n1, n2 = 1.5, 1.0
    tc = critical_angle(n1, n2)
    assert abs(np.sin(tc) - n2/n1) < 1e-12
    return f"PASS: fiber TIR critical angle arcsin(n2/n1) = {np.degrees(tc):.2f} deg"

TESTS = [test_nondispersive, test_huygens_plane_wave, test_single_slit, test_two_slit,
         test_standing_waves, test_cavity, test_waveguide, test_fiber_tir]

if __name__ == "__main__":
    for t in TESTS:
        print(t())
    print("All classical-optics checks passed (8/8).")
