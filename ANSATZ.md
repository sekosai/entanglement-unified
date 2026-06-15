# An Entanglement Ansatz for the Mach–Sciama Relation

> **Authoritative version:** [`ANSATZ.pdf`](ANSATZ.pdf) is the canonical document. This markdown is an older draft; the PDF supersedes it on framing and scope.

## Abstract

The relation $G \sim c^2 R/M$ between Newton's gravitational constant
and cosmic boundary conditions is the well-known Mach–Sciama identity:
in any flat critical-density cosmology, $G$ and $c^2 R/M$ are
algebraically related through the Friedmann equation. What is *not*
explained in standard cosmology is *why* the universe should sit at
this self-consistency point. We propose a quantum entanglement
mechanism — orthogonal jerk creating helical trajectories, with bond
energy $\hbar c/r$ and torque geometry from the Bisognano–Wichmann
theorem — that predicts the specific prefactor

$$
G \;=\; \frac{4}{5}\,\frac{c^2 R_{\text{universe}}}{M_{\text{universe}}}
$$

from the modular Hamiltonian of the cosmic reduced density matrix.
The numerical value is consistent with the measured $G$ to within
current cosmic-parameter uncertainties.

**Scope.** This is *not* a free or local derivation of $G$. The cosmic
inputs $R_{\text{universe}}$ and $M_{\text{universe}}$ are themselves
determined within general-relativistic cosmology and contain $G$
implicitly. Worse, the same formula evaluated on any local causal patch
(e.g., Earth) fails by ~36 orders of magnitude — the formula only works
where $M/R$ is forced by the critical-density condition, which itself
contains $G$. So the cosmic match is a Mach–Sciama consistency check at
one scale, not a local statement of $G$. The substantive content is the
predicted prefactor $4/5$ and the mechanism itself, not the numerical
value of $G$. A cleaner $G$-independent test of the same mechanism — the
exact derivation of the Bohr magneton at the electron scale — is given
in `DERIVE_EM.pdf`. The PDF includes "Alternate Choices of $R$ and $M$,"
the explicit local Earth-as-patch test, and a "Toward a Local
Derivation" section pointing at the Jacobson–Padmanabhan–Verlinde
program.

---

## The Empirical Anchor: A $G$-Free Test (Read First)

The strongest evidence for the mechanism is *not* the cosmic $G$ match below —
which, as the Scope note explains, is a one-scale consistency check entangled
with $G$ through the cosmic inputs. The strongest evidence is an **exact,
parameter-free, $G$-free** result obtained by applying the *same* helical-jerk /
modular-Hamiltonian mechanism at the electron Compton scale. The electron's
orthogonal-jerk trajectory is a current loop whose magnetic moment is exactly
the Bohr magneton:

$$
\mu = I \cdot A = \frac{e\,\omega_e}{2\pi}\,\pi \lambda_{C,e}^2
   = \frac{e\hbar}{2 m_e} = \mu_B,
$$

using only $e$, $\hbar$, $m_e$, $c$ — every input independently measured, with
$G$ nowhere present and no fitted parameters or cosmic inputs. (Full treatment in
`DERIVE_EM.pdf`.)

The logic of this paper follows from that anchor: *the mechanism is validated
exactly and $G$-freely at the electron scale; what follows is what the same
mechanism implies for cosmic boundary conditions.* Gravity is an **application**
of a validated mechanism, not the primary evidence for it. The cosmic number in
§6 should be read in that light, and the genuinely falsifiable claims are
collected in §7.

---

## 1. Theoretical Foundation

The ansatz rests on five independent results from quantum field theory
and conformal field theory:

### 1.1 Bisognano-Wichmann Theorem (1975/1976)

The modular Hamiltonian for a half-space in relativistic QFT is the generator
of Lorentz boosts perpendicular to the entangling surface:

$$
K = 2\pi \int_{x>0} d^{d-1}x \; x \; T_{00}(x)
$$

This is a **theory-independent** result. It applies to any relativistic QFT,
interacting or free. The modular Hamiltonian is always a weighted integral of
the stress-energy tensor $T_{00}$, with the weight being the distance $x$ from
the entangling surface.

**Physical meaning:** Entanglement creates a boost-rotation geometry, not a
time-translation. The nucleon's spin faces ORTHOGONALLY to the displacement
toward the partner.

### 1.2 Casini-Huerta-Myers (2011)

For a spherical region of radius $R$ in a $d$-dimensional CFT, the modular
Hamiltonian is:

$$
K = 2\pi \int_{|\vec{x}|<R} d^{d-1}x \; \beta(r) \; T_{00}(\vec{x})
$$

where the weight function is:

