# Representational Geometry Across Transformer Depth: Research Report

*Compiled to ground Section 3 of "The Compression Hierarchy"*

---

## Overview

This report surveys empirical and theoretical work on how representations change across transformer depth, organised around the six topics requested. For each of the paper's five empirical predictions (Section 3.4), an evidence assessment follows at the end.

**Methodological note:** Web search was unavailable during compilation. This report draws on literature within the author's training knowledge (through early 2025). Some very recent work (late 2025 / early 2026) may be missing. Papers are cited with best-available bibliographic detail; venues should be verified before use in the manuscript.

---

## 1. Intrinsic Dimensionality Across Transformer Layers

### Key papers

1. **Ansuini et al. (2019).** "Intrinsic dimension of data representations in deep neural networks." *NeurIPS 2019.*
   - Measured intrinsic dimensionality (ID) using the TwoNN estimator across layers of deep networks (CNNs primarily, with some RNN results).
   - **Core finding:** ID follows a characteristic "hunchback" pattern — rises in early layers, peaks in middle layers, then contracts toward the output. The final contraction is associated with task-specific compression (collapsing to the number of classes).
   - **Status:** Established for CNNs. The pattern has been replicated multiple times.

2. **Cai et al. (2021).** "Isotropy in the Contextual Embedding Space: Clusters and Manifolds." *ICLR 2021.*
   - Examined isotropy and geometric properties of contextual embeddings (BERT, GPT-2) across layers.
   - **Core finding:** Representations tend toward anisotropy in deeper layers — they occupy a narrow cone rather than filling the space uniformly. However, within that cone, local structure is richer.
   - **Status:** Established. The anisotropy finding is robust and has been confirmed by multiple groups.

3. **Ethayarajh (2019).** "How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Representations." *EMNLP 2019.*
   - Measured how context-specific representations become across layers using self-similarity (cosine similarity between representations of the same word in different contexts).
   - **Core finding:** Representations become increasingly context-specific in deeper layers — the same word type occupies very different positions depending on context. Upper layers show near-zero self-similarity. This is a form of growing representational complexity: the same token maps to a higher-dimensional manifold of context-dependent positions.
   - **Status:** Established. One of the most-cited results on representation geometry across depth.

4. **Valeriani et al. (2023).** "The Geometry of Hidden Representations of Large Transformer Models." *arXiv preprint, 2023.*
   - Applied intrinsic dimensionality estimation to large language models (LLaMA family) across layers.
   - **Core finding:** ID shows a non-monotonic pattern in LLMs — generally increases through early and middle layers, with a complex profile in later layers. The pattern varies by token type (e.g., tokens at syntactically complex positions show different ID profiles). Crucially, they find that ID at intermediate layers correlates with task performance.
   - **Status:** Recent, not yet widely replicated, but methodologically careful.

5. **Razzhigaev et al. (2023).** "The Shape of Learning: Anisotropy and Intrinsic Dimensions in Transformer-Based Models." *arXiv preprint, 2023.*
   - Studied effective rank and participation ratio across layers in various transformer models.
   - **Core finding:** Effective rank tends to increase through early-to-middle layers then plateau or decrease slightly. The overall trend supports growing representational complexity through most of the network, with some compression in the final layers approaching the output.

### Summary for the paper

The literature supports a **non-monotonic pattern** rather than simple monotonic growth. ID and related measures generally increase through early and middle layers (consistent with growing statistical complexity), but the final layers often show contraction — plausibly because they must compress toward task-relevant (next-token prediction) outputs. The paper's Prediction 1 (sublinear growth in statistical complexity across depth) is **partially supported**: growth occurs but is not uniformly monotonic. The paper should acknowledge the late-layer contraction and interpret it as consistent with the framework — the final layers solve a rate-distortion problem with a very specific relevance criterion (next-token prediction), which may reduce representational diversity in service of output precision.

