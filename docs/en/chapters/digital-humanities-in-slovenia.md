---
title: "Digital humanities in Slovenia: infrastructures, languages and communities"
description: "An analytical map of Slovenian cultural-heritage portals, research infrastructures, language resources and scholarly communities."
tags: [foundations, slovenia, infrastructure, language-resources, cultural-heritage]
status: draft
---

# Digital humanities in Slovenia: infrastructures, languages and communities

## Learning outcomes

After this chapter, you should be able to:

- distinguish a portal, repository, research infrastructure, research centre, knowledge centre, project, digital edition, corpus, tool and conference;
- explain how dLib.si, DARIAH-SI, SIstory, CLARIN.SI and CLASSLA support different parts of a research process;
- assess whether a public cultural-heritage object is also usable as machine-readable research data;
- relate Slovene and South Slavic language resources to task, period, genre, variety, licence and expert support;
- design a plausible path from a digitized source to a documented, citable and maintainable research object;
- prepare a reproducible profile of a Slovenian digital resource without repeating institutional publicity as evaluation.

## Before you begin: what makes a source usable?

Which Slovenian digital collections, dictionaries or corpora do you already use? Who selects, describes, funds and maintains them? Can you inspect a page image, search text, download structured data, cite a version and determine its licence—or only some of these things?

**Prerequisites:** read [Histories and genealogies of digital humanities](history-of-digital-humanities.md) and [Infrastructures of digital humanities](critical-infrastructures.md). **Input:** one Slovenian digital object and a humanities question that might use it. **Output:** a resource profile and a bounded research plan. **Check:** distinguish institutional description, observed interface behaviour, downloaded-file inspection, your own test and your interpretation. **Limits:** do not bypass access controls, redistribute protected material or assume that public viewing permits computational reuse.

The chapter's central claim is that **digital humanities in Slovenia is produced through relations among cultural-heritage institutions, research infrastructures, scholarly communities, language-resource centres, standards, public portals, repositories and teaching practices**. Those relations create real methodological possibilities, but also shape coverage, access, language support, preservation and the claims a researcher can responsibly make.

## A note on scope and historiography

This is a selective orientation to durable infrastructures and representative practices, current as observed on **22 July 2026**. It is not a complete catalogue, a ranking or a definitive institutional genealogy. Nor does it equate digital humanities with language technology. Work now read as digital humanities has often appeared under more specific names: scholarly editing, corpus linguistics, historical research data, lexicography, cultural-heritage digitization, spatial humanities, language technology and digital publishing. The absence of the label *digital humanities* is therefore not evidence that a practice was absent; retrospective naming must remain distinct from the terms used by participants at the time.

The following distinctions prevent a polished website from standing in for the organization, data and labour behind it:

| Official name | Type | Responsible institution or consortium | Principal scholarly function | Important limitation |
| --- | --- | --- | --- | --- |
| Digitalna knjižnica Slovenije – dLib.si | national digital-library portal and aggregator | Narodna in univerzitetna knjižnica (NUK) with contributing partners | discovery, metadata and access to digitized and born-digital heritage | public access does not guarantee bulk data, usable OCR or open reuse |
| Zgodovina Slovenije – SIstory | history portal and research-data environment | Research Infrastructure of Slovenian Historiography at the Institute of Contemporary History (INZ) | publication and contextualization of historical sources, literature, recordings and data | not a general OCR or language-processing service |
| DARIAH-SI | distributed national research infrastructure | nationally coordinated institutional network connected to DARIAH-EU | methods, standards, tools, training and community coordination | not one database or an automatic project pipeline |
| CLARIN.SI | national consortium and node of European CLARIN | Slovene consortium of research, university and other partners | repository, concordancers, language resources, tools and expert support | deposit and persistent identification do not make every resource open or fit for a question |
| CLASSLA | CLARIN Knowledge Centre | CLARIN.SI, CLADA-BG and the Institute of Croatian Language and Linguistics | documentation, helpdesk, training and publication support for South Slavic language resources and technologies | support and model quality vary by language, task and domain |
| Center za jezikovne vire in tehnologije Univerze v Ljubljani (CJVT UL) | university research and infrastructure centre | University of Ljubljana | development and maintenance of Slovene language resources and applications | an interface or centre catalogue does not establish one licence for all resources |
| Fran | lexicographic and language-resource portal | Fran Ramovš Institute of the Slovenian Language ZRC SAZU | integrated search across dictionaries and related language resources | portal display is not identical to downloadable source data |
| eZISS: Elektronske znanstvenokritične izdaje slovenskega slovstva | scholarly digital-edition series/project | Institute of Slovenian Literature and Literary Studies ZRC SAZU with the Jožef Stefan Institute (IJS) | facsimiles, scholarly transcriptions, apparatus and commentary encoded with open standards | content, source-file access and citation must be checked for each edition |
| Jezikovne tehnologije in digitalna humanistika (JT-DH) | recurring scholarly conference | current organizers named on the conference site | exchange across language technology, humanities fields and digital publishing | a meeting point is not the origin or complete boundary of a field |

