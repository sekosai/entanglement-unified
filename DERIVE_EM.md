# The Bohr Magneton from Helical-Jerk Geometry: A G-Free Test

> **Authoritative version:** [`DERIVE_EM.pdf`](DERIVE_EM.pdf) is the canonical document. This markdown is an older draft; the PDF supersedes it on framing and scope.

## Abstract

The companion paper proposes an entanglement mechanism for the
Mach–Sciama relation $G \sim c^2 R/M$, but acknowledges that the
cosmic inputs are not independent of $G$ and the gravity calculation
is therefore a consistency check rather than a free derivation. Here
we apply the *same mechanism* at the electron scale, where every
input is independently measured and $G$ never appears. The mechanism
predicts that the electron's orthogonal jerk drives a helical
trajectory at the Compton scale, and that the magnetic moment of
this trajectory is exactly the Bohr magneton:

$$
\mu_B \;=\; \frac{e \hbar}{2 m_e}.
$$

This is an exact result with no fitted parameters. As a
$G$-independent test of the mechanism that powered the gravity paper,
it is a much cleaner check than the cosmological calculation. We
then discuss the parallel structure between gravity and
electromagnetism and the open question of why the per-pair couplings
differ by 36 orders of magnitude.

---

## 1. Parallel Structure

The same entanglement torque mechanism operates at both the nucleon and electron
mass scales. The underlying mechanism is identical: orthogonal jerk creates a
helical trajectory, the entanglement bond energy scales as $\hbar c/r$, and the
torque geometry follows from the Bisognano--Wichmann theorem.

| Property | Nucleon (gravity) | Electron (electromagnetism) |
|----------|-------------------|----------------------------|
| Mass | $1.673 \times 10^{-27}$ kg | $9.109 \times 10^{-31}$ kg |
| Compton wavelength | $1.321 \times 10^{-15}$ m | $2.426 \times 10^{-12}$ m |
| Compton frequency | $1.119 \times 10^{24}$ rad/s | $7.763 \times 10^{20}$ rad/s |
| Spin angular momentum | $\sqrt{3}/2 \cdot \hbar$ | $\sqrt{3}/2 \cdot \hbar$ |
| Coupling fraction | $\alpha_{\mathrm{grav}} \approx 5.9 \times 10^{-39}$ | $\alpha_{\mathrm{em}} \approx 7.297 \times 10^{-3}$ |
| Phase coherence | Random (thermal) | Aligned (ferromagnetic) |
| Bond energy | $\hbar c/r$ | $\hbar c/r$ |

The bond energy formula is identical. The coupling fraction differs by 36 orders of
magnitude.

---

## 2. The Force Ratio

The central numerical fact is the ratio of electromagnetic to gravitational force
between two protons:

$$
\frac{F_{\mathrm{em}}}{F_{\mathrm{grav}}}
= \frac{\alpha_{\mathrm{em}}}{\alpha_{\mathrm{grav}}}
= 1.24 \times 10^{36}
$$

This is the quantity that any unified theory must explain. Our mechanism
decomposes it into three components.

### 2.1 Mass ratio squared

The coupling fraction for a particle of mass $m$ scales as $m^2$ through the
Compton wavelength:

$$
\alpha_x = \left(\frac{\ell_{\mathrm{P}}}{\lambda_{\mathrm{C},x}}\right)^2
= \left(\frac{\ell_{\mathrm{P}} m_x c}{\hbar}\right)^2
$$

Therefore:

$$
\left(\frac{m_p}{m_e}\right)^2 = 3.40 \times 10^6
$$

This accounts for six orders of magnitude. The nucleon is heavier, so its
gravitational coupling fraction is proportionally larger in the mass-squared sense --
but the electron's electromagnetic coupling fraction is vastly larger, so there must
be additional factors.

### 2.2 Locus size ratio

The electron's Compton wavelength is 1836 times larger than the proton's:

$$
\frac{\lambda_{\mathrm{C},e}}{\lambda_{\mathrm{C},p}} = \frac{m_p}{m_e} = 1836
$$

The entanglement bond energy $\hbar c/r$ is stronger at smaller separations.
The larger electron locus means the bond extends further, but the per-pair
strength at a given distance is the same. The squared ratio:

$$
\left(\frac{\lambda_{\mathrm{C},e}}{\lambda_{\mathrm{C},p}}\right)^2
= \left(\frac{m_p}{m_e}\right)^2 = 3.40 \times 10^6
$$

This is the same factor as the mass ratio squared, since the Compton wavelength
is inversely proportional to mass.

### 2.3 Phase coherence factor

After accounting for the mass ratio squared, the remaining factor is:

