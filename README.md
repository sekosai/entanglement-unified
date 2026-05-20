# Forces from Entanglement

An entanglement-torque mechanism applied across all four fundamental forces. The cleanest empirical leg is an exact derivation of the Bohr magneton at the electron scale; the rest is a mix of consistency checks, structural matches, and explicit sketches.

## What this is, and is not

**The clean empirical test is the Bohr magneton.** Applied at the electron Compton scale, the helical-jerk mechanism reproduces `μ_B = eℏ/(2mₑ)` exactly, with no fitted parameters and no `G`. Inputs are `e`, `ℏ`, `mₑ`, `c` — all measured independently to high precision. This is the strongest leg of the program and the only one where every input is `G`-free.

**The cosmic relation is *not* a local derivation of `G`.** A relation of the form `G ∼ c²R/M` is the well-known Mach–Sciama identity; it follows from the Friedmann equation and contains `G` implicitly through the cosmic inputs. We add a specific predicted prefactor, `γ = 4/5`, derived from the modular Hamiltonian of free fermions on a Racah chain at low filling fraction. Combined with the standard cosmic parameters, this is consistent with the measured `G` to within current parameter uncertainties — but evaluated on any local causal patch (e.g., Earth) the same formula gives `G_eff ∼ 10²⁶`, off by 36 orders of magnitude. So the cosmic match is a consistency check at the one scale where `M/R` is forced by the critical-density condition, not a local statement of `G`. The gravity paper makes this explicit.

**The other forces are sketches.** The weak and strong sectors are structurally parallel but quantitatively dependent on inputs (W mass, QCD scale) that are themselves measured rather than derived. Mass generation, charge quantization, and frame dragging are organizational analogies or open problems, not quantitative predictions, and the documents say so explicitly.

**The most important open problem.** A local derivation of `G` along the lines of the Jacobson–Padmanabhan–Verlinde program — i.e., Newtonian gravity from a local entanglement bond density `η` that is computable from QFT without `G` as an input. This would convert the cosmic relation from a one-scale consistency check into a derivation. We do not have it; nobody else has it either.

## Documents

| Document | Description |
|----------|-------------|
| [DERIVATION.pdf](DERIVATION.pdf) | Entanglement mechanism for the Mach–Sciama relation, with predicted prefactor 4/5. Includes a Circularity & Scope section, the Earth-as-patch local test, and a "Toward a Local Derivation" section. |
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
pdflatex UNIFIED.tex && pdflatex UNIFIED.tex
```

## Run

```bash
python3 derive_G.py
python3 derive_bond_energy.py
python3 derive_3d_extension.py
python3 derive_unified.py
```

## Status

Active work-in-progress. Comments and disagreement welcome — particularly on:

1. The prefactor `γ = 4/5` derivation from the Racah-chain modular Hamiltonian.
2. The EFT justification for applying free-fermion modular Hamiltonians at cosmic scales.
3. Any proposal for a local derivation of `G` that computes the entanglement bond density without using `G` as an input.

The Bohr magneton derivation is the empirical anchor. The rest is honest about what is sketch, what is consistency check, and what is genuinely open.
