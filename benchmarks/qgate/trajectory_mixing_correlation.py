"""QGATE-016: direct trajectory-instability / Born-relaxation correlation.

The bars and interpretation were locked in
analysis/QGATE016_mixing_bars_LOCKED.md before this benchmark was run.
"""
from __future__ import annotations

from dataclasses import dataclass
import csv
from pathlib import Path
import sys
import numpy as np

try:
    from benchmarks.qgate.born_relaxation_locked import _sample_sin2, _reflect_unit, _velocity
    from benchmarks.qgate.born_relaxation_mode_count import (
        MODE_COUNTS, SEEDS, _mode_pool, _spearman,
    )
except ModuleNotFoundError:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from benchmarks.qgate.born_relaxation_locked import _sample_sin2, _reflect_unit, _velocity
    from benchmarks.qgate.born_relaxation_mode_count import (
        MODE_COUNTS, SEEDS, _mode_pool, _spearman,
    )


@dataclass(frozen=True)
class MixingRow:
    seed: int
    modes: int
    ftle: float
    H_drop: float
    L1_drop: float


def _midpoint_step(x: np.ndarray, y: np.ndarray, t: float, dt: float,
                   modes: np.ndarray, coeff: np.ndarray,
                   omega: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    vx, vy = _velocity(x, y, t, modes, coeff, omega)
    xm = _reflect_unit(x + 0.5 * dt * vx)
    ym = _reflect_unit(y + 0.5 * dt * vy)
    vxm, vym = _velocity(xm, ym, t + 0.5 * dt, modes, coeff, omega)
    return _reflect_unit(x + dt * vxm), _reflect_unit(y + dt * vym)


def _ftle(seed: int, count: int, trajectories: int = 256,
          steps: int = 1200, total_time: float = 4.0,
          renorm_every: int = 20, delta0: float = 1e-6) -> float:
    """Mean finite-separation exponent with periodic pair renormalization."""
    pool = _mode_pool()
    rng_coeff = np.random.default_rng(seed)
    coeff_pool = rng_coeff.normal(size=64) + 1j * rng_coeff.normal(size=64)
    modes = pool[:count]
    coeff = coeff_pool[:count].copy()
    coeff /= np.linalg.norm(coeff)
    omega = 0.5 * np.pi**2 * (modes[:, 0] ** 2 + modes[:, 1] ** 2)

    # Separate deterministic stream for trajectory and displacement sampling.
    rng = np.random.default_rng(seed + 100_003)
    x = _sample_sin2(rng, trajectories, mode=1)
    y = _sample_sin2(rng, trajectories, mode=1)
    theta = rng.uniform(0.0, 2.0 * np.pi, trajectories)
    xp = _reflect_unit(x + delta0 * np.cos(theta))
    yp = _reflect_unit(y + delta0 * np.sin(theta))

    dt = total_time / steps
    log_growth = np.zeros(trajectories, dtype=float)
    t = 0.0
    for step in range(1, steps + 1):
        x, y = _midpoint_step(x, y, t, dt, modes, coeff, omega)
        xp, yp = _midpoint_step(xp, yp, t, dt, modes, coeff, omega)
        t += dt
        if step % renorm_every == 0 or step == steps:
            dx = xp - x
            dy = yp - y
            dist = np.sqrt(dx * dx + dy * dy)
            safe = np.maximum(dist, 1e-15)
            log_growth += np.log(safe / delta0)
            # Preserve the measured direction; regenerate only collapsed pairs.
            collapsed = dist < 1e-15
            if np.any(collapsed):
                angles = rng.uniform(0.0, 2.0 * np.pi, int(np.sum(collapsed)))
                dx[collapsed] = np.cos(angles)
                dy[collapsed] = np.sin(angles)
                safe[collapsed] = 1.0
            xp = _reflect_unit(x + delta0 * dx / safe)
            yp = _reflect_unit(y + delta0 * dy / safe)

    # Median across trajectories is robust to rare near-node bursts.
    return float(np.median(log_growth / total_time))


def _load_relaxation(path: Path) -> dict[tuple[int, int], tuple[float, float]]:
    out: dict[tuple[int, int], tuple[float, float]] = {}
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out[(int(row["seed"]), int(row["modes"]))] = (
                float(row["H_drop"]), float(row["L1_drop"])
            )
    expected = {(s, m) for s in SEEDS for m in MODE_COUNTS}
    if set(out) != expected:
        raise RuntimeError("QGATE-015 result grid is incomplete or changed")
    return out


def run() -> list[MixingRow]:
    root = Path(__file__).resolve().parents[2]
    relax = _load_relaxation(root / "analysis" / "QGATE015_mode_count_results.csv")
    rows: list[MixingRow] = []
    for seed in SEEDS:
        for count in MODE_COUNTS:
            ftle = _ftle(seed, count)
            h, l1 = relax[(seed, count)]
            rows.append(MixingRow(seed, count, ftle, h, l1))
            print(f"seed={seed:2d} M={count:2d} lambda_FT={ftle: .6f} "
                  f"Hdrop={100*h:6.2f}% L1drop={100*l1:6.2f}%", flush=True)
    return rows


def _write_csv(rows: list[MixingRow], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["seed", "modes", "lambda_FT", "H_drop", "L1_drop"])
        for r in rows:
            w.writerow([r.seed, r.modes, r.ftle, r.H_drop, r.L1_drop])


def test() -> None:
    rows = run()
    root = Path(__file__).resolve().parents[2]
    _write_csv(rows, root / "analysis" / "QGATE016_mixing_results.csv")

    med = {m: float(np.median([r.ftle for r in rows if r.modes == m]))
           for m in MODE_COUNTS}
    ftle = np.asarray([r.ftle for r in rows])
    h = np.asarray([r.H_drop for r in rows])
    l1 = np.asarray([r.L1_drop for r in rows])
    logm = np.log2(np.asarray([r.modes for r in rows], dtype=float))
    rho_h = _spearman(ftle, h)
    rho_l1 = _spearman(ftle, l1)
    rho_m_h = _spearman(logm, h)
    unstable = sum(med[m] >= med[1] + 0.05 for m in MODE_COUNTS[1:])

    print("\nMedian finite-time exponents:")
    for m in MODE_COUNTS:
        print(f"M={m:2d}: {med[m]: .6f}")
    print(f"Spearman(lambda_FT, H_drop):  {rho_h: .6f}")
    print(f"Spearman(lambda_FT, L1_drop): {rho_l1: .6f}")
    print(f"Spearman(log2 M, H_drop):     {rho_m_h: .6f}")
    print(f"Multimode medians > control+0.05: {unstable}/6")

    # Mechanically verify the preregistered outcome, including the failed fifth bar.
    assert abs(med[1]) < 0.05, "B1 outcome drifted"
    assert unstable >= 5, "B2 outcome drifted"
    assert rho_h > 0.30, "B3 outcome drifted"
    assert rho_l1 > 0.30, "B4 outcome drifted"
    assert not (abs(rho_h) > abs(rho_m_h)), "B5 outcome drifted: FTLE now outperforms mode count"
    print("PASS: locked outcome reproduced (B1-B4 pass; B5 fails and is kept).")


if __name__ == "__main__":
    test()
