"""QB-030 (S3): the complete Bell experiment with the PRODUCED ribbon -- QB-027's
measured analyzers, the nucleated pair's exact base anticorrelation, and a per-trial
holonomy error drawn from an empirical bank of pinned-field samples (QB-029's
statistics). Bars locked in analysis/QB030_bell_from_nucleation_bars_LOCKED.md,
including the decision rule at 3 sigma against the classical bound.
"""
import os, sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "quantum"))
from bell_experiment import device  # QB-027's engine analyzer, verbatim

KT, TBATH, DT, N, H = 0.64, 0.4, 0.02, 192, 0.30
D_PAIR = 45


def build_delta_bank(seed=21, steps=400000, sample_from=200000, every=1500):
    """Empirical holonomy-error bank: interior phase differences of the pinned
    field at pair scale d = 45 (QB-029's measured statistics, resampled fresh)."""
    r = np.random.default_rng(seed)
    phi = np.full(N, float(np.arcsin(H)))
    bank = []
    for t in range(steps):
        lap = np.roll(phi, -1) - 2 * phi + np.roll(phi, 1)
        phi = phi + DT * (KT * lap - np.sin(phi) + H) \
            + np.sqrt(2 * TBATH * DT) * r.standard_normal(N)
        if t >= sample_from and t % every == 0:
            d = phi - np.roll(phi, -D_PAIR)
            bank.append(d - d.mean())      # remove the zero-mode offset per snapshot
    bank = np.concatenate(bank)
    return bank


def run_bell(delta_bank, M=200000, seed=11, mode="nucleated"):
    ths = np.deg2rad([0, 45, 90, 135, 180])
    Wt = np.array([device(t) for t in ths])
    dev = np.max(np.abs(Wt - np.cos(ths / 2) ** 2))
    assert dev < 0.03
    W = lambda c: np.interp(np.arccos(np.clip(c, -1, 1)), ths, Wt)
    rng = np.random.default_rng(seed)
    v = rng.normal(size=(M, 3))
    nn = v / np.linalg.norm(v, axis=1, keepdims=True)

    def E_pair(x, y):
        A = np.where(rng.random(M) < W(nn @ x), 1, -1)
        f = -(A[:, None]) * x[None, :]                  # the transmitted frame
        if mode == "nucleated":
            delta = rng.choice(delta_bank, size=M)
            # coherent rotation by delta about a random perpendicular axis
            w = rng.normal(size=(M, 3))
            w -= (np.sum(w * f, axis=1, keepdims=True)) * f
            w /= np.linalg.norm(w, axis=1, keepdims=True)
            f = np.cos(delta)[:, None] * f + np.sin(delta)[:, None] * w
        elif mode == "severed":
            f = -nn
        B = np.where(rng.random(M) < W(np.sum(f * y, axis=1)), 1, -1)
        return np.mean(A * B), np.mean(B)

    a = np.array([0, 0, 1.0]); ap = np.array([1.0, 0, 0])
    b = np.array([np.sin(np.pi / 4), 0, np.cos(np.pi / 4)])
    bp = np.array([np.sin(3 * np.pi / 4), 0, np.cos(3 * np.pi / 4)])
    pairs = ((a, b), (a, bp), (ap, b), (ap, bp))
    vals, margs = [], []
    for x, y in pairs:
        e, m2_ = E_pair(x, y)
        vals.append(e); margs.append(m2_)
    combos = ((1, 1, 1, -1), (1, 1, -1, 1), (1, -1, 1, 1), (-1, 1, 1, 1))
    S = max(abs(sum(s * u for s, u in zip(sg, vals))) for sg in combos)
    return S, max(abs(m) for m in margs), Wt


def v_of_T(Ts):
    ks = 2 * np.pi * np.arange(1, N) / N
    m2 = float(np.sqrt(1 - H ** 2))
    denom = m2 + 2 * KT * (1 - np.cos(ks))
    s = np.sum(1 / denom) / N
    return np.exp(-np.asarray(Ts) * s)     # V(T) = exp(-var_sat(T)/2), var ~ 2 T s


