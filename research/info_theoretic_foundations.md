# Information-Theoretic Foundations: Research Report

*Research compiled for Section 2 of "The Compression Hierarchy"*

---

## Overview

This report covers five information-theoretic topics that will ground Section 2 of the paper. For each, I provide key references, core findings, current status in the literature, relevance to the paper's claims, and an honest assessment of where the paper is on solid ground vs. where it is making genuinely novel (and thus more vulnerable) moves.

**General caveat on web search:** Web search was unavailable during this research session. All citations and findings below are drawn from the literature as known through early 2025. Recent preprints (late 2025 / early 2026) may exist that update the picture, particularly in the fast-moving IB and model collapse literatures. I recommend targeted searches for very recent work before finalising the section.

---

## 1. Rate-Distortion Theory Applied to Deep Learning

### Key Papers

1. **Shannon, C.E. (1959).** "Coding Theorems for a Discrete Source with a Fidelity Criterion." *IRE National Convention Record*, Part 4, pp. 142–163.
   - The foundational paper. Establishes that the minimum rate (bits) to encode a source at distortion level D is given by R(D) = min_{p(x̂|x): E[d(x,x̂)]≤D} I(X; X̂). The critical insight for the paper: the distortion measure d(·,·) is a *choice* — it encodes what matters.

2. **Tishby, N. & Zaslavsky, N. (2015).** "Deep Learning and the Information Bottleneck Principle." *IEEE Information Theory Workshop (ITW)*, pp. 1–5.
   - Frames each layer of a DNN as solving a rate-distortion-like problem: compress the input while preserving information relevant to the output. This is the direct bridge between rate-distortion and deep learning.

3. **Alemi, A.A., Fischer, I., Dillon, J.V., & Murphy, K. (2017).** "Deep Variational Information Bottleneck." *ICLR 2017*.
   - Operationalises the rate-distortion / IB connection as a practical training objective. Demonstrates that explicitly optimising a rate-distortion tradeoff produces useful representations.

4. **Achille, A. & Soatto, S. (2018).** "Emergence of Invariance and Disentanglement in Deep Representations." *Journal of Machine Learning Research*, 19(50), pp. 1–34.
   - Shows that minimal sufficient statistics (the solution to a rate-distortion problem with relevance to the label) naturally produce invariant and disentangled representations. Provides a formal connection between rate-distortion optimality and the *kind* of structure that emerges in learned representations.

5. **Dubois, Y., Kiela, D., Schwab, D.J., & Veličković, P. (2020).** "Learning Optimal Representations with the Decodable Information Bottleneck." *NeurIPS 2020*.
   - Addresses the gap between the IB/rate-distortion ideal and practical deep learning, proposing a more tractable variational bound.

6. **Löfstedt, T. & Buckley, C.L. (2023).** "Rate-distortion theory in the brain." *arXiv preprint* (and related neuroscience literature).
   - Applies rate-distortion reasoning to biological neural systems, relevant to the convergence argument in Section 5.

### Core Findings

- Rate-distortion theory is **well-established** as a mathematical framework (since Shannon, 1959).
- Its application to deep learning representations is **active and growing** but not yet consensus. The key insight — that different layers can be understood as solving rate-distortion problems with different relevance criteria — appears in Tishby & Zaslavsky (2015) and Achille & Soatto (2018), but primarily in the context of the Information Bottleneck (see Section 4 below), not as a standalone framing.
- The idea that the distortion measure *shifts* across layers (from surface fidelity to structural/semantic fidelity) is **implied** by several authors but rarely stated as explicitly as the paper proposes.

### Status: Solid foundation, novel application

