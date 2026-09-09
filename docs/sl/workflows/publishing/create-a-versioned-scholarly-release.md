---
title: "Kako pripravite oštevilčeno znanstveno izdajo?"
description: "Pripravite preverljiv načrt izdaje z manifestom, obsegom recenzije, podatki za navajanje, pravicami, kontrolnimi vsotami in pogojno potjo v hrambo."
category: "Objavljanje in podatki FAIR"
category_id: "Publishing & FAIR data"
difficulty: "srednje zahtevno"
time: "90–150 min"
tags: [objavljanje, različice, hramba, recenziranje, metapodatki]
status: draft
translation_status: "machine-assisted draft; requires human language review"
---

# Kako pripravite oštevilčeno znanstveno izdajo?

<div class="answer-meta" markdown="span">
<span>Objavljanje in podatki FAIR</span><span>srednje zahtevno</span><span>90–150 min</span>
</div>

!!! warning "Osnutek in obseg vaje"
    Postopek je pripravljen s strojno pomočjo ter čaka na strokovni in slovenski jezikovni pregled usposobljenih pregledovalcev. Z njim pripravite načrt izdaje; ne objavite izdaje, ne registrirate identifikatorjev in ne potrdite založniške pogodbe.

## Kaj želite doseči

Bralec mora vedeti, katero dvojezično učno gradivo podpira navedeno argumentacijo. Pripravite paket, v katerem se vsebina, dokazila o pregledu, pravice in podatki za navajanje ujemajo. S poglavjem [Živi odprti priročnik](../../chapters/open-living-handbook.md) ločite recenzirano izdajo od sproti vzdrževanega izvora.

## Kaj potrebujete

- Majhen učni projekt z razjasnjenimi pravicami, izvorno revizijo in navodili za gradnjo.
- Popis vključenih in izključenih strani s stanjem jezikovnih parov.
- Razpoložljive zapise pregledov ter pisne založniške in depozitne zahteve, če so potrjene.
- Lokalni delovni prostor in orodje za kontrolne vsote; skrbniška dovoljenja niso potrebna.

## Postopek

1. Določite znanstveno trditev izdaje in občinstvo. Izberite kandidatno revizijo ter popišite vključene predmete. Ločite recenzirano gradivo od spremljevalne žive zbirke; stran zunaj manifesta ne more prevzeti recenzijskega statusa izdaje.
2. Zabeležite obseg pregleda, imena, kadar jih smete objaviti, datume in pregledano revizijo. Prevode preverite po pomenu in navodilih; osnutke in nadomestne strani označite. Za vsak bralni format posebej navedite dostopnostni pregled in preostale izjeme.
3. Po uredniških pravilih izberite različico in odločitev pojasnite v dnevniku sprememb. Uskladite predlagano oznako, navedek, manifest, opombe ob izdaji in imena paketov. Oznaka v Gitu, izdaja na GitHubu in znanstveni identifikator so različni predmeti.
4. Izbrani izvor zgradite v dokumentiranem okolju. Preglejte oba jezika, povezave, lokatorje virov, tabele in branje brez povezave. Pripravite izvorni arhiv in ustrezne bralne kopije z licencami ter navedbami sodelavcev. SHA-256 izračunajte po dokončanju datotek; spremenjeni ZIP potrebuje novo vsoto.
5. Izpolnite spodnji zapis. `null` v predlogi pomeni, da podatek še ni pridobljen, ne dodeljene vrednosti ali uspešnega preverjanja. Nadomestite ga šele s preverjenim commitom ali kontrolno vsoto. Vnose manifesta in datotek ponovite za celoten popis.
6. Z založnikom in ustanovo uskladite pristojnosti za identifikatorje ter pogoje hrambe. DOI in ISBN ostaneta pogojna. Ko je odobreni depozit dejansko opravljen, preverite prevzete bajte in pristajalno stran z metapodatki. Artefakt GitHub Actions sam ni ureditev dolgoročne hrambe.
7. Drug urednik naj primerja vse zapise. Navedite odprte ovire in ostanite pri kandidatu, če manjkajo zahtevani pregledi, pravice, dostopnostna presoja ali založniške odločitve.

## Dokumentacijski zapis

Predloga je namenjena izmišljeni dvojezični učni izdaji o štetju virov. Poti pripadajo vaji, ne temu repozitoriju. Strojni ključi so v obeh jezikih enaki. Prazne vrednosti izrecno označujejo čakanje, ne popolnosti.