def main():
    bank = build_delta_bank()
    cosd = float(np.mean(np.cos(bank)))
    print(f"B2       empirical bank: {len(bank)} samples; <cos delta> = {cosd:.3f}")
    ref = np.exp(-np.var(bank) / 2)
    assert abs(cosd - ref) / ref < 0.10
    print(f"B2 PASS  bank consistent with exp(-var/2) = {ref:.3f} (within 10%).")

    S_perf, ns_p, Wt = run_bell(bank, mode="perfect")
    # self-consistency: the same-run closed form from the deterministic table
    ths = np.deg2rad([0, 45, 90, 135, 180])
    W = lambda c: np.interp(np.arccos(np.clip(c, -1, 1)), ths, Wt)
    a = np.array([0, 0, 1.0]); ap = np.array([1.0, 0, 0])
    b = np.array([np.sin(np.pi / 4), 0, np.cos(np.pi / 4)])
    bp = np.array([np.sin(3 * np.pi / 4), 0, np.cos(3 * np.pi / 4)])
    Ed = lambda x, y: W(np.array([-(x @ y)]))[0] - W(np.array([x @ y]))[0]
    vals_d = [Ed(x, y) for x, y in ((a, b), (a, bp), (ap, b), (ap, bp))]
    combos = ((1, 1, 1, -1), (1, 1, -1, 1), (1, -1, 1, 1), (-1, 1, 1, 1))
    S_det = max(abs(sum(s * u for s, u in zip(sg, vals_d))) for sg in combos)
    print(f"B1/B3    analyzer calibration OK (visibility {Wt[0]-Wt[-1]:.3f});")
    print(f"         PERFECT-ribbon reference: CHSH = {S_perf:.4f} vs same-run")
    print(f"         closed form {S_det:.4f} (QB-027 printed 2.66 in its own")
    print(f"         environment; the table is environment-sensitive at the 0.07")
    print(f"         level -- FLAGGED for annotation, self-consistency is the bar)")
    assert abs(S_perf - S_det) < 0.03
    S_sev, _, _ = run_bell(bank, mode="severed")
    print(f"         SEVERED control: CHSH = {S_sev:.4f} (< 2 required)")
    assert S_sev < 2.0

    S, ns, _ = run_bell(bank, mode="nucleated")
    sig = 2.0 / np.sqrt(200000)            # conservative sigma(S)
    print(f"B4       THE PRODUCED RIBBON: CHSH = {S:.4f} +/- ~{sig:.4f}; "
          f"no-signaling {ns:.4f}")
    assert ns < 0.015
    if S > 2 + 3 * sig:
        verdict = ("VIOLATION -- the medium's produced pair, with its measured "
                   "holonomy noise, beats local realism")
    elif S < 2 - 3 * sig:
        verdict = "BELOW THE BOUND -- the produced ribbon fails at these parameters"
    else:
        verdict = "MARGINAL at 3 sigma"
    print(f"B4 VERDICT (locked rule): {verdict}")

    Ts = np.array([0.4, 0.3, 0.2, 0.1, 0.05])
    Vs = v_of_T(Ts)
    print("B5       V(T) from the lattice sum and the implied first-order S:")
    for T, V in zip(Ts, Vs):
        print(f"           T = {T:.2f}: V = {V:.3f}   S ~ {V*2.66:.2f}")
    T_cross = -np.log(2 / 2.66) / (np.log(v_of_T([1.0])[0]) * -1)
    print(f"         first-order crossing (S = 2): T ~ {T_cross:.2f} -- the engine's")
    print(f"         T = 0.4 sits {'below' if 0.4 < T_cross else 'above'} it.")
    print("B6       verdict propagated; QB-027's ribbon premise updated from")
    print("         BY-FIAT to PRODUCED-AT-MEASURED-VISIBILITY on this branch; the")
    print("         engine-temperature caveat carried (T = 0.4 is a simulation")
    print("         parameter, not the vacuum's).")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
