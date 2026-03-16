# Title TBD
*Restructured Outline*

---

## Abstract

Core thesis in three moves: (1) The effectiveness of large language models reflects hierarchical multi-scale compression — organisational and semantic, not merely algorithmic — operating simultaneously within the forward pass and sequentially across the autoregressive loop. (2) The autoregressive loop is fundamentally ambivalent: it can enrich or degrade representational diversity through the same mechanism. (3) This ambivalence recurs at the ecological scale, where model outputs re-enter the knowledge ecosystem through nested feedback loops, threatening a silent flattening that preserves surface quality while eroding higher-order structure.

Information theory provides the natural formal language: rate-distortion theory characterises the hierarchy, the data processing inequality clarifies what depth can and cannot do, channel capacity formalises the projection bottleneck, and statistical complexity provides the measure of what grows across depth. The framework generates specific testable predictions and identifies representational diversity — the structural complexity of the configurations a system can reach — as the critical variable governing whether these systems enrich or impoverish the knowledge ecology they are entering.

---

## 1. The Compression Hierarchy

**Purpose:** Establish the central conceptual distinction. Short, decisive, no redundancy.

### Core claims:
- Data, information, and knowledge are not synonyms. The transitions between them require progressively deeper compression.
- Three levels, precisely distinguished:
  - **Algorithmic compression**: reduces bits. Exploits surface redundancy. Lossless or near-lossless. Does not generalise.
  - **Organisational compression**: reduces complexity by discovering structure. Encodes shape rather than instances. Generalises (grammar, taxonomy, game principles vs. memorised games).
  - **Semantic compression**: reduces conceptual distance. Builds navigable geometry where meaning is spatial. Supports inference through structure. This is what transformers do.
- The hierarchy is not substrate-specific. It describes a general property of systems that must compress knowledge for transmission. (Flagged here; developed in Section 4.)

### Key distinction from current version:
- Cut by ~40%. The taxonomy is clear within three paragraphs. Current version over-elaborates.

---

## 2. Information-Theoretic Foundations

**Purpose:** Ground the compression hierarchy in formal information theory. This replaces the Heaps' law apparatus as the theoretical backbone.

### 2.1 Rate-distortion theory and the hierarchy

- Rate-distortion formalises the core tradeoff: minimum bit rate to represent a source at a given distortion level.
- Crucially, "distortion" is defined relative to a *relevance criterion* — what counts as loss depends on what you're trying to preserve.
- The three compression levels map directly onto different rate-distortion problems:
  - Algorithmic: minimise rate, preserve surface fidelity
  - Organisational: accept surface distortion, preserve structural relationships
  - Semantic: accept further surface distortion, preserve meaning — navigability, inferential structure, analogical relations
- Each layer of a transformer can be understood as solving a rate-distortion problem where the relevance criterion shifts from surface statistics toward abstract relational structure as you ascend.
- **Claim:** This isn't analogy. It's direct application. The compression hierarchy *is* a hierarchy of rate-distortion problems with progressively more abstract relevance criteria.

### 2.2 The data processing inequality and the additive paradox

- The DPI: processing cannot increase mutual information about the source.
- Apparent tension with the central claim that layers *generate* new representational structure.
- Resolution — and this is a key move: what layers generate is not new *information about the input* but new *organisation* of existing information. Making implicit structure explicit. Surfacing regularities that were present but computationally inaccessible.
- The DPI holds (no new information created), but the *utility* of the representation increases because latent structure becomes manifest.
- **This is the precise, information-theoretically grounded version of the additive/subtractive distinction.** IB tracks mutual information reduction (subtractive, consistent with DPI). The present framework tracks something the DPI permits but doesn't measure: the reorganisation of preserved information into forms that support new kinds of inference.

### 2.3 Statistical complexity as the measure of what grows

- Introduce Crutchfield's excess entropy / statistical complexity: measures genuine structure in a process (distinguished from both randomness and simple order).
- **This is the replacement for β.** The claim that representational diversity grows across layers becomes: each layer increases the statistical complexity of the encoding.
- The DPI constrains total information; growth must therefore come from reorganisation, not creation. Statistical complexity tracks exactly this — how much structure is explicitly accessible in the representation.
- Growth rate of statistical complexity across depth is a formally defined, empirically measurable quantity grounded in information theory itself.
- Note on measurement difficulty: information-theoretic quantities in high-dimensional continuous spaces are hard to estimate (the Saxe/Shwartz-Ziv debate illustrates this). The formalisation sharpens predictions without solving the measurement problem. Be upfront about this.

