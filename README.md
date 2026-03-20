# Integration

**Compression, composition, and the projection bottleneck in large language models**

This paper argues that LLM effectiveness reflects hierarchical multi-scale
compression, and that the autoregressive loop is fundamentally ambivalent —
enriching when each token surfaces structure unavailable from context,
degrading when tokens reinforce existing trajectories.

**[Summary →](https://ddisisto.github.io/integration-framework/summary.html)** · **[Full paper →](https://ddisisto.github.io/integration-framework/integration.html)**

The full paper includes a PDF download link.

## Building locally

Requires Python, [Quarto](https://quarto.org), and TinyTeX.

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cd paper && quarto render   # outputs to docs/
```

## License

This work is licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
