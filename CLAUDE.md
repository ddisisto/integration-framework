# Integration

## Project

Independent research paper arguing that LLM effectiveness reflects hierarchical multi-scale compression, the autoregressive loop is fundamentally ambivalent (enriching vs degrading regimes), and this ambivalence recurs at ecological scale through nested feedback loops. Compression is the mechanism; **integration** is the thesis.

## Status

Chapters 1–6 are written. The appendix is stubbed. The Quarto book structure is in place. Research reports in `research/` ground all claims.

```
paper/
├── _quarto.yml                        ← book config
├── index.qmd                          ← abstract + preface
├── 01_compression_hierarchy.qmd       ← DONE (~1,040 words)
├── 02_structure_across_depth.qmd      ← DONE (~3,200 words)
├── 03_autoregressive_loop.qmd         ← DONE (~2,600 words)
├── 04_convergence_across_substrates.qmd ← DONE (~2,300 words)
├── 05_recursive_loop.qmd             ← DONE (~2,800 words)
├── 06_of_meaning.qmd                 ← DONE (~1,100 words)
├── references.bib                     ← ~76 entries
├── cross-references.md                ← canonical IDs (prediction sections: sec-predictions-ch{N})
├── appendix_formal_foundations.qmd    ← STUB (write after main chapters)
└── references.qmd
```

Other files: `v1_draft.md` (source material), `v2_outline.md` (superseded), `integration_framework.md` (working outline).

## Writing principles

- Say what needs saying, then stop. One idea per paragraph.
- Show the seams: when a claim is novel, established, or speculative, say so.
- Earn every formal term at the moment it appears.
- No references to earlier drafts or revisions — the reader sees only this version.
- The stubs contain everything needed to write each chapter: structure, citations, calibration notes, target length.

## Key decisions

- **Formalism:** Main body uses info theory as precise vocabulary. Appendices carry the formal constructions. Rate-distortion in Ch1, DPI + statistical complexity in Ch2, channel capacity in Ch3. Distributed, not frontloaded.
- **Audience:** ML researchers, cognitive scientists, informed generalists. Clarity over gatekeeping; rigour available in appendices.
- **Multi-scale output:** Full paper → blog post → interactive web app (semantic zoom). Blog and web app come after the paper exists.
- **Human-AI collaboration** acknowledged in preface, stated plainly.

## What's novel (handle with care)

- Four-loop feedback taxonomy (within-context, agentic, human-mediated, training-distributional)
- Silent flattening as named phenomenon with hierarchical erosion prediction
- Autoregressive loop as sequential coding through bandwidth-limited channel
- Grounding problem as rate-distortion question
- Processor-to-carrier transition framing
- Alignment as distortion measure mismatch (model's implicit measure vs receiver's; correction as projection bottleneck problem)
- Attention allocation as distortion measure selection; algorithmic capture as adaptive exploit at ecological scale

These have no clear precedent in the literature. Present as contributions, not established theory.
