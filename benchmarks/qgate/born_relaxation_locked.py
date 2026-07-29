"""QGATE-014 (Modeled): BORN RELAXATION UNDER LOCKED BARS.

Question: under the de Broglie guidance flow v = Im(Psi* grad Psi)/|Psi|^2,
does a deliberately non-Born ensemble coarse-grain toward |Psi|^2?

Protocol locked before data:
  * 2-D unit square with hard-wall sine modes.
  * 16-mode superposition with fixed seeded complex coefficients.
  * Nonequilibrium ensemble sampled from the ground-state density while
    guided by the excited 16-mode superposition.
  * Meter 1: coarse-grained relative entropy H = sum rho log(rho/Psi2).
  * Meter 2: coarse-grained L1 distance sum |rho-Psi2|.
  * Control: a single stationary real mode. Its Bohmian velocity is zero,
    so the same nonequilibrium ensemble must not relax.

Pre-committed bars:
  B1: H must fall by more than half.
  B2: L1 distance must fall by at least half.
  B3: stationary-mode control must show |Delta H|/H_initial < 15%.

Scope: this is a deterministic numerical existence demonstration of
coarse-grained relaxation for one mode-mixing flow. It does not prove
universal relaxation, derive Psi from rope mechanics, or establish the
Born measure for every state.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class Result:
    H_initial: float
    H_final: float
    L1_initial: float
    L1_final: float
    control_H_initial: float
    control_H_final: float

    @property
    def H_drop(self) -> float:
        return 1.0 - self.H_final / self.H_initial

    @property
    def L1_drop(self) -> float:
        return 1.0 - self.L1_final / self.L1_initial

    @property
    def control_fractional_change(self) -> float:
        return abs(self.control_H_final - self.control_H_initial) / max(self.control_H_initial, 1e-15)


def _sample_sin2(rng: np.random.Generator, n: int, mode: int = 1) -> np.ndarray:
    """Rejection sample the normalized 1-D density 2 sin^2(mode*pi*x)."""
    out: list[float] = []
    while len(out) < n:
        x = rng.random(n)
        accept = rng.random(n) < np.sin(mode * np.pi * x) ** 2
        out.extend(x[accept].tolist())
    return np.asarray(out[:n])


def _reflect_unit(z: np.ndarray) -> np.ndarray:
    """Reflect trial steps at the hard walls rather than wrapping them."""
    z = np.mod(z, 2.0)
    return np.where(z <= 1.0, z, 2.0 - z)


def _velocity(
    x: np.ndarray,
    y: np.ndarray,
    t: float,
    modes: np.ndarray,
    coeff: np.ndarray,
    omega: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    j = modes[:, 0, None]
    k = modes[:, 1, None]
    sx = np.sin(np.pi * j * x)
    sy = np.sin(np.pi * k * y)
    phase = (2.0 * coeff * np.exp(-1j * omega * t))[:, None]
    psi = np.sum(phase * sx * sy, axis=0)
    dpsi_x = np.sum(phase * (np.pi * j) * np.cos(np.pi * j * x) * sy, axis=0)
    dpsi_y = np.sum(phase * sx * (np.pi * k) * np.cos(np.pi * k * y), axis=0)
    density = np.maximum(np.abs(psi) ** 2, 1e-9)
    vx = np.imag(np.conj(psi) * dpsi_x) / density
    vy = np.imag(np.conj(psi) * dpsi_y) / density
    # Node singularities are physical to the guidance field but require a
    # finite numerical step limiter. The same limiter is used in all runs.
    return np.clip(vx, -40.0, 40.0), np.clip(vy, -40.0, 40.0)


def _advance(
    x: np.ndarray,
    y: np.ndarray,
    total_time: float,
    steps: int,
    modes: np.ndarray,
    coeff: np.ndarray,
    omega: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Midpoint integration of the guidance trajectories."""
    dt = total_time / steps
    x = x.copy()
    y = y.copy()
    for step in range(steps):
        t = step * dt
        vx, vy = _velocity(x, y, t, modes, coeff, omega)
        xm = _reflect_unit(x + 0.5 * dt * vx)
        ym = _reflect_unit(y + 0.5 * dt * vy)
        vxm, vym = _velocity(xm, ym, t + 0.5 * dt, modes, coeff, omega)
        x = _reflect_unit(x + dt * vxm)
        y = _reflect_unit(y + dt * vym)
    return x, y


