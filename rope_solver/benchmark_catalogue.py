"""
rope_solver.benchmark_catalogue  --  Formal, frozen benchmark numbering.

Every benchmark has a stable ID (e.g. G-001) that papers cite instead of
re-stating numbers. The ID, expected value, tolerance, and the test that
verifies it are all recorded here, so a paper saying "see benchmark G-002"
points to one frozen, regression-tested quantity.

ID scheme (frozen as of rope_solver 2.0):
  N-xxx  numerical primitives (solver, linking, tension)
  G-xxx  gravity / PPN
  EM-xxx electromagnetism + light
  P-xxx  particles (charge, links, mass machinery)
  S-xxx  spectrum / fluctuation determinant

Adding benchmarks is allowed in 2.x (new IDs only). Renumbering or repurposing
an existing ID is a BREAKING change reserved for a major version, because papers
cite these IDs.
"""

CATALOGUE = [
    # --- numerical primitives ---
    {"id": "N-001", "name": "Laplacian on plane wave",
     "value": "ratio 0.991", "test": "test_validation",
     "module": "psi.solver", "desc": "nabla^2 sin(kx) = -k^2 sin(kx)"},
    {"id": "N-002", "name": "psi ~ 1/r (boundary-corrected)",
     "value": "corr 0.99998", "test": "test_validation",
     "module": "psi.solver", "desc": "point-source field shape"},
    {"id": "N-003", "name": "Brill-Lindquist harmonic",
     "value": "max 0.003", "test": "test_validation",
     "module": "psi.solver", "desc": "nabla^2(1+rs/4r) ~ 0 interior"},
    {"id": "N-004", "name": "Tension force = -grad(length)",
     "value": "err 4e-10", "test": "test_validation",
     "module": "geometry.curve", "desc": "rope tension, not spring"},

    # --- gravity ---
    {"id": "G-001", "name": "Schwarzschild / PPN",
     "value": "gamma=beta=1", "test": "test_physics",
     "module": "gravity", "desc": "PPN parameters of the rope metric"},
    {"id": "G-002", "name": "Mercury perihelion",
     "value": "43.00 arcsec/cy", "test": "test_physics",
     "module": "gravity", "desc": "perihelion advance"},
    {"id": "G-003", "name": "Light deflection",
     "value": "1.751 arcsec", "test": "test_physics",
     "module": "gravity", "desc": "solar-limb deflection"},
    {"id": "G-004", "name": "Nordtvedt eta",
     "value": "0", "test": "test_physics",
     "module": "gravity", "desc": "strong equivalence principle"},

    # --- electromagnetism + light ---
    {"id": "EM-001", "name": "Maxwell chain",
     "value": "4 eqs, d=3", "test": "test_electromagnetism",
     "module": "electromagnetism", "desc": "Bianchi + Chern-Weil + Helmholtz"},
    {"id": "EM-002", "name": "EM constants (eps0, Z0, alpha)",
     "value": "Z0=376.7 ohm", "test": "test_electromagnetism",
     "module": "electromagnetism", "desc": "structural constant relations"},
    {"id": "EM-003", "name": "Charge quantization (q=Lk)",
     "value": "integer Lk", "test": "test_electromagnetism",
     "module": "electromagnetism", "desc": "topological charge"},
    {"id": "EM-004", "name": "Photon (Lk=0, non-dispersive)",
     "value": "omega=ck", "test": "test_electromagnetism",
     "module": "electromagnetism.photon", "desc": "massless, no vacuum dispersion"},
    {"id": "EM-005", "name": "Cosmic birefringence EB/EE",
     "value": "0.0119", "test": "test_electromagnetism",
     "module": "electromagnetism.photon", "desc": "LiteBIRD prediction"},
    {"id": "EM-006", "name": "Cross-sector locks",
     "value": "alpha, c, eps0 agree", "test": "test_electromagnetism",
     "module": "electromagnetism", "desc": "EM<->particles<->gravity<->chemistry"},

    # --- particles ---
    {"id": "P-001", "name": "Charge = linking number",
     "value": "q=Lk", "test": "test_physics",
     "module": "particles", "desc": "Hopf charge 1"},
    {"id": "P-002", "name": "Hopf relaxation conserves Lk",
     "value": "|Lk|=1,2,3", "test": "reproduce_results",
     "module": "relaxation", "desc": "topology conserved under relaxation"},
    {"id": "P-003", "name": "Coupling kappa = alpha/2pi",
     "value": "0.00116", "test": "test_physics",
     "module": "particles", "desc": "coupling identification"},
    {"id": "P-004", "name": "Lepton mass ratios (Koide phase)",
     "value": "0.5% (CONJECTURE)", "test": "test_physics",
     "module": "particles", "desc": "phi=(3+Phi)theta_W; see open_problems"},
    {"id": "P-005", "name": "Chiral central charge",
     "value": "c=9/5", "test": "test_physics",
     "module": "particles", "desc": "SU(2)_3 breaks T (fiber mode T-odd)"},
    {"id": "P-006", "name": "Knot action O(1) / mass external",
     "value": "S_E=1", "test": "test_physics",
     "module": "particles", "desc": "mass suppression not internal to knot"},

    # --- spectrum ---
    {"id": "S-001", "name": "Fluctuation determinant",
     "value": "Poschl-Teller validated", "test": "test_physics",
     "module": "spectrum", "desc": "one-loop mass mechanism falsified"},

    # --- ring soliton ---
    {"id": "N-005", "name": "Stable ring knot",
     "value": "R*=0.86, m=12.1 M_Pl", "test": "reproduce_results",
     "module": "psi.solver", "desc": "tension-field balance soliton"},
    {"id": "N-006", "name": "Hopf link sourced minimum",
     "value": "R*=0.84", "test": "reproduce_results",
     "module": "psi.solver", "desc": "two-component link equilibrium"},
]


def by_id(bid):
    """Return the catalogue entry with the given ID, or None."""
    for b in CATALOGUE:
        if b["id"] == bid:
            return b
    return None


def by_prefix(prefix):
    """Return all entries whose ID starts with the given prefix (e.g. 'G')."""
    return [b for b in CATALOGUE if b["id"].split("-")[0] == prefix]


def print_catalogue():
    """Print the benchmark catalogue grouped by prefix."""
    order = ["N", "G", "EM", "P", "S"]
    names = {"N": "Numerical primitives", "G": "Gravity",
             "EM": "Electromagnetism + light", "P": "Particles",
             "S": "Spectrum"}
    print("=" * 70)
    print("ROPE_SOLVER BENCHMARK CATALOGUE")
    print("=" * 70)
    for pre in order:
        items = sorted(by_prefix(pre), key=lambda b: b["id"])
        if not items:
            continue
        print(f"\n[{names[pre]}]")
        for b in items:
            print(f"  {b['id']:<7} {b['name']:<34} {b['value']:<22} "
                  f"({b['test']})")
    print("\n" + "-" * 70)
    print(f"  {len(CATALOGUE)} benchmarks. Cite by ID in papers, e.g. "
          f"'see benchmark G-002'.")
    print("=" * 70)


if __name__ == "__main__":
    print_catalogue()
