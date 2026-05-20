"""constants.py -- physical constants shared across all gravity experiments.

G is NOT defined here. It is derived, not assumed. See derive_G.py.
"""
from __future__ import annotations

import math

# ---------------------------------------------------------------------------
# Fundamental constants (CODATA 2018)
# ---------------------------------------------------------------------------
HBAR = 1.054571817e-34       # J*s  (reduced Planck constant)
C = 2.99792458e8             # m/s  (speed of light)
M_P = 1.6726219e-27          # kg   (proton mass -- representative nucleon)
M_E = 9.1093837e-31          # kg   (electron mass)
E_CHARGE = 1.602176634e-19   # C    (elementary charge)
K_B = 1.380649e-23           # J/K  (Boltzmann constant)
EPS_0 = 8.854187817e-12      # F/m  (vacuum permittivity)
K_E = 8.987551787e9          # N*m^2/C^2 (Coulomb constant)

# Derived from fundamental constants (no G required)
LAMBDA_C_P = HBAR / (M_P * C)      # 2.103e-16 m  (proton Compton wavelength)
LAMBDA_C_E = HBAR / (M_E * C)      # 2.426e-12 m  (electron Compton wavelength)
OMEGA_COMPTON_P = M_P * C**2 / HBAR  # 1.425e+24 rad/s (proton Compton frequency)
S_12 = math.sqrt(0.5 * 1.5) * HBAR  # 9.133e-35 J*s (spin-1/2 angular momentum)

# Fine structure constant (electromagnetic)
ALPHA_EM = E_CHARGE**2 / (4 * math.pi * EPS_0 * HBAR * C)  # ~1/137

# ---------------------------------------------------------------------------
# Earth parameters
# ---------------------------------------------------------------------------
M_EARTH = 5.972e24           # kg
R_EARTH = 6.371e6            # m
J_EARTH = 5.86e33            # kg*m^2/s (Earth's angular momentum)
G_TARGET = 9.807             # m/s^2 (measured g at surface)

# ---------------------------------------------------------------------------
# Observable universe parameters
# ---------------------------------------------------------------------------
M_UNIVERSE_BARYONIC = 2.32e52   # kg (baryonic matter only, ~4.9% of total)
M_UNIVERSE_DM = 1.268e53        # kg (cold dark matter, ~26.8% of total)
M_UNIVERSE_MATTER = 1.50e53     # kg (baryonic + dark matter, ~31.7% of total)
M_UNIVERSE_TOTAL = 4.73e53      # kg (total energy density, ~100% Lambda-CDM)
R_UNIVERSE = 4.4e26             # m  (observable universe radius)

# Lambda-CDM fractions (Planck 2018)
FRACTION_BARYONIC = 0.049
FRACTION_DARK_MATTER = 0.268
FRACTION_DARK_ENERGY = 0.683

# Hubble constant
H0 = 67.4e-3                 # m/s/Mpc
MPC = 3.086e22               # m per Mpc
H0_SI = H0 / MPC             # s^-1

# ---------------------------------------------------------------------------
# Measured G -- for verification ONLY, never as an input to derivation
# ---------------------------------------------------------------------------
G_MEASURED = 6.67430e-11     # m^3/(kg*s^2) (CODATA 2018)


def nucleon_count(mass: float) -> float:
    """Convert mass to nucleon count."""
    return mass / M_P


def concurrence_from_cosmic(M_universe: float = M_UNIVERSE_TOTAL,
                             R_universe: float = R_UNIVERSE) -> float:
    """Derive concurrence from cosmic energy balance.

    E_entanglement = E_mass
    3/4 * N^2 * concurrence * hbar*c / R = M * c^2
    concurrence = (4/3) * (m_p^2 * c * R) / (M * hbar)
    """
    return (4/3) * (M_P**2 * C * R_universe) / (M_universe * HBAR)


def G_from_cosmic(M_universe: float = M_UNIVERSE_TOTAL,
                   R_universe: float = R_UNIVERSE) -> float:
    """Derive G from cosmic parameters.

    G = (4/3) * c^2 * R_universe / M_universe
    (4/3 is the spherical geometry correction)
    """
    return (4/3) * C**2 * R_universe / M_universe
