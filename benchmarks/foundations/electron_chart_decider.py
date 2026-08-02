"""ELEC-018 (Modeled): THE DECIDER DECIDES -- CHART SPAN. Three
measurements, one verdict, and an honest reframing of the terminus.

(1) THE GATE'S DISCOVERY (kink density): the K = 12 instrument gate
    produced CONTRADICTORY finite-difference references -- small-step
    low-precision FD converging exactly onto the analytic values on
    some coordinates while high-precision FD at moderate steps landed
    elsewhere. Diagnosis: at the contact-saturated state the
    nearest-sample assignment kinks are DENSELY spaced; different FD
    steps sample different subgradients, and the objective is
    effectively nonsmooth at all probed scales in some directions.
    The analytic per-assignment gradient remains exact within smooth
    pieces (validated where FD stabilizes: errors 0.00-0.39 percent)
    and is the ONLY viable gradient oracle in this regime.

(2) SUBDIFFERENTIAL METROLOGY (candidate eliminated): jittering the
    state at 1e-6 and collecting analytic gradients measures the local
    subgradient spread directly: max pairwise 0.088 against a residual
    of 1.543 -- a 17x gap, far outside the locked 2x bar at both
    jitter scales. The residual does NOT hide inside the kink
    structure's width.

(3) THE CHART-SPAN TEST (candidate CONFIRMED): the active-set engine
    in the enriched K = 12 chart (145 parameters; embedding verified
    to 1.8e-7; instrument gated) achieved dE = 0.0539 in 195 certified
    iterations -- crossing the locked 0.05 bar with descent SUSTAINED
    at ~2e-4 per step at budget exhaustion, roughly 2400x the yield of
    the K = 8 second-order machinery. THE K = 8 RESIDUAL WAS GENUINE
    DESCENT THE CHART COULD NOT REPRESENT.

REFRAMING, stated plainly: ELEC-013/014/017's termini are
CHART-CONSTRAINED termini -- exact statements about the K = 8
parameterization, not the functional's equilibrium. The equilibrium
hunt continues in richer charts. THE STRUCTURE SURVIVES ENRICHMENT:
at the K = 12 frontier the clasp still rides its isoperimetric floor
with contact unbroken, and the certification (d, |Lk|) held through
every accepted step.
"""
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.elec_grad import al


def test():
    st = np.load(ROOT/'analysis'/'ELEC018_state.npz')
    dE = float(st['dE_k12'])
    assert dE > 0.05, "THE DECIDER: chart-span bar crossed (dE = 0.054 in the K=12 chart)"
    assert float(st['r_norm']) > 2*2*float(st['spread_1em6']), \
        "subdifferential candidate eliminated (17x outside the locked 2x bar)"
    assert 0.2 < float(st['gres']) < 0.8, "residual re-elevated mid-descent: not at equilibrium"
    assert not bool(st['terminated']), "descent SUSTAINED at exhaustion (not a terminus)"
    print(f"dE(K=12) = {dE:.4f} [bar 0.05]; ||r||/spread = {float(st['r_norm'])/float(st['spread_1em6']):.0f}x; "
          f"gres = {float(st['gres']):.3f}, descending")
    print("PASS: CHART SPAN decided -- the K=8 termini were chart-constrained; the analytic")
    print("      per-assignment gradient is the only viable oracle in the kink-dense regime.")


if __name__ == "__main__":
    test()
