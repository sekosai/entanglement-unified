# Forces from Entanglement

An entanglement-torque mechanism applied across all four fundamental forces. The cleanest empirical leg is an exact derivation of the Bohr magneton at the electron scale; the rest is a mix of consistency checks, structural matches, and explicit sketches.

## What this is, and is not

**This is not a free derivation of Newton's constant `G`.** A relation of the form `G ~ c²R/M` is the well-known Mach–Sciama identity; it follows from the Friedmann equation and contains `G` implicitly through the cosmic inputs. What we add is a specific predicted prefactor, `γ = 4/5`, derived from the modular Hamiltonian of free fermions on a Racah chain at low filling fraction. Combined with the standard cosmic parameters, this is consistent with the measured `G` to within current parameter uncertainties (≈5–10% on `R_universe` and `M_universe`).

**The clean empirical test is the Bohr magneton.** Applied at the electron scale, the same helical-jerk mechanism reproduces `μ_B = eℏ/(2mₑ)` exactly, with no fitted parameters and no `G`. This is the strongest empirical leg of the program.

**The other forces are sketches.** The weak and strong sectors are structurally parallel but quantitatively dependent on inputs (W mass, QCD scale) that are themselves measured rather than derived. Mass generation, charge quantization, and frame dragging are organizational analogies or open problems, not quantitative predictions, and the documents say so explicitly.

## Documents

| Document | Description |
|----------|-------------|
| [DERIVATION.pdf](DERIVATION.pdf) | Entanglement mechanism for the Mach–Sciama relation, with predicted prefactor 4/5. Includes a Circularity and Scope section. |
| [DERIVE_EM.pdf](DERIVE_EM.pdf) | Bohr magneton from helical-jerk geometry: a `G`-free test of the same mechanism. |
| [UNIFIED.pdf](UNIFIED.pdf) | Sketch across all four forces, with explicit limitations. |

## Source

| File | Description |
|------|-------------|
| `DERIVATION.tex` | LaTeX source for the gravity paper |
| `DERIVE_EM.tex` | LaTeX source for the EM paper |
| `UNIFIED.tex` | LaTeX source for the unified sketch |
| `references.bib` | BibTeX bibliography |
| `derive_G.py` | Main gravity calculation |
| `derive_bond_energy.py` | Bond energy `E = ℏc/r` from the modular Hamiltonian |
| `derive_3d_extension.py` | 3+1D extension via Huerta & van der Velde |
| `derive_unified.py` | Unified-theory companion script |
| `constants.py` | Physical constants |

## Compile

```bash
pdflatex DERIVATION.tex && bibtex DERIVATION && pdflatex DERIVATION.tex && pdflatex DERIVATION.tex
pdflatex DERIVE_EM.tex && pdflatex DERIVE_EM.tex && pdflatex DERIVE_EM.tex
pdflatex UNIFIED.tex && bibtex UNIFIED && pdflatex UNIFIED.tex && pdflatex UNIFIED.tex
```

## Run

```bash
python3 derive_G.py
python3 derive_bond_energy.py
python3 derive_3d_extension.py
python3 derive_unified.py
```

## Status

Active work-in-progress. Comments and disagreement welcome — particularly on the prefactor derivation, the EFT justification for applying free-fermion modular Hamiltonians at cosmic scales, and any proposal for a `G`-independent test of the `4/5` prefactor.
