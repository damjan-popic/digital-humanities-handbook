---
translation_status: machine-assisted draft; requires human language review
reference_status: machine-assisted reference draft; pending human review
reference_version: TNLP-REF-2
---

# Pravila referenčnega anotiranja CLASSLA

Štiri datoteke CoNLL-U so strojno podprti osnutek referenčne anotacije različice
`TNLP-REF-2`, ki čaka na strokovni človeški pregled. Omogočajo pregleden preizkus
ene zamrznjene izvedbe CLASSLA, ne določajo pa univerzalne jezikoslovne resnice
ali splošne kakovosti modela.

## Odločitve

1. Ohranite izbrano poved, velike in male črke ter ločila. Ponudnikovega OCR ne
   zamenjajte prikrito z referenčnim prepisom.
2. Pri sodobnih vzorcih in referenčnem prepisu anotirajte branje dane plasti.
   Pri ponudnikovem OCR ohranite opaženo obliko, vendar anotirajte na podlagi
   posnetka preverjeno raziskovalno mejo besede ali lemo, kadar arhivski paket
   dokumentira očitno napako prepoznavanja.
3. Zlepljeni OCR `narodain` zapišite kot večbesedno pojavnico CoNLL-U `naroda`
   + `in`. Ohranite opažene oblike `stavovske`, `kultrunega` in `i`, pripišite
   pa izvorno utemeljene leme `stanovski`, `kulturen` in `ki`.
4. V zvezi `s Slovensko ljudsko stranko` pripnite `stranko` na drugi `gre` kot
   `obl` (pojavnica 34 v `TNLP-AF-REF`, 33 v `TNLP-AF-OCR`). Pripenjanje na
   `naziranja` kot `nmod` spremeni razmerje na ravni stavka.
5. Posamostaljeni `vse` v `zato gre vse` obravnavajte kot `PRON`, lemo `ves`
   in osebek glagola `gre`. To ostaja sporna odločitev v osnutku, ne prikriti
   popravek ali človeško razsojena oznaka.

## Pregled osnutka in nerazrešene analize

Vse štiri datoteke — `TNLP-CLEAN-01`, `TNLP-CLEAN-02`, `TNLP-AF-REF` in
`TNLP-AF-OCR` — so bile pri strojno podprtem uredniškem popravku različice
`TNLP-REF-2` pregledane po vrsticah; strokovnega človeškega pregleda ni bilo.
Pri sodobnih primerih ostajata odprti analiza poklicnega naziva z osebnim imenom
(`Kustosinja Maja Kovač`) in skupni osebek pri priredno povezanih glagolih. Pri
zgodovinskih primerih ostajajo odprti posamostaljeni `vse`, diskurzna oziroma
skladenjska vloga `zato` in anotacija oblike OCR `i` kot izvorno utemeljenega
oziralnega `ki`. Usposobljeni pregledovalec mora te odločitve preveriti ob
navedenih anotacijskih smernicah.

Za prehod v stanje `human-reviewed` zapišite ime pregledovalca, datum pregleda
po standardu ISO, obseg pregleda datotek in plasti, nestrinjanja ter morebitno
razsojanje. Dokler vsa štiri polja niso izpolnjena, ohranite `reference_status`
kot `machine-assisted reference draft; pending human review`. Pri ponovni rabi
navedite to omejitev, ta pravila in imenovalce posameznih plasti.