These types overlap without becoming synonyms. A centre may operate a repository; a project may publish a corpus through a portal; a conference may connect people who maintain an infrastructure. The useful question is not “Which website contains my topic?” but “Which organization and data model can support this stage of my argument?”

## Digitization, libraries and cultural heritage

The **Narodna in univerzitetna knjižnica (NUK; National and University Library)** develops and maintains **Digitalna knjižnica Slovenije – dLib.si** with material from many partner institutions. The portal brings together digitized and born-digital books, periodicals, manuscripts, photographs, maps, music and other heritage objects. Its official history distinguishes the development of a digital-library concept in 2003, a public presentation in November 2005, and large digitization projects and the inclusion of partners from 2006 onward; later work established a national aggregation role connected to Europeana.[^dlib-history] These dates describe different events, not competing “launch” dates.

Methodologically, dLib.si can support discovery, bibliographic and descriptive metadata, inspection of page images and source criticism through facsimiles. It cannot be treated as a ready-made corpus. A catalogue record or viewer does not automatically establish bulk download, an API, article segmentation, machine-readable OCR of adequate quality, an open licence or representative coverage. The portal's terms distinguish public-domain material from rights-reserved objects, note that conditions can differ by item and location, and advise users to seek clarification where rights information is absent.[^dlib-rights] Researchers must therefore inspect the record, files, rights statement and actual download behaviour for the object they use.

This distinction changes the research question. A complete run of visible newspaper pages may still require transcription, article boundaries and issue metadata before frequency comparison. Conversely, a small set of page images can be excellent evidence for typography, layout or marginalia even when it is unsuitable for large-scale text analysis. “Digitized” describes a transformation and an access condition; “research-ready” is a claim that must be justified for a particular method.

## Historical research data: DARIAH-SI and SIstory

**DARIAH-SI** is the Slovenian branch of the distributed European Digital Research Infrastructure for the Arts and Humanities, DARIAH-EU. Its official overview describes a network that links institutions, people, projects, methods, standards and tools; national coordination is at the Institute of Contemporary History, with ZRC SAZU documented as a partner.[^dariah] DARIAH is thus social and technical infrastructure, not a single database. It can support shared practice through training, standards work and collaboration, while the institutions that hold or publish data retain concrete responsibilities for provenance, rights and maintenance.

**Zgodovina Slovenije – SIstory** must be kept separate from that network. The official project account dates its development to 2008 within the **Raziskovalna infrastruktura slovenskega zgodovinopisja** (Research Infrastructure of Slovenian Historiography) at the **Inštitut za novejšo zgodovino (INZ; Institute of Contemporary History)**. It describes a portal and research-data environment for historical sources, literature, recordings and data collections, connected to DARIAH-SI.[^sistory] SIstory can make structured historical data and its context publishable and reusable. It does not replace archival provenance, resolve every licence or perform universal OCR and natural-language processing.

