---
title: "Critical infrastructures: power, access and maintenance"
description: "How collections, standards, interfaces, labour and maintenance shape digital-humanities evidence before analysis begins."
tags: [foundations, infrastructure, power, access, maintenance]
status: draft
---

# Critical infrastructures: power, access and maintenance

## Learning outcomes

After this chapter, you should be able to:

- define infrastructure as a relational arrangement rather than a list of machines;
- distinguish research, project, interface/information and social infrastructures;
- trace how archival, descriptive, technical and access decisions shape a humanities claim;
- explain how standards enable collaboration while constraining representation;
- identify sustaining labour and evaluate how governance distributes credit, authority and risk;
- distinguish access from accessibility and several meanings of openness;
- explain the different scopes of FAIR and CARE;
- design a reproducible infrastructure audit for a digital collection or tool.

## Before you begin: what stands behind a search?

Enter a word in a historical corpus and results appear in seconds. The action seems to involve a reader, a box and an index. Yet the result depends on records having been created and preserved; institutional selection and funding; cataloguing, scanning, optical character recognition (OCR) and article segmentation; identifiers and metadata; servers, software and ranking; rights decisions; and people who maintain every layer. Which of these conditions could change the result without changing the query?

**Prerequisites:** read [Models, evidence and interpretation](models-evidence-interpretation.md), especially its account of selection, categories and uncertainty. No programming is required. **Practice input:** one publicly describable digital collection or research service and one proposed humanities claim. **Output:** an evidence-labelled infrastructure audit. **Check:** another reader should be able to distinguish what you observed, what the institution states, what you tested and what you inferred. **Limits:** do not bypass access controls, expose sensitive records or treat legal availability as ethical permission.

The chapter's central claim is straightforward: **before an algorithm is chosen, infrastructures have already shaped what survives, what is digitized, how it is described, who can use it, which languages are supported, whose labour is visible and which claims can be sustained.**

## Infrastructure becomes visible when it fails

Infrastructure is not simply hardware, software or a large institution. It is a **relational arrangement** of people, organizations, standards, funding, routines, expertise, identifiers, interfaces, repositories, networks, material systems and maintenance. Something becomes infrastructure in relation to a practice: a persistent identifier supports citation only while registries, resolution services, metadata, contracts and local workflows continue to work.

Star and Ruhleder describe infrastructure as embedded in other arrangements, built on an installed base, learned through membership and connected to conventions. They also show how breakdown can make normally unnoticed dependencies perceptible.[^star-ruhleder] “Visible upon breakdown” is a useful investigative heuristic, not a universal law. An infrastructure may be highly visible to the administrator repairing it, the cataloguer entering data or the disabled reader encountering a barrier, while remaining unnoticed by a well-served user. Planned audits can reveal dependencies before failure.

Four overlapping levels help locate responsibility:

| Level | Examples | Characteristic question |
| --- | --- | --- |
| **Research infrastructure** | repositories, standards, shared services, centres, networks, preservation arrangements | Which communities can deposit, discover and sustain research objects? |
| **Project infrastructure** | code, schemas, servers, workflows, staffing, documentation and governance | Who can understand, operate and revise this project? |
| **Interface/information infrastructure** | search, ranking, metadata display, APIs, identifiers and default views | What becomes findable, comparable or exportable? |
| **Social infrastructure** | expertise, training, trust, funding, institutional memory and maintenance labour | Which relationships keep the other levels usable? |

These are analytical distinctions, not separate boxes. An API is technical, contractual and social at once. To trace power without declaring technology vaguely “biased,” ask of each important decision: **who decides; what becomes possible; what becomes difficult or invisible; who performs and maintains the work; who receives credit, access or risk; and what could be documented, redesigned or governed differently?**

## Archives and digitization are successive selections

A digital collection is neither the past nor an unmediated copy of an archive. At least nine selections precede a later corpus:

1. people and institutions create records, while other activities leave few or no records;
2. material survives use, neglect, deliberate destruction and accident;
3. archives appraise and acquire only part of what survives;
4. preservation and cataloguing allocate attention and description;
5. funders and institutions select materials for digitization;
6. scanning, transcription and OCR render some features more accurately than others;
7. segmentation and metadata define documents, dates, genres, persons and relations;
8. rights, privacy and cultural authority determine conditions of access;
9. interfaces rank results, after which researchers sample and clean another subset.

Archival scholarship has shown that record creation, appraisal and description participate in the production of social memory rather than neutrally storing it.[^archives-power] Klein's study of James Hemings demonstrates a specifically digital problem: visualization can reproduce an archival absence as empty space while careful design and reading make the conditions of that absence an object of interpretation.[^klein-absence] An absence does not, however, disclose its own cause. Non-creation, loss, exclusion, appraisal, unprocessed material, rights restrictions, failed OCR and search design can all produce an empty result. The responsible claim identifies known mechanisms, distinguishes evidence from hypothesis and records what investigation would be needed.

Selection distributes power concretely. A colonial administration may have produced extensive records about governed populations while preserving little self-authored testimony. A digitization board may prioritize famous holdings because they promise use and funding. Rights staff may restrict living-person records to prevent harm. Each choice can be justified in context, yet its consequences accumulate. Document collection scope, selection policies, known omissions and uncertainty rather than treating a large download as a complete population.

## Standards and classifications govern interpretation

Common structures enable exchange. A documented TEI customization can be validated, shared and transformed; a metadata schema aligns fields; identifiers connect versions; authority records gather name variants; a controlled vocabulary—an authorized set of preferred terms and relations—supports consistent retrieval. The TEI Guidelines themselves combine conformance with documented customization, acknowledging that a broad standard must be adapted to particular texts.[^tei]

The same arrangements constrain. A required single date may not represent “spring 1898”; a person/place distinction may mishandle a sacred geography; an authority record may privilege a colonial name; a controlled term can stabilize a category that historical actors disputed. Posner argues that identity fields are not neutral containers: their structure participates in constructing the data they appear merely to hold.[^posner] Bowker and Star likewise show that standards and classifications coordinate work while making some viewpoints routine and others difficult to express.[^bowker-star]

Interoperability is therefore neither neutral salvation nor cultural violence by definition. Ask what common structure the collaboration requires, which local distinctions must survive, and how source wording, ambiguity, uncertainty and extensions will be documented. Keep the original category beside a normalized one where feasible. Test whether “other” gathers systematic exclusions. Publish the schema version and mapping decisions. A valid file can still embody a poor historical model; an idiosyncratic file can preserve nuance yet prevent reuse.

## Labour, collaboration and credit

Digital scholarship is sustained by librarians, archivists, conservators, cataloguers, annotators, developers, research software engineers, designers, system administrators, students, crowd workers, rights staff, project managers and long-term maintainers. Their work may be intellectual, technical, clerical, administrative and affective at once. A clean dataset often hides decisions about illegible text, offensive description, uncertain identities and communication with represented communities. D'Ignazio and Klein treat this labour and the distribution of its benefits as part of data methodology, not background logistics.[^data-feminism]

Collaboration is not automatically exploitation. The difference turns on material and governing conditions: Were roles and pay agreed before work began? Can annotators contest a harmful category? Do contractors retain protections and receive usable documentation? Are maintenance and community consultation funded? Who owns the output and decides access? Who is named as author, contributor or acknowledged worker, and who carries liability when something fails?

Authorship cannot recognize every contribution by itself. Contracts, governance records, decision logs, acknowledgements and structured contributor statements can distribute credit and responsibility more precisely. The CRediT taxonomy offers fourteen standardized roles, including data curation, software, validation and project administration, while explicitly not deciding who qualifies as an author.[^credit] A project should adapt any taxonomy to its field and record labour it omits. Credit without decision-making power or fair compensation is not a substitute for just collaboration.

Maintenance is scholarly work because it preserves the conditions under which evidence can be inspected. Dependency updates can alter tokenization; a server migration can break identifiers; undocumented moderation can change a collection; staff turnover can erase knowledge of a schema. Funding novelty without migration, documentation and succession creates an epistemic weakness, not merely an IT inconvenience.