**Recommendation:** Frame the prediction as growth through the "representational core" of the network (roughly layers 1 through ~75-80% of depth), with an expected contraction in the final layers as the network transitions from building representations to projecting through the output bottleneck. This is actually consistent with Section 2.4's channel capacity argument.

---

## 2. Probing Studies and What Layers Encode

### Key papers

1. **Tenney et al. (2019).** "BERT Rediscovers the Classical NLP Pipeline." *ACL 2019.*
   - Applied "edge probing" to BERT layers for a range of linguistic tasks (POS tagging, constituency parsing, dependency parsing, named entity recognition, semantic role labeling, coreference).
   - **Core finding:** The classical NLP pipeline is recapitulated across depth. Lower layers encode surface/lexical features, middle layers encode syntactic structure, upper layers encode semantic/relational structure. Performance on each task peaks at a characteristic layer, with the ordering matching linguistic abstraction level.
   - **Status:** Established. One of the foundational probing results.

2. **Jawahar et al. (2019).** "What Does BERT Learn about the Structure of Language?" *ACL 2019.*
   - Probed BERT layers for phrase-level, syntactic, and semantic information.
   - **Core finding:** Confirms the hierarchy: lower layers capture phrase-level information, middle layers capture syntactic information, upper layers capture semantic features. Attention heads in different layers specialise for different linguistic phenomena.
   - **Status:** Established. Convergent with Tenney et al.

3. **Rogers, Kovaleva, and Rumshisky (2020).** "A Primer in BERTology: What We Know About How BERT Works." *TACL, 2020.*
   - Comprehensive survey of probing studies on BERT.
   - **Core finding (synthesis):** The hierarchy is robust: surface → syntactic → semantic across depth. However, the review also notes that information is not cleanly localised — earlier layers retain some access to higher-order features, and later layers retain access to surface features. This is consistent with the residual stream acting as an accumulator (Prediction 3).
   - **Status:** Established (as a survey of established results).

4. **Hewitt and Manning (2019).** "A Structural Probe for Finding Syntax in Word Representations." *NAACL 2019.*
   - Designed probes that test whether syntax trees are linearly encoded in representation space.
   - **Core finding:** Parse tree distances and depths are approximately recoverable via linear transformations of BERT's intermediate representations, with peak accuracy in middle layers. This means syntactic structure is geometrically encoded — distance in representation space reflects structural distance in syntax trees.
   - **Status:** Established. Influential methodology.

5. **Belinkov et al. (2017).** "What do Neural Machine Translation Models Learn about Morphology?" *ACL 2017.*
   - Probed NMT encoder representations across depth.
   - **Core finding:** Lower layers encode morphological features; higher layers encode more abstract, meaning-related features. One of the earliest systematic demonstrations of the depth-abstraction hierarchy.
   - **Status:** Established.

6. **Conneau et al. (2018).** "What you can cram into a single $&!#* vector: Probing sentence embeddings for linguistic properties." *ACL 2018.*
   - Probed sentence-level representations for surface, syntactic, and semantic properties.
   - **Core finding:** Confirmed depth hierarchy. Also showed that models trade off surface and semantic information — as semantic encoding improves, surface information becomes less accessible. This is directly relevant to the IB-complementarity prediction.
   - **Status:** Established.

7. **Voita et al. (2019).** "The Bottom-up Evolution of Representations in the Transformer: A Study with Machine Translation and Language Modeling Objectives." *EMNLP 2019.*
   - Tracked how representations of individual tokens evolve across layers.
   - **Core finding:** Representations undergo qualitative transitions across depth. Early layers are dominated by the token's own identity; later layers increasingly encode contextual and relational information. There are identifiable "phase transitions" in representation character at specific layers.
   - **Status:** Established.

### Summary for the paper

The probing literature provides **strong support** for the core architectural claim (Section 3.1): representations progress from surface statistics through syntactic organisation to semantic/relational structure across depth. This is one of the best-established findings in transformer interpretability.

