---
title: "Models, evidence and interpretation"
description: "How selection, representation, operationalization and validation turn cultural sources into evidence for a humanities argument."
tags: [foundations, modelling, evidence, interpretation, uncertainty]
status: draft
---

# Models, evidence and interpretation

## Learning outcomes

After this chapter, you should be able to:

- trace an argument from a cultural source through selection, data construction and modelling to evidence and interpretation;
- distinguish broad humanistic modelling from statistical and machine-learning models;
- explain *capta* as a critical intervention without treating the ordinary word *data* as inherently mistaken;
- operationalize a concept by specifying units, indicators, inclusion rules and a validation strategy;
- distinguish a computational output from evidence and evidence from an interpretation;
- use close reading, distant reading, error reading, outlier reading and contextual return as movements between analytical scales;
- compare alternative models by stating what each gains, loses, supports and cannot establish;
- locate uncertainty in sources, measurements, models, visualizations and interpretations.

## Before you begin: where does evidence enter?

Imagine a newspaper article in which a minister calls an economic forecast “encouraging,” an opposition speaker describes public “fear,” and an editorial cartoon makes the whole exchange look absurd. What would count as evidence about emotion: the two words, the emotions speakers attribute to political actors, the cartoon, readers' responses, or a later researcher's classification? Each answer produces a different research object.

**Prerequisites:** read [What is digital humanities?](what-is-digital-humanities.md) and the preceding [historical chapter](history-of-digital-humanities.md). No programming or statistics is required. **Practice input and output:** one bounded question and a legally usable source set; two competing models with evidential limits. **Check:** another reader should identify every unit, category, transformation and inferential step. **Failure modes:** treating convenient records as a complete archive or a result as self-interpreting. **Limits:** respect copyright, privacy and community authority; do not infer inner states from public language without a defensible design.

This chapter follows an analytical chain:

> **cultural source → selection and representation → data or capta → model → output → evidence → interpretation**

The arrows do not describe an irreversible chronology. Interpretation guides selection; an outlier sends the researcher back to a source; a failed validation revises the model. The chain is useful because it prevents stages from collapsing into one another.

## Representation and modelling: purposeful partiality

A model is a selective representation made for a purpose. A chronology models succession; an edition models a text and its variants; a catalogue models a collection; a map models spatial relations; a database schema models entities and links; a period term models historical difference. None has to be numerical. McCarty describes modelling as a heuristic practice in which a representation is constructed and manipulated for study, or a design is made for bringing something new into being. On this account, the model matters as an activity: it changes through a repeated exchange between the researcher, the representation and what resists it.[^modeling]

Selectivity cannot simply be removed. A map preserving every material feature of a territory would cease to function as a map. Ask instead: **which differences did the model preserve, which did it suppress, for whose purpose, and with what consequences?** A correspondence network organized around senders and recipients may obscure drafts, secretaries, uncertain authorship and the material dossier.

The word *model* also has narrower technical meanings. Keep at least three uses apart:

1. A **humanistic or conceptual model** makes an object thinkable by selecting entities, relations, boundaries, sequences or viewpoints. An argument and an interface can model a field without fitting an equation.
2. A **statistical model** expresses relationships among variables and normally represents variation or uncertainty under stated assumptions. It may be descriptive, predictive or inferential.
3. A **machine-learning model** is fitted from examples to perform a task such as classification, ranking, prediction or representation learning. Supervised classifiers and embedding models belong here, but they do not exhaust modelling.

The narrower kinds are nested within the broader one. Before training a classifier, researchers have selected documents, defined labels and units, and decided which differences can become features. Underwood emphasizes models connecting linguistic measurements to meaningful categories; McCarty the wider heuristic work of explicit representation.[^model-kinds] They address different levels rather than one agreed definition.

## From cultural sources to data or *capta*

A cultural source is not a transparent container of facts. It has a production history, material form, institutional location and prior uses. A corpus of parliamentary speeches is shaped by speaking rules, transcription practices and archival survival before a researcher downloads it. Turning that source into analyzable records adds further decisions: which sessions to include, whether interruptions count as speech, how speakers are identified, what counts as a sentence and how corrections are represented.

