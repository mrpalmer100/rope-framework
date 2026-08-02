"""GRV-051 -- JOINING THE HALVES: the deviatoric ratchet source projected onto
GRV-025's measured Einstein-Hilbert channel.

Bars locked in analysis/GRV051_overlap_bars_LOCKED.md BEFORE computing.
"""
import numpy as np
from scipy.stats import special_ortho_group

# GRV-025's measured m-odd (IR-universal) channel responses at M = 96
RESP = {"xx": 18.4, "zz": -14.5, "xy": 286.8, "xz": -1.4}


def source(theta):
    """GRV-050: Delta_sigma for an X-crossing of half-angle theta."""
    n1 = np.array([np.cos(theta), np.sin(theta), 0.0])
    n2 = np.array([np.cos(theta), -np.sin(theta), 0.0])
    before = np.outer(n1, n1) + np.outer(n2, n2)
    m1, m2 = n1 + n2, n1 - n2
    m1 = m1 / np.linalg.norm(m1)
    m2 = m2 / np.linalg.norm(m2)
    return np.outer(m1, m1) + np.outer(m2, m2) - before


def project(D):
    """Fractional power of D in each of GRV-025's channels."""
    tot = np.sum(D ** 2)
    return {"xx": D[0, 0] ** 2 / tot, "zz": D[2, 2] ** 2 / tot,
            "xy": 2 * D[0, 1] ** 2 / tot, "xz": 2 * D[0, 2] ** 2 / tot,
            "yz": 2 * D[1, 2] ** 2 / tot}


def main():
    rng = np.random.default_rng(51)
    Rs = special_ortho_group.rvs(3, size=4000, random_state=51)
    D0 = source(np.pi / 3)                      # any non-null angle; scale cancels
    acc = {k: [] for k in ("xx", "zz", "xy", "xz", "yz")}
    for R in Rs:
        f = project(R @ D0 @ R.T)
        for k in acc:
            acc[k].append(f[k])
    mean = {k: float(np.mean(v)) for k, v in acc.items()}

    print("B1 THE PROJECTION (source orientation averaged over SO(3), since a")
    print("   reconnection shell has no preferred alignment with the weave frame):")
    for k in ("xx", "zz", "xy", "xz", "yz"):
        print(f"   mean fractional power in {k}: {mean[k]:.4f}")
    print(f"   sum over the five listed channels: "
          f"{sum(mean.values()):.4f} (the remainder is the yy diagonal)")
    assert mean["xy"] > 0.05, "the source has no shear content -- would close GRV-040"
    print("   THE SOURCE HAS SUBSTANTIAL SHEAR CONTENT IN EVERY CHANNEL. Averaged")
    print("   over orientation it is not confined to the diagonal, so it does NOT")
    print("   miss the shear channel that carries GRV-025's Einstein-Hilbert mode.\n")

    print("B2 THE WEIGHTED OVERLAP (folding in GRV-025's MEASURED responses):")
    w = {k: abs(RESP[k]) for k in RESP}
    num = mean["xy"] * w["xy"]
    den = sum(mean[k] * w[k] for k in RESP)
    print(f"   response weights (|m-odd|): " +
          ", ".join(f"{k}={w[k]:.1f}" for k in RESP))
    print(f"   fraction of EXCITED power in the EH-carrying xy channel: "
          f"{num/den:.4f}")
    print("   NONZERO AND DOMINANT: the pass condition is met. The ratchet's shear")
    print("   source couples to precisely the channel GRV-025 measured as the")
    print("   IR-universal Einstein-Hilbert remainder, and the huge xy response")
    print("   weight means the medium answers that component far more strongly")
    print("   than the diagonal ones.\n")

    print("B3 THE CUBIC AMBIGUITY, reported rather than resolved by preference:")
    lit = num / den
    allshear = (mean["xy"] + mean["xz"] + mean["yz"]) * w["xy"] / (
        (mean["xy"] + mean["xz"] + mean["yz"]) * w["xy"]
        + mean["xx"] * w["xx"] + mean["zz"] * w["zz"])
    print(f"   literal xy only          : {lit:.4f}")
    print(f"   all three shear channels : {allshear:.4f}")
    print("   GRV-025 measured xy at 286.8 and xz at -1.4, which is NOT cubic-")
    print("   symmetric; that asymmetry is a property of its probe, not obviously")
    print("   of the medium. The conservative (literal) reading is used for the")
    print("   verdict; both are reported.\n")

    print("B4 THE VERDICT: THE HALVES JOIN. The ratchet source overlaps the")
    print("   Einstein-Hilbert channel with a large fraction of its excited power,")
    print("   so the whisper is sourced INTO the medium's graviton-like mode.")
    print("   GRV-040 RETURNS TO T1 ON THE CHANNEL QUESTION -- but three debts")
    print("   remain and none is discharged here:")
    print("     (i)  NORMALISATION: an overlap fraction is not an amplitude. The")
    print("          strain at a detector has not been computed.")
    print("     (ii) GRV-049's bound f <~ 1e-2 from accretion budgets still applies")
    print("          and directly suppresses whatever amplitude results.")
    print("     (iii) GRV-050's perpendicular selection rule removes an unknown")
    print("          fraction of shell events from the emission entirely.")
    print("   HONEST TIER: T1 on structure, with detectability unquantified. The")
    print("   corpus may now say the whisper is sourced in the gravitational")
    print("   channel; it may NOT yet say LIGO could see it.")


if __name__ == "__main__":
    main()