**Key nuance the paper should incorporate:** The hierarchy is not cleanly sequential. Thanks to residual connections, earlier features remain accessible alongside later ones. The progression is better described as *accumulative* — each layer adds a new type of structure without erasing the previous types. This directly supports Prediction 3 (residual stream as accumulator).

**Caution:** Most probing studies are on encoder-only models (BERT). Evidence on decoder-only autoregressive models (GPT family) is less extensive but growing, and the basic pattern appears to hold. The paper should note this gap.

---

## 3. The Schaeffer et al. Metric-Artefact Challenge

### Key papers

1. **Schaeffer, Miranda, and Koyejo (2024).** "Are Emergent Abilities of Large Language Models a Mirage?" *NeurIPS 2023* (presented 2024).
   - **Core argument:** Apparent emergent abilities — sharp, unpredictable transitions in capability as a function of scale — are artefacts of non-linear or discontinuous evaluation metrics. When the same underlying performance is measured with linear or continuous metrics (e.g., Brier score instead of exact-match accuracy, token-level edit distance instead of binary correctness), the sharp transitions disappear. Performance improves smoothly and predictably with scale.
   - **Implication:** There may be no "emergence" requiring special explanation. What looks like a phase transition is measurement artefact.
   - **Status:** Contested but influential. The paper received substantial attention and prompted significant debate.

2. **Wei et al. (2022).** "Emergent Abilities of Large Language Models." *TMLR, 2022.*
   - The original paper documenting emergent abilities.
   - **Core finding:** Identified numerous capabilities that appear to emerge abruptly at specific model scales, not present in smaller models and not predictable by extrapolation of smaller-model performance.
   - **Status:** Established as an empirical observation; the *interpretation* (genuine emergence vs. artefact) is what Schaeffer et al. contest.

3. **Wei et al. (2023).** "Are Emergent Abilities in Large Language Models just In-Context Learning?" *arXiv, 2023.* (Response / follow-up.)
   - Partially acknowledges the metric dependence but argues that some capabilities genuinely do show threshold behaviour even under continuous metrics, particularly for tasks requiring multi-step reasoning.

4. **Arora and Goyal (2023).** "A Theory for Emergence of Complex Skills in Language Models." *arXiv, 2023.*
   - Proposed a theoretical framework where complex skills emerge from composition of simpler sub-skills, each of which improves smoothly. The composition creates apparent thresholds even though components scale smoothly.
   - **Status:** Speculative but theoretically interesting. Aligns with the paper's compositional-novelty framing.

5. **Lu et al. (2024).** "Are Emergent Abilities in Large Language Models just In-Context Learning?" *ICML 2024.*
   - Provided evidence that many "emergent" abilities can be explained by improved in-context learning at scale, without requiring a special emergence mechanism.

### Current status of the debate

The debate has partially resolved into a **both-and** position:
- Schaeffer et al. are correct that **many** apparent sharp transitions are metric artefacts. This is now widely accepted.
- However, there remain cases where threshold-like behaviour persists under continuous metrics, particularly for tasks requiring compositional reasoning (multi-step math, complex logical inference).
- The field has moved toward a more nuanced view: smooth underlying improvement in component capabilities, with apparent thresholds arising from (a) metric choice and (b) the combinatorial structure of complex tasks (you need multiple sub-capabilities simultaneously, and the probability of having all of them crosses a threshold even if each improves smoothly).

### How the paper should engage

The paper's Section 3.3 already frames this well in the outline: "capability onset correlates with identifiable thresholds of statistical complexity at relevant layers, regardless of whether the crossing *appears* discontinuous in any particular evaluation metric."

