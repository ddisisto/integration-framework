# Cross-Reference Conventions

Canonical IDs for use across all chapter files. Use `@sec-*` for sections,
`@pred-*` for predictions, `@fig-*` / `@tbl-*` / `@eq-*` as needed.

---

## Chapter IDs

| ID | Chapter | File |
|----|---------|------|
| `sec-compression-hierarchy` | 1. The Compression Hierarchy | `01_compression_hierarchy.qmd` |
| `sec-structure-across-depth` | 2. Structure Across Depth | `02_structure_across_depth.qmd` |
| `sec-autoregressive-loop` | 3. The Autoregressive Loop | `03_autoregressive_loop.qmd` |
| `sec-convergence` | 4. Convergence Across Substrates | `04_convergence_across_substrates.qmd` |
| `sec-recursive-loop` | 5. The Recursive Loop | `05_recursive_loop.qmd` |
| `sec-of-meaning` | 6. Of Meaning | `06_of_meaning.qmd` |

## Part IDs

| ID | Part |
|----|------|
| `sec-part-compression` | Part I — Compression |
| `sec-part-composition` | Part II — Composition |
| `sec-part-ecology` | Part III — Ecology |

## Key Subsection IDs

### Chapter 1
- `sec-lossless-lossy` — The one sharp boundary; entry of relevance
- `sec-compression-continuum` — Lossy compression as continuum (perceptual → structural → semantic)
- `sec-what-transformers-do` — Bridging to deep learning; forward reference to Ch 2

### Chapter 2
- `sec-architectural-mechanisms` — How transformers generate representational structure
- `sec-dpi-resolution` — DPI and the reorganisation/creation distinction
- `sec-statistical-complexity` — Statistical complexity as measure of growth
- `sec-ib-complementarity` — Contrast with the Information Bottleneck
- `sec-emergence-thresholds` — Emergent capabilities as threshold-crossing
- `sec-predictions-ch2` — Predictions 1–5

### Chapter 3
- `sec-two-compression-systems` — Fixed weight geometry + dynamic context
- `sec-channel-capacity` — Channel capacity and the projection bottleneck
- `sec-compositional-novelty` — Compositional novelty from fixed geometry
- `sec-enriching-degrading` — The enriching and degrading regimes
- `sec-cot-icl` — CoT and ICL as steering strategies
- `sec-predictions-ch3` — Predictions 6–7
- `sec-autoregressive-limitations` — Limitations of the autoregressive account

### Chapter 4
- `sec-projection-bottleneck` — Channel capacity as substrate-independent constraint (Vygotsky, Fodor, speech bandwidth, RSA evidence woven in)
- `sec-convergence-limits` — What convergence explains and what it doesn't (Deacon, Levinson)
- `sec-grounding-rate-distortion` — Grounding as rate-distortion question (novel)
- `sec-predictions-ch4` — Prediction 8

### Chapter 5
- `sec-carriers` — Knowledge carriers and persistence ecology
- `sec-carrier-asymmetry` — Endogenous vs exogenous persistence
- `sec-nested-loops` — Four nested feedback loops
- `sec-silent-flattening` — Top-down erosion and silent flattening
- `sec-curation-defence` — Human curation as primary defence
- `sec-predictions-ch5` — Predictions 9–10
- `sec-eroding-asymmetry` — Processor-to-carrier transition

### Chapter 6
- `sec-thematic-spine` — Integration vs mere accumulation
- `sec-shannon-surprise` — Shannon's insight as closing frame
- `sec-distortion-alignment` — Alignment as distortion measure mismatch (novel)
- `sec-iit-resonance` — IIT resonance (light touch)
- `sec-consolidated-predictions` — Summary of all 10 predictions
- `sec-final-gesture` — What the hierarchy points toward without reaching

## Prediction IDs

| ID | # | Prediction | Chapter |
|----|---|-----------|---------|
| `pred-complexity-depth` | 1 | Statistical complexity scales with depth (sublinear) | 2 |
| `pred-capability-complexity` | 2 | Capability onset correlates with complexity thresholds | 2 |
| `pred-accumulator` | 3 | Residual stream as measurable accumulator | 2 |
| `pred-ib-complement` | 4 | IB compression and complexity growth are complementary | 2 |
| `pred-training-shift` | 5 | Power-law dynamics; qualitative shift across training | 2 |
| `pred-cot-quality` | 6 | CoT quality predicts effectiveness better than length | 3 |
| `pred-icl-failure` | 7 | ICL fails when regularity type absent from geometry | 3 |
| `pred-rsa-convergence` | 8 | Transformer/biological representational similarity | 4 |
| `pred-ecological-erosion` | 9 | Top-down erosion in recursive training loops | 5 |
| `pred-critical-fraction` | 10 | Characterisable threshold for self-reinforcing degradation | 5 |

## Citation conventions

- Use `@citekey` for inline citations: `@achille_soatto_2018`
- Use `[@citekey]` for parenthetical: `[@achille_soatto_2018]`
- Use `[@key1; @key2]` for multiple: `[@shannon_1948; @cover_thomas_2006]`
- All citekeys defined in `references.bib`
