"""ELEC-047 -- THE BUNDLE CENSUS AT THE COHERENCE RADIUS.

Bars locked in analysis/ELEC047_bundle_census_bars_LOCKED.md BEFORE this ran.
QGATE-004's census returned "underdetermined by one ratio" because w was free;
ELEC-040 fixed it. This census counts strands in the medium's actual 3D
geometry (Poisson line process at spacing w) and asks whether the derived
barrier's own dynamics can supply the event duration that causal recruitment
requires.

Units: w = 1 for geometry; SI where stated. All inputs registered.
"""
import numpy as np

HBAR = 1.054571817e-34
C = 2.99792458e8
T_S = 1.70e3
# [ELEC-049 SUPERSESSION NOTE] The w = 2.87e-16 m below was a promotion error
# (Ledger A, never registered); adjudicated spacing is w = 5.78e-17 m. This file
# is preserved AS RUN because registered claims pin its arithmetic; ELEC-048's
# two-ledger test shows every verdict survives re-basing. Do not update silently.
W_SP = 2.87e-16
NT_DEMAND = 498.0          # ELEC-046
DC = 3.2e-3                # d_c / w


# ---------- geometry: Poisson line process ----------
def mc_count(R, rho_L=1.0, trials=200000, rng=None):
    """Monte Carlo: expected number of isotropic Poisson lines (length density
    rho_L per w^2) intersecting a ball of radius R. Sample lines by hitting
    measure: a line hits the ball iff its closest approach b < R; generate
    impact parameter b with density ~ b (disk) at random orientation and use
    the exact hitting-intensity normalization E[N] = rho_L * pi * R^2 as the
    analytic target; the MC verifies via chord-length bookkeeping:
    E[total length in ball] = rho_L * (4/3) pi R^3 and mean chord = 4R/3."""
    rng = rng or np.random.default_rng(7)
    b = R * np.sqrt(rng.random(trials))          # impact parameters of hitting lines
    chord = 2.0 * np.sqrt(R ** 2 - b ** 2)
    mean_chord = chord.mean()                    # -> 4R/3
    n_expected = rho_L * (4.0 / 3.0) * np.pi * R ** 3 / mean_chord
    return n_expected, mean_chord


def n_analytic(R):
    return np.pi * R ** 2


# ---------- dynamics: traversal time on the derived barrier (ELEC-045) ----------
def V_of_s(s, l=4.0):
    d = (1.0 - s) / 2.0
    return 2.0 * (2.0 * np.hypot(l / 2.0, d) - l)


def mu_of_s(s, l=4.0, n=2001):
    x = np.linspace(-l / 2, l / 2, n)
    tri = 1.0 - np.abs(x) / (l / 2.0)
    d = (1.0 - s) / 2.0
    seg = np.hypot(l / 2.0, d)
    return 2.0 * np.trapezoid((tri / 2.0) ** 2 * (seg / (l / 2.0)), x)


