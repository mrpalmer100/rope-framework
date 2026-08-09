# EM-RECON-018 — the standoff refinement: the survival band narrows 41-fold, and the tight tail was never physically accessible

Date: 2026-08-09. Commission: EM-RECON-017's settler #2.
Bars: `analysis/EMRECON018_standoff_bars_LOCKED.md` (locked first).
Benchmark: `benchmarks/em/emrecon018_standoff_refinement.py`.

## The derivation

Coverage counting from the registered percolation fraction: three
families of width-w strands give 3·πw²/(4a²) = f_c, so w/a = 0.362 at
f_c = 0.309 (sensitivity across the registered window: 0.18–0.38). The
contact range σ0 is the interpenetration scale — surfaces interact at
center distance ~ one width; the contact form's knee IS the touching
condition.

The admissible standoff readings, enumerated per bar 2 and both carried:
reading A (in-family touching neighbors, d0 = σ0) gives d0/σ0 = 1.00;
reading B (cross-family half-spacing offset, d0 = a/2) gives 1.38.
Reusing EM-RECON-017's C(d0/σ0) unchanged: C = 5.06 and 4.37.

## The refined band

    survival threshold on E_x/(T0·a): [0.40, 0.46]   (was [0.40, 3.00])

**A 41-fold narrowing** — and its meaning is structural: the coverage
threshold FORCES the standoff into the contact form's knee region, so the
tight-standoff tail of the old band (thresholds up to 3.0) was never
physically accessible. The loose edge the old band happened to start at
is where the physics actually lives.

## The confrontation (sealed until the band was fixed)

Survival in multiplicity terms at L1 = 1: **m_b < 63–73 strand pairs per
bundle bond** (the L1 factor-3 band widens this to ~20–200).

| multiplicity model | ratio | verdict vs [0.40, 0.46] |
|---|---|---|
| single pair | 29.0 | SURVIVES |
| surface line ~22 | 1.32 | SURVIVES |
| contact patch ~63 | 0.46 | SURVIVES (at the edge) |
| full section ~498 | 0.06 | FAILS |

The refinement converts the question. Before: "does the ratio clear a
band a factor of 8 wide?" — undecidable at any multiplicity. Now: "is the
bundle contact multiplicity below ~60–70?" — a sharp geometric question
about how two fiber bundles touch. Every physically-motivated contact
geometry (point, line, patch) survives; only full-cross-section contact
fails, and full-section contact is geometrically implausible for
touching cylinders. The estimates remain not-adopted, but the survival
region now contains all of them except the implausible one.

## Consequences

- EM-RECON-017's survival condition is superseded to the refined band;
  face annotation placed.
- FND-029's bounded reduction sharpens: the width question w must now hit
  a target an order of magnitude smaller, and the both-census tripwire
  inherits the refined band.
- Honest edge carried: the coverage-counting step treats the three
  families' disks as non-overlapping at threshold (leading order in f_c);
  and reading B's a/2 cross-family offset is a routing idealization. Both
  named; neither moves the band's order.

## Not claimed

m_b; w; survival (the estimates are displayed, not adopted); any new
parameter. Spend remains ONE.
