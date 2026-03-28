# Integration

## Project

Independent research paper arguing that LLM effectiveness reflects hierarchical multi-scale compression, and the autoregressive loop is fundamentally ambivalent (enriching vs stabilising regimes). Compression is the mechanism; **integration** is the thesis.

Ecological implications (feedback loops, silent flattening, surprisal leakage, carrier transition) are staged in `paper2/` for a companion piece.

## Status

Paper 1 is tightened to Sections 1–4 + Conclusion. Appendix A written. Tagged v0.7. Renders cleanly as HTML + PDF. GitHub Pages live (deploying from `publish` branch).

**Branching:** `main` is the working branch. `publish` tracks the latest released version (currently v0.7). Merge to `publish` when ready to update the live site.

**Version injection:** `paper/_version.py` runs as a Quarto pre-render script, writing `git describe` output to `_version.yml` and `_version.tex`. Version appears in the preface (both formats) and PDF page footer.

```
paper/
├── _quarto.yml                        ← render config (pre-render: _version.py)
├── _version.py                        ← generates _version.yml/.tex from git describe
├── integration.qmd                    ← main document (abstract, preface, includes all sections)
├── 01_compression_hierarchy.qmd       ← §1: rate-distortion, compression continuum, what transformers do
├── 02_structure_across_depth.qmd      ← §2: DPI resolution, statistical complexity, emergence thresholds
├── 03_autoregressive_loop.qmd         ← §3: channel capacity, enrichment fraction, figures
├── 04_grounding_alignment.qmd         ← §4: distortion measure decomposition, grounding, alignment
├── 05_conclusion.qmd                  ← conclusion: integration/accumulation, alignment, predictions, future
├── predictions.qmd                    ← single source of truth for all predictions
├── references.bib                     ← bibliography
├── cross-references.md                ← canonical IDs
├── appendix_formal_foundations.qmd    ← formal constructions (four sections)
├── figures.py                         ← figure generation from autoloop data
├── figure-spec.md                     ← data requirements for §3 figures
├── data/                              ← JSON data exports from autoloop
└── references.qmd

paper2/                                ← staging for companion piece
├── README.md                          ← scope and key concepts
├── 05_recursive_loop.qmd             ← ecology / feedback loops
├── 06_of_meaning.qmd                 ← meaning and integration
└── 07_surprisal_leakage.qmd          ← surprisal leakage, channel controllability, model asymmetry

drafts/                                ← discussion posts, outreach drafts
```

## Rendering

Requires: Python venv (`.venv/`), Quarto, TinyTeX. Setup for a fresh clone:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
quarto render paper       # outputs HTML + PDF to paper/docs/
```

Output goes to `paper/docs/` (HTML site + PDF). The `paper/docs/` directory is committed so that tagged versions always include a current render.

**Releasing:** Use `/release v0.X` to run the full tag-render-publish pipeline. The skill handles CLAUDE.md updates, tagging, rendering, tag-move, merge to `publish`, and push. See `.claude/skills/release/SKILL.md` for the full procedure.

## Writing principles

- Say what needs saying, then stop. One idea per paragraph.
- Show the seams: when a claim is novel, established, or speculative, say so.
- Earn every formal term at the moment it appears.
- No references to earlier drafts or revisions — the reader sees only this version.

## Key decisions

- **Formalism:** Main body uses info theory as precise vocabulary. Appendices carry the formal constructions. Rate-distortion in §1, DPI + statistical complexity in §2, channel capacity in §3. Distributed, not frontloaded.
- **Audience:** ML researchers, cognitive scientists, informed generalists. Clarity over gatekeeping; rigour available in appendices.
- **Scope:** Paper 1 covers compression and composition (the formally constrained core). Ecological dynamics (feedback loops, silent flattening, surprisal leakage, carrier transition, attention economy) deferred to paper 2.
- **Structure:** Flat sections (no Part I/II/III). Use "section" not "chapter" or "part" in all copy.
- **Terminology:** enriching/stabilising (not enriching/degrading). Enrichment fraction as continuous variable.
- **Human-AI collaboration** acknowledged in preface, stated plainly. CLAUDE.md is public.

## What's novel (handle with care)

### In Paper 1
- Autoregressive loop as sequential coding through bandwidth-limited channel
- Grounding problem as rate-distortion question
- Alignment as distortion measure mismatch; binding constraint is feedback *bandwidth* not quality
- Subtractive vs generative processing distinction (IB tracks what's discarded; this framework tracks what's generated)
- Predictive organisation (not geometric complexity) as the type of quantity that grows across depth; $C_\mu$ as canonical formalisation, commitment to family not specific measure

### Staged for Paper 2
- Four-loop feedback taxonomy (within-context, agentic, human-mediated, training-distributional)
- Silent flattening as named phenomenon with hierarchical erosion prediction
- Surprisal leakage: involuntary prediction error broadcast as feedback channel; controllability hierarchy; model asymmetry (perfect suppression by default)
- Processor-to-carrier transition framing
- Attention allocation as distortion measure selection; algorithmic capture as adaptive exploit at ecological scale

These have no clear precedent in the literature. Present as contributions, not established theory.

## Next steps

1. ~~**Prediction table.**~~ Done. Seven predictions with Status column.
2. ~~**Training/dataset section.**~~ Done. Distributed into §1 and §2.
3. ~~**Figures in §3.**~~ Done. Three figures from autoloop data.
4. ~~**v0.3: Enrichment fraction reframe.**~~ Done.
5. ~~**v0.5: Version injection, reviewer feedback, terminology fixes.**~~ Done.
6. ~~**v0.7: Mirostat lineage integration.**~~ Done. Three-regime prior art acknowledged (Holtzman, Basu/Mirostat, Meister, Nakaishi, Mikhaylovskiy). Predictions 1–2 reframed as partially established. Convergent evidence argument added to conclusion.
7. **v0.8: Grounding circularity escape.** Make the distortion-measure decomposition explicit in §4 — model's measure (training-induced) vs task-specific measure, grounding as overlap. Notes in `drafts/v0.8-target-notes.md`.
8. **Zenodo integration.** Link repo to Zenodo for DOI minting on tagged releases.
9. **Outreach.** README rewritten as landing page. Discussion post drafted. First audience TBD.
10. **Paper 2 development.** Surprisal leakage section drafted. Ecological argument to develop.