The boundary matters. A table published through SIstory may encode persons, occupations or places according to a documented research design; DARIAH-SI may connect the project to methods and training. Neither fact proves that the table exhausts a population or that categories used in the source are analytically neutral. Researchers still need to inspect selection, schema, identifiers, missing values and change history. Current item totals are omitted here because institutional pages use mutable snapshots; scale is less informative than the conditions of a specific collection.

## Language resources: CLARIN.SI and CLASSLA

**Slovenska raziskovalna infrastruktura za jezikovne vire in tehnologije CLARIN.SI** is the Slovene national consortium and node of the European CLARIN infrastructure. Its official history distinguishes initial funding for a Slovene node at IJS in October 2013, signature of the consortium agreement in June 2014 and Slovenia's official CLARIN membership in 2015.[^clarin-history] The chronology records funding, organizational agreement and international membership—not three interchangeable founding dates.

CLARIN.SI operates a certified repository, concordancers and other services, and provides technical support, training and knowledge transfer. Repository records can describe corpora, lexicons, models, audio, video and tools; persistent identifiers support citation; licences and access controls record conditions; preservation arrangements support continued access.[^clarin-repository] None of these properties guarantees that a deposited object is open, ethically unproblematic, documented well enough for a new purpose or accurate for a particular period. A persistent identifier identifies an object or version; it does not replace a citation, provenance statement or quality evaluation. Rounded totals on CLARIN.SI pages were inconsistent when consulted, so this chapter does not reconcile or repeat them.

In 2019 CLARIN.SI and the Bulgarian national CLARIN centre established a South Slavic knowledge centre.[^clarin-history] Its current official Slovene name is **CLASSLA: K-center oziroma središče znanja CLARIN za južnoslovanske jezike**. The current page identifies CLARIN.SI, CLADA-BG and the Institute of Croatian Language and Linguistics as managing partners. CLASSLA provides documentation, a helpdesk for using, modifying, creating and publishing resources and technologies, training, and regional cooperation.[^classla-centre] It is therefore more than the CLASSLA-Stanza processing pipeline.

CLASSLA-web illustrates both the value and the limits of comparison. Version 1.0 was collected in 2021–2022 and released in 2024; the documented version 2.0 was collected in 2024 and deposited in 2026. The resource applies related collection, filtering and annotation procedures to web corpora for seven South Slavic languages.[^classla-web] This improves procedural comparability, but national-domain web text is not a national population. Coverage differs by language, domain, genre and script, and annotation quality remains task- and model-dependent. A comparative finding must therefore report the corpus version, per-language composition, query and validation—not infer equal support from a shared interface.

## Representative scholarly practices

Four cases show why object type and data access matter more than institutional prestige.

**Scholarly editing — eZISS.** The eZISS series integrates facsimiles, diplomatic or critical transcriptions, scholarly apparatus and commentary, sometimes with audiovisual material. Its documented technical approach uses Unicode, XML and the Text Encoding Initiative (TEI), separating a structured scholarly source from reading views.[^eziss][^eziss-method] The public object is an edition, not merely a scan. It enables comparison of witnesses and editorial interventions, but the interface alone does not authorize every download or make an editor's reconstruction into the unmediated text. Edition, version, source files, citation and reuse terms must be checked individually.

**Historical Slovene — IMP.** The *Digital library and corpus of historical Slovene IMP 1.1* combines facsimiles, corrected transcriptions, metadata and TEI P5 encoding; its downloadable CLARIN.SI record also provides an automatically annotated corpus and warns through its documentation that automatic linguistic annotation is error-prone.[^imp-record] Erjavec's peer-reviewed account explains the relation among digital library, annotated corpus, lexicon and historical-language processing.[^imp-article] IMP enables diachronic reading, concordancing and reproducible work with source XML. It does not make every year or genre equally represented, and a predicted lemma must not be treated as a verified historical fact.

