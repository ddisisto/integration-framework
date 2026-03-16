# Integration

## Project overview

An independent research framework arguing that LLM effectiveness reflects hierarchical multi-scale compression (algorithmic → organisational → semantic), the autoregressive loop is fundamentally ambivalent (enriching vs degrading regimes), and this ambivalence recurs at ecological scale through nested feedback loops threatening silent representational flattening. The unifying concept is **integration** — compression is the mechanism, integration is the thesis.

## Files

- `v1_draft.md` — Complete first draft. Strong on autoregressive loop analysis, carrier ecology, enriching/degrading distinction. Superseded structurally but remains source material.
- `v2_outline.md` — Intermediate restructuring plan. Replaced Heaps' apparatus with info-theoretic grounding. Superseded by integration_framework.md.
- `integration_framework.md` — **Current working outline.** Three-part exploration/integration structure. This is the version to write.
- `research/` — Four research reports (grounding layer for all writing):
  - `info_theoretic_foundations.md` — Rate-distortion, DPI, statistical complexity, IB framework
  - `representational_geometry.md` — Intrinsic dimensionality, probing studies, emergence debate
  - `model_collapse_ecology.md` — Shumailov et al., synthetic data feedback, silent flattening
  - `biological_convergence.md` — RSA, Vygotsky/Deacon/Levinson, grounding problem

## Working outline (integration_framework.md)

Three parts, each containing one exploration chapter and one integration chapter:
- **Part I — Compression:** Ch1 (The Compression Hierarchy) + Ch2 (Structure Across Depth)
- **Part II — Composition:** Ch3 (The Autoregressive Loop) + Ch4 (Convergence Across Substrates)
- **Part III — Ecology:** Ch5 (The Recursive Loop) + Ch6 (Of Meaning)

The structure enacts the thesis: each part opens territory then consolidates. Info-theoretic tools arrive where they do work, not frontloaded.

## Multi-scale output strategy

The project produces outputs at multiple scales — the framework applied to its own presentation:

1. **Full paper** — Canonical reference. All formal apparatus, appendices, 10 predictions, full argumentation. The "zoom all the way in" version.
2. **Blog post / accessible piece** — ~15 min read. Core ideas (enriching/degrading, silent flattening, nested loops, processor-to-carrier threshold). Links to full paper. Written after full paper exists.
3. **Web app / semantic zoom device** — Interactive presentation where readers navigate the framework at their preferred depth. Axes: formality (philosophy ↔ science), focus (predictions, ecology, architecture, etc.). The framework presented as a navigable compression hierarchy of itself.

## Key decisions

- **Info-theoretic formalism:** Main body uses info theory as precise vocabulary — clear, accessible. Appendices carry formal constructions. Each appendix answers a specific question a sceptical reader would actually ask.
- **Distributed formalism:** Rate-distortion in Ch1, DPI + statistical complexity in Ch2, channel capacity in Ch3. No standalone maths section.
- **Audience:** Broad — ML researchers, cognitive scientists, informed generalists. Prioritise clarity; make dismissal costly through available rigour.
- **Human-AI collaboration:** Acknowledged in end matter, stated plainly. The paper is itself an instance of the integration it describes.

## Key vocabulary

- "statistical complexity" / "structural complexity growth" (replaces β / β amplifier)
- "representational diversity contraction" (replaces β-degradation)
- "enriching/degrading regime" (retained from v1)
- "compressive novelty" — governing variable at all feedback loop scales
- "integration" vs "mere accumulation" — the thematic spine

## Research findings to incorporate

- **Hunchback pattern:** Intrinsic dimensionality grows then contracts in final layers. Predict this explicitly — final contraction is the projection bottleneck.
- **Accumulator claim:** Among best-supported predictions (transformer circuits, logit lens, tuned lens).
- **DPI resolution:** Achille & Soatto (2018) is closest precursor. Cite prominently, distinguish clearly.
- **Statistical complexity measurement gap:** Theoretically sound, empirically untested in neural nets. Own this honestly. Proxy measures (intrinsic dimensionality, participation ratio) exist.
- **Autoregressive-as-channel:** Novel framing, no precedent found. Address joint coding complication (message constructed during transmission).
- **Silent flattening:** Alemohammad et al. (diversity collapses faster than quality) is closest empirical precedent. Four-loop taxonomy is genuinely novel.
- **Levinson spatial cognition:** Hedge the strong claim. "Language biases default strategies" holds; "reshapes internal representation" overstated per Li & Gleitman (2002).
- **Grounding-as-rate-distortion:** No precedent found. Present as novel framing, not established theory.
- **Most evidence from encoders:** Extrapolation to large autoregressive models needs acknowledgment.

## Writing guidance

- The paper's strongest material: autoregressive loop (Ch3), enriching/degrading distinction, carrier ecology (Ch5), nested feedback loops. Preserve largely intact from v1.
- The conclusion's final gesture — from representational diversity to "what's worth attending to" — is the paper's most memorable moment. One paragraph, decisive.
- Do not over-elaborate. The integration_framework outline identifies where to cut; trust it.
- 10 predictions must remain specific and testable. They are what make the framework falsifiable.
- Ch4 (biological convergence) is the shortest chapter. Once channel capacity formalises the constraint, the case is made quickly.
- IIT resonance in Ch6: light touch. Two programmes converging on "integration" is interesting; don't overclaim the connection.