$$
\mathcal{C}
= \frac{\alpha_{\mathrm{em}}/\alpha_{\mathrm{grav}}}{(m_p/m_e)^2}
= 1.84 \times 10^{29}
$$

This is the **phase coherence amplification factor**. It quantifies how much
stronger the effective coupling becomes when phases are aligned (ferromagnetic
ordering of electrons) versus random (thermal averaging of nucleons).

For aligned phases, the torque contributions add coherently:

$$
F_{\mathrm{aligned}} \propto N^2
$$

For random phases, they add incoherently:

$$
F_{\mathrm{random}} \propto N
$$

The coherence factor $\mathcal{C} \approx 1.8 \times 10^{29}$ is approximately
the square of the number of coherently aligned electrons in a typical
ferromagnetic domain.

---

## 3. The Helical Trajectory and the Bohr Magneton

The electron's orthogonal jerk creates a helical trajectory. This is the same
mechanism that produces the nucleon's helical trajectory, but at the electron
mass scale.

### 3.1 Helix parameters

The helical trajectory is characterized by:

$$
\omega_e = \frac{m_e c^2}{\hbar} = 7.763 \times 10^{20} \; \mathrm{rad/s}
$$

$$
\lambda_{\mathrm{C},e} = \frac{\hbar}{m_e c} = 2.426 \times 10^{-12} \; \mathrm{m}
$$

The angular momentum of the helix:

$$
L = m_e \lambda_{\mathrm{C},e} c = \hbar
$$

The helix carries exactly one unit of $\hbar$ angular momentum.

### 3.2 The Bohr magneton

The helical trajectory is a current loop. The current is:

$$
I = \frac{e}{T} = \frac{e \omega_e}{2\pi}
$$

The area of the loop is:

$$
A = \pi \lambda_{\mathrm{C},e}^2
$$

The magnetic moment is:

$$
\mu = I \cdot A
= \frac{e \omega_e}{2\pi} \cdot \pi \lambda_{\mathrm{C},e}^2
= \frac{e \omega_e \lambda_{\mathrm{C},e}^2}{2}
$$

Substituting $\omega_e = m_e c^2/\hbar$ and $\lambda_{\mathrm{C},e} = \hbar/(m_e c)$:

$$
\mu = \frac{e \cdot (m_e c^2/\hbar) \cdot (\hbar/(m_e c))^2}{2}
= \frac{e \hbar}{2 m_e}
= \mu_B
$$

**The Bohr magneton is the magnetic moment of the electron's helical jerk
trajectory.** This is an exact derivation with no free parameters.

---

## 4. Ferromagnetic Alignment

### 4.1 Exchange interaction as entanglement correlation

In ordinary matter, electron jerk directions are random. The torques cancel,
just as orthogonal components of gravitational torque cancel to leave only the
radial component.

In ferromagnetic materials (iron, nickel, cobalt), the exchange interaction
aligns electron spins. In the jerk picture, this means the orthogonal jerk
directions become aligned. The torques then add coherently rather than canceling.

The Pauli exclusion principle prevents two electrons from occupying the same
quantum state. In the jerk picture, this means two electrons cannot have the
same jerk-phase at the same position. When electrons are close (in a metal),
the lowest energy configuration is for their jerk-phases to be aligned. This
is the exchange interaction: **aligned jerk minimizes the entanglement energy**.

### 4.2 Curie temperature

Thermal energy disrupts the alignment:

$$
k_B T_C \approx E_{\mathrm{exchange}}
$$

For iron, $T_C = 1043$ K. Above this temperature, thermal jitter overcomes
the exchange alignment. The jerk directions randomize, and the material loses
its magnetic moment.

---

## 5. Maxwell's Equations from Jerk Conservation

The electromagnetic field is the jerk field. Maxwell's equations are the
conservation laws governing its flow.

### 5.1 Gauss's law for electricity

$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}
$$

Jerk has sources: charges are concentrations of aligned jerk-phase.

### 5.2 Gauss's law for magnetism

$$
\nabla \cdot \mathbf{B} = 0
$$

Jerk has no monopoles. The helical trajectory is a closed loop -- the jerk
must return to its starting phase. The torque field has no source or sink,
only circulation.

### 5.3 Faraday's law

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
$$

A changing jerk-phase creates an electric field. The time derivative of the
jerk circulation is the induced electromotive force.

### 5.4 Ampere--Maxwell law

$$
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
$$

Jerk flow (current) creates the magnetic field. The displacement current term
is the propagation of jerk-phase change at speed $c$.

---

## 6. Light as Propagating Jerk

An accelerating charge changes its jerk-phase. This change propagates at speed
$c$ -- the maximum speed of jerk-phase propagation. The propagating jerk-phase
change **is** the electromagnetic wave.

