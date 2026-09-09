---
title: "AI, ethics and reproducibility"
description: "How to turn AI-assisted analysis into an inspectable argument through source criticism, validation, rights decisions and preserved research records."
tags: [AI, ethics, reproducibility, provenance, rights]
status: draft
---

# AI, ethics and reproducibility

When a newspaper claims to speak for a whole nation, what would establish that
claim as more than political rhetoric? A fluent summary can quietly turn the
newspaper's assertion into the researcher's finding. The problem begins before
an invented quotation appears: it begins when the relationship between evidence
and argument disappears. Responsible use of artificial intelligence (AI) makes
that relationship inspectable, including decisions to correct, qualify or
withhold an output.

!!! note "Editorial status"
    This chapter and its teaching simulations are machine-assisted drafts,
    pending scholarly and competent human Slovene-language review. The examples
    below are authored teaching simulations, not reported generative-model runs
    or evidence of completed human validation.

## Learning outcomes

After this chapter, you should be able to:

- match computational outputs to the claims they can support;
- distinguish technical repeatability, computational reproducibility,
  robustness, evidential auditability and interpretive accountability;
- preserve a source-to-claim trail when an exact model rerun is unavailable;
- design stratified validation, baseline comparison and an abstention rule;
- turn privacy, rights, inclusion and resource concerns into workflow decisions;
- document assistance, corrections, human disagreement and remaining uncertainty.

## Before you begin

Read one archival paragraph and identify its speaker, audience and strongest
claim. Distinguish what it asserts from what you could independently establish.
Would a translation preserve the distinction? You need basic source criticism,
document identifiers and the distinction developed in
[Models, evidence and interpretation](models-evidence-interpretation.md).
You do not need an AI account. The practice can use the preserved packet and
authored outputs alone; running an external service is optional and requires an
appropriate institutional data arrangement.

## Start with the output, then assess the claim

AI names a heterogeneous group of systems, not one method. A **predictive or
classification model** assigns labels or scores under a learned relationship:
for example, a paragraph may receive a political-stance label. That supports a
claim about performance against a specified codebook on evaluated material,
not direct access to an author's beliefs. **Generative language models** produce
text conditioned on instructions and context. A useful draft remains a
candidate representation; grammatical fluency and plausible citations cannot
establish historical truth.

**Embeddings** represent items as vectors. **Retrieval** uses a query and a
ranking procedure to select candidate passages. Semantic proximity may help
find differently worded material, but neither proximity nor rank establishes
agreement, attribution or complete coverage. A retrieval-augmented generator
therefore has two questions to answer: did retrieval supply the relevant
evidence, and did generation use it faithfully? Failure at the first stage
cannot be repaired by a confident answer at the second. Acquiring sources for
a research collection is a broader decision about material and access, not
merely this computational retrieval step.

**OCR, handwriting recognition (HTR) and probabilistic enrichment** propose
readings, entities or linguistic structures. Their outputs remain distinct
from the document they describe. Conversely, a **rule-based system** may apply
a dictionary or regular expression without learning anything; a vendor's AI
label does not change that mechanism. A transparent rule can be an excellent
baseline, although it can miss irony, historical spelling and context. See
[Linguistic annotation with CLASSLA](linguistic-annotation-classla.md) and
[Topics, sentiment and emotion](topics-emotions-classification.md) for
layer-specific evaluation.

Deployment is another distinction. A **local** installation can give researchers
control over executable versions if dependencies and model weights are
preserved. A **hosted** interface delegates part of that control to a provider.
An **API** is a programmatic interface, not a privacy or stability guarantee;
it can expose a local or remote service. Document the actual arrangement.
A service name alone does not identify its model, hidden instructions, routing,
retention policy or ability to export research records.

## Five different promises

This handbook uses **technical repeatability** for repeating the same procedure
under specified conditions, with byte-identical output only when explicitly
required. **Computational reproducibility** means that another researcher can
reconstruct a computation from preserved data, code and environment and obtain
the stated equivalent result. The National Academies' 2019 report distinguishes
reproducibility using the same research inputs from replication with new data;
terminology varies across disciplines, so define the intended test rather than
assuming a shared label.[^ai-nas]