**Digital lexicography — Fran and CJVT UL.** Fran integrates dictionaries and related resources of the Fran Ramovš Institute in a common search environment; its design has developed beyond a static reproduction of print dictionaries.[^fran][^fran-article] CJVT UL develops and maintains corpora, concordancers, lexicons and applications for contemporary Slovene across university partners.[^cjvt] Together they demonstrate how corpus evidence, lexicographic analysis and interfaces can interact. Yet one portal search can collapse differences among dictionary purposes and editions, and a public application does not imply that every underlying dataset has the same format, licence or maintenance plan.

**Historical data publication — SIstory.** A SIstory collection can join structured records, identifiers, contextual documentation and a public interface. That arrangement enables filtering, linking and reuse when a collection supplies the necessary files and terms. It cannot by itself establish the completeness of archival survival, the neutrality of a category or the accuracy of an imported record. Those are collection-level claims requiring documentation and tests.

## Teaching, conferences and communities

The **Slovensko društvo za jezikovne tehnologije (SDJT; Slovenian Language Technologies Society)** documents a conference tradition beginning with Language Technologies in 1998. The thematic expansion to **Jezikovne tehnologije in digitalna humanistika (JT-DH; Language Technologies and Digital Humanities)** was introduced in 2016. The conference is biennial and its proceedings provide a record of contributions.[^jtdh] It is best understood as a visible meeting point for language technology, digital linguistics, history, literary studies, cultural heritage, archaeology, education and digital publishing—not as the moment digital humanities was founded in Slovenia.

Community is also made through repository support, documentation, workshops, recorded lectures and helpdesks. These activities transfer tacit knowledge that a download cannot contain: how to interpret an annotation, choose a licence, diagnose historical-language errors or prepare a deposit. They also reveal a sustainability question. Training and coordination require funded people and institutional memory; a “free” service is not labour-free.

## The smaller-language condition and the European connection

Slovene should not be labelled inherently “low-resource.” Support is relational: good contemporary news lemmatization does not imply reliable eighteenth-century OCR; a large web corpus may omit spoken, dialectal or protected material; a multilingual model may expose an interface in Slovene while its training evidence remains unclear. Evaluate support by **task, genre, period, variety, licence, annotation standard, interface, model and available expertise**.

Constraints include historical orthography and inflection, older print and layouts, copyright, small licensable datasets for some tasks, dependence on multilingual systems and uneven regional or genre coverage. Strengths include concentrated expert communities, mature lexicographic and corpus traditions, reusable infrastructures, nationally coordinated standards and South Slavic cooperation. Neither deficit rhetoric nor technological nationalism is warranted. Language-specific scholarship adds knowledge that a generic multilingual system may lack, but local origin does not exempt a resource from evaluation.

CLARIN and DARIAH complicate a simple centre/periphery story. National nodes contribute resources, tools, expertise and standards work while gaining preservation arrangements, shared discovery, training and collaboration. They retain responsibility for local languages, rights, communities and priorities. European membership neither means “catching up” to a single centre nor erases unequal funding, institutional capacity and language visibility. Distributed infrastructure is a negotiated relation, not an equality certificate.

## Worked example: from a periodical page to a citable corpus

Suppose a student asks how a political concept changed in a small set of nineteenth- and early-twentieth-century Slovene periodicals discovered through dLib.si. The project is hypothetical, so no availability is assumed.

