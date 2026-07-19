"""Attempt (negative result) to compute the lepton mass spectrum as a knot
excitation spectrum. The excitation FRAMING (PM-003) is correct, but the actual
spectrum does NOT fall out of the corpus's soliton/knot physics without tuning.
Lepton masses remain irreducible inputs. No spectrum was fitted.

Checked, all non-tuned mechanisms fail:
 * Natural soliton spectra are O(1)-spaced (real baryons: nucleon->Delta = 1.3x),
   not the 207x and 3477x the lepton ratios require.
 * Energy ~ winding^2 cannot distinguish generations (all leptons winding 1, PM-003).
 * Tunneling splitting gives near-degeneracy (wrong direction).
 * Simple ladders fail: sqrt(m/m_e) = 1,14.4,59 (non-integer); log = 0,5.3,8.2
   (unequal); successive ratios 207,16.8 (non-geometric).
 * The Koide relation (K=0.66666 vs 2/3) matches to ~0.001% but only CONSTRAINS
   (one equation, two masses free) -- it does not generate the spectrum; already
   registered honestly as PM-001 (Conjecture).

Conclusion: lepton masses are irreducible inputs, on the same footing as the mesh
scale a (FND-MATTER-005) and the super-quadratic coefficient (EM-RECON-008).
"""
import numpy as np

M = np.array([0.511, 105.66, 1776.86])  # e, mu, tau (MeV)


def natural_soliton_spacing_is_order_one():
    """Real topological-soliton excited states are within ~a few x of the ground
    state (nucleon 939 -> Delta 1232 = 1.31x), not 200-3000x."""
    nucleon, delta = 939.0, 1232.0
    return (delta / nucleon) < 2.0


def lepton_ratios_are_not_order_one():
    """Lepton ratios span 3477x -- incompatible with a natural soliton tower."""
    return (M[2] / M[0]) > 1000.0


def no_simple_ladder_matches():
    r = M / M[0]
    sqrt_lvl = np.sqrt(r)
    log_lvl = np.log(r)
    not_int = not np.allclose(sqrt_lvl, np.round(sqrt_lvl), atol=0.1)
    not_equal = abs((log_lvl[1] - log_lvl[0]) - (log_lvl[2] - log_lvl[1])) > 0.5
    not_geom = abs((M[1] / M[0]) - (M[2] / M[1])) > 1.0
    return not_int and not_equal and not_geom


def koide_constrains_but_does_not_generate():
    """Koide K ~ 2/3 to ~0.001% -- but it is one constraint among three masses."""
    me, mmu, mtau = M
    K = (me + mmu + mtau) / (np.sqrt(me) + np.sqrt(mmu) + np.sqrt(mtau)) ** 2
    return abs(K - 2 / 3) < 1e-3          # remarkable match, but only a constraint


def test():
    assert natural_soliton_spacing_is_order_one(), "real soliton spectra are O(1)-spaced"
    assert lepton_ratios_are_not_order_one(), "lepton ratios span >1000x"
    assert no_simple_ladder_matches(), "no simple excitation ladder matches"
    assert koide_constrains_but_does_not_generate(), "Koide matches but only constrains"
    print("natural soliton spacing O(1) (nucleon->Delta 1.3x); lepton ratios span 3477x -> incompatible")
    print("no simple ladder matches; winding^2 fails (all winding 1); Koide constrains not generates")
    print("PASS (negative result): the knot excitation spectrum does NOT reproduce lepton")
    print("      masses without tuning. Masses remain irreducible inputs; no spectrum fitted.")


if __name__ == "__main__":
    test()