## Language, geography and the “global” field

“Low-resource” should describe a **relationship**, not a deficient language or community. Resources vary by task, genre, period and domain as well as by the availability and licensing of corpora, dictionaries, annotated examples, models, compute, interfaces and expert time. A language well supported for contemporary news translation may be poorly supported for eighteenth-century OCR or dialectal named-entity recognition. Research into the term itself finds several interacting axes and little consensus on a single threshold.[^low-resource]

For Slovene, a tool trained on contemporary standard-language prose may not transfer reliably to older typography, historical morphology or regionally mixed newspapers. A multilingual catalogue may display Slovene descriptions but rank queries through an English-centred index. These are testable infrastructure dependencies, not claims that Slovene lacks complexity or that every tool performs badly. Report performance for the actual period, genre and variety; preserve language tags and original wording; involve relevant expertise; and compare plausible baselines.

Risam's postcolonial account warns that apparently global digital knowledge can reproduce colonial cultural records and institutional centres while presenting local practices as peripheral.[^risam] Geography enters through funding eligibility, network reliability, hosting, travel, publication language and whose standards count. A locally maintainable method may be more rigorous than a prestigious service whose training data, contractual future or language performance cannot be inspected.

## Race, gender, coloniality and disability are infrastructural

Power operates through mechanisms already encountered: colonial record production shapes survival; racialized names and categories enter catalogues; gendered divisions of data-cleaning labour disappear behind an authored article; a search engine ranks commercial and socially dominant representations; an interface assumes a particular body, language and device. McPherson connects the separation of race from technical work to histories of computational and academic organization, while Noble's research on commercial search demonstrates that ranking and business models structure racialized and gendered visibility.[^mcpherson][^noble] These arguments concern specific histories and systems; they do not license a claim that every algorithm works identically.

Critical redesign changes decision points. Communities can participate in description and governance; source terminology can be retained beside revised access terms; harmful labels can be contextualized rather than silently normalized; subgroup and language errors can be measured; data workers can contest categories and receive credit. These measures do not repair a missing archive, but they change how its limits are represented and who can act.

**Access** means that a resource is available under stated permission and material conditions. **Accessibility** asks whether people with different bodies, senses, cognitive practices and assistive technologies can actually use it. An openly licensed image-only PDF without structure or text alternatives may provide access while excluding a screen-reader user. Williams argues for universal design in digital humanities: accessibility should inform creation, organization, presentation and preservation rather than appear as a late accommodation.[^williams] Universal design aims at broad use but does not remove the need for particular accommodations or consultation with disabled users. Keyboard operation, semantic headings, captions, transcripts, sufficient contrast, non-colour cues and documented alternative formats are scholarly inspectability features.

## Access, openness and rights

“Open” names several non-equivalent conditions:

- **open access** concerns access to a publication;
- **open data** permits data access and reuse under a stated open licence;
- **open-source software** makes source code available under a qualifying licence;
- **interoperable or reusable data** are structured and documented for further use;
- **public-domain material** is not restricted by copyright, though privacy or cultural responsibilities may remain;
- **controlled or mediated access** permits use through authorization, secure settings or community protocols.

One component does not determine the others. Open-source code can operate on restricted records; a public-domain scan can be delivered through an inaccessible interface; metadata can be reusable while images remain licensed. “As open as possible” must not become a reason to ignore people represented in the material, and closure must not escape scrutiny merely because it is protective.

The 2016 FAIR principles make digital research objects **Findable, Accessible, Interoperable and Reusable**. “Accessible” permits authentication and authorization where necessary; FAIR does not require unrestricted public download and does not by itself establish data quality or ethical legitimacy.[^fair] The CARE Principles for Indigenous Data Governance foreground **Collective Benefit, Authority to Control, Responsibility and Ethics**. They were developed through Indigenous data-sovereignty networks and address Indigenous Peoples' rights and interests in data about their peoples, territories, knowledges and cultures.[^care][^gida]