1. Record the dLib.si object and issue metadata, page range, holding institution and access date.
2. Inspect the item-level rights statement and actual download options before acquiring files.
3. Determine whether page images, OCR or transcriptions exist; sample errors by period and typography.
4. Produce or correct only the transcription permitted by rights and required by the question; preserve links to facsimiles.
5. Define article boundaries and document editorial metadata, advertisements, supplements and missing pages.
6. Keep diplomatic text separate from normalized forms. Test historical-language annotation on a stratified hand-checked sample; do not transfer contemporary-model accuracy.
7. Build a versioned corpus and run one bounded analysis, such as concordance comparison across named titles and periods. Return to page images for interpretation.
8. Publish permitted code, metadata, evaluation samples and derived data; state what cannot be shared.
9. Choose a repository or portal according to object type, deposit criteria and audience. Obtain a persistent identifier where appropriate and cite the version.
10. Assign responsibility for corrections, documentation, dependency changes and eventual retirement.

| Service or institution | Where it helps | Where it does not help automatically |
| --- | --- | --- |
| dLib.si | discovery, descriptive metadata, facsimiles and item-level rights information | clean bulk OCR, API access, article segmentation, open reuse or representative coverage |
| SIstory | historical-data publication and contextualization when the project and deposit arrangement fit | general language processing, copyright clearance or proof of archival completeness |
| CLARIN.SI | repository, concordancers, language resources and persistent identification when criteria and rights permit | a copyright solution, ethical approval or guaranteed historical-model accuracy |
| CLASSLA | documentation, expertise and tools for South Slavic processing | validated performance on this historical Slovene collection without local testing |
| DARIAH-SI | methods, standards, training and connection to a research community | a one-click transformation pipeline or automatic technical integration among services |

The arrows between these rows represent scholarly labour: rights research, transcription, modelling, validation, documentation and negotiation with maintainers. Unless an official source documents an integration, do not describe one.

## Practice: map one resource as a research object

Choose one Slovenian portal, repository, infrastructure, corpus, tool, edition or service. Create a versioned resource profile containing:

- official name, stable URL, type and access date;
- responsible institution or community;
- stated scope, documented omissions, languages, periods and genres;
- scholarly objects and unit of access;
- formats, metadata, search, API, download and export options;
- licence, copyright, privacy and access conditions;
- persistent identifier and recommended citation, if supplied;
- preservation or maintenance statement;
- one method the resource enables and one claim it cannot support without additional work;
- one lawful test you performed and the exact result.

Label every statement **institutional description**, **observed interface**, **download inspection**, **own test** or **interpretation**. **Check:** another student should be able to repeat your test. **Failure mode:** “the portal provides open data” is not evidence unless you name the item, file, licence and observed access path.

## Reflection

- Which Slovenian digital-humanities practices become invisible if the field is mapped only by projects that use the label *digital humanities*?
- When does a common European standard expand a local resource's reach, and which distinctions might it suppress?
- How would your result change if OCR errors, missing issues or model performance were distributed unevenly across periods and publishers?
- Who should decide whether maintaining, migrating or retiring a resource best serves its scholarly community?

## Summary

The Slovenian ecosystem is not a single centre or platform. NUK and its partners provide cultural-heritage discovery through dLib.si; DARIAH-SI connects institutions, methods and communities; SIstory publishes and contextualizes historical sources and data; CLARIN.SI sustains language resources, repository services and expertise; CLASSLA organizes South Slavic knowledge transfer; centres, edition projects, lexicographic portals and conferences create further scholarly objects and communities.

These relations do not turn public objects automatically into research-ready data. A responsible project identifies the type and maintainer of each service, checks files and rights at object level, evaluates language support for the actual task and period, preserves provenance, and records the manual work between systems. European infrastructures broaden collaboration while local institutions retain responsibility. The practical test is whether a researcher can connect a bounded claim to inspectable evidence, documented transformations, a citable version and a realistic maintenance path.

## Further reading and references