def traversal_time(eps, l=4.0, ns=40001):
    """Time to cross the barrier from s = 1 (rest) to s = d_c at
    E = E_b (1 + eps): tau = int ds sqrt(mu / (2 (E - V)))."""
    s = np.linspace(DC, 1.0 - 1e-9, ns)
    V = V_of_s(s, l)
    Eb = V_of_s(DC, l)
    E = Eb * (1.0 + eps)
    mu = np.array([mu_of_s(si, l, 401) for si in s[:: ns // 100 + 1]])
    mu = np.interp(s, s[:: ns // 100 + 1], mu)
    integrand = np.sqrt(mu / (2.0 * np.maximum(E - V, 1e-300)))
    return float(np.trapezoid(integrand, s))


def main():
    # B1: bookkeeping closure (flagged tautology-adjacent)
    rho = (T_S / C ** 2) / W_SP ** 2
    rho_nuc = 2.3e17
    b1 = abs(rho / rho_nuc - 1) < 0.20
    print(f"B1 bookkeeping: rho_medium = (T_s/c^2)/w^2 = {rho:.3e} kg/m^3 vs nuclear "
          f"{rho_nuc:.1e} ({rho/rho_nuc:.3f}x)  [{'PASS' if b1 else 'FAIL'}] -- "
          f"TAUTOLOGY-ADJACENT: w was DEFINED from nuclear density; this validates the "
          f"line-counting convention, not the physics.")

    # B2: instrument -- MC vs analytic
    errs = []
    for R in (5.0, 12.0, 22.0):
        n_mc, mc_chord = mc_count(R)
        err = abs(n_mc / n_analytic(R) - 1)
        errs.append(err)
        print(f"    R={R:4.1f}w: MC {n_mc:8.1f} vs analytic pi R^2 = {n_analytic(R):8.1f} "
              f"({err*100:.2f}%); mean chord {mc_chord:.4f} vs 4R/3 = {4*R/3:.4f}")
    b2 = all(e < 0.05 for e in errs)
    print(f"B2 instrument: [{'PASS' if b2 else 'FAIL -- VOID'}]")
    assert b2, "B2 FAIL"

    # B3: THE CENSUS
    n_at_22 = n_analytic(22.3)
    R_req = np.sqrt(NT_DEMAND / np.pi)
    print(f"B3 census: n(22.3w) = {n_at_22:.0f} strands ({n_at_22/NT_DEMAND:.2f}x the demand); "
          f"the demand n = 498 is met at R_req = {R_req:.2f} w -- SMALLER than the quoted "
          f"22.3w (the 2D sheet scaling in ELEC-046 was conservative; 3D geometry is richer). "
          f"GEOMETRIC VERDICT: the medium CONTAINS the strands, comfortably.")

    # B4: the mechanism -- AS LOCKED this bar assumed separatrix slowing (log-divergent
    # traversal time). THE PREMISE IS WRONG for the derived profile: V(s) is MONOTONE,
    # the barrier top is an ENDPOINT not a stationary point, so E - V vanishes linearly
    # at the boundary and the traversal time converges to a FINITE limit. Measured:
    eps_grid = np.array([1e-1, 1e-2, 1e-3, 1e-4, 1e-6, 1e-8])
    taus = np.array([traversal_time(e) for e in eps_grid])
    tau0 = taus[-1]                       # saturated limit, w/c units
    R_free = tau0                         # one-way causal radius of the bare event
    n_free = np.pi * R_free ** 2
    tau_req_oneway = R_req
    shortfall_t = tau_req_oneway / tau0
    shortfall_n = NT_DEMAND / n_free
    b4 = False
    print(f"B4 mechanism: tau(eps) SATURATES: {list(zip(eps_grid, taus.round(3)))}")
    print(f"    [FAIL AND KEPT -- the locked bar's premise was wrong: no separatrix slowing "
          f"exists (monotone profile, endpoint top); third locked-formula error caught by its "
          f"own bars this arc.]")
    print(f"    The bare event's causal budget: tau0 = {tau0:.2f} w/c, R_free = {R_free:.2f} w, "
          f"n_free = pi R_free^2 = {n_free:.1f} strands recruited for free.")
    print(f"    Shortfall to the demand: {shortfall_t:.1f}x in duration, {shortfall_n:.0f}x in count.")

    # B5: verdict discipline
    print("B5 verdict, against ELEC-046's trichotomy: the DYNAMICS returned the ~order-10 "
          f"branch (n_free = {n_free:.0f}), not ~500. THE CHAIN DOES NOT CLOSE FROM REGISTERED "
          "PHYSICS: the medium contains 498 strands within 12.6w (geometry, B3) but the bare "
          "reconnection event can causally recruit only ~12 of them (dynamics, B4). What "
          "survives is exactly ELEC-043's named escape -- a PRE-CORRELATED medium -- now "
          "priced precisely: correlations spanning >= 12.6 w must deliver ~498 participating "
          "strands, a 45x recruitment gap the event itself cannot bridge. Causal contact is "
          "NECESSARY for participation, not sufficient; that sentence is load-bearing -- and "
          "tonight even the necessary condition failed at the required scale. The "
          "hbar-from-reconnection chain is DEAD AS A DERIVATION and alive only as a "
          "long-range-order postulate carrying its own unpaid bill.")
    print("PASS: the census answered decisively in the medium's own geometry and the "
          "barrier's own dynamics; the verdict is the negative one, reported without "
          "softening.")


if __name__ == "__main__":
    main()
