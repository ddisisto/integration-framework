# What is surprisal actually telling us — and why are we throwing it away?

**[D] Discussion**

Every token a language model generates comes with a surprisal value — the model's own prediction error, computed for free as part of inference. It's the most direct window we have into what the model "expected" versus what it produced. We use it during training (it's the loss function). We occasionally inspect it for debugging. And then, at inference time, we throw it away.

I think this is a mistake, and I think the reason it's a mistake is more interesting than it first appears.

## Surprisal as a compression signal

I've been working on a framework ([paper here](https://ddisisto.github.io/integration-framework/integration.html), [repo](https://github.com/ddisisto/integration-framework)) that treats what LLMs do as hierarchical multi-scale compression, and the autoregressive loop as sequential coding through a bandwidth-limited channel. Within that framework, surprisal at each token isn't just a loss metric — it's a real-time signal about whether generation is doing novel compressive work or reinforcing existing trajectories.

The core idea: at any point during generation, you can look at the relationship between the model's entropy (uncertainty before sampling) and the surprisal of what was actually sampled. When surprisal is high relative to entropy, the token carried genuinely new information — it moved the context somewhere the model's own compression didn't fully anticipate. When surprisal is low, the token was predictable from context — scaffolding, continuation, pattern completion.

Neither is inherently good or bad. You need both. But the *ratio* over a window of generation — what the paper calls the enrichment fraction — turns out to characterise the qualitative regime of the output. High enrichment fraction with coherence = productive generation. Low enrichment fraction = the model settling into attractors (the repetitive loops everyone has seen). Very high enrichment fraction = noise (the model surprising itself because it's lost coherent structure, not because it's generating novelty).

## The biological parallel that sharpens the point

Here's where it gets interesting. Coupé et al. (2019) measured information transfer rates across 17 languages and found convergence on roughly 39 bits per second — languages spoken faster carry less information per syllable, slower languages carry more, same rate. That's the *linguistic* channel. But face-to-face, humans communicate on many channels simultaneously: prosody, facial expression, gesture, gaze, timing.

And critically, some of those channels carry *surprisal itself*. When you're talking to someone and they widen their eyes, raise an eyebrow, shift their posture — they're involuntarily broadcasting their prediction error. You're getting real-time signal about where your interlocutor's model diverged from what you said. This is low-bandwidth but extremely high-value: it tells the speaker what the listener expected, which is partial information about the listener's compression — their model of the topic.

Speakers adjust in real time based on this. They slow down when confusion registers, skip ahead when the listener nods, elaborate when surprise shows. This is closed-loop calibration of the sender's output to the receiver's needs, mediated by involuntary surprisal leakage.

LLMs have none of this. The model computes surprisal at every token but doesn't broadcast it. The user has no involuntary leakage channel either — the model can't see their face. Both sides of the calibration loop that biological communication relies on are structurally absent.

## What we could do with it

Surprisal dynamics during generation are directly observable and don't require any model modification. You can instrument them right now. Some things they could tell us:

- **Degeneration detection.** Repetition loops, attractor collapse, and mode collapse all have distinctive surprisal signatures — they're visible in the dynamics well before they're obvious in the text.
- **Enrichment monitoring.** Rather than evaluating output quality post-hoc, track the enrichment fraction in real time. If it drops below a threshold, the model is coasting on its own momentum.
- **Temperature diagnostics.** The relationship between temperature and enrichment fraction is non-monotonic and model-specific. Surprisal dynamics could inform adaptive sampling strategies that maintain productive generation rather than picking a fixed temperature.
- **Alignment signal.** This is the speculative one, but: if the user's surprisal could be captured (even approximately, even through text-based signals of confusion or engagement), the gap between model-surprisal and user-surprisal would be a real-time proxy for distortion measure mismatch — the model finding something predictable that the user finds surprising, or vice versa.

## The question I can't answer

All of this is observable and in-principle testable. But there's a harder question underneath. Biological communication evolved a credibility gradient — involuntary signals (pupil dilation, micro-expressions) are hard to fake, which is exactly what makes them informative. Voluntary signals (words) are easy to fake, which is why we cross-reference them against the involuntary channels.

If we build systems that surface model surprisal as a communication signal — uncertainty displays, confidence indicators, attention visualisations — these are *constructed* channels, fully voluntary. They can be gamed, tuned, optimised. They lack the credibility that comes from being involuntary.

So: **can a deliberately constructed transparency channel ever do the calibrating work that involuntary leakage does? Or does the credibility gradient require that the signal be outside the sender's control?**

I genuinely don't know. But I think the question matters for how we think about human-AI interaction, and I think surprisal — sitting right there in the logprobs, computed and discarded — is where the answer starts.

---

Paper: [Integration: Compression, distortion, novelty, and meaning](https://ddisisto.github.io/integration-framework/integration.html) (v0.5, living document)

Repo: [github.com/ddisisto/integration-framework](https://github.com/ddisisto/integration-framework)

*Independent research — no affiliation, no funding, no product. Feedback welcome, especially from anyone who's actually instrumented surprisal dynamics during generation.*