- Center za jezikovne vire in tehnologije Univerze v Ljubljani. “[CJVT UL](https://www.cjvt.si/)” and “[Tools and resources](https://www.cjvt.si/en/tools-and-resources/).” *Center za jezikovne vire in tehnologije Univerze v Ljubljani* website. Accessed July 22, 2026.
- CLARIN.SI. “[About the repository](https://www.clarin.si/info/about-repository/).” *CLARIN Slovenia* website. Accessed July 22, 2026.
- CLARIN.SI. “[CLASSLA: K-center za južnoslovanske jezike](https://www.clarin.si/info/k-center/).” *CLARIN Slovenija* website. Accessed July 22, 2026.
- CLARIN.SI. “[General information](https://www.clarin.si/info/general-information/).” *CLARIN Slovenia* website. Accessed July 22, 2026.
- CLASSLA. “[CLASSLA-web: South Slavic Web Corpora for Linguistic Research and Language Technology Development](https://clarinsi.github.io/classla-web/).” *CLASSLA-web* project website. Accessed July 22, 2026.
- Kuzman Pungeršek, Taja, Peter Rupnik, and Nikola Ljubešić. “[South Slavic Web Corpus Collection CLASSLA-web 2.0](https://www.clarin.si/repository/xmlui/handle/11356/2079).” CLARIN.SI repository record, issued January 27, 2026. PID: `http://hdl.handle.net/11356/2079`. Accessed July 22, 2026.
- DARIAH-SI. “[DARIAH-SI](https://dariah.si/dariah-si-eng/).” *DARIAH-SI* website. Accessed July 22, 2026.
- DARIAH-SI. “[SIstory](https://dariah.si/projekti/sistory/).” *DARIAH-SI* project pages. Accessed July 22, 2026.
- Erjavec, Tomaž. “[The IMP Historical Slovene Language Resources](https://doi.org/10.1007/s10579-015-9294-7).” *Language Resources and Evaluation* 49, no. 3 (2015): 753–775. DOI: `10.1007/s10579-015-9294-7`.
- Erjavec, Tomaž. “[Elektronske znanstvenokritične izdaje slovenskega slovstva: standardi in izzivi](https://nl.ijs.si/e-zrc/bib/eziss-knjiga.pdf).” In *Znanstvene izdaje in elektronski medij*, edited by Matija Ogrin, 51–70. Ljubljana: Založba ZRC, 2005. Accessed July 22, 2026.
- Erjavec, Tomaž. “[Digital library and corpus of historical Slovene IMP 1.1](https://www.clarin.si/repository/xmlui/handle/11356/1031).” CLARIN.SI repository record, issued July 28, 2014. PID: `http://hdl.handle.net/11356/1031`. Accessed July 22, 2026.
- Fran Ramovš Institute of the Slovenian Language ZRC SAZU. “[O portalu](https://www.fran.si/o-portalu).” *Fran: slovarji Inštituta za slovenski jezik Frana Ramovša ZRC SAZU* website. Accessed July 22, 2026.
- Ljubešić, Nikola, and Taja Kuzman. “[CLASSLA-web: Comparable Web Corpora of South Slavic Languages Enriched with Linguistic and Genre Annotation](https://aclanthology.org/2024.lrec-main.291/).” In *Proceedings of LREC-COLING 2024*, 3271–3282. ELRA and ICCL, 2024.
- Narodna in univerzitetna knjižnica. “[About dLib.si](https://www.dlib.si/About.aspx)” and “[Terms of use](https://www.dlib.si/Help.aspx).” *Digitalna knjižnica Slovenije – dLib.si* website. Accessed July 22, 2026.
- Perdih, Andrej. “[Portal Fran: od začetkov do danes](https://doi.org/10.31724/rihjj.46.2.28).” *Rasprave: Časopis Instituta za hrvatski jezik i jezikoslovlje* 46, no. 2 (2020): 997–1018. DOI: `10.31724/rihjj.46.2.28`.
- Slovensko društvo za jezikovne tehnologije. “[Konference Jezikovne tehnologije in digitalna humanistika](https://www.sdjt.si/wp/dogodki/konference/)” and “[Zborniki](https://www.sdjt.si/wp/dogodki/konference/zborniki/).” *SDJT – Slovensko društvo za jezikovne tehnologije* website. Accessed July 22, 2026.
- Založba ZRC. “[e-ZISS: Elektronske znanstvenokritične izdaje slovenskega slovstva](https://zalozba.zrc-sazu.si/sl/publikacije/e-ziss).” *ZRC SAZU* publication website. Accessed July 22, 2026.

[^dlib-history]: Narodna in univerzitetna knjižnica, “About dLib.si,” *Digitalna knjižnica Slovenije – dLib.si* website, accessed July 22, 2026. The page dates concept development, public presentation and subsequent project phases separately.
[^dlib-rights]: Narodna in univerzitetna knjižnica, “Terms of use,” *Digitalna knjižnica Slovenije – dLib.si* website, accessed July 22, 2026. Rights and access conditions are item-dependent; the page also notes that information may be incomplete.
[^dariah]: DARIAH-SI, “DARIAH-SI,” *DARIAH-SI* website, accessed July 22, 2026. The chapter reports institutional relations as documented on that date, not a permanent consortium list.
[^sistory]: DARIAH-SI, “SIstory,” project page, accessed July 22, 2026. The page dates development to 2008 and locates it within the Research Infrastructure of Slovenian Historiography at INZ.
[^clarin-history]: CLARIN.SI, “General information,” sections “First steps,” “Establishment of the Slovene CLARIN centre” and “CLARIN.SI today,” *CLARIN Slovenia* website, accessed July 22, 2026.
[^clarin-repository]: CLARIN.SI, “About the repository,” *CLARIN Slovenia* website, accessed July 22, 2026. The description covers certification, persistent identification, licences, access conditions and preservation arrangements; it does not imply unrestricted access.
[^classla-centre]: CLARIN.SI, “CLASSLA: K-center za južnoslovanske jezike,” *CLARIN Slovenija* website, accessed July 22, 2026. The managing institutions and services are current facts as displayed on that date.
[^classla-web]: CLASSLA, “CLASSLA-web,” *CLASSLA-web* project website, accessed July 22, 2026; Kuzman Pungeršek, Rupnik and Ljubešić, “South Slavic Web Corpus Collection CLASSLA-web 2.0,” CLARIN.SI repository record; Ljubešić and Kuzman, “CLASSLA-web.” The repository record dates version 2.0 to January 27, 2026; the peer-reviewed article describes version 1.0.
[^eziss]: Založba ZRC, “e-ZISS,” *ZRC SAZU* publication website, accessed July 22, 2026. The page dates the series from 2004 and describes the combination of facsimiles, transcriptions and scholarly commentary.
[^eziss-method]: Erjavec, “Elektronske znanstvenokritične izdaje slovenskega slovstva,” 51–70. The essay documents the XML/TEI method and the transformation from canonical source to reading formats.
[^imp-record]: Erjavec, “Digital library and corpus of historical Slovene IMP 1.1,” CLARIN.SI repository record. The record documents TEI files, derived formats, licence, metadata, facsimile links and automatic annotation.
[^imp-article]: Erjavec, “The IMP Historical Slovene Language Resources.” The article's reported composition describes the 2015 resource state; the repository record should govern citation and reuse of the deposited version.
[^fran]: Fran Ramovš Institute, “O portalu,” *Fran* website, accessed July 22, 2026. Current version and holding totals were not used because they are mutable.
[^fran-article]: Perdih, “Portal Fran: od začetkov do danes.” The article documents the portal's establishment in October 2014 and development through September 2019; it is not a statement of every current function.
[^cjvt]: CJVT UL, “CJVT UL” and “Tools and resources,” *Center za jezikovne vire in tehnologije Univerze v Ljubljani* website, accessed July 22, 2026.
[^jtdh]: Slovensko društvo za jezikovne tehnologije, “Konference” and “Zborniki,” *SDJT* website, accessed July 22, 2026. The event list begins in 1998; the conference page dates the thematic expansion to 2016 and describes the conference as biennial.
