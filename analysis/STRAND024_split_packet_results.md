# FND-STRAND-024 — the split packet: results

Bars: analysis/STRAND024_split_packet_bars_LOCKED.md. Data archived:
analysis/STRAND024_split_packet_data.json.

## Calibration: the intensive pricing worked (first outing)

Full-packet response at sigma = 4: P(click) = 0.000 / 0.125 / 0.625 /
1.000 at V = 0.9 / 1.2 / 1.6 / 2.1 — a sharp threshold sigmoid, bracketed
inside the priced grid. V50 = 1.50. The device is certified a threshold
detector, which is B3's clause (i) by construction.

## THE HEADLINE, direct and well-powered: a split quantum clicks NOTHING

- Half-packet, single lobe (V_h = V50/sqrt(2), exactly half the energy):
  0/48 clicks.
- The one-quantum split itself (both half-lobes delivered simultaneously
  to sites 24 and 72): 0/64 clicks in EITHER region.

The response nonlinearity is so sharp that half a quantum's energy
density sits below the sigmoid's foot entirely. Two consequences,
registered at full volume:

1. ONE-CLICK EXCLUSIVITY IS TRIVIALLY ENFORCED at the classical level:
   a split single quantum cannot double-click because it cannot click.
   Sub-additivity kills the double before any drainage or scarcity
   mechanism is even needed.
2. THE MEASURED CLASSICALITY LIMIT — the session's real product: real
   single photons behind a beamsplitter click ONE arm at ~50% each.
   This classical engine's split packet clicks NEITHER arm. The
   framework's classical detector story therefore reproduces the
   one-click rule but FAILS to reproduce the quantum 50/50 single-arm
   statistics. The place where genuine quantumness must enter the
   measurement story is now pinned by a measurement, not an argument:
   it is the reassembly of a split quantum's full energy at ONE
   absorption site — the funneling step — which no classical local
   dynamics in this engine performs.

## The near-threshold interaction ensemble (deviation logged, underpowered)

The committed adjustment rule failed at the sigmoid's foot (linear
extrapolation to a nonsense V = 4.86); the logged deviation adopted the
fullcal-curve interpolation V' = 1.38. Executed: S = 128 split runs at
V' per lobe. Marginals ran 0.156 / 0.141 — well BELOW the 0.35 target
(the sigmoid's steepness defeated the interpolation too), so the
pricing note's own condition for an adequate branch call was not met.
Measured: rho = 0.71, approximate 95% CI [0.0, 2.4] — CONSISTENT WITH
INDEPENDENCE, registered as measured, NO branch verdict (underpowered
as executed, said plainly). Symmetry sanity: A = 20 vs B = 18, clean.

## B3 alibi: letter fails, purpose passes (stated, not smoothed)

Two full packets: marginals 0.375 / 0.281 (again below the 0.5 the
letter priced), doubles 6/64 = 0.094 vs the 0.15 letter — LETTER FAIL.
Independence product from the REALIZED marginals: 0.105; observed
0.094 — the instrument sees doubles at the rate independence predicts.
PURPOSE PASS. The letter was mispriced on marginals that did not
materialize; both facts on the record.

## Lessons (sixth entry, and a rule upgrade)

At sharp thresholds, interpolated operating points systematically
undershoot: (a) never linearly interpolate at a sigmoid's foot (the
adjustment-rule defect); (b) VERIFY the realized marginal with a small
gate ensemble BEFORE committing the main ensemble (a two-stage gate
becomes the standing rule for response-curve operating points).

## What this changes upstream

- The exclusivity question is CLOSED at the classical level (trivially,
  by threshold nonlinearity) and simultaneously converted into the
  corpus's sharpest known limit: the FUNNELING STEP (split-quantum
  reassembly at one site) is not classical in this engine. The honest
  registry language for the double-slit account: wave delivers the
  odds; bath delivers the dot; and the ODDS-TO-DOT conversion for
  SPLIT quanta requires physics beyond the registered classical
  detector — named, bounded, measured.
- The predictions paper should NOT gain a new prediction from tonight;
  it should gain the LIMIT statement (a framework that documents where
  its mechanism ends is worth more than one that extrapolates past it).
  Deferred to the next docs pass, named here.
- Which-path, delayed choice, and the eraser now have a sharper
  entrance: they live exactly on the far side of the funneling step.

## Ledger

- Calibration bracketed (intensive pricing vindicated); headline finding
  well-powered (0/112 clicks across half-packet and split ensembles);
  interaction statistic consistent-with-independence, underpowered, no
  branch verdict; alibi letter-fail/purpose-pass logged; adjustment
  deviation logged; sixth lesson + two-stage-gate rule adopted.
- Status: Modeled. Absolute scale untouched (FND-MATTER-003).
