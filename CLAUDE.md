# Integration

## Project

Independent research paper arguing that LLM effectiveness reflects hierarchical multi-scale compression, and the autoregressive loop is fundamentally ambivalent (enriching vs degrading regimes). Compression is the mechanism; **integration** is the thesis.

Ecological implications (feedback loops, silent flattening, carrier transition) are staged in `paper2/` for a companion piece.

## Status

Paper 1 is tightened to Chapters 1–4 + Conclusion. Appendix A written. Renders cleanly.

```
paper/
├── _quarto.yml                        ← render config
├── integration.qmd                    ← main document (includes all chapters)
├── index.qmd                          ← abstract + preface
├── 01_compression_hierarchy.qmd       ← DONE (~1,040 words)
├── 02_structure_across_depth.qmd      ← DONE (~3,200 words)
├── 03_autoregressive_loop.qmd         ← DONE (~2,600 words)
├── 04_convergence_across_substrates.qmd ← TIGHTENED (~1,200 words, was ~2,300)
├── 05_conclusion.qmd                  ← NEW (~900 words) — predictions + future directions
├── references.bib                     ← ~76 entries
├── cross-references.md                ← canonical IDs
├── appendix_formal_foundations.qmd    ← DONE (four sections)
└── references.qmd

paper2/                                ← staging for companion piece
├── README.md                          ← scope and key concepts
├── 05_recursive_loop.qmd             ← original Ch5 (ecology)
└── 06_of_meaning.qmd                 ← original Ch6 (meaning)
```

Other files: `v1_draft.md` (source material), `v2_outline.md` (superseded), `integration_framework.md` (working outline), `feedback-v0.1.md` (external reviewer feedback).

## Rendering

Requires: Python venv (`.venv/`), Quarto, TinyTeX. Setup for a fresh clone:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cd paper && quarto render       # outputs HTML + PDF to web/
```

Output goes to `web/` (HTML site + `Integration.pdf`). The `web/` directory is committed so that tagged versions always include a current render.

**Always run `cd paper && quarto render` before tagging or when changes need review.**

## Writing principles

- Say what needs saying, then stop. One idea per paragraph.
- Show the seams: when a claim is novel, established, or speculative, say so.
- Earn every formal term at the moment it appears.
- No references to earlier drafts or revisions — the reader sees only this version.

## Key decisions

- **Formalism:** Main body uses info theory as precise vocabulary. Appendices carry the formal constructions. Rate-distortion in Ch1, DPI + statistical complexity in Ch2, channel capacity in Ch3. Distributed, not frontloaded.
- **Audience:** ML researchers, cognitive scientists, informed generalists. Clarity over gatekeeping; rigour available in appendices.
- **Scope:** Paper 1 covers compression and composition (the formally constrained core). Ecological dynamics (feedback loops, silent flattening, carrier transition, attention economy) deferred to paper 2.
- **Multi-scale output:** Full paper → blog post → interactive web app (semantic zoom). Blog and web app come after the paper exists.
- **Human-AI collaboration** acknowledged in preface, stated plainly.

## What's novel (handle with care)

### In Paper 1
- Autoregressive loop as sequential coding through bandwidth-limited channel
- Grounding problem as rate-distortion question
- Alignment as distortion measure mismatch (model's implicit measure vs receiver's; correction as projection bottleneck problem)
- Subtractive vs generative processing distinction (IB tracks what's discarded; this framework tracks what's generated)

### Staged for Paper 2
- Four-loop feedback taxonomy (within-context, agentic, human-mediated, training-distributional)
- Silent flattening as named phenomenon with hierarchical erosion prediction
- Processor-to-carrier transition framing
- Attention allocation as distortion measure selection; algorithmic capture as adaptive exploit at ecological scale

These have no clear precedent in the literature. Present as contributions, not established theory.
