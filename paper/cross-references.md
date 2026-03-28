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
| `sec-grounding-alignment` | 4. Grounding and Alignment | `04_grounding_alignment.qmd` |
| `sec-conclusion` | 5. Conclusion | `05_conclusion.qmd` |

## Key Subsection IDs

### Section 1
- `sec-lossless-lossy` — The one sharp boundary; entry of relevance
- `sec-compression-continuum` — Lossy compression as continuum (perceptual → structural → semantic)
- `sec-information-surprisal` — Information content and surprisal

### Section 2
- `sec-architectural-mechanisms` — How transformers generate representational structure
- `sec-dpi-resolution` — DPI and the reorganisation/creation distinction
- `sec-predictive-organisation` — Predictive organisation as measure of what grows
- `sec-ib-complementarity` — Contrast with the Information Bottleneck
- `sec-emergence-thresholds` — Emergent capabilities as threshold-crossing
- `sec-ib-implications` — Implications for internal structure (forward ref to predictions)

### Section 3
- `sec-two-compression-systems` — Fixed weight geometry + dynamic context
- `sec-channel-capacity` — Channel capacity and the projection bottleneck
- `sec-compositional-novelty` — Compositional novelty from fixed geometry
- `sec-enriching-degrading` — Compressive novelty and the enrichment fraction
- `sec-cot-icl` — CoT and ICL as steering strategies
- `sec-autoregressive-limitations` — Limitations of the autoregressive account

### Section 4
- `sec-training` — What determines the model's distortion measure (training objective + dataset)
- `sec-two-measures` — Two distortion measures (training-induced vs task-specific)
- `sec-grounding-rate-distortion` — Grounding as rate-distortion question (novel)
- `sec-distortion-alignment` — Alignment as distortion measure mismatch (novel)
- `sec-shared-structure` — The shared formal structure of grounding and alignment

### Section 5 (Conclusion)
- `sec-thematic-spine` — Integration vs mere accumulation
- `sec-predictions` — Predictions (included from `predictions.qmd`)
- `sec-future-directions` — Ecological dynamics and measurement operationalisation

## Prediction IDs

All predictions defined in `predictions.qmd` (single source of truth, included in conclusion).

### Testable predictions
| ID | Prediction |
|----|-----------|
| `pred-enrichment-decay` | Enrichment fraction decays in unconstrained generation |
| `pred-temperature-enrichment` | Temperature–enrichment curve is non-monotonic |
| `pred-scale-enrichment` | Larger models sustain enrichment longer |
| `pred-surface-dominance` | Cheapest-compressed regularities dominate unconstrained output |

### Theoretical commitments
| ID | Prediction |
|----|-----------|
| `pred-complexity-depth` | Statistical complexity scales with depth (sublinear) |
| `pred-capability-complexity` | Capability onset correlates with complexity thresholds |
| `pred-accumulator` | Residual stream as measurable accumulator |
| `pred-ib-complement` | IB compression and complexity growth are complementary |
| `pred-training-shift` | Power-law dynamics; qualitative shift across training |
| `pred-icl-failure` | ICL fails when regularity type absent from geometry |
| `pred-dataset-distortion` | Dataset composition shapes representational structure |

### Predictions moved to Paper 2 (ecological dynamics)
| ID | Prediction |
|----|-----------|
| `pred-ecological-erosion` | Top-down erosion in recursive training loops |
| `pred-critical-fraction` | Characterisable threshold for self-reinforcing degradation |

## Citation conventions

- Use `@citekey` for inline citations: `@achille_soatto_2018`
- Use `[@citekey]` for parenthetical: `[@achille_soatto_2018]`
- Use `[@key1; @key2]` for multiple: `[@shannon_1948; @cover_thomas_2006]`
- All citekeys defined in `references.bib`