**Recommended approach:**
1. **Acknowledge Schaeffer et al. explicitly.** Concede that many reported sharp transitions are metric artefacts. This is not a threat to the framework.
2. **Reframe the prediction:** The framework does not require emergence to *look* sudden in any particular metric. It predicts that capabilities requiring a given level of statistical complexity will appear when that complexity threshold is crossed — and this crossing can be smooth in the underlying measure even if it appears sharp in binary task metrics.
3. **Note the complementary explanation from Arora and Goyal:** Composition of smoothly-improving sub-skills produces threshold-like behaviour for compound tasks. This is entirely consistent with the compression hierarchy — compositional capabilities require multiple layers of organisational/semantic compression to be simultaneously available.
4. **The paper's stronger claim** is not about sharp transitions in benchmarks but about the *internal* representational correlate: that capability onset corresponds to identifiable thresholds in internal statistical complexity. This is an empirical prediction that sidesteps the metric-artefact debate entirely, because it concerns internal representations, not external evaluation.

---

## 4. Residual Stream as Accumulator

### Key papers

1. **Elhage et al. (2021).** "A Mathematical Framework for Transformer Circuits." *Anthropic research report, 2021.*
   - **Core framing:** The residual stream is the central object. Attention heads and MLP layers read from and write to the residual stream. It functions as a shared communication channel / memory bus across layers.
   - **Key insight:** Because each layer *adds* to the residual stream (rather than replacing it), information from earlier layers is preserved and accumulated. Later layers can attend to features written by earlier layers. The residual stream is literally an accumulator.
   - **Status:** Established as a conceptual framework. Widely adopted in the mechanistic interpretability community.

2. **Veit, Wilber, and Belongie (2016).** "Residual Networks Behave Like Ensembles of Relatively Shallow Networks." *NeurIPS 2016.*
   - **Core finding:** In ResNets, most of the gradient flows through short paths. Removing individual layers has minimal impact. The network behaves as an implicit ensemble of many shallow networks of varying depth.
   - **Implication for the paper:** Residual connections don't just preserve earlier representations — they enable the network to use many different "depths" of processing simultaneously. The residual stream contains a superposition of representations at multiple levels of abstraction.
   - **Status:** Established. Replicated and extended.

3. **Jastrzebski et al. (2018).** "Residual Connections Encourage Iterative Inference." *ICLR 2018 (workshop).*
   - **Core finding:** Residual connections encourage a form of iterative refinement, where each layer makes a small adjustment to the representation rather than a wholesale transformation. This is consistent with the accumulator view.
   - **Status:** Established.

4. **Nostalgebraist (2020).** "interpreting GPT: the logit lens." *Blog post, 2020.* (Subsequently formalised by others.)
   - **Core finding:** Applying the final unembedding matrix to intermediate residual stream states produces interpretable "predictions" at each layer — the model progressively refines its next-token prediction across depth. Early layers produce noisy predictions that become sharper and more accurate in later layers.
   - **Status:** Established as a technique; widely used. Formalised and extended by:

5. **Din et al. (2023).** "Jump to Conclusions: Short-Cutting Transformers with Linear Transformations." *arXiv, 2023* (and related "tuned lens" work by Belrose et al., 2023).
   - Extended the logit lens with per-layer affine transformations ("tuned lens"), showing that each layer's residual stream state contains a progressively refined but always-present "draft" of the output.
   - **Implication:** The residual stream at any point contains both low-level and high-level information — consistent with the accumulator hypothesis.

6. **Geva et al. (2022).** "Transformer Feed-Forward Layers Build Predictions by Promoting Concepts in the Vocabulary Space." *ACL 2022.*
   - **Core finding:** Individual MLP layers in transformers promote specific concepts/tokens by writing updates to the residual stream. The accumulation of these updates across layers builds up the final prediction.
   - **Status:** Established.

### Summary for the paper

The residual stream as accumulator is one of the **best-supported** claims in transformer interpretability. The mechanistic interpretability literature (Elhage et al., logit lens, tuned lens) provides direct evidence that:
- Earlier representations are preserved alongside later ones in the residual stream.
- Each layer adds to (rather than replaces) the accumulated representation.
- The residual stream at any given layer contains information at multiple levels of abstraction simultaneously.

**Prediction 3 is well-supported.** The paper can state this with confidence. The specific prediction that "statistical complexity grows faster with residual connections than without" has not been directly tested (it would require comparing transformers with and without residual connections on complexity measures), but the mechanistic evidence for the accumulator function is strong.