Drucker proposed *capta*—things taken rather than simply given—to make those constitutive acts visible. Her intervention is especially forceful against graphics that make selected, cleaned and aggregated values look like direct observations of an independent reality. It reminds us that parameterization precedes the chart.[^capta] Yet *capta* is not an obligatory replacement for every use of *data*. Lavin accepts the need for situated and constructed knowledge while disputing the claim that the word *data* necessarily commits a researcher to naïve realism. Data can be fragmentary, purposefully assembled and still empirically useful.[^situated-data]

This chapter therefore uses **data** as the ordinary umbrella term and **capta**, **constructed data** or **situated data** when the act of taking needs emphasis. The important test is not vocabulary alone. Ask whether the project documents:

- the relation between source objects and analytical records;
- the sampling frame, omissions and access conditions;
- transcription, OCR, normalization and annotation decisions;
- historical categories alongside categories imposed by the research;
- provenance, rights, versions and responsible labour;
- people or communities made vulnerable by collection and classification.

D'Ignazio and Klein frame data work as a distribution of power: deciding what counts, whose knowledge is authoritative and who receives credit or bears harm.[^power] That argument does not make empirical research impossible. It makes the standpoint, labour and consequences of data construction part of the method. The practical procedures for documenting rows, identifiers, missingness and provenance belong to [Data, metadata and models](data-metadata-models.md); the present chapter asks what those procedures permit a scholar to claim.

## Units, categories and operationalization

Humanities concepts—genre, influence, fear, public memory, marginality—cannot enter an analysis merely by being named. **Operationalization** links a concept to observations by specifying what will be inspected and how. A usable operational definition contains at least:

- a **concept** and the aspect of it relevant to the question;
- a **unit**, such as a token, passage, speech, volume, person, event or place;
- one or more **indicators**, the observable features treated as bearing on the concept;
- **inclusion and exclusion rules**, including mixed, absent and uncertain cases;
- a **procedure** for producing a value or category;
- a **validation strategy** that asks whether the procedure measures the intended concept in this context.

Moretti presents operationalization as a bridge from a concept to measurement. In his example, two measures of dramatic prominence—the number of words spoken and the number of links between characters—produce different protagonists. The difference is intellectually useful because each operation makes another aspect of prominence visible.[^operationalizing] But precision alone does not establish validity. Adcock and Collier distinguish disagreement about a concept from problems in the observations used to measure it and insist that validation is contextual to the claim.[^validity] Operationalization is therefore not only reduction. It is also clarification, comparison and a test of whether an abstract idea survives contact with sources.

Consider “fear in political language.” At least four indicators are plausible: occurrences of words associated with fear; clauses in which a speaker expresses fear; clauses attributing fear to another actor; and passages judged by readers to create a fearful frame. These are not interchangeable measurements of one hidden quantity. They operationalize different relations among language, speaker, target and reader.

Record category provenance. Historical categories may come from sources; analytical categories may be defined in the research design. Supervised models learn to predict researcher-defined labels from annotated examples; they do not invent the scheme. Unsupervised methods may induce groupings, which still require human interpretation, naming and validation. A nineteenth-century catalogue label and a normalized modern genre record different classifications, not synonyms. Preserve source wording where feasible, allow uncertain or mixed cases, and inspect “other” for institutional exclusions.

## Formalization, gain and loss

**Formalization** makes selected relations explicit enough for consistent application: a codebook defines labels, TEI distinguishes textual structures, a graph represents nodes and edges, and an equation connects variables. Computational explicitness can expose assumptions left tacit in prose. For McCarty, the resulting surprises and failures are a scholarly benefit of modelling.[^modeling]

Every formalization has a **gain-and-loss profile**:

| Formal choice | Possible gain | Possible loss or displacement |
| --- | --- | --- |
| One row per speech | comparable units and metadata joins | interruptions, page layout and exchange may recede |
| Fixed emotion labels | consistent annotation and counting | mixed, historically specific or unnamed affects may be forced apart |
| Network edges for correspondence | relational patterns become calculable | the material letter and semantic character of a tie are compressed |
| Two-dimensional chart | change becomes quickly comparable | missingness, aggregation and alternative scales may disappear |

Loss does not prove failure, just as structure does not prove validity. Ask whether the gain answers the question, the loss threatens the claim, and another representation can recover what matters. A source link may reverse one loss; an archive that never collected oral testimony cannot.

