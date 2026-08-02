"""ELEC-052 (Amendment 1 active; see bars file: full-range rule failed B1\nat d=0.9/1.0, void; signal-termination cut locked answer-blind) -- THE DEFINITIVE WIDTH: THE E^2-WEIGHTED INTEGRAL ON THE PAPER'S
OWN LATTICE POINTS (arXiv 2409.20168v1 ancillary data, uploaded by hand).

Bars locked in analysis/ELEC052_ancdata_bars_LOCKED.md BEFORE parsing.
Requires the anc/ directory (public arXiv ancillary files); path via env
ANC_DIR, default ./anc_data. If absent, prints SKIP (data is external).
"""
import os, re, sys
import numpy as np

R_PRED = 0.342   # fm (ELEC-050)
R_51 = 0.404     # fm (ELEC-051 reconstruction)
T_TUBE = 1.878e5
ANC = os.environ.get("ANC_DIR", "anc_data")
FILES = {0.7: "Ex_NP_d0.7fm_scaling_normfact.agr",
         0.9: "Ex_NP_d0.9fm_scaling_normfact.agr",
         1.0: "Ex_NP_d1.0fm_scaling_normfact.agr"}
PAPER_W = "width_from_integral.agr"


def parse_agr(path):
    sets, cur, on = [], [], False
    for line in open(path):
        if line.startswith("@type"):
            on = True; cur = []; continue
        if line.startswith("&"):
            if on and cur: sets.append(np.array(cur))
            on = False; continue
        if on:
            try: cur.append([float(v) for v in line.split()][:3])
            except ValueError: pass
    return sets


def widths(r, E):
    iE = np.trapezoid(r * E, r)
    if iE <= 0: return np.nan, np.nan
    wE = np.sqrt(np.trapezoid(r ** 3 * E, r) / iE)
    Req = np.sqrt(2 * np.trapezoid(r ** 3 * E ** 2, r) / np.trapezoid(r * E ** 2, r))
    return wE, Req


def truncate(r, E, dE):
    """Amendment 1: cut at signal termination -- first r where SNR<2 twice running."""
    snr = np.abs(E) / np.where(dE > 0, dE, np.inf)
    low = snr < 2
    for i in range(1, len(r)):
        if low[i] and low[i - 1]:
            return r[:i], E[:i], dE[:i]
    return r, E, dE


def fold(d):
    x, E, dE = d[:, 0], d[:, 1], d[:, 2]
    r = np.abs(x)
    order = np.argsort(r)
    return r[order], E[order], dE[order]


def main():
    if not os.path.isdir(ANC):
        print(f"SKIP: ancillary data not present at {ANC} (external, public: arXiv 2409.20168v1 /anc)")
        return
    rng = np.random.default_rng(52)
    agg_Req, report = [], []
    # paper's own widths for B1 (set S0 = NP per figure 6)
    pw = parse_agr(os.path.join(ANC, PAPER_W))[0]
    for dist, fn in FILES.items():
        wEs, Reqs, ReqCs = [], [], []
        for s in parse_agr(os.path.join(ANC, fn)):
            r, E, dE = fold(s)
            r, E, dE = truncate(r, E, dE)
            wE, Req = widths(r, E)
            _, ReqC = widths(r, np.clip(E, 0, None))
            if np.isnan(wE): continue
            wEs.append(wE); Reqs.append(Req); ReqCs.append(ReqC)
            draws = [widths(r, E + rng.normal(0, dE))[1] for _ in range(200)]
            agg_Req.append((Req, np.nanstd(draws)))
        mwE, mReq, mReqC = np.median(wEs), np.median(Reqs), np.median(ReqCs)
        near = pw[np.argmin(np.abs(pw[:, 0] - dist))]
        ok = abs(mwE / near[1] - 1) < 0.10
        report.append((dist, ok, mReq))
        print(f"d={dist} fm ({len(wEs)} setups): median w_E={mwE:.3f} vs paper's {near[1]:.3f} "
              f"({(mwE/near[1]-1)*100:+.1f}%) [{'B1 PASS' if ok else 'B1 FAIL - VOID'}] | "
              f"R_eq={mReq:.3f} fm (clip-variant {mReqC:.3f})")
    bearing = [x for x in report if x[1]]
    assert bearing and any(d == 0.7 for d, _, _ in bearing), \
        "no verdict-bearing distance (B1 nowhere satisfied): adjudication VOID"
    print(f"\nRESOLUTION (bars file): verdict-bearing distances = "
          f"{[d for d, _, _ in bearing]} (B1-validated); others exploratory.")
    R = float(np.median([q for _, _, q in bearing]))
    spread = float(np.ptp([q for _, _, q in report]))
    mc = float(np.median([e for _, e in agg_Req]))
    dev = R / R_PRED - 1
    print(f"\nB2 THE ADJUDICATION on real lattice points: R_eq = {R:.3f} fm "
          f"(all-distance exploratory range {spread:.3f}, MC err {mc:.3f})")
    print(f"   vs R_pred = {R_PRED} fm: {dev*100:+.1f}% -> "
          f"{'SUPPORTS' if abs(dev) < 0.15 else f'TENSION ({dev*100:+.0f}%)'}")
    print(f"   vs ELEC-051 reconstruction {R_51} fm: {(R/R_51-1)*100:+.1f}% "
          f"({'reconstruction CONFIRMED' if abs(R/R_51-1) < 0.10 else 'reconstruction OVERTURNED'})")
    n = 3 * np.pi * (R * 1e-15 / 1e-16) ** 2
    print(f"B3 propagation: n = {n:.0f}, T0 = {T_TUBE/n:.0f} J/m, "
          f"Sigma_eq = {T_TUBE/(np.pi*(R*1e-15)**2):.2e} J/m^3")
    print("B4 limits: 1D midplane cut + azimuthal symmetry (as the paper itself uses);")
    print("   negative-tail noise bounded by the pre-registered clip variant; per-distance")
    print("   values shown above unaveraged.")
    print("PASS: the named zero-cost decider executed on the actual public data.")


if __name__ == "__main__":
    main()
