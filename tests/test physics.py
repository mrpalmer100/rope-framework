"""
tests/test_physics.py  --  Regression tests for the physics-endpoint modules.

These pin the gravity, spectrum, and particle quantities to their published
values, so no future change (or new paper) can quote a number inconsistent
with the reference implementation.

Run:  python3 tests/test_physics.py
"""
import numpy as np
import sys
from rope_solver.gravity import (ppn_parameters, mercury_perihelion_arcsec_per_century,
    light_deflection_arcsec, nordtvedt_eta)
from rope_solver.spectrum import (poschl_teller_bound_states, log_det_ratio,
    required_log_det_for_electron)
from rope_solver.particles import (kappa_from_alpha, dimensional_transmutation_b,
    charge_is_linking_number, higher_link_energy_scaling)
from rope_solver.topology.linking import hopf_curves


def main():
    results = []
    def check(name, cond, detail=""):
        results.append((name, cond))
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}  {detail}")

    print("="*64); print("PHYSICS REGRESSION SUITE"); print("="*64)

    print("\n1. Gravity: PPN parameters and classical tests")
    g, b = ppn_parameters()
    check("gamma = 1", abs(g-1) < 1e-9, f"gamma={g}")
    check("beta = 1", abs(b-1) < 1e-9, f"beta={b}")
    merc = mercury_perihelion_arcsec_per_century()
    check("Mercury perihelion ~ 42.98 arcsec/cy", abs(merc-42.98) < 1.0,
          f"{merc:.2f}")
    defl = light_deflection_arcsec()
    check("Light deflection ~ 1.751 arcsec", abs(defl-1.751) < 0.02, f"{defl:.3f}")
    check("Nordtvedt eta = 0", abs(nordtvedt_eta()) < 1e-9, f"{nordtvedt_eta()}")

    print("\n2. Spectrum: Poeschl-Teller validation + determinant magnitude")
    bs = poschl_teller_bound_states(1)
    check("Poeschl-Teller ell=1 has 1 bound state", len(bs) == 1,
          f"n={len(bs)}")
    check("Poeschl-Teller ground state E ~ -1", abs(bs[0]+1.0) < 0.01,
          f"E={bs[0]:.4f}")
    need = required_log_det_for_electron()
    check("electron needs ln[det]~108 (one-loop gives O(1))", need > 100,
          f"need={need:.0f}, one-loop~0.1 -> falsified")

    print("\n3. Particles: coupling, charge, transmutation")
    check("kappa = alpha/2pi", abs(kappa_from_alpha() - (1/137.036)/(2*np.pi)) < 1e-9,
          f"{kappa_from_alpha():.5f}")
    C1, C2 = hopf_curves(60, R=1.0)
    q = charge_is_linking_number(C1, C2)
    check("Hopf charge q=Lk=1", abs(abs(q)-1) < 0.1, f"q={q:.3f}")
    b_e = dimensional_transmutation_b(4e-23)
    check("electron transmutation b ~ 17", 14 < b_e < 20, f"b={b_e:.1f}")
    p = higher_link_energy_scaling([1,2,3], [126.1,132.9,138.1])
    check("higher-link E~Lk^p sub-linear (p<0.2)", p < 0.2, f"p={p:.3f}")

    print("\n4. Lepton mass ratios via Koide phase (CONJECTURE -- see open_problems)")
    from rope_solver.particles import (quantum_dimension_su2k, koide_phase_coefficient,
        lepton_mass_ratios, GOLDEN_RATIO)
    # the rigorous part: d_1/2 = Phi exactly at k=3
    d_half = quantum_dimension_su2k(1, 3)
    check("d_1/2 = Phi at k=3 (rigorous TQFT)", abs(d_half - GOLDEN_RATIO) < 1e-9,
          f"d={d_half:.6f}")
    check("(3+Phi) coefficient = 4.6180", abs(koide_phase_coefficient() - 4.618034) < 1e-5,
          f"{koide_phase_coefficient():.5f}")
    # the numerical success: ratios match to <1% WITH measured theta_W
    r = lepton_mass_ratios(sin2_thetaW=0.23122)
    check("m_mu/m_e ~ 206.8 (measured theta_W)", abs(r["mu/e"] - 206.77)/206.77 < 0.01,
          f"{r['mu/e']:.1f}")
    check("m_tau/m_e ~ 3477 (measured theta_W)", abs(r["tau/e"] - 3477.2)/3477.2 < 0.01,
          f"{r['tau/e']:.0f}")
    # the HONEST caveat, pinned: with the rope's OWN sin2thetaW=1/(3sqrt2) it FAILS
    r_rope = lepton_mass_ratios(sin2_thetaW=1/(3*np.sqrt(2)))
    check("NOT parameter-free: rope's own theta_W breaks it (>5x error)",
          abs(r_rope["mu/e"] - 206.77)/206.77 > 1.0,
          f"mu/e={r_rope['mu/e']:.0f} with rope theta_W")

    print("\n5. Chiral central charge -> fiber mode T-odd (rigorous upgrade)")
    from rope_solver.particles import chiral_central_charge, breaks_time_reversal
    c3 = chiral_central_charge(3)
    check("c(SU(2)_3) = 9/5 (exact)", abs(c3 - 9/5) < 1e-12, f"c={c3}")
    check("SU(2)_3 breaks time reversal (c != 0)", breaks_time_reversal(3),
          "-> fiber mode T-odd by theorem, not by failed helicity/linking args")
    # the rope's claimed sin2thetaW is the SOFT external input; record it's off
    check("rope sin2thetaW=1/(3sqrt2) is ~1.9% from measured 0.23122",
          abs(1/(3*np.sqrt(2)) - 0.23122)/0.23122 > 0.015,
          f"1/(3sqrt2)={1/(3*np.sqrt(2)):.4f}")

    print("\n6. Absolute mass: suppression is provably external to the knot")
    from rope_solver.particles import (knot_euclidean_action_planck_units,
        mass_suppression_is_internal)
    check("knot Euclidean action = O(1) in Planck units",
          abs(knot_euclidean_action_planck_units() - 1.0) < 1e-9, "S_E=1")
    check("electron suppression NOT internal to knot (must be cosmological)",
          mass_suppression_is_internal() == False, "-> knot-cosmos coupling")

    print("\n7. Tension beta function: dimensional transmutation closed by structure")
    from rope_solver.particles import (luscher_critical_scale_planck,
        wzw_beta_function, dimensional_transmutation_works)
    check("Luscher critical scale is O(1) Planck (power-law, no hierarchy)",
          0.1 < luscher_critical_scale_planck() < 2.0,
          f"{luscher_critical_scale_planck():.3f} L_Pl")
    check("SU(2)_3 WZW beta = 0 (conformal fixed point, no running)",
          wzw_beta_function(3) == 0.0, "beta=0")
    check("dimensional transmutation cannot make the mass scale",
          dimensional_transmutation_works() == False, "-> needs cosmological breaking")

    print("\n8. Benchmark catalogue integrity")
    from rope_solver.benchmark_catalogue import CATALOGUE, by_id, by_prefix
    check("catalogue non-empty", len(CATALOGUE) > 0, f"n={len(CATALOGUE)}")
    check("all IDs unique", len(set(b["id"] for b in CATALOGUE)) == len(CATALOGUE), "")
    valid_tests = {"test_validation","test_physics","test_electromagnetism","reproduce_results"}
    check("every benchmark cites a known test suite",
          all(b["test"] in valid_tests for b in CATALOGUE), "")
    check("G-002 is Mercury perihelion (frozen ID)",
          by_id("G-002")["name"] == "Mercury perihelion", "")
    check("ID prefixes are the frozen set",
          set(b["id"].split("-")[0] for b in CATALOGUE) <= {"N","G","EM","P","S"}, "")

    print("\n9. Cosmic closure relation (expansion-tension origin of G)")
    from rope_solver.gravity import cosmic_closure_ratio
    r = cosmic_closure_ratio()
    check("G M /(R c^2) = 1/2 (universe at its Schwarzschild radius)",
          abs(r - 0.5) < 1e-9, f"ratio={r}")
    # honest: this is a consistency relation, not a derivation of G (M carries G)
    check("closure ratio is H0-independent (pure consistency relation)",
          abs(cosmic_closure_ratio(H0_km_s_Mpc=67.0) - cosmic_closure_ratio(H0_km_s_Mpc=73.0)) < 1e-12,
          "same for any H0 -> yields no absolute G")

    print("\n10. Electron mass: Hubble-Planck exponent and CFT-dressing scan")
    from rope_solver.particles import hubble_planck_mass_exponent, su2k3_dressing_scan
    p1 = hubble_planck_mass_exponent(70.0); p2 = hubble_planck_mass_exponent(70.0, two_pi_convention=True)
    check("required exponent p ~ 0.367 (H0=70, plain convention)",
          0.367 < p1 < 0.368, f"p={p1:.5f}")
    check("IR-mass convention shifts p by ~1.3% (coincidences sharper than 1% are noise)",
          abs(p1-p2)/p1 > 0.01, f"plain={p1:.5f} vs 2pi={p2:.5f}")
    gap, best = su2k3_dressing_scan()
    check("no SU(2)_3 natural number matches p within 1% (dressing route CLOSED)",
          gap > 1.0, f"best candidate {best} misses by {gap:.2f}% (bar is <0.1%)")

    print("\n"+"="*64)
    npass = sum(1 for _, ok in results if ok)
    print(f"RESULT: {npass}/{len(results)} physics regression tests passed")
    print("="*64)
    return 0 if npass == len(results) else 1



def test_physics_regression():
    """Pytest entry point: the regression suite must pass in full."""
    assert main() == 0


if __name__ == "__main__":
    sys.exit(main())