Formalization also includes presentation. Burdick and collaborators argue that interface, database, navigation, access and preservation choices help stage a digital scholarly argument.[^interface] A ranked search result, default map extent or hidden “unknown” category is therefore not packaging after the analysis. It is another model that distributes attention and constrains what a reader can inspect.

## Moving across scales: close, distant, error and outlier reading

Moretti's *distant reading* names an influential attempt to study literary systems and large populations of texts beyond the limits of a canon. Its polemical force challenged the assumption that a few intensively read works could stand for literary history.[^distance] The term has also encouraged an unhelpful binary in which close reading signifies interpretation and distant reading signifies numbers. Underwood instead connects macroscopic literary study to book history and the social sciences and argues that scale alone is less important than models linking linguistic and social evidence.[^underwood]

Close and distant reading are best treated here as movements, not rival allegiances:

1. **Distant orientation** compares distributions across a collection and locates a pattern that no single passage can establish.
2. **Close reading** examines form, rhetoric and ambiguity in selected passages and helps construct or challenge categories.
3. **Error reading** inspects false positives, false negatives, OCR failures and annotator disagreements to learn where the operational definition or data breaks down.
4. **Outlier reading** examines unusual but not necessarily erroneous cases that may reveal another genre, period, source practice or explanation.
5. **Contextual return** reconnects the pattern to production, circulation, institutions, language history and prior scholarship before a claim is made.

*Error reading* and *outlier reading* are used here as pedagogical names for practices, not as settled schools with universally agreed definitions. An error is a mismatch relative to a specified task or reference standard; an outlier is unusual relative to a distribution and may be the most revealing source in the collection. Neither should be silently deleted. Close reading can occur at any point, including when a codebook is drafted or a visualization is criticized. Distant work may involve fifty carefully chosen texts rather than millions. Scale is relational: it depends on the question, unit, available population and existing knowledge.

Ramsay treats algorithmic transformation as an occasion for critical reading rather than a procedure that adjudicates a final meaning.[^ramsay] The practical loop is therefore **source → model → output → selected source passages → revised model**. Movement across scales is a validation practice and a method of discovery.

## Output is not automatically evidence

Three terms need explicit boundaries:

- An **output** is an immediate product of a procedure: a count, label, probability, topic, cluster, embedding, map or chart.
- **Evidence** is source material or an output made relevant to a bounded claim through provenance, validation, comparison and an account of limitations.
- An **interpretation** is a reasoned account that connects evidence to a humanities question, context and alternative explanations.

Roles can change. After the corpus, labels, test and errors are documented, classifier predictions may become evidence about language under that operational definition—but not about authors' private feelings or readers' responses. A surprising false positive may support a separate close-reading argument.

The transition from output to evidence requires at least four checks:

1. **Provenance:** can the result be traced to sources, transformations, versions and responsible agents?
2. **Validity:** does the operation bear on the intended concept, and against which independent sources, expert judgements or held-out cases was that tested?
3. **Comparison:** would a baseline, another sample, another operationalization or a plausible alternative explanation produce the same pattern?
4. **Claim fit:** is the conclusion no broader than the population, period, language and kind of relation actually studied?

Evidence constrains but does not mechanically select an interpretation. Two accounts may explain the same frequency change through genre composition, political events or semantic change. They are not equally strong if one ignores known missingness or contradicts source passages. Plurality is not arbitrariness.

Underwood's statistical approach aims to connect linguistic variables to categories that already have social or literary significance; Ramsay emphasizes the opening of interpretive possibilities; Drucker emphasizes the constitutive character of representation. Their emphases do not produce a consensus about what computation should do.[^epistemic-disagreement] Together they make a useful demand: show how an output became evidence and why the proposed interpretation is preferable to alternatives.

## Uncertainty, ambiguity and visual form

Uncertainty enters at several non-equivalent levels:

| Location | Question to ask | Appropriate response |
| --- | --- | --- |
| Source and corpus | What is missing, damaged, inaccessible or overrepresented? | document the sampling frame, gaps and survival conditions |
| Representation and measurement | Which unit or category is ambiguous, and how often do coders disagree? | preserve alternatives, disagreement or confidence; revise the codebook |
| Model and output | How sensitive is the result to data, parameters, random variation or domain shift? | use held-out tests, baselines, calibration and sensitivity analysis |
| Visualization | Which defaults, bins, scales or encodings imply more certainty than exists? | expose denominators, missingness, intervals and consequential design choices |
| Interpretation | Which contextual explanation remains undecidable from these observations? | bound the claim and state rival readings or required evidence |

