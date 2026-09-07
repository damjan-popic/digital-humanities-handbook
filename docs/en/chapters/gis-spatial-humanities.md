---
title: "GIS and spatial humanities"
description: "Historical places, competing identifications and dated geometries: how spatial models become testable humanities arguments."
tags: [GIS, mapping, geocoding, place, uncertainty]
status: draft
---

# GIS and spatial humanities

## Learning outcomes

After this chapter, you should be able to:

- distinguish a place, its names, its geometries and its administrative memberships;
- separate source date, represented time and the date of a spatial identification;
- explain coordinate reference systems, georeferencing, scale and positional accuracy;
- preserve unresolved candidates and validate an identification against independent evidence;
- test how boundaries, denominators, missing records and transport assumptions change a spatial claim;
- publish an accessible map with a non-visual account of its evidence and limitations.

## Before you begin

Did a person cross a border, or did a border cross the person? A record that assigns a resident to a different jurisdiction does not by itself establish migration. Nor does a letter headed “St. Peter” identify one unambiguous point. Before opening a map, write down what evidence would distinguish movement, administrative change and editorial misidentification. Which of these explanations could your surviving sources actually test?

The recurring companion dossier from [Databases and SQL](databases-sql.md) concerns names, status, language use and territorial membership. Its people and boundary experiment are explicitly synthetic. They are not reconstructed biographies of people in the authentic archival-friction newspaper. The [downloadable packet](../../assets/downloads/contested-models-v1.zip) also contains an authentic Ljubljana plan and current landmark coordinates. Keep these evidence classes separate: the historical plan does not authenticate the invented boundary experiment.

## The argument: coordinates are qualified claims

