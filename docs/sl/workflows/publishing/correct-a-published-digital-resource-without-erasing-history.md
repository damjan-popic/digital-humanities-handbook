---
title: "Kako popravite objavljeni digitalni vir, ne da bi izbrisali njegovo zgodovino?"
description: "Dokumentirajte napako, njeno znanstveno posledico, popravljeno izdajo in nadaljnjo pot navajanja."
category: "Objavljanje in podatki FAIR"
category_id: "Publishing & FAIR data"
difficulty: "srednje zahtevno"
time: "60–100 min"
tags: [popravki, objavljanje, različice, etika, navajanje]
status: draft
translation_status: "machine-assisted draft; requires human language review"
---

# Kako popravite objavljeni digitalni vir, ne da bi izbrisali njegovo zgodovino?

<div class="answer-meta" markdown="span">
<span>Objavljanje in podatki FAIR</span><span>srednje zahtevno</span><span>60–100 min</span>
</div>

!!! warning "Osnutek in obseg vaje"
    Postopek je pripravljen s strojno pomočjo ter čaka na strokovni in slovenski jezikovni pregled usposobljenih pregledovalcev. Številke izdaj in pisem so hipotetične. Zapise pripravite lokalno; dejanska objava ali odstranitev ni potrebna.

## Kaj želite doseči

Kako naj poznejši bralec izve, da je starejša izdaja isto zgodovinsko pismo preštela dvakrat? Spremembo in njeno dokazno posledico pokažite z izvornim popravkom, javnim obvestilom in navodilom za navajanje. Uporabite razlike iz poglavja [Živi odprti priročnik](../../chapters/open-living-handbook.md).

## Kaj potrebujete

- Določljivo starejšo izdajo in natančne lokatorje prizadetih razdelkov oziroma tabel.
- Dokazila za neodvisno preverjanje, vključno z dovoljenim dostopom do virov.
- Obe jezikovni različici, ustvarjene izhode in morebitna pravila popravljanja.
- Urednika, odgovornega za odločitev o obsegu popravka in pregleda.

## Postopek

1. Ponovite preverjanje prijavljene napake, preden jo razvrstite. Določite prizadete izdaje, jezike, slike, podatke in izračune. Negotov obseg navedite; popravek tabele lahko zahteva spremembo besedila, ki jo navaja.
2. Presodite, ali gre za omejen ali vsebinski popravek, zastaranje, nadomestitev ali umik. Erratum je obvestilo, ne nadomestilo za opredelitev težave. Resna nezanesljivost zahteva uredniško obravnavo; negotovost v preiskavi ločite od dokazane ugotovitve.
3. Po lokalnih pravilih presodite vpliv na različico. Izdaja popravka je primerna le brez spremembe učne argumentacije. Vsebinsko popravljeno gradivo v obstoječi zgradbi lahko zahteva manjšo izdajo; spremenjena metoda ali zgradba pa večjo recenzirano izdajo. Utemeljite odločitev.
4. Pripravite dvojezični izvorni popravek in spremembe odvisnih izhodov. Isti identifikator napake uporabite v dnevniku sprememb, erratumu in opombah ob izdaji. Zapišite napako, način preverjanja, spremembo in ugotovitve, ki ostajajo veljavne.
5. Običajne prej navedene datoteke ohranite določljive. Njihovemu pristajalni strani z metapodatki dodajte vidno povezavo do popravka in naslednika; popravljene datoteke sodijo v naslednjo izdajo. Dokumentirajte spremembo uredljivih metapodatkov na pristajalni strani, ne da bi trdili, da ste spremenili izvorne bajte.
6. Razkritje zasebnih ali varnostno občutljivih podatkov obravnavajte ločeno po pristojni institucionalni poti. Kadar je potrebno, omejite ali odstranite škodljivo vsebino, tudi iz zgodovine, depozitov in predpomnilnikov, kjer je izvedljivo. Dokazila ohranite le z odobrenim omejenim dostopom; objavite neobčutljivo obvestilo. Podatkov ne ponavljajte v prijavi in ne obljubljajte popolnega izbrisa tujih kopij.
7. Pregledovalec naj preveri celotno sled v obeh jezikih. Znova ustvarite prizadete izhode, primerjajte trditve in kontrolne vsote, preverite povezave s starejše pristajalne strani z metapodatki ter pripravite navodila za navajanje. Če posledice to upravičujejo, po odobrenih poteh obvestite znane izvajalce predmetov ali repozitorije.

