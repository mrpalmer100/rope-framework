"""QGATE-015: mode-count robustness campaign for Born relaxation.

A preliminary 800-step fixed-resolution pilot failed at M=64. A disclosed
timestep-convergence diagnostic showed that this was a numerical resolution
artifact: at 1200 steps all three M=64 seeds recovered strong relaxation.
The registered benchmark therefore uses 1200 steps uniformly for all M.
"""
from __future__ import annotations

from dataclasses import dataclass
import csv
from pathlib import Path
import sys
import numpy as np

try:
    from benchmarks.qgate.born_relaxation_locked import (
        _advance, _empirical_cells, _meters, _sample_sin2,
    )
except ModuleNotFoundError:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from benchmarks.qgate.born_relaxation_locked import (
        _advance, _empirical_cells, _meters, _sample_sin2,
    )

MODE_COUNTS = (1, 2, 4, 8, 16, 32, 64)
SEEDS = (17, 29, 43)

@dataclass(frozen=True)
class Row:
    seed: int
    modes: int
    H_initial: float
    H_final: float
    L1_initial: float
    L1_final: float

    @property
    def H_drop(self) -> float:
        return 1.0 - self.H_final / max(self.H_initial, 1e-15)

    @property
    def L1_drop(self) -> float:
        return 1.0 - self.L1_final / max(self.L1_initial, 1e-15)


def _mode_pool() -> np.ndarray:
    modes = [(j, k) for j in range(1, 9) for k in range(1, 9) if (j, k) != (1, 1)]
    modes.sort(key=lambda p: (p[0] ** 2 + p[1] ** 2, p[0], p[1]))
    # Need 64 excited modes; add the next energy shell deterministically.
    if len(modes) < 64:
        extra = [(j, k) for j in range(1, 10) for k in range(1, 10)
                 if (j, k) != (1, 1) and (j, k) not in modes]
        extra.sort(key=lambda p: (p[0] ** 2 + p[1] ** 2, p[0], p[1]))
        modes.extend(extra)
    return np.asarray(modes[:64], dtype=int)



def _born_cells_fast(modes: np.ndarray, coeff: np.ndarray, omega: np.ndarray,
                     t: float, bins: int, quadrature: int = 8) -> np.ndarray:
    """Vectorized deterministic midpoint quadrature of |Psi|^2 by cell."""
    n = bins * quadrature
    grid = (np.arange(n) + 0.5) / n
    sx = np.sin(np.pi * modes[:, 0, None] * grid[None, :])
    sy = np.sin(np.pi * modes[:, 1, None] * grid[None, :])
    phase = 2.0 * coeff * np.exp(-1j * omega * t)
    psi = np.einsum("a,ax,ay->xy", phase, sx, sy, optimize=True)
    density = np.abs(psi) ** 2
    cells = density.reshape(bins, quadrature, bins, quadrature).mean(axis=(1, 3))
    return cells / cells.sum()

def _rankdata(values: np.ndarray) -> np.ndarray:
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty(len(values), dtype=float)
    i = 0
    while i < len(values):
        j = i + 1
        while j < len(values) and values[order[j]] == values[order[i]]:
            j += 1
        ranks[order[i:j]] = 0.5 * (i + j - 1) + 1.0
        i = j
    return ranks


def _spearman(x: np.ndarray, y: np.ndarray) -> float:
    rx, ry = _rankdata(x), _rankdata(y)
    return float(np.corrcoef(rx, ry)[0, 1])


def _run_seed(args: tuple[int, int, int, float, int]) -> list[Row]:
    seed, particles, steps, total_time, bins = args
    pool = _mode_pool()
    rng = np.random.default_rng(seed)
    coeff_pool = rng.normal(size=64) + 1j * rng.normal(size=64)
    x0 = _sample_sin2(rng, particles, mode=1)
    y0 = _sample_sin2(rng, particles, mode=1)
    rho0 = _empirical_cells(x0, y0, bins)
    rows: list[Row] = []
    for count in MODE_COUNTS:
        modes = pool[:count]
        coeff = coeff_pool[:count].copy()
        coeff /= np.linalg.norm(coeff)
        omega = 0.5 * np.pi**2 * (modes[:, 0] ** 2 + modes[:, 1] ** 2)
        xf, yf = _advance(x0, y0, total_time, steps, modes, coeff, omega)
        born0 = _born_cells_fast(modes, coeff, omega, 0.0, bins)
        bornf = _born_cells_fast(modes, coeff, omega, total_time, bins)
        H0, L10 = _meters(rho0, born0)
        Hf, L1f = _meters(_empirical_cells(xf, yf, bins), bornf)
        rows.append(Row(seed, count, H0, Hf, L10, L1f))
    return rows


def run(particles: int = 1500, steps: int = 1200, total_time: float = 4.0,
        bins: int = 14) -> list[Row]:
    from concurrent.futures import ProcessPoolExecutor
    args = [(seed, particles, steps, total_time, bins) for seed in SEEDS]
    with ProcessPoolExecutor(max_workers=len(SEEDS)) as ex:
        chunks = list(ex.map(_run_seed, args))
    return [row for chunk in chunks for row in chunk]

def summarize(rows: list[Row]) -> dict[int, tuple[float, float]]:
    out = {}
    for count in MODE_COUNTS:
        selected = [r for r in rows if r.modes == count]
        out[count] = (float(np.median([r.H_drop for r in selected])),
                      float(np.median([r.L1_drop for r in selected])))
    return out


def write_csv(rows: list[Row], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["seed", "modes", "H_initial", "H_final", "H_drop",
                    "L1_initial", "L1_final", "L1_drop"])
        for r in rows:
            w.writerow([r.seed, r.modes, r.H_initial, r.H_final, r.H_drop,
                        r.L1_initial, r.L1_final, r.L1_drop])


def test() -> None:
    rows = run()
    summary = summarize(rows)
    output = Path(__file__).resolve().parents[2] / "analysis" / "QGATE015_mode_count_results.csv"
    write_csv(rows, output)

    one_h = abs(summary[1][0])
    high = (16, 32, 64)
    broad_passes = sum(summary[m][0] > 0.50 for m in MODE_COUNTS[1:])
    x = np.log2(np.asarray(MODE_COUNTS[1:], dtype=float))
    y = np.asarray([summary[m][0] for m in MODE_COUNTS[1:]])
    rho = _spearman(x, y)

    for m in MODE_COUNTS:
        print(f"M={m:2d}: median H drop={100*summary[m][0]:7.2f}%  "
              f"median L1 drop={100*summary[m][1]:7.2f}%")
    print(f"Spearman(log2 M, median H drop), M>=2: {rho:.3f}")
    print(f"Multimode counts with median H drop >50%: {broad_passes}/6")

    assert one_h < 0.15, "B1 failed: one-mode control changed H by >=15%"
    assert all(summary[m][0] > 0.50 for m in high), "B2 failed: high-mode H robustness"
    assert all(summary[m][1] >= 0.50 for m in high), "B3 failed: high-mode L1 robustness"
    assert broad_passes >= 4, "B4 failed: fewer than four multimode counts passed H bar"
    assert rho > 0.0, "B5 failed: no positive directional mode-count scaling"
    print("PASS: all locked mode-count robustness bars met.")

if __name__ == "__main__":
    test()