$$
\beta(r) = \frac{R^2 - r^2}{2R}
$$

This is a parabola that vanishes at the boundary $r = R$ and is maximal at
the center $r = 0$. The result is derived by conformally mapping the ball to
a half-space and applying the BW theorem.

### 1.3 Cardy-Tonni (2016)

For an interval of length $l$ in 1+1D CFT, the entanglement Hamiltonian is
derived via conformal mapping from a punctured strip to an annulus:

$$
H_E = 2\pi \int_0^l dx \; \beta(x) \; T_{00}(x)
$$

where the inverse temperature profile is:

$$
\beta(x) = \frac{l}{\pi} \frac{\cos(\pi x_0/l) - \cos(\pi x/l)}{\sin(\pi x_0/l)}
$$

For the full interval ($x_0 = l/2$), $\cos(\pi/2) = 0$ and $\sin(\pi/2) = 1$, so:

$$
\beta(x) = -\frac{l}{\pi} \cos(\pi x/l)
$$

The energy scale is set by the inverse of the interval length: $E \sim \hbar c/l$.

### 1.4 Bernard et al. (2024)

The modular Hamiltonian for inhomogeneous free-fermion chains has a commuting
operator $T_A$ whose eigenvalues approximate the entanglement spectrum:

$$
\epsilon_k = \frac{2\pi \lambda_k}{\text{scale} \cdot N^2}
$$

For the Racah chain (most general case), the inverse temperature $\beta(x)$
is parabolic. When the filling fraction is low ($\rho \ll 1/2$), the active
region of the Fermi velocity is small and concentrated near the boundary.
The modular Hamiltonian weight on this region is quadratic to leading order:

$$
\beta(r) = (1 - r/R)^2
$$

This $(1-r/R)^2$ form is established for *specific integrable free-fermion
chains* as the leading term in the low-filling limit; it is not a general
theorem about arbitrary low-density states. Carrying it over to the cosmic
ensemble requires the separate (and unproven) identification discussed in §3.1
— "$\Omega_b \approx 0.049$ is small" is necessary but not sufficient
justification.

Reference: Bernard et al., "Entanglement Hamiltonian and orthogonal polynomials,"
arXiv:2412.12021 (2024), published in Nuclear Physics B (2025).

### 1.5 Huerta & van der Velde (2023-2024)

The modular Hamiltonian for a spherical region in $d$-dimensional CFT can be
obtained by dimensional reduction to the radial semi-infinite line. When a
$d$-dimensional free massless field is decomposed into angular modes, the
modular Hamiltonian decomposes as:

$$
K = \sum_{\ell, \vec{m}} K_{\ell, \vec{m}}
$$

where each mode contribution $K_{\ell, \vec{m}}$ is **exactly** the dimensional
reduction of the parent CFT modular Hamiltonian. The weight function $\beta(r)$
is **preserved** under dimensional reduction.

Critically, the 1D reduced theories are **non-conformal** (they carry a
$1/r^2$ potential from the angular Laplacian), yet their modular Hamiltonian
remains local in the energy density with the **same weight function** as the
$d$-dimensional CFT. This is proven for both scalar fields and Dirac fermions.

References:

- M. Huerta & G. van der Velde, JHEP 06 (2023) 097, arXiv:2301.00294
- M. Huerta & G. van der Velde, arXiv:2307.08755

---

## 2. The Bond Energy $E_{\text{bond}} = \hbar c / r$

### 2.1 Dimensional Analysis

The modular Hamiltonian $K$ is dimensionless (it appears in $\rho_A = e^{-K}/Z$).
The weight $\beta$ has dimensions $[L]$ (boost parameter = proper distance).
The energy density $T_{00}$ has dimensions $[E]/[L]^d$. The volume element
$d^d x$ has dimensions $[L]^d$.

$$
K = 2\pi \int d^d x \; \beta(x) \; T_{00}(x)
$$

The integral has dimensions $[L]^d \cdot [L] \cdot [E]/[L]^d = [E] \cdot [L]$.
For $K$ to be dimensionless:

$$
\frac{[E] \cdot [L]}{\hbar c} = \text{dimensionless} \implies E \sim \frac{\hbar c}{L}
$$

This is the universal scaling: the entanglement energy between two subsystems
at separation $L$ is $\hbar c/L$, up to a dimensionless coefficient.

**Region entanglement vs. pairwise bonds (a genuine leap).** The modular
Hamiltonian describes the entanglement of a *region* with its *complement* — it
is not, on its face, a sum of pairwise bonds between particles. The derivation
below (§§4–5) nonetheless decomposes the cosmic entanglement into pairwise terms
$C\,\kappa\hbar c/r$ summed over nucleon pairs. That decomposition is an
*assumption*, not a theorem: it is the ansatz that the region-level modular
structure can be repackaged as additive two-body bonds with the same $\hbar c/r$
scaling. It is plausible for a dilute, weakly-correlated ensemble, but it is not
derived from the modular Hamiltonian.