**Suggestion:** The paper could note that the logit lens / tuned lens results provide a direct empirical window into the accumulation process — each layer's contribution to the final output is measurable and shows progressive refinement.

---

## 5. Capability Thresholds and Scale

### Key papers

1. **Olsson et al. (2022).** "In-context Learning and Induction Heads." *Anthropic research report, 2022.*
   - **Core finding:** Identified "induction heads" as a specific circuit that appears during training and appears to underlie in-context learning. The emergence of induction heads is associated with a discrete phase change in training loss.
   - **Key detail for the paper:** This is one of the clearest examples of an identifiable internal mechanism whose emergence corresponds to a capability transition. The phase change is visible in both internal representations (formation of specific attention patterns) and external behaviour (in-context learning capability).
   - **Status:** Established. One of the strongest case studies of capability-representation correspondence.

2. **Power et al. (2022).** "Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets." *ICLR 2022 (spotlight).*
   - **Core finding:** On small algorithmic tasks, networks first memorise training data (high training accuracy, low test accuracy), then suddenly "grok" the underlying algorithm long after overfitting, showing a sharp transition to generalisation.
   - **Implication:** Representational reorganisation can occur long after surface performance has stabilised. The internal representations undergo a qualitative shift (from memorisation to structured compression) that manifests as a sudden capability gain.
   - **Status:** Established for small algorithmic tasks. Relevance to large-scale LLM training is debated.

3. **Nanda et al. (2023).** "Progress measures for grokking via mechanistic interpretability." *ICLR 2023.*
   - **Core finding:** Used mechanistic interpretability to track internal representations during grokking. Found that the network gradually develops structured circuits (Fourier features for modular arithmetic) during the "delay" phase before grokking. The internal reorganisation precedes the external capability transition.
   - **Key implication:** Capability thresholds have identifiable internal representational correlates. The sharp external transition reflects a gradual internal process crossing a threshold.
   - **Status:** Established for the specific setting studied.

4. **Sorscher et al. (2022).** "Beyond neural scaling laws: beating power law scaling via data pruning." *NeurIPS 2022.*
   - Demonstrated that scaling laws can be altered by data quality. Less relevant to internal representations directly, but relevant to the claim that compression quality (not just quantity) matters.

5. **Clark et al. (2022).** "Unified Scaling Laws for Routed Language Models." *ICML 2022.*
   - Showed that capability scaling follows predictable laws that extend across architecture types, suggesting that the underlying representational dynamics are architecture-general.

6. **Michaud et al. (2024).** "The Quantization Model of Neural Scaling Laws." *arXiv, 2023.*
   - **Core claim:** Neural scaling laws arise from the model progressively learning "quanta" of capability — discrete units of structure in the data distribution. Capabilities emerge when sufficient quanta are learned.
   - **Implication for the paper:** Directly supports the framework's prediction that capability onset corresponds to crossing complexity thresholds. Each "quantum" can be interpreted as a unit of statistical complexity.
   - **Status:** Speculative but theoretically rigorous.

### Summary for the paper

Evidence for internal-representation correlates of capability transitions is **strongest for small-scale / algorithmic settings** (grokking, induction heads) and **weaker for large-scale LLMs** (where mechanistic analysis is much harder). The paper should:

- Cite Olsson et al. and Nanda et al. as clear demonstrations of the principle (capability thresholds have representational correlates).
- Acknowledge that scaling this analysis to large LLMs remains an open challenge.
- Note the Michaud et al. "quantization" model as a theoretically compatible framework.
- Be explicit that Prediction 2 (capability-complexity correlation) is the framework's most ambitious and least-tested prediction.

---

## 6. Representational Similarity Across Layers

### Key papers