FAIR asks mainly whether data and metadata can be found, accessed under clear conditions, combined and reused. CARE asks who benefits, who has authority and which responsibilities govern use in the specific context of Indigenous data. They can complement one another, but a technically FAIR object may violate CARE, and legitimate authority to control may limit reuse. CARE is neither confined to one country nor a generic ethics acronym to detach from Indigenous governance. Other projects may learn to ask relational questions about benefit and authority without appropriating CARE or claiming compliance where its scope is not engaged.

## Maintenance and environmental cost

Digital preservation is active. Storage media fail; backups and redundant copies require equipment, energy and checking; formats and dependencies need migration; certificates, domains and identifiers expire; models require computation; devices are manufactured, transported and replaced. Jackson's “broken world” perspective treats repair as a site of knowledge, care and power rather than a lesser activity after innovation.[^jackson] Pendergrass and colleagues similarly argue that appraisal, permanence and availability must be reconsidered within environmentally sustainable digital preservation.[^sustainability]

There is no single comparable carbon number for “a digital project.” Impacts depend on electricity, hardware, location, storage policy, traffic, model, reuse and system boundary. Sensational estimates obscure decisions. Ask instead: What storage, duplication and compute are justified by the scholarly and preservation purpose? Can scans, models or pipelines be reused? Would a smaller method answer the question? Which files merit which preservation level? Who budgets for migration, documentation, security, accessibility and eventual decommissioning after funding ends?

Technical debt is the future work created when expedient design choices make change harder. Some debt is deliberate and documented; hidden debt transfers cost to maintainers or users. A sustainability plan should name owners, service levels, dependencies, export routes, preservation targets, funding assumptions and a responsible end-of-life path. Keeping everything online forever is not the only form of care, but silent disappearance is not a preservation policy.

## Worked example: a smaller-language historical newspaper corpus

Suppose researchers ask how public fear was framed in a smaller-language newspaper tradition across a century. The infrastructure dependency chain is cumulative:

1. **Survival:** only certain titles, years and physical copies remain; survival may differ by region and publisher.
2. **Digitization selection and funding:** an institution chooses a subset, perhaps prioritizing condition, demand, significance, rights or available funds; the rationale and rejected material should be recorded.
3. **Scanning:** bound volumes, bleed-through, damaged paper, columns and advertisements affect image and layout quality.
4. **OCR:** accuracy varies with period, typeface, orthography, language variety and page condition; evaluation must be stratified rather than reduced to one score.
5. **Segmentation and metadata:** article boundaries, dates, genres, titles and newspaper identities are inferred or entered; a page is not automatically an article.
6. **Rights and delivery:** copyright, privacy or contracts may allow reading but prohibit bulk download, or provide an API with limits; this changes reproducibility and sampling.
7. **Search and ranking:** default date ranges, stemming, snippet generation and relevance ranking affect discovery; a search result is not a random sample.
8. **Researcher construction:** the team defines inclusion, removes duplicates, cleans OCR and records exclusions; each transformation receives a version and audit trail.
9. **Analysis:** a topic or emotion model operationalizes “fear” through words, passages or labels; its categories and language resources add another layer.
10. **Validation:** researchers compare OCR with page images across titles, periods and layouts; inspect article boundaries; manually code a stratified sample; and test whether results survive alternative cleaning and coverage controls.
11. **Publication and preservation:** the team publishes permitted data, identifiers, code, model and error summaries, documents restricted inputs, deposits a versioned package and assigns maintenance responsibility.

Two distortions show why the chain matters. First, if older pages have worse OCR, fewer fear-related words may be recognized, producing an apparent historical increase even when printed usage is stable. Period-stratified OCR evaluation, image checks and sensitivity analyses can bound that claim. Second, failed article boundaries may attach a crime report to an adjacent political editorial, while uneven newspaper coverage changes the mixture of genres and political positions. The resulting shift in “emotional framing” could be compositional rather than linguistic. Boundary checks, title/genre distributions and within-stratum comparisons offer tests.