### 2.2 Why Free Fermions Apply to Nucleons

The Bernard et al. calculation works with free fermions. Nucleons interact via
the strong force. Why does the free fermion result apply?

1. **BW theorem is theory-independent:** The modular Hamiltonian structure
   $K = 2\pi \int \beta T_{00}$ applies to ANY relativistic QFT, interacting
   or free. The specific form of $T_{00}$ does not change the local structure.

2. **Dimensional analysis is theory-independent:** The scaling $E \sim \hbar c/L$
   depends only on the dimensions of $T_{00}$ and $\beta$, which are universal.

3. **Bernard et al. is a verification, not an assumption:** It confirms the
   universal structure in a concrete solvable model.

4. **EFT argument (with a caveat):** The long-wavelength behavior is controlled
   by the effectively massless low-energy sector, and the $1/r$ scaling depends
   only on dimensions. But integrating out QCD does *not* turn nucleons into free
   fermions — they remain massive composite particles with residual
   interactions. The free-fermion modular Hamiltonian is used as a tractable
   *model* of the low-filling sector (justified by points 1–2, where structure
   and scaling are theory-independent), not as a claim that nucleons are
   literally non-interacting.

5. **Cross-check:** At the nucleon scale ($r \sim 1$ fm), $\hbar c/r \sim 200$ MeV,
   matching $\Lambda_{\text{QCD}}$. This agreement at both nucleon and cosmic
   scales is independent confirmation.

### 2.3 Numerical Verification

| Scale | $r$ | $E_{\text{bond}} = \hbar c/r$ | Physical interpretation |
|-------|-----|-------------------------------|-------------------------|
| Nucleon | 1 fm | $3.2 \times 10^{-11}$ J (200 MeV) | Strong force scale ($\Lambda_{\text{QCD}}$) |
| Earth | 6371 km | $5.0 \times 10^{-33}$ J | $3.1 \times 10^{-14}$ eV |
| Cosmic | $4.4 \times 10^{26}$ m | $7.2 \times 10^{-53}$ J | Gravitational binding scale |

---

## 3. The Geometric Factor $\gamma = 4/5$

### 3.1 The 1D Racah Chain Result

The cosmic filling fraction is $\rho = \Omega_b = 0.049$ (the baryon fraction).
In the Racah chain framework, this maps to parameters:

$$
x_1 = \frac{\Omega_{\text{DM}}}{\Omega_b} = 5.47, \quad x_2 = \frac{\Omega_{\text{DE}}}{\Omega_b} = 13.94, \quad x_3 = \frac{\Omega_{\text{DM}}}{\Omega_{\text{DE}}} = 0.39
$$

The Fermi velocity $v_F(x)$ is non-zero only on the active region
$[x_-, x_+] = [0.868, 1.000]$, a narrow band near the boundary.
The modular Hamiltonian weight on this region is quadratic:

$$
\beta_{\text{1D}}(x) = (1 - x/L)^2
$$

**The load-bearing conjecture.** Everything downstream depends on one
identification that is *assumed*, not derived: that the cosmic reduced density
matrix is well-approximated by a **low-filling free-fermion (Racah-chain)
state**, with filling fraction set by the baryon fraction
$\rho = \Omega_b \approx 0.049 \ll 1/2$. This is the single physics step that
selects the low-filling weight $(1 - r/R)^2$ — and hence $\gamma = 4/5$ — over
the vacuum weight, which would give $16/15$ (§3.3). We do not derive it from
first principles; it is the conjecture on which the whole result rests and where
the argument is most vulnerable. It decomposes into three separate, individually
unproven leaps:

1. *Why fermionic?* The cosmic reduced density matrix contains bosons (photons,
   gluons, Higgs, gravitons) as well as fermions; we have no argument for why a
   free-*fermion* model should approximate its modular Hamiltonian.
2. *Why $\Omega_b$ sets the filling?* The matter fraction
   $\Omega_m \approx 0.31$ (also below $1/2$) or another parameter would be at
   least as defensible; the specific mapping to the Racah parameters
   $x_1, x_2, x_3$ is not derived.
3. *Why the Racah chain?* It is the most general *integrable* free-fermion
   chain, but the universe is not an integrable spin chain; we do not justify
   integrability at cosmic scales beyond tractability.

