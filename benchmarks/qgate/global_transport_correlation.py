"""QGATE-017: empirical global-transport / Born-relaxation correlation.

Bars were locked in analysis/QGATE017_global_transport_bars_LOCKED.md before
this benchmark was executed.
"""
from __future__ import annotations

from dataclasses import dataclass
import csv
from pathlib import Path
import sys
import numpy as np

try:
    from benchmarks.qgate.born_relaxation_locked import _sample_sin2, _reflect_unit, _velocity
    from benchmarks.qgate.born_relaxation_mode_count import MODE_COUNTS, SEEDS, _mode_pool, _spearman
except ModuleNotFoundError:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from benchmarks.qgate.born_relaxation_locked import _sample_sin2, _reflect_unit, _velocity
    from benchmarks.qgate.born_relaxation_mode_count import MODE_COUNTS, SEEDS, _mode_pool, _spearman


@dataclass(frozen=True)
class TransportRow:
    seed: int
    modes: int
    transition_entropy: float
    cross_cell_fraction: float
    spectral_gap: float
    H_drop: float
    L1_drop: float


def _midpoint_step(x, y, t, dt, modes, coeff, omega):
    vx, vy = _velocity(x, y, t, modes, coeff, omega)
    xm = _reflect_unit(x + 0.5 * dt * vx)
    ym = _reflect_unit(y + 0.5 * dt * vy)
    vxm, vym = _velocity(xm, ym, t + 0.5 * dt, modes, coeff, omega)
    return _reflect_unit(x + dt * vxm), _reflect_unit(y + dt * vym)


def _cells(x: np.ndarray, y: np.ndarray, bins: int) -> np.ndarray:
    ix = np.minimum((x * bins).astype(int), bins - 1)
    iy = np.minimum((y * bins).astype(int), bins - 1)
    return ix * bins + iy


def _largest_recurrent_component(counts: np.ndarray) -> np.ndarray:
    """Return indices in largest undirected-connected active component.

    The empirical operator is time-aggregated and finite. Using the largest
    connected active component avoids assigning a fake gap to unvisited cells.
    """
    active = np.flatnonzero(counts.sum(axis=1) + counts.sum(axis=0) > 0)
    if len(active) <= 1:
        return active
    adj = (counts[np.ix_(active, active)] + counts[np.ix_(active, active)].T) > 0
    seen = np.zeros(len(active), dtype=bool)
    comps = []
    for s in range(len(active)):
        if seen[s]:
            continue
        stack = [s]; seen[s] = True; comp = []
        while stack:
            i = stack.pop(); comp.append(i)
            for j in np.flatnonzero(adj[i]):
                if not seen[j]:
                    seen[j] = True; stack.append(int(j))
        comps.append(comp)
    largest = max(comps, key=len)
    return active[np.asarray(largest, dtype=int)]


def _metrics(counts: np.ndarray) -> tuple[float, float, float]:
    total = float(counts.sum())
    if total <= 0:
        return 0.0, 0.0, 0.0
    rows = counts.sum(axis=1)
    active_rows = rows > 0
    p = np.zeros_like(counts, dtype=float)
    p[active_rows] = counts[active_rows] / rows[active_rows, None]
    with np.errstate(divide="ignore", invalid="ignore"):
        logs = np.where(p > 0, np.log(p), 0.0)
    row_entropy = -np.sum(p * logs, axis=1)
    n_active = max(2, int(np.sum(active_rows)))
    entropy = float(np.sum(rows * row_entropy) / total / np.log(n_active))
    cross = float((total - np.trace(counts)) / total)

    comp = _largest_recurrent_component(counts)
    if len(comp) <= 1:
        gap = 0.0
    else:
        sub = counts[np.ix_(comp, comp)].astype(float)
        r = sub.sum(axis=1)
        keep = r > 0
        sub = sub[np.ix_(keep, keep)]
        r = sub.sum(axis=1)
        if len(sub) <= 1:
            gap = 0.0
        else:
            P = sub / r[:, None]
            vals = np.linalg.eigvals(P)
            mags = np.sort(np.abs(vals))[::-1]
            gap = float(max(0.0, 1.0 - mags[1])) if len(mags) > 1 else 0.0
    return entropy, cross, gap


def _load_relaxation(path: Path):
    out = {}
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out[(int(row["seed"]), int(row["modes"]))] = (
                float(row["H_drop"]), float(row["L1_drop"]))
    return out


