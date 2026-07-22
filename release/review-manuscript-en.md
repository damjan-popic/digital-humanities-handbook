# Digital Humanities Handbook

**Stable core and course pathways — development review snapshot**

**Version:** 0.1.0-dev  
**Date:** 2026-07-20  
**Author/editor:** Damjan Popič

> This file is generated from the version-controlled source. The public web edition is canonical for navigation and interactive material.

---

# Part I: Handbook chapters

## What is digital humanities?

## Learning outcomes

After this chapter, you should be able to:

- explain digital humanities as a relationship between humanities questions, structured evidence and computation;
- distinguish digitization, digital research and critical interpretation;
- describe the main stages of a digital-humanities project;
- identify where modelling choices and bias enter a workflow;
- explain why computational scale does not remove the need for close reading.

## Before you begin

Think of one humanities object you know well: a novel, newspaper archive, translation corpus, collection of letters, historical map, oral-history interview or museum catalogue. What parts of that object are immediately visible to a reader, and what would have to be represented explicitly before a computer could work with it?

## A field, a method and an argument

Digital humanities is often described through tools: corpora, OCR, GIS, databases, network analysis, topic models or machine learning. That list is useful, but incomplete. A project becomes digital-humanities research when computational work is part of a humanities argument about language, culture, history, literature, memory, space or society.

Three activities are related but not identical:

1. **Digitization** creates digital representations of analogue materials, for example scans and OCR text.
2. **Digital scholarly work** organizes, searches, annotates, links or publishes cultural materials.
3. **Computational analysis** uses formal procedures to identify, compare or model patterns that are difficult to inspect manually.

None of these activities automatically produces interpretation. A frequency table does not explain a historical change; a map does not prove spatial causation; a topic model does not discover the true themes of a corpus. The researcher still has to connect the result to a defensible claim and to the contexts in which the evidence was produced.

## The research cycle

A useful project can be understood as a cycle rather than a straight pipeline:

1. **Question** — formulate a humanities problem that can be investigated with evidence.
2. **Sources** — select and document materials, including exclusions and rights.
3. **Model** — decide what counts as a document, person, place, event, emotion, topic or relation.
4. **Transform** — digitize, clean, normalize, annotate or link the material.
5. **Analyse** — apply a method appropriate to the question and data.
6. **Validate** — inspect errors, compare baselines and test alternative explanations.
7. **Interpret** — return patterns to historical, linguistic, literary or cultural context.
8. **Publish** — make the reasoning, data provenance and limitations inspectable.

The cycle matters because later findings often force earlier decisions to be revised. An OCR error may explain a suspicious keyword. A map may reveal inconsistent place names. Manual checking may show that an emotion lexicon confuses fear with politeness. Iteration is not failure; undocumented iteration is.

## Data are made, not found

Cultural material does not arrive as neutral data. A corpus is produced through selection. A database is produced through categories. An annotation scheme decides which differences matter. Missing values can represent absence, uncertainty, loss, censorship or simply an unrecorded fact.

This does not make digital methods invalid. It makes documentation essential. A strong project records:

- where each source came from;
- how it was transformed;
- which units and categories were defined;
- which material was excluded and why;
- which errors were measured or observed;
- which claims the method can and cannot support.

## Scale and reading

Digital methods can move across thousands of documents, but scale is not a replacement for reading. It changes where reading happens. Researchers read sample texts to design categories, read model errors to understand limitations, read outliers to discover unexpected cases, and read passages in context to test whether aggregate patterns are meaningful.

A productive relationship is therefore not **close reading versus distant reading**, but movement between levels: collection, document, passage, token, entity, place and relation.

## Worked example: changing descriptions of migration

Suppose you ask how Slovenian newspapers framed migration between 1995 and 2025.

A weak design downloads whatever articles are easy to find, counts words and treats the graph as the answer.

A stronger design asks:

- Which newspapers and genres are represented in each period?
- Are article counts comparable across years?
- Which terms are used to retrieve relevant texts, and what do they miss?
- Is the unit of analysis an article, paragraph, sentence or quoted speaker?
- How will frames be operationalized: keywords, collocations, manual labels, embeddings or a combination?
- How will automatic labels be validated?
- Which political and media changes must be considered when interpreting the result?

The computational method is only one component. The argument depends equally on source criticism, corpus design, validation and historical interpretation.

## Practice

Choose one cultural collection and write a one-page project sketch with eight headings: question, sources, model, transformation, analysis, validation, interpretation and publication. Under each heading, state one decision and one risk.

## Reflection

- Which part of your project is most likely to be mistaken for a purely technical task?
- Where could an apparently reasonable category impose a modern or institutional viewpoint on the sources?
- What would you need to read manually before trusting a large-scale result?

## Summary

Digital humanities joins computation to humanities inquiry. Its central object is not the tool but the chain of reasoning from sources to claims. Because cultural data are constructed through selection and modelling, a credible project makes those decisions visible, validates automated results and moves repeatedly between aggregate patterns and contextual reading.

## Further reading

- Burdick, Anne et al. *Digital_Humanities*. MIT Press, 2012.
- Drucker, Johanna. *Graphesis: Visual Forms of Knowledge Production*. Harvard University Press, 2014.
- Gold, Matthew K., and Lauren F. Klein, eds. *Debates in the Digital Humanities*. University of Minnesota Press.
- Ramsay, Stephen. *Reading Machines: Toward an Algorithmic Criticism*. University of Illinois Press, 2011.

---

## Histories and genealogies of digital humanities

## Learning outcomes

After this chapter, you should be able to:

- explain why digital humanities has several overlapping histories rather than one uncontested origin;
- distinguish retrospective precursors from work described in its own time as *humanities computing* or *digital humanities*;
- relate punched-card processing, professional associations, text encoding, personal computing and networks to changing forms of humanities research;
- identify the scholarly, technical, clerical and maintenance labour hidden by founder-centred narratives;
- compare competing periodizations and explain the shift in terminology without treating it as a simple replacement;
- evaluate a historical claim by checking the date, institutional source, terminology and material evidence on which it depends.

## Before you begin: what counts as a beginning?

Where should a history of digital humanities begin: with a medieval concordance, nineteenth-century counting, electronic computers, a professional association, a book title, or the moment when researchers began calling themselves *digital humanists*? Each answer creates a different object of study. A long genealogy emphasizes continuities in indexing, comparison and modelling; a narrower institutional history asks when a recognizable community acquired journals, conferences, centres and names.

**Prerequisites:** no programming is required, but you should be familiar with the distinction between digitization, digital research and interpretation in the preceding chapter. **Inputs for the practice task:** one timeline claim, an official or primary source and a peer-reviewed historical source. **Ethical and licensing limits:** cite rather than appropriate source material, keep quotations short, respect access restrictions and do not reproduce archival images or personal testimony without checking rights, consent and context.

This chapter therefore uses **precursor** for an earlier practice that can illuminate a later method without being identical to it. It reserves **humanities computing** for a historically situated cluster of computer-assisted research, teaching and support practices, particularly from the mid-twentieth century onward. **Digital humanities** names a later and broader formation whose boundaries remain disputed. These are analytical distinctions, not three sealed eras.

## Why the field has more than one history

Susan Hockey's influential account organizes humanities computing into beginnings (1949 to the early 1970s), consolidation (the 1970s to the mid-1980s), new developments (the mid-1980s to the early 1990s) and the Internet era. That sequence is valuable for tracing text-centred methods, but Hockey herself warns that a linear chronology cannot answer every question about an interdisciplinary activity.[^periodization] Other histories begin with libraries and scholarly editing, quantitative literary study, historical databases, archaeology, linguistic corpora, digital art, public history, media studies or cultural-heritage institutions. Empirical study of the early journals also shows more work on sound, images, teaching and technology than a text-only origin story admits.[^journals]

Periodization is consequently an argument. A history built from conference proceedings foregrounds professional identity; an oral history reveals informal learning and support work; a history of standards follows negotiation and maintenance; a critical or global history asks whose languages, institutions and material conditions disappear when a North Atlantic network is made to stand for the whole field. No single archive answers all of these questions, and important administrative and technical records were never preserved. Nyhan and Flinn accordingly describe the surviving evidence as partial and use testimony alongside documents, while cautioning that recollection is itself situated evidence.[^oral-history]

The plural **histories** is not an invitation to list everything that ever combined culture and calculation. It is a method: specify the genealogy being traced, identify the evidence that makes it visible, and state what that evidence leaves out.

## Before electronic computing: retrospective precursors

Concordances, catalogues, indexes, editions, chronologies and prosopographies organized cultural evidence long before electronic machines. A **concordance** lists occurrences of words, normally with enough surrounding text or location information to support comparison. Its making requires decisions about the text, token boundaries, spelling variants, headwords and reference systems. Those intellectual operations did not begin with computers.

Nineteenth- and early twentieth-century scholars also counted word lengths, vocabulary and stylistic features, while philologists, historians, librarians and social scientists constructed samples, tables and classifications. Underwood's genealogy of distant reading is instructive: large-scale and empirical literary history has social-scientific as well as computational lineages, so it should not be projected backward as if every quantitative predecessor were already practising digital humanities.[^precursors] Similarly, a manuscript catalogue may resemble a database without belonging to the institutional or technical formation later called humanities computing.

Calling these practices precursors can reveal continuities in modelling and labour. It can also distort them by making the past look like an incomplete version of the present. The responsible question is not “How early can digital humanities be found?” but “Which problem, practice or institution is this genealogy meant to explain?”

## 1940s to early 1970s: humanities computing

Roberto Busa's *Index Thomisticus* is indispensable to this period, but it is not a creation story for an entire field. Busa later recalled searching for mechanized assistance between 1941 and 1946 and securing IBM collaboration in 1949. Scholarship therefore uses both 1946, for the project's conception, and 1949, for its IBM-supported implementation; neither date makes all earlier or parallel genealogies disappear.[^busa] The project sought a lemmatized concordance to the works of Thomas Aquinas and related texts. **Lemmatization** groups inflected forms under a dictionary headword, a demanding task in medieval Latin. Punched cards, sorting and concordance programs enabled work at a new scale, but human judgment remained necessary where automatic procedures failed.[^hockey-history]

The familiar image of Busa at a machine conceals an organization. The *Index* depended on IBM engineers and equipment, programmers, scholarly collaborators, keypunch operators, verifiers, trainers, transport and institutional funding. Archival and oral-history research recovered women who encoded and checked cards in Busa's training school from 1954 to 1967; their contribution had largely vanished from published accounts even though the data foundation depended on it.[^busa-labour] “Automation” redistributed labour and authority rather than removing people from the process.

In the workflows Hockey surveys, textual data were entered on punched cards holding up to eighty characters or on paper tape, processed in batches and returned as printout. Character representation was constrained, and large datasets stored on magnetic tape had to be processed sequentially.[^material-history] Access depended on institutional computing centres. These conditions were methodological: a representation designed around a card layout, storage medium or particular program could determine what counted as a textual unit and which variants survived.

The emerging community was already wider than one project. Researchers produced concordances, dictionaries, authorship studies and textual analyses; centres supplied technical support; conferences circulated techniques. *Computers and the Humanities* began publication in 1966, and a recurring literary and linguistic computing conference series followed a Cambridge symposium in 1970.[^early-institutions] These venues made shared problems visible, but their published authors were only part of the workforce. Operators, computing-centre staff, librarians, research assistants and administrators also made computation usable.

## 1970s to the mid-1980s: professionalization and consolidation

During the 1970s, reusable programs, text archives, centres, courses and regular meetings reduced the need for every project to invent its own technical system. The Association for Literary and Linguistic Computing (ALLC) was founded in 1973, initially to support computing in language and literature; the Association for Computers and the Humanities (ACH) followed in 1978.[^associations] Their titles show that there was no single stable label: *literary and linguistic computing*, *computers and the humanities* and *humanities computing* overlapped.

Professionalization did not mean methodological uniformity. Literary scholars and linguists developed concordances, stylistics, lexicography and corpora; historians tested databases and quantitative records; archaeologists and art historians worked with structured descriptions and images; teachers explored computer-assisted learning. Mainframe access still tied projects to computing centres, where support staff translated humanities questions into data structures, jobs and output. Generic packages such as concordance programs lowered some costs while embedding assumptions about text and retrieval.

Journals and conferences established review, credit and memory. ALLC launched *Literary and Linguistic Computing* in 1986, after its earlier bulletin and meetings had already supported the community.[^llc] Yet consolidation can be read in two ways. It created durable expertise and archives; it could also separate a specialist community from mainstream disciplinary publication and make service labour less visible than authored scholarship. A history of institutions must therefore ask not only when an organization was founded, but who could participate, whose work counted as research and which infrastructures could be maintained.

## Late 1980s and 1990s: encoding, editions and networks