The conclusion is not that computational analysis is impossible. Infrastructure changes the evidential basis. A defensible finding might concern the **digitized, licensed and validated subset under documented error and coverage conditions**, not “the national press” without qualification.

## Practice: conduct a reproducible infrastructure audit

Choose one digital collection, repository, corpus or scholarly tool and one proposed humanities claim. Produce a table or dossier covering:

| Audit area | Minimum evidence |
| --- | --- |
| Responsibility and scope | responsible institution/community; stated collection scope; documented omissions and your observed gaps |
| Objects and description | formats, identifiers, metadata schema, classifications, controlled vocabularies, source terminology and uncertainty |
| Transformation | digitization, OCR or transcription method; language support; published quality claims; your lawful spot tests |
| Use | accessibility with keyboard/assistive technology where you can test it; rights, privacy, cultural authority; search, ranking, API and export conditions |
| People and authority | labour and contributor roles; governance, credit, funding and who can correct or remove material |
| Continuity and materiality | maintenance owner, preservation plan, dependencies, storage/compute needs and documented environmental policy or its absence |
| Consequence | one way each finding enables, limits or changes the proposed claim; a validation or redesign response |

Label every entry as one of four evidence statuses: **observed fact** (what you can inspect), **institutional claim** (with page and access date), **test result** (method, sample and date) or **your interpretation** (reasoning and alternatives). Do not convert an undocumented feature into an accusation. Record “not found after checking X and Y” rather than “does not exist.”

**Output:** the completed audit, a dependency diagram or ordered chain, and a 500-word claim assessment. **Check:** a peer should reproduce two observations and one test from your record. **Failure modes:** relying only on an “About” page; confusing no search result with no historical record; testing only an easy document; or recommending openness without checking rights and authority.

## Reflection

- Which dependency was invisible to you before the audit, and to whom was it probably already visible?
- Where does a standard enable comparison, and which distinction does it displace?
- Who can change a harmful category or inaccessible interface, and who bears the cost while waiting?
- Which absence in your collection has a documented cause, which has several plausible causes and which remains uninterpretable?
- What level of maintenance and environmental cost is proportionate to the claim and future reuse?

## Summary

Infrastructure is a relational condition of knowledge production. Archives, digitization, metadata, classifications, interfaces, rights, language support and preservation successively select what can become evidence. These arrangements distribute visibility, labour, credit, authority, access and risk. Their effects must be traced through decisions rather than condensed into a claim that technology is simply biased.

Standards can enable validation, exchange and preservation while constraining local or ambiguous meanings. Collaboration becomes more just through governance, compensation, contestable categories and precise credit; maintenance protects the inspectability of evidence. Smaller-language support is relative to task, period, genre and infrastructure. Access is not accessibility, and openness, FAIRness and responsible governance are distinct. CARE retains its specific grounding in Indigenous data governance. Environmental responsibility is best approached through proportionality, reuse and named long-term ownership.

An infrastructure audit does not stand outside interpretation. It establishes the population, transformations, permissions and uncertainties to which an interpretation must remain answerable. The later chapter [AI, ethics and reproducibility](ai-ethics-reproducibility.md) turns many of these structural questions into project-level safeguards and documentation practices.

## Further reading and references

