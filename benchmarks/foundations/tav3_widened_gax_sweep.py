"""COMMISSION TAV3 -- the widened G-AX sweep (two-number decider).

Executed under analysis/TAV3_widened_gax_bars_LOCKED.md. Instrument
inherited VERBATIM from tav2_bundle_contact.py: contact form
Ac/(1 + (r/sigma)^4), Ac = 1, sigma = 0.12; hex-spiral bundles;
G-AX facing cross sections at end-plane gap = internal gap;
pitch = sigma + gap. Sweep, settling criteria, and verdict corners
fixed at lock. No free numbers.
"""
import numpy as np

SIG = 0.12
AC = 1.0
G_HEX = 0.050 * SIG
G_FC = 0.799 * SIG
PITCH = lambda g: SIG + g  # centerline pitch = 2 r_s + gap, r_s = sigma/2

NS = [7, 19, 37, 61, 91, 127, 169, 217, 271, 331, 397, 469, 547]
PIN = (63.0, 73.4)
WINDOWS = {"(kappa50,f_c)": (5, 9), "(kappa50,hex)/(kappa250,f_c)": (14, 27),
           "(kappa250,hex)": (40, 81), "tube census": (47, 198)}


def f(r):
    return AC / (1.0 + (r / SIG) ** 4)


def hex_bundle(n, pitch):
    """First n sites of a centered hex spiral, scaled by pitch
    (identical to TAV2's construction)."""
    pts = [(0.0, 0.0)]
    ring = 1
    while len(pts) < n:
        for k in range(6 * ring):
            side, step = divmod(k, ring)
            ang0 = np.pi / 3 * side
            ang1 = np.pi / 3 * (side + 1)
            p0 = ring * np.array([np.cos(ang0), np.sin(ang0)])
            p1 = ring * np.array([np.cos(ang1), np.sin(ang1)])
            pts.append(tuple(p0 + (p1 - p0) * step / ring))
            if len(pts) == n:
                break
        ring += 1
    return np.array(pts[:n]) * pitch


def e_ax(n, gap):
    """Axial contact energy: facing cross sections at end-plane gap
    (end-to-end nearest distance = PITCH(gap) for aligned pairs)."""
    b = hex_bundle(n, PITCH(gap))
    z = PITCH(gap)
    d = np.sqrt(((b[:, None, :] - b[None, :, :]) ** 2).sum(-1) + z * z)
    return f(d).sum()


def e1(gap):
    return f(PITCH(gap))


def local_exponents(ns, E):
    """dlnE/dlnn on consecutive triples (central OLS slope)."""
    x, y = np.log(ns), np.log(E)
    return np.array([np.polyfit(x[i:i + 3], y[i:i + 3], 1)[0]
                     for i in range(len(ns) - 2)])


def run(name, gap):
    ns = np.array(NS, float)
    E = np.array([e_ax(n, gap) for n in NS])
    meff = E / e1(gap)
    r = meff / ns

    # M3: exponent settling
    lp = local_exponents(ns, E)
    last3 = lp[-3:]
    m3_triples = last3.max() - last3.min() <= 0.05
    x, y = np.log(ns), np.log(E)
    h = len(NS) // 2  # top half = upper half of the widened sweep
    top_x, top_y = x[h:], y[h:]
    th = len(top_x) // 2
    plo = np.polyfit(top_x[:th + 1], top_y[:th + 1], 1)[0]
    phi = np.polyfit(top_x[th:], top_y[th:], 1)[0]
    m3_half = abs(plo - phi) <= 0.10
    m3 = m3_triples and m3_half
    p_inf = last3.mean()

    # M4: multiplicity settling
    r3 = r[-3:]
    m4 = (r3.max() - r3.min()) / r3.mean() <= 0.10
    r_inf = r3.mean()

    print(f"\n== G-AX / {name} (gap = {gap/SIG:.3f} sigma) ==")
    for n, m, rr in zip(NS, meff, r):
        print(f"  n = {n:3d}: m_eff = {m:10.3f}   m_eff/n = {rr:.4f}")
    print(f"  local exponents: {np.round(lp, 4)}")
    print(f"  M3 settled = {m3} (last3 spread {last3.max()-last3.min():.4f}"
          f" <= 0.05: {m3_triples}; top-half halves {plo:.4f}/{phi:.4f}"
          f" within 0.10: {m3_half}); p_inf = {p_inf:.4f}")
    print(f"  M4 settled = {m4} (last3 rel spread"
          f" {(r3.max()-r3.min())/r3.mean():.4f} <= 0.10); r_inf = {r_inf:.4f}")

    return dict(ns=ns, meff=meff, p_inf=p_inf, r_inf=r_inf, m3=m3, m4=m4)


def corner(res):
    if not (res["m3"] and res["m4"]):
        return "CORNER 4: UNSTABLE-PERSISTENT (Failed-and-kept)"
    fs = 0.85 <= res["p_inf"] <= 1.15
    cur = 0.5 <= res["r_inf"] <= 1.5
    if fs and cur:
        sel = [int(n) for n, m in zip(res["ns"], res["meff"])
               if PIN[0] <= m <= PIN[1]]
        lo = np.interp(PIN[0], res["meff"], res["ns"])
        hi = np.interp(PIN[1], res["meff"], res["ns"])
        return (f"CORNER 1: CHAIN A SURVIVES; n_b readout sampled {sel}, "
                f"interpolated [{lo:.1f}, {hi:.1f}]")
    if fs:
        lo, hi = PIN[0] / res["r_inf"], PIN[1] / res["r_inf"]
        hits = [w for w, (a, b) in WINDOWS.items() if not (hi < a or lo > b)]
        hitstr = (str(hits) if hits else
                  "NONE -- tension CONFIRMED AT SETTLED LEVEL, "
                  "adjudication per FND-080 return clause")
        return (f"CORNER 2: FULL-SECTION, WRONG CURRENCY; measured inversion "
                f"n = [{lo:.1f}, {hi:.1f}]; window hits: {hitstr}")
    return ("CORNER 3: NOT FULL-SECTION (p_inf outside band); geometry "
            "premise CONVICTED at engine level; adjudication")


def main():
    print("TAV3 -- widened G-AX sweep (locked bars, two-number decider)")
    for name, gap in (("hex", G_HEX), ("f_c", G_FC)):
        res = run(name, gap)
        v = corner(res)
        print(f"  VERDICT ({name}): {v}")
        if name == "hex":
            print("  (hex is the Chain A confrontation cell per bars)")


if __name__ == "__main__":
    main()