### 2.4 Channel capacity and the projection bottleneck

- Shannon's noisy channel theorem: maximum rate of reliable transmission through a bandwidth-limited channel.
- The output vocabulary is a discrete channel. The autoregressive loop is serial transmission through it.
- Internal representations have entropy far exceeding per-token channel capacity.
- The autoregressive loop is a sequential coding scheme for transmitting a high-entropy source through a low-capacity channel.
- This formalises the projection bottleneck described informally in the current Section 4 (Vygotsky, inner/external speech) and gives the biological convergence argument its sharpest form: the constraint is information-theoretic, not substrate-specific.

### Structural note:
- The IB discussion from current 2.3 is retained but compressed — it becomes a contrast within 2.2 rather than a standalone subsection. The Saxe et al. / Shwartz-Ziv debate is acknowledged briefly as illustration of measurement difficulty, not given full treatment.

---

## 3. Representational Diversity Across Depth

**Purpose:** The architectural argument — how transformers specifically implement the information-theoretic framework from Section 2. This is current Section 2 rebuilt without Heaps' as load-bearing structure.

### 3.1 How transformers generate representational structure across depth

- Architectural mechanisms (carried forward, well-stated in current 2.2):
  - Attention as variable-scale compression (multiple heads = multiple simultaneous rate-distortion solutions at different scales)
  - Residual streams as accumulation (earlier organisations preserved alongside later ones — the accumulator)
  - Depth as recursive compression (compression of already-compressed representations surfaces progressively higher-order structure)
- **Key claim, now grounded:** Each layer increases the statistical complexity of the representation. The DPI means total information is bounded; what grows is the explicit accessibility of structure. Diminishing returns are expected — each layer operates on increasingly organised input, so the marginal structural novelty available decreases — but the structure that remains to be surfaced is higher-order and more powerful.
- This is what produces disproportionate returns on scale. Not merely "deeper is better" but: the *kind* of growth matters. Each layer adds qualitatively different structure than the one below.

### 3.2 Relationship to the information bottleneck

- Brief, focused contrast (not the extended treatment of current 2.3).
- IB describes what layers discard (input-specific noise). The present framework describes what layers generate (new organisation of preserved information). These are complementary, not competing.
- A layer that discards surface noise while introducing a higher-order abstraction is doing both simultaneously.
- Why the distinction matters: IB alone doesn't predict disproportionate returns on scale. Efficient noise removal makes you more efficient; it doesn't make you more *capable*. The generative side — growth of statistical complexity — is what accounts for capability emergence.

### 3.3 Emergent capabilities as threshold-crossing

- Carried forward from current 2.4, tightened.
- If statistical complexity grows across depth and scale, capabilities requiring specific structural configurations should appear when complexity crosses characteristic thresholds.
- Address the Schaeffer et al. metric-artefact challenge directly and concisely.
- The more precise prediction: capability onset correlates with identifiable thresholds of statistical complexity at relevant layers, regardless of whether the crossing *appears* discontinuous in any particular evaluation metric.

### 3.4 Empirical predictions

Stated cleanly, now grounded in information theory:

1. **Statistical complexity scaling with depth.** Measurable growth in statistical complexity (or proxy measures: intrinsic dimensionality, participation ratio) across layers, consistent with sublinear scaling as successive layers face diminishing marginal returns.
2. **Capability-complexity correlation.** Capability onset correlates with statistical complexity crossing identifiable thresholds at relevant layers — approximately constant across model sizes for a given capability.
3. **Residual stream as accumulator.** Statistical complexity grows faster with residual connections than without, because earlier organisations are preserved alongside later ones.
4. **Complementarity with IB compression.** Layers showing high IB compression (reduced MI with input) nonetheless show *growth* in statistical complexity. Negative correlation would be evidence against the framework.
5. **Qualitative shift across training.** (a) Statistical complexity growth across checkpoints follows power-law dynamics. (b) Early-training dimensions encode surface statistical regularities; late-training dimensions encode higher-order compositional structure. Qualitative prediction about the *type* of growth, not just tempo.

