---
title: "How do I georeference and check a historical map in QGIS?"
description: "Georeference a rights-documented historical plan, reserve check points and report residual uncertainty."
category: "Mapping"
category_id: "Mapping"
difficulty: "intermediate"
time: "90–120 min"
tags: [QGIS, georeferencing, control-points, CRS, spatial-uncertainty]
status: draft
---

# How do I georeference and check a historical map in QGIS?

<div class="answer-meta" markdown>
<span>Mapping</span><span>intermediate</span><span>90–120 min</span>
</div>

## What you are trying to do

Test whether a historical plan and a current reference layer locate the same features closely enough for your research question. A small fitted error is not an accuracy certificate. [GIS and spatial humanities](../../chapters/gis-spatial-humanities.md) explains the distinction between fit, independent checks and historical interpretation.

## You need

Unpack the [companion ZIP](../../../assets/downloads/contested-models-v1.zip), with Koch's 1910 Ljubljana scan, source-rights notes and cached current landmark coordinates. dLib labels this scan public domain; current structured coordinates derive from Wikidata's CC0 data. Read the precise attribution and limitations in `rights-and-provenance.md`.

Use Python 3.10+ for the numerical route and QGIS for the raster exercise. Interface steps follow the [QGIS 3.40 manual](https://docs.qgis.org/3.40/en/docs/user_manual/managing_data_source/georeferencer.html). The numerical pilot is tested; this GUI procedure has not yet received a recorded QGIS session review. Record your installed version and any menu differences. Do not treat 3.40 as the newest release.

Repository maintainers should complete `release/issue-25-qgis-review-checklist.md`,
which records the exact environment, point, residual, visual-inspection and
decision fields. Its pending state is not evidence that this procedure was run.

## Workflow

### 1. Reproduce the baseline

```bash
python run.py --output output-first
```

Inspect `gcp-residuals.csv`, `gcp-leave-one-out.csv` and `current-landmarks.csv`. Inputs use the original 5747 × 7287 pixel image. Recompressed or differently cropped copies need new pixel selections. The six supplied points are first-pass candidates, not approved controls.

### 2. Inspect features before fitting

Open `source/ljubljana-1910.jpg`. Compare each candidate against its Wikidata identifier, cached coordinates and description in `input/landmarks.csv`. A bridge centre, building centre and survey corner are not interchangeable. Keep G5 and G6 for independent checking; do not enable them to improve the fit.

In QGIS, open the Georeferencer from the Layer menu and load the image. Load the generated `output-first/ljubljana-1910.points`. Its source y values are negative, matching the georeferencer coordinate convention; the input CSV records pixel y positive downward. Verify the points appear on the intended features before proceeding. If not, stop and record the mismatch.

### 3. Set and record the transformation

Select Polynomial 1 (affine), target CRS EPSG:3794, nearest-neighbour resampling and a new GeoTIFF output filename. Retain G1–G4 as enabled controls and G5–G6 disabled. Save the control-point file and transformation settings, then run georeferencing. Keep the original image unchanged.

The generated points file's residual columns initially contain zeros as placeholders, not measured errors. Compare QGIS's recalculated residuals only after confirming units and settings. Resampling affects pixel appearance, not the validity of a landmark identification.

### 4. Compare with the current layer

Add `current-landmarks.csv` as a delimited-text point layer with x=`target_e_m`, y=`target_n_m`, CRS EPSG:3794. Overlay it with the output raster. Inspect all six points, especially the disabled station and cathedral. Save the project and export the reference layer to GeoPackage if useful; no remote basemap is required.

| Numerical baseline | RMSE in metres |
|---|---:|
| Four fitted controls | 15.231 |
| Two independent checks | 220.063 |

The independent result fails an approximately 15 m accuracy claim. Check spatial distribution too: leaving out the western control produces a 1,090.241 m error at that point. This is a sensitivity warning, not a recommended positional tolerance.

### 5. Review, do not conceal, mismatch

Investigate one failed point. Was the wrong building selected, did the referent change, or is the current coordinate too coarse? Write a decision row with old point, revised point, source evidence and reason. Save the revised CSV and output under new names. Compare the same independent checks before and after; never silently remove an inconvenient check.

Protect sensitive locations when adapting the exercise. Generalize or restrict access where justified, and retain a safe audit trail without publishing protected coordinates.

## Output

Submit the original-source citation, rights note, QGIS version, CRS, transformation and resampling settings, controls with enabled flags, GeoTIFF/project when available, residual table and mismatch log. Include a text account of the overlay. Tables alone provide the numerical alternative, but do not constitute a completed raster/GUI review.

## Check yourself

Can another reader identify the same feature in both sources? Are independent checks truly withheld? Are residual units metres rather than pixels? Does the claim survive the independent result?

## Common traps

Assigning a CRS instead of transforming coordinates; using a rescaled scan with old pixel points; counting disabled-point zero placeholders as successful checks; and interpreting a smooth overlay as evidence of historical accuracy.

## Practice task

Audit one fitted and one withheld point, then submit the unchanged baseline and one justified revision or a documented decision to leave it unresolved. Explain why the synthetic boundary experiment must never be overlaid as an authentic Ljubljana boundary.
