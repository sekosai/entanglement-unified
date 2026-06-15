"""verify_symbolic.py -- exact (symbolic) verification of the ANSATZ core math.

This is a *symbolic* companion to the numerical scripts. Where the numerical
scripts evaluate the relations to floating point, this script proves the core
arithmetic exactly with sympy, so a reader can confirm the results are algebraic
identities rather than numerical coincidences.

It checks three things:

  1. The weighted mean <1/r> integrals in 3+1D, for both admissible CFT weights:
       - low-filling (Racah)  beta = (1 - r/R)^2  ->  <1/r> = 5/(2R),  gamma = 4/5
       - vacuum (CHM)         beta = (R^2-r^2)/2R ->  <1/r> = 15/(8R), gamma = 16/15
     and the continuous family beta = (1 - r/R)^a -> gamma(a) = 4/(a+3).

  2. The discrete dichotomy: the two regimes differ by exactly 4/3 (a 33% split).

  3. The Step A-F derivation chain: solving the cosmic energy balance for the
     per-pair coupling C and substituting into the pairwise force reproduces
       G = (4/5) c^2 R_u / M_u
     with hbar, m_p, and kappa cancelling exactly.

Run:  python3 verify_symbolic.py
"""
from __future__ import annotations

import sympy as sp

# Symbols (all positive reals where physical).
r, R, u, a = sp.symbols("r R u a", positive=True)
hbar, c, m_p, kappa = sp.symbols("hbar c m_p kappa", positive=True)
M_u, R_u, C, N = sp.symbols("M_u R_u C N", positive=True)


def weighted_inv_r(beta):
    """<1/r>_3D = int beta(r) r dr / int beta(r) r^2 dr over [0, R]."""
    num = sp.integrate(beta * r, (r, 0, R))
    den = sp.integrate(beta * r**2, (r, 0, R))
    return sp.simplify(num / den)


def gamma_from(beta):
    """gamma = 2 / (<1/r> * R)  (the factor 2 is the inverse pair-counting 1/2)."""
    return sp.simplify(2 / (weighted_inv_r(beta) * R))


def check(label, got, want):
    ok = sp.simplify(got - want) == 0
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}: {sp.nsimplify(got)} (expected {want})")
    return ok


def main() -> int:
    all_ok = True
    print("ANSATZ symbolic verification (sympy)")
    print("=" * 60)

    # --- 1. Weighted-mean integrals -------------------------------------
    print("\n[1] Weighted mean <1/r> and gamma for each CFT weight")

    beta_lowfill = (1 - r / R) ** 2
    inv_lowfill = weighted_inv_r(beta_lowfill)
    all_ok &= check("low-filling <1/r>", inv_lowfill, sp.Rational(5, 2) / R)
    all_ok &= check("low-filling gamma", gamma_from(beta_lowfill), sp.Rational(4, 5))

    beta_vac = (R**2 - r**2) / (2 * R)
    inv_vac = weighted_inv_r(beta_vac)
    all_ok &= check("vacuum CHM <1/r>", inv_vac, sp.Rational(15, 8) / R)
    all_ok &= check("vacuum CHM gamma", gamma_from(beta_vac), sp.Rational(16, 15))

    # Continuous family gamma(a) = 4/(a+3), verified via the Beta-function ratio.
    num_a = sp.integrate(u * (1 - u) ** a, (u, 0, 1))      # ~ int beta r dr / R^2
    den_a = sp.integrate(u**2 * (1 - u) ** a, (u, 0, 1))   # ~ int beta r^2 dr / R^3
    gamma_a = sp.simplify(2 / (sp.simplify(num_a / den_a)))
    all_ok &= check("continuous gamma(a)", gamma_a, 4 / (a + 3))
    all_ok &= check("gamma(a=2)", gamma_a.subs(a, 2), sp.Rational(4, 5))

    # --- 2. Discrete dichotomy ------------------------------------------
    print("\n[2] Discrete dichotomy: vacuum / low-filling ratio")
    ratio = sp.simplify(sp.Rational(16, 15) / sp.Rational(4, 5))
    all_ok &= check("gamma_vac / gamma_lowfill", ratio, sp.Rational(4, 3))

    # --- 3. Step A-F derivation chain -----------------------------------
    print("\n[3] Step A-F: energy balance -> G, with hbar/m_p/kappa cancelling")

    inv_r_cosmic = sp.Rational(5, 2) / R_u  # <1/r> = 5/(2 R_u)

    # Step E: total entanglement energy = M_u c^2 (sum over N^2/2 distinct pairs)
    E_ent = sp.Rational(1, 2) * N**2 * C * kappa * hbar * c * inv_r_cosmic
    C_sol = sp.solve(sp.Eq(E_ent, M_u * c**2), C)[0]
    C_sol = C_sol.subs(N, M_u / m_p)
    C_sol = sp.simplify(C_sol)
    all_ok &= check(
        "C from balance",
        C_sol,
        sp.Rational(4, 5) * m_p**2 * c * R_u / (kappa * M_u * hbar),
    )

    # Step F: pairwise force F = (M/m_p)(m/m_p) C kappa hbar c / r^2, with C above.
    M, m = sp.symbols("M m", positive=True)
    F = (M / m_p) * (m / m_p) * C_sol * kappa * hbar * c / r**2
    F = sp.simplify(F)

    # Read off G by comparing to Newton F = G M m / r^2.
    G_expr = sp.simplify(F * r**2 / (M * m))
    G_target = sp.Rational(4, 5) * c**2 * R_u / M_u
    all_ok &= check("G = (4/5) c^2 R_u / M_u", G_expr, G_target)

    # Confirm the nuisance constants are truly gone.
    leftover = G_expr.free_symbols & {hbar, m_p, kappa}
    cancelled = len(leftover) == 0
    print(f"  [{'PASS' if cancelled else 'FAIL'}] hbar, m_p, kappa cancel: "
          f"G depends only on {sorted(map(str, G_expr.free_symbols))}")
    all_ok &= cancelled

    print("\n" + "=" * 60)
    print("RESULT:", "ALL CHECKS PASSED" if all_ok else "SOME CHECKS FAILED")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