## Dokumentacijski zapis

V učnem primeru iz 40 vrstic odstranimo štiri podvojene predstavitve in dobimo 36 različnih pisem. Izbira različice velja za ta primer, ne za vsak številčni popravek. Skupni strojni ključi omogočajo primerjavo EN/SL. Zapis je predloga, ne dokaz opravljenega človeškega pregleda.

Vnos `LETTER-COUNT-01` zajema tabelo in njene ustvarjene bralne kopije.

```yaml
record_type: publication-correction
record_status: template
correction_id: EX-ERR-001
affected_release: "1.0.0"
affected_objects:
  - "en/source-counting#worked-example"
  - "sl/source-counting#razdelan-primer"
  - "LETTER-COUNT-01"
evidence: "Primerjajte podvojene identifikatorje virov v vrsticah 37–40 s prejšnjimi vnosi"
category: substantive-correction
claim_before: "Tabela predstavlja 40 različnih zgodovinskih pisem"
claim_after: "40 vrstic predstavlja 36 različnih zgodovinskih pisem"
release_classification:
  level: minor
  target_version: "1.1.0"
  rationale: "Popravljeni učni sklep v obstoječi zgradbi; ni navaden popravek"
source_change: "Dvojezični popravek in ponovni izračun; commit v čakanju"
changelog: "EX-ERR-001 določi prizadeti razdelek 1.0.0 in načrtovano 1.1.0"
erratum: "Osnutek datiranega obvestila: dokazilo, napačen imenovalec, posledica, nadomestitev"
release_notes: "Povežite EX-ERR-001; opišite obseg pregleda in vse znova ustvarjene izhode"
prior_version_access: "Ohranite običajne datoteke 1.0.0; povežite erratum s pristajalne strani z metapodatki"
supersession: "1.1.0 nadomesti prizadeti učni primer; ohranite prejšnjo identiteto"
later_citation: "Navedite popravljeni razdelek 1.1.0; za zgodovino 1.0.0 in EX-ERR-001"
review: "Strokovni in slovenski jezikovni pregled še nista opravljena; zabeležite pregledovalce, datum in revizijo"
privacy_action: "V hipotetičnem primeru ni osebnih podatkov; vsak dejanski primer presodite znova"
```

## Rezultat

Dokumentacija popravka z izvornimi spremembami, dokazili, razvrstitvijo izdaje, erratumom, popravljenimi metapodatki, obsegom pregleda in navodili za poznejše navajanje. Predlagana dejanja ločite od izvedenih. Bralec mora razumeti posledice brez poznavanja sistema Git.

## Preverite se

- Ali bralec starejše izdaje najde vidno pot do popravka?
- Ali lahko loči nespremenjene datoteke od novih datotek naslednje izdaje?
- Ali erratum pove, če se interpretacija spremeni?
- Ali jezikovna zapisa navajata isto napako in naslednjo izdajo?
- Ali zasebnostni primer prepreči kopiranje občutljivih dokazil v javno zgodovino?

## Pogoste pasti

- Zamenjava arhiviranega ZIP pod istim imenom in tiha sprememba kontrolne vsote.
- Označitev spremenjenega sklepa kot tipkarske napake, ker se spremeni en stavek.
- Obravnava zastaranja kot dokaza, da je bila prejšnja zgodovinska analiza napačna.
- Ohranjanje škodljivega javnega razkritja v imenu preglednosti.

## Vaja

Izmenjajte dokumentacijo. Številčno napako nadomestite z nedelujočo povezavo, ki ima ustreznega avtoritativnega naslednika, nato z razkritimi podatki udeleženca. Pojasnite razlike v dejanjih in razvrstitvi izdaje. Utemeljen odgovor navede negotovosti in odgovorne odločevalce, ne izmišljenih potrditev.

## Viri in preverjanje storitev

Preverjeno **7. septembra 2026**: COPE, [Retraction guidelines](https://doi.org/10.24318/cope.2019.1.4), različica 3 (2025), in [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html). Vira podpirata razlike; odločitve o izdaji določa uredniška politika publikacije. Za naslednji paket uporabite [pripravo oštevilčene znanstvene izdaje](create-a-versioned-scholarly-release.md).
