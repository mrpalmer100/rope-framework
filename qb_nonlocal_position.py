"""Parameter-count analysis of the rope medium: the primitives {T, kappa, a}
form exactly ONE dimensionless group Pi = kappa*a/T (dimensional reduction 3->1);
Lorentz invariance fixes the line density mu = T/c^2 but leaves Pi untouched
(mu is dimensionally orthogonal to Pi); and the lattice dispersion shows Lorentz
violation ~ (k a)^2/24, bounding the SCALE a but not the coupling Pi.
Supports rope_parameter_count.docx."""
import numpy as np
from sympy import Matrix, lcm, denom

def dimensionless_groups(D):
    """Number and integer form of dimensionless groups from a dimension matrix D
    (rows = base dims, cols = primitives)."""
    n = D.shape[1]; r = D.rank()
    groups = []
    for v in D.nullspace():
        Lc = 1
        for x in v: Lc = lcm(Lc, denom(x))
        groups.append([int(x*Lc) for x in v])
    return n - r, groups

def test_three_primitives_one_group():
    """{T, kappa, a} -> exactly one dimensionless group Pi = kappa*a/T."""
    # rows M,L,Ti ; cols T,kappa,a
    D = Matrix([[1,1,0],[1,0,1],[-2,-2,0]])
    ngroups, groups = dimensionless_groups(D)
    assert ngroups == 1, f"expected 1 dimensionless group, got {ngroups}"
    # the group should be T^-1 kappa^1 a^1 (up to overall sign/scale)
    g = groups[0]
    # normalise so kappa exponent is +1
    assert g == [-1,1,1] or g == [1,-1,-1], f"unexpected group {g}"
    return f"PASS: 3 primitives -> 1 dimensionless group Pi = kappa*a/T (exponents {g})"

def test_mu_is_independent():
    """mu (mass/length) cannot be built from {T,kappa,a}: it is a 4th primitive."""
    # T,kappa both ~ Ti^-2; any product has Ti^(-2(x+y)); mu~Ti^0 forces x+y=0,
    # then M-exponent x+y=0 != 1. Unreachable. Confirm via linear solve.
    from sympy import symbols, Eq, solve
    x,y,z = symbols('x y z')
    sol = solve([Eq(x+y,1), Eq(x+z,-1), Eq(-2*x-2*y,0)], [x,y,z], dict=True)
    assert sol == [], "mu should NOT be expressible from T,kappa,a"
    return "PASS: mu is dimensionally independent of {T,kappa,a} (a 4th primitive)"

def test_lorentz_leaves_pi_free():
    """With 4 primitives {T,kappa,a,mu}, still exactly ONE group, and mu has
    exponent 0 in it -> Lorentz (mu=T/c^2) is orthogonal to Pi=kappa*a/T."""
    D = Matrix([[1,1,0,1],[1,0,1,-1],[-2,-2,0,0]])  # cols T,kappa,a,mu
    ngroups, groups = dimensionless_groups(D)
    assert ngroups == 1, f"expected 1 group with mu added, got {ngroups}"
    g = groups[0]  # [T,kappa,a,mu] exponents
    assert g[3] == 0, f"mu should have exponent 0 in the dimensionless group; got {g}"
    return f"PASS: adding mu keeps 1 group with mu-exponent 0 (exponents {g}); Lorentz fixes mu, not Pi"

def test_lorentz_violation_scales_as_a2():
    """Lattice dispersion: relative Lorentz violation ~ (k a)^2/24 -> bounds scale a, not Pi."""
    c=1.0; a=1.0
    for ka in [0.2,0.1,0.05]:
        k=ka/a
        omega=c*np.sqrt((2/a**2)*(1-np.cos(k*a)))
        viol=abs(omega-c*k)/(c*k)
        pred=(ka)**2/24
        assert abs(viol-pred)/pred < 0.05, f"violation not ~(ka)^2/24 at ka={ka}"
    return "PASS: Lorentz violation ~ (k a)^2/24 (bounds scale a, not dimensionless Pi)"

if __name__=="__main__":
    print(test_three_primitives_one_group())
    print(test_mu_is_independent())
    print(test_lorentz_leaves_pi_free())
    print(test_lorentz_violation_scales_as_a2())
    print("All parameter-count checks passed.")