A conventional confidence interval expresses uncertainty in an estimated quantity due to sampling variability under specified model assumptions. It does not generally capture uncertainty about model structure, category design, domain shift, missing archives or interpretation. Nor can it decide whether irony counts as fear. Published code reveals a procedure, not the adequacy of its concept.

Drucker asks humanists to design for situated knowledge; *Digital_Humanities* places visual and interface design within scholarly argument.[^visual-uncertainty] This does not make every bar chart naïve or decorative blur meaningful. Visual form should match the uncertainty: an interval, gap, multiple classifications, linked passage or explicit admission that the evidence cannot decide.

## Worked example: three models of emotion in parliamentary debate

Suppose a project asks: **How did speakers mobilize fear and hope in Slovene parliamentary debate about climate policy between 2000 and 2025?** The corpus is licensed, sessions and speakers are documented, OCR is not involved, and the claim concerns public language—not private psychological states. Three teams can answer different versions of the question.

| Model | Unit and categories | Output and validation | What it can support / cannot establish | Gain / loss |
| --- | --- | --- | --- | --- |
| **Lexicon counts** | Unit: lemmatized token within a speech. Categories: words associated with fear or hope; negated matches flagged separately. | Output: matches per 1,000 tokens by period and speaker role. Validate on stratified concordance samples, inspect negation, quotation, morphology and period-specific senses, and compare a no-lemmatization baseline. | Supports a claim about the distribution of lexicon-associated vocabulary under documented rules. Cannot establish who experiences an emotion, whether a passage is ironic, or whether an audience felt fear. | Gains coverage, speed and inspectable rules; loses syntax, attribution, implicit expression and much historical semantics. |
| **Manual expressed/attributed annotation** | Unit: clause or short passage plus speaker, possible experiencer and target. Categories: speaker expresses fear/hope; speaker attributes it to another actor; quoted expression; mixed/uncertain; absent. | Output: annotated passages, category proportions and coder disagreement. Validate through pilot coding, independent double annotation, adjudication logs, counterexamples and reading full speech turns. | Supports an account of how debate allocates emotion rhetorically among actors. Cannot reveal private states or cheaply characterize every speech; agreement does not by itself prove conceptual validity. | Gains role, target, implicit phrasing and contextual nuance; loses scale and introduces documented interpretive labour. |
| **Supervised classifier with embeddings** | Unit: sentence or short speech turn. Labels come from the manual scheme; an embedding represents linguistic context in a learned vector space where proximity may reflect task- and model-dependent similarity; the classifier predicts labels or probabilities. | Output: held-out predictions and aggregates. Split by session and period; report class-specific precision/recall, calibration and confusion; test subperiods; inspect errors and nearest neighbours; compare lexicon and majority baselines. | Supports an estimated scheme distribution if performance and temporal and domain stability are adequate. Cannot turn labels into natural kinds, recover excluded archives or establish audience effects. | Gains scalable contextual sensitivity; loses direct rule transparency, compresses context into learned dimensions and risks temporal or domain shift. |

Word–emotion lexicons associate terms with categories; their creators explicitly distinguish association from an emotion evoked in a reader.[^lexicon] Contemporary emotion analysis also includes classification, regression and role labelling, confirming that “emotion analysis” is not one operation.[^emotion-analysis] The three models may therefore disagree without one being defective. A rise in the word *fear* inside quotations may increase the lexicon series, be coded mainly as attributed emotion, and challenge a classifier trained on direct expressions. That divergence is evidence about the operationalizations.

A responsible interpretation might conclude: *within the licensed corpus of sessions, explicit mentions of fear and attributions of fear to others became more frequent after a specified date, while independently coded cases where speakers themselves expressed fear did not rise as quickly*. Historical explanation would then require close reading and contextual sources about policy events, parliamentary rhetoric and corpus composition. None of the tables alone explains the change.

## Practice: design two competing models

Choose a question about a cultural collection—authority in letters, mobility in newspapers, belonging in oral histories, genre in book catalogues or emotion in fiction—and design **two genuinely competing models**.

For each model, provide:

