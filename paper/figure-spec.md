# Figure Data Spec

Data requirements for illustrative figures in §3 (The Autoregressive Loop). Produced by the autoloop project, consumed by this paper. The paper handles all visual presentation; autoloop delivers structured data only.

## Source constraints

- Model: SmolLM-135M (the paper will say "a 135M-parameter language model")
- All examples from sweep runs with documented (L, T, seed) so they are reproducible
- Data format: one JSON file per figure, schema below

## Figure A: Collapse transition

Four consecutive context windows spanning the transition from coherent output into a permanent attractor basin.

**Selection criteria:**
- Choose a clean collapse: coherent prose → narrowing vocabulary → verbatim loop, within 3-4 windows
- L=128 preferred (clean window boundaries)
- The final window should show surprisal < 0.001 (deep basin)

**Schema:** `figure_a_collapse.json`

```json
{
  "metadata": {
    "model": "SmolLM-135M",
    "L": 128,
    "T": 0.60,
    "seed": 42,
    "step_range": [67200, 67712],
    "description": "Collapse from coherent prose into 5-token attractor basin"
  },
  "windows": [
    {
      "window_id": 1,
      "step_range": [67200, 67328],
      "stats": {
        "mean_entropy": 1.743,
        "mean_surprisal": 0.784,
        "pct_enriching": 12.0
      },
      "tokens": [
        {"token": " than", "surprisal": 0.42, "entropy": 1.61, "gap": 1.19},
        ...
      ]
    },
    ...
  ]
}
```

**What the paper will do with this:** A step plot of mean entropy and mean surprisal across the four windows, with a representative text excerpt beneath each. The visual story is the four-orders-of-magnitude surprisal drop.

## Figure B: Token-level regime markup (coherent prose)

A passage of 60-100 tokens from the rich dynamics regime, with per-token metrics for color-coded rendering.

**Selection criteria:**
- T in the 0.70-0.80 range (coherent, topically shifting)
- ~15-20% enriching tokens
- Choose a passage with clear semantic content — nouns, topic shifts, specific details — so the enriching/stabilising pattern is visually legible
- Avoid passages with artefacts, broken words, or formatting noise

**Schema:** `figure_b_tokens.json`

```json
{
  "metadata": {
    "model": "SmolLM-135M",
    "L": 192,
    "T": 0.70,
    "seed": 42,
    "step_range": [55000, 55128],
    "description": "Coherent prose with ~18% enriching tokens"
  },
  "stats": {
    "mean_entropy": 1.57,
    "mean_surprisal": 1.07,
    "pct_enriching": 18.0
  },
  "tokens": [
    {"token": " Now", "surprisal": 0.83, "entropy": 1.42, "gap": 0.59},
    {"token": ",", "surprisal": 0.12, "entropy": 0.95, "gap": 0.83},
    ...
  ]
}
```

**What the paper will do with this:** Render the passage with each token colored on a continuous scale by gap value. Cool/neutral for stabilising (gap > 0), warm for enriching (gap < 0). The reader sees that semantic content words are enriching; grammatical scaffolding is stabilising.

## Figure C: Noise extreme

A passage of 60-100 tokens from the noise regime, same per-token schema as Figure B.

**Selection criteria:**
- T >= 1.50 (high entropy, incoherent output)
- \>50% enriching tokens by gap metric
- Mean surprisal > mean entropy (negative average gap)
- Output should be clearly unstructured — no accidental coherent phrases

**Schema:** `figure_c_noise.json`

Same structure as Figure B, different metadata.

```json
{
  "metadata": {
    "model": "SmolLM-135M",
    "L": 128,
    "T": 1.50,
    "seed": 42,
    "step_range": [50000, 50128],
    "description": "Noise regime — 83% enriching by gap metric, incoherent output"
  },
  ...
}
```

**What the paper will do with this:** Same color treatment as Figure B. The visual contrast is the point: nearly all tokens are warm-colored (enriching by the metric) but the text is word salad. "Both extremes are pathological" becomes immediate.

## Delivery

Place output files in `../autoloop/exports/framework-figures/`. The paper will reference them at render time or copy them into `paper/data/`.

## Notes

- The examples in `autoloop/docs/enriching-stabilising-examples.md` already contain suitable candidates for all three figures. This spec asks for the same data in structured form.
- Gap is defined as `entropy + log_prob` (equivalently `entropy - surprisal`). Positive gap = stabilising, negative gap = enriching. Include this in metadata if helpful.
- Token strings should preserve leading whitespace (the tokenizer's spacing).
- If a better example exists than the ones in the examples doc, use it. The selection criteria matter more than matching specific step ranges.