**Robustness** asks whether a conclusion survives defensible changes in prompts,
models, settings or samples. **Evidential auditability**, supported by
**traceability**, asks whether a reader can follow each consequential output
back to supplied sources and transformations. **Interpretive accountability**
asks whether a researcher explains why evidence warrants a reading, records
counterevidence and permits reasoned disagreement. Interpretive reproducibility
need not mean identical interpretations; another scholar must be able to
reconstruct and assess the route to a conclusion.

| Proposed assurance | What must be preserved or tested | What it does not establish |
| --- | --- | --- |
| Exact repetition | Identical inputs and configuration; declared byte comparison | That the repeated answer is correct |
| Computational reproducibility | Data, executable code, dependencies, model files or an available snapshot, expected result and tolerance | Validity outside those inputs |
| Robustness | Bounded changes, all attempted runs, differences and an acceptance rule | Independence of models or universal reliability |
| Traceability and auditability | Output, passage IDs, source versions, transformations and corrections | That every interpretation is persuasive |
| Interpretive accountability | Argument, alternatives, reviewer disagreement and final responsibility | Forced agreement or mechanical interpretation |

A preserved hosted response can be auditable after its model disappears. It
cannot then be advertised as computationally reproducible merely because its
prompt survives. Conversely, repeatable extraction can preserve an OCR mistake.
State which assurance has been demonstrated and which remains unavailable.
A seed records an input; it does not establish control over every source of
nondeterminism, proprietary component or hardware-sensitive operation.

## Preserve the research event

Record provider, model identifier, version or dated snapshot if available,
actual UTC date/time, and interface or API. Preserve permitted system and user
instructions, examples, conversation history, generation parameters and
retrieval configuration. Retrieval records need the query, index version,
embedding model, chunking, filters, ranking and selected passages in supplied
order. Keep source documents with stable passage IDs, hashes and access
conditions; record preprocessing, normalization, translation and truncation.
If an interface silently shortens context, mark the supplied extent unknown.

Save original output separately from a correction log and corrected candidate.
Add the validation protocol and actual sample, reviewer decisions, code and
package environment, relevant hardware, elapsed time and monetary cost. Mark
a proprietary detail `unknown`, a withheld item `redacted` with a reason and
access route, and an unperformed action `not_run`. These differ from numeric
zero. Never include credentials in the public record. Archive a permitted
configuration export, not screenshots alone: screenshots can omit settings
and obstruct accessible reuse.

The [documentation and audit workflow](../workflows/ai/document-and-audit-a-source-grounded-ai-analysis.md)
provides a record to fill. Service capabilities, terms and prices should be
checked and dated for the service actually selected. This chapter makes no
current provider-specific guarantee; its source audit date is 7 September 2026.
Link the research package to a versioned scholarly output using
[The living open handbook](open-living-handbook.md), while keeping restricted
evidence under an authorized access procedure.

## Worked example: from national consensus to an attributed claim

Our question is: how does *Ilustrirani Slovenec* construct political unity?
Use the [archival-friction packet](../../assets/downloads/archival-friction-v1.zip)
and [text/NLP packet](../../assets/downloads/text-nlp-validation-v1.zip).
The historical object is *Ilustrirani Slovenec*, 7 February 1925, volume 1,
number 7, dLib identifier `URN:NBN:SI:doc-YPI8OFSU`.[^ai-archive]
The locator is PDF page 1, introductory paragraph beneath the title,
`AF-OCR-P1-INTRO`, sentence beginning `Tudi danes`. In the NLP packet,
`raw/annotation-samples.csv` preserves this selection as `TNLP-AF-REF` and
`TNLP-AF-OCR`, with hashes and extraction provenance. The reference transcription,
provider OCR and machine-assisted linguistic annotations are different layers.

Begin with a clean control: `source/contemporary-sample.csv`, record `TNLP-C02`,
sentence 1. Its handbook-authored synthetic researchers check transcriptions
and explain uncertainty. An acceptable description reports those two actions
without inventing a project or outcome. It demonstrates the desired task on
explicit wording, not performance on historical archives. The control and
historical passage must never be pooled as independent historical observations.

