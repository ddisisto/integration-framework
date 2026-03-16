# Biological Convergence Evidence: Research Report for Section 5

Research compiled for "The Compression Hierarchy" v2 revision.

---

## 1. Representational Similarity Analysis (RSA) Across Biological and Artificial Systems

### Key papers

- **Kriegeskorte, N., Mur, M., & Bandettini, P. (2008).** "Representational similarity analysis -- connecting the branches of systems neuroscience." *Frontiers in Systems Neuroscience*, 2, 4. -- Introduced the RSA framework: compare systems by comparing their representational dissimilarity matrices (RDMs), abstracting away from the specific units/voxels/neurons.

- **Kriegeskorte, N. (2015).** "Deep neural networks: A new framework for modeling biological vision and brain information processing." *Annual Review of Vision Science*, 1, 417-446. -- Made the explicit case that deep CNNs trained on object recognition produce representations that, layer by layer, align with the ventral visual stream (V1 -> V2 -> V4 -> IT).

- **Yamins, D.L.K., Hong, H., Cadieu, C.F., Solomon, E.A., Seibert, D., & DiCarlo, J.J. (2014).** "Performance-optimized hierarchical models predict neural responses in higher visual cortex." *PNAS*, 111(23), 8619-8624. -- Showed that CNNs optimised for ImageNet performance (not for neural prediction) nonetheless predicted IT neural responses better than any previous model. This was a landmark result for convergence claims.

- **Schrimpf, M., Kubilius, J., Hong, H., Majaj, N.J., Rajalingham, R., Issa, E.B., Kar, K., Bashivan, P., Prescott-Roy, J., Geiger, F., Schmidt, K., Nayebi, A., Bear, D., Yamins, D.L.K., & DiCarlo, J.J. (2021).** "Brain-Score: Which artificial neural network for object recognition is most brain-like?" *bioRxiv* / later published work. -- Established Brain-Score, a composite benchmark measuring neural predictivity across visual areas. Found that better-performing networks tend to be more brain-like, but the correlation is imperfect and plateaus.

- **Conwell, C., Prince, J.S., Kay, K.N., Alvarez, G.A., & Konkle, T. (2023).** "What can 1.8 billion regressions tell us about the pressures shaping high-level visual representation in brains and machines?" *bioRxiv*. -- Large-scale comparison finding that task-optimised DNNs explain substantial variance in high-level visual cortex but the match is far from ceiling, and different architectures capture different aspects.

- **Goldstein, A., Zada, Z., Buchnik, E., Sber, M., Price, A.R., Aubrey, B., Nastase, S.A., Feder, A., Emanuel, D., Cohen, A., Jansen, A., Gazula, H., Choe, G., Patil, A., Honey, C., Gross, J., & Hasson, U. (2022).** "Shared computational principles for language processing in humans and deep language models." *Nature Neuroscience*, 25, 369-380. -- Extended RSA-style comparison to language: GPT-2 activations predict neural responses during natural language processing (measured via ECoG), with layer-wise alignment to temporal cortex processing stages.

### Core findings

1. **The convergence is real but partial.** Task-optimised DNNs trained on natural data produce internal representations that predict biological neural responses substantially better than hand-engineered features or random networks. This is a genuine empirical finding, not an artefact.

2. **The convergence is strongest for vision, weaker but present for language.** The visual case (Yamins et al., Kriegeskorte, Schrimpf) has the deepest evidence base. The language case (Goldstein et al.) is more recent and less extensively replicated but directionally consistent.

3. **Better task performance correlates with better neural prediction, but the correlation saturates.** The Brain-Score finding that more accurate networks are more brain-like suggests the convergence is driven by the task structure, not architectural coincidence. But the plateau means current networks are capturing something real about the problem without fully matching biological solutions.

4. **The match is better for higher-level representations than lower-level ones.** Early layers (V1-like features) are matched easily; the interesting convergence is at mid and higher levels, where organisational compression is doing the heavy lifting.

