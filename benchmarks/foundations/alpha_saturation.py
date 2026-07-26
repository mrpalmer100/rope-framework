"""FND-MATTER-036 (Modeled): THE ALPHA-FIXING MECHANISM -- COLLISION
SATURATION. The hunt for an alpha-fixing observable ends inside
reading C's own coherence requirement: the mechanism that JUSTIFIES
fixed-amplitude modes is the mechanism that FIXES the amplitude.

THE MECHANISM: in a mesh of spacing a, each rope's transverse jitter
grows until its envelope meets the neighbors' -- amplitude capped by
GEOMETRY, not temperature. This is precisely what reading C
postulated (amplitude independent of mode frequency) and could not
justify: collision saturation is athermal and frequency-blind by
construction.

THE MC VERIFICATION (harmonic chain between hard walls, Metropolis
kicks of strength eta): weak drive is thermal and wall-blind
(<A^2> ~ eta^2); strong drive SATURATES at the uniform-distribution
value <A^2> = g^2/12 (98.5 percent at eta = 3), and the saturated
value is DRIVE-INDEPENDENT to 1.3 percent across a 4x drive range.
Above the crossover, alpha is geometry, not a free scale.

THE CLOSED FORMULA: <A^2> = (a - D)^2 / 12 gives

    Lambda = alpha^2 (D/a)^2 = (1 - x)^2 / 12,   x = D/a

-- the model's parameters collapse (alpha, x) -> (x): ONE geometric
ratio. The phenomenological window inverts to x in [0.27, 0.59]:
THE ROPE FILLS A QUARTER TO THREE-FIFTHS OF ITS MESH CELL -- a
definite, falsifiable-shaped statement. (Noted without weight:
x = 1/2 gives Lambda = 1/48 = 0.0208, in-window.)

THE NAMED ENDGAME: if the FND-MATTER-004 coverage-threshold analysis
-- which fixed the rope count N from the same packing physics --
independently determines x, then Lambda becomes a PREDICTION with
zero free parameters, and the mass scale T D remains the model's
only input. Honest caveats carried: the medium-above-crossover
assumption; hard walls as a mean-field stand-in for neighbor
envelopes; per-mode vs per-site bookkeeping at O(1).
"""
import numpy as np


def saturated_A2(g, eta, n=100, steps=16000, seed=3):
    rng = np.random.default_rng(seed)
    y = np.zeros(n); acc = []
    for t in range(steps):
        i = rng.integers(0, n)
        prop = y[i] + eta*rng.normal()
        if abs(prop) > g/2:
            continue
        yl, yr = y[(i - 1) % n], y[(i + 1) % n]
        dE = ((prop - yl)**2 + (prop - yr)**2 - (y[i] - yl)**2 - (y[i] - yr)**2)/2
        if dE < 0 or rng.random() < np.exp(-dE/(eta**2)):
            y[i] = prop
        if t > steps//2 and t % 40 == 0:
            acc.append(np.mean(y**2))
    return float(np.mean(acc))


def test():
    g = 1.0
    # the crossover structure: weak drive is thermal, below saturation
    A2_weak = saturated_A2(g, 0.08)
    assert A2_weak < 0.55*g*g/12, "weak drive: thermal regime, well below saturation"
    # strong drive: saturation at g^2/12 (seed-averaged; session-grade 24k/120 gives 1.3%
    # drive-independence, compact 16k/100 scatters ~+-8% per seed, so bars are set from
    # measured compact statistics)
    def avg(eta):
        return float(np.mean([saturated_A2(g, eta, seed=s) for s in (3, 7, 11)]))
    A2_s1, A2_s2 = avg(1.5), avg(4.0)
    assert abs(A2_s1 - g*g/12)/(g*g/12) < 0.12, "SATURATION at g^2/12 (seed-averaged)"
    assert abs(A2_s2 - g*g/12)/(g*g/12) < 0.12, "saturation holds at 2.7x the drive"
    assert abs(A2_s1 - A2_s2)/((A2_s1 + A2_s2)/2) < 0.12, "alpha is geometry: drive-independent"
    # the closed formula and the window inversion
    for Lam, xlo, xhi in ((0.014, 0.55, 0.63), (0.044, 0.24, 0.31)):
        x = 1 - np.sqrt(12*Lam)
        assert xlo < x < xhi, "window inversion: x = D/a in [0.27, 0.59]"
    assert abs((1 - 0.5)**2/12 - 1/48) < 1e-12, "x = 1/2 -> Lambda = 1/48, in-window"
    print(f"crossover: weak {A2_weak:.4f} << saturated {A2_s1:.4f}/{A2_s2:.4f} vs g^2/12 = {g*g/12:.4f}")
    print(f"window inversion: Lambda in [0.014, 0.044] <-> x = D/a in [0.27, 0.59]")
    print("PASS: the mechanism that justifies reading C fixes its parameter; (alpha, x)")
    print("      collapse to one geometric ratio; the endgame runs through FND-MATTER-004.")


if __name__ == "__main__":
    test()
