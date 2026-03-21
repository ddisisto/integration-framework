# Cross-Reference Conventions

Canonical IDs for use across all section files. Use `@sec-*` for sections,
`@pred-*` for predictions, `@fig-*` / `@tbl-*` / `@eq-*` as needed.

---

## Section IDs

| ID | Section | File |
|----|---------|------|
| `sec-compression-hierarchy` | 1. The Compression Hierarchy | `01_compression_hierarchy.qmd` |
| `sec-structure-across-depth` | 2. Structure Across Depth | `02_structure_across_depth.qmd` |
| `sec-autoregressive-loop` | 3. The Autoregressive Loop | `03_autoregressive_loop.qmd` |
| `sec-convergence` | 4. Convergence Across Substrates | `04_convergence_across_substrates.qmd` |
| `sec-conclusion` | 5. Conclusion | `05_conclusion.qmd` |

## Key Subsection IDs

### Section 1
- `sec-lossless-lossy` — The one sharp boundary; entry of relevance
- `sec-compression-continuum` — Lossy compression as continuum (perceptual → structural → semantic)
- `sec-what-transformers-do` — Bridging to deep learning; forward reference to Ch 2

### Section 2
- `sec-architectural-mechanisms` — How transformers generate representational structure
- `sec-dpi-resolution` — DPI and the reorganisation/creation distinction
- `sec-statistical-complexity` — Statistical complexity as measure of growth
- `sec-ib-complementarity` — Contrast with the Information Bottleneck
- `sec-emergence-thresholds` — Emergent capabilities as threshold-crossing
- `sec-predictions-ch2` — Predictions 1–5

### Section 3
- `sec-two-compression-systems` — Fixed weight geometry + dynamic context
- `sec-channel-capacity` — Channel capacity and the projection bottleneck
- `sec-compositional-novelty` — Compositional novelty from fixed geometry
- `sec-enriching-degrading` — Compressive novelty and the enrichment fraction
- `sec-cot-icl` — CoT and ICL as steering strategies
- `sec-predictions-ch3` — Predictions 6–7
- `sec-autoregressive-limitations` — Limitations of the autoregressive account

### Section 4
- `sec-projection-bottleneck` — Channel capacity as substrate-independent constraint
- `sec-convergence-limits` — What convergence explains and what it doesn't
- `sec-grounding-rate-distortion` — Grounding as rate-distortion question (novel)
- `sec-predictions-ch4` — Prediction 8

### Section 5 (Conclusion)
- `sec-thematic-spine` — Integration vs mere accumulation
- `sec-distortion-alignment` — Alignment as distortion measure mismatch (novel)
- `sec-consolidated-predictions` — Summary of all 8 predictions with testability ranking
- `sec-future-directions` — Ecological dynamics and measurement operationalisation

## Prediction IDs

| ID | # | Prediction | Section |
|----|---|-----------|---------|
| `pred-complexity-depth` | 1 | Statistical complexity scales with depth (sublinear) | 2 |
| `pred-capability-complexity` | 2 | Capability onset correlates with complexity thresholds | 2 |
| `pred-accumulator` | 3 | Residual stream as measurable accumulator | 2 |
| `pred-ib-complement` | 4 | IB compression and complexity growth are complementary | 2 |
| `pred-training-shift` | 5 | Power-law dynamics; qualitative shift across training | 2 |
| `pred-cot-quality` | 6 | CoT quality predicts effectiveness better than length | 3 |
| `pred-icl-failure` | 7 | ICL fails when regularity type absent from geometry | 3 |
| `pred-rsa-convergence` | 8 | Transformer/biological representational similarity | 4 |

### Predictions moved to Paper 2 (ecological dynamics)
| `pred-ecological-erosion` | 9 | Top-down erosion in recursive training loops | paper2 |
| `pred-critical-fraction` | 10 | Characterisable threshold for self-reinforcing degradation | paper2 |

## Citation conventions

- Use `@citekey` for inline citations: `@achille_soatto_2018`
- Use `[@citekey]` for parenthetical: `[@achille_soatto_2018`]
- Use `[@key1; @key2]` for multiple: `[@shannon_1948; @cover_thomas_2006]`
- All citekeys defined in `references.bib`