From the mid-1980s, personal computers allowed some researchers to work without registering at a computing centre and made interactive searching available in several text-analysis programs. Graphical interfaces on systems such as the Macintosh improved the display of non-standard characters, while electronic mail and discussion lists connected a geographically dispersed community. Some collections circulated on CD-ROM—Hockey notes the 1992 *Index Thomisticus* edition—and the World Wide Web later expanded networked publication and access. None of these changes guaranteed compatibility or preservation: the TEI's institutional history identifies proliferating, mutually incompatible systems and weak provisions for longevity and reuse as central problems of the period.[^desktop-media]

The Standard Generalized Markup Language (SGML) became an ISO standard in October 1986. SGML is a metalanguage: it provides rules for defining descriptive markup systems rather than prescribing the visual appearance of one document.[^sgml] This distinction matters for **scholarly encoding**, the interpretive practice of representing structures and features—such as divisions, speakers, deletions, names or variant readings—so that they can be processed and documented. Encoding does not merely copy a text; it makes a model of it.

The Text Encoding Initiative (TEI) was established in 1987 after a meeting at Vassar College, sponsored by ACH and funded by the US National Endowment for the Humanities. ACH, ALLC and the Association for Computational Linguistics organized the work. More than fifty scholars were directly involved by the end of 1989, the P1 draft appeared in June 1990, and the first official Guidelines, P3, in May 1994.[^tei-history] Nearly two hundred people ultimately contributed to the core development effort. TEI therefore exemplifies standards as scholarly and social infrastructure: negotiated classifications, documentation, governance, training and continued maintenance, not a neutral technical decree. Its later consortium charter committed the Guidelines and schemas to open use and international, interdisciplinary participation.[^tei-charter]

The web did not simply replace CD-ROMs or print editions. Media coexisted, and publication on a network did not guarantee preservation, accessibility or analytical depth. The 1990s widened audiences and objects of study while leaving familiar questions—variant texts, documentation, interoperability and sustainability—unresolved.

## The 2000s: from humanities computing to digital humanities

The 2004 *Companion to Digital Humanities* is a useful marker because its title and contents register both continuity and expansion. Its editors traced the volume to text-focused humanities computing but presented a field extending across disciplines, media, digital objects and critical reflection.[^companion] Kirschenbaum documents that *digital humanities* emerged from title negotiations begun in 2001: *humanities computing* was familiar, while *digitized humanities* sounded too narrowly like conversion. This episode helped institutionalize the newer phrase; it did not instantaneously coin a universally accepted field or abolish the older term.[^naming]

The shift also coincided with organizational change. ALLC and ACH began formal work toward an umbrella alliance at their 2002 conference; governance arrangements were approved in 2005, and the 2006 joint conference was the first formally designated “Digital Humanities.”[^adho] The Alliance of Digital Humanities Organizations (ADHO) enabled shared conference, publication and administrative infrastructures and later incorporated more constituent organizations. Public history, digital libraries, cultural heritage, born-digital scholarship, design and collaborative project work became more prominent alongside text analysis and encoding.

Different interpretations remain defensible. One treats the new name as a broader public and critical orientation; another sees strategic branding around funding and institutional visibility; a third stresses continuity in people, methods and organizations. Evidence from language use suggests a gradual overlap, not a clean succession.[^oral-history] Terminology must therefore be tied to speaker, place and date.

## The 2010s to the present: an expanded and contested field

Mass digitization and born-digital collections supported analysis at scales difficult to imagine in the mainframe era. GIS and spatial humanities, network analysis, cultural analytics, computational imaging, three-dimensional modelling and machine learning joined established work in corpora, editions and archives. The “expanded field” described by Klein and Gold included activism, pedagogy, public work and digital creation as well as tools and quantitative analysis.[^expanded-field] Expansion produced opportunity, not consensus.

Critics asked whether tool-building was sufficiently connected to cultural criticism, and how race, gender, class, colonialism and political economy shaped collections, categories and infrastructures. Liu argued that critical attention to data and metadata should extend to the social, economic and political systems in which they operate.[^cultural-critique] Global digital-humanities scholarship in turn challenged the treatment of Anglophone, well-funded institutions as a universal model. Unequal access to digitized collections, reliable networks, language technologies, training and long-term hosting changes which questions can be asked and whose work becomes visible. Open scholarship can reduce some barriers, but “open” data may conflict with copyright, privacy, community authority or culturally specific protocols.[^infrastructure]

Artificial intelligence is part of this contested present, not the endpoint of a progress story. Machine learning and generative systems can assist transcription, retrieval, description and pattern detection, while reproducing errors and harmful categories from collections and training data. Work with visual archives shows both the potential for discovery and the risks of amplified bias, uncertain consent and decontextualized sensitive material.[^ai-archives] The historical lesson is to keep people, provenance and maintenance in view: a model's output depends on earlier selection, digitization, metadata and labour.

There is no settled final period. Future histories may organize the present around environmental cost, platform dependence, Indigenous data governance, multilingual infrastructure or forms of scholarship not currently recognized by dominant journals. A responsible contemporary account stays revisable.

## A checked timeline of selected milestones

The timeline is selective, not a list of inventions. Each milestone has been checked against the cited institutional, primary or peer-reviewed source.

| Date | Milestone | What it establishes—and what it does not |
| --- | --- | --- |
| 1946 / 1949 | Busa conceived the *Index Thomisticus* project during the 1940s and secured IBM collaboration in 1949.[^busa] | An important genealogy of machine-assisted textual scholarship, not the birth of every digital-humanities practice. |
| 1966 | *Computers and the Humanities* began publication.[^early-institutions] | A durable publication venue and evidence of a forming community. |
| 1970 | A Cambridge symposium initiated a recurring literary and linguistic computing conference series.[^early-institutions] | A precursor to later joint conferences, not yet an umbrella organization. |
| 1973 | The Association for Literary and Linguistic Computing was founded.[^associations] | Formal professional organization with an initially language-and-literature-centred scope. |
| 1978 | The Association for Computers and the Humanities was founded.[^associations] | A second association with a broader humanities title and North American base. |
| 1986 | ISO published SGML as ISO 8879:1986; ALLC launched *Literary and Linguistic Computing*.[^sgml][^llc] | A general markup standard and a specialist journal—technical and social infrastructure. |
| 1987 | The TEI was established and its foundational meeting held at Vassar College.[^tei-history] | Coordinated, community-based work on interoperable humanities text encoding. |
| 1990 | The TEI released the P1 draft Guidelines in June.[^tei-history] | A public draft in an iterative standardization process. |
| 1994 | The TEI released its first official Guidelines, P3, in May.[^tei-history] | A mature scholarly encoding framework, still subject to revision and extension. |
| 2004 | *A Companion to Digital Humanities* appeared.[^companion] | A prominent consolidation of the newer name and a deliberately broadened field. |
| 2005 | ACH and ALLC approved ADHO governance and conference protocols.[^adho] | The formalization of a shared organizational infrastructure begun in 2002. |
| 2006 | The joint conference was first formally designated “Digital Humanities.”[^adho] | Institutional uptake of the name, not proof that older terminology vanished. |
| 2012 | ALLC adopted the name European Association for Digital Humanities (EADH).[^associations] | Acknowledgment of expanded scope in the association's own institutional history. |

## Worked example: one question in three historical formations

Consider the question: **How did Slovene newspapers describe migration, and how did that language change over time?** The question is stable enough to compare, but the available evidence and scholarly object change.

**A humanities-computing project around 1965.** Researchers would select a small, deliberately bounded set of articles, key the text onto cards, devise codes for publication and date, and run batch jobs producing a concordance and frequency lists. A linguist or historian would work with operators, programmers and a computing centre. Checks would include double-keying or verification, documented spelling decisions and inspection of concordance lines. The output might be printed tables supporting a close historical argument. Cost, character encoding and access to the mainframe would strongly limit the corpus. Calling the result “objective” would hide both sampling and clerical labour.

**A networked edition or corpus around 1995.** Researchers could transcribe or OCR a larger sample, describe articles with SGML or TEI, distribute data on CD-ROM and publish an interface on the web. Markup could distinguish headlines, quotations, named people and editorial metadata; queries could compare decades or newspapers. Checks would include schema validation, comparison against page images, documentation of OCR error and tests across browsers or retrieval systems. The encoding would make a reusable scholarly resource, but it would also formalize one interpretation of article structure. Copyright and format obsolescence would affect access and preservation.

**A digital-humanities project today.** Researchers might assemble a much larger licensed corpus, measure OCR quality by period, record missing newspapers, and combine close reading with collocations, classification, named-entity recognition, maps or networks. Machine learning or a language model could propose labels, but a stratified human-coded sample would be needed to test error across dates, genres and social groups. The team would publish provenance, code, evaluation results and permitted data, while documenting privacy, copyright and representational harms. It would also ask whose archives were digitized, whether Slovene tools perform consistently on historical language, who maintains the corpus and whether computational expense is justified.

The comparison does not show steady technical improvement. Each formation enables some questions and suppresses others. The historian's task is to connect an output to the institutions, representations and labour that made it possible.

## Practice

Choose one milestone from the timeline and prepare a two-page source audit.

1. Formulate a claim no broader than the evidence requires.
2. Locate one primary or official institutional source and one peer-reviewed historical account.
3. Record the exact date, names used at the time, stable URL or DOI, and access date.
4. Compare what the sources agree on, what they phrase differently and what neither can establish.
5. Identify at least one form of technical, clerical, administrative or maintenance labour involved.
6. Rewrite the claim with a footnote and a one-sentence uncertainty statement.

**Output:** the claim, a 200-word comparison of sources, full references and the uncertainty statement. **Check:** another reader must be able to follow every citation and reproduce your conclusion without using an unsourced summary. **Failure mode:** if sources disagree, do not average their dates; explain which event each date describes.

## Reflection

- Which history becomes dominant if the archive contains published articles but not project correspondence, code, employment records or maintenance logs?
- When does a new name indicate intellectual change, and when does it perform institutional or funding work?
- How would a genealogy centred on Slovene language resources, libraries or cultural institutions alter this chapter's periodization?
- What obligations follow when open access conflicts with privacy, copyright or a community's authority over cultural data?

## Summary

Digital humanities has no neutral point of origin. Pre-electronic indexing and quantitative work are relevant precursors, but they should not be renamed retrospectively. Mid-century humanities computing joined humanities questions to punched-card and mainframe systems; its achievements depended on teams and infrastructures, including labour later omitted from founder-centred accounts. Associations, journals, shared software and centres consolidated a professional community. Personal computers, SGML, TEI and networks changed how scholars represented, exchanged and published cultural evidence. The newer name *digital humanities* gained institutional force in the 2000s while older terminology and practices continued.

Since the 2010s, a wider field has incorporated new media, methods, publics and critical traditions. Global, feminist, anti-racist, infrastructural and open-scholarship debates have shown that access, standards and computation distribute power. AI renews rather than resolves these questions. Historical understanding therefore requires plural genealogies, individually checked claims and explicit uncertainty.

## Further reading and references

