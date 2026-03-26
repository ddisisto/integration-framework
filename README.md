# Integration

**Compression, distortion, novelty, and meaning in large language models**

**[Read the paper →](https://ddisisto.github.io/integration-framework/paper/docs/integration.html)** · **[PDF](https://ddisisto.github.io/integration-framework/paper/docs/integration.pdf)**

*Independent research — no affiliation, no funding, no product.*

---

Every token a language model generates comes with a surprisal value — the model's own prediction error, computed for free as part of inference. We use it during training (it's the loss function). We occasionally inspect it for debugging. And then, at inference time, we throw it away.

This paper argues that's a mistake, and that the reason it's a mistake reveals something fundamental about what these systems are doing.

## The argument in brief

The paper treats what LLMs do as **hierarchical multi-scale compression**, and the autoregressive loop as **sequential coding through a bandwidth-limited channel**. From this, a single measurable variable falls out: the **enrichment fraction** — the proportion of tokens doing novel compressive work over a window of generation. It determines whether output is productive, degenerate, or noise — a distinction invisible in fluency metrics but directly observable in the model's own surprisal.

<p align="center">
<img src="paper/figures/figure_a_collapse.png" width="32%" alt="Attractor collapse — surprisal drops to near-zero as generation locks into a repeating loop">
<img src="paper/figures/figure_b_tokens.png" width="32%" alt="Coherent prose — mix of enriching and stabilising tokens">
<img src="paper/figures/figure_c_noise.png" width="32%" alt="Noise regime — high surprisal throughout, no coherent structure">
</p>
<p align="center"><em>Left: attractor collapse (enrichment → 0). Centre: coherent prose (mixed enriching/stabilising). Right: noise (enrichment → 1).</em></p>

The three-regime structure itself is well-established empirically (Holtzman et al. 2020, Basu et al. 2021, Nakaishi 2024, Mikhaylovskiy 2025). The contribution is the enrichment fraction as a continuous, theoretically grounded metric — and its embedding within the compression hierarchy, which explains *why* these regimes exist rather than merely documenting that they do.

## What's novel

- **The autoregressive loop as sequential coding** through a bandwidth-limited channel — the mismatch between internal state dimensionality and single-token output is not metaphorical but information-theoretic.
- **The enrichment fraction** as a continuous variable characterising generation regime, derived from the model's own surprisal.
- **What grows across depth despite the data processing inequality** — not information about the input, but the *organisation* of preserved information (statistical complexity).
- **Grounding as a rate-distortion question** — converts a philosophical debate into one with measurable parameters.
- **Alignment as bandwidth constraint** — the binding constraint is feedback *bandwidth*, not feedback quality. The receiver's distortion measure is too rich to convey through available channels.

## Predictions

The framework generates testable predictions — four measurable via generation statistics, seven concerning internal structure. Two are already partially established by convergent results across independent research programmes. The predictions and their current status are tracked in the paper.

## Sections

The paper is four sections plus a conclusion, with formal constructions in an appendix.

1. **The Compression Hierarchy** — Rate-distortion as the organising principle. The one sharp boundary (lossless/lossy), the compression continuum, what transformers do, and how training fixes the distortion measure.
2. **Structure Across Depth** — What grows across layers despite the data processing inequality. The DPI resolution, statistical complexity as the measure of what grows, and why depth buys capability rather than merely capacity.
3. **The Autoregressive Loop** — The projection bottleneck formalised. Enrichment fraction, the three regimes, chain-of-thought and in-context learning as steering strategies. Where the framework meets and extends the Mirostat / typical sampling literature.
4. **Grounding and Alignment** — Two distortion measures (training-induced vs task-specific). Grounding as rate-distortion question. Alignment as distortion measure mismatch — the binding constraint is feedback bandwidth, not quality.

## Versioning

Tagged releases (`v0.x`) mark stable versions. `main` is the working branch; `publish` tracks the latest tagged release and serves the [live site](https://ddisisto.github.io/integration-framework/paper/docs/integration.html). The version string is injected automatically at render time via `git describe`.

## Building locally

Requires Python, [Quarto](https://quarto.org), and TinyTeX.

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
quarto render paper   # outputs to paper/docs/
```

## Citation

If you reference this work, please cite:

```bibtex
@misc{disisto2026integration,
  author       = {DiSisto, Daniel},
  title        = {Integration: Compression, Distortion, Novelty, and Meaning},
  year         = {2026},
  url          = {https://github.com/ddisisto/integration-framework},
  note         = {Living document, v0.7}
}
```

## License

This work is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
