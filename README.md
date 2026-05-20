# Forces from Entanglement

An entanglement-torque mechanism applied across all four fundamental forces. The cleanest empirical leg is an exact derivation of the Bohr magneton at the electron scale; the rest is a mix of consistency checks, structural matches, and explicit sketches.

## What this is, and is not

**The clean empirical test is the Bohr magneton.** Applied at the electron Compton scale, the helical-jerk mechanism reproduces `μ_B = eℏ/(2mₑ)` exactly, with no fitted parameters and no `G`. Inputs are `e`, `ℏ`, `mₑ`, `c` — all measured independently to high precision. This is the strongest leg of the program and the only one where every input is `G`-free.

**The cosmic relation is a boundary-condition statement, not a local law.** `G ∼ c²R/M` is the well-known Mach–Sciama identity. We add a specific predicted prefactor, `γ = 4/5`, derived from the Racah-chain modular Hamiltonian at low filling fraction — and we make the case that, conditional on identifying the cosmic ensemble with a low-filling fermionic state, the prefactor is *forced* (not fitted). The vacuum CHM weight, by contrast, gives `γ = 16/15`, which would be wrong by 33%. So `4/5` distinguishes between two universal CFT regimes; the cosmic regime identification is the load-bearing physics step.

Applied to any local causal patch (e.g., Earth) the same formula gives `G_eff ∼ 10²⁶`, off by 36 orders of magnitude. The right reading is *not* "the formula fails locally" but "the formula is a cosmic boundary-condition relation, not a local field equation." A local theory of gravity from the same mechanism would require a separate Jacobson–Padmanabhan–Verlinde-style derivation from local causal horizons. We don't have it; nobody else has it either, and we're explicit that this is the open problem.

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

1. The identification of the cosmic ensemble with a Racah-chain low-filling state. This is the load-bearing physics step that makes `γ = 4/5` forced rather than chosen. (The arithmetic from the weight to `4/5` is rigorous; the regime identification is the part that could be wrong.)
2. The EFT justification for applying free-fermion modular Hamiltonians at cosmic scales.
3. Any proposal for a local derivation of `G` that computes the entanglement bond density without using `G` as an input.

The Bohr magneton derivation is the empirical anchor — same mechanism, no `G`, no fitted parameters, no cosmic inputs, exact result. The gravity paper is best read as: *given the mechanism that produces the Bohr magneton, here is what it predicts about cosmic boundary conditions, and here is what would be needed to make it a local law.*