- *What would support it:* a derivation of why the cosmic ensemble is fermionic
  and low-filling, why $\Omega_b$ (rather than $\Omega_{\text{total}}$) sets the
  filling, and a check that the active band $[x_-, x_+]$ follows from $\rho$ with
  no further input.
- *What would falsify it:* improved cosmic parameters that drive the consistent
  prefactor away from $4/5$ toward $16/15$ or the Schwarzschild $1/2$.

### 3.2 The 3+1D Extension

The Huerta & van der Velde theorem proves that the 1D modular Hamiltonian
on the radial line is the dimensional reduction of the $d$-dimensional sphere.
The weight function $\beta(r)$ is **preserved** under dimensional reduction.

In 3+1D, the spherical volume element $r^2 dr$ modifies the weighted average.
The weighted average of $1/r$ with the quadratic weight is:

$$
\left\langle \frac{1}{r} \right\rangle_{\text{3D}} = \frac{\int_0^R \beta(r) \cdot r \, dr}{\int_0^R \beta(r) \cdot r^2 \, dr}
$$

For $\beta(r) = (1 - r/R)^2$:

**Numerator:**

$$
\int_0^R (1 - r/R)^2 \cdot r \, dr = R^2 \int_0^1 u^2(1-u) \, du = R^2 \left(\frac{1}{3} - \frac{1}{4}\right) = \frac{R^2}{12}
$$

**Denominator:**

$$
\int_0^R (1 - r/R)^2 \cdot r^2 \, dr = R^3 \int_0^1 u^2(1-u)^2 \, du = R^3 \left(\frac{1}{3} - \frac{1}{2} + \frac{1}{5}\right) = \frac{R^3}{30}
$$

**Result:**

$$
\left\langle \frac{1}{r} \right\rangle = \frac{R^2/12}{R^3/30} = \frac{5}{2R}
$$

The geometric factor is:

$$
\gamma = \frac{2}{\langle 1/r \rangle \cdot R} = \frac{2}{5/2} = \frac{4}{5}
$$

**Origin of the factor 2.** The normalization in $\gamma = 2/(\langle 1/r \rangle R)$
is not an arbitrary choice: the factor of 2 is the inverse of the pairwise-counting
factor $1/2$ in the energy balance of Step E (§5). There the total entanglement
energy sums over the $N_{\text{universe}}^2/2$ distinct nucleon pairs,
$E_{\text{ent}} = \tfrac{1}{2} N_{\text{universe}}^2 \, C \, \kappa \hbar c \, \langle 1/r \rangle$.
Equating to $M_{\text{universe}} c^2$ and solving for the coupling carries that
$1/2$ into the denominator, so the prefactor multiplying $c^2 R / M_{\text{universe}}$
is $1/(\tfrac{1}{2}\langle 1/r \rangle R) = 2/(\langle 1/r \rangle R) = \gamma$.
In other words $\gamma$ is *defined by* and *identical to* the prefactor produced
by the Step-E energy balance; §3.2 is a preview of that result. The only
genuinely independent input is the weighted mean $\langle 1/r \rangle = 5/(2R)$,
which follows from the quadratic weight $\beta(r) = (1 - r/R)^2$.

### 3.3 The Discrete Dichotomy: $4/5$ vs $16/15$

The relevant question is not "what continuous exponent $a$ fits $G$?" but
"which of the two *physically admissible* universal CFT weights describes the
cosmic ensemble?" Conformal field theory supplies exactly two candidate weight
functions for a spherical region, and they give two discrete, parameter-free
prefactors.

**Vacuum regime (Casini–Huerta–Myers).** The vacuum modular weight is the
parabola $\beta(r) = (R^2 - r^2)/2R$ (§1.2). Then

$$
\left\langle \frac{1}{r} \right\rangle_{\text{vac}}
= \frac{\int_0^R \beta\, r\, dr}{\int_0^R \beta\, r^2\, dr}
= \frac{R^3/8}{R^4/15} = \frac{15}{8R},
\qquad
\gamma_{\text{vac}} = \frac{2}{\langle 1/r \rangle R} = \frac{16}{15} \approx 1.067.
$$

**Low-filling regime (Bernard et al. / Racah chain).** At low filling fraction
the active weight is $\beta(r) = (1 - r/R)^2$ (§1.4), giving
$\langle 1/r \rangle = 5/(2R)$ and $\gamma = 4/5 = 0.800$ (§3.2).

| Regime | weight $\beta(r)$ | $\langle 1/r \rangle R$ | $\gamma$ | $G$ vs measured |
|--------|-------------------|-------------------------|----------|-----------------|
| Vacuum CHM | $(R^2 - r^2)/2R$ | $15/8$ | $16/15$ | $+33\%$ |
| **Low-filling Racah** | $(1 - r/R)^2$ | $5/2$ | $\mathbf{4/5}$ | $+0.2\%$ |

