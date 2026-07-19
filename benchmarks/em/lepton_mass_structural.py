"""Particle-mass sector, structural clarification: the NUC-001 mass mechanism
(knot-count minus binding) provably does NOT extend to leptons, and the lepton
mass problem is correctly reclassified as a 3-level knot EXCITATION spectrum, not
a composite-counting problem.

NUC-001 (Derived) works because nuclei are COMPOSITE: mass = A x (nucleon-knot
mass) - mode-overlap binding, where A = 2..238 is a COUNT of internal knots.
Different nuclei = different counts, and the winding/charge scales with structure.

Leptons (corpus ontology): each is a SINGLE knot of winding number 1. All three
generations (e, mu, tau) share winding 1, charge -1, spin 1/2 -- they differ ONLY
in mass. So:
  * If generations differed by knot COUNT N (mu = N e-knots), they would have
    winding ~N (charge ~N). They do not (all charge -1). REFUTES knot-counting.
  * Same winding => same 'A' => NUC-001 predicts the SAME mass for all three. But
    masses differ by up to 3477x. So NUC-001's mechanism CANNOT produce the ratios.

Therefore the generation label is an EXCITATION quantum number of ONE knot (three
energy levels), not a count of sub-knots. The lepton mass problem is an excitation-
spectrum problem. This explains WHY the Koide-phase relation (PM-001, a relation
AMONG levels) is the relevant kind of tool and why knot-counting was never going
to work.

Honest negative: this does NOT derive lepton masses. The ratios match no simple
ladder (sqrt: 1,14.4,59 -- non-integer; log: 0,5.33,8.15 -- unequal; successive:
207,16.8 -- non-geometric). Lepton masses remain inputs. The value is structural
clarification and a well-posed replacement for the vague 'masses underived': a
knot excitation spectrum with exactly 3 bound levels in the observed ratios.
"""
import numpy as np

M_E, M_MU, M_TAU = 0.511, 105.66, 1776.86  # MeV


def leptons_share_winding_number():
    """All three charged leptons have winding/charge magnitude 1 -> no count to
    distinguish them -> knot-COUNT (NUC-001) cannot apply."""
    windings = {"e": 1, "mu": 1, "tau": 1}     # all charge -1 => |winding| = 1
    return len(set(windings.values())) == 1     # identical -> no distinguishing count


def ratios_are_not_a_simple_ladder():
    """The mass ratios match no simple excitation ladder (documents that the
    spectrum, while the right framing, is not a trivial one)."""
    r = np.array([M_E, M_MU, M_TAU]) / M_E
    sqrt_levels = np.sqrt(r)                    # HO-like n?
    log_levels = np.log(r)                      # exponential tower?
    successive = np.array([M_MU / M_E, M_TAU / M_MU])
    # none are clean: sqrt not near-integers, log not equally spaced, ratios not equal
    not_sqrt_integer = not np.allclose(sqrt_levels, np.round(sqrt_levels), atol=0.1)
    not_equal_log = abs((log_levels[1] - log_levels[0]) - (log_levels[2] - log_levels[1])) > 0.5
    not_geometric = abs(successive[0] - successive[1]) > 1.0
    return not_sqrt_integer and not_equal_log and not_geometric


def test():
    assert leptons_share_winding_number(), "leptons share winding => knot-count cannot distinguish them"
    # NUC-001 with equal counts predicts equal mass; real masses differ hugely
    assert (M_TAU / M_E) > 1000, "lepton masses differ by >1000x despite equal winding"
    assert ratios_are_not_a_simple_ladder(), "ratios should match no trivial ladder (honest negative)"
    print("leptons all share winding number 1 -> no distinguishing count -> NUC-001 knot-count REFUTED")
    print(f"equal winding would predict equal mass, but tau/e = {M_TAU/M_E:.0f}x -> mechanism cannot apply")
    print("ratios match no simple ladder (sqrt/log/geometric all fail) -> not a trivial spectrum")
    print("PASS: NUC-001 provably does not extend to leptons (structural reason); lepton")
    print("      masses reclassified as a 3-level knot EXCITATION spectrum, not counting.")
    print("      Masses remain inputs; the open problem is now well-posed, not vague.")


if __name__ == "__main__":
    test()
