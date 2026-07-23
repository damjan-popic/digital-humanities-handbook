---
title: "GIS and spatial humanities"
description: "How place names, coordinates, historical gazetteers and spatial uncertainty become maps that support rather than replace interpretation."
tags: [GIS, mapping, geocoding, place, uncertainty]
status: draft
---

# GIS and spatial humanities

## Learning outcomes

After this chapter, you should be able to:

- distinguish a place mention, a place identity and a coordinate;
- explain geocoding, coordinate reference systems, layers and spatial joins;
- design a place table that preserves names, time and uncertainty;
- recognize how digitization, scale and map design shape spatial arguments;
- evaluate a map as an analytical claim rather than as an illustration.

## Before you begin

A nineteenth-century diary says that its author travelled to *St. Peter*. Which place is meant? The answer may depend on language, period, route, administrative boundaries and the writer's habits. Assigning coordinates is not clerical work; it is an interpretation that needs evidence.

Geocoding turns historical descriptions into modelled spatial entities. Use [Models, evidence and interpretation](models-evidence-interpretation.md) to document that transformation and [Infrastructures of digital humanities](critical-infrastructures.md) to assess the gazetteers, map services and access conditions on which it depends.

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