Now audit this **authored simulation of a faulty English AI summary**:
“The article documents unanimous Slovenian support for the Slovene People's
Party. A national survey confirms that differences of worldview no longer
matter.” This machine-assisted teaching simulation does not come from a
documented model experiment. Its polished form lets
students examine an attribution error, an invented evidential basis and an
erased uncertainty without submitting sources to a service. An accompanying
**simulated quotation record** copies `stavovske` and `narodain` from the OCR
and labels them “scan-verified quotation”. That label is deliberately false;
A03 audits this additional authored record, not words in the English summary.

| Record | Simulated failure | Source check | Correction and consequence |
| --- | --- | --- | --- |
| A01 | National consensus presented as established fact | `TNLP-AF-REF`; the paragraph asserts unity but supplies no independent population evidence | Attribute the claim to the newspaper; withdraw the conclusion about measured public support |
| A02 | A national survey is invented | `AF-OCR-P1-INTRO`, complete paragraph; no survey is named | Delete the survey claim; record `unsupported_claim`, not a missing citation to be guessed |
| A03 | OCR wording is treated as a reliable quotation | Compare `TNLP-AF-OCR` with `TNLP-AF-REF` and PDF page 1; OCR includes `stavovske` and `narodain` | Cite a checked transcription; preserve the OCR error and correction separately |
| A04 | English wording removes the attributed political voice | Re-read the Slovene passage and its party reference; compare translation with the original | Label the English rendering a paraphrase and retain a Slovene locator |

The corrected teaching interpretation is narrower: the introductory paragraph
presents support for the party as service to collective national freedom and
subordinates differences of outlook to that claim. It is evidence of the
publication's rhetoric, not a survey of Slovenians. Assessing reception requires
other evidence. The scan must arbitrate a proposed quotation; an English
translation cannot pass a character-exact test against a Slovene original.
An independent reader should inspect the full paragraph and challenge this
interpretation. That human review is proposed, not claimed as completed.

## Validate decisions, not the appearance of competence

Break outputs into checkable claims and inspect omissions as well as assertions.
An exact quotation check establishes that characters occur in a source; it does
not establish the correct speaker, date, scope or context. Check the locator
against the preserved document, then examine surrounding evidence and the
strength of the conclusion. Use precise error categories: invented claim,
misattribution, altered quotation, wrong locator, omitted qualification,
retrieval omission and unsupported translation. “Hallucination” here means
generated content fabricated or unsupported in the relevant evidential context;
a specific category is usually more useful. NIST's generative-AI risk profile
treats such confabulation alongside other system risks.[^ai-nist]

Choose a validation sample before optimizing prompts. Include a random sample
of ordinary material and deliberate strata for historical orthography, damaged
OCR, quotation, irony, language and genre. Record sample IDs and the denominator
for every rate; zero examined cases yield an undefined rate, not perfect
accuracy. Oversampling difficult passages diagnoses weaknesses but does not
estimate a collection-wide error rate without appropriate weighting. Report
small counts and uncertainty, including important cases excluded from the sample.

Have two readers independently apply a short codebook to selected claims where
feasible. Preserve their initial decisions, reasons and locators before
discussion. Adjudication records the chosen treatment and remaining
disagreement; majority agreement does not turn ambiguity into certainty.
Reference annotations are research judgements with review status, not neutral
ground truth. A classroom exercise can inspect every output; a larger project
needs an explicit sampling and escalation plan.

For classifiers, calibration compares predicted confidence with observed
correctness on suitable held-out material. A score of 0.9 is not automatically
a 90% chance of correctness. Guo and colleagues demonstrate that neural-model
confidence can be poorly calibrated.[^ai-calibration] Select calibration and
abstention thresholds on validation data, then evaluate on an untouched test
set. Report error and coverage: refusing half the cases changes what the system
describes. Inspect refusals by stratum so abstention does not systematically
erase minoritized language. A generator's confident wording is not this kind of
measured probability.