def _transport(seed: int, count: int, trajectories: int = 1000,
               steps: int = 1200, total_time: float = 4.0,
               sample_every: int = 20, bins: int = 10):
    pool = _mode_pool()
    rngc = np.random.default_rng(seed)
    coeff_pool = rngc.normal(size=64) + 1j * rngc.normal(size=64)
    modes = pool[:count]
    coeff = coeff_pool[:count].copy(); coeff /= np.linalg.norm(coeff)
    omega = 0.5 * np.pi**2 * (modes[:, 0]**2 + modes[:, 1]**2)
    rng = np.random.default_rng(seed + 200_003)
    x = _sample_sin2(rng, trajectories, mode=1)
    y = _sample_sin2(rng, trajectories, mode=1)
    prev = _cells(x, y, bins)
    counts = np.zeros((bins*bins, bins*bins), dtype=np.int64)
    dt = total_time / steps
    t = 0.0
    for step in range(1, steps + 1):
        x, y = _midpoint_step(x, y, t, dt, modes, coeff, omega)
        t += dt
        if step % sample_every == 0:
            cur = _cells(x, y, bins)
            np.add.at(counts, (prev, cur), 1)
            prev = cur
    return _metrics(counts)


def run():
    root = Path(__file__).resolve().parents[2]
    relax = _load_relaxation(root / "analysis" / "QGATE015_mode_count_results.csv")
    rows = []
    for seed in SEEDS:
        for m in MODE_COUNTS:
            ent, cross, gap = _transport(seed, m)
            h, l1 = relax[(seed, m)]
            rows.append(TransportRow(seed, m, ent, cross, gap, h, l1))
            print(f"seed={seed:2d} M={m:2d} entropy={ent:.6f} cross={cross:.6f} "
                  f"gap={gap:.6f} Hdrop={h:.6f}", flush=True)
    return rows


def _write(rows, path):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["seed","modes","transition_entropy","cross_cell_fraction","spectral_gap","H_drop","L1_drop"])
        for r in rows:
            w.writerow([r.seed,r.modes,r.transition_entropy,r.cross_cell_fraction,r.spectral_gap,r.H_drop,r.L1_drop])


def test():
    rows = run()
    root = Path(__file__).resolve().parents[2]
    out = root / "analysis" / "QGATE017_global_transport_results.csv"
    _write(rows, out)
    med = {}
    for m in MODE_COUNTS:
        rs = [r for r in rows if r.modes == m]
        med[m] = tuple(float(np.median([getattr(r, k) for r in rs]))
                       for k in ("transition_entropy","cross_cell_fraction","spectral_gap"))
    e = np.array([r.transition_entropy for r in rows])
    c = np.array([r.cross_cell_fraction for r in rows])
    g = np.array([r.spectral_gap for r in rows])
    h = np.array([r.H_drop for r in rows]); l1 = np.array([r.L1_drop for r in rows])
    rho_e_h = _spearman(e,h); rho_e_l1 = _spearman(e,l1)
    rho_c_h = _spearman(c,h); rho_g_h = _spearman(g,h)
    multimode = sum((med[m][0] > med[1][0]+0.05 and med[m][1] > med[1][1]+0.05) for m in MODE_COUNTS[1:])
    print("\nMedians by mode count:")
    for m in MODE_COUNTS:
        print(f"M={m:2d}: entropy={med[m][0]:.6f} cross={med[m][1]:.6f} gap={med[m][2]:.6f}")
    print(f"rho(entropy,H)={rho_e_h:.6f}")
    print(f"rho(entropy,L1)={rho_e_l1:.6f}")
    print(f"rho(cross,H)={rho_c_h:.6f}")
    print(f"rho(gap,H)={rho_g_h:.6f}")
    print(f"multimode transport families={multimode}/6")

    b1 = med[1][0] < .02 and med[1][1] < .02 and med[1][2] < .02
    b2 = multimode >= 5
    b3 = rho_e_h > .30
    b4 = rho_e_l1 > .30
    b5 = max(abs(rho_e_h), abs(rho_c_h), abs(rho_g_h)) > .573
    b6 = rho_g_h > 0
    outcome = [b1,b2,b3,b4,b5,b6]
    print("bars:", outcome)
    # Freeze the observed outcome after first execution; all outcomes are kept.
    assert all(outcome), "One or more preregistered bars failed; inspect and register the kept outcome."
    print("PASS: all locked global-transport bars met.")

if __name__ == "__main__":
    test()