def _born_cells(
    modes: np.ndarray,
    coeff: np.ndarray,
    omega: np.ndarray,
    t: float,
    bins: int,
    quadrature: int = 8,
) -> np.ndarray:
    """Deterministic midpoint quadrature of |Psi|^2 in each coarse cell."""
    out = np.zeros((bins, bins), dtype=float)
    offsets = (np.arange(quadrature) + 0.5) / quadrature
    for ix in range(bins):
        xs = (ix + offsets) / bins
        for iy in range(bins):
            ys = (iy + offsets) / bins
            xx, yy = np.meshgrid(xs, ys, indexing="ij")
            psi = np.zeros(xx.size, dtype=complex)
            for a, (j, k) in enumerate(modes):
                psi += (
                    2.0
                    * coeff[a]
                    * np.exp(-1j * omega[a] * t)
                    * np.sin(j * np.pi * xx.ravel())
                    * np.sin(k * np.pi * yy.ravel())
                )
            out[ix, iy] = np.mean(np.abs(psi) ** 2) / bins**2
    return out / out.sum()


def _empirical_cells(x: np.ndarray, y: np.ndarray, bins: int) -> np.ndarray:
    hist, _, _ = np.histogram2d(x, y, bins=bins, range=((0.0, 1.0), (0.0, 1.0)))
    return hist / hist.sum()


def _meters(rho: np.ndarray, born: np.ndarray) -> tuple[float, float]:
    mask = rho > 0.0
    H = float(np.sum(rho[mask] * np.log(rho[mask] / np.maximum(born[mask], 1e-15))))
    L1 = float(np.sum(np.abs(rho - born)))
    return H, L1


def run(
    particles: int = 3000,
    steps: int = 1200,
    total_time: float = 4.0,
    bins: int = 14,
    seed: int = 17,
) -> Result:
    rng = np.random.default_rng(seed)
    modes = np.asarray([(j, k) for j in range(1, 5) for k in range(1, 5)], dtype=int)
    coeff = rng.normal(size=16) + 1j * rng.normal(size=16)
    coeff /= np.linalg.norm(coeff)
    omega = 0.5 * np.pi**2 * (modes[:, 0] ** 2 + modes[:, 1] ** 2)

    # Deliberately wrong ensemble: ground-state density, but an excited
    # 16-mode superposition supplies the guidance flow and target density.
    x0 = _sample_sin2(rng, particles, mode=1)
    y0 = _sample_sin2(rng, particles, mode=1)
    xf, yf = _advance(x0, y0, total_time, steps, modes, coeff, omega)

    rho0 = _empirical_cells(x0, y0, bins)
    rhof = _empirical_cells(xf, yf, bins)
    born0 = _born_cells(modes, coeff, omega, 0.0, bins)
    bornf = _born_cells(modes, coeff, omega, total_time, bins)
    H0, L10 = _meters(rho0, born0)
    Hf, L1f = _meters(rhof, bornf)

    # Integrable control: stationary real (2,1) mode. v=0 exactly. Launch
    # the same wrong ground-state ensemble; no relaxation may occur.
    control_modes = np.asarray([(2, 1)], dtype=int)
    control_coeff = np.asarray([1.0 + 0.0j])
    control_omega = 0.5 * np.pi**2 * np.asarray([5.0])
    cxf, cyf = _advance(x0, y0, total_time, steps, control_modes, control_coeff, control_omega)
    control_born = _born_cells(control_modes, control_coeff, control_omega, 0.0, bins)
    control_H0, _ = _meters(rho0, control_born)
    control_Hf, _ = _meters(_empirical_cells(cxf, cyf, bins), control_born)

    return Result(H0, Hf, L10, L1f, control_H0, control_Hf)


def test() -> None:
    result = run()
    assert result.H_drop > 0.50, "B1: coarse-grained H must fall by more than half"
    assert result.L1_drop >= 0.50, "B2: L1 distance to |Psi|^2 must at least halve"
    assert result.control_fractional_change < 0.15, "B3: stationary control must not relax"
    print(
        f"H {result.H_initial:.3f} -> {result.H_final:.3f} "
        f"({100*result.H_drop:.1f}% fall)"
    )
    print(
        f"L1 {result.L1_initial:.3f} -> {result.L1_final:.3f} "
        f"({100*result.L1_drop:.1f}% fall)"
    )
    print(
        f"control H {result.control_H_initial:.3f} -> {result.control_H_final:.3f} "
        f"({100*result.control_fractional_change:.3f}% change)"
    )
    print("PASS: mode mixing produces controlled coarse-grained Born relaxation under all locked bars.")


if __name__ == "__main__":
    test()