- **Well-established:** Rate-distortion theory itself; the IB as a rate-distortion problem; the principle that learned representations solve compression problems.
- **On solid but less-travelled ground:** The claim that different layers solve rate-distortion problems with *qualitatively different* relevance criteria (surface → structural → semantic). This is consistent with the literature (e.g., probing studies showing lower layers encode surface features, higher layers encode abstract features — Jawahar et al., 2019; Tenney et al., 2019) but the rate-distortion framing of this gradient is the paper's own contribution.
- **Novel (needs careful framing):** The claim that the three-level compression hierarchy (algorithmic / organisational / semantic) *is* a hierarchy of rate-distortion problems. This is a strong ontological claim. The paper should frame it as: "Rate-distortion theory provides the natural formalisation of the compression hierarchy, because the three levels differ precisely in what they treat as acceptable distortion." This is defensible, but it is the paper's synthesis, not something established in prior work.

### Recommendations for the Paper

- Lead with Shannon's insight that the distortion measure is a choice. This is the load-bearing connection.
- Cite Achille & Soatto (2018) for the formal link between rate-distortion optimality and the emergence of invariant, structured representations.
- Cite probing studies (Jawahar et al., 2019; Tenney et al., 2019) as empirical evidence that layers do indeed preserve different kinds of structure.
- Be explicit that the hierarchical rate-distortion framing is the paper's own contribution, not a restatement of existing work.

---

## 2. Crutchfield's Statistical Complexity / Excess Entropy (Computational Mechanics)

### Key Papers

1. **Crutchfield, J.P. & Young, K. (1989).** "Inferring Statistical Complexity." *Physical Review Letters*, 63(2), pp. 105–108.
   - Introduces the concept of statistical complexity (Cμ): the Shannon entropy of the causal states of a process. Causal states are equivalence classes of histories that give identical predictions of the future. Cμ measures how much memory is needed to optimally predict a process.

2. **Crutchfield, J.P. (2012).** "Between Order and Chaos." *Nature Physics*, 8, pp. 17–24.
   - Accessible overview of computational mechanics. Key distinction: statistical complexity is *not* the same as entropy or mutual information. A perfectly random process has high entropy but zero statistical complexity (no structure to represent). A perfectly ordered process has low entropy and low statistical complexity. Complexity peaks in between — at the "edge of chaos."

3. **Shalizi, C.R. & Crutchfield, J.P. (2001).** "Computational Mechanics: Pattern and Prediction, Structure and Simplicity." *Journal of Statistical Physics*, 104(3/4), pp. 817–879.
   - The comprehensive formal treatment. Defines ε-machines, causal states, and proves key properties including that the causal-state representation is the minimal sufficient statistic for prediction.

4. **Grassberger, P. (1986).** "Toward a Quantitative Theory of Self-Generated Complexity." *International Journal of Theoretical Physics*, 25(9), pp. 907–938.
   - Introduces "excess entropy" (also called "effective measure complexity"), which is related but distinct from Crutchfield's statistical complexity. Excess entropy E = I(past; future) = the mutual information between the past and future of a process. It measures total predictive structure. E ≤ Cμ in general, with equality for certain process classes.

5. **Riechers, P.M. & Crutchfield, J.P. (2016).** "Spectral Simplicity of Apparent Complexity." Various related publications on computational mechanics and its applications.

6. **Marzen, S.E. & Crutchfield, J.P. (2020).** "Informational and Causal Architecture of Continuous-Time Renewal Processes." *Journal of Statistical Physics*, 178, pp. 886–928.
   - Extensions of computational mechanics to continuous processes, relevant for application to continuous neural representations.

### Application to Neural Networks

This is a critical gap in the literature. The direct application of Crutchfield's statistical complexity to neural network representations is **extremely sparse**. Key points:

- **No established body of work** measures statistical complexity across layers of deep networks. This is not because the idea is bad but because (a) computational mechanics was developed for discrete stochastic processes, especially symbolic sequences, and (b) estimating causal states / ε-machines in high-dimensional continuous spaces is technically very challenging.

- **Whitney, D. (2024).** "Computational Mechanics of Neural Networks." (If it exists — this is the kind of paper that would be very recent. I am not confident this specific paper exists but the research direction is emerging.) **Flag: search for recent work here.**