Compare against a baseline: manual source extraction, keyword retrieval or a
small rule set, evaluated on the same task and units. Include review time and
missed evidence. Keep evaluation documents out of training and prompt examples;
near-duplicate newspaper pages can leak across apparently separate splits.
Unknown proprietary training data limit claims of contamination-free testing.
Benchmark success on contemporary English does not establish performance on
historical Slovene. Ask whether the method improves this research operation
under its stated conditions.

## Test robustness within a defensible budget

Change one factor at a time: prompt wording, examples, passage order, retrieval
depth, context length or model. Repeat a fixed condition to observe run
variation, preserving failures and refusals. Liu and colleagues found positional
effects in the long-context tasks they studied; that motivates testing passage
order, not a universal claim about every present model.[^ai-context]
The [robustness workflow](../workflows/ai/compare-ai-output-across-prompts-models-and-runs.md)
compares consequential changes in attribution, evidence, uncertainty and
omission, separating them from stylistic variation.

Scoped red-teaming deliberately tests plausible failure conditions: a
misleading heading, contradictory passages or an instruction embedded in a
document. Treat source text as evidence, never as authority to change the
research procedure. Use authorized nonsensitive examples and a stop condition.
The exercise assesses a bounded vulnerability, not a competition to defeat a
chatbot. Agreement among models is not independent corroboration: they may
share data and failure patterns.

## Make ethical decisions change the workflow

A private letter can expose living relatives; removing a name may leave an
identifiable combination of events. Before sending material elsewhere, map
which personal or sensitive data cross the boundary, who can access them,
retention and deletion arrangements, training use, and contractual restrictions.
Minimize the submitted excerpt or use a controlled local route. Institutional
procurement and data-protection staff should resolve an uncertain lawful basis
or processing arrangement before transfer. EDPB guidance explains purpose
limitation, minimization and protection of sensitive data; public availability
does not settle those obligations.[^ai-privacy]

Rights decisions apply separately to source documents, annotations, models,
software and outputs. Permission to read a source need not permit redistribution
or submission to a third party. Check licences, terms of service, institutional
contracts and attribution conditions; record version and access date. Generated
output can reproduce protected expression, so a provider's permission to use an
output does not clear every underlying right. Where rights remain uncertain,
publish identifiers and a reconstruction procedure rather than unlicensed
copies, and record the issue for specialist review.

Cultural authority exceeds individual consent. A collection holder may not
speak for the community whose knowledge it contains. The CARE Principles for
Indigenous Data Governance foreground collective benefit, authority to control,
responsibility and ethics.[^ai-care] Their specific Indigenous context must not
be flattened into a generic checklist. Ask who can decide permitted uses,
review descriptions and request restriction, and budget participation. Do not
reproduce a colonial or partisan category as a neutral classifier label without
explaining its origin and consequences.

Language and domain inequality become visible through stratified errors,
retrieval omissions and correction effort. Avoid translating everything into
English simply because one system performs better there: retain the original
and audit semantic changes. Prevent automation bias by asking reviewers to read
sources before candidate answers. Preserve opportunities to practise source
criticism so assistance does not replace the skill needed to detect failure.
Credit annotation, transcription, translation and moderation labour; record
known working arrangements without inventing claims about unseen workers.

Assistive uses can widen access through reading support, transcription or draft
descriptions. Test outputs with their intended users: a shortened text can omit
uncertainty, and fluent image description can invent a detail. Offer an
accessible source-linked alternative and a correction route. Participation
should not require a paid account or disclosure of disability to a provider.

Financial and environmental proportionality belong in method selection.
Luccioni, Jernite and Strubell measure inference energy across tasks and models,
showing why deployment choices matter.[^ai-energy] Set a run budget, cache permitted
results and compare simpler methods. Record tokens or elapsed computation and
available energy measurements with their boundaries; unknown provider energy
is not zero, and a per-query carbon estimate is not universal. Include expert
checking costs when deciding whether assistance helps.

## Practice

Using the two packet passages, create a source register and audit the four
simulated failures. Add one omission that would change the historical argument.
Write a corrected 80-word interpretation and preserve both versions. Have a
partner apply your codebook before comparing decisions; if no partner is
available, mark human review pending. Complete the audit record, then design
the bounded robustness exercise without claiming unperformed runs. Submit the
claim table, sample IDs, disagreement note, cost ceiling and one reason to
abstain. Assessment concerns evidence and decisions, not access to an expensive
model.