These are **discrete** alternatives, not a tuned continuum: the prediction is a
choice between two universal regimes, and the data selects the low-filling one.
The prefactors differ by a factor $\tfrac{16}{15} \div \tfrac{4}{5} = \tfrac{4}{3}$,
so the vacuum regime overshoots $G$ by 33% — far outside cosmic-parameter
uncertainty. The load-bearing physics is therefore the *regime identification*
(§3.1), not a fit; given that identification, $4/5$ is forced.

A continuous scan over $\beta = (1 - r/R)^a$ gives the closed form
$\gamma(a) = 4/(a+3)$ (so $a=2 \Rightarrow 4/5$), which is indeed sensitive near
$a=2$. But that scan is only illustrative: the physics admits the two discrete
weights above, not an arbitrary exponent.

---

## 4. The Mechanism

### 4.1 Obligation-to-Entangle

Every nucleon has an obligation to entangle with every other nucleon. The
angular momentum budget per nucleon is:

$$
s = \frac{\sqrt{3}}{2} \hbar
$$

This budget is allocated across $N_{\text{universe}}$ partners, with the
allocation following the modular Hamiltonian structure ($\hbar c/r$).

### 4.2 Torque Geometry

The BW theorem shows that the modular flow is a boost rotation, not a time
translation. The nucleon's spin faces ORTHOGONALLY to the displacement toward
the partner. This is the "torque geometry" of entanglement.

### 4.3 Unresolved Entanglement

When the coupling fraction between two particles is far below unity, the pair
has not collapsed to a definite correlation. The entanglement amplitude
still exists but remains unresolved. For gravity, the coupling fraction is
$\alpha_{\mathrm{grav}} \approx 5.9 \times 10^{-39}$, so essentially all
nucleon pairs are in this unresolved regime.

This is not zero force. The unresolved amplitude carries the cosmic
entanglement field: each nucleon is entangled with $N_{\mathrm{universe}}$
other nucleons. The balance of angular momentum is the rest of the universe.
In QFT language, this is the reduced density matrix obtained by tracing out
the complement. The universe's isotropic entanglement field is the baseline;
any local mass breaks the isotropy.

### 4.4 Gravity as Anisotropy

The boost rotation back toward the mass is the gravitational force. Gravity
is not a fundamental force -- it is the anisotropy in the cosmic entanglement
field created by local mass concentrations.

---

## 5. The Ansatz

### Step A: Angular Momentum Budget

Each nucleon has angular momentum $s = \sqrt{3}/2 \cdot \hbar$.

### Step B: Entanglement Bond Energy

From the modular Hamiltonian (Sections 1-2):

$$
E_{\text{bond}} = \kappa \frac{\hbar c}{r}
$$

where $\kappa$ is the geometric coefficient (order unity).

### Step C: Torque Geometry

The BW theorem shows the modular flow is a Lorentz boost. The nucleon faces
orthogonally to the displacement toward the partner.

### Step D: Cosmic Balance

The isotropic background cancels. Only anisotropy remains.

### Step E: Coupling Fraction from Energy Balance

The coupling fraction $C$ (entanglement strength per pair) is determined by the
total entanglement energy of the universe. The universe's mass-energy is stored
as entanglement energy across all nucleon pairs:

$$
E_{\text{entanglement}} = \frac{N_{\text{universe}}^2}{2} \cdot C \cdot \kappa \hbar c \cdot \left\langle \frac{1}{r} \right\rangle
$$

where $\langle 1/r \rangle = 5/(2R_{\text{universe}})$ from the quadratic weight.
Equating to the universe's mass-energy $M_{\text{universe}} c^2$:

$$
\frac{N_{\text{universe}}^2}{2} \cdot C \cdot \kappa \hbar c \cdot \frac{5}{2R} = M_{\text{universe}} c^2
$$