```yaml
record_type: scholarly-release-plan
record_status: template
project: "Izmišljena učna izdaja o štetju virov"
candidate_version: "1.0.0-rc.1"
source_commit: null
manifest:
  - path: "docs/en/source-counting.md"
    title: "Counting historical sources"
    language: en
    content_type: stable-chapter
    review_status: pending-human-review
    review_scope: "Vsebina, metoda, didaktika; pregledovalec/datum/revizija v čakanju"
    translation_status: "Vzporedni slovenski osnutek; pregled enakovrednosti v čakanju"
    licence: CC-BY-4.0
    source_sha256: null
    inclusion_status: proposed-reviewed-edition
    external_dependencies: []
    accessibility: "Pregled naslovov, tabel in tipkovnice v čakanju"
  - path: "docs/sl/source-counting.md"
    title: "Štetje zgodovinskih virov"
    language: sl
    content_type: stable-chapter
    review_status: pending-human-review
    review_scope: "Slovenski jezik in vsebina; pregledovalec/datum/revizija v čakanju"
    translation_status: "Strojno podprt osnutek v paru z angleškim"
    licence: CC-BY-4.0
    source_sha256: null
    inclusion_status: proposed-reviewed-edition
    external_dependencies: []
    accessibility: "Pregled naslovov, tabel in tipkovnice v čakanju"
changelog: "Osnutek vnosa za 1.0.0-rc.1; ne datum objave"
citation_metadata: "Osnutek avtor/naslov/različica/lokator; uskladitev pred objavo"
identifiers:
  doi: null
  isbn: null
  assignment_authority: "Založnik in institucionalni repozitorij; potrditev v čakanju"
  status: pending-agreement
artefacts:
  - path: "source-counting-1.0.0-rc.1-source.zip"
    sha256: null
  - path: "source-counting-1.0.0-rc.1-reading.zip"
    sha256: null
archive:
  repository: "Institucionalni repozitorij; sprejem v čakanju"
  deposit_status: not-deposited
  verification: "Čakajo prevzem, primerjava vsot in pregled pristajalne strani z metapodatki"
build_environment: "Zapišite OS, izvajalno okolje, odvisnosti, ukaz in opaženi rezultat"
approval: "Čakajo imenovani urednik, zapis pregledov in zahtevana založniška potrditev"
```

## Rezultat

Kandidatni paket z manifestom, dnevnikom sprememb, osnutkom navedka, licencami, zapisi sodelavcev in pregledov ter kontrolnimi vsotami. Ločite pripravljene datoteke od opravljenega depozita. Dejanska založniško usklajena izdaja tega priročnika sodi v [nalogo #30](https://github.com/damjan-popic/digital-humanities-handbook/issues/30).

## Preverite se

- Ali druga oseba lahko določi izvorno revizijo in vse vključene predmete?
- Ali se trditve o pregledu in prevodih ujemajo z zapisi v obeh jezikih?
- Ali paket lahko razširite in bistveno vsebino preberete brez povezave?
- Ali se ponovno izračunane vsote ujemajo in so manjkajoče odvisnosti navedene?
- Ali ima vsak nedodeljeni identifikator status čakanja in določeno pristojno stran?

## Pogoste pasti

- Enačenje uspešnega CI z recenzijo ali oznake z dolgoročno hrambo.
- Pripisovanje repozitorijske licence vsem zunanjim podatkom.
- Navajanje nedatirane veje `main` po uporabi oštevilčene izdaje.
- Domneva, da dostopni HTML dokazuje dostopnost PDF.

## Vaja

Izmenjajte kandidatne načrte. Uvedite manjkajočo slovensko stran, sliko brez dovoljenja in spremenjeni ZIP. Določite trditve, ki jih je treba umakniti, in datoteke, ki jih je treba znova ustvariti. Oddajte popravljeni načrt in utemeljitev, ali se objava lahko nadaljuje.

## Viri in preverjanje storitev

Preverjeno **7. septembra 2026**: [GitHub: About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases), [Zenodo: Digital Object Identifier (DOI)](https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/) in [Digital Preservation Coalition: Fixity and checksums](https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums). Pred izvedbo znova preverite izbrano storitev in institucionalne zahteve.