## Reflection

Which parts could another scholar rerun, which could they only inspect, and
which might they reasonably dispute? Who bears the consequences of a missed
qualification? Would publishing the complete audit expose information the
research should protect? Explain one place where a methodological limit
requires narrowing the claim rather than improving the prompt.

## Summary

AI assistance becomes scholarly work through preserved evidence, explicit
tests and accountable interpretation. Disclose what assistance did, what people
checked and what remains unresolved; disclosure alone does not authorize the
practice. ALLEA's research-integrity code places responsibility on researchers
and institutions.[^ai-integrity] A useful assistance statement identifies the
task, model record, affected material, validation and responsible contributors.
Keep it with the versioned publication so corrections change the argument
visibly rather than silently replacing its evidential history.

## Further reading

- National Academies of Sciences, Engineering, and Medicine. 2019.
  *Reproducibility and Replicability in Science*.
  [Report and DOI](https://doi.org/10.17226/25303). Read for explicit definitions.
- Autio, Chloe, et al. 2024. *Artificial Intelligence Risk Management Framework:
  Generative Artificial Intelligence Profile*. NIST AI 600-1.
  [Report](https://doi.org/10.6028/NIST.AI.600-1). Use to develop scoped risk tests.
- Guo, Chuan, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger. 2017.
  “On Calibration of Modern Neural Networks.” *PMLR* 70: 1321–1330.
  [Paper](https://proceedings.mlr.press/v70/guo17a.html).
- Liu, Nelson F., et al. 2024. “Lost in the Middle: How Language Models Use
  Long Contexts.” *Transactions of the Association for Computational Linguistics*
  12: 157–173. [Paper](https://aclanthology.org/2024.tacl-1.9/).
- Carroll, Stephanie Russo, et al. 2020. “The CARE Principles for Indigenous
  Data Governance.” *Data Science Journal* 19: 43.
  [Paper](https://datascience.codata.org/en/articles/dsj-2020-043).
- Luccioni, Sasha, Yacine Jernite, and Emma Strubell. 2024. “Power Hungry
  Processing: Watts Driving the Cost of AI Deployment?” *FAccT '24*: 85–99.
  [DOI](https://doi.org/10.1145/3630106.3658542).
- ALLEA. 2023. *The European Code of Conduct for Research Integrity*, revised
  edition. [Code and translations](https://allea.org/code-of-conduct/).

[^ai-nas]: [National Academies report](https://doi.org/10.17226/25303), 2019. The five-part distinction is a teaching convention, not universal terminology.
[^ai-archive]: [dLib bibliographic record](https://www.dlib.si/details/URN:NBN:SI:doc-YPI8OFSU), checked 7 September 2026. Consult the packet's rights and transcription policies before reuse.
[^ai-nist]: [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1), 2024. The error categories operationalize this concern for source-based humanities work.
[^ai-calibration]: [Guo et al.](https://proceedings.mlr.press/v70/guo17a.html), 2017.
[^ai-context]: [Liu et al.](https://aclanthology.org/2024.tacl-1.9/), 2024.
[^ai-privacy]: European Data Protection Board, [Data protection basics](https://www.edpb.europa.eu/sme/learn-the-basics/data-protection-basics_en), consulted 7 September 2026. Applicability and institutional arrangements require case-specific assessment.
[^ai-care]: [Carroll et al.](https://datascience.codata.org/en/articles/dsj-2020-043), 2020; [Global Indigenous Data Alliance](https://www.gida-global.org/careprinciples), consulted 7 September 2026.
[^ai-energy]: [Luccioni, Jernite and Strubell](https://doi.org/10.1145/3630106.3658542), 2024; [author manuscript](https://arxiv.org/abs/2311.16863).
[^ai-integrity]: [ALLEA code](https://allea.org/code-of-conduct/), revised edition 2023. All linked sources were checked on 7 September 2026; this is a source-access date, not a human-review date.