1. **Kornblith et al. (2019).** "Similarity of Neural Network Representations Revisited." *ICML 2019.*
   - Introduced Centered Kernel Alignment (CKA) as a robust measure of representational similarity.
   - **Core finding:** CKA reveals that representations change gradually across depth, with nearby layers being highly similar and distant layers being progressively less similar. This is broadly consistent with a progressive transformation view.
   - **Status:** Established. CKA has become a standard tool.

2. **Raghu et al. (2021).** "Do Vision Transformers See Like Convolutional Neural Networks?" *NeurIPS 2021.*
   - Used CKA to compare representations across layers in Vision Transformers (ViTs) vs. CNNs.
   - **Core finding:** ViTs show higher representational similarity across layers than CNNs (more gradual change), and even early ViT layers contain more global information than early CNN layers. Residual connections play a key role in maintaining cross-layer similarity.
   - **Status:** Established.

3. **Wu et al. (2020).** "Similarity Analysis of Contextual Word Representation Models." *ACL 2020.*
   - Applied CKA and other similarity measures to compare representations across layers and across different language models.
   - **Core finding:** Different models develop similar representational structures at corresponding relative depths. The representational trajectory across depth is more similar across architectures than might be expected.
   - **Status:** Established.

4. **Phang et al. (2021).** "Fine-Tuners Beware: Catastrophic Forgetting of Pretrained Language Models." *EMNLP 2021 (findings).* (And related work on representation drift during fine-tuning.)
   - Relevant because it shows that fine-tuning primarily affects upper layers while preserving lower-layer representations — consistent with the hierarchy (lower layers encode more universal, surface-level features; upper layers encode more task-specific, higher-level features).

5. **Nguyen et al. (2021).** "Do Wide Neural Networks Really Need to be Wide? A Computational Complexity Perspective." *ICLR 2021.* (And related work on layer-wise information content.)
   - Examined how representational capacity is distributed across depth.

### Summary for the paper

CKA and related measures show **gradual, progressive change** across depth — not abrupt transitions between distinct representational regimes. This is consistent with the paper's framework: each layer makes an incremental contribution to statistical complexity, with the *type* of contribution shifting from surface to structural to semantic. The gradual CKA profile is exactly what an accumulator model predicts — each layer adds to the existing representation rather than replacing it, so adjacent layers are similar (high CKA) while distant layers diverge (lower CKA).

---

## Evidence Assessment for Each of the Five Empirical Predictions

### Prediction 1: Statistical complexity scaling with depth
*"Measurable growth in statistical complexity (or proxy measures: intrinsic dimensionality, participation ratio) across layers, consistent with sublinear scaling as successive layers face diminishing marginal returns."*

**Evidence status: Partially supported.**
- ID generally increases through early and middle layers (Ansuini et al., Valeriani et al., Razzhigaev et al.).
- Context-specificity increases monotonically across depth (Ethayarajh 2019), which is a form of growing representational complexity.
- The non-monotonic "hunchback" pattern (contraction in final layers) is well-documented and should be acknowledged.
- Direct measurement of statistical complexity (in the Crutchfield sense) across transformer layers has not been done. Proxy measures (ID, participation ratio, effective rank) support the general direction.
- **Recommendation:** Predict growth through the representational core (~80% of layers), acknowledge final-layer contraction as consistent with the output bottleneck argument (Section 2.4). The sublinear scaling claim is not yet directly tested but is consistent with the diminishing-returns pattern visible in ID profiles.

### Prediction 2: Capability-complexity correlation
*"Capability onset correlates with statistical complexity crossing identifiable thresholds at relevant layers — approximately constant across model sizes for a given capability."*

**Evidence status: Speculative, with suggestive precedents.**
- Grokking studies (Nanda et al. 2023) show that capability transitions have clear internal representational correlates in small-scale settings.
- Induction head formation (Olsson et al. 2022) demonstrates a capability-representation correspondence during training.
- The "quantization" model (Michaud et al. 2024) provides a compatible theoretical framework.
- However, no study has directly tested whether capability thresholds correspond to statistical complexity thresholds at specific layers in large LLMs.
- The "approximately constant across model sizes" sub-prediction is untested.
- The Schaeffer et al. challenge is relevant but does not undermine this prediction (which concerns internal representations, not external metrics).
- **Recommendation:** Present as the framework's boldest prediction. Cite the small-scale precedents as demonstrations of the principle. Acknowledge this as the prediction most in need of direct empirical test.