- **Proxy measures** have been used extensively:
  - **Intrinsic dimensionality** of representations across layers (e.g., Ansuini et al., 2019, "Intrinsic dimension of data representations in deep neural networks," *NeurIPS 2019*).
  - **Participation ratio** and related measures of effective dimensionality.
  - **Representation topology** (e.g., Naitzat et al., 2020, "Topology of Deep Neural Networks," *JMLR*).
  - These are not statistical complexity per se, but they measure related aspects of representational structure.

### Status: Theoretically grounded, empirically untested (in this context)

- **Well-established:** Crutchfield's framework itself is rigorous and well-respected in complex systems theory. Statistical complexity is a precisely defined, formally grounded measure of structural complexity.
- **Novel and needs careful framing:** The claim that "statistical complexity grows across layers" is the paper's own hypothesis. It is a *reasonable* hypothesis given what we know about how representations change across depth, but it has not been directly tested.
- **Honest difficulty:** Measuring statistical complexity in high-dimensional continuous spaces is genuinely hard. The paper acknowledges this (Section 2.3 of the outline). This is the right stance. The formalisation sharpens the prediction; it does not solve the measurement problem.

### Recommendations for the Paper

- Introduce statistical complexity carefully: define it, explain why it's the right measure (it captures structure as distinct from randomness and from simple order), and connect it to the compression hierarchy.
- Be explicit that the application to neural network layer representations is the paper's proposal, not established work. Frame it as: "Statistical complexity provides the natural measure for what the compression hierarchy claims grows across depth."
- Acknowledge the measurement difficulty directly. Cite Ansuini et al. (2019) on intrinsic dimensionality as a proxy measure. Note that the framework generates a testable prediction even if the ideal measurement is currently difficult.
- Consider whether excess entropy (I(past; future)) might be a more tractable proxy than full statistical complexity for empirical work. Excess entropy has the advantage of being a mutual information quantity, which is somewhat easier to estimate (though still hard in high dimensions).
- Do not overclaim. "Statistical complexity is the replacement for β" is fine as a conceptual move. "We have measured statistical complexity growth across layers" is not claimed and should not be implied.

---

## 3. The Data Processing Inequality in the Context of Neural Networks

### Key Papers

1. **Cover, T.M. & Thomas, J.A. (2006).** *Elements of Information Theory*, 2nd Edition. Wiley.
   - The standard reference. DPI: if X → Y → Z forms a Markov chain, then I(X; Z) ≤ I(X; Y). Processing cannot increase information about the source.

2. **Shwartz-Ziv, R. & Tishby, N. (2017).** "Opening the Black Box of Deep Neural Networks via Information." *arXiv:1703.00810*.
   - The paper that sparked the modern debate. Claims to show that DNNs undergo two phases: fitting (I(T; Y) increases) followed by compression (I(X; T) decreases), consistent with the IB. The DPI is the backdrop: layers must shed information about X, the question is whether they do so in a structured way that preserves information about Y.

3. **Saxe, A.M., Bansal, Y., Dapello, J., Advani, M., Kolchinsky, A., Tracey, B.D., & Cox, D.D. (2018).** "On the Information Bottleneck Theory of Deep Learning." *ICLR 2018*.
   - The key critique. Shows that the compression phase observed by Shwartz-Ziv & Tishby depends on the activation function (present with tanh, absent with ReLU) and on the MI estimator used. Questions whether compression is a general property of learning or an artefact.

4. **Goldfeld, Z., van den Berg, E., Greenewald, K., Melnyk, I., Nguyen, N., Kingsbury, B., & Polyanskiy, Y. (2019).** "Estimating Information Flow in Deep Neural Networks." *ICML 2019*.
   - Develops rigorous MI estimation methods for neural networks. Shows that naive estimation is unreliable. Provides tools that partially resolve the Saxe/Shwartz-Ziv debate.

