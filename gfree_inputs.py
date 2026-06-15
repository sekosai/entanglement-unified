"""gfree_inputs.py -- test the Mach-Sciama prefactor with G-FREE inputs.

This addresses the circularity critique head-on. The headline relation is

    G = (4/5) * c^2 * R / M.

The paper's 0.21% match uses R = particle horizon and M = total LambdaCDM
energy budget -- but that M is gravitationally inferred (it contains G). Here we
ask the honest question: if we feed the formula ONLY radii and masses obtainable
WITHOUT Newton's G, what value of G comes out?

G-free radii (expansion kinematics, no G):
  - Hubble radius        R_H = c / H0           (H0 from redshift-distance)
  - Particle horizon     R_obs ~ 46.5 Gly       (expansion-history integral)

G-free baryonic mass (no G):
  - n_gamma from the CMB blackbody temperature (pure thermodynamics)
  - n_b = eta * n_gamma, eta from BBN / light-element abundances
  - M_b = n_b * m_p * V(R)

NOT G-free (shown only for contrast):
  - critical-density mass  rho_c = 3 H0^2 / (8 pi G)   (contains G)
  - matter mass (baryon + dark matter; DM is gravitationally inferred)
  - total LambdaCDM energy budget (the paper's back-fit input)

Run:  python3 gfree_inputs.py
"""
from __future__ import annotations

import math

from constants import (
    C, M_P, HBAR, K_B, G_MEASURED, GAMMA_PREFACTOR,
    H0_SI, R_UNIVERSE, M_UNIVERSE_TOTAL, M_UNIVERSE_MATTER,
    FRACTION_BARYONIC, FRACTION_DARK_MATTER,
)

LY = 9.4607e15          # m per light-year
GLY = 1e9 * LY

# ---------------------------------------------------------------------------
# G-free radii (expansion kinematics)
# ---------------------------------------------------------------------------
R_HUBBLE = C / H0_SI                 # c / H0
R_PARTICLE_HORIZON = R_UNIVERSE      # ~4.4e26 m ~ 46.5 Gly (expansion integral)

# ---------------------------------------------------------------------------
# G-free baryon number density: CMB blackbody + BBN
# ---------------------------------------------------------------------------
T_CMB = 2.7255                       # K (COBE/FIRAS)
ZETA_3 = 1.2020569
N_GAMMA = (2 * ZETA_3 / math.pi**2) * (K_B * T_CMB / (HBAR * C)) ** 3  # photons/m^3
ETA_BARYON = 6.1e-10                 # baryon-to-photon ratio (BBN/PDG)
N_BARYON = ETA_BARYON * N_GAMMA      # baryons/m^3

# CMB radiation energy density (also G-free), for completeness
SIGMA_SB = 5.670374419e-8           # W m^-2 K^-4
A_RAD = 4 * SIGMA_SB / C            # radiation constant a
U_CMB = A_RAD * T_CMB ** 4          # J/m^3

# G-laden critical density (for contrast only)
RHO_CRIT = 3 * H0_SI**2 / (8 * math.pi * G_MEASURED)   # kg/m^3 (uses G!)


def volume(R: float) -> float:
    return (4.0 / 3.0) * math.pi * R**3


def baryonic_mass(R: float) -> float:
    return N_BARYON * M_P * volume(R)


def radiation_mass(R: float) -> float:
    return U_CMB * volume(R) / C**2


def critical_mass(R: float) -> float:
    return RHO_CRIT * volume(R)


def G_pred(R: float, M: float) -> float:
    return GAMMA_PREFACTOR * C**2 * R / M


def row(label: str, R: float, M: float, gfree: str) -> None:
    g = G_pred(R, M)
    ratio = g / G_MEASURED
    print(f"  {label:38s} R={R:8.2e} m  M={M:8.2e} kg  "
          f"G={g:8.2e}  G/Gmeas={ratio:8.3f}  [{gfree}]")


def main() -> int:
    print("G-FREE INPUT TEST for  G = (4/5) c^2 R / M")
    print("=" * 96)
    print(f"  measured G              = {G_MEASURED:.4e} m^3/(kg s^2)")
    print(f"  H0                      = {H0_SI:.3e} s^-1  "
          f"({H0_SI*3.086e22/1e3:.1f} km/s/Mpc)")
    print(f"  R_Hubble = c/H0         = {R_HUBBLE:.3e} m  ({R_HUBBLE/GLY:.1f} Gly)")
    print(f"  R_particle_horizon      = {R_PARTICLE_HORIZON:.3e} m  "
          f"({R_PARTICLE_HORIZON/GLY:.1f} Gly)")
    print(f"  n_gamma (CMB)           = {N_GAMMA:.3e} /m^3  ({N_GAMMA/1e6:.0f} /cm^3)")
    print(f"  n_baryon = eta*n_gamma  = {N_BARYON:.3e} /m^3")
    print(f"  rho_crit (uses G!)      = {RHO_CRIT:.3e} kg/m^3")
    print()

    print("  --- purely G-free (radius: kinematics; mass: photon-count baryons) ---")
    row("Hubble R x baryonic(count)", R_HUBBLE, baryonic_mass(R_HUBBLE), "G-free")
    row("Particle horizon x baryonic", R_PARTICLE_HORIZON,
        baryonic_mass(R_PARTICLE_HORIZON), "G-free")
    print()

    print("  --- mass-equivalent of CMB radiation alone (G-free, negligible) ---")
    row("Particle horizon x CMB rad.", R_PARTICLE_HORIZON,
        radiation_mass(R_PARTICLE_HORIZON), "G-free")
    print()

    print("  --- G-laden masses (shown for contrast; NOT independent of G) ---")
    row("Hubble R x critical-density", R_HUBBLE, critical_mass(R_HUBBLE), "G-laden")
    row("Particle horizon x critical", R_PARTICLE_HORIZON,
        critical_mass(R_PARTICLE_HORIZON), "G-laden")
    row("Particle horizon x matter", R_PARTICLE_HORIZON, M_UNIVERSE_MATTER, "G-laden")
    row("Particle horizon x TOTAL (paper)", R_PARTICLE_HORIZON, M_UNIVERSE_TOTAL,
        "G-laden")
    print()

    # Key analytic observations
    print("  --- observations ---")
    g_hub_crit = G_pred(R_HUBBLE, critical_mass(R_HUBBLE))
    print(f"  * Hubble radius @ critical density gives G/Gmeas = "
          f"{g_hub_crit/G_MEASURED:.3f}  (= 8/5 = 1.600 exactly,")
    print("    because there c^2 R/M = 2G, so the 4/5 prefactor overshoots the")
    print("    natural Mach-Sciama 1/2 by 8/5).")
    g_bary = G_pred(R_PARTICLE_HORIZON, baryonic_mass(R_PARTICLE_HORIZON))
    print(f"  * Best purely-G-free combo (particle horizon x counted baryons) is")
    print(f"    off by {g_bary/G_MEASURED:.2f}x. To hit measured G with this")
    R_needed = math.sqrt(g_bary / G_MEASURED) * R_PARTICLE_HORIZON
    print(f"    baryon density you would need R ~ {R_needed/GLY:.0f} Gly")
    print(f"    (a universe ~{R_needed/R_PARTICLE_HORIZON:.1f}x the observable radius).")
    print()
    print("  CONCLUSION: no purely G-free (R, M) pair reproduces measured G.")
    print("  The 0.21% match requires the gravitationally-inferred total mass.")
    print("  This quantifies the circularity the paper already concedes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
