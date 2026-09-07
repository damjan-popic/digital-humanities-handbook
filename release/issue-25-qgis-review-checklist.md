# Issue 25 QGIS manual review checklist

Status: **pending — not performed**. This checklist is a hand-off record, not
evidence that the GUI workflow or historical alignment has passed review.

Automated baseline retained for comparison: four fit points give 15.231 m RMSE;
the two independent checks give 220.063 m RMSE. The failed independent baseline
must not be replaced by a visual impression of a good fit.

## Environment and inputs

- [ ] Reviewer name: ____________________
- [ ] Review date (YYYY-MM-DD): ____________________
- [ ] QGIS version: ____________________
- [ ] Operating system: ____________________
- [ ] Packet/archive SHA256: ____________________
- [ ] Source image: `source/ljubljana-1910.jpg`
- [ ] Source image dimensions confirmed as 5747 × 7287 px
- [ ] Source image SHA256 confirmed as `d3c6c0475a6976c69c99065b7b9df1ae57a5fe6416a9acc858ef0cf75aebf21c`
- [ ] Machine-readable item record checked: `source/dlib-ljubljana-1910.json`
- [ ] Project/target CRS recorded as EPSG:3794
- [ ] Transformation type recorded: ____________________
- [ ] Resampling method recorded: ____________________

## Control and check points

- [ ] `input/gcps.csv` and generated `ljubljana-1910.points` imported without silently changing axis order or y sign
- [ ] Each point ID checked against the printed feature and the current coordinate record
- [ ] Source pixel x/y recorded for every point
- [ ] Target easting/northing recorded for every point
- [ ] Fit/check role preserved for every point
- [ ] Dragon Bridge (`SYN-G1`) identification checked
- [ ] Trnovo church (`SYN-G2`) identification checked
- [ ] Ljubljana Castle (`SYN-G3`) identification checked
- [ ] Tivoli Castle (`SYN-G4`) identification checked
- [ ] Railway station (`SYN-G5`, independent check) re-identified or rejected with reason: ____________________
- [ ] Cathedral (`SYN-G6`, independent check) re-identified or rejected with reason: ____________________
- [ ] QGIS per-point residuals copied to: ____________________
- [ ] QGIS fit RMSE copied here: ____________________ m
- [ ] Independent-check RMSE copied here: ____________________ m
- [ ] Leave-one-out results compared with `expected/gcp-leave-one-out.csv`

## Visual and methodological inspection

- [ ] Alignment inspected near every fit point at useful zoom
- [ ] Alignment inspected near every independent check point at useful zoom
- [ ] Alignment inspected away from control points, including map edges and corners
- [ ] Rotation, scale, shear and local distortion described: ____________________
- [ ] No modern basemap feature was treated as proof that the 1910 feature had the same position
- [ ] Publication date was not treated as a verified survey date
- [ ] Synthetic boundary/place data were kept separate from the authentic map
- [ ] Any rejected or moved point retains its earlier coordinates and a written rationale
- [ ] Screenshot or project evidence saved at: ____________________
- [ ] Generated raster/project path and SHA256 recorded: ____________________

## Decision

- [ ] **Fail / teaching baseline retained**
- [ ] **Revise controls and repeat review**
- [ ] **Pass for the stated teaching purpose**

Decision rationale and uncertainty:

______________________________________________________________________________

Methodological reviewer/sign-off: ____________________

Until every applicable field is completed and a decision is signed, handbook
language must continue to describe the raster and pixel selections as unapproved.