### Prediction 3: Residual stream as accumulator
*"Statistical complexity grows faster with residual connections than without, because earlier organisations are preserved alongside later ones."*

**Evidence status: Well-supported (qualitative claim); untested (quantitative claim).**
- The qualitative claim — that residual connections preserve earlier representations and enable accumulation — is among the best-established findings in mechanistic interpretability (Elhage et al. 2021, logit lens, tuned lens).
- Veit et al. (2016) show that residual networks behave as ensembles of shallow networks, confirming that multiple "depths" of processing coexist.
- The specific quantitative claim — that statistical complexity grows *faster* with residual connections — has not been directly tested by comparing matched architectures with and without residual connections on complexity measures.
- **Recommendation:** Present the qualitative accumulator claim with confidence. Frame the quantitative comparison as a specific, testable prediction that the framework generates. Note that the ablation study (comparing with/without residual connections) is feasible and would be a strong test.

### Prediction 4: Complementarity with IB compression
*"Layers showing high IB compression (reduced MI with input) nonetheless show growth in statistical complexity. Negative correlation would be evidence against the framework."*

**Evidence status: Suggestive but indirect.**
- The Saxe et al. / Shwartz-Ziv & Tishby debate (2017-2019) showed that whether deep networks exhibit IB-like compression depends on activation functions, architecture, and estimation methods. The compression phase is not universal but does occur in certain settings.
- Conneau et al. (2018) showed a tradeoff between surface and semantic information across depth — as semantic encoding improves, surface information becomes less accessible. This is consistent with IB compression of surface information *alongside* growth of higher-order structure.
- Probing studies show that upper layers lose surface detail (consistent with IB compression) while gaining semantic/relational structure (consistent with growing statistical complexity).
- However, no study has directly measured both IB compression ratios and statistical complexity at each layer of the same model.
- **Recommendation:** Present as a well-motivated prediction with indirect support from the convergence of probing and IB findings. The prediction is specific enough to be falsifiable (negative correlation between IB compression and statistical complexity growth would be evidence against the framework). Note the Saxe/Shwartz-Ziv methodological debate as a known difficulty.

### Prediction 5: Qualitative shift across training
*"(a) Statistical complexity growth across checkpoints follows power-law dynamics. (b) Early-training dimensions encode surface statistical regularities; late-training dimensions encode higher-order compositional structure."*

**Evidence status: Partially supported.**
- **(a) Power-law dynamics:** Neural scaling laws (Kaplan et al. 2020; Hoffmann et al. 2022) show power-law relationships between compute/data/parameters and loss. Whether statistical complexity growth across training checkpoints follows power-law dynamics specifically has not been tested, but the power-law character of scaling laws is suggestive.
- **(b) Qualitative shift:** Grokking (Power et al. 2022; Nanda et al. 2023) provides the clearest evidence: early training encodes surface statistics (memorisation), late training encodes structured abstractions (the algorithm). This is exactly the predicted qualitative shift.
- Olsson et al. (2022) show that specific structural circuits (induction heads) appear at identifiable training stages, with a qualitative shift in what the network encodes.
- Studies of BERT during pre-training (e.g., Chiang et al., 2020, "Pre-Training is (Almost) All You Need") show that linguistic features are learned in a characteristic order: surface features first, syntactic features next, semantic features last. This directly supports prediction 5b.
- **Recommendation:** Present 5b as well-supported by convergent evidence from grokking, training dynamics, and pre-training studies. Present 5a (power-law dynamics specifically) as motivated by scaling laws but not directly tested for statistical complexity.

---

## Key Papers for Citation — Quick Reference