**This is a constraint, not a dynamical law.** This equality is the weakest step
in the chain: it is *imposed* ("the universe's mass-energy equals its total
pairwise entanglement energy"), not derived from an equation of motion. It is in
the spirit of holographic equipartition, but we do not derive it. A reader who
does not grant the matching condition does not get $C$ or the force law that
follows; supplying its dynamical justification is part of the open problem (§8).

Solving for $C$ and substituting $N_{\text{universe}} = M_{\text{universe}}/m_p$:

$$
C = \frac{4}{5} \frac{m_p^2 c R_{\text{universe}}}{\kappa M_{\text{universe}} \hbar}
$$

### Step F: G Emerges

The force per nucleon pair is:

$$
F_{\text{pair}} = C \cdot \kappa \frac{\hbar c}{r^2}
$$

The total force between two test masses $M$ and $m$ at distance $r$ (these
are local masses, distinct from the cosmic $M_{\text{universe}}$ that enters
through $C$):

$$
F = \frac{M}{m_p} \cdot \frac{m}{m_p} \cdot C \cdot \kappa \frac{\hbar c}{r^2}
$$

Substituting $C$:

$$
F = \frac{4}{5} \cdot M \cdot m \cdot \frac{c^2 R_{\text{universe}}}{M_{\text{universe}}} \cdot \frac{1}{r^2}
$$

Comparing to Newton's law $F = G \cdot M \cdot m / r^2$:

$$
G = \frac{4}{5} \frac{c^2 R_{\text{universe}}}{M_{\text{universe}}}
$$

**Note:** $\hbar$, $m_p$, and $\kappa$ all cancel. The final expression depends
only on $c$, $R_{\text{universe}}$, and $M_{\text{universe}}$.

---

## 6. Numerical Result

Using:

- $c = 2.998 \times 10^8$ m/s
- $R_{\text{universe}} = 4.4 \times 10^{26}$ m
- $M_{\text{universe}} = 4.73 \times 10^{53}$ kg (total, including dark matter and dark energy)

$$
G_{\text{derived}} = \frac{4}{5} \frac{(2.998 \times 10^8)^2 \cdot (4.4 \times 10^{26})}{4.73 \times 10^{53}} = 6.688 \times 10^{-11} \text{ m}^3/(\text{kg}\cdot\text{s}^2)
$$

$$
G_{\text{measured}} = 6.674 \times 10^{-11} \text{ m}^3/(\text{kg}\cdot\text{s}^2)
$$

$$
\frac{G_{\text{derived}}}{G_{\text{measured}}} = 1.0021
$$

The numerical agreement is within 0.21%. As emphasized in the Scope note,
this is *not* an independent measurement of $G$: the cosmic inputs
$R_{\text{universe}}$ and $M_{\text{universe}}$ are themselves fixed within
general-relativistic cosmology and carry $G$ implicitly (the critical-density
condition forces $M/R$). The match should therefore be read as a Mach–Sciama
consistency check at the cosmic scale, with the substantive content being the
predicted prefactor $4/5$ and the mechanism, not the numerical value of $G$.

### 6.1 Error Budget

The central value should be quoted with the uncertainty propagated from its
cosmic inputs, not as a bare $0.21\%$:

$$
\frac{\delta G}{G} = \sqrt{\left(\frac{\delta R}{R}\right)^2 + \left(\frac{\delta M}{M}\right)^2}.
$$

Two very different uncertainties matter:

- **Measurement uncertainty (definitions of $R$, $M$ fixed).** With the
  particle-horizon radius and the critical-density mass at Planck-level
  precision, $\delta R/R \sim 2\%$ and $\delta M/M \sim 3\%$, giving
  $\delta G/G \sim 4\%$, i.e. $G_{\text{derived}} = (6.7 \pm 0.3)\times10^{-11}$.
  The measured value sits comfortably inside this band — but the band is
  $\sim 20\times$ wider than the $0.21\%$ central offset, so the agreement is a
  *consistency*, not a precision test.
- **Definitional uncertainty (which $R$, which $M$).** This dominates and is far
  larger. Hubble radius vs. particle horizon moves $R$ by tens of percent;
  baryonic, matter ($1.5\times10^{53}$ kg), or total energy ($4.7\times10^{53}$
  kg) moves $M$ across an order of magnitude (see the honest $G$-free census in
  §6.2). The prefactor lands on $4/5$ only for one mutually consistent
  critical-density choice — which is exactly the Mach–Sciama statement, and
  exactly why this is not an independent measurement of $G$.

The honest reading: $4/5$ is the prediction; the sub-percent central match is
fortuitous given the input uncertainties; and the substantive falsifiable
content is the discrete $4/5$-vs-$16/15$ choice (§3.3) and the $G$-free
electron-scale test (the Empirical Anchor, §7.1).

### 6.2 A Fully $G$-Free Evaluation

We can feed the formula *only* inputs obtainable without $G$: a radius from
expansion kinematics, and a baryonic mass from CMB photon-counting ($n_\gamma$
from the blackbody temperature) times the BBN baryon-to-photon ratio $\eta$. An
honest baryon census in the particle-horizon volume gives
$M_b \approx 1.5\times10^{53}$ kg — about $6\times$ larger than the
$\Omega_b \times M_{\text{universe}}$ figure, which silently inherits the
back-fit total.

| $R$ (G-free) | $M$ (G-free) | $G_{\text{pred}}/G_{\text{meas}}$ |
|---|---|---|
| Hubble radius $c/H_0$ (14.5 Gly) | baryon census (CMB+BBN) | $32.6$ |
| Particle horizon (46.5 Gly) | baryon census (CMB+BBN) | $3.2$ |

So purely $G$-free inputs land within a factor of $\sim 3$ — **not** the factor
of $\sim 20$ a naive $\Omega_b$ scaling suggests. A clean analytic check
sharpens the point: at the Hubble radius and critical density, $c^2R/M = 2G$
identically, so the $4/5$ prefactor gives *exactly* $G_{\text{pred}} =
\tfrac{8}{5}G = 1.600\,G$, overshooting the textbook Mach–Sciama coefficient
$1/2$ by $8/5$. The $0.21\%$ match is recovered only by pairing the particle
horizon ($\sim 3.2\times$ larger than the Hubble radius) with the
gravitationally inferred total mass. No purely $G$-free $(R, M)$ pair reproduces
measured $G$; the closest is within $\sim 3\times$. These evaluations are
reproduced in `gfree_inputs.py`.

---

## 7. Predictions and Falsifiability

We separate genuinely falsifiable, input-independent predictions from
qualitative or order-of-magnitude consequences, and label each honestly.

### 7.1 Exact, $G$-free prediction: the Bohr magneton

The sharpest falsifiable claim. The same mechanism applied at the electron
Compton scale predicts the electron magnetic moment *exactly*,
$\mu = e\hbar/2m_e = \mu_B = 9.274\times10^{-24}$ J/T, with no fitted parameters
and no $G$ (Empirical Anchor; `DERIVE_EM.pdf`). Any departure of the
Dirac-level moment from $e\hbar/2m_e$ would falsify the mechanism at its
cleanest point; none exists.

### 7.2 Discriminating prediction: the cosmic prefactor is $4/5$, not $16/15$

The mechanism predicts a *discrete* prefactor selected by the cosmic ensemble's
CFT regime (§3.3): $4/5$ (low-filling) versus $16/15$ (vacuum) — a $33\%$ split.
This is falsifiable with improved cosmology: as $R_{\text{universe}}$ and
$M_{\text{universe}}$ tighten, the consistent prefactor must converge on $4/5$.
Convergence toward $16/15$ or the naive Schwarzschild $1/2$ would falsify the
low-filling identification.

### 7.3 $G$-free cross-check: bond energy at the nucleon scale

The bond energy $E_{\text{bond}} = \hbar c/r$ (§2) evaluated at the nucleon
radius $r \approx 1$ fm gives $\approx 200$ MeV, matching $\Lambda_{\text{QCD}}$
— a numeric, $G$-free cross-check at a scale $\sim 40$ orders of magnitude from
the cosmic one.

### 7.4 Gravitational coupling (restatement, not independent)

$\alpha_{\text{grav}} = C = 5.9 \times 10^{-39}$ equals $G m_p^2/\hbar c$; it is
a re-expression of the cosmic balance, not an independent test.

### 7.5 Frame dragging (qualitative)

The boost-generator structure (BW theorem) implies rotating masses drag the
local entanglement field (Lense–Thirring). At present this is structural only: a
compactness-based estimate is off by $\sim 3\times10^3$ (`DERIVE_EM.pdf` §9.7),
so it is not yet a quantitative prediction.

### 7.6 Dark energy (order-of-magnitude)

The unresolved cosmic entanglement field gives
$\rho_{\text{DE}} \approx 8.1 \times 10^{-11}$ J/m$^3$, the right order of
magnitude but $\sim 8\times$ below the measured
$\rho_\Lambda \approx 6.9 \times 10^{-10}$ J/m$^3$ — a consistency check, not a
match.

---

## 8. Toward a Local Derivation

The cosmic match is a one-scale consistency check precisely because the inputs
$R_{\text{universe}}$, $M_{\text{universe}}$ carry $G$ implicitly. The way to
remove the circularity is a *local* derivation in the spirit of the
Jacobson–Padmanabhan–Verlinde program, in which $G$ is fixed by a locally
computable entanglement bond density rather than by cosmic boundary values.

**The target relation.** Jacobson (1995) derives the Einstein equations from the
Clausius relation $\delta Q = T\,\delta S$ on local Rindler horizons, with the
Unruh temperature $T = \hbar a/2\pi k_B c$ and an entropy proportional to horizon
area, $S = \eta\, k_B\, \mathcal{A}$. Newton's constant then emerges as

$$
G = \frac{c^3}{4 \hbar\, \eta},
$$

where $\eta$ is the **entanglement entropy per unit horizon area** (bonds per
unit area). In this language, a local derivation of $G$ is exactly a calculation
of $\eta$ from the modular Hamiltonian — *without* using $G$ as an input.

**What the present mechanism contributes.** The same ingredients that fix the
cosmic prefactor have local analogues that should determine $\eta$:

1. the bond energy $E_{\text{bond}} = \kappa\,\hbar c/r$ (§2), the energy per
   entanglement link crossing the horizon;
2. the modular weight $\beta(r)$ (§1), which sets how links are distributed with
   proper distance from the entangling surface;
3. the torque/boost geometry (BW theorem), which fixes the orthogonal projection
   that survives the isotropic average.

**A concrete attempt (and where it fails).** To make the gap concrete rather
than a sketch, take the area law $S = \eta\,k_B\,\mathcal{A}$ and suppose the
horizon is threaded by entanglement links each carrying $\sim k_B \ln 2$, with
areal density set by a single cutoff length $\ell$, so $\eta \sim \ln 2/\ell^2$.
Then $G = c^3/(4\hbar\eta)$ gives $G \sim c^3\ell^2/(4\hbar\ln 2)$, and demanding
the measured $G$ *fixes the cutoff* at

$$
\ell^2 \sim \frac{4\hbar G \ln 2}{c^3} = 4\ln 2\,\ell_P^2
\quad\Longrightarrow\quad \ell \sim \ell_P = \sqrt{\hbar G/c^3}.
$$

This is exactly where it breaks: getting the right $G$ requires the link density
to be the Planck density, but $\ell_P$ contains $G$ by definition. We have not
computed $\eta$ from $G$-free inputs; we have re-expressed $G$ via a cutoff that
already encodes it — the same circularity that defeats the
Jacobson–Padmanabhan–Verlinde programs at the area-law coefficient. A genuine
derivation needs an independent, $G$-free determination of $\ell$ or $\eta$
(e.g. a finite, regulator-independent entanglement entropy density of the
relevant QFT), which we do not have. Neither does anyone else. It is the central open problem. The honest status of this paper
is: *given a mechanism that is exact and $G$-free at the electron scale (the
Empirical Anchor) and that fixes the cosmic prefactor (§§3–6), the missing piece
is the local bond density $\eta$ that would turn the cosmic consistency check
into a derivation.*

---

## 9. References

1. J. J. Bisognano and E. H. Wichmann, "On the duality condition for a
   Hermitian scalar field," J. Math. Phys. 16 (1975) 985.
2. J. J. Bisognano and E. H. Wichmann, "Computation of the algebra of
   local observables for the quantized free Dirac field in a wedge-shaped
   region," J. Math. Phys. 17 (1976) 303.
3. H. Casini, M. Huerta, and R. C. Myers, "Towards a derivation of
   holographic entanglement entropy," JHEP 05 (2011) 036, arXiv:1102.0440.
4. J. Cardy and E. Tonni, "Entanglement hamiltonians in two-dimensional
   conformal field theory," J. Stat. Mech. 1612 (2016) 123103,
   arXiv:1608.01283.
5. D. Bernard et al., "Entanglement Hamiltonian and orthogonal polynomials,"
   arXiv:2412.12021, published in Nuclear Physics B (2025).
6. M. Huerta and G. van der Velde, "Modular Hamiltonian of the scalar in
   the semi infinite line: dimensional reduction for spherically symmetric
   regions," JHEP 06 (2023) 097, arXiv:2301.00294.
7. M. Huerta and G. van der Velde, "Modular Hamiltonian in the semi infinite
   line, Part II: dimensional reduction of Dirac fermions in spherically
   symmetric regions," arXiv:2307.08755.

---

## 10. Computational Verification

All derivations are implemented in Python scripts:

- `derive_G.py` -- Main cosmic-Mach-Sciama prefactor calculation (752 lines)
- `derive_bond_energy.py` -- $E_{\text{bond}} = \hbar c/r$ derivation (420 lines)
- `derive_3d_extension.py` -- 3+1D extension via Huerta & van der Velde (350 lines)
- `verify_symbolic.py` -- Symbolic (`sympy`) proof of the $\langle 1/r \rangle$
  integrals, the discrete $4/5$ vs $16/15$ prefactors, and the Step A–F algebra
  (showing $\hbar$, $m_p$, $\kappa$ cancel exactly)
- `gfree_inputs.py` -- Evaluates the prefactor on purely $G$-free inputs
  (expansion-kinematics radii; CMB+BBN baryon census), quantifying the circularity
- `constants.py` -- Physical constants and helper functions

All scripts run cleanly and produce consistent results. The symbolic check makes
the core arithmetic exact rather than numerical: run `python3 verify_symbolic.py`.