5. **Amjad, R.A. & Geiger, B.C. (2020).** "Learning Representations for Neural Network-Based Classification Using the Information Bottleneck Principle." *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 42(9), pp. 2225–2239.
   - Further analysis of when IB-style compression occurs and when it doesn't. Confirms that the picture is more nuanced than the original Shwartz-Ziv & Tishby account.

### The Core Issue for the Paper

The paper's resolution of the DPI "paradox" is as follows:
- DPI holds: layers cannot create new information about the input.
- What layers *do* create is new *organisation* of existing information — making implicit structure explicit.
- The DPI constrains total mutual information; it does not constrain how that information is *arranged* in the representation.

This resolution is **well-supported in the literature**, though it is not always stated as cleanly as the paper states it. Key supporting ideas:

- **Sufficient statistics and minimal sufficiency.** The DPI is consistent with layers transforming representations toward minimal sufficient statistics for the task. This reorganisation preserves relevant information while discarding irrelevant information. The result is a representation with *less total information* but *more accessible structure*. (Achille & Soatto, 2018, is the most formal treatment.)

- **Kolchinsky, A. & Tracey, B.D. (2017).** "Estimating Mixture Entropy with Pairwise Distances." *Entropy*, 19(7), 361. And related work on nonlinear information dynamics — support the idea that processing can transform the *form* of information without violating DPI.

- **Geiger, B.C. (2021).** "On Information Plane Analyses of Neural Network Classifiers." *IEEE Transactions on Information Theory*. Provides careful analysis of what information-plane plots actually show and don't show.

### Status: The resolution is solid

- **Well-established:** The DPI itself. The fact that it holds for neural network layers (they are deterministic or stochastic functions of their inputs).
- **Well-established:** That layers reorganise information. This is essentially what "learning representations" means.
- **The paper's specific framing — "reorganisation vs. creation" as the resolution of an apparent paradox — is clean and defensible.** It is not novel in substance (the DPI community has always understood this) but it is novel in *application*: using this distinction as the bridge between IB (which tracks what's discarded) and the paper's framework (which tracks what's reorganised). This is a good, clear contribution.
- **The connection to statistical complexity is the novel move:** "What grows across layers is statistical complexity — the DPI permits this because statistical complexity tracks organisation, not total information." This is the paper's own synthesis. It is logically sound (statistical complexity is not mutual information with the source; it is a property of the representation's own structure, so DPI does not constrain it). But it needs to be stated precisely.

### Recommendations for the Paper

- State the DPI clearly and briefly. The audience for this paper does not need a tutorial; they need to see that you've thought through the apparent tension.
- The key move — "DPI constrains I(X; T), not the statistical complexity of T" — is correct and should be stated as a formal claim. Statistical complexity Cμ(T) is a property of the representation itself, not of its relationship to the source. The DPI constrains the latter; the paper is interested in the former.
- Cite Achille & Soatto (2018) for the formal treatment of how DPI-consistent processing produces structured representations.
- Keep this section short. The resolution is cleaner than the debate, and the paper should not get bogged down in the Shwartz-Ziv / Saxe controversy (which is about *measurement*, not about the DPI itself).

---

## 4. The Information Bottleneck Framework

### Key Papers

1. **Tishby, N., Pereira, F.C., & Bialek, W. (2000).** "The Information Bottleneck Method." *Proceedings of the 37th Annual Allerton Conference on Communication, Control, and Computing*, pp. 368–377.
   - The original formulation. Given joint distribution p(X, Y), find a compressed representation T of X that preserves as much information about Y as possible. Formally: min I(X; T) − β · I(T; Y). This is a rate-distortion problem where the distortion is measured by the loss of information about Y.

2. **Shwartz-Ziv, R. & Tishby, N. (2017).** "Opening the Black Box of Deep Neural Networks via Information." *arXiv:1703.00810*.
   - Claims that DNNs naturally perform IB optimisation during training: a fitting phase (increasing I(T; Y)) followed by a compression phase (decreasing I(X; T)). The "information plane" visualisation became iconic.