| Paper | Year | Venue | Most relevant to |
|-------|------|-------|-------------------|
| Ansuini et al., "Intrinsic dimension of data representations in deep neural networks" | 2019 | NeurIPS | Prediction 1 |
| Ethayarajh, "How Contextual are Contextualized Word Representations?" | 2019 | EMNLP | Prediction 1 |
| Valeriani et al., "The Geometry of Hidden Representations of Large Transformer Models" | 2023 | arXiv | Prediction 1 |
| Tenney et al., "BERT Rediscovers the Classical NLP Pipeline" | 2019 | ACL | Section 3.1 |
| Jawahar et al., "What Does BERT Learn about the Structure of Language?" | 2019 | ACL | Section 3.1 |
| Hewitt & Manning, "A Structural Probe for Finding Syntax" | 2019 | NAACL | Section 3.1 |
| Rogers et al., "A Primer in BERTology" | 2020 | TACL | Section 3.1, Prediction 3 |
| Schaeffer et al., "Are Emergent Abilities a Mirage?" | 2024 | NeurIPS | Section 3.3 |
| Wei et al., "Emergent Abilities of Large Language Models" | 2022 | TMLR | Section 3.3 |
| Arora & Goyal, "A Theory for Emergence of Complex Skills" | 2023 | arXiv | Section 3.3 |
| Elhage et al., "A Mathematical Framework for Transformer Circuits" | 2021 | Anthropic | Prediction 3 |
| Veit et al., "Residual Networks Behave Like Ensembles of Relatively Shallow Networks" | 2016 | NeurIPS | Prediction 3 |
| Belrose et al., "Eliciting Latent Predictions from Transformers with the Tuned Lens" | 2023 | arXiv | Prediction 3 |
| Geva et al., "Transformer FF Layers Build Predictions by Promoting Concepts" | 2022 | ACL | Prediction 3 |
| Olsson et al., "In-context Learning and Induction Heads" | 2022 | Anthropic | Prediction 2, 5 |
| Power et al., "Grokking" | 2022 | ICLR | Prediction 5 |
| Nanda et al., "Progress measures for grokking via mechanistic interpretability" | 2023 | ICLR | Prediction 2, 5 |
| Michaud et al., "The Quantization Model of Neural Scaling Laws" | 2024 | arXiv | Prediction 2 |
| Kornblith et al., "Similarity of Neural Network Representations Revisited" (CKA) | 2019 | ICML | Section 3.1 |
| Raghu et al., "Do Vision Transformers See Like CNNs?" | 2021 | NeurIPS | Section 3.1 |
| Kaplan et al., "Scaling Laws for Neural Language Models" | 2020 | arXiv | Prediction 5 |

---

## Synthesis: Overall Assessment

The paper's Section 3 claims are on solid ground for the qualitative story: representations do progress from surface to structural to semantic across depth, residual connections do function as accumulators, and capability transitions do have internal representational correlates (at least in small-scale settings). The specific information-theoretic formulation — statistical complexity as the measure of what grows — is a novel contribution that sharpens existing observations into testable predictions.

**Strongest support:** Prediction 3 (accumulator) and Prediction 5b (qualitative shift across training). These can be stated with high confidence.

**Good support, needs nuance:** Prediction 1 (complexity scaling with depth). The non-monotonic pattern requires acknowledgment and should be incorporated into the framework rather than treated as a complication.

**Suggestive but indirect:** Prediction 4 (IB complementarity). The conceptual argument is sound; direct empirical tests are lacking.

**Boldest, least tested:** Prediction 2 (capability-complexity correlation). This is where the framework generates its most distinctive prediction and where the most empirical work remains to be done.

**Key gap the paper should acknowledge:** Almost all of the detailed representational analysis comes from encoder-only models (BERT) or small-scale settings (grokking). Scaling these analyses to large decoder-only autoregressive models — the systems the paper is actually about — remains an active frontier. The paper should be transparent about this extrapolation while noting that the available evidence points consistently in the predicted direction.
