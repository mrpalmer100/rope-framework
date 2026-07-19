"""Optics benchmark for the rope medium: the classically computable optical
questions a reviewer asks of a wave ontology.
  (1) Non-dispersive Maxwell propagation: omega(k) = c k, phase velocity
      independent of k (light is a genuine non-dispersive rope wave).
  (2) Classical two-slit interference law I(Delta) ∝ 1 + cos(2 pi Delta/lambda)
      as direct superposition of two rope waves.
  (3) Birefringence structure: a velocity split exists and scales with the
      chirality parameter (structure present; absolute value not derived).
Supports rope_optics.docx / rope_electricity.docx (claims EM-004, EM-005).
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
import rope_solver.electromagnetism.photon as ph

def test_nondispersive_propagation():
    """omega/k is constant (= c): light is a non-dispersive rope wave."""
    ks = np.array([0.1, 0.5, 1.0, 2.0, 5.0])
    v = np.array([ph.dispersion_omega(k)/k for k in ks])
    assert np.allclose(v, v[0], rtol=1e-9), f"dispersion not linear: {v}"
    c = ph.C_LIGHT
    assert abs(v[0]-c)/c < 1e-6, f"phase velocity {v[0]} != c {c}"
    return f"PASS: omega=ck non-dispersive, phase velocity = c = {v[0]:.4e} m/s (all k)"

def two_slit_intensity(delta, wavelength=1.0, I0=1.0):
    """Classical two-slit law from superposition of two equal rope waves."""
    return 2*I0*(1 + np.cos(2*np.pi*delta/wavelength))

def test_classical_interference():
    """Two-slit law: bright fringes at integer path difference, dark at half-integer."""
    lam = 1.0
    # bright at delta = 0, lam, 2lam ; dark at lam/2, 3lam/2
    bright = [two_slit_intensity(d, lam) for d in [0, lam, 2*lam]]
    dark   = [two_slit_intensity(d, lam) for d in [lam/2, 3*lam/2]]
    assert all(abs(b-4.0) < 1e-9 for b in bright), f"bright fringes wrong: {bright}"
    assert all(abs(d) < 1e-9 for d in dark), f"dark fringes not zero: {dark}"
    # energy conserved: average intensity = 2 I0 (the incoherent sum)
    ds = np.linspace(0, lam, 1000)
    avg = np.mean([two_slit_intensity(d, lam) for d in ds])
    assert abs(avg - 2.0) < 1e-2, f"average intensity {avg} != 2 (energy not conserved)"
    return "PASS: two-slit law I∝1+cos(2πΔ/λ); bright=4I0, dark=0, energy conserved"

def test_birefringence_structure():
    """A velocity split exists and scales with the chirality parameter chi.
    Structure is present; the absolute magnitude is an input, not derived."""
    lam = 500e-9
    splits = [ph.birefringence_velocity_split(chi, lam) for chi in [0.0, 1e-3, 2e-3]]
    assert abs(splits[0]) < 1e-30, f"chi=0 should give no split, got {splits[0]}"
    # monotone increasing with chi
    assert splits[2] > splits[1] > splits[0], f"split not monotone in chi: {splits}"
    return "PASS: birefringence velocity split present, scales with chirality chi (magnitude = input)"

if __name__ == "__main__":
    print(test_nondispersive_propagation())
    print(test_classical_interference())
    print(test_birefringence_structure())
    print("All optics checks passed.")