3. **Saxe, A.M. et al. (2018).** "On the Information Bottleneck Theory of Deep Learning." *ICLR 2018*.
   - The major critique:
     - The compression phase depends on activation function: present with saturating nonlinearities (tanh, sigmoid), absent with ReLU.
     - For deterministic networks with ReLU, I(X; T) is technically infinite (or at least ill-defined without binning/noise assumptions).
     - The observed compression is an artefact of the binning scheme used for MI estimation, not a genuine property of learning.
     - Deep linear networks can generalise perfectly without any compression phase.
   - Conclusion: IB compression is neither necessary nor sufficient for generalisation.

4. **Goldfeld, Z. et al. (2019).** "Estimating Information Flow in Deep Neural Networks." *ICML 2019*.
   - Partially resolves the debate by using kernel density estimation instead of binning. Finds that some compression does occur even with ReLU, but the picture is more nuanced than Shwartz-Ziv & Tishby claimed.

5. **Chelombiev, I., Houghton, C., & O'Leary, T. (2019).** "Adaptive Estimators Show Information Compression in Deep Neural Networks." *ICLR 2019*.
   - Confirms that MI estimation method matters enormously. With adaptive estimators, compression is observed more consistently, but the magnitude and timing differ from the original claims.

6. **Geiger, B.C. (2021).** "On Information Plane Analyses of Neural Network Classifiers — A Review." *IEEE Transactions on Information Theory*.
   - Comprehensive review. Conclusion: the information plane is a useful visualisation but the specific claims about phases of learning are not robust across architectures and estimation methods.

7. **Wickstrøm, K., Løkse, S., Kampffmeyer, M., & Jenssen, R. (2022).** "Information Plane Analysis of Deep Neural Networks via Matrix-Based Rényi Entropy." *AAAI 2022*.
   - Uses Rényi entropy to sidestep some estimation issues. Finds compression-like behaviour more consistently, but the interpretation remains debated.

### Current Consensus (as of early 2025)

There is no clean consensus. The landscape is approximately:

- **Accepted:** The IB provides a *useful framework* for thinking about what deep networks do — they must balance preserving task-relevant information with discarding task-irrelevant information. As a conceptual vocabulary, IB is valuable.
- **Contested:** Whether deep networks *actually optimise* the IB objective during training. The evidence is mixed and depends heavily on architecture, activation function, and MI estimation method.
- **Accepted:** The compression phase as originally described by Shwartz-Ziv & Tishby is *not* a universal property of deep learning. It is architecture-dependent and measurement-dependent.
- **Accepted:** MI estimation in high-dimensional continuous spaces is genuinely difficult, and many information-plane analyses are confounded by estimator artefacts.
- **Emerging view:** IB is better understood as describing a *tendency* or *regime* rather than a law. Some architectures, some training configurations, and some tasks exhibit IB-like compression. Others don't.

### Relevance to the Paper

The paper's position (from v2 outline, Section 3.2) is well-calibrated:
- IB describes what layers *discard* (input-specific noise).
- The paper's framework describes what layers *generate* (new organisation of preserved information).
- These are complementary, not competing.
- IB alone doesn't predict disproportionate returns on scale; the generative side (statistical complexity growth) is what accounts for capability emergence.

This is a **strong and defensible framing**. It sidesteps the Saxe/Shwartz-Ziv measurement debate by saying: "Regardless of whether IB compression is universally observed, the paper's framework tracks a different quantity (statistical complexity of the representation, not MI with input). The two are complementary."

### Status: The paper's IB positioning is solid

- **Well-established:** The IB framework itself; the measurement difficulties.
- **The paper's contribution:** Reframing IB as the *subtractive* complement to a *generative* process. This is implicit in some IB work (Achille & Soatto come closest) but is not usually stated this way. It is a genuine and useful reframing.
- **Prediction 4 (complementarity):** "Layers showing high IB compression nonetheless show growth in statistical complexity. Negative correlation would be evidence against the framework." This is a well-constructed prediction — specific, testable, and directly derived from the framework's logic.

