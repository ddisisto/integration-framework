# Integration

## Project

Independent research paper arguing that LLM effectiveness reflects hierarchical multi-scale compression, and the autoregressive loop is fundamentally ambivalent (enriching vs stabilising regimes). Compression is the mechanism; **integration** is the thesis.

Ecological implications (feedback loops, silent flattening, surprisal leakage, carrier transition) are staged in `paper2/` for a companion piece.

## Status

Paper 1 has Introduction + Sections 2–5 + Conclusion + Appendix A. Preparing for v1.0 Zenodo upload. Renders cleanly as HTML + PDF. GitHub Pages live (deploying from `publish` branch). License is CC BY 4.0.

**Branching:** `main` is the working branch. `publish` tracks the latest released version (currently v0.8). Merge to `publish` when ready to update the live site.

**Version injection:** `paper/_version.py` runs as a Quarto pre-render script, writing `git describe` output to `_version.yml` and `_version.tex`. Version appears in the preface (both formats) and PDF page footer.

```
paper/
├── _quarto.yml                        ← render config (pre-render: _version.py)
├── _version.py                        ← generates _version.yml/.tex from git describe
├── integration.qmd                    ← main document (abstract, preface, includes all sections)
├── 00_introduction.qmd               ← §1: problem, prior work positioning, contributions, outline
├── 01_compression_hierarchy.qmd       ← §2: rate-distortion, compression continuum, what transformers do
├── 02_structure_across_depth.qmd      ← §3: DPI resolution, statistical complexity, emergence thresholds
├── 03_autoregressive_loop.qmd         ← §4: channel capacity, enrichment fraction, figures
├── 04_grounding_alignment.qmd         ← §5: distortion measure decomposition, grounding, alignment
├── 05_conclusion.qmd                  ← conclusion: integration/accumulation, predictions, future
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

- **Formalism:** Main body uses info theory as precise vocabulary. Appendices carry the formal constructions. Rate-distortion in §2, DPI + statistical complexity in §3, channel capacity in §4. Distributed, not frontloaded.
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
7. ~~**v0.8: Reviewer feedback revision.**~~ Done. C_μ commitment softened to predictive complexity family. Grounding reframed (not dissolved). Two-compression-system disanalogy made explicit. Nayebi 2025 added as formal support for bandwidth constraint. Bibliography rationalised (75→52 entries, paper2 refs split out). Stale §4 references updated across repo.
8. **v0.9/v1.0: Preprint prep.** Introduction added. Prior work positioning written. New refs integrated (Huh, Huang, Voita & Titov, Mollo & Millière). Abstract tightened, keywords added, license changed to CC BY 4.0. Remaining: conclusion/discussion review, final abstract pass, tag v1.0.
9. **Zenodo upload.** Upload v1.0 PDF for DOI. ORCID registered. Link DOI back to paper metadata.
10. **Outreach.** Strategy: Zenodo first (priority + DOI) → targeted emails to Basu, Meister, Nayebi (seeking feedback + possible arXiv endorsement) → arXiv submission if endorsed.
11. **Paper 2 development.** Surprisal leakage section drafted. Ecological argument to develop.
