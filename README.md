# Forces from Entanglement

A unified derivation of all four fundamental forces from the quantum entanglement structure of the vacuum.

## Documents

| Document | Description |
|----------|-------------|
| [DERIVATION.pdf](DERIVATION.pdf) | Derivation of Newton's constant G from cosmic entanglement (8 pages) |
| [DERIVE_EM.pdf](DERIVE_EM.pdf) | Electromagnetism from the same mechanism at the electron scale (6 pages) |
| [UNIFIED.pdf](UNIFIED.pdf) | All four forces: unified treatment (5 pages) |

## Source

| File | Description |
|------|-------------|
| `DERIVATION.tex` | LaTeX source for G derivation |
| `DERIVE_EM.tex` | LaTeX source for EM derivation |
| `UNIFIED.tex` | LaTeX source for unified theory |
| `references.bib` | BibTeX bibliography (7 entries) |
| `derive_G.py` | Main G derivation script |
| `derive_bond_energy.py` | Bond energy derivation |
| `derive_3d_extension.py` | 3+1D extension via Huerta & van der Velde |
| `derive_unified.py` | Unified theory: all four forces |
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