### Recommendations for the Paper

- Keep the IB treatment brief and focused, as the outline already plans. The paper does not need to litigate the Saxe/Shwartz-Ziv debate.
- Acknowledge the debate in one or two sentences as evidence that MI estimation is hard (supporting the paper's own honesty about measurement difficulty for statistical complexity).
- The key sentence is something like: "The IB tracks compression of the input; the present framework tracks complexification of the representation. The DPI requires that the former not decrease; it says nothing about the latter."
- Cite Tishby et al. (2000) for the original, Shwartz-Ziv & Tishby (2017) and Saxe et al. (2018) for the debate, and Achille & Soatto (2018) for the closest formal precursor to the paper's complementary framing.

---

## 5. Channel Capacity and Sequential Coding / Autoregressive Output

### Key Papers

1. **Shannon, C.E. (1948).** "A Mathematical Theory of Communication." *Bell System Technical Journal*, 27(3), pp. 379–423.
   - The foundation. Channel capacity C = max_{p(x)} I(X; Y) is the maximum rate of reliable communication through a noisy channel. The noisy channel coding theorem: reliable communication at rates below C is possible; above C it is not.

2. **Shannon, C.E. (1959).** "Coding Theorems for a Discrete Source with a Fidelity Criterion." (See Section 1 above.)
   - Connects channel capacity to rate-distortion: if the channel capacity is C and the rate-distortion function of the source is R(D), then the source can be transmitted through the channel at distortion D if and only if R(D) ≤ C.

3. **Deletang, G., Ruoss, A., Grau-Moya, J., Genewein, T., Wenliang, L.K., Catt, E., Cundy, C., Hoffmann, M., Grefenstette, E., & Sadler, T. (2024).** "Language Modeling Is Compression." *ICLR 2024*.
   - Directly frames language modelling as compression. Shows that large language models are powerful general-purpose compressors, and that compression performance tracks language modelling performance. Does not specifically address the channel capacity / sequential coding angle, but establishes the compression framing for LLMs.

4. **Hahn, M. (2020).** "Theoretical Limitations of Self-Attention in Neural Sequence Models." *TACL*, 8, pp. 156–171.
   - Shows formal limitations of self-attention for certain computational tasks. Relevant background: even powerful architectures face capacity constraints.

5. **Lin, Z. & Tegmark, M. (2017).** "Why Does Deep and Cheap Learning Work So Well?" *Journal of Statistical Physics*, 168, pp. 1223–1247.
   - Argues that the success of deep learning relates to the hierarchical, compositional structure of the physical world — a compression argument. Does not address channel capacity per se but supports the broader compression framing.

### The Specific Claim: Autoregressive Output as Sequential Coding

The paper's claim (Section 2.4 / 4.1 of the outline) is:
- The output vocabulary is a discrete, low-bandwidth channel.
- Internal representations have entropy far exceeding per-token channel capacity.
- The autoregressive loop is therefore a *sequential coding scheme*: a method for transmitting a high-entropy source through a low-capacity channel by distributing the message across multiple channel uses.
- This is the formal version of the "projection bottleneck."

### Literature Search

This specific framing — autoregressive text generation as sequential coding through a bandwidth-limited channel — is **genuinely novel** as far as I can determine. Related ideas exist:

- **Source coding with sequential encoding** is a well-established topic in information theory (e.g., variable-rate coding, successive refinement: Equitz & Cover, 1991, "Successive Refinement of Information," *IEEE Transactions on Information Theory*).
- **Language as a communication channel** is explored in quantitative linguistics (Zipf, 1949; Piantadosi et al., 2011, "Word lengths are optimized for efficient communication," *PNAS*) and the "efficient communication" literature (Gibson et al., 2019, "How Efficiency Shapes Human Language," *Trends in Cognitive Sciences*).
- **The bottleneck between internal representation and linguistic output** is discussed qualitatively in cognitive science (Vygotsky, 1934/1962; Fodor, 1975; Levinson, 2003) but is not typically formalised in channel-capacity terms.
- **Deletang et al. (2024)** frame LM as compression but do not frame the output loop as sequential coding through a capacity-limited channel.

### Status: Genuinely novel — handle with care

- **Well-established foundation:** Shannon's channel capacity theorem; the mathematics of sequential/successive coding; the empirical observation that internal representations are high-dimensional while outputs are low-dimensional.
- **Novel synthesis:** Framing the autoregressive loop specifically as sequential coding through a bandwidth-limited channel. This is the paper's own contribution.
- **The biological parallel** (Vygotsky's inner-to-external speech as the same bottleneck) gives this claim its sharpest form but also makes it the most ambitious. The claim that the constraint is "information-theoretic, not substrate-specific" is a strong universality claim.

### Can the claim be defended?

Yes, but it requires careful statement:

1. **The mathematical facts are clear:** Internal representations (e.g., residual stream vectors in transformers, ~12,000+ dimensional continuous vectors) have far higher entropy than per-token output (log₂|V| ≈ 15–17 bits for typical vocabularies of 32k–128k tokens, and effective entropy is lower due to non-uniform distribution).
2. **The sequential coding interpretation follows logically:** If you must transmit a high-entropy source through a low-capacity channel, you need multiple channel uses. The autoregressive loop provides exactly that.
3. **The novelty is in making this explicit and drawing consequences.** The consequences are significant: it predicts that longer sequences can express higher-entropy internal states, that the quality of sequential coding matters (not just length but the informativeness of each token), and that the "projection bottleneck" has a precise information-theoretic characterisation.

### Where it gets speculative

- Whether internal representations actually *have* a well-defined "message" that is being "transmitted" through the output channel is debatable. The metaphor of transmission implies a pre-existing message that is encoded; in practice, the autoregressive process is generative (the "message" is constructed during transmission). The paper should address this: the generation process is better understood as *joint* source-channel coding, where the message and its encoding are determined simultaneously.
- The channel capacity framing treats each token as a channel use, but tokens are not independent channel uses — each conditions on all previous tokens. The effective capacity per token is not simply log₂|V|. Shannon's framework handles this (channel capacity with memory / feedback), but the paper should not oversimplify.

### Recommendations for the Paper

- This is one of the paper's most original ideas. Give it room but frame it carefully.
- Lead with the mathematical observation: dimensionality mismatch between internal representation and output vocabulary. This is factual and striking.
- Introduce the sequential coding framing as "a natural formalisation" rather than a proof. The claim is that the information-theoretic framework *illuminates* the autoregressive loop, not that the autoregressive loop was designed as a Shannon coding scheme.
- Address the joint source-channel coding issue briefly: "The autoregressive process does not transmit a pre-existing message; it constructs and transmits simultaneously. This is analogous to joint source-channel coding, where the encoding adapts to the channel in real time."
- The connection to Vygotsky is evocative and useful but should be clearly flagged as an analogy supported by structural similarity, not a formal equivalence.

---

## Summary Table: Support Levels for Key Claims

| Claim | Support Level | Key Gap |
|-------|--------------|---------|
| The compression hierarchy maps onto rate-distortion problems with different relevance criteria | **Solid foundation, novel synthesis** | No prior work states this exact mapping. The ingredients are all established; the synthesis is the paper's own. |
| Layers solve rate-distortion problems with progressively more abstract relevance criteria | **Well-supported** | Probing studies confirm the empirical gradient; the rate-distortion framing is the paper's contribution. |
| Statistical complexity is the right measure for what grows across layers | **Theoretically grounded, empirically untested** | No one has measured Cμ across DNN layers. Proxy measures (intrinsic dimensionality) exist. |
| The DPI permits growth of statistical complexity because Cμ is not MI with the source | **Logically sound** | Correct formal argument; not previously stated in this context. |
| IB tracks discarding; the paper tracks reorganisation; these are complementary | **Strong, defensible reframing** | Implicit in Achille & Soatto; novel as an explicit claim. |
| The autoregressive loop is sequential coding through a bandwidth-limited channel | **Genuinely novel** | No prior work frames it this way. The mathematical ingredients are solid. |
| The projection bottleneck is information-theoretic, not substrate-specific | **Novel universality claim** | Supported by structural analogy; not proven. |

---

## Cross-Cutting Recommendations

### 1. Measurement honesty as a feature, not a bug

The paper should lean into the measurement difficulty rather than hiding from it. The Saxe/Shwartz-Ziv debate is not a liability — it is evidence that information-theoretic quantities in deep networks are hard to measure. The paper's framework sharpens *predictions* (what should be measured, what direction of change would confirm or disconfirm the framework) without claiming to solve the measurement problem. This is the correct epistemic stance for a theoretical paper.

### 2. The Achille & Soatto (2018) connection

This paper is the single closest precursor to several of the paper's claims. It shows that:
- Minimal sufficient statistics for the task naturally arise from a rate-distortion / IB-like objective.
- These statistics are invariant and disentangled — they have *structure* beyond what MI with the input captures.
- The DPI is compatible with (indeed requires) reorganisation of information.

Cite it prominently and distinguish the paper's contribution from it clearly.

### 3. What's genuinely novel

The paper's strongest original contributions in Section 2 are:
1. The explicit mapping of the compression hierarchy onto a hierarchy of rate-distortion problems with different relevance criteria.
2. The proposal of statistical complexity (Crutchfield) as the measure of what grows across layers, replacing β.
3. The framing of the autoregressive loop as sequential coding through a bandwidth-limited channel.
4. The synthesis: DPI constrains MI, not Cμ; IB tracks discarding, the framework tracks reorganisation; these are complementary.

These are all defensible, logically coherent, and grounded in established theory. But they are genuinely novel syntheses, not restatements of existing work. The paper should own this — "We propose..." not "It is well known that..."

### 4. Papers to search for (post-2025)

- Any work measuring statistical complexity or ε-machines in neural network representations.
- Recent work on rate-distortion theory in transformers specifically (not just DNNs generally).
- Updates to the IB debate (new estimation methods, new architectures tested).
- Work on model collapse (Shumailov et al., 2024, "AI models collapse when trained on recursively generated data," *Nature*) — relevant to Section 6 but may also bear on the information-theoretic grounding.
- Any work formalising autoregressive generation as a coding problem.

### 5. Additional References to Consider

- **Kolchinsky, A. & Tracey, B.D. (2018).** "Caveats for Information Bottleneck in Deterministic Scenarios." *ICLR 2018*. Important for understanding when IB applies and when it doesn't.
- **Gabrié, M., Manoel, A., Luneau, C., Barbier, J., Macris, N., Krzakala, F., & Zdeborová, L. (2018).** "Entropy and Mutual Information in Models of Deep Neural Networks." *NeurIPS 2018*. Statistical physics perspective on information in deep networks.
- **Goldfeld, Z. & Polyanskiy, Y. (2020).** "The Information Bottleneck Problem and Its Applications in Machine Learning." *IEEE Journal on Selected Areas in Information Theory*. Good review for citing the state of the field.
- **Piantadosi, S.T., Tily, H., & Gibson, E. (2011).** "Word Lengths Are Optimized for Efficient Communication." *PNAS*. Supports the channel-capacity framing for natural language.
- **Jawahar, G., Sagot, B., & Seddah, D. (2019).** "What Does BERT Learn about the Structure of Language?" *ACL 2019*. Empirical evidence for the layer-wise gradient from surface to abstract features.
- **Tenney, I., Das, D., & Pavlick, E. (2019).** "BERT Rediscovers the Classical NLP Pipeline." *ACL 2019*. Same empirical gradient.

---

*Report compiled March 2026. Web search was unavailable; all citations are from literature known through early 2025. Recommend targeted searches for recent work before finalising Section 2.*