1. the bounded research question and source population;
2. the selection rule and one consequential omission;
3. the unit, categories or variables and indicators;
4. inclusion, exclusion, mixed and missing-value rules;
5. the expected output and a validation strategy;
6. one claim the output could support and one it could not;
7. a gain-and-loss statement;
8. a plan for error reading, outlier reading and contextual return;
9. rights, privacy, representational-harm and labour constraints.

**Output:** a comparison table and 500-word rationale. **Check:** exchange models with another reader, who should be able to predict at least one source passage the models would classify differently. **Failure mode:** if both models use the same unit, categories and indicator but different software, they are probably one operationalization with two implementations, not competing models.

## Reflection

- At which arrow in the source-to-interpretation chain does your strongest interpretive commitment enter?
- Which loss in your formalization is recoverable by linking back to sources, and which loss is built into the archive?
- Would a disagreement between two annotators count as noise, evidence of a poor codebook or evidence of a contested concept?
- What additional evidence could decide between two interpretations of the same output—and what disagreement would remain interpretive?
- Does your visualization show a measured uncertainty, merely symbolize doubt, or conceal the issue altogether?

## Summary

Digital-humanities evidence is made through a revisable chain from cultural sources to claims. Selection and representation construct data; *capta* emphasizes that constitutive work, while situated use of the ordinary term *data* remains legitimate. Humanistic modelling includes conceptual, material and interface representations as well as statistical and machine-learning models. Operationalization connects a concept to units, indicators, rules and validation. Formalization produces analytical gains and losses that must be named rather than celebrated or condemned in advance.

An output becomes evidence only after checks of provenance, validity, comparison and claim fit. Evidence constrains but does not automate interpretation. Close, distant, error and outlier reading plus contextual return move iteratively through sources and models. Missing archives, ambiguous categories, measurement error, model instability, visual rhetoric and rival interpretations are distinct uncertainties requiring distinct responses. The aim is an inspectable argument showing what was taken, transformed, tested, learned and left unresolved.

## Further reading and references