The photon is a quantum of propagating jerk:

$$
E_{\mathrm{photon}} = \hbar \omega
$$

This is the energy of one jerk-phase rotation.

---

## 7. Magnetic Dipoles and the Absence of Monopoles

Gravity is isotropic: all nucleon pairs contribute, random spin orientations
cancel to leave only the radial component. Electromagnetism is directional:
aligned spins create a preferred axis.

The aligned jerk creates a torque field:

$$
\boldsymbol{\tau}(\mathbf{r}) = \sum_i \mathbf{r}_i \times (\mathbf{S}_i \times \mathbf{r}_i) / |\mathbf{r}_i|^3
$$

When all $\mathbf{S}_i$ point in the same direction (ferromagnetic):

- Along the axis: torques add (strong attraction)
- Perpendicular to axis: torques partially cancel
- Opposite to axis: torques oppose (repulsion)

This creates the dipole field pattern. A monopole would require jerk that
spirals in only one direction everywhere. But the jerk is a third derivative
of position -- it must close on itself. The helical trajectory returns to its
starting phase. This is why $\nabla \cdot \mathbf{B} = 0$.

---

## 8. Numerical Summary

| Quantity | Value |
|----------|-------|
| $\alpha_{\mathrm{em}}$ | $7.297 \times 10^{-3}$ (1/137.036) |
| $\alpha_{\mathrm{grav}}$ | $5.906 \times 10^{-39}$ |
| Force ratio | $1.24 \times 10^{36}$ |
| $(m_p/m_e)^2$ | $3.40 \times 10^6$ |
| Phase coherence $\mathcal{C}$ | $1.84 \times 10^{29}$ |
| Bohr magneton $\mu_B$ | $9.274 \times 10^{-24}$ J/T |
| Electron Compton wavelength | $2.426 \times 10^{-12}$ m |
| Electron Compton frequency | $7.763 \times 10^{20}$ rad/s |

---

## 9. What Remains for a Unified Theory

The gravity derivation and the EM derivation share the same mechanism. To
unify them into a single coherent framework, the following gaps remain:

### 9.1 The phase coherence factor $\mathcal{C}$

The value $\mathcal{C} = 1.84 \times 10^{29}$ is currently a residual. It
should be derived from first principles -- specifically from the number of
coherently aligned electrons in a domain and the statistical mechanics of
phase alignment. A derivation of $\mathcal{C}$ would close the 36-order-of-
magnitude gap between gravity and electromagnetism.

### 9.2 The fine structure constant $\alpha_{\mathrm{em}}$ itself

We have explained $\alpha_{\mathrm{em}}/\alpha_{\mathrm{grav}}$ in terms of
mass ratios and phase coherence, but we have not derived $\alpha_{\mathrm{em}}$
from first principles. The value $1/137.036$ needs to emerge from the
entanglement structure at the electron scale, just as $\alpha_{\mathrm{grav}}$
emerges from the cosmic energy balance.

### 9.3 The weak and strong nuclear forces

The unified theory must account for all four fundamental forces. The weak
force operates at the $W/Z$ boson mass scale ($\sim 80-90$ GeV). The strong
force operates at the QCD scale ($\Lambda_{\mathrm{QCD}} \sim 200$ MeV). Each
requires identifying the relevant mass scale, coupling fraction, and phase coherence
structure.

### 9.4 Mass generation

Why do particles have the masses they do? The mechanism works at any mass
scale, but the specific values ($m_e$, $m_p$, $m_W$, etc.) are inputs rather
than outputs. A Higgs-like mechanism within the entanglement framework is
needed.

### 9.5 The geometric factor across forces

Gravity has $\gamma = 4/5$ from the Racah chain. Does electromagnetism have
a corresponding geometric factor? Is it the same? Different? The answer
depends on whether the modular Hamiltonian weight function $\beta(r)$ is
universal or force-dependent.

### 9.6 Quantization of charge

Why is charge quantized in units of $e$? The entanglement framework naturally
produces discrete angular momentum ($\hbar$), but charge quantization needs
a separate argument.

### 9.7 Frame dragging quantitative match

The frame dragging mechanism is structurally correct but off by a factor of
$\sim 3 \times 10^3$ in the compactness-based prediction. Closing this gap
requires a more precise treatment of how rotation creates the off-line
displacement $\delta\sigma$ at the nucleon level.

### 9.8 Resolution scale of the forces

At what resolution do the various forces become distinguishable?
Gravity is in the unresolved entanglement regime at all practical scales.
Electromagnetism resolves at a much higher energy scale. The weak and strong
forces need their own resolution scales.