### Limitations and caveats

- **Neural predictivity != mechanistic identity.** RSA measures similarity of representational geometry, not of underlying computation. Two systems can have similar RDMs via completely different mechanisms.
- **The comparison is to *specific* brain measurements** (fMRI, ECoG, single-unit recordings), each with their own biases and resolution limits. fMRI measures hemodynamic responses, not neural codes directly.
- **Model selection bias.** Researchers naturally test models that seem likely to match. The space of models tested is a biased sample.
- **Explained variance is typically 30-60% at best** even for the best-matching layers and areas, meaning substantial divergence remains.
- **Language models and auditory/language cortex comparisons** are methodologically harder (temporal dynamics, context effects) and less mature than the visual literature.

### Current status: **Established** (convergence exists) with **contested** (interpretation and depth of convergence)

### Relation to the paper's claims

The RSA evidence directly supports the structural convergence argument: systems optimised for similar tasks on similar data converge on similar representational geometries, regardless of substrate. This is the paper's strongest empirical anchor for the convergence claim. However, the partial nature of the match (30-60% variance explained) equally supports the paper's honest acknowledgment that the convergence is structural, not mechanistic, and that grounding/co-evolution may account for the gap.

**Calibration for v2:** State confidently. The basic convergence finding is well-established. The interpretation (convergence driven by shared computational problem, not substrate similarity) is the mainstream reading. Hedge on depth: note that substantial unexplained variance remains and may reflect the grounding/co-evolution gap.

---

## 2. Vygotsky's Inner/External Speech Distinction

### Key papers

- **Vygotsky, L.S. (1934/1986).** *Thought and Language.* Translated and edited by A. Kozulin. Cambridge, MA: MIT Press. -- The foundational source. Inner speech is abbreviated, predicative, semantically dense, saturated with private context. External speech is grammatically expanded for intersubjective recovery.

- **Fernyhough, C. (2004).** "Alien voices and inner dialogue: Towards a developmental account of auditory verbal hallucinations." *New Ideas in Psychology*, 22(1), 49-68. -- Developed a model of inner speech development from Vygotskian principles.

- **Alderson-Day, B. & Fernyhough, C. (2015).** "Inner speech: Development, cognitive functions, phenomenology, and neuroscience." *Psychological Bulletin*, 141(5), 931-965. -- Major review of the inner speech literature. Confirms that inner speech is phenomenologically compressed relative to overt speech, but emphasises its heterogeneity: inner speech ranges from fully expanded (close to overt speech) to highly condensed.

- **Grandchamp, R., Rapin, L., Perrone-Bertolotti, M., Pichat, C., Haldin, C., Cousin, E., Lachaux, J.-P., Dohen, M., Perrier, P., Garnier, M., Baciu, M., & Loevenbruck, H. (2019).** "The ConDialInt model: Condensation, dialogicality, and intentionality dimensions of inner speech within a hierarchical predictive control framework." *Frontiers in Psychology*, 10, 2019. -- Proposes that inner speech exists on a continuum of condensation, not a binary compressed/expanded dichotomy.

- **Perrone-Bertolotti, M., Rapin, L., Lachaux, J.-P., Baciu, M., & Loevenbruck, H. (2014).** "What is that little voice inside my head? Inner speech phenomenology, its role in cognitive performance, and its relation to self-monitoring." *Behavioural Brain Research*, 261, 220-239. -- Reviews neural correlates; inner speech activates overlapping but not identical networks compared to overt speech.

### Core findings

1. **The basic distinction holds up well.** Inner speech is genuinely more compressed than external speech. This is supported by phenomenological, developmental, and neuroimaging evidence.

2. **But it is a continuum, not a binary.** Modern work emphasises that inner speech varies in its degree of condensation. Sometimes it is nearly as expanded as overt speech (e.g., when rehearsing what to say); sometimes it is highly abbreviated.