Spatial humanities asks how location, distance, territory and experienced place contribute to interpretation. A point map can reveal a distribution, but it cannot determine what a place meant to an inhabitant or why a record named it. The interdisciplinary agenda collected in [The Spatial Humanities](https://iupress.org/9780253222176/the-spatial-humanities/) treats GIS as a research instrument whose representations must accommodate historical and interpretive questions, not as a replacement for them.

Our operational principle is therefore simple: retain the passage, identification decision, geometry and temporal qualification as separable records. An administrative label is evidence about classification; a coordinate is an editorial representation. Neither necessarily describes self-identification. Historical cartography also warrants source criticism. Harley's [“Deconstructing the Map”](https://doi.org/10.3138/E635-7827-1757-9T53) makes mapmaking's social and political conditions part of analysis. Ask who commissioned a plan, what it made legible and what its conventions excluded.

## Place, name, geometry and territory

A **toponym** is a name used for a place. A **place entity** is the project's continuing referent, whose identity may itself require argument. A **geometry** is a spatial representation chosen for a purpose. An **administrative unit** is an institutionally defined territory; its name, jurisdiction and boundary need not change together. A **route** represents a sequence or possible path, whereas a **region** may be vernacular, ecological or administrative. An imagined homeland or a remembered neighbourhood may not admit a defensible closed polygon.

For the dossier, maintain a place table, a name-assertion table and dated territorial memberships. Do not rename every historical occurrence when a modern authority supplies a preferred label. Preserve “St. Peter” as source wording alongside the candidates `SYN-L1` and `SYN-L2`. Both candidates are inventions for the exercise, not claims that two particular real locations had that name.

A neighbourhood point can support approximate display. A building footprint supports a different question; a region's centroid does not show where its population lived. Record why each geometry is adequate, and specify what cannot be inferred from it.

## Gazetteers without automatic certainty

Historical gazetteers link names, identifiers and descriptions across different temporal and linguistic contexts. [Southall, Mostern and Berman](https://doi.org/10.3366/ijhac.2011.0028) explain why a historical gazetteer needs more than a list of coordinate pairs. An authority identifier helps distinguish records, but it does not settle every historical identity problem.

For each lookup, retain the original query, language, source date, resource name, version or retrieval date, returned identifier, alternatives and review decision. Search more than one name form. Examine neighbouring places, institutional context and a contemporary description. A service score can describe string similarity or ranking; do not relabel it “90% historically correct” without a calibrated validation study.

Keep rejected and unresolved candidates. Record why one was rejected, rather than silently erasing it. A name absent from a modern gazetteer may identify a vanished settlement, an unofficial district, a renamed street or a transcription error. Conversely, a successful response may select a distant contemporary place with the same name. Review a sample of confident matches as well as failures.

## A historically qualified place model

The source, place identification and territorial join answer different questions:

| Record | Modern point shortcut | Qualified alternative |
|---|---|---|
| “St. Peter” in `SYN-D2` | choose the first search result | retain `SYN-L1` and `SYN-L2`; identification unresolved |
| A's residence at `SYN-L1` | one coordinate and current country | dated residence assertion, geometry and membership |
| A later jurisdiction label | infer a move | compare residence stability with boundary versions |
| A map published in 1910 | date every feature to 1910 | distinguish publication from represented or surveyed time |

A historical source can describe an earlier journey, reproduce an older plan or propose a future road. Store publication date separately from represented time and survey or revision information when known. Unknown dates remain unknown. Do not manufacture a precise interval merely because the GIS temporal controller requires one.

For candidate identification, the appropriate output may be two rows and a paragraph, not two confidently plotted residences. A candidate count is not a count of actual locations occupied. The packet keeps the mention's event window separate from boundary and toponym validity. Its comparison period is the actual half-open intersection of one boundary version and one name version, explicitly labelled as candidate-place history rather than mention duration. A 1917 name change inside the 1910–1919 boundary version is therefore not lost.

## Coordinate systems and transformations

Coordinates require a **coordinate reference system** (CRS), including units and the reference framework in which positions are expressed. Geographic longitude and latitude are angular coordinates. Projected coordinates support planar operations within a stated area of use. Measuring a polygon in square degrees does not produce its area in square metres.

Assigning a CRS declares what existing numbers mean; transforming coordinates calculates different numbers for another system. Confusing these operations can move a layer while leaving its shape persuasive. Check coordinate ranges, axis order and units before interpreting an overlay. The packet transforms cached longitude/latitude using an explicit longitude-first setting into EPSG:3794. The Slovenian surveying authority documents the national projected framework and its [D96-17/TM terminology](https://www.e-prostor.gov.si/podrocja/drzavni-koordinatni-sistem/horizontalna-sestavina/); software may display the familiar D96/TM label.

Record the source CRS, target CRS, transformation implementation and any required grids. A project's on-the-fly display setting does not change the stored source coordinates. See the versioned [QGIS projection documentation](https://docs.qgis.org/3.40/en/docs/user_manual/working_with_projections/working_with_projections.html) for interface-specific operations.

## Scale, resolution and accuracy

Scale relates a map distance to a ground distance. Resolution describes the smallest represented or sampled unit. Positional accuracy concerns agreement with a defensible reference location. Precision concerns the granularity of recorded numbers. These properties are related but not interchangeable.

The authentic plan in the packet is Ciril Metod Koch's *Ljubljana*, published in 1910 at 1:8,200, as catalogued by [dLib.si](https://dlib.si/details/URN:NBN:SI:IMG-132KCU7C). At that nominal scale, one printed millimetre represents 8.2 metres. A building symbol may nevertheless be generalized or displaced. Increasing scan resolution cannot recover detail that the cartographer never recorded.

Similarly, six decimal places in a current landmark record do not establish survey-grade accuracy. The packet records the precision reported by Wikidata separately from our manually selected image points. Some coordinates describe an entity generally rather than an identifiable corner. A comparison that ignores this mismatch confuses different spatial referents.

## Georeferencing as a testable fit

Georeferencing estimates a transformation between image coordinates and reference coordinates. Choose control points that identify the same physical feature in both sources, distribute them across the study area and avoid relying on one street or cluster. Corners may be more reproducible than vague centres, provided the building has not changed.

An affine transformation permits translation, rotation, scaling and shear. It does not reproduce every local distortion. A more flexible transformation can improve fitted residuals while making unsupported distortions between controls. Select a transformation for its assumptions and validation performance, not just its attractive appearance.

Reserve independent check points that do not determine the fit. A residual is the difference between predicted and reference position for a point. Root-mean-square error (RMSE) summarizes those distances, but its meaning depends on units, point quality and where points lie. The [QGIS georeferencer documentation](https://docs.qgis.org/3.40/en/docs/user_manual/managing_data_source/georeferencer.html) explains available transformations and control-point handling; the software does not certify historical correspondence.

## Worked example: a failed alignment check

The packet supplies the public-domain-labelled dLib scan, six first-pass landmark selections, cached current coordinates and a reproducible affine calculation. Four points fit the transformation; the railway station and cathedral are withheld. These are a deliberately retained pilot, not approved survey controls. Landmark centres and image selections require manual review.

| Check | Result in metres | Interpretation |
|---|---:|---|
| Four fitted controls, RMSE | 15.231 | describes fit at selected controls only |
| Two independent checks, RMSE | 220.063 | does not support a claim of approximately 15 m accuracy |
| Leave out the western fitted point, check it afterwards | 1,090.241 | exposes weak spatial support and extrapolation |
| Cathedral check alone | 142.481 | re-examine the selected feature and coordinate referent |

These outputs can be reproduced without QGIS. The paired [georeferencing workflow](../workflows/mapping/georeference-and-check-a-historical-map-in-qgis.md) adds the GUI procedure, saving the transformation and inspecting a current landmark layer. The interface procedure still requires a recorded QGIS review; the numerical pilot is not a claim that the resulting raster has been visually validated.

Do not delete a bad check merely to improve a score. Reopen the source image, inspect the reference description and record whether a point was misidentified, moved, generalized or insufficiently precise. Save a corrected run separately. A low fitted RMSE alongside a poor independent result is useful evidence about the limits of the model.

## Worked example: the border moves

The boundary experiment uses an explicitly fictional 1,000-metre square in a local engineering coordinate system, not EPSG:3794 and not historical Ljubljana boundaries. A vertical divider changes from x=500 to x=600 in 1920. A's residence remains at x=550; the dossier stipulates continuity through 1925. East includes the dividing line, making the containment rule explicit.

| Candidate | Centre x | 1910 centre membership | 1925 centre membership | With ±75 m positional uncertainty |
|---|---:|---|---|---|
| `SYN-L1` | 550 m | `SYN-EAST` | `SYN-W` | either territory in both periods |
| `SYN-L2` | 800 m | `SYN-EAST` | `SYN-EAST` | east in both periods |

Under centre-point classification, A's territorial affiliation changes without migration. Under the uncertainty envelope, membership cannot be uniquely assigned from geometry alone. The ±75 metres is a stipulated sensitivity range, not a measured confidence interval. The unresolved workplace mention must not replace the residence assertion.

The [dated-place workflow](../workflows/mapping/model-changing-place-names-and-boundaries.md) reproduces this table. An actual historical project would additionally need evidence for the boundary date, geometry, residence continuity and administrative meaning. The synthetic calculation establishes logical consequences, not historical facts.

## Spatial joins and missingness

A spatial join adds attributes according to relations such as within, intersects or nearest. Combine the spatial predicate with a time predicate: a point and polygon that overlap on screen may refer to different centuries. State how boundary points, overlapping jurisdictions and uncertain intervals are handled. Distinguish possible membership from membership under every allowed location.

Record unlocated mentions in the denominator of your coverage report. If ten of twenty letters can be located, mapping only those ten does not establish the geography of the whole correspondence. Missingness may follow language, cataloguing practice, urban address coverage or selective preservation. An empty region might lack surviving records, digitization or successful identifications rather than historical activity.

Compare matched and unmatched records by period, source type and language before interpreting density. Publish the unmatched table with reasons and permitted source excerpts. Do not force a coordinate simply to achieve complete-looking coverage.

## Choropleths and the unit problem

A choropleth shades areas by a value. Counts answer a different question from rates. Suppose two fictional districts contain 20 and 10 surviving letters, but their relevant populations are 2,000 and 500. Counts rank the first district higher; rates are 10 and 20 letters per thousand residents. Neither describes literacy without further assumptions about authorship, survival and the population at risk.

Aggregation also changes results when boundaries or area sizes change: this is the **modifiable areal unit problem**. [Fotheringham and Wong](https://doi.org/10.1068/a231025) examine its implications for multivariate analysis. For our simpler exercise, compare counts and rates under alternative groupings and explain which residents and observations enter each denominator.

Do not divide an 1850 numerator by a convenient modern population without justification. Mark missing values separately from zero. Publish the underlying numerator, denominator, period and classification bins so a reader can reconstruct the shading without seeing the map.

## Routes, distance and accessibility

A straight line between two mentioned places is not evidence of a journey. The source may describe remembered locations, reported events or an imagined destination. Even when travel is documented, a shortest modern road path can be historically impossible. Bridges, border controls, gradients, seasonal conditions and available transport affect accessibility.

Define whether you estimate geometric distance, network distance, travel time or a documented itinerary. A route network needs dated segments and explicit cost assumptions. Test at least one plausible alternative: remove an unverified bridge or vary walking speed rather than presenting one exact travel time.

For the ambiguous “St. Peter” mention, compare what each candidate would imply, but do not invent a route to decide the identity circularly. A route plausibility argument is supporting evidence only if its historical transport assumptions are independently justified. Preserve the textual sequence even when no defensible line can be drawn.

## Design, access and sensitive locations

Map design shapes the argument through extent, labels, classification and omission. Use a sequential palette for ordered quantities and a clear neutral treatment for missing information. Do not rely on colour alone: pair candidate symbols with identifiers, uncertainty categories and explanatory text. Label the synthetic boundary model prominently.

Provide a table giving every plotted identifier, period, membership, uncertainty and source link. A text description should state the pattern and exceptions, not merely announce that a map exists. Keep labels legible at the intended output size and test light and dark backgrounds. Interactive maps also need keyboard access and a downloadable alternative.

Precise locations can expose vulnerable living communities, sacred sites or archaeological remains to harm. Public availability does not remove responsibility. Assess consent, legal restrictions and foreseeable misuse before publication; consider generalization or restricted access. Keep a secure source record where permitted, and explain the public transformation without revealing protected coordinates.

## Hybrid modelling

One representation need not carry everything. Relational tables preserve queryable place assertions; TEI/XML retains textual variants and editorial structure; GeoPackage can hold dated geometries; a graph may explore routes. Facsimiles and diplomatic transcription preserve evidence, while prose records distinctions that should resist categorical reduction. Ask which distinctions must be queryable, which must remain recoverable and which should resist formalization.

## Practice

Unpack the companion archive and run:

```bash
python run.py --output output-first
```

Use a new output directory for each run. Inspect `membership.csv`, `gcp-residuals.csv` and `gcp-leave-one-out.csv` before making any map. Compare centre-based membership with uncertain membership; explain why the name candidates cannot be counted as two residences. Then audit one fitted and one withheld landmark against the image and the cached reference record.

Submit the tables, source and rights note, CRS and transformation record, a candidate-decision log and a 200-word interpretation. Name one conclusion that survives the sensitivity checks and one that fails. If you cannot use GIS, the tables and explicit containment rules form a complete non-visual submission.

## Reflection

- Which apparent migration could instead be a change in boundaries or classification?
- What does your geocoder's confidence actually measure?
- Would another denominator, reference point or plausible candidate reverse your claim?
- Which locations should remain approximate or unpublished, and who should decide?

## Summary

Spatial evidence becomes credible through qualified identification, not through polished plotting. Names, places, geometries, jurisdictions and routes require distinct records and explicit dates. Independent checks can expose a misleadingly good fit. Candidate preservation, uncertainty-aware joins, defensible denominators and historical transport assumptions make a spatial argument inspectable. A table that honestly retains ambiguity can be a stronger result than a seamless map.

## Further reading

- Bodenhamer, David J., John Corrigan and Trevor M. Harris, eds. 2010. [*The Spatial Humanities: GIS and the Future of Humanities Scholarship*](https://iupress.org/9780253222176/the-spatial-humanities/). Indiana University Press.
- Harley, J. B. 1989. [“Deconstructing the Map.”](https://doi.org/10.3138/E635-7827-1757-9T53) *Cartographica* 26(2): 1–20.
- Southall, Humphrey, Ruth Mostern and Merrick Lex Berman. 2011. [“On historical gazetteers.”](https://doi.org/10.3366/ijhac.2011.0028) *International Journal of Humanities and Arts Computing* 5(2): 127–145.
- Fotheringham, A. S., and D. W. S. Wong. 1991. [“The Modifiable Areal Unit Problem in Multivariate Statistical Analysis.”](https://doi.org/10.1068/a231025) *Environment and Planning A* 23(7): 1025–1044.
- QGIS Documentation. [Georeferencer, version 3.40](https://docs.qgis.org/3.40/en/docs/user_manual/managing_data_source/georeferencer.html). Versioned operational reference, not an assertion that this is the newest release.