- Bowker, Geoffrey C., and Susan Leigh Star. [*Sorting Things Out: Classification and Its Consequences*](https://mitpress.mit.edu/9780262522953/sorting-things-out/). MIT Press, 1999. *MIT Press* website. Accessed July 22, 2026.
- Carroll, Stephanie Russo, Ibrahim Garba, Oscar L. Figueroa-Rodríguez, et al. “[The CARE Principles for Indigenous Data Governance](https://doi.org/10.5334/dsj-2020-043).” *Data Science Journal* 19 (2020): 43. DOI: `10.5334/dsj-2020-043`.
- D'Ignazio, Catherine, and Lauren F. Klein. [*Data Feminism*](https://doi.org/10.7551/mitpress/11805.001.0001). MIT Press, 2020. DOI: `10.7551/mitpress/11805.001.0001`.
- Global Indigenous Data Alliance. “[CARE Principles for Indigenous Data Governance](https://www.gida-global.org/careprinciples).” *Global Indigenous Data Alliance* website. Accessed July 22, 2026.
- Jackson, Steven J. “[Rethinking Repair](https://doi.org/10.7551/mitpress/9780262525374.003.0011).” In *Media Technologies: Essays on Communication, Materiality, and Society*, edited by Tarleton Gillespie, Pablo J. Boczkowski and Kirsten A. Foot, 221–240. MIT Press, 2014. DOI: `10.7551/mitpress/9780262525374.003.0011`.
- Klein, Lauren F. “[The Image of Absence: Archival Silence, Data Visualization, and James Hemings](https://doi.org/10.1215/00029831-2367310).” *American Literature* 85, no. 4 (2013): 661–688. DOI: `10.1215/00029831-2367310`.
- McPherson, Tara. “[Why Are the Digital Humanities So White? or Thinking the Histories of Race and Computation](https://doi.org/10.5749/minnesota/9780816677948.003.0017).” In *Debates in the Digital Humanities*, edited by Matthew K. Gold, 139–160. University of Minnesota Press, 2012. DOI: `10.5749/minnesota/9780816677948.003.0017`.
- National Information Standards Organization. “[ANSI/NISO Z39.104-2022, CRediT, Contributor Roles Taxonomy](https://doi.org/10.3789/ansi.niso.z39.104-2022).” NISO, 2022. DOI: `10.3789/ansi.niso.z39.104-2022`.
- Nigatu, Hellina Hailu, Atnafu Lambebo Tonja, Benjamin Rosman, Thamar Solorio, and Monojit Choudhury. “[The Zeno’s Paradox of ‘Low-Resource’ Languages](https://doi.org/10.18653/v1/2024.emnlp-main.983).” In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*, 17753–17774. Association for Computational Linguistics, 2024. DOI: `10.18653/v1/2024.emnlp-main.983`.
- Noble, Safiya Umoja. [*Algorithms of Oppression: How Search Engines Reinforce Racism*](https://nyupress.org/9781479866762/algorithms-of-oppression/). NYU Press, 2018. *NYU Press* website. Accessed July 22, 2026.
- Pendergrass, Keith L., Walker Sampson, Tim Walsh, and Laura Alagna. “[Toward Environmentally Sustainable Digital Preservation](https://doi.org/10.17723/0360-9081-82.1.165).” *The American Archivist* 82, no. 1 (2019): 165–206. DOI: `10.17723/0360-9081-82.1.165`.
- Posner, Miriam. “[What’s Next: The Radical, Unrealized Potential of Digital Humanities](https://doi.org/10.5749/j.ctt1cn6thb.6).” In *Debates in the Digital Humanities 2016*, edited by Matthew K. Gold and Lauren F. Klein, 32–41. University of Minnesota Press, 2016. DOI: `10.5749/j.ctt1cn6thb.6`.
- Risam, Roopika. [*New Digital Worlds: Postcolonial Digital Humanities in Theory, Praxis, and Pedagogy*](https://nupress.northwestern.edu/9780810138865/new-digital-worlds/). Northwestern University Press, 2018. *Northwestern University Press* website. Accessed July 22, 2026.
- Schwartz, Joan M., and Terry Cook. “[Archives, Records, and Power: The Making of Modern Memory](https://doi.org/10.1007/BF02435628).” *Archival Science* 2 (2002): 1–19. DOI: `10.1007/BF02435628`.
- Star, Susan Leigh, and Karen Ruhleder. “[Steps Toward an Ecology of Infrastructure: Design and Access for Large Information Spaces](https://doi.org/10.1287/isre.7.1.111).” *Information Systems Research* 7, no. 1 (1996): 111–134. DOI: `10.1287/isre.7.1.111`.
- Text Encoding Initiative Consortium. “[TEI: Guidelines for Electronic Text Encoding and Interchange](https://tei-c.org/release/doc/tei-p5-doc/en/html/).” P5 version 4.11.0, last updated February 18, 2026. *Text Encoding Initiative* website. Accessed July 22, 2026.
- Wilkinson, Mark D., Michel Dumontier, IJsbrand Jan Aalbersberg, et al. “[The FAIR Guiding Principles for Scientific Data Management and Stewardship](https://doi.org/10.1038/sdata.2016.18).” *Scientific Data* 3 (2016): 160018. DOI: `10.1038/sdata.2016.18`.
- Williams, George H. “[Disability, Universal Design, and the Digital Humanities](https://doi.org/10.5749/minnesota/9780816677948.003.0020).” In *Debates in the Digital Humanities*, edited by Matthew K. Gold, 202–212. University of Minnesota Press, 2012. DOI: `10.5749/minnesota/9780816677948.003.0020`.

[^star-ruhleder]: Star and Ruhleder, “Steps Toward an Ecology of Infrastructure,” 111–134. Their account develops from a particular distributed scientific collaboration; the properties are analytical resources, not a universal checklist that every infrastructure exhibits identically.
[^archives-power]: Schwartz and Cook, “Archives, Records, and Power,” 1–19, on records and archives as active participants in the formation of memory and identity. The nine-stage sequence in this chapter extends the analysis into digitization, interfaces and later research use.
[^klein-absence]: Klein, “The Image of Absence,” 661–688. The case concerns the archive of slavery and James Hemings; it supports attention to how visualization engages absence, not a general inference about the cause of every missing record.
[^tei]: Text Encoding Initiative Consortium, *TEI Guidelines*, especially chapters 1 and 24 on schemas, validation, customization, conformance and documentation.
[^posner]: Posner, “What’s Next,” 32–41. Her argument is a programmatic intervention about data models, difference and power, not a claim that formalization should be abandoned.
[^bowker-star]: Bowker and Star, *Sorting Things Out*, on classification and standards as information infrastructure with practical and distributive consequences.
[^data-feminism]: D'Ignazio and Klein, *Data Feminism*, especially the principles on examining power, challenging binaries, elevating emotion and embodiment, embracing pluralism, considering context and making labour visible.
[^credit]: National Information Standards Organization, *ANSI/NISO Z39.104-2022*. The standard describes contributions; it explicitly does not set authorship criteria.
[^low-resource]: Nigatu et al., “Zeno’s Paradox,” 17753–17774. Their review of 150 publications identifies multiple interacting axes and limited agreement in uses of “low-resource.”
[^risam]: Risam, *New Digital Worlds*, especially chapters 2 and 3 on colonial violence in digital cultural records and the relation between local practices and global formations.
[^mcpherson]: McPherson, “Why Are the Digital Humanities So White?,” 139–160. Her historical analogy between modularity and racial formations is an argument against separating cultural critique from technical production, not a one-to-one technological determinism.
[^noble]: Noble, *Algorithms of Oppression*, on commercial search, ranking, advertising and racialized and gendered representation. The present chapter applies that insight only to discoverability and interface power, not to every scholarly retrieval system.
[^williams]: Williams, “Disability, Universal Design,” 202–212. His intervention argues that digital-humanities design can disable users and should incorporate accessibility from the outset.
[^fair]: Wilkinson et al., “FAIR Guiding Principles,” especially principle A1.2, which permits authentication and authorization. FAIR specifies characteristics for machine-assisted discovery and reuse; it is not a synonym for open data.
[^care]: Carroll et al., “CARE Principles,” article 43, on Collective Benefit, Authority to Control, Responsibility and Ethics as people- and purpose-oriented principles for Indigenous data governance.
[^gida]: Global Indigenous Data Alliance, “CARE Principles,” on the 2018 Gaborone workshop, Indigenous data-sovereignty networks and the intended complementarity with FAIR. The page is mutable; access date is recorded.
[^jackson]: Jackson, “Rethinking Repair,” 221–240, on breakdown, maintenance and repair as sites of creativity, knowledge, power and care.
[^sustainability]: Pendergrass et al., “Toward Environmentally Sustainable Digital Preservation,” 165–206, on integrating environmental criteria into appraisal, permanence and availability rather than relying on technological efficiency alone.