3. **No quantitative compression ratio exists.** There is no published figure for "the compression ratio between internal representation and linguistic output" in rigorous quantitative terms. The 39 bits/second speech bandwidth (Reed & Durlach) provides one side; the information content of neural population codes is estimated at orders of magnitude higher (possibly 10^7-10^8 bits/second for cortical population codes, though estimates vary enormously and depend on assumptions about coding). But these are not directly commensurable measurements.

4. **Neural correlates partially overlap.** Inner speech recruits left inferior frontal gyrus (Broca's area) and supplementary motor area, overlapping with overt speech production areas but with reduced motor execution components. This is consistent with the compression-of-the-same-content interpretation.

### Limitations

- **Phenomenological evidence is inherently limited.** Much of the evidence for inner speech compression relies on introspective reports, which are unreliable for the most condensed forms of inner speech (which may be precisely those least accessible to introspection).
- **The Vygotskian framework is developmental, not information-theoretic.** The mapping to compression/projection is productive but interpretive, not formal.
- **"Inner speech" may not be the right level of analysis.** Some researchers (e.g., Carruthers, 2018) argue that much of cognition does not involve inner speech at all, and that treating inner speech as the substrate of thought overestimates its role.

### Current status: **Established** (the distinction exists and inner speech is compressed) with **important nuances** (continuum, not binary; inner speech is not all of thought)

### Relation to the paper's claims

The Vygotsky parallel is the paper's most intuitive entry point for the projection bottleneck argument. The basic claim (internal representation is richer than its linguistic projection) is safe. The v1 draft's use of this is appropriate. For v2, the main refinement is: (a) acknowledge the continuum rather than implying a sharp binary, and (b) avoid implying that inner speech is the totality of internal representation -- it is one manifestation of a broader pattern.

**Calibration for v2:** State confidently as an illustration of the projection bottleneck. Do not claim a specific quantitative compression ratio. The qualitative point (internal representation richer than output) is well-supported.

---

## 3. Channel Capacity of Biological Communication

### Key papers

- **Reed, C.M. & Durlach, N.I. (1998).** "Note on information transfer rates in human communication." *Presence: Teleoperators and Virtual Environments*, 7(5), 509-518. -- Estimated information transfer rate of speech at approximately 39 bits/second. This is a widely cited estimate, though the methodology involves assumptions about phoneme information content.

- **Coupé, C., Oh, Y.M., Dediu, D., & Pellegrino, F. (2019).** "Different languages, similar encoding efficiency: Comparable information rates across the human linguistic spectrum." *Science Advances*, 5(9), eaaw2594. -- Found that despite variation in syllable rates across languages (from ~4 to ~8 syllables/second), information rates are remarkably similar: approximately 39 bits/second across 17 languages. Faster-spoken languages pack less information per syllable. This is a striking finding for the bottleneck argument.

- **Szekely, P., Korem, Y., Moran, U., Mayo, A., & Alon, U. (2015).** "The mass-longevity triangle: Pareto optimality and the geometry of life-history trait space." *PLoS Computational Biology*. -- Not directly relevant, but part of a broader literature on biological optimality under constraints.

- **Niven, J.E. & Laughlin, S.B. (2008).** "Energy limitation as a selective pressure on the evolution of sensory systems." *Journal of Experimental Biology*, 211, 1792-1804. -- Energy constraints on neural information processing as a fundamental bottleneck.

- **Levy, R. & Jaeger, T.F. (2007).** "Speakers optimize information density through syntactic reduction." *Advances in Neural Information Processing Systems* 20. -- Speakers adjust their speech to maintain relatively uniform information density, consistent with operating near channel capacity.

### On neural population code bandwidth

- **Georgopoulos, A.P., Schwartz, A.B., & Kettner, R.E. (1986).** "Neuronal population coding of movement direction." *Science*, 233, 1416-1419. -- Foundational work on population codes.

- Estimates of information in cortical population codes vary enormously depending on assumptions (independent vs. correlated neurons, temporal coding, etc.). A rough order of magnitude: a population of 10^4 neurons with ~10 discriminable firing rates each, updated at ~100 Hz, could in principle carry 10^5-10^6 bits/second if coding were efficient and independent. Real neural populations have enormous redundancy, so effective information rates are lower but still vastly exceed the 39 bits/second speech output.

### Core findings

1. **The ~39 bits/second figure is robust.** The Coupe et al. (2019) cross-linguistic replication is particularly striking: languages trade off syllable rate against information per syllable to arrive at approximately the same information rate. This suggests a fundamental channel capacity constraint, not a contingent property of any particular language.

2. **The bottleneck ratio is enormous.** Even conservative estimates of neural population coding bandwidth exceed speech output bandwidth by 3-4 orders of magnitude.

3. **Speakers behave as if operating near capacity.** The uniform information density findings (Levy & Jaeger) are consistent with speakers optimising their use of a bandwidth-limited channel.

### Limitations

- **"Bits per second" in speech involves assumptions** about the information content of phonemes, which depend on the language model used to estimate entropy. The 39 bits/second figure assumes a particular phoneme-level entropy estimate.
- **Neural population code bandwidth estimates are highly uncertain.** The comparison (10^5+ bits/sec internally vs. 39 bits/sec externally) is order-of-magnitude, not precise.
- **The bottleneck is not purely informational.** Motor constraints on articulation, real-time processing demands on the listener, and social coordination all contribute to limiting speech rate. It is not solely a Shannon channel capacity problem.

### Current status: **Established** (speech bandwidth is low and approximately constant across languages; internal bandwidth vastly exceeds it) with **caveats on precision**

### Relation to the paper's claims

This is excellent quantitative grounding for the projection bottleneck. The Coupe et al. cross-linguistic result is especially valuable: it suggests the bottleneck is not a contingent property of English but a constraint on human communication generally. The v1 draft cites Reed & Durlach; the v2 should add Coupe et al. (2019) as stronger evidence.

**Calibration for v2:** State confidently. The order-of-magnitude mismatch between internal bandwidth and output bandwidth is well-established. Cite Coupe et al. for the cross-linguistic invariance. Avoid implying precise ratio (e.g., "10,000:1") -- stick with "orders of magnitude."

---

## 4. Deacon's *The Symbolic Species*

### Key paper

- **Deacon, T.W. (1997).** *The Symbolic Species: The Co-evolution of Language and the Brain.* New York: W.W. Norton.

- **Deacon, T.W. (2012).** *Incomplete Nature: How Mind Emerged from Matter.* New York: W.W. Norton. -- Follow-up extending the argument into a broader theory of emergent properties and "absential" features.

### Core claims

1. **Language and the brain co-evolved.** The human brain was not a general-purpose computer to which language was added; neural architecture was substantially shaped by the demands of symbolic communication across evolutionary time.

2. **Symbolic reference is qualitatively different** from iconic and indexical reference (Peirce's trichotomy). The capacity for symbolic reference required reorganisation of prefrontal cortex and its connections, driven by selective pressure from the advantages of symbolic communication.

3. **The Baldwin effect** as mechanism: learned behaviours (proto-symbolic communication) created selective pressure for neural architectures better suited to those behaviours, without requiring Lamarckian inheritance.

### Reception and current status

- **Broadly well-received in anthropology and cognitive science** as a stimulating synthesis, though specific claims have been challenged.
- **The co-evolution thesis is mainstream** in broad strokes: the idea that language and brain co-evolved is widely accepted. The specific mechanisms Deacon proposes (particularly regarding prefrontal cortex reorganisation) are more contested.
- **Challenged by Chomsky/minimalist linguistics,** which favours a saltationist account (language faculty emerged relatively suddenly via a single mutation or small set of changes) rather than Deacon's gradualist co-evolutionary account. Berwick & Chomsky (2016), *Why Only Us*, present the alternative view.
- **Challenged on empirical specifics** by Fitch (2010), *The Evolution of Language*, who is sympathetic to co-evolution but disagrees with some of Deacon's neural claims.
- **Deacon's 2012 follow-up** was more philosophically ambitious and less well-received in empirical communities.
- **The Baldwin effect mechanism** has been supported by computational modelling (e.g., Kirby, Cornish, & Smith, 2008, on iterated learning showing how cultural transmission shapes language structure, though this is cultural rather than genetic evolution).

### Current status: **The broad co-evolution thesis is mainstream; specific mechanisms are contested; the philosophical extensions (2012) are speculative.**

### Relation to the paper's claims

The paper uses Deacon well -- as the source for the co-evolution disanalogy. The point is that biological cognition had a feedback loop (language reshaping neural architecture across evolutionary time) that transformers lack. This is a genuine and important disanalogy.

**Calibration for v2:** The co-evolution thesis can be stated confidently as mainstream in cognitive science and evolutionary anthropology (even if specific mechanisms are debated). The v1 draft's use of Deacon is appropriate and honestly framed. Keep the disanalogy argument; it's one of the paper's strengths that it acknowledges this honestly.

---

## 5. Levinson and Cross-Linguistic Spatial Cognition

### Key papers

- **Levinson, S.C. (2003).** *Space in Language and Cognition: Explorations in Cognitive Diversity.* Cambridge University Press. -- The major monograph presenting the Nijmegen group's findings.

- **Levinson, S.C., Kita, S., Haun, D.B.M., & Rasch, B.H. (2002).** "Returning the tables: Language affects spatial reasoning." *Cognition*, 84(2), 155-188.

- **Majid, A., Bowerman, M., Kita, S., Haun, D.B.M., & Levinson, S.C. (2004).** "Can language restructure cognition? The case for space." *Trends in Cognitive Sciences*, 8(3), 108-114.

- **Haun, D.B.M., Rapold, C.J., Call, J., Janzen, G., & Levinson, S.C. (2006).** "Cognitive cladistics and cultural override in Hominid spatial cognition." *PNAS*, 103(46), 17568-17573. -- Compared human spatial cognition across cultures with great apes; found that the "default" hominid strategy is geocentric (absolute), and relative-frame languages culturally override this default.

- **Li, P. & Gleitman, L. (2002).** "Turning the tables: Language and spatial reasoning." *Cognition*, 83(3), 265-294. -- Major challenge to Levinson's claims, arguing that apparent linguistic effects are artefacts of experimental design (particularly the role of environmental cues).

- **Li, P., Abarbanell, L., Gleitman, L., & Papafragou, A. (2011).** "Spatial reasoning in Tenejapan Mayans." *Cognition*, 120(1), 33-53. -- Further challenge showing that Tzeltal Mayan speakers (who use absolute spatial language) can use relative reasoning when environmental cues are controlled.

- **Majid, A., Boster, J.S., & Bowerman, M. (2008).** "The cross-linguistic categorization of everyday events: A study of cutting and breaking." *Cognition*, 109(2), 235-250. -- Extended the cross-linguistic influence findings beyond spatial cognition.

### Core findings and status of the debate

1. **The original Levinson findings are genuine.** Speakers of absolute-frame languages (e.g., Tzeltal Maya, Guugu Yimithirr) do behave differently on non-linguistic spatial reasoning tasks compared to speakers of relative-frame languages.

2. **The strong Whorfian interpretation has been significantly weakened.** Li & Gleitman (2002) and subsequent work showed that much of the effect is modulated by environmental cues. When landmarks are removed or controlled, the differences shrink substantially.

3. **The current consensus is a moderate position.** Language influences spatial reasoning strategies (which frame is preferentially recruited) but does not determine or fundamentally reshape internal spatial representation. Speakers of absolute-frame languages can use relative frames and vice versa; language biases which strategy is deployed by default.

4. **The "cultural override" finding (Haun et al., 2006) is interesting** but compatible with the moderate position: language/culture shifts the default strategy rather than eliminating alternatives.

5. **The field has moved toward "thinking for speaking" (Slobin, 1996)** as a middle ground: language influences cognition specifically when cognitive tasks are linked to linguistic encoding, rather than reshaping cognition across the board.

### Current status: **The strong claim (language reshapes internal spatial representation) is contested and largely retreated from. The moderate claim (language influences default cognitive strategies) is established.**

### Relation to the paper's claims

The v1 draft uses Levinson to argue that "the compression medium is reaching back and reshaping the compressed content." This is the strong Whorfian reading, which has been weakened. For v2, recalibrate:

**Calibration for v2:** The Levinson work should be described more carefully. The finding is that language biases which cognitive strategies are preferentially deployed, not that it fundamentally reshapes internal representation. This actually still serves the paper's purposes -- it shows that even moderate co-evolutionary effects (language influencing default cognitive strategies) represent a feedback loop absent in the transformer case. But the language should be hedged from "reshaping internal representation" to "biasing default processing strategies." The disanalogy with transformers still holds, just at reduced strength.

---

## 6. Fodor's Language of Thought (LOT)

### Key papers

- **Fodor, J.A. (1975).** *The Language of Thought.* Cambridge, MA: Harvard University Press.

- **Fodor, J.A. (2008).** *LOT 2: The Language of Thought Revisited.* Oxford University Press. -- Revised version maintaining the core commitments.

- **Quilty-Dunn, J., Porot, N., & Mandelbaum, E. (2023).** "The best game in town: The reemergence of the language-of-thought hypothesis across the cognitive sciences." *Behavioral and Brain Sciences*, 46, e261. -- Major target article arguing for a revival of LOT, drawing on converging evidence from multiple subfields.

- **Churchland, P.M. (1981).** "Eliminative materialism and the propositional attitudes." *Journal of Philosophy*, 78(2), 67-90. -- Classic eliminativist challenge to LOT.

- **Smolensky, P. (1988).** "On the proper treatment of connectionism." *Behavioral and Brain Sciences*, 11(1), 1-23. -- The connectionist challenge: distributed representations rather than discrete symbols.

- **Marcus, G.F. (2001).** *The Algebraic Mind: Integrating Connectionism and Cognitive Science.* Cambridge, MA: MIT Press. -- Argued for reconciliation, suggesting that connectionist systems need symbolic-like structure.

### Core findings and current status

1. **Fodor's full package is not consensus.** The strong LOT hypothesis (cognition operates over discrete, language-like symbolic representations with compositional semantics implemented in a "Mentalese") remains contested. The eliminativists and connectionists each scored points, and the debate never reached resolution.

2. **The structural claim is widely shared.** The narrower claim -- that internal representation is richer than, and underdetermined by, linguistic output -- commands very broad agreement across otherwise opposed positions. Even connectionists (Smolensky) agree that internal representation has structure not captured by output; they just deny it is language-like.

3. **LOT is experiencing a revival.** The Quilty-Dunn et al. (2023) BBS target article argues that evidence from developmental psychology, animal cognition, neuroscience, and AI has converged to support structured, compositional mental representations. The revival is not exactly Fodor's original -- it emphasises probabilistic, graded, and context-sensitive structure rather than classical logical forms -- but it rehabilitates the core insight.

4. **The transformer era has complicated the picture.** LLMs show that distributed, non-symbolic architectures can exhibit compositional behaviour, which might seem to vindicate the connectionists. But mechanistic interpretability work (e.g., Olah et al., Elhage et al.) has found discrete, interpretable features within distributed representations, which arguably supports a synthesis: distributed implementation of quasi-symbolic structure.

### Current status: **The full LOT hypothesis is contested. The structural claim (output underdetermines internal representation) is established. LOT is experiencing a qualified revival.**

### Relation to the paper's claims

The v1 draft uses Fodor exactly right -- extracting the structural claim that output underdetermines internal representation while bracketing Fodor's stronger commitments. This is precisely the move the current cognitive science literature supports.

**Calibration for v2:** The structural claim can be stated confidently as widely shared. Optionally cite Quilty-Dunn et al. (2023) as evidence that the structured-representation view is experiencing a revival. Do not commit to the full LOT package. The v1 framing is already well-calibrated here.

---

## 7. The Grounding Problem as Rate-Distortion Question

### Key papers

- **Harnad, S. (1990).** "The symbol grounding problem." *Physica D*, 42, 335-346. -- The original statement of the grounding problem: how do symbols get their meaning? Purely formal symbol manipulation is ungrounded.

- **Bender, E.M. & Koller, A. (2020).** "Climbing towards NLU: On meaning, form, and understanding in the age of data." *Proceedings of ACL 2020*, 5185-5198. -- The "octopus test" paper arguing that LLMs trained only on form cannot achieve meaning.

- **Merrill, W., Goldberg, Y., Schwartz, R., & Smith, N.A. (2021).** "Provable limitations of acquiring meaning from ungrounded form: What will future language models understand?" *Transactions of the Association for Computational Linguistics*, 9, 1047-1060. -- Formal argument that text-only models cannot learn certain aspects of meaning that require grounding.

- **Piantadosi, S.T. & Hill, F. (2022).** "Meaning without reference in large language models." *arXiv preprint*. -- Counter-argument: meaning can be constituted by inferential role (use) rather than reference, and LLMs may achieve this.

- **Bisk, Y., Holtzman, A., Thomason, J., Andreas, J., Bengio, Y., Chai, J., ..., & Turian, J. (2020).** "Experience grounds language." *Proceedings of EMNLP 2020*. -- Argues that full language understanding requires grounding in perception and action, proposing a hierarchy of grounding levels.

- **Tishby, N. & Zaslavsky, N. (2015).** "Deep learning and the information bottleneck principle." *IEEE Information Theory Workshop (ITW)*, 1-5. -- The IB principle applied to deep learning, which is adjacent to the rate-distortion framing.

### On the rate-distortion framing specifically

I found **no published work that explicitly frames the grounding debate in rate-distortion terms** -- i.e., asking whether text-only compression can achieve the same rate-distortion optimality as grounded compression when the distortion metric includes meaning-relevant properties. This appears to be a novel contribution of the paper.

The closest existing work:

- **Zaslavsky, N., Kemp, C., Regier, T., & Tishby, N. (2018).** "Efficient compression in color naming across languages." *PNAS*, 115(31), 7937-7942. -- Uses rate-distortion theory to explain cross-linguistic patterns in colour naming. Demonstrates that languages achieve near-optimal compression of colour space. This is rate-distortion applied to the language-cognition interface, but for a specific domain, not the grounding problem in general.

- **Zaslavsky, N., Kemp, C., Tishby, N., & Regier, T. (2019).** "Communicative need in colour naming." *Cognitive Neuropsychology*, 37(5-6), 312-324. -- Further development of the rate-distortion approach to linguistic categorisation.

- **Steels, L. (2008).** "The symbol grounding problem has been solved. So what's next?" In *Symbols and Embodiment*. -- Argues the problem is dissolved by embodied AI approaches. Not information-theoretic.

### Core situation

1. **The grounding debate is active and unresolved.** The Bender & Koller (2020) position (text-only models cannot achieve genuine understanding) and the Piantadosi & Hill (2022) counter (meaning can be constituted by inferential role) represent live opposing positions.

2. **The rate-distortion framing appears novel.** Recasting the grounding question as: "does solving rate-distortion problems against meaning-relevant distortion metrics *require* sensorimotor grounding, or is the statistical structure of text sufficient?" would be a genuine contribution.

3. **The Zaslavsky et al. work on colour naming** provides a concrete precedent for applying rate-distortion theory to the language-cognition interface, though in a specific rather than general domain.

4. **Multimodal models complicate the debate.** Models with vision+language training (e.g., CLIP, GPT-4V, Gemini) partially close the grounding gap without full embodiment, suggesting that the grounding question may be a matter of degree rather than kind.

### Current status: **The grounding debate is active and contested. The rate-distortion framing is novel and potentially valuable.**

### Relation to the paper's claims

The paper flags this as an open question, which is exactly the right calibration. The rate-distortion framing could strengthen the open question by making it precise: what is the rate-distortion cost of lacking grounding? Is there a provable gap in achievable rate-distortion performance between grounded and ungrounded systems for meaning-relevant distortion metrics?

**Calibration for v2:** Flag as open question. The rate-distortion framing is novel and can be stated as such. Cite Zaslavsky et al. as precedent for rate-distortion analysis of linguistic categorisation. Do not claim the question is resolved in either direction. The multimodal model evidence suggests the answer may be "grounding helps but text-only gets further than expected," which is the honest position.

---

## Summary: Calibration for Section 5 (v2)

### Claims that can be stated confidently

1. **The projection bottleneck is real and quantifiable in both systems.** Speech at ~39 bits/second, internal bandwidth orders of magnitude higher. Cross-linguistically invariant (Coupe et al., 2019). Transformer internal dimensionality vs. per-token output presents an analogous mismatch.

2. **Task-optimised artificial systems converge on representational geometries similar to biological systems.** RSA evidence from vision (Yamins, Kriegeskorte, Schrimpf) and language (Goldstein et al.) is substantial.

3. **The convergence is structural, not mechanistic.** Both systems face the same information-theoretic constraints and arrive at the same type of solution (hierarchical compression through a serial bottleneck).

4. **Output underdetermines internal representation.** Widely shared across opposing positions in cognitive science (Fodor's structural claim, now reviving via Quilty-Dunn et al.).

5. **The co-evolution disanalogy is real.** Language and brain co-evolved (mainstream view); transformers adapt to language unidirectionally. This is an honest and important qualification.

### Claims that need hedging

1. **Levinson's cross-linguistic spatial cognition.** The strong claim (language reshapes internal representation) has been weakened. Use the moderate version: language biases default processing strategies. Still serves the argument but with reduced force.

2. **Depth of convergence.** RSA explains 30-60% of variance, meaning substantial divergence remains. State the convergence but note the gap.

3. **Whether the convergence implies shared depth of semantic compression.** The grounding problem remains open. The rate-distortion framing is novel and precise but does not resolve the question.

### Claims that are novel (and should be flagged as such)

1. **The grounding problem as a rate-distortion question.** No existing literature frames it this way. This is a genuine contribution of the paper and should be presented as a novel framing, not as established theory.

### Recommended structure for compressed Section 5

Given the v2 target of ~60% of current length, the following structure preserves what's strong and cuts what's weak:

**5.1 The projection bottleneck as substrate-independent constraint** (~40% of section)
- Channel capacity: Reed & Durlach, Coupe et al. -- quantitative, cross-linguistic, strong evidence
- Vygotsky's inner/external speech as illustration (brief, qualitative, well-established)
- Fodor's structural claim as widely shared (one sentence, cite Quilty-Dunn et al.)
- RSA evidence for actual convergence (Yamins, Kriegeskorte, Schrimpf, Goldstein)

**5.2 Convergence and its limits** (~60% of section)
- Co-evolution disanalogy (Deacon) -- honest, strengthening
- Levinson recalibrated (biases strategies, not reshapes representation)
- Grounding as rate-distortion question (novel framing, flagged as open)
- What convergence explains and what it doesn't (brief, decisive)

### Key references to add for v2

- Coupe et al. (2019) -- cross-linguistic speech rate invariance (strengthens bottleneck claim)
- Goldstein et al. (2022) -- RSA for language models (extends convergence beyond vision)
- Quilty-Dunn et al. (2023) -- LOT revival (supports the structural claim about output underdetermining representation)
- Li & Gleitman (2002) -- Levinson challenge (forces honest recalibration)
- Zaslavsky et al. (2018) -- rate-distortion for linguistic categorisation (precedent for the novel framing)
