"""ELEC-043 (Modeled): THE COLLECTIVE NUMBER, DERIVED -- causality gives
n_t ~ 1 where the framework needs 1e8. The escape route the sector has
leaned on for two claims does not survive its own physics.

THE DERIVATION. For a relativistic strand the transverse wave speed is
v = sqrt(T/mu) with mu = T/c^2, hence EXACTLY c -- no free parameter.
During a reconnection event of duration tau only strands within a
light-crossing radius c tau can participate, so n_t <= (c tau/w)^2.
Evaluating at every local timescale the object offers:
    core crossing   d_c/c : n_t = 1.05e-5
    object crossing R/c   : n_t = 2.62e-3
    whole length    L/c   : n_t = 0.155
    (the spacing timescale w/c returns exactly 1 by construction and
     is listed only to show the scale where a second strand is first
     reachable)
EVERY local timescale returns n_t of order one or less. A reconnection
is causally confined to a region smaller than the strand spacing, so
no strand but the two involved can take part.

THE INVERSION. Producing n_t = 2.95e8 requires a coherence radius
R_c = w sqrt(n_t) = 993 fm and an event duration 3.31e-21 s. Against
the object those are 3.36e5 times its size and 3.36e5 times its
light-crossing time. A process spanning three hundred thousand
electron-diameters is not a local topological change.

THE VERDICT. The collective number cannot be derived from local
causality at the magnitude the framework requires; causality gives ~1
and the framework needs 1e8, a gap of 3e8. What survives is one named
escape: a PRE-CORRELATED medium, in which the strands are already
coherent over 993 fm before any event occurs. That is not a
reconnection mechanism but a long-range-order hypothesis, and it
carries its own unpaid bill -- order across ~1.7e4 strand spacings in
each direction.

A FLAGGED COMPARISON, not leaned on: R_c lands within 2.6x of the
electron's reduced Compton wavelength. The ratio scales as s and is
therefore not an identity, only a consequence of the independently
chosen tension-matched scale. Registered under the corpus's standing
rule against promoting underived coincidences.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def test():
    s = np.load(ROOT/'analysis'/'ELEC043_state.npz')
    a = np.load(ROOT/'analysis'/'ELEC043_audit.npz')
    # B1: every local timescale gives n_t <= 1
    for k in ('n_causal_core', 'n_causal_obj', 'n_causal_L'):
        assert float(s[k]) < 1.0, f"{k}: causal n_t below unity"
    assert float(s['n_causal_core']) < 1e-4, "at the core timescale, n_t ~ 1e-5"
    # B2: the inversion
    assert float(s['ratio_size']) > 1e4, "required coherence 3.4e5 x the object's size"
    assert abs(float(s['ratio_size']) - float(s['ratio_time']))/float(s['ratio_size']) < 1e-6, \
        "size and time ratios coincide exactly (both are R_c/R): a consistency check"
    assert 5e-13 < float(s['Rc']) < 2e-12, "coherence radius ~993 fm"
    # B3: the gap
    gap = float(s['n_req'])/max(float(s['n_causal_L']), 1e-30)
    assert gap > 1e8, "the gap between derived and required is >= 1e8"
    # the flagged comparison is scale-dependent, hence not an identity
    assert bool(a['scale_dep']), "the Compton comparison scales as s: flagged, not claimed"
    assert 1.5 < float(a['ratio']) < 4.0, "R_c within 2.6x of the reduced Compton wavelength"
    print(f"causal n_t: core {float(s['n_causal_core']):.1e}, object {float(s['n_causal_obj']):.1e}, "
          f"length {float(s['n_causal_L']):.2f}; required {float(s['n_req']):.1e}; "
          f"R_c {float(s['Rc'])*1e15:.0f} fm = {float(s['ratio_size']):.1e}x the object")
    print("PASS: causality derives n_t ~ 1 against a requirement of 1e8 -- the collective")
    print("      escape fails on its own physics; only a pre-correlated medium survives.")


if __name__ == "__main__":
    test()