---

## 4. The Autoregressive Loop as a Distinct Compression Scale

**Purpose:** The temporal dimension. Everything in Section 3 occurs within a single forward pass. The autoregressive loop adds a qualitatively different scale. This is the paper's strongest original contribution and should be given room.

### 4.1 Two compression systems, one forward pass

- Carried forward from current 3.1, largely intact — this is well-written.
- Fixed weight geometry (static, vast — accumulated compression of training distribution) + dynamic context (shallow, narrow — running compression of current trajectory).
- Navigation, not reshaping. The geometry is constant; what changes is the path through it. But the combinatorial richness of available paths means the distinction nearly collapses in practice.
- Now formally grounded: the weight geometry defines the channel (in the information-theoretic sense); the context determines which signal is being transmitted through it.

### 4.2 Compositional novelty from fixed geometry

- Carried forward from current 3.2.
- How traversal of a fixed geometry produces genuine novelty: compositional combination of individually learned regularities in unprecedented configurations.
- What this rules out: the model cannot produce outputs requiring regularities not encoded in the weights. Compositional novelty within the span of the geometry; silence beyond it.
- The predicted failure modes: confabulation (locally coherent but globally unmoored navigation) and the subtler failure of spurious cross-domain coherence (individually valid regularities that don't validly compose at their intersection).

### 4.3 The enriching and degrading regimes

- Core of current 3.3 — the paper's most important conceptual contribution.
- Context as ambivalent representational feedback. Each generated token either:
  - **Enriches**: surfaces genuinely new structure, changes the local geometry of what's probable next, opens new representational territory. The loop is doing compressive work.
  - **Degrades**: reinforces existing trajectory, reproduces known patterns, settles into attractor paths. Fluency preserved; diversity contracts.
- The governing variable is **compressive novelty** of each token relative to existing context.
- Neither regime is a fixed property of model or task. It's a property of the *interaction*: capacity × task demands × context seeding × generation parameters.
- **Degradation is invisible in surface metrics.** Fluency, grammaticality, coherence are properties of lower-level compression, maintained throughout. What degrades is higher-order statistical complexity. This is the framework's central warning.
- Information-theoretic restatement: in the enriching regime, each token increases the statistical complexity of the context. In the degrading regime, it increases length without increasing complexity — adding tokens without adding structure.

### 4.4 Chain-of-thought and in-context learning as steering strategies

- Carried forward from current 3.4.
- CoT: converts depth into length. Problems exceeding single-pass statistical complexity become tractable when intermediate steps progressively enrich context.
- CoT as steering: well-constructed chains keep each token in the enriching regime. Poorly constructed chains (restating premises, circling, predictable steps) are in the degrading regime despite having the surface form of reasoning.
- **Prediction:** CoT quality (measured by compressive novelty per step) should predict effectiveness better than chain length.
- In-context learning: examples as seeding strategies — positioning the trajectory's starting point in a productive region of the weight geometry.
- Unifying claim: CoT, ICL, and prompting strategies generally are instances of a single dynamic — steering the autoregressive loop into the enriching regime by managing what enters the context.

### 4.5 Limitations

- Finite context window as hard upper bound on temporal compression depth.
- Two separable sources of degradation in long generation: attentional (architectural ceiling) and compositional (regime drift). Concurrent but distinct.
- The novelty account is *compositional*. Whether genuinely new abstractions or regularity types can emerge within the loop (vs. requiring weight updates) is an open question.

---

## 5. Structural Convergence Across Substrates

**Purpose:** The biological parallel, substantially tightened. Argue for convergence precisely, concede limitations honestly, and move on. This is supporting evidence, not a core pillar.

### 5.1 The projection bottleneck as substrate-independent constraint

- Now grounded formally via channel capacity (from 2.4).
- Both biological cognition and transformers face the same information-theoretic constraint: internal representations with entropy exceeding output channel capacity, requiring serial coding through a low-bandwidth channel.
- Vygotsky's inner/external speech distinction as the best-documented case in the biological literature. Brief treatment — the point is made quickly once the formal groundwork is in place.
- Fodor's Language of Thought: the structural claim (output underdetermines internal representation) is widely shared even among those who reject Fodor's specifics.

### 5.2 Convergence and its limits

- The convergence is structural, not mechanistic. Same problem → same type of solution. Birds and aircraft.
- Acknowledge the specific disanalogy: biological co-evolution (Deacon). Language and neural architecture mutually shaped each other across evolutionary time. Transformers adapt to language; language doesn't adapt to transformers. RLHF partially closes this gap but remains weak-sense feedback, not co-evolution.
- Levinson's cross-linguistic spatial cognition work as evidence that the compression medium reshapes internal representation in biology — a feedback loop absent in the transformer case.
- **What convergence explains:** the effectiveness of transformers is less surprising than it appears — hierarchical multi-scale compression is what the problem demands.
- **What it doesn't explain:** whether compression built from text alone (no grounding, no embodiment, no co-evolution) supports the same depth and robustness as its biological counterpart. This is empirically approachable (representational similarity analysis across biological and artificial systems) but unresolved.
- **Open question flagged explicitly:** the grounding problem as a question about rate-distortion — whether solving rate-distortion problems against increasingly abstract relevance criteria *requires* grounding in sensorimotor experience, or whether the statistical structure of language is sufficient.

### Structural note:
- Target ~60% of current Section 4 length. Remove anything that doesn't directly serve the convergence argument or honestly state its limits.

---

## 6. Knowledge Ecology and the Recursive Loop

**Purpose:** Scale up. The same ambivalent dynamic from Section 4.3, operating at ecological timescales through nested feedback loops. This is where the framework becomes consequential.

### 6.1 Carriers and the ecology of persistence

- Knowledge persistence requires carriers — systems changed by what passes through them, transmitting that change forward.
- Humans have never persisted knowledge through neural plasticity alone. The unit of persistence is the *ecology*: neural plasticity + external stores + cultural practices + transmission channels.
- Language models are not outside this ecology. They read from it (training) and write into it (outputs). They are a novel node type: one that compresses the ecology's accumulated stores and writes compressed outputs back into them.

### 6.2 The carrier asymmetry

- What models lack: intra-trajectory persistence. Context closes → accumulated state lost. Next conversation starts from same weights.
- Humans have endogenous persistence (neural state carries forward). Models have exclusively exogenous persistence (deposit into broader ecology or lose it).
- **But:** the asymmetry is not between processing capacity and its absence. Models may be among the most powerful knowledge-processing systems ever built. The limitation is what happens *after* processing — results exit entirely, dependent on external carriers.
- **Binding constraint:** not generation (superabundant) but reception and integration — the bandwidth and integrative capacity of other ecological nodes that must receive, validate, and carry forward what models produce.

### 6.3 Nested feedback loops

- The ecology is recursive. Model outputs re-enter the stores from which future training corpora are drawn.
- **Four nested loops, operating at progressively longer timescales:**
  1. **Within-context:** generated tokens feeding back as input to subsequent generation (Section 4.3's enriching/degrading dynamic)
  2. **Agentic:** persistent memory, tool use, multi-session accumulation — models writing to external state without human intermediary at each step
  3. **Human-mediated:** model outputs integrated by human carriers — edited, curated, published, taught, institutionalised
  4. **Training-distributional:** model outputs entering the training data of successor models
- **Same governing variable at every scale:** the compressive novelty of what feeds back relative to what is already present.
- **Same degradation shape at every scale:** surface quality preserved, higher-order statistical complexity erodes. Not visible failure but silent flattening.

### 6.4 The specific prediction: upward-cascading erosion

- Degradation is non-uniform. The compression hierarchy predicts it erodes from the top down:
  - First to go: novel abstraction, cross-domain connection, structural surprise (high-level semantic compression)
  - Last to go: fluency, grammaticality, local coherence (algorithmic and low-level organisational compression)
- This is the "model collapse" concern (Shumailov et al.) given a precise characterisation: not collapse of quality but contraction of the space of reachable configurations. Representational diversity narrows while surface metrics remain stable or even improve.
- **Human curation as the primary defence.** At the human-mediated loop, human carriers perform selection — choosing what to integrate, what to discard, what to elevate. This is the principal mechanism keeping the ecology in the enriching regime. Its declining effectiveness (as volume overwhelms curation capacity) is a critical variable.
- **Open question on detection:** How do you measure silent flattening? The framework needs to identify non-surface metrics that would reveal it — distributional signatures, diversity measures on generated corpora, structural properties of the representation space. This is honestly flagged as an unresolved problem the framework creates for itself.

### 6.5 The eroding asymmetry

- Brief section. The carrier asymmetry (6.2) is historically contingent and actively eroding.
- Agentic architectures, persistent memory, tool use → models transitioning from memoryless processors to persistent ecological participants.
- By the logic of the framework, this is the most consequential threshold: from processor to carrier. Not a distant prospect — components assembling now.

---

## 7. Open Questions and Limitations

**Purpose:** Honest accounting of what the framework doesn't resolve, stated as research questions rather than hand-waving.

### Formal:
- Can statistical complexity across layers be reliably measured in practice, given known difficulties with information-theoretic estimation in high-dimensional spaces? If not, what proxy measures are adequate?
- The relationship between rate-distortion optimality at different relevance criteria and the actual learned representations — is the rate-distortion framing descriptive (a useful vocabulary for what's happening) or prescriptive (the system is actually solving rate-distortion problems)?

### Architectural:
- Where exactly is the boundary between compositional novelty (new combinations of known regularities) and genuine conceptual novelty (new regularity types)? Can this be formalised?
- Does the enriching/degrading regime distinction admit of continuous measurement, or is it better understood as a tendency with no sharp threshold?

### Ecological:
- What are the timescales of training-distributional feedback, and how do they interact with the shorter loops?
- Can upward-cascading erosion of representational diversity be detected before it becomes severe? What are the early indicators?
- Is there a critical fraction of model-generated content in the training distribution beyond which degradation becomes self-reinforcing? Can this be characterised formally?

### Convergence:
- Does the compression hierarchy require sensorimotor grounding to achieve full depth, or is linguistic statistical structure sufficient? (The grounding problem as a rate-distortion question.)
- What would systematic divergence in representational geometry between biological and artificial systems tell us about the limits of convergence?

---

## 8. Conclusion

- **The single-variable claim, restated with care.** Statistical complexity — the structural complexity of configurations a system can reach — is a summary statistic, not a causal lever. But it is the right summary statistic: what the compression hierarchy produces, and what the recursive loops threaten.
- **Shannon's foundational insight as closing frame.** Information is surprise. The framework is, at root, about whether systems optimised for producing unsurprising output (fluent, coherent, high-probability) preserve or destroy the capacity for surprise at higher levels of description. The nested loops optimise for the unsurprising. The compression hierarchy generates the surprising. Both are accelerating through the same architectures.
- **Final move:** the framework identifies what to watch and warns that the answer won't be found in surface metrics. Restated without the extended poetic register of the current conclusion — one paragraph, not three.

---

## Structural Notes

**Total target length:** ~60-70% of current paper. Major savings from:
- Section 1 compressed (~40% shorter)
- Section 5 (biological) compressed (~40% shorter)
- IB discussion integrated rather than standalone
- Conclusion tightened substantially
- Heaps' apparatus removed throughout (no β, no β-amplifier, no Heaps' law invocations)

**New material required:**
- Section 2 (information-theoretic foundations) is substantially new
- Section 7 (open questions) is new as a standalone section
- Connections from information-theoretic grounding into Sections 3, 4, and 6 need threading through

**What's preserved largely intact:**
- Autoregressive loop analysis (current 3.1-3.3) — the paper's strongest material
- Enriching/degrading regime distinction
- CoT and ICL reframing
- Ecological feedback loop structure
- Carrier asymmetry analysis

**Key vocabulary changes:**
- "β" / "β amplifier" → "statistical complexity" / "structural complexity growth"
- "β-degradation" → "erosion of statistical complexity" / "representational diversity contraction"
- "Representational vocabulary" → "representational diversity" or "statistical complexity" depending on context
- "Dynamic β-elevation" → eliminated; replaced by enriching/degrading regime language (already present)