# COMMISSION CURRENT-AS-SPIN (RESH2) -- RESULTS (2026-08-16)

Bars: analysis/RESH2_current_as_spin_bars_LOCKED.md (locked first).
Benchmark: benchmarks/em/current_as_spin_resh2.py (sympy-exact, all
assertions pass). Verdict: RATE-UNDERDETERMINED, with the missing
input named and the injection side DERIVED. The asymmetry is
quantified in closed form with an exact zero.

## (a) TORQUE INJECTION -- the injection side DERIVES, exactly

From the registered lock energy (lambda/2)(delta_tau +
gamma tau0 eps)^2 alone (EM-RECON-012, Derived), the generalized
torque density on the azimuthal coordinate is

    Gamma(z) = lambda [ phi'' + gamma tau0 eps' ]

so a steady EMF-class strain gradient eps' = E0 on an unwound span
injects torque at

    Gamma_inj = lambda gamma tau0 E0        [DERIVED, exact]

per unit length. This is the drill-bit statement made quantitative:
longitudinal drive on a WOUND strand (tau0 != 0) is an azimuthal
torque; on an unwound strand (tau0 = 0) it is not. The winding is
the transmission.

## (a') TORQUE BALANCE -- the rate does NOT close: RATE-UNDERDETERMINED

Azimuth-blindness is exact (dV/dphi = 0 identically, EM-RECON-023;
re-verified on the lock energy: no phi dependence, only phi'). So
registered structure supplies NO azimuthal drag coefficient at the
crossings. The only registered escape is the lock chain, whose
crossing transfer RATE is exactly GRV-118's vertex obligation (3),
explicitly not owed and refused at these bars. The balance is

    lambda gamma tau0 E0 = eta_chain * Omega
    Omega = lambda gamma tau0 E0 / eta_chain

with eta_chain UNREGISTERED. THE MISSING INPUT, NAMED: the crossing
transfer rate of the lock chain, owned by the vertex session
(GRV-118 obligation 3). In the eta_chain -> 0 limit the drive gives
steady angular ACCELERATION d(I Omega)/dt = lambda gamma tau0 E0:
rotation is what the drive buys, with or without the closure.

## (b) SPIN PERSISTENCE -- the asymmetry, quantified

The stiffness matrix [[lambda, c_L],[c_L, k_s]] has its off-diagonal
read off the SAME lock energy: c_L = lambda gamma tau0 (consistent
with EM-RECON-023's constant-entry commitment). The twist-dominant
eigenbranch carries stretch fraction sin^2(chi) with

    tan(2 chi) = 2 lambda gamma tau0 / (k_s - lambda)

and ONLY that stretch admixture reaches the O(g) crossing channel
(EM-RECON-026). The pure-twist component's crossing coupling is
ZERO EXACTLY (dV/dphi = 0). Therefore, per crossing:

    L_transverse ~ O(g)                       (every crossing)
    L_azimuth    = sin^2(chi) x O(g) x C_chain

with C_chain <= 1 the unpriced lock-chain factor. Even at the most
generous C_chain = 1:

    L_az / L_tr <= sin^2(chi) < 1/2   whenever k_s > lambda

and sin^2(chi) -> 0 as the lock is switched off (chi -> 0 at
tau0 -> 0, machine-verified) -- the lock that lets torque IN is the
only door letting spin OUT, and it is the same narrow door.
Numeric evaluation of sin^2(chi) is GATED on tau0 (no registered
numeric); gamma carries its registered bracket ~2-4.

## THE ANSWER TO THE AUTHOR'S QUESTION, in one paragraph

Conduction ropes spin because winding converts longitudinal drive
into torque exactly (Gamma_inj = lambda gamma tau0 E0, derived), and
they KEEP spinning because the azimuthal reservoir leaks only
through its own stretch admixture sin^2(chi) of the O(g) channel,
strictly less than half the transverse leak and further suppressed
by the unpriced chain factor, while transverse vibration pays O(g)
at every crossing in full. Current is spin because spin is what the
winding buys and what the blindness protects. The steady RATE awaits
one number, and that number has an owner: the vertex session.

## REFUSALS HONORED
No suppression order computed; no new coupling; GRV-118 untouched;
titles read at verdict level; the gate on tau0 named, not filled.