- Adcock, Robert, and David Collier. “[Measurement Validity: A Shared Standard for Qualitative and Quantitative Research](https://doi.org/10.1017/S0003055401003100).” *American Political Science Review* 95, no. 3 (2001): 529–546. DOI: `10.1017/S0003055401003100`.
- Burdick, Anne, Johanna Drucker, Peter Lunenfeld, Todd Presner, and Jeffrey Schnapp. [*Digital_Humanities*](https://doi.org/10.7551/mitpress/9248.001.0001). MIT Press, 2012. DOI: `10.7551/mitpress/9248.001.0001`.
- D'Ignazio, Catherine, and Lauren F. Klein. [*Data Feminism*](https://doi.org/10.7551/mitpress/11805.001.0001). MIT Press, 2020. DOI: `10.7551/mitpress/11805.001.0001`.
- Drucker, Johanna. “[Humanities Approaches to Graphical Display](https://dhq.digitalhumanities.org/vol/5/1/000091/000091.html).” *Digital Humanities Quarterly* 5, no. 1 (2011). *Digital Humanities Quarterly* website, published by the Alliance of Digital Humanities Organizations and the Association for Computers and the Humanities. Accessed July 22, 2026. DOI: `10.63744/r4ysrh7ae534`.
- Lavin, Matthew. “[Why Digital Humanists Should Emphasize Situated Data over Capta](https://doi.org/10.63744/r8bk8knh3wbk).” *Digital Humanities Quarterly* 15, no. 2 (2021). DOI: `10.63744/r8bk8knh3wbk`.
- McCarty, Willard. “[Modeling: A Study in Words and Meanings](https://doi.org/10.1002/9780470999875.ch19).” In *A Companion to Digital Humanities*, edited by Susan Schreibman, Ray Siemens and John Unsworth, 254–270. Blackwell, 2004. DOI: `10.1002/9780470999875.ch19`.
- Mohammad, Saif M., and Peter D. Turney. “[Crowdsourcing a Word–Emotion Association Lexicon](https://doi.org/10.1111/j.1467-8640.2012.00460.x).” *Computational Intelligence* 29, no. 3 (2013): 436–465. DOI: `10.1111/j.1467-8640.2012.00460.x`.
- Moretti, Franco. [*Distant Reading*](https://www.versobooks.com/products/2309-distant-reading). Verso, 2013. *Verso Books* website. Accessed July 22, 2026.
- Moretti, Franco. “[Operationalizing: Or, the Function of Measurement in Literary Theory](https://doi.org/10.64590/daw).” *New Left Review* 84 (November–December 2013): 103–119. DOI: `10.64590/daw`.
- Ramsay, Stephen. [*Reading Machines: Toward an Algorithmic Criticism*](https://www.press.uillinois.edu/books/?id=p078200). University of Illinois Press, 2011. *University of Illinois Press* website. Accessed July 22, 2026.
- Štajner, Sanja, and Roman Klinger. “[Emotion Analysis from Texts](https://doi.org/10.18653/v1/2023.eacl-tutorials.2).” In *Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics: Tutorial Abstracts*, 7–12. Association for Computational Linguistics, 2023. DOI: `10.18653/v1/2023.eacl-tutorials.2`.
- Underwood, Ted. [*Distant Horizons: Digital Evidence and Literary Change*](https://doi.org/10.7208/chicago/9780226612973.001.0001). University of Chicago Press, 2019. DOI: `10.7208/chicago/9780226612973.001.0001`.

[^modeling]: McCarty, “Modeling,” especially his provisional definition of modelling, the distinction between a model *of* and a model *for*, and the role of iterative failure. His account is a proposal for the shared intellectual ground of humanities computing, not a universally accepted definition of every humanities method.
[^model-kinds]: McCarty, “Modeling,” on broad heuristic representation; Underwood, *Distant Horizons*, especially chapter 1, on statistical models connecting linguistic measurements to socially meaningful categories. The distinction among conceptual, statistical and machine-learning models in this chapter is analytical; disciplinary usage overlaps.
[^capta]: Drucker, “Humanities Approaches,” especially the argument that data visualizations can hide the interpretive framework through which phenomena were selected and parameterized.
[^situated-data]: Lavin, “Why Digital Humanists,” accepts the situated and constructed character of knowledge but disputes replacing *data* with *capta* as a general terminological rule. The present chapter adopts that qualified position.
[^power]: D'Ignazio and Klein, *Data Feminism*, especially chapters 1, 4, 5 and 6 on power, classification, labour and the claim that numbers do not interpret themselves.
[^operationalizing]: Moretti, “Operationalizing,” 103–119. His word-space and character-network measures show that different operations can produce different, simultaneously relevant aspects of literary prominence.
[^validity]: Adcock and Collier, “Measurement Validity,” 529–546, on the relation among background concepts, systematized concepts, indicators and scores, and on context-sensitive validation across qualitative and quantitative research.
[^interface]: Burdick et al., *Digital_Humanities*, especially the discussion of digital scholarly arguments as staged through interface, interactivity, database design, markup, navigation, access, dissemination and archiving. The book is programmatic and design-centred rather than a consensus standard.
[^distance]: Moretti, *Distant Reading*. The volume collects essays written over two decades and advances a deliberately polemical alternative to canon-bound literary history; it should not be read as the sole definition of large-scale literary study.
[^underwood]: Underwood, *Distant Horizons*, preface and chapters 1 and 5, on macroscopic literary history, statistical models and the risks of distant reading. See also his critical differentiation of distant reading from a simple increase in corpus size.
[^ramsay]: Ramsay, *Reading Machines*, especially his account of algorithmic transformation as a constraint that generates objects for criticism rather than a mechanism for settling interpretation.
[^epistemic-disagreement]: Underwood, *Distant Horizons*; Ramsay, *Reading Machines*; Drucker, “Humanities Approaches.” Underwood gives a larger role to empirically validated statistical models, Ramsay to generative deformation and subjective criticism, and Drucker to constitutive interpretation and its visual forms. These are compatible in some projects but not identical positions.
[^visual-uncertainty]: Drucker, “Humanities Approaches”; Burdick et al., *Digital_Humanities*. Drucker's proposed visual forms are an intervention against realist certainty, not evidence that any particular graphical device can encode every kind of ambiguity.
[^lexicon]: Mohammad and Turney, “Crowdsourcing,” 436–465. Their experiments distinguish asking whether a term is associated with an emotion from asking whether it evokes an emotion; a word–emotion association lexicon does not identify a speaker's psychological state.
[^emotion-analysis]: Štajner and Klinger, “Emotion Analysis from Texts,” 7–12, surveys classification, regression, emotion-role labelling, resources, social impact and methodological challenges.