- Alliance of Digital Humanities Organizations. “[About](https://adho.org/about/).” *Alliance of Digital Humanities Organizations* website; see “History” for the 2002–2006 organizational milestones. Accessed July 22, 2026.
- Busa, Roberto A. “[Foreword: Perspectives on the Digital Humanities](https://companions.digitalhumanities.org/DH/content/9781405103213_foreword.html).” In *A Companion to Digital Humanities*, edited by Susan Schreibman, Ray Siemens and John Unsworth. Blackwell, 2004. *A Companion to Digital Humanities* online edition, presented by the Alliance of Digital Humanities Organizations. Accessed July 22, 2026.
- European Association for Digital Humanities. “[About](https://eadh.org/about).” *EADH: The European Association for Digital Humanities* website. Accessed July 22, 2026.
- Fiormonte, Domenico, Sukanta Chaudhuri, and Paola Ricaurte, eds. “[Introduction](https://dhdebates.gc.cuny.edu/read/global-debates-in-the-digital-humanities/section/e8110c52-f084-44d2-a29f-1ef4525ad1fe).” In *Global Debates in the Digital Humanities*. University of Minnesota Press, 2022. *Debates in the Digital Humanities* website. Accessed July 22, 2026.
- Hockey, Susan. “[The History of Humanities Computing](https://companions.digitalhumanities.org/DH/content/9781405103213_chapter_1.html).” In *A Companion to Digital Humanities*, edited by Susan Schreibman, Ray Siemens and John Unsworth. Blackwell, 2004. *A Companion to Digital Humanities* online edition, presented by the Alliance of Digital Humanities Organizations. Accessed July 22, 2026. DOI: [10.1002/9780470999875.ch1](https://doi.org/10.1002/9780470999875.ch1).
- International Organization for Standardization. “[ISO 8879:1986: Standard Generalized Markup Language (SGML)](https://www.iso.org/standard/16387.html).” ISO website. Published October 1986. Accessed July 22, 2026.
- Jaillant, Lise. “[Introduction to the Special Issue: Using Visual AI Applied to Digital Archives](https://dhq.digitalhumanities.org/vol/18/2/000752/000752.html).” *Digital Humanities Quarterly* 18, no. 2 (2024). *Digital Humanities Quarterly* website. Accessed July 22, 2026.
- Kirschenbaum, Matthew G. “[What Is Digital Humanities and What’s It Doing in English Departments?](https://doi.org/10.5749/minnesota/9780816677948.003.0001).” In *Debates in the Digital Humanities*, edited by Matthew K. Gold, 3–11. University of Minnesota Press, 2012. Originally published in *ADE Bulletin* 150 (2010): 55–61. DOI: `10.5749/minnesota/9780816677948.003.0001`.
- Klein, Lauren F., and Matthew K. Gold. “[Digital Humanities: The Expanded Field](https://dhdebates.gc.cuny.edu/read/untitled/section/14b686b2-bdda-417f-b603-96ae8fbbfd0f).” Introduction to *Debates in the Digital Humanities 2016*. University of Minnesota Press, 2016. *Debates in the Digital Humanities* website. Accessed July 22, 2026.
- Lieb, Irwin C. “[The ACLS Program for Computer Studies in the Humanities: Notes on Computers and the Humanities](https://doi.org/10.1007/BF00188012).” *Computers and the Humanities* 1 (1966): 7–11. DOI: `10.1007/BF00188012`.
- Liu, Alan. “[Where Is Cultural Criticism in the Digital Humanities?](https://dhdebates.gc.cuny.edu/read/untitled-88c11800-9446-469b-a3be-3fdb36bfbd1e/section/896742e7-5218-42c5-89b0-0c3c75682a2f).” In *Debates in the Digital Humanities*, edited by Matthew K. Gold, 490–509. University of Minnesota Press, 2012. *Debates in the Digital Humanities* website. Accessed July 22, 2026.
- Nyhan, Julianne, and Andrew Flinn. [*Computation and the Humanities: Towards an Oral History of Digital Humanities*](https://doi.org/10.1007/978-3-319-20170-2). Springer, 2016. DOI: `10.1007/978-3-319-20170-2`.
- Pawlicka-Deger, Urszula. “[Infrastructuring Digital Humanities: On Relational Infrastructure and Global Reconfiguration of the Field](https://doi.org/10.1093/llc/fqab086).” *Digital Scholarship in the Humanities* 37, no. 2 (2022): 534–550. DOI: `10.1093/llc/fqab086`.
- Schreibman, Susan, Ray Siemens, and John Unsworth. “[The Digital Humanities and Humanities Computing: An Introduction](https://companions.digitalhumanities.org/DH/content/9781405103213_intro.html).” In *A Companion to Digital Humanities*. Blackwell, 2004. *A Companion to Digital Humanities* online edition, presented by the Alliance of Digital Humanities Organizations. Accessed July 22, 2026. Book DOI: [10.1002/9780470999875](https://doi.org/10.1002/9780470999875).
- Sula, Chris Alen, and Heather V. Hill. “[The Early History of Digital Humanities: An Analysis of Computers and the Humanities (1966–2004) and Literary and Linguistic Computing (1986–2004)](https://doi.org/10.1093/llc/fqz072).” *Digital Scholarship in the Humanities* 34, supplement 1 (2019): i190–i206. DOI: `10.1093/llc/fqz072`.
- Terras, Melissa, and Julianne Nyhan. “[Father Busa’s Female Punch Card Operatives](https://dhdebates.gc.cuny.edu/read/untitled/section/1e57217b-f262-4f25-806b-4fcf1548beb5).” In *Debates in the Digital Humanities 2016*, edited by Matthew K. Gold and Lauren F. Klein, 60–65. University of Minnesota Press, 2016. *Debates in the Digital Humanities* website. Accessed July 22, 2026.
- Text Encoding Initiative. “[Charter](https://old.tei-c.org/about/charter/).” Final draft, 28 November 2000. *TEI: Text Encoding Initiative* website. Accessed July 22, 2026.
- Text Encoding Initiative. “[History](https://tei-c.org/about/history/).” Institutional history and release chronology. *TEI: Text Encoding Initiative* website. Accessed July 22, 2026.
- Underwood, Ted. “[A Genealogy of Distant Reading](https://dhq.digitalhumanities.org/vol/11/2/000317/000317.html).” *Digital Humanities Quarterly* 11, no. 2 (2017). *Digital Humanities Quarterly* website. Accessed July 22, 2026.
- Vanhoutte, Edward. “[The Journal is dead, long live The Journal!](https://academic.oup.com/dsh/pages/dsh_name_change).” *Digital Scholarship in the Humanities*. Oxford Academic journal name-change/editorial page. Undated. Accessed July 22, 2026.

[^periodization]: Hockey, “The History of Humanities Computing,” introduction and section headings. Her chronological frame is influential but explicitly selective.
[^journals]: Sula and Hill, “The Early History of Digital Humanities,” especially their analysis of 1,334 articles in *Computers and the Humanities* and *Literary and Linguistic Computing*.
[^oral-history]: Nyhan and Flinn, *Computation and the Humanities*, especially the introduction on incomplete archives, oral testimony and multiple kinds of work. The authors present the transition in chronological terms for convenience while warning that other factors matter.
[^precursors]: Hockey, “The History of Humanities Computing,” on pre-computer quantitative work; Underwood, “A Genealogy of Distant Reading,” on the distinct social-scientific genealogy of large-scale literary study.
[^busa]: Busa, “Foreword,” recalls seeking machines between 1941 and 1946 and finding IBM support in 1949. Hockey uses 1949 as the beginning of the implemented project; Sula and Hill discuss 1946 as the date of Busa's plans. The dates describe different events.
[^hockey-history]: Hockey, “The History of Humanities Computing,” on the *Index Thomisticus*, lemmatization, punched cards and continuing human decisions.
[^busa-labour]: Terras and Nyhan, “Father Busa’s Female Punch Card Operatives”; Nyhan and Flinn, *Computation and the Humanities*, introduction. The recovered evidence concerns the 1954–1967 training school and shows why a single-author account is inadequate.
[^material-history]: Hockey, “The History of Humanities Computing,” section “Beginnings: 1949 to early 1970s,” describes paper tape, eighty-character punched cards, batch processing, character-set workarounds, serial magnetic-tape storage and fixed-format card layouts. Her survey documents prominent text- and data-processing practices, not every project in the period.
[^early-institutions]: Hockey, “The History of Humanities Computing,” dates *Computers and the Humanities* to 1966 and the Cambridge symposium to March 1970. The first volume of the journal is also independently recorded by Springer.
[^associations]: EADH, “About,” dates the founding of ALLC to 1973 and its adoption of the EADH name to 2012; ADHO, “About,” independently dates ACH to 1978.
[^llc]: Hockey, “The History of Humanities Computing,” and the Oxford University Press history of *Digital Scholarship in the Humanities* identify 1986 as the first year of *Literary and Linguistic Computing*.
[^desktop-media]: Hockey, “The History of Humanities Computing,” sections “Beginnings: 1949 to early 1970s,” “New Developments: Mid-1980s to Early 1990s” and “The Era of the Internet,” on the 1992 *Index Thomisticus* CD-ROM, personal computers, interactive searching, character display, electronic mail and web publication; TEI, “History,” section “Origins of the TEI,” on mutually incompatible systems, preservation barriers and weak provisions for longevity and reuse. Hockey's period boundaries are not universally accepted divisions.
[^sgml]: ISO's catalogue records ISO 8879:1986, edition 1, with publication in October 1986. The TEI history explains why SGML's descriptive, system-independent approach mattered to humanities projects.
[^tei-history]: TEI, “History,” documents the November 1987 Vassar meeting, sponsoring organizations, participant counts and P1/P3 release dates.
[^tei-charter]: TEI, “Charter,” final draft dated 28 November 2000, sets out free use, open participation and international and interdisciplinary representation.
[^companion]: Schreibman, Siemens and Unsworth, “The Digital Humanities and Humanities Computing: An Introduction”; Wiley's catalogue dates the print volume to 1 January 2004 and records book DOI `10.1002/9780470999875`.
[^naming]: Kirschenbaum, “What Is Digital Humanities and What’s It Doing in English Departments?” The account reports a 2001 title discussion and treats the name as socially and institutionally consequential, not as a complete definition.
[^adho]: ADHO, “About,” dates the formal effort to 2002, the steering committee to 2004, approved protocols to 2005 and the first formally designated “Digital Humanities” conference to 2006.
[^expanded-field]: Klein and Gold, “Digital Humanities: The Expanded Field.” Their “expanded field” is an editorial interpretation of heterogeneous practices, not a universally agreed boundary.
[^cultural-critique]: Liu, “Where Is Cultural Criticism in the Digital Humanities?” The chapter is a critical intervention rather than a neutral description of every project.
[^infrastructure]: Pawlicka-Deger, “Infrastructuring Digital Humanities”; the introduction to *Global Debates in the Digital Humanities*. Both stress situated, unequal and multilingual infrastructures; the latter also records continuing Anglophone overrepresentation.
[^ai-archives]: Jaillant, “Introduction to the Special Issue,” on computer vision for digitized archives, amplified collection bias, consent, sensitive material and the need for human oversight.

---

## From question to method

## Learning outcomes

After this chapter, you should be able to:

- turn a broad humanities interest into an answerable research question;
- define units of analysis, variables, comparisons and baselines;
- match methods to claims rather than to available software;
- design manual validation and error analysis;
- distinguish exploratory findings from confirmatory evidence.

## Before you begin

Write down a question you would ask even if no digital tool existed. Then underline the nouns and verbs. The nouns often point to objects and units; the verbs often reveal the kind of comparison or explanation the project requires.

## A question is not yet a method

Questions such as “How is identity represented in literature?” or “What emotions appear in political discourse?” are intellectually meaningful but computationally underspecified. A computer cannot act on *identity*, *representation* or *emotion* until the project decides what observable evidence will stand for those concepts.

**Operationalization** is the process of connecting a concept to observable, recordable and contestable indicators. It should not be hidden as a technical detail. Operationalization is part of the argument.

For example, “visibility of women in a newspaper” might be represented by:

- the proportion of named people recognized as women;
- the number of quotations attributed to women;
- the roles in which women are mentioned;
- article topics where women appear;
- prominence in headlines or opening paragraphs.

Each indicator answers a different question. None is a complete measure of visibility.

## Define the unit of analysis

A project needs a clear unit: document, page, article, paragraph, sentence, token, person, place, event, image or relation. The choice affects both statistics and interpretation.

If sentiment is calculated per sentence, one article may contribute dozens of observations. Treating those sentences as independent can exaggerate certainty. If a place is counted every time it appears, a travel narrative may dominate a corpus. If authors are compared by document, unequal document lengths may distort frequency measures.

Write the unit into the research question whenever possible:

> How does the frequency and context of migration-related terms differ **between editorials** in two newspaper periods?

## Comparisons and baselines

A pattern becomes meaningful through comparison. Ask “compared with what?” before running a method.

Useful baselines include:

- another period, genre, author, institution or region;
- the rest of the corpus;
- a random or majority-class prediction;
- a simple frequency method before a complex model;
- human agreement before machine accuracy;
- shuffled data to test whether structure exceeds chance.

A sophisticated model that barely beats a simple baseline is not a strong result. A simple method that answers the question transparently may be preferable.

## Exploratory and confirmatory work

Exploratory analysis looks for patterns and generates hypotheses. It is appropriate when categories or relationships are not yet known. Confirmatory analysis tests a pre-specified expectation with data and evaluation criteria chosen in advance.

Digital-humanities projects often move between the two. The danger is to explore many possibilities and then present the most attractive pattern as if it had been predicted. Keep an analysis log. Record when a category, threshold, corpus boundary or visualization changed and why.

## Validation is designed, not appended

Validation should be planned before the full analysis. Depending on the method, it can include:

- manually checking a random sample;
- oversampling rare or high-risk cases;
- calculating precision, recall or agreement;
- comparing two annotators and resolving disagreement;
- checking whether results survive alternative preprocessing;
- reading examples from both the centre and the edges of a distribution;
- testing whether a result is driven by one source, period or author.

Accuracy alone is rarely enough. A model with 90% accuracy may fail almost completely on the category that matters most. Error analysis asks which errors occur, for whom, in which genres and with what interpretive consequence.

## Triangulation

A strong project often combines methods that fail differently. Frequencies show scale but not meaning. Concordances restore context but are laborious. A topic model groups co-occurring terms but needs interpretation. Interviews may explain institutional practice but not historical prevalence.

Triangulation does not mean that every method must agree. Disagreement can be analytically valuable when it exposes different levels of the object.

## Worked example: emotion in parliamentary debate

Broad question: *How did emotional language change during a political crisis?*

A research design might specify:

- **sources:** official transcripts from six months before and after a defined event;
- **unit:** each speaker turn, preserving speaker and party metadata;
- **concept:** emotion represented through a manual multi-label scheme plus a lexicon baseline;
- **comparison:** pre-event versus post-event, by party and speaker role;
- **validation:** two annotators on a stratified sample, confusion analysis for automatic labels;
- **interpretation:** close reading of high-change categories and attention to quotation, irony and procedural language;
- **claim limit:** language in the transcript, not the private emotional state of speakers.

The last distinction is crucial. Text analysis can measure textual cues and labels; it does not directly read minds.

## Practice

Take a broad question from your field and complete this design card:

| Element | Decision |
|---|---|
| Research question | |
| Corpus or collection | |
| Unit of analysis | |
| Operational indicator(s) | |
| Comparison/baseline | |
| Validation sample | |
| Main confound | |
| Maximum defensible claim | |

## Reflection

- What does your operationalization make visible, and what does it erase?
- Which simpler baseline should a complex method beat?
- What error would most seriously damage the humanities interpretation?

## Summary

A digital method is appropriate only in relation to a research question, evidence model and claim. Operationalization, units, comparisons and validation are intellectual decisions. Good design defines the strongest claim the evidence can support and plans error analysis before scale makes mistakes expensive.

---

## Data, metadata and models

## Learning outcomes

After this chapter, you should be able to:

- distinguish data, metadata and documentation;
- design stable identifiers and a simple tabular data model;
- represent provenance, uncertainty and missingness explicitly;
- recognize when a spreadsheet should become a relational database;
- evaluate whether a schema reflects the research question or merely the available source format.

## Before you begin

Open a table you have used for research. Can you tell, without asking its creator, what one row represents, which columns are required, what blank cells mean, where the values came from and which version you are looking at? If not, the problem is not “messy data” alone; it is missing semantics.

## Data, metadata and documentation

In humanities research, **data** are recorded observations or representations used as evidence. **Metadata** describe the objects, records or processes: title, date, creator, source, language, rights, collection, coordinates, transcription status or annotation version. **Documentation** explains how the data and metadata were produced and how they should be interpreted.

The distinction depends on the question. A publication date may be metadata in a corpus search but become analysed data in a study of publishing history.

A robust project keeps all three layers:

- the source or a stable reference to it;
- structured records used in analysis;
- documentation of transformations and decisions.

## What does one row mean?

The most important table-design question is the **observation unit**. One row should represent one clearly defined thing: one document, person, place, event, sentence, annotation or relationship.

Mixing levels creates errors. A table with one row per author but multiple book titles squeezed into cells cannot answer book-level questions reliably. A table with one row per newspaper issue but article-level topics in comma-separated lists cannot be filtered or counted without ambiguity.

A useful test is to complete the sentence:

> Each row represents exactly one ________.

If several answers are possible, split the data into related tables.

## Identifiers before names

Names are labels, not stable identifiers. People change names; places have historical and multilingual variants; titles are repeated; spelling varies. Assign each entity a stable internal ID such as `person_0042` or `place_0187`, and store names as attributes or aliases.

Identifiers should be:

- unique within the project;
- persistent across revisions;
- free of sensitive meaning where possible;
- never silently recycled;
- mapped to external identifiers such as Wikidata, VIAF or GeoNames when appropriate, without treating external reconciliation as infallible.

## Missing, unknown and not applicable

A blank cell is dangerously ambiguous. It might mean:

- the value is unknown;
- the value was not recorded;
- the field does not apply;
- the source is illegible;
- the value is being withheld;
- the work has not yet been completed.

Choose an explicit policy. In analysis tables, a machine-readable missing value may be appropriate, but preserve a separate status or note when different forms of uncertainty matter historically.

Do not replace unknown values with zero unless zero is a real observed value. “No recorded letters” is not the same as “zero letters were written.”

## Controlled vocabularies and open text

Controlled vocabularies make comparison possible: `novel`, `poetry`, `essay` rather than dozens of spelling variants. But fixed categories can erase ambiguity and impose modern distinctions.

A practical pattern is to keep:

- a controlled field for analysis;
- the original source wording;
- a note or confidence field;
- a vocabulary document defining each category and its revisions.

Categories should be few enough to use consistently and rich enough to support the research question. “Other” is often necessary, but it should be inspected rather than treated as a bin for discomfort.

## Provenance and transformation

Every derived value should be traceable. Record at least:

- source identifier and location;
- date of acquisition;
- method or script used;
- software/model version where relevant;
- person or process responsible;
- manual corrections;
- relationship between raw, cleaned and analysed files.

A common folder structure separates `data/raw`, `data/interim`, `data/processed` and `output`. Raw data should be read-only whenever possible. Corrections belong in a documented transformation or correction table, not in silent overwriting.

## When a spreadsheet stops being enough

A spreadsheet is excellent for inspection and small flat datasets. Consider a relational database when:

- one person has many works and one work has many persons;
- records need stable relationships across tables;
- repeated text values create inconsistency;
- several people edit or query the data;
- integrity rules matter;
- the project needs reusable queries.

The decision is not about prestige. A database is useful when relationships and constraints are part of the evidence.

## Worked example: correspondence data

A correspondence project might use four tables:

- `persons(person_id, preferred_name, birth_year, ...)`
- `letters(letter_id, date_text, date_start, date_end, source_id, ...)`
- `letter_participants(letter_id, person_id, role)`
- `places(place_id, preferred_name, latitude, longitude, ...)`

The participant table allows several senders, recipients, copied persons or uncertain roles without adding columns such as `recipient_2` and `recipient_3`. The date is represented both as the original string and as a computable interval, preserving uncertainty such as “spring 1898.”

## Practice

Take a small humanities collection and create:

1. a data dictionary with field name, definition, type, allowed values and missing-value policy;
2. five example records;
3. a provenance note explaining one transformation;
4. a list of entities that need stable identifiers.

## Reflection

- Which categories come from the historical source, and which come from your research design?
- Could another researcher reconstruct a derived value from your records?
- What does a blank cell mean in each field?

## Summary

Data structure is interpretation made operational. Clear observation units, stable identifiers, explicit missingness, documented vocabularies and provenance make analysis possible without pretending that cultural evidence is cleaner or more certain than it is. Use a database when relationships and constraints matter, not simply because the dataset is “serious.”

---

## Texts, corpora and OCR

## Learning outcomes

After this chapter, you should be able to:

- distinguish document images, OCR text, corrected text, linguistic annotation and metadata;
- design a corpus around a question rather than around convenience;
- assess representativeness, balance and comparability;
- choose a normalization policy appropriate to historical or non-standard language;
- measure OCR quality and explain its effect on later analysis.

## Before you begin

Open a scanned historical page and its OCR transcription. Find five differences. Which errors would prevent search? Which would change a word frequency? Which would mislead a named-entity recognizer? Not every error has the same research cost.

## A digital text has layers

A single document can have several related representations:

1. **image** — the scan or photograph;
2. **layout description** — regions, columns, lines, marginalia;
3. **diplomatic transcription** — a close record of visible characters and structure;
4. **normalized text** — standardized spelling, punctuation or encoding;
5. **linguistic annotation** — tokens, lemmas, part-of-speech tags, entities or syntax;
6. **metadata** — source, date, author, genre, rights and processing history.

These layers should not silently overwrite one another. The image remains evidence when OCR is uncertain. The diplomatic text preserves historical form. A normalized version may support search, but it is an interpretation and should be linked to the original.

## Corpus design begins with inclusion rules

A corpus is a purposive collection of texts, not simply a folder containing many files. Its boundaries must be justified.

Specify:

- target population: what larger body of texts the corpus is intended to represent;
- sampling frame: which materials were actually available for selection;
- inclusion and exclusion criteria;
- time, genre, region, language and authorship coverage;
- unit of sampling and unit of analysis;
- known gaps, duplication and rights restrictions.

A million web pages may be less useful than one thousand well-documented documents if the research requires period, genre or authorship comparisons.

## Representativeness is a claim

No corpus represents “language” or “culture” in the abstract. It represents a defined population under a set of choices. Web corpora overrepresent material that is public, crawlable and search-engine visible. Newspaper archives reflect survival, licensing and digitization priorities. Literary corpora often overrepresent canonical, public-domain works.

Use metadata tables and distribution plots to inspect balance. Count documents and words by year, genre, source, author and other relevant strata. Large word counts do not compensate for a missing category.

## OCR as measurement

Optical character recognition predicts text from images. It is not neutral transcription. Quality depends on print, script, language model, scan resolution, layout, hyphenation, page damage and historical spelling.

Two common measures are:

- **character error rate (CER):** substitutions, insertions and deletions relative to reference characters;
- **word error rate (WER):** the same logic at word level.

A global score can hide unequal failure. Proper names, diacritics, small type, tables or minority-language passages may be much worse than ordinary prose. Evaluate a stratified sample that includes difficult pages and the text features central to the research.

## The downstream cost of OCR errors

OCR affects methods differently:

- full-text search loses recall when target words are misspelled;
- frequency lists fragment one word into many erroneous forms;
- lemmatizers and taggers may fail on corrupted tokens;
- named-entity recognition is especially vulnerable to unusual names;
- topic models may create noise topics around repeated OCR artefacts;
- quotations and editions require much higher fidelity than aggregate trends.

The right correction effort therefore depends on the claim. A rough trend analysis may tolerate errors that a scholarly edition cannot.

## Normalization and historical variation

Normalization can improve comparability but erase evidence. Keep the original and normalized forms separately. Document rules for:

- Unicode and character encoding;
- line-break hyphenation;
- historical characters and diacritics;
- spelling variants;
- punctuation and quotation marks;
- boilerplate, headers and page numbers;
- language mixing and code-switching.

Automatic normalization should be reversible or at least auditable. A correction list with source form, replacement, context and reason is preferable to undocumented search-and-replace.

## Deduplication and document identity

Digital collections often contain duplicates: mirrored web pages, syndicated news, revised editions, OCR exports of the same scan or documents quoted inside other documents. Duplicates can dominate frequencies and falsely increase confidence.

Assign document IDs, calculate exact hashes for identical files and use similarity methods for near-duplicates. Do not delete blindly: duplicated circulation may itself be historically meaningful. Mark relationships such as `duplicate_of`, `reprint_of` or `version_of` and decide which level the analysis needs.

## Worked example: a historical newspaper corpus

A defensible workflow might be:

1. select newspaper titles and years according to the question;
2. record issue-level and article-level metadata;
3. retain page images and OCR separately;
4. sample pages across titles, years and layout types for OCR evaluation;
5. correct high-impact systematic errors;
6. segment articles and preserve links to page coordinates;
7. document missing issues and changes in publication frequency;
8. compare word and document distributions before analysis;
9. keep an error register and cite the corpus release.

## Practice

Create a corpus card for a collection you could realistically build. Include target population, sampling frame, inclusion rules, exclusion rules, metadata fields, expected OCR or extraction errors, duplicate policy and the strongest comparison the corpus can support.

## Reflection

- Which missing texts are invisible because they were never digitized?
- Would normalization remove a feature your interpretation might later need?
- Which OCR errors matter most for your planned method?

## Summary

A text corpus is a documented research instrument. It consists of linked layers, explicit boundaries, metadata and measured transformations. OCR and normalization create useful text but also new uncertainty. Corpus quality is not the number of tokens; it is the fit between selection, representation, error profile and research claim.

---

## Linguistic annotation and CLASSLA

## Learning outcomes

After this chapter, you should be able to:

- distinguish tokenization, lemmatization, part-of-speech tagging, morphology, dependency parsing and named-entity recognition;
- explain why linguistic annotation is a model-based interpretation rather than a neutral fact;
- choose annotation layers that match a humanities research question;
- run and document a basic CLASSLA workflow for Slovene or another supported South Slavic language;
- validate automatic output with a task-specific sample and error analysis.

## Before you begin

Take the sentence *Zala je v Novi Gorici predstavila novo Zalo.* Is *Zala* a person, a product, a place or something else? What evidence would a human use? An annotator has to make related decisions from form, context and patterns learned from data.

## Annotation creates analytical layers

Raw text contains characters and spacing. Most computational methods first create more explicit units:

- **tokens** divide running text into words, punctuation marks or other units;
- **sentences** establish boundaries for local context;
- **lemmas** group inflected forms under a dictionary-like base form;
- **part-of-speech and morphological tags** describe grammatical category and features;
- **dependency relations** represent syntactic links between words;
- **named entities** identify spans such as people, organizations, locations or dates.

These layers enable questions that surface forms alone cannot answer. Lemmas support comparisons across inflection. Morphological tags help examine case, number or tense. Entities can connect texts to databases and maps. Dependency relations can approximate who acts upon whom.

## Every annotation is a claim

Automatic annotation is produced by rules or statistical models trained on previously annotated examples. The output therefore reflects:

- the annotation scheme used in training data;
- the genres, periods and varieties represented there;
- tokenization and normalization decisions;
- model architecture and software version;
- ambiguities that the available context cannot resolve.

A tag is not a discovered property in the same sense as a page number. It is a prediction under a particular representation. This distinction matters most when the research claim depends on a small category, unusual language, historical spelling, dialect, poetry or named entities absent from training data.

## CLASSLA in a South Slavic context

CLASSLA provides linguistic processing pipelines and resources for Slovene and several other South Slavic languages. A typical pipeline can tokenize text, split sentences, assign lemmas and morphosyntactic descriptions, parse dependencies and recognize named entities, depending on language and model availability.

The practical advantage is not merely convenience. Using a documented regional infrastructure makes it easier to cite models, compare languages and understand tag sets. The methodological obligation remains the same: record the language, model or package version, processors used, input preparation and date of processing.

## Choose only the layers you need

More annotation is not automatically better. Each layer introduces computation, storage and possible error.

For a study of lexical change, tokens, lemmas and metadata may be enough. A study of grammatical constructions may need morphology and dependencies. A map of institutions requires named entities plus entity resolution. Running every processor because it is available can make a workflow slower and harder to audit without improving the argument.

Start with the research variable. Ask what observable feature is required, which annotation approximates it, and how errors in that layer would change the result.

## From output to a tidy table

A useful annotation table commonly contains one row per token and fields such as:

| document_id | sentence_id | token_id | form | lemma | upos | feats | head | deprel |
|---|---:|---:|---|---|---|---|---:|---|
| d001 | 1 | 1 | Raziskovalke | raziskovalka | NOUN | Case=Nom\|Gender=Fem\|Number=Plur | 2 | nsubj |

Keep document metadata in a separate table linked by `document_id`. Preserve the original text and, where possible, character offsets that map annotations back to it. Exporting only a flattened spreadsheet can destroy sentence structure, multiword tokens or uncertainty.

## Validation must match the research task

A global accuracy reported by a model author is not a validation of your corpus. Draw a sample from your own material and examine the layer your analysis uses.

A defensible procedure is:

1. stratify the sample by genre, period or other likely source of variation;
2. manually annotate or verify the relevant features;
3. compare automatic and reference labels;
4. report precision, recall or agreement where appropriate;
5. inspect recurring error types, not only one aggregate score;
6. estimate whether errors are random or systematically related to the groups being compared.

If a named-entity recognizer misses historical women more often because names are abbreviated differently, a group comparison can be biased even when overall accuracy looks respectable.

## Entity recognition is not entity resolution

Recognizing the string *Ljubljana* as a location does not identify which database record it refers to. Likewise, *J. Novak*, *Janez Novak* and *Novak* may denote one person or several. **Entity resolution** links mentions to stable identities and records uncertainty.

Use identifiers, aliases, temporal information and provenance. Do not force a link when evidence is insufficient. An unresolved mention is better than a confident but false connection.

## Worked example: verbs of speaking in newspapers

Suppose we want to compare reporting verbs across two newspaper periods.

1. Define and sample comparable newspaper material.
2. Preserve article and date metadata.
3. run tokenization, lemmatization, morphology and dependency parsing;
4. identify candidate speech verbs by lemma and construction;
5. manually check a stratified sample, including headlines and quotations;
6. separate true reporting uses from homonyms and parsing errors;
7. normalize counts by corpus size and article distribution;
8. interpret differences alongside editorial and historical context.

The annotation reduces the search space. It does not replace the interpretive distinction between quotation, reported speech, metaphor and formulaic language.

## Practice

Choose one research question and create an annotation plan. Name the required layers, software and language model, input format, output fields, validation sample, expected errors and the point at which a human decision is required.

## Reflection

- Which categories in your material are poorly represented in standard training data?
- Would an error affect all documents equally, or could it distort a comparison?
- Which annotation layers can be omitted without weakening the argument?

## Summary

Linguistic annotation makes textual patterns computable by adding predicted layers such as lemmas, grammatical tags, syntax and entities. CLASSLA offers a strong infrastructure for Slovene and South Slavic material, but its output remains model-dependent. Use only the layers demanded by the question, preserve links to source text, record versions and validate the exact feature on which the interpretation depends.

---

## Text analysis

## Learning outcomes

After this chapter, you should be able to:

- distinguish counts, normalized frequencies, proportions and document frequency;
- use concordances to connect quantitative patterns with textual context;
- explain what keyword and collocation statistics compare;
- design a comparison corpus and avoid common denominator errors;
- combine exploratory computation with close reading and validation.

## Before you begin

A word occurs 300 times in corpus A and 180 times in corpus B. Is it more characteristic of A? You cannot know until you know corpus sizes, document distribution, genre composition and how the word was counted. Numbers become evidence only after the denominator and comparison are defined.

## Counting is a model of relevance

Text analysis often begins with a count, but several counts answer different questions:

- **token frequency** counts every occurrence;
- **document frequency** counts how many documents contain an item;
- **normalized frequency** expresses occurrences per fixed number of tokens;
- **proportion** expresses a category relative to an appropriate total;
- **dispersion** describes how evenly occurrences are distributed.

A word used 100 times in one speech is not equivalent to a word used once in each of 100 speeches. Report both frequency and distribution when concentration matters.

## Concordances reconnect pattern and context

A keyword-in-context concordance places each occurrence in a short window. It is one of the most important bridges between distant and close reading.

Use concordances to:

- identify recurring meanings and constructions;
- separate homographs or irrelevant uses;
- inspect negation, quotation and irony;
- check whether a numerical pattern is generated by boilerplate;
- select passages for deeper reading without pretending they are statistically representative by themselves.

Sort by the words to the left or right, group by metadata and save the query definition. A screenshot of a concordance is not a reproducible result.

## Keywords require a reference

A **keyword** is not merely a frequent word. It is unusually frequent in a target corpus relative to a reference corpus. The result depends on both sides.

Choose a reference corpus that controls the comparison you intend. To examine differences between political parties in the same election, use comparable genres and dates. Comparing one party's speeches with a general web corpus would mix political, genre, medium and period effects.

Statistical measures such as log-likelihood indicate evidence against equal relative frequency; effect-size measures such as log ratio indicate the magnitude and direction of difference. A very large corpus can make tiny, uninteresting differences statistically strong, so inspect both evidence and effect.

## Collocation measures association, not meaning

Collocates are words that co-occur within a defined window or grammatical relation more than expected. Parameters matter:

- node word or lemma;
- window size and direction;
- token or sentence boundaries;
- minimum frequency;
- association measure;
- corpus subdivision and stop-list policy.

Mutual information favours relatively exclusive, sometimes rare pairs. Frequency-based or likelihood measures tend to favour robust common patterns. No score directly proves semantic importance. Concordance inspection is essential.

## Comparability before calculation

Before comparing groups, inspect:

- document counts and lengths;
- genres, authors, dates and publication venues;
- duplicate or syndicated texts;
- OCR and annotation quality;
- whether one author or document dominates;
- missing categories and uneven sampling.

Aggregate corpora can exhibit Simpson's paradox: a trend visible overall may reverse inside genres or time periods. Use metadata strata and document-level summaries rather than treating every token as independent.

## Style and stylometry

Stylometry compares texts through measurable features such as function-word frequencies, character n-grams, sentence lengths or grammatical patterns. It can support questions about authorship, genre, period or translation style.

A sound workflow separates:

- **feature design:** what aspects of writing are represented;
- **distance or model:** how texts are compared;
- **evaluation:** whether the pattern generalizes beyond the sample;
- **interpretation:** what historical or literary process could explain it.

Clusters do not name their own causes. Publication date, OCR quality, editor, genre and text length can create apparent authorial groups.

## From exploration to confirmation

Exploratory analysis is valuable for finding candidate patterns. Problems arise when the same data are used to discover a pattern and then to present it as if it had been independently tested.

Whenever possible:

1. explore on one subset;
2. formulate a clear claim and analysis rule;
3. test it on held-out documents or a new corpus;
4. report failed as well as successful comparisons;
5. archive queries, scripts and intermediate tables.

Humanities research does not need to imitate a clinical trial, but it should distinguish discovery from corroboration.

## Worked example: changing descriptions of migration

A project might compare newspaper language around migration in two periods.

1. Build comparable article sets and document the search strategy.
2. Examine corpus balance and duplicates.
3. calculate normalized lemma frequencies and document frequencies;
4. generate keywords with effect sizes against the other period;
5. inspect concordances for top candidates;
6. calculate collocates for selected terms under fixed parameters;
7. stratify by outlet and article genre;
8. close-read representative and contradictory passages;
9. interpret results in relation to policy events and editorial context.

The output is not “the discourse” in full. It is a documented set of recurring textual contrasts in a defined collection.

## Practice

Select two small text groups. Define a defensible denominator, calculate frequency and document frequency for five items, inspect every occurrence in context, and write one claim that the data support plus one claim they do not support.

## Reflection

- What is the correct unit of analysis: token, sentence, document, author or event?
- Could one document be driving the pattern?
- What reference corpus would isolate the contrast you actually care about?

## Summary

Text analysis turns repeated textual features into structured comparisons, but the calculations inherit every corpus and parameter choice. Counts need denominators, keywords need references, collocations need windows and stylometry needs evaluation. Concordance reading, metadata stratification and independent checking keep quantitative patterns connected to language, documents and interpretation.

---

## Topics, sentiment and emotion

## Learning outcomes

After this chapter, you should be able to:

- distinguish supervised classification, unsupervised clustering and topic modelling;
- explain the difference between sentiment, stance, affect and emotion;
- design an annotation scheme and evaluate agreement;
- interpret topic-model output as an exploratory representation rather than discovered truth;
- validate model output against source texts, metadata and human judgement.

## Before you begin

The sentence *Brilliant—another glorious delay* contains positive words but probably expresses negative evaluation. A model that scores vocabulary without context may fail. Before selecting a tool, decide what exactly the category means and which textual evidence licenses the label.

## Classification starts with an operational definition

A classifier assigns texts or passages to predefined categories. Examples include genre, period, author, stance, sentiment, emotion or relevance. The central research act is not choosing an algorithm; it is translating a concept into observable annotation rules.

A good codebook specifies:

- the unit to label: sentence, paragraph, document or event;
- category definitions and boundaries;
- inclusion and exclusion examples;
- treatment of uncertainty, mixed cases and absence;
- the intended use of the labels;
- known cultural, historical and genre limitations.

If trained annotators cannot apply a category consistently, a model cannot repair the conceptual ambiguity.

## Sentiment is not emotion

**Sentiment analysis** usually predicts evaluative polarity—positive, negative or neutral—toward a target. **Stance** concerns support, opposition or positioning toward a proposition or actor. **Emotion analysis** attempts categories or dimensions such as joy, fear, anger, sadness, arousal or valence. **Affect** may refer more broadly to expressed or evoked intensity.

These are not interchangeable. A historical letter may describe fear without the author being afraid; a tragedy may evoke sadness while containing little negative evaluation; satire may use praise to criticize. State whether the aim is to classify wording, narrator, character, speaker, target or reader response.

## Three common approaches

### Lexicon-based methods

A lexicon maps words to scores or categories. It is transparent and easy to inspect, but context, negation, intensification, metaphor, domain shift and morphology can undermine it. For Slovene, inflection and lemmatization choices matter, and translated lexicons need cultural validation.

### Supervised models

A supervised model learns from labelled examples. Its ceiling is set by label quality and representativeness. Split data by document, author or source where leakage is possible. A random sentence split can make performance look excellent because nearly identical passages occur in both training and test sets.

### Prompted language models

A language model can classify using instructions and examples, but its behaviour can vary with wording, model version and context length. Treat prompts as part of the method, preserve exact inputs and outputs, test stability and do not substitute fluent explanations for evaluation.

## Evaluation beyond accuracy

For imbalanced categories, accuracy can be misleading. Report a confusion matrix and class-specific precision, recall and F1 where appropriate. Compare against simple baselines: majority class, lexicon rule or metadata-only model.

Also ask:

- Are errors concentrated in one genre, period or social group?
- Does the model learn document source rather than the intended concept?
- Are uncertain human cases counted as model failures without acknowledging ambiguity?
- Would the remaining error change the historical or literary conclusion?

## Topic models are lenses

Topic models and related clustering methods reduce a document-term or embedding space into recurring patterns. In a probabilistic topic model, a “topic” is a distribution over words and documents, not a ready-made subject with a natural name.

Results depend on:

- preprocessing and vocabulary;
- unit of analysis and document length;
- number of topics or clusters;
- random initialization and hyperparameters;
- model family, such as LDA, NMF or embedding-based clustering;
- corpus composition and duplicated text.

Topic labels are supplied by researchers after inspecting words and documents. A label should therefore be accompanied by representative documents, negative cases and uncertainty—not merely a word cloud.

## Stability and interpretability

A coherent-looking topic can be unstable across random seeds or minor corpus changes. Run multiple configurations and compare whether the pattern persists. Statistical coherence scores may help select candidates, but they do not replace domain interpretation.

A defensible topic-analysis report includes:

1. corpus and preprocessing decisions;
2. model and parameter settings;
3. selection process for the reported solution;
4. representative and contradictory documents;
5. topic prevalence by relevant metadata with uncertainty;
6. sensitivity to another seed, model or topic count;
7. an account of what the model excludes or conflates.

## Worked example: emotional framing in parliamentary debate

Suppose we study emotional framing around climate policy.

1. Define the target: emotion words used by speakers, attributed emotion, or emotional framing of policy.
2. Sample debates and preserve speaker, party, date and agenda metadata.
3. Develop a codebook on a pilot sample and revise ambiguous categories.
4. Have at least two annotators label a subset and discuss disagreement.
5. Compare a lexicon baseline, a supervised model and a prompted model if feasible.
6. Test by party, period and speech type, not only overall.
7. Read false positives, false negatives and high-confidence cases.
8. Use topic or cluster analysis only as a complementary exploratory view.
9. Present model output as evidence about language in the corpus, not direct access to speakers' inner states.

## Practice

Write a one-page codebook for one category: relevance, sentiment, stance or emotion. Include five positive examples, five exclusions, two uncertain cases, the unit of analysis and the consequences of a false positive and false negative.

## Reflection

- Are you measuring language, an attributed state, or a psychological state?
- Could a model predict the label from source or period without reading the relevant passage?
- Which human disagreements reveal genuine conceptual complexity rather than poor annotation?

## Summary

Classification and topic analysis can organize large text collections, but labels and themes are constructed through operational definitions, data and modelling choices. Sentiment is not emotion, a topic is not an independently existing subject, and fluent model output is not validation. Codebooks, baselines, held-out evaluation, subgroup error analysis, sensitivity checks and close reading turn these methods into defensible humanities evidence.

---

## Databases and SQL

## Learning outcomes

After this chapter, you should be able to:

- distinguish a spreadsheet from a relational database;
- identify entities, attributes, relationships, keys and cardinalities;
- design a normalized schema for a small humanities project;
- write basic SQL queries that filter, join, group and count records;
- represent uncertainty, provenance and changing interpretations explicitly.

## Before you begin

Imagine a table with columns `author_1`, `author_2`, `author_3`, `place_1`, `place_2` and several cells containing comma-separated names. It may look convenient, but how would you reliably ask which authors published in the same place, or correct one person's name everywhere? The structure determines which questions remain possible.

## A database is an argument about the world

A database does more than store facts. Its schema states what kinds of things exist in the project and how they relate. For a literary history project, we might model people, works, editions, publishers, places and events. Choosing *work* and *edition* as separate entities is already an interpretive decision.

Relational modelling asks:

- What is one identifiable thing?
- Which properties belong to it?
- Can one thing have many values of this property?
- Which relationships connect entities?
- What evidence supports each assertion?

The schema should follow research needs while remaining explicit enough to revise.

## Tables, rows, columns and keys

A relational database stores records in tables:

- a **row** represents one record;
- a **column** represents one defined attribute;
- a **primary key** uniquely identifies a row;
- a **foreign key** refers to a row in another table.

Use stable internal identifiers rather than names as keys. Names change, collide and vary in spelling. `person_id = 1042` can remain stable while the database stores several name forms and their sources.

## Relationships and cardinality

Common relationships include:

- one-to-many: one newspaper has many issues;
- many-to-many: many people contribute to many works;
- one-to-one: rare and often a sign that two tables could be combined.

A many-to-many relationship needs a junction table. Instead of columns `author_1`, `author_2` and `author_3`, use a `contribution` table with `person_id`, `work_id`, role, order and evidence. The relationship itself can then carry historically meaningful information.

## Normalization without dogma

Normalization reduces duplication and contradictory updates. A useful basic rule is: one cell, one value; one table, one kind of entity; each fact stored in the place where it belongs.

Do not repeat a publisher address in every edition row. Store the publisher once and link editions to it. Do not store a person's birth year both in the person table and every authorship record.

Yet humanities data are not always tidy. An uncertain date such as “between 1848 and 1851” should not be forced into one exact year. Model earliest date, latest date, display text and certainty separately, or create a date assertion table with evidence.

## Provenance and assertions

A value may be quoted from an archive, inferred by an editor, imported from Wikidata or proposed by a student. Store provenance at the level required by the claim.

For contested information, model **assertions** rather than overwriting one value:

| assertion_id | subject | property | value | source | certainty | contributor |
|---:|---|---|---|---|---|---|
| 81 | person_1042 | birth_place | place_17 | archive_A_52 | probable | dp |

This makes disagreement queryable and preserves the history of editorial decisions.

## SQL as a research language

Structured Query Language expresses questions about tables. A few core patterns go far:

```sql
SELECT title, year
FROM work
WHERE year BETWEEN 1900 AND 1918
ORDER BY year;
```

A join follows relationships:

```sql
SELECT p.preferred_name, COUNT(*) AS works
FROM person AS p
JOIN contribution AS c ON c.person_id = p.person_id
WHERE c.role = 'author'
GROUP BY p.person_id
ORDER BY works DESC;
```

Queries should be saved as project files, not reconstructed manually for each publication. A query is part of the analytical method.

## Integrity and validation

Databases can enforce useful constraints:

- keys must be unique;
- required fields cannot be empty;
- foreign keys must point to existing records;
- categories can be restricted to controlled values;
- dates or numerical ranges can be checked.

Constraints prevent accidental inconsistency, but they cannot decide whether the underlying historical claim is correct. Validation also requires source review, duplicate detection, authority control and documented editorial policy.

## SQLite for small humanities projects

SQLite stores a complete relational database in one portable file and supports standard SQL without a server. It is an excellent step beyond spreadsheets for teaching, prototypes and many research datasets.

Keep alongside it:

- a schema file that can recreate the database;
- import scripts or documented procedures;
- controlled vocabularies;
- data dictionaries and field definitions;
- saved analytical queries;
- versioned exports in open formats such as CSV.

The database file is convenient; the documented process is what makes it reproducible.

## Worked example: correspondence network

To study correspondence, create tables for persons, letters, places and participation. A letter has a date, repository identifier and perhaps uncertainty. A participation table links a person to a letter with a role such as sender, recipient, mentioned person or editor. A place link can specify origin, destination or place mentioned.

This structure supports questions about exchange, mobility and mediation without collapsing every relationship into a single edge. It also makes explicit which relationships come from document metadata and which are extracted from letter text.

## Practice

Design a schema for one project: a bibliography, oral-history archive, literary corpus, cultural-heritage inventory or correspondence collection. Draw entities and relationships, assign keys, identify one many-to-many relationship and show how uncertainty and provenance will be recorded.

## Reflection

- Which categories in your schema are analytical interpretations rather than source facts?
- What information would be lost by exporting the database to one flat table?
- Which query would reveal the strongest weakness in your data coverage?

## Summary

A relational database is a formal, revisable model of entities and relationships. Keys and normalized tables reduce ambiguity; junction tables express many-to-many relations; SQL makes analytical steps explicit. Humanities databases become trustworthy when they also preserve uncertainty, provenance, contested assertions, editorial rules and recreatable structure.

---

## GIS and spatial humanities

## Learning outcomes

After this chapter, you should be able to:

- distinguish a place mention, a place identity and a coordinate;
- explain geocoding, coordinate reference systems, layers and spatial joins;
- design a place table that preserves names, time and uncertainty;
- recognize how digitization, scale and map design shape spatial arguments;
- evaluate a map as an analytical claim rather than as an illustration.

## Before you begin

A nineteenth-century diary says that its author travelled to *St. Peter*. Which place is meant? The answer may depend on language, period, route, administrative boundaries and the writer's habits. Assigning coordinates is not clerical work; it is an interpretation that needs evidence.

## Space is more than latitude and longitude

Humanities sources refer to places through names, descriptions, institutions, regions, routes and imagined geographies. A place can change name, boundary, function and political affiliation. One name may denote several locations; one location may have many names.

Keep separate:

- the **mention** as it appears in the source;
- the **normalized name** used for search or display;
- the **place entity** with a stable project identifier;
- the **geometry** used on a map;
- the **time period** for which the identification applies;
- the **evidence and certainty** supporting the link.

This separation allows a corrected identification without changing the source transcription.

## Gazetteers and geocoding

A **gazetteer** is a structured place-name resource containing identifiers, names, types, coordinates and often historical or administrative information. **Geocoding** links an address or place string to a spatial location.

Commercial or contemporary geocoders are optimized for current addresses. They may silently map historical names to modern centres, choose the most populous place or fail on dialect and multilingual forms. Record the service, date, query string, returned identifier, score and manual decision. Cache results where licences permit so that the project is not dependent on a changing external response.

## Geometry and uncertainty

A point is not always the right representation. A historical region may need a polygon, a journey a line and an uncertain location a set of candidates or an approximate area.

Useful fields include:

| mention_id | place_id | geometry_type | certainty | start_date | end_date | source |
|---|---|---|---|---|---|---|
| m18 | p204 | point | probable | 1849 | 1851 | diary_7_f12 |

Avoid invented precision. A coordinate with six decimal places can imply metre-level certainty even when the source only identifies a valley. Represent uncertainty through ranges, confidence categories, multiple candidates, buffers or qualitative notes—and explain the convention in the legend.

## Coordinate reference systems

Coordinates are interpreted within a **coordinate reference system** (CRS). Geographic coordinates such as WGS 84 use latitude and longitude; projected systems transform the earth onto a plane for particular regions and measurements.

A map can look plausible even when layers use mismatched systems. Record the CRS for every spatial dataset. Reproject intentionally before measuring distance or area, and choose a projection suited to the geographic extent and analytical goal.

## Layers and spatial joins

GIS organizes information in layers: places, boundaries, roads, land use, events, documents or demographic indicators. A **spatial join** links records according to spatial relations such as within, intersects or nearest.

This enables questions such as:

- Which letters originated within a historical border?
- Which archaeological finds lie near a Roman road?
- Which dialect observations fall inside present and historical administrative regions?

But the relation is only as meaningful as the geometries and time alignment. Joining an 1850 event to a 2026 municipal boundary may answer an administrative convenience, not a historical question.

## Maps are arguments

Every map chooses extent, scale, projection, classification, symbols, labels and omissions. Points can hide density; large polygons dominate visual attention; colour bins can exaggerate a threshold; missing data can look like absence.

A scholarly map should state:

- data source and coverage;
- unit of analysis;
- temporal scope;
- spatial resolution and uncertainty;
- transformation and classification rules;
- missing or excluded records;
- whether the map is exploratory, descriptive or inferential.

Do not use a heat map simply because it is visually dramatic. Density estimation introduces bandwidth and edge choices that need interpretation.

## Texts and spatial extraction

To map places mentioned in texts, a workflow typically combines named-entity recognition, manual review, entity resolution and geocoding. Frequency of mention is not presence, residence or importance. A newspaper may mention a capital frequently because it is a political centre; a travel diary may name only unusual stops and omit familiar locations.

Link every mapped point back to the passage and document. This allows readers to inspect whether a location is literal, metaphorical, reported, imagined or uncertain.

## Worked example: literary mobility

Suppose we study movement in a novel and its historical context.

1. Define whether the unit is a mention, scene, journey segment or character presence.
2. Extract candidate place mentions and retain passage identifiers.
3. Resolve names with period-appropriate gazetteers and scholarly sources.
4. Assign geometry and certainty without forcing ambiguous cases.
5. Distinguish narrated, remembered, imagined and referenced places.
6. Build routes only where sequence and movement are supported by the text.
7. compare the literary geography with historical transport or borders cautiously;
8. publish a map with filters, source passages and an uncertainty legend;
9. interpret absences as possible narrative choices, not automatic evidence of irrelevance.

## Practice

Create a ten-row place table from a text or heritage list. Preserve source form, normalized name, identifier, coordinates or geometry, date, certainty, evidence and notes. Map it, then identify three ways in which the map could mislead a reader.

## Reflection

- Does the map represent mentions, events, people, documents or inferred movement?
- Which historical boundary or place-name decision is most contestable?
- What appears empty because your sources or geocoder do not cover it?

## Summary

Spatial humanities turns place evidence into linked, time-aware and interpretable spatial data. A mention is not a coordinate, modern geocoding is not historical identification, and a map is not a neutral window. Gazetteers, stable identifiers, coordinate systems, provenance and explicit uncertainty make spatial visualizations useful as humanities arguments.

---

## Networks and visualization

## Learning outcomes

After this chapter, you should be able to:

- define nodes, edges, direction, weight and bipartite networks;
- distinguish observed relationships from relationships inferred by a construction rule;
- interpret basic centrality and community measures cautiously;
- design a visualization that exposes scale, uncertainty and missing data;
- document the transformations from source records to a graph.

## Before you begin

Two people occur in the same newspaper article. Are they connected? Perhaps they collaborated, opposed one another, were merely listed, or appear in unrelated paragraphs. A network edge is not found automatically in the source. It is created by a rule whose meaning must be defended.

## A network is a data model

A graph contains **nodes** and **edges**. Nodes may represent people, texts, places, institutions or concepts. Edges may represent correspondence, citation, kinship, co-authorship, travel, co-occurrence or another relationship.

Specify whether an edge is:

- directed or undirected;
- weighted or unweighted;
- dated or time-bounded;
- observed directly or inferred;
- positive, negative or typed;
- supported by one or several sources.

Different edge definitions create different networks. The definition belongs in the methods section and ideally in machine-readable data.

## One-mode and bipartite networks

A one-mode network links the same kind of node, such as person to person. A **bipartite** network links two kinds, such as people to organizations or characters to scenes.

Projects often project a bipartite network into a one-mode co-occurrence network: two characters are linked if they appear in the same scene. Projection loses information and can create dense edges around large scenes. Preserve the original bipartite data and state the projection and weighting rule.

## Centrality is question-dependent

Common measures include:

- **degree:** number of immediate connections;
- **weighted degree:** sum of edge weights;
- **betweenness:** how often a node lies on shortest paths;
- **closeness:** distance to other reachable nodes;
- **eigenvector/PageRank-style measures:** connection to already well-connected nodes.

No measure equals “importance” in general. Degree may indicate visibility, opportunity or simply better documentation. Betweenness depends strongly on the assumption that shortest paths model the process. Disconnected and very small networks require special care.

## Communities and clusters

Community-detection algorithms partition networks into groups with dense internal connections. Results depend on algorithm, resolution and random initialization. A community is not automatically a historical faction or literary theme.

Compare multiple resolutions, inspect boundary nodes and relate groups to independent metadata. Report when several plausible partitions exist. A visually tidy modular graph may be produced by the layout even when evidence is weak.

## Time and change

Aggregating decades of relationships into one graph can create connections that never coexisted. Build time slices, interval networks or event-based views when chronology matters.

Ask whether nodes can enter and leave, whether edge weights accumulate, and whether missing years reflect no activity or no surviving data. Animation can be attractive but hard to compare; small multiples or interactive filters often communicate change more clearly.

## Missing data and unequal visibility

Networks are especially sensitive to archival survival. A prolific correspondent may look peripheral because only one archive survives. Famous figures may have better cataloguing and entity resolution. Co-occurrence networks privilege long documents and common names.

Represent coverage and source counts. Consider sensitivity analyses: remove uncertain edges, use alternative thresholds or compare archives. Absence of an edge often means “not observed under this procedure,” not “no relationship existed.”

## Visualization as analytical design

A network plot needs more than colourful nodes. Decisions include layout, node size, edge opacity, labels, filtering and colour categories. Force-directed layouts optimize readability, not geographical or chronological truth; repeated runs can place nodes differently.

Good practice:

- label only when labels serve the question;
- explain every visual encoding;
- avoid scaling node area in a misleading way;
- show isolated nodes when exclusion would hide coverage;
- provide a table or searchable view for exact values;
- preserve accessibility in colour and contrast;
- include provenance and a downloadable edge list.

## Worked example: a literary character network

A defensible workflow might be:

1. Define character identity, aliases and collective characters.
2. Choose an edge rule: shared scene, direct address or reported interaction.
3. Segment the text and preserve passage references.
4. Build a bipartite character-scene table.
5. Project only if the research question requires a character-character graph.
6. Test alternative scene definitions and edge thresholds.
7. compare centrality with narrative point of view and amount of speech;
8. inspect apparently central and surprisingly peripheral characters in the text;
9. publish both the visualization and construction data.

The graph summarizes one relational aspect of the novel. It does not model character depth, thematic importance or reader experience unless those have been operationalized separately.

## Practice

Construct a small network from at least ten source records. Write the edge rule in one sentence, keep an evidence field for every edge, calculate degree, and create two visualizations with different thresholds. Explain which relationships disappear and why.

## Reflection

- What does an edge mean in source terms?
- Which nodes are visible because their records survive or are easier to recognize?
- Would a bipartite representation preserve distinctions hidden by projection?

## Summary

Networks are explicit models of relationships, not transparent pictures of society or literature. Node and edge definitions, projection, time, missing data and algorithms shape every result. Centrality is not generic importance, communities are not self-interpreting groups and layouts are not evidence. Traceable construction rules and source-linked edges make network analysis suitable for humanistic interpretation.

---

## AI, ethics and reproducibility

## Learning outcomes

After this chapter, you should be able to:

- distinguish reproducibility, replicability and transparency;
- document data, code, models, prompts and environments as research materials;
- identify privacy, copyright, representational and labour risks in digital-humanities projects;
- design source-grounded uses of generative AI and verify their outputs;
- create a release package that another person can inspect and rerun.

## Before you begin

A chatbot produces a fluent summary with three convincing quotations. One quotation is slightly altered, one belongs to another author and one does not exist. The problem is not merely that “AI can hallucinate.” The workflow asked a generative system to act as a source of evidence without preserving a verifiable path back to the documents.

## Reproducibility is a design choice

A result is **computationally reproducible** when another person can use the same data, code and environment to obtain the same or acceptably equivalent output. **Replicability** often refers to testing the claim with independently collected data or another implementation. **Transparency** means the relevant decisions, transformations and limitations are available for inspection.

Humanities projects may involve interpretive steps that cannot be reproduced mechanically. Those steps can still be made transparent through codebooks, decision logs, examples and provenance.

## Record the whole chain

A minimal research package should identify:

- source materials and access conditions;
- data selection and exclusion rules;
- scripts, queries and manual transformations;
- software, package and model versions;
- configuration, random seeds and hardware-sensitive steps;
- prompts, system instructions and model identifiers for generative AI;
- intermediate and final outputs;
- validation procedures and known failures;
- contributor roles and licences.

A notebook that runs only on the author's laptop is not reproducible. Neither is a repository that omits private data without explaining how authorized researchers can reconstruct the analysis.

## Environments and versioning

Dependencies change. Pin compatible versions in `requirements.txt`, `environment.yml`, a lockfile or a container definition. Include a small smoke test and expected output. Tag public releases and cite the release rather than the moving `main` branch.

Version data as well as code. A corrected corpus can change counts even when scripts remain identical. Release notes should distinguish content corrections, methodological changes and cosmetic edits.

## Ethical review begins before collection

Ask before acquiring data:

- Were the materials created for public circulation or a limited context?
- Do legal access and ethical permission point in the same direction?
- Could quotation, linking or aggregation expose a person who was obscure in the source context?
- Are there vulnerable communities, minors, health data or family histories?
- Does a platform's interface make data visible while its terms or social norms discourage bulk collection?
- Who bears the work of cleaning, annotation and moderation, and is that labour credited?

“Publicly accessible” is not a complete ethical argument.

## Copyright, licensing and reuse

Separate rights in source materials, annotations, code, documentation and outputs. A corpus may be shareable only as metadata, identifiers, derived features or scripts that authorized users can run locally. Do not assume that an open repository makes every included object openly licensed.

For each component, state:

- rights holder or source;
- licence or legal basis;
- permitted redistribution;
- attribution requirements;
- access restrictions and takedown procedure.

Use the least restrictive licence you can legitimately grant, not one you merely prefer.

## Bias and representational harm

Digital collections overrepresent what was preserved, digitized, catalogued, legible to OCR and available under workable rights. Models add biases from training data, annotation categories and performance differences across languages and communities.

Evaluation should therefore include:

- coverage by relevant group, genre, period and language;
- missingness and survival bias;
- subgroup error rates;
- examples of harmful or stereotyped output;
- consultation where communities are represented or named;
- limits on claims and publication of sensitive details.

A model can be technically accurate on average while reproducing a harmful historical category or failing precisely on minoritized material.

## Source-grounded generative AI

Generative AI is most defensible when it transforms or navigates supplied sources and every important assertion can be checked.

A source-grounded workflow might:

1. retrieve bounded passages from a documented collection;
2. ask the model to summarize or classify only those passages;
3. require passage identifiers and quoted evidence;
4. automatically check that quoted spans exist;
5. have a human verify interpretation and omissions;
6. preserve prompt, model, parameters, retrieved context and output;
7. compare against a non-generative baseline where possible.

Do not let citations generated from memory enter a bibliography unchecked. Treat model confidence language as rhetoric, not calibrated probability.

## Human responsibility and disclosure

A tool cannot accept authorship responsibility, obtain consent or judge whether a publication harms a living person. Name who made final decisions. Disclose AI assistance at the level relevant to readers: ideation, translation, coding, classification, copy-editing or generation.

Disclosure should enable evaluation, not perform ritual confession. “AI was used” is too vague; “Model X, version/date, classified 1,200 paragraphs under codebook Y; two annotators reviewed all low-confidence and a 20% random sample” is useful.

## Worked example: an AI-assisted archive guide

A team uses a language model to draft descriptions of archival folders.

1. Limit inputs to authorized catalogue notes and selected documents.
2. Define required fields and forbidden inferences.
3. Require source identifiers for each claim.
4. Test extraction accuracy on a manually prepared sample.
5. flag names, sensitive information and uncertain dates for review;
6. compare performance across languages and document types;
7. keep the generated description separate from the archival record until approved;
8. record reviewer, date and changes;
9. publish the model-use statement and correction channel.

The system accelerates drafting; archivists remain responsible for description and access decisions.

## Practice

Create a reproducibility and ethics checklist for one project. Include data rights, privacy, selection bias, model versions, random elements, human review, validation, release files, citation and a response plan for errors or takedown requests.

## Reflection

- Which parts of your workflow cannot be shared, and how can they still be documented?
- Who is represented in the data but absent from project decision-making?
- Would the result survive a changed model or unavailable web service?

## Summary

Responsible digital humanities combines technical repeatability with ethical accountability. Preserve the chain from source to output, version code and data, state rights and limits, test performance where harm or bias may concentrate and keep generative AI grounded in verifiable evidence. Reproducibility is not a folder added at the end; it is the architecture of a research process that others can inspect, challenge and improve.

---

## The living open handbook

## Learning outcomes

After this chapter, you should be able to:

- distinguish a living edition from a stable reviewed release;
- cite a versioned digital publication correctly;
- design contribution, review and translation workflows;
- explain how Git, GitHub Pages and an archive serve different publication functions;
- evaluate whether an update requires a patch, minor or major release.

## Before you begin

A printed software tutorial can be obsolete before students open it. A constantly changing website can be impossible to cite or review. The solution is not to choose between permanence and change. It is to give each a defined layer.

## Two editions, one publication

This handbook separates:

1. the **living edition** on the default branch, where corrections, new workflows and translations are developed; and
2. a **stable release**, identified by a version tag, date and archived snapshot.

The living edition supports teaching and maintenance. The stable release is the object of formal review, citation and preservation. Readers can always see which edition they are using.

This model is common in software and data publishing, but it also suits fields whose methods and interfaces change rapidly. The conceptual chapters should change slowly; practical workflows can be updated more frequently.

## Roles of the publication infrastructure

Different components have different jobs:

- **Git repository:** source files, history, issues, review and contributions;
- **GitHub Pages:** readable public web edition;
- **tagged release:** frozen set of files representing an edition;
- **archival repository:** long-term record and persistent identifier;
- **publisher record:** peer review, metadata, cataloguing and institutional recognition;
- **optional PDF snapshot:** offline, deposit and review format, not the editorial master.

No single platform should carry every responsibility. A URL to a branch is not an archive, and a PDF is not a maintainable source.

## Version numbers communicate meaning

A practical semantic scheme is:

- **patch** release, such as 1.0.1: corrections that do not materially change method or learning outcomes;
- **minor** release, such as 1.1.0: new workflows, translations or backward-compatible additions;
- **major** release, such as 2.0.0: substantial reorganization, changed methodological recommendations or a newly reviewed edition.

Every release should include a changelog, citation metadata and a statement of review status. Do not silently rewrite an archived edition.

## Citation and review status

The site should display:

- current version or development status;
- publication and last-updated dates;
- preferred citation;
- DOI or archival identifier when assigned;
- editorial and peer-review statement;
- licences for text, code and data;
- link to the exact source revision.

A reader citing a research claim should cite the stable version used. A classroom may use the living edition and record the commit or semester release.

## Contribution is not unmoderated editing

Openness means that people can propose and inspect changes, not that every change is published automatically. A contribution workflow should require:

1. a defined problem and intended audience;
2. source and rights checks;
3. a reproducible minimal example;
4. expected output and failure modes;
5. editorial and technical review;
6. language review where relevant;
7. disclosure of contributor role and licence agreement;
8. automated checks before merge.

Students can be genuine contributors. Their work should be credited, reviewed and licensed with informed agreement. Assessment and publication decisions must be separated so that students are not coerced into public authorship.

## Bilingual publication is editorial work

A language switch is a technical feature; a bilingual handbook requires editorial equivalence.

Each language version needs:

- idiomatic terminology rather than mechanical word replacement;
- aligned learning outcomes and examples;
- a way to mark missing or outdated translations;
- reviewers competent in the relevant language and field;
- translation provenance and date;
- a policy for changes that affect only one language.

The versions need not be identical sentence by sentence. They should support equivalent learning and make differences visible. The default language may temporarily provide fallback pages, but missing translations must not masquerade as complete coverage.

## Governance prevents the bus-factor problem

A living resource should not depend on one person's memory. Record:

- editor and maintainer roles;
- who can approve content, translation and technical changes;
- review intervals for software-dependent pages;
- labels for tested, outdated or archived workflows;
- correction and takedown procedures;
- succession and repository ownership arrangements;
- how conflicts of interest are handled.

Governance makes openness durable. It also lets a publisher recognize a changing project without assuming that every commit has undergone formal peer review.

## A release workflow

A formal release can follow these steps:

1. declare a content freeze and release candidate;
2. run automated link, structure and code checks;
3. complete scholarly and didactic review of the stable core;
4. resolve required changes and record reviewer approval;
5. complete language and accessibility checks;
6. tag the source and build the web/PDF artifacts;
7. archive the release and mint or register its persistent identifier;
8. publish citation metadata and release notes;
9. reopen the living edition for development.

This preserves both accountability and momentum.

## Worked example: a student contribution

A student proposes a workflow for mapping places in oral-history transcripts.

- The student submits a small anonymized sample, method, output and limitations.
- A peer reproduces the steps.
- An editor reviews privacy, geocoding uncertainty and terminology.
- The contribution is revised and credited.
- It enters the living edition as a reviewed workflow.
- At the next minor release it becomes part of a stable archived edition.

The student's work is real scholarly communication, not disposable homework, while the editorial process protects readers and participants.

## Practice

Take one digital teaching resource and draft its publication architecture. Identify the living source, stable release, archive, citation, editorial roles, contribution route, translation policy and criteria for a major new edition.

## Reflection

- What exactly has been peer reviewed: every page, the core chapters or one release?
- How will a reader know that a software-dependent workflow is still current?
- Who owns and can maintain the project if the original editor leaves?

## Summary

A living handbook can be open and academically citable when development and publication are separated clearly. Git supports history and contribution, a web site supports reading, tagged releases support review, and an archive supports preservation. Versioning, governance, bilingual editorial policy and explicit review status turn continuous change from a weakness into a documented scholarly method.

---

# Part II: Course pathways

## Information Society Literacy

## Purpose

This path is designed for students who need to become confident and critical users of digital information before they become technical specialists. It combines information literacy, data literacy, digital research practice, basic text analysis and responsible use of artificial intelligence.

The course should not be reduced to software menus. Interfaces change. The durable outcome is the ability to define a task, choose an appropriate representation and tool, preserve evidence, check output and communicate limits.

## Prior knowledge

No programming experience is required. Students should be able to use a web browser, create and organize files and prepare a basic written assignment. Every task should be possible with a graphical tool or a carefully scaffolded command where command-line exposure is pedagogically useful.

## Learning outcomes

By the end of the path, students should be able to:

- search for and critically evaluate scholarly and public digital sources;
- organize files, references and small datasets with meaningful structure and metadata;
- distinguish text, image, OCR, annotation and derived data;
- perform and interpret basic corpus searches, frequencies and visualizations;
- assess privacy, copyright, licensing and source provenance;
- use generative AI in a source-grounded and documented way;
- package a small digital research dossier that another student can understand and verify.

## Suggested 14-module sequence

### 1. Digital literacy as critical practice

Read [What is digital humanities?](../chapters/what-is-digital-humanities.md). Map a familiar academic task from source discovery to final submission and identify every point where a platform or format shapes the result.

### 2. Questions, sources and evidence

Read [From question to method](../chapters/research-design.md). Turn a broad topic into one researchable question and list the evidence needed to answer it.

### 3. Files, formats and durable organization

Create a project folder with `data`, `sources`, `notes`, `outputs` and a README. Compare `.docx`, `.pdf`, `.txt`, `.csv` and image files. Practise meaningful file names and a backup rule.

### 4. Search and source evaluation

Build a search strategy using keywords, synonyms, Boolean combinations and source filters. Compare a library catalogue, bibliographic database, institutional repository and general search engine. Record the search rather than only the final links.

### 5. Citations, bibliographic metadata and reference management

Create a small reference library. Correct incomplete metadata, distinguish a stable identifier from a URL and export the bibliography in one agreed style.

### 6. Data and metadata

Read [Data, metadata and models](../chapters/data-metadata-models.md). Convert messy notes into a tidy table. Prepare a data dictionary and mark missing, unknown and not-applicable values differently.

### 7. Spreadsheets without spreadsheet chaos

Use sorting, filtering, formulas and pivot tables on a small cultural dataset. Check for mixed data types, merged cells, duplicate records and formulas that silently exclude rows.

### 8. Documents, OCR and corpus basics

Read [Texts, corpora and OCR](../chapters/texts-corpora-ocr.md). Compare a scan and OCR text, identify high-impact errors and write inclusion rules for a five-document mini-corpus.

### 9. Search, concordance and frequency

Read the opening sections of [Text analysis](../chapters/text-analysis.md). Use a corpus interface or desktop tool to search a word, inspect concordances and compare token frequency with document frequency.

### 10. Visual communication

Create one table and one chart from the same data. State the unit, denominator, source and missing values. Redesign one misleading visualization and explain the correction.

### 11. Places and maps

Read the introductory sections of [GIS and spatial humanities](../chapters/gis-spatial-humanities.md). Build a small place table with source forms, normalized names, coordinates and uncertainty, then produce a basic map.

### 12. Generative AI with evidence

Read [AI, ethics and reproducibility](../chapters/ai-ethics-reproducibility.md). Ask a model to summarize supplied sources, require passage identifiers and verify every factual claim and quotation. Record the model, date, prompt and corrections.

### 13. Rights, privacy and responsible publication

Apply the [ethics checklist](../resources/ethics-checklist.md) to the final project. Decide what may be public, restricted, anonymized or omitted and justify the licence for each component.

### 14. Reproducible digital dossier

Exchange projects. Another student must locate the sources, understand the data, repeat one operation and identify the strongest limitation without oral explanation from the author.

## Assessment model

A balanced assessment can combine:

- **weekly practice portfolio (30%)** — short source, data and tool tasks;
- **critical audit (20%)** — analysis of a misleading dataset, visualization or AI output;
- **digital research dossier (40%)** — final project with question, evidence, data, output and documentation;
- **peer reproducibility review (10%)** — structured review of another student's dossier.

Assessment should reward documented judgement, not merely successful clicking. A student who identifies a method's failure honestly may demonstrate more competence than one who produces a polished but unverified output.

## Final project specification

The final dossier should contain:

1. a focused question and intended audience;
2. a search and source-selection log;
3. a five-to-fifty-record dataset or small text collection;
4. metadata and a data dictionary;
5. one analytical operation, such as filtering, counting, concordance, mapping or comparison;
6. one table or visualization with a complete caption;
7. a 700–1,000 word interpretation;
8. an ethics, rights and limitations statement;
9. a README that lets a peer reproduce one result;
10. a disclosure of any AI assistance.

## Course versioning

At the start of the semester, record the handbook release in the syllabus, for example `Digital Humanities Handbook 1.0.0`. Corrections may be consulted in the living edition, but graded instructions should link to a stable release or commit so that requirements do not shift during the course.

---

## Digital Slovenian Studies

## Purpose

This path trains students to design, execute and critically interpret computational research on Slovene language, literature and cultural material. It is technically more demanding than Information Society Literacy: students work with structured data, Python environments, CLASSLA, relational databases and reproducible project repositories.

Technical competence is not the final goal. Every operation must remain connected to a Slovenian-studies question, source criticism and the linguistic, literary or historical consequences of modelling choices.

## Prior knowledge

Students should be comfortable with files, CSV tables, basic corpus concepts, references and critical source evaluation. No advanced programming is assumed, but the course uses Python 3.12, the command line, virtual environments and short scripts. A preparatory clinic should be available for students without this background.

## Learning outcomes

By the end of the path, students should be able to:

- formulate a digital Slovenian-studies question and an auditable research design;
- build and document a small Slovene or South Slavic corpus;
- use CLASSLA and interpret annotation layers and errors;
- calculate and validate corpus, stylistic, thematic and emotion-related features;
- model humanities entities and relationships in SQLite and SQL;
- resolve and map place evidence with uncertainty;
- construct and critique a source-linked network;
- release data, code and interpretation as a citable, reproducible project.

## Suggested 14-module sequence

### 1. Digital Slovenian studies as a field

Read [What is digital humanities?](../chapters/what-is-digital-humanities.md) and [From question to method](../chapters/research-design.md). Reformulate one traditional Slovenian-studies question so that data, unit of analysis, comparison and limits are explicit.

### 2. Reproducible Python workspace

Create a Python 3.12 virtual environment, install packages, run a script and initialize a repository. Complete the relevant [Python and NLP workflows](../workflows/nlp/index.md). Commit a README and environment specification.

### 3. Text formats, encoding and corpus design

Read [Texts, corpora and OCR](../chapters/texts-corpora-ocr.md). Inspect plain text, CSV, JSON and TEI/XML examples. Design a corpus card with sampling rules, document IDs, metadata and rights.

### 4. Collection, OCR, cleaning and deduplication

Acquire or prepare a small authorized corpus. Preserve raw and processed layers, measure an OCR or extraction sample, remove boilerplate and flag exact or near duplicates without losing provenance.

### 5. CLASSLA annotation

Read [Linguistic annotation and CLASSLA](../chapters/linguistic-annotation-classla.md). Install/test CLASSLA, annotate text and export token-level results. Record model and software versions and inspect errors in Slovene names, non-standard forms or historical language.

### 6. Concordance, frequency, keywords and collocation

Read [Text analysis](../chapters/text-analysis.md). Compare two defensible subcorpora, normalize counts, calculate document frequency and inspect concordances. Report at least one effect size and one corpus-composition limitation.

### 7. Style and authorship signals

Create a document-feature matrix from function words, character n-grams or other justified features. Visualize similarity, test sensitivity to text length and genre and distinguish clustering from proof of authorship.

### 8. Topics, sentiment and emotion

Read [Topics, sentiment and emotion](../chapters/topics-emotions-classification.md). Prepare a codebook and human-labelled sample. Compare one simple baseline with one model or topic approach and conduct a qualitative error analysis.

### 9. Entities and relational data

Read [Databases and SQL](../chapters/databases-sql.md). Extract or manually identify people, places, institutions or works, resolve aliases and design a normalized SQLite schema with provenance and uncertainty.

### 10. SQL analysis

Import the data, enforce keys and write saved SQL queries that join entities, aggregate records and reveal missing coverage. Export one query result for further analysis while preserving the query itself.

### 11. GIS and literary/cultural space

Read [GIS and spatial humanities](../chapters/gis-spatial-humanities.md). Resolve place mentions against appropriate gazetteers, preserve alternatives and dates and build a map whose legend shows uncertainty.

### 12. Networks

Read [Networks and visualization](../chapters/networks-visualization.md). Define an edge from source evidence, build an edge list, compare a bipartite and projected view and interpret centrality only in relation to the construction rule.

### 13. AI, ethics and research packaging

Read [AI, ethics and reproducibility](../chapters/ai-ethics-reproducibility.md). Audit licences, privacy and representational bias. Add tests, citation metadata, a data dictionary, limitations and an AI-use statement.

### 14. Release and defence

Read [The living open handbook](../chapters/open-living-handbook.md). Tag a release candidate, exchange projects for reproducibility review, repair blocking issues and present both a substantive finding and the strongest reason for caution.

## Assessment model

A suggested distribution is:

- **technical labs (25%)** — reproducible exercises in Python, CLASSLA, SQL, GIS and networks;
- **method critique (15%)** — close analysis of one published or public digital project;
- **corpus/data design dossier (15%)** — sampling, metadata, rights and validation plan;
- **final reproducible project (35%)** — data, code, results and interpretation;
- **peer review and oral defence (10%)** — rerun another project and defend methodological choices.

Code elegance should not outweigh research validity. Evaluation should distinguish a technically failed but well-diagnosed experiment from an opaque successful run.

## Final project specification

The project release should include:

1. one specific Slovenian-studies research question;
2. source and rights statement;
3. corpus or data model with inclusion rules;
4. raw-data location or reconstruction instructions;
5. documented preprocessing and annotation;
6. one primary method and one validation strategy;
7. source-linked examples supporting the interpretation;
8. at least one table, plot, map or network with complete caption;
9. discussion of error, bias, uncertainty and alternative explanations;
10. README, environment file, licence and `CITATION.cff`;
11. tagged release and changelog;
12. a short contribution back to the handbook when the workflow is reusable.

## Recommended project themes

Suitable themes include lexical or grammatical change, literary style, newspaper discourse, emotion framing, translation history, named entities in historical collections, spatial narrative, correspondence networks, terminology, digitized heritage or evaluation of language technology for Slovene.

The question should remain small enough for manual validation. A modest corpus with inspectable evidence is preferable to an enormous dataset that the student cannot understand.

## Course versioning

Pin one stable handbook release and one tested environment file for the semester. When a tool breaks, document the change in the living edition and issue a course patch rather than altering graded instructions silently. Student repositories should record the exact commit or release from which workflows were followed.

---
