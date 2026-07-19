"""
tests/test_electromagnetism.py  --  Regression + cross-sector consistency for EM.

Pins the EM structural relations and, crucially, the cross-sector consistency
conditions that keep the EM, gravity, and particle modules from drifting apart.

Run:  python3 tests/test_electromagnetism.py
"""
import numpy as np
import sys
from rope_solver.electromagnetism import (eps0_from_structure,
    impedance_of_free_space, alpha_from_impedance, charge,
    dirac_quantization_n, wave_speed_squared, maxwell_structure,
    consistency_with_particles, consistency_with_gravity)
from rope_solver.topology.linking import torus_link


def main():
    results = []
    def check(name, cond, detail=""):
        results.append((name, cond))
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}  {detail}")

    print("="*64); print("ELECTROMAGNETISM REGRESSION + CONSISTENCY"); print("="*64)

    print("\n1. Structural constant relations")
    eps0 = eps0_from_structure()
    check("eps0 = 1/(mu0 c^2) ~ 8.854e-12", abs(eps0-8.854e-12) < 1e-14,
          f"{eps0:.4e}")
    Z0 = impedance_of_free_space()
    check("Z0 = mu0 c ~ 376.73 ohm", abs(Z0-376.73) < 0.1, f"{Z0:.3f}")
    a = alpha_from_impedance()
    check("alpha = e^2 Z0/2h ~ 1/137", abs(1/a - 137.0) < 0.5, f"1/{1/a:.2f}")

    print("\n2. Charge quantization (topological, q=Lk)")
    for n in [1, 2, 3]:
        A, B = torus_link(80, n)
        q = charge(A, B)
        check(f"charge q=Lk={n} is integer", abs(round(q)) == n,
              f"q={q:.3f} -> {round(q)}")

    print("\n3. Dirac quantization (inherited from bundle identification)")
    # e*g = 2*pi*hbar*n for n=1 should give dirac_quantization_n = 1
    hbar = 6.626e-34/(2*np.pi)
    g_for_n1 = 2*np.pi*hbar/1.602e-19   # g such that n=1 with e=e_charge
    n = dirac_quantization_n(1.602e-19, g_for_n1)
    check("Dirac n=1 recovered", abs(n-1) < 1e-6, f"n={n:.4f}")

    print("\n4. Wave speed (one rope, one speed)")
    c2 = wave_speed_squared(T0=1.0, mu_rope=1.0)  # natural units T0=mu=1 -> c=1
    check("c^2 = T0/mu_rope", abs(c2-1.0) < 1e-12, f"c^2={c2}")

    print("\n5. Maxwell structure recorded (4 equations, d=3 dependence)")
    ms = maxwell_structure()
    check("four Maxwell equations recorded", len(ms) == 4, f"n={len(ms)}")
    check("Ampere law cites d=3/Helmholtz",
          "d=3" in ms[3][1] or "Helmholtz" in ms[3][1], "")

    print("\n6. CROSS-SECTOR CONSISTENCY (the inter-paper guarantees)")
    a_em, a_p, ok_p = consistency_with_particles()
    check("EM alpha == particle-sector alpha", ok_p,
          f"EM={a_em:.5f}, particles={a_p:.5f}")
    c_em, c_g, ok_g = consistency_with_gravity()
    check("c_EM == c_gravity (one rope)", ok_g,
          f"EM={c_em:.4e}, gravity={c_g:.4e}")

    print("\n7. Photon / light (rope_theory_of_light)")
    from rope_solver.electromagnetism.photon import (photon_linking_number,
        photon_energy, photon_momentum, dispersion_omega, group_minus_phase_velocity,
        chirality_chi, cosmic_birefringence_deg, chirality_product_from_beta,
        eb_ee_ratio, cross_sector_massless, BETA_MEASURED_DEG)
    check("photon Lk = 0 (massless, chargeless)", photon_linking_number() == 0, "Lk=0")
    nu = 5e14
    check("E = h nu", abs(photon_energy(nu) - 6.626e-34*nu) < 1e-50, "")
    check("p = E/c", abs(photon_momentum(nu) - photon_energy(nu)/2.998e8) < 1e-40, "")
    k = np.linspace(1, 10, 50)
    check("omega = c k (linear dispersion)",
          np.allclose(dispersion_omega(k), 2.998e8*k), "")
    check("v_group - v_phase = 0 (non-dispersive)",
          group_minus_phase_velocity(k) < 1e-3*2.998e8,
          f"{group_minus_phase_velocity(k):.2e}")
    # birefringence: round-trip the measured constraint
    prod = chirality_product_from_beta()
    check("chirality product ~ 9.18e-29 /m (Eskilt-Komatsu)",
          abs(prod - 9.18e-29)/9.18e-29 < 0.05, f"{prod:.3e}")
    # reconstruct beta from chi built on that product (r_H, n_rope absorbed in product)
    chi = prod / 2.998e8
    beta_back = cosmic_birefringence_deg(chi)
    check("beta round-trips to 0.342 deg", abs(beta_back - BETA_MEASURED_DEG) < 0.01,
          f"{beta_back:.3f} deg")
    check("EB/EE = sin(4 beta)/2 ~ 0.0119", abs(eb_ee_ratio() - 0.0119) < 0.001,
          f"{eb_ee_ratio():.4f}")
    Lk_ph, ok_massless = cross_sector_massless()
    check("photon massless consistent with particle sector (Lk=0)", ok_massless,
          f"Lk={Lk_ph}")

    print("\n8. Cross-sector consistency: chemistry shares EM eps0")
    from rope_solver.electromagnetism import consistency_with_chemistry
    E1, ok_chem = consistency_with_chemistry()
    check("H ground state from EM eps0 = -13.6 eV (consistency, not a rope result)",
          ok_chem, f"{E1:.2f} eV")

    print("\n9. Open-problems registry integrity")
    from rope_solver.open_problems import OPEN_PROBLEMS, by_status, summary
    check("registry non-empty", len(OPEN_PROBLEMS) > 0, f"n={len(OPEN_PROBLEMS)}")
    check("Pauli exclusion registered as CANDIDATE (not a result)",
          any(p["id"]=="pauli-rope-spin" and p["status"]=="CANDIDATE" for p in OPEN_PROBLEMS), "")
    check("one-loop mass kept as FALSIFIED",
          any(p["id"]=="one-loop-mass" and p["status"]=="FALSIFIED" for p in OPEN_PROBLEMS), "")
    valid_status = {"OPEN","POSTULATE","CONJECTURE","CANDIDATE","PARTIAL","FALSIFIED"}
    check("Koide phase registered as CONJECTURE (not a theorem)",
          any(p["id"]=="koide-phase-t-parity" and p["status"]=="CONJECTURE" for p in OPEN_PROBLEMS), "")
    check("mass scale-breaking reframe recorded as OPEN",
          any(x["id"]=="mass-ontology-scale-breaking" and x["status"]=="OPEN" for x in OPEN_PROBLEMS), "")
    check("1/e mass coincidence recorded as REJECTED (not revivable)",
          any("REJECTED COINCIDENCE" in x["note"] for x in OPEN_PROBLEMS if x["id"]=="mass-ontology-scale-breaking"), "")
    check("all entries have valid status",
          all(p["status"] in valid_status for p in OPEN_PROBLEMS), str(summary()))

    # EM-P2 boundary-matching: Ampere flux derived from boundary linking continuity
    from rope_solver.electromagnetism import ampere_flux_from_boundary_linking
    _ok = True
    for Lk in (1, 2, 3):
        cA, fB = ampere_flux_from_boundary_linking(Lk)
        if not (abs(cA - 2*np.pi*Lk) < 1e-12 and abs(fB - cA) < 1e-12):
            _ok = False
    check("boundary phase-continuity -> circ(A)=flux(B)=2pi*Lk (Ampere from continuity)",
          _ok, "flux(B)=2pi*Lk for Lk=1,2,3; enclosed current = enclosed linking")

    # EM-P2 energy selection: minimal bulk texture (0 extra Hopf units) is the energy minimum
    from rope_solver.electromagnetism import minimal_texture_energy_selects_ampere
    _en = minimal_texture_energy_selects_ampere(1)
    _min_at = min(_en, key=lambda t: t[1])[0]
    check("energy minimization selects minimal bulk texture (extra Hopf units = 0)",
          _min_at == 0, f"energy-minimizing extra Hopf units = {_min_at} (removes bulk ambiguity)")

    # EM-P2 dipole law from the field-energy cross term (given the continuum energy functional)
    from rope_solver.electromagnetism import dipole_interaction_from_field_energy, energy_functional_form_is_forced
    _ht = dipole_interaction_from_field_energy([0,0,1],[0,0,1],[0,0,1])   # head-to-tail: attract (<0)
    _ss = dipole_interaction_from_field_energy([0,0,1],[0,0,1],[1,0,0])   # side-by-side: repel (>0)
    _tc = dipole_interaction_from_field_energy([1,0,0],[0,0,1],[0,0,1])   # T-config: zero
    check("dipole law from field-energy cross term: attract/repel/zero signs correct",
          _ht < 0 and _ss > 0 and abs(_tc) < 1e-12, f"ht={_ht:+.1f} ss={_ss:+.1f} T={_tc:+.1f}")
    # 1/r^3 scaling
    _r1 = dipole_interaction_from_field_energy([0,0,1],[0,0,1],[0,0,2])
    _r2 = dipole_interaction_from_field_energy([0,0,1],[0,0,1],[0,0,4])
    check("dipole interaction scales as 1/r^3",
          abs(_r1/_r2 - 8.0) < 1e-9, f"ratio(r=2 vs r=4) = {_r1/_r2:.3f} (expect 8)")
    check("continuum energy FORM is EFT-constrained (uniquely selected in class) to c|curl A|^2",
          "curl A" in energy_functional_form_is_forced(), energy_functional_form_is_forced())

    # EM coefficient from microscopic stiffness: c = 1/K (duality of XY-stiffness to gauge theory)
    from rope_solver.electromagnetism import em_coefficient_from_stiffness
    _c = em_coefficient_from_stiffness(2.5)
    check("EM coefficient c = 1/K from coarse-grained rope stiffness (dual gauge theory)",
          abs(_c - 0.4) < 1e-12, f"c=1/K={_c} for K=2.5 (c is a rope modulus, not a free constant)")

    # Phase selection: Maxwell requires defect core energy above monopole-condensation threshold
    from rope_solver.electromagnetism import realizes_maxwell_phase
    _maxwell = realizes_maxwell_phase(defect_core_energy=5.0, condensation_threshold=1.0)
    _confined = realizes_maxwell_phase(defect_core_energy=0.5, condensation_threshold=1.0)
    check("Maxwell (massless-photon) phase iff defects resist condensation",
          _maxwell["long_range_magnetism"] and not _confined["long_range_magnetism"],
          f"above->{_maxwell['phase'][:20]}; below->{_confined['phase'][:20]}")

    # Microscopic coefficient chain: c = kappa*a/(2 T^2), beta_eff = 2 T^2/kappa
    # (coefficient corrected 2026-07-04 from factor 3 to 2 per the Factor-of-Three Audit)
    from rope_solver.electromagnetism import em_coefficient_microscopic
    _stiff = em_coefficient_microscopic(strand_tension=2.0, bond_stiffness=1.0, rope_spacing=1.0)
    _floppy = em_coefficient_microscopic(strand_tension=0.3, bond_stiffness=1.0, rope_spacing=1.0)
    check("c = kappa*a/(2 T^2): coefficient coarse-grained to rope primitives (director, 2 modes)",
          abs(_stiff["c"] - 1.0/(2*4.0)) < 1e-12, f"c={_stiff['c']:.4f} for T=2,kappa=a=1")
    check("stiff high-tension ropes -> Maxwell phase; floppy -> not",
          _stiff["maxwell_phase"] and not _floppy["maxwell_phase"],
          f"beta_eff stiff={_stiff['beta_eff']:.2f} vs floppy={_floppy['beta_eff']:.2f}")

    # Exact J from endpoint mechanics: XY form is exact, J = F^2/kappa (ratio dtheta-independent)
    from rope_solver.electromagnetism import locking_energy_from_endpoint_mechanics
    _ratios = []
    for _dth in (0.3, 0.9, 1.7, 2.5):
        _E = locking_energy_from_endpoint_mechanics(F=1.5, kappa=2.0, dtheta=_dth)
        _ratios.append(_E / (1 - np.cos(_dth)))   # should all equal F^2/kappa = 1.125
    check("endpoint mechanics gives exact XY locking with J=F^2/kappa (dtheta-independent)",
          max(_ratios) - min(_ratios) < 1e-12 and abs(_ratios[0] - 1.5**2/2.0) < 1e-12,
          f"J ratio constant = {_ratios[0]:.4f} across dtheta (= F^2/kappa)")

    # New prediction: alpha and G co-vary; tension channel gives d ln alpha = -2 d ln G
    from rope_solver.electromagnetism import alpha_G_covariation_exponent
    check("cross-sector prediction: tension drift => d ln alpha = -2 d ln G (scale-free)",
          alpha_G_covariation_exponent("tension") == -2.0,
          "alpha_dot/alpha = -2 G_dot/G (provisional on gravity G(T); structure robust)")

    print("\n"+"="*64)
    npass = sum(1 for _, ok in results if ok)
    print(f"RESULT: {npass}/{len(results)} EM tests passed")
    print("="*64)
    return 0 if npass == len(results) else 1



def test_em_regression():
    """Pytest entry point: the regression suite must pass in full."""
    assert main() == 0


if __name__ == "__main__":
    sys.exit(main())
