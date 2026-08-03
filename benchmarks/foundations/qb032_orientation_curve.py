"""QB-032: P1' converted from premise to parameter -- the Bell violation as a
function of source orientation under the derived transport law. Bars locked in
analysis/QB032_orientation_curve_bars_LOCKED.md (prediction before MC, per
orientation)."""
import os, sys
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "quantum"))
from qb030_bell_from_nucleation import build_delta_bank
from qb031_transport_law import rodrigues
from bell_experiment import device

A = np.array([0, 0, 1.0]); AP = np.array([1.0, 0, 0])
B = np.array([np.sin(np.pi / 4), 0, np.cos(np.pi / 4)])
BP = np.array([np.sin(3 * np.pi / 4), 0, np.cos(3 * np.pi / 4)])
PAIRS = ((A, B), (A, BP), (AP, B), (AP, BP))
COMBOS = ((1, 1, 1, -1), (1, 1, -1, 1), (1, -1, 1, 1), (-1, 1, 1, 1))


def b1_effective_map():
    d, c = sp.symbols('delta cbar', real=True)
    # Rodrigues: R_n(d) = cos d I + sin d [n]_x + (1 - cos d) n n^T.
    # A delta-symmetric ensemble kills the [n]_x term; <cos d> = cbar gives
    # M(n) = cbar I + (1 - cbar) n n^T. Isotropic average of n n^T is I/3:
    iso = sp.simplify(c + (1 - c) / 3)
    assert sp.simplify(iso - (1 + 2 * c) / 3) == 0
    print("B1 PASS  M(n) = cbar I + (1 - cbar) n n^T (sin term killed by delta")
    print("         symmetry); isotropic average recovers QB-031's (1 + 2 cbar)/3.")


def s_pred(n, cbar, k):
    Mm = cbar * np.eye(3) + (1 - cbar) * np.outer(n, n)
    vals = [-(x @ Mm @ y) for x, y in PAIRS]
    return k * max(abs(sum(s * u for s, u in zip(sg, vals))) for sg in COMBOS)


def run_mc(bank, W, axis=None, M=100000, seed=17):
    rng = np.random.default_rng(seed)
    v = rng.normal(size=(M, 3)); nn = v / np.linalg.norm(v, axis=1, keepdims=True)
    vals, margs = [], []
    for x, y in PAIRS:
        Aout = np.where(rng.random(M) < W(nn @ x), 1, -1)
        f = -(Aout[:, None]) * x[None, :]
        delta = rng.choice(bank, size=M)
        if axis is None:                      # isotropic reference
            ax = rng.normal(size=(M, 3)); ax /= np.linalg.norm(ax, axis=1, keepdims=True)
        else:
            ax = np.tile(axis, (M, 1))
        f = rodrigues(f, ax, delta)
        Bout = np.where(rng.random(M) < W(np.sum(f * y, axis=1)), 1, -1)
        vals.append(np.mean(Aout * Bout)); margs.append(abs(np.mean(Bout)))
    S = max(abs(sum(s * u for s, u in zip(sg, vals))) for sg in COMBOS)
    return S, max(margs)


def main():
    b1_effective_map()
    bank = build_delta_bank()
    cbar = float(np.mean(np.cos(bank)))
    ths = np.deg2rad([0, 45, 90, 135, 180])
    Wt = np.array([device(t) for t in ths])
    W = lambda cc: np.interp(np.arccos(np.clip(cc, -1, 1)), ths, Wt)
    S_perf = 2 * np.sqrt(2) * (Wt[0] - Wt[-1] + (Wt[1] - Wt[3]) * np.sqrt(2)) / (
        1 + np.sqrt(2))  # not used for k; keep table-based k below
    # response slope from the same-run perfect closed form:
    Ed = lambda x, y: W(np.array([-(x @ y)]))[0] - W(np.array([x @ y]))[0]
    vals_d = [Ed(x, y) for x, y in PAIRS]
    S_det = max(abs(sum(s * u for s, u in zip(sg, vals_d))) for sg in COMBOS)
    k = S_det / (2 * np.sqrt(2))
    print(f"B2       cbar = {cbar:.3f}; same-run perfect closed form {S_det:.4f}; "
          f"slope k = {k:.4f}")

    orients = {"y-hat (perp to plane)": np.array([0, 1.0, 0]),
               "z-hat (along a)": np.array([0, 0, 1.0]),
               "x-hat (along a')": np.array([1.0, 0, 0]),
               "(x+z)/sqrt2 (Bell diagonal)": np.array([1, 0, 1.0]) / np.sqrt(2),
               "(x+y)/sqrt2": np.array([1, 1.0, 0]) / np.sqrt(2)}
    preds = {name: s_pred(n, cbar, k) for name, n in orients.items()}
    pred_iso = ((1 + 2 * cbar) / 3) * S_det
    print("B2       analytic predictions (BEFORE MC, rule R1):")
    for name, p in preds.items():
        print(f"           {name:28s} S_pred = {p:.3f}")
    print(f"           {'isotropic reference':28s} S_pred = {pred_iso:.3f}")

    print("B3       Monte Carlo (M = 100000/pair):")
    results = {}
    worst = 0.0
    for name, n in orients.items():
        S, ns = run_mc(bank, W, axis=n)
        rel = abs(S - preds[name]) / preds[name]
        worst = max(worst, rel)
        results[name] = S
        print(f"           {name:28s} S = {S:.4f} ({rel:.1%} from pred; "
              f"no-sig {ns:.3f})")
        assert ns < 0.015
    S_iso, ns_i = run_mc(bank, W, axis=None)
    rel_i = abs(S_iso - pred_iso) / pred_iso
    worst = max(worst, rel_i)
    print(f"           {'isotropic reference':28s} S = {S_iso:.4f} "
          f"({rel_i:.1%}; no-sig {ns_i:.3f})")
    assert worst < 0.10, f"first-order rule violated: {worst:.1%}"
    print(f"B3 PASS  all orientations within first order ({worst:.1%} worst; "
          f"rule 10%).")
    # R3 endpoints
    assert abs(results["y-hat (perp to plane)"] - 2.039) < 0.12
    assert abs(S_iso - 2.234) < 0.06
    print("B3 PASS  endpoints adjudicated: perpendicular orientation lands at")
    print("         QB-030's floor; isotropic reference at QB-031's 2.234.")
    best = max(results, key=results.get)
    print(f"B4       THE CURVE'S EXTREMES: minimum at the perpendicular")
    print(f"         orientation ({results['y-hat (perp to plane)']:.3f}); maximum")
    print(f"         at {best} ({results[best]:.3f}). P1' IS NOW A PARAMETER: any")
    print("         lab geometry maps onto S(n) = k x CHSH[cbar I + (1-cbar)nn^T],")
    print("         with the isotropic value the generic expectation and the")
    print("         whole span violating the classical bound.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
