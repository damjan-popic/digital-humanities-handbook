---
title: "Predloga za kritično študijo primera"
description: "Predloga s petnajstimi razdelki za preučevanje javnega humanističnega projekta prek virov, pregledanih dokazov, modeliranja, pravic in omejitev."
tags: [predloga, študije-primerov, dokazno-gradivo, kritika-virov]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Predloga za kritično študijo primera

S predlogo pojasnite, kakšno spoznavanje omogoča humanistični projekt in česa
njegov vmesnik, podatki ali koda ne dokazujejo. Izhajajte iz raziskovalnega
vprašanja, ne promocijskega opisa. Odgovorna študija lahko obravnava vmesnik,
podatkovno zbirko ali dokumentacijo brez zagona kode. Navedite dejansko
opravljen pregled in njegove omejitve.

!!! note "Stanje prevoda"
    To je strojno podprt osnutek, ki čaka na strokovni in jezikovni pregled.
    Predloga ne predstavlja že pregledane študije ali človeške odobritve.

V mapah `docs/en/case-studies/` in `docs/sl/case-studies/` ustvarite par strani
z istim imenom datoteke. Ohranite spodnjih petnajst naslovov, navodila pa
nadomestite s povezano razlago, utemeljeno v dokaznem gradivu.

Avtorski kataložni zapis pripravite v `data/case-studies.yml` po navodilih
`data/case-study-schema.json` in `data/case-study-metadata.md`. Polja
`case_id`, lokalizirani `title`, `content_standard`, `translation_status` in `audit_record`
v metapodatkih strani morajo biti usklajena s tem zapisom. Za nov osnutek
vzorčne študije v obeh jezikih uporabite spodnje ogrodje in zamenjajte vse
izrecno označene nadomestne vrednosti:

```yaml
---
case_id: "REPLACE_WITH_REGISTERED_CASE_ID"
title: "REPLACE_WITH_SLOVENE_CASE_TITLE"
description: "Navedite raziskovalno vprašanje in kaj lahko bralec v tem primeru preveri."
tags: [case-study]
status: draft
content_standard: showcase-v1
translation_status: paired-draft
audit_record: "release/case-study-audit.md#REPLACE_WITH_CASE_ANCHOR"
---
```

`showcase-v1` označuje zahtevano vsebinsko strukturo, ne opravljene recenzije.
Študije s stanjem `legacy-audited` ne označite kot dokončane zgolj z dodajanjem
naslovov; zapisane vrzeli odpravite z vsebinsko omejenim prispevkom. Pri stanju
`deferred` potrebujete izrecno pojasnilo v revizijskem zapisu. Strojno podprte
osnutke ohranite vidno označene, dokler ni zabeležen ustrezen človeški pregled.

Generator iz avtorskih zapisov in kanoničnih povezav pripravi
`data/case-studies-index.json` ter oba kataloga. Teh izhodov ne urejajte ročno.
Trditve o trenutni dostopnosti in licenci potrebujejo datirano dokazno gradivo
v `release/case-study-audit.md`. Običajno preverjanje ne obiskuje zunanjih
storitev in ne dokazuje, da so še vedno dostopne.

## Raziskovalno vprašanje in predmet raziskave

Navedite, kaj želi projekt spoznati, predstaviti, objaviti ali omogočiti.
Opredelite predmet raziskave, na primer zbirko, izdajo, zgodovinsko razmerje
ali način opisovanja. Pojasnite vprašanje svoje študije primera in ga ločite
od ambicij, ki jih navaja projekt. Določite pregledano različico in obseg
argumenta.

## Predvideni uporabniki ali skupnosti

Opredelite predvidene bralce, raziskovalce, učeče se ali skupnosti in dokaze
za takšno opredelitev. Predvideno občinstvo ustanove ločite od opažene rabe;
ne izmišljajte si podatkov o uporabi in ne predpostavljajte podpore skupnosti.
Pojasnite, kdo lahko prispeva, ugovarja opisu ali zahteva omejitev dostopa
ter čigav jezik, potrebe po dostopnosti ali znanje lahko zasnova izključuje.

## Viri in pokritost

Opišite vključeno in izključeno gradivo, obdobje, geografijo, jezik, žanr in
znane vrzeli. Navedite enoto izbora ter razmerje med majhnim pregledanim
vzorcem in širšo zbirko. Ohranite identifikatorje virov in podatke o njihovem
izvoru. Rezultati iskanja v vmesniku niso nujno popoln popis; povejte, katere
trditve o pokritosti ste lahko preverili.

## Pravice in dostop

Dostop do vmesnika ločite od dovoljenja za prenos, obdelavo, razširjanje ali
pošiljanje gradiva v zunanjo storitev. Preglejte ustrezno licenco, izjavo o
dostopu ali pogodbo ter zapišite njeno mesto, obseg in datum. Ločeno obravnavajte
kodo, izvorne dokumente, izpeljane podatke, slike in dokumentacijo. Prepoznajte
osebne ali občutljive podatke, pristojnosti skupnosti in dostop prek pristojne
ustanove. Če dovoljenje ostaja nejasno, izberite dovoljen način pregleda in
navedite, česa ne morete pregledati ali deliti.

## Podatki in odločitve pri modeliranju

Pojasnite enote, identifikatorje, shemo, kategorije in standarde, s katerimi
viri postanejo podatki. Eni pregledani izvorni enoti sledite do njene
predstavitve. Pokažite, kako model obravnava negotovost, manjkajoče podatke,
nasprotujoča si imena ali spreminjajoče se datume in kje poenostavi pomembne
razlike. Iz imena datoteke s shemo ali obljube v README ne sklepajte, da je
preverjanje že izvedeno; preglejte ustrezna polja, pravila ali dokumentirane
primere.

## Tehnična in institucionalna arhitektura

Opišite javni vmesnik, morebitni repozitorij, podatkovne formate, prenose ali
vmesnike API, pomembne odvisnosti in odgovorne ustanove. Ločite javne,
omejeno dostopne, generirane in gostovane sestavine ter tiste, ki jih je
mogoče rekonstruirati lokalno. Navedite vzdrževalca sistema in dokazno podlago
te navedbe. Repozitorij lahko razkrije le eno sestavino širše storitve;
njegovega obstoja ne enačite s popolno reproducibilno namestitvijo.

## Pregledano dokazno gradivo

Vključite spodnjo tabelo dokaznega gradiva. Različna opažanja zapišite v
ločene vrstice z natančnimi mesti v virih, datumi dostopa in različicami
oziroma identifikatorji commitov, kjer so na voljo. Navodila nadomestite z
dejanskimi zapisi; sama ne poročajo o opravljenem pregledu. Če določene vrste
dokaznega gradiva ni, to izrecno navedite in pojasnite razlog.

| Vrsta dokaznega gradiva | Natančna enota, različica in mesto | Datum in opravljeno dejanje | Ugotovitev in omejitev |
| --- | --- | --- | --- |
| Trditev projekta ali ustanove | Navedite uradno izjavo in razdelek | Zapišite datum branja | Trditev pripišite viru in povejte, ali ste jo neodvisno preverili |
| Opaženo delovanje vmesnika | Določite stran, kontrolnik, poizvedbo in pomembno stanje | Zapišite interakcijo in datum dostopa | Opišite opaženi odziv, ne nevidnega delovanja zaledja |
| Pregledano dokazno gradivo iz repozitorija ali datoteke | Določite datoteko in commit, izdajo ali kontrolno vsoto | Zapišite, kaj ste prebrali ali primerjali | Pojasnite, kaj vsebina datoteke podpira in kaj ostaja nepreizkušeno |
| Rezultat lokalnega zagona | Določite dovoljeni vhod, ukaz, okolje in izhod | Zapišite dejanski datum izvedbe ali navedite, da ni bilo zagona | Poročajte o rezultatu, napaki ali odločitvi za opustitev zagona in njenem razlogu |
| Uredniški sklep | Določite vrstice dokaznega gradiva, na katerih temelji | Zapišite razmislek in morebitni opravljeni pregled | Označite interpretacijo in verjetno alternativno razlago |

Projektna trditev in opaženi rezultat se lahko razlikujeta. Ohranite to
neskladje in njegove posledice za študijo. Zaslonski posnetki potrebujejo
urejene pravice in dostopne opise; sam posnetek ne dokazuje celotnega
delovanja sistema.

## Minimalni postopek dovoljenega pregleda ali zagona

Navedite omejen postopek s predpogoji, dovoljenimi vhodi, natančnimi dejanji,
pričakovanim preverljivim izhodom, korakom preverjanja in pogojem ustavitve.
Določite velikost vzorca in približen čas. Zadostuje lahko ena dokumentirana
poizvedba v vmesniku, primerjava dveh podatkovnih zapisov ali branje sheme
z določeno različico.

Zagon kode ni obvezen. Kadar je smiseln, navedite preizkušeni ukaz, različice
odvisnosti in najmanjši dovoljeni vhod; dejanski lokalni rezultat ločite od
nepreizkušenega projektnega navodila. Če izvedba zahteva manjkajoče podatke,
infrastrukturo, poverilnice ali dovoljenje, pojasnite oviro in ponudite pregled
brez zagona. Ne obidite nadzora dostopa, ne začnite neomejenega spletnega
zajema in iz uspešne majhne demonstracije ne sklepajte o popolni
reproducibilnosti.

## Kje postopek odpove

Dokumentirajte vsaj eno opaženo ali dokazljivo napako, robni primer, dvoumen
zapis, manjkajočo odvisnost ali nedostopno sestavino. Navedite vhod in dokaze,
pričakovano delovanje, dejansko opažanje ter posledico za raziskovalno
vprašanje. Če bi bilo ponavljanje napake neprimerno, pojasnite, katere dokaze
lahko pregledate na dovoljen način. Učno simulacijo izrecno označite;
izmišljene napake nikoli ne predstavite kot opažene pomanjkljivosti projekta.

## Ročni posegi in odprta vprašanja

Pojasnite, kaj morajo ljudje popraviti, uskladiti, interpretirati ali pustiti
odprto. Eni odločitvi sledite od dokazov prek drugih možnih rešitev do njene
posledice. Ohranite nestrinjanje in soglasja ne obravnavajte kot dokaz.
Pri opravljenem pregledu navedite osebo, datum in obseg; nedokončani pregled
jasno označite kot čakajoč. Povejte, katera vprašanja zahtevajo vzdrževalca
projekta, področnega strokovnjaka, predstavnika skupnosti ali imetnika pravic
namesto nepodprte uredniške domneve.

## Možnosti ponovne uporabe in natančni licenčni pogoji

Ločeno navedite zamisli, kodo, sheme, podatke ali učne vzorce, ki jih je
mogoče ponovno uporabiti. Za vsako predlagano uporabo navedite pregledano
licenco ali dovoljenje ter obseg, različico, zahteve glede priznanja avtorstva
in omejitve. Odprto licenco ločite od javne vidnosti, prenosljivega vzorca ali
dostopa prek pristojne ustanove. Nepreverjeno licenco označite kot neznano
in navedite razlog; manjkajoče licence ne razlagajte kot dovoljenje.
Pojasnite, kaj lahko učna vaja pregleda, ne da bi trdili, da je dovoljeno
ponovno objaviti vse projektno gradivo.

## Podprte in nepodprte trditve

Navedite najmočnejšo trditev, ki jo pregledani dokazi upravičujejo, in eno
privlačno trditev, ki je ne podpirajo. Omejitev povežite s pokritostjo virov,
modeliranjem ali globino pregleda. Ločite tehnično delovanje, uspešnost na
omejenem vzorcu in znanstveno interpretacijo. Pojasnite, kako bi drugačen
utemeljen izbor ali odločitev pri modeliranju lahko spremenila rezultat.

## Vzdrževanje in dolgoročna hramba

Datirajte oceno stanja ter navedite različico, odgovorno ustanovo, dostopne
dokaze o vzdrževanju in nerazrešene odvisnosti. Ločite dosegljivo spletno
mesto, aktivnega vzdrževalca in trajno ohranjen znanstveni objekt. Zapise
različic, izvoze, trajne povezave, varnostne kopije ali ureditev hrambe
opišite le na podlagi pregledanih dokazov. Nejasno, arhivirano ali nedostopno
stanje vidno označite; nedaven odziv strani sam po sebi ne dokazuje
dolgoročne hrambe.

## Povezave s priročnikom

Pojasnite, zakaj bralcu pri razumevanju primera pomagata vsaj eno poglavje
in en praktični postopek. Sezname konceptualnih povezav urejajte samo v
`intertextuality.yml`; generator iz tega zemljevida izpelje
`chapter_connections` in `workflow_connections`. V metapodatkih kataloga ali
strani ne vzdržujte konkurenčnih seznamov povezav. V tem razdelku razložite
utemeljitev, trenutne povezave pa naj prikaže generirani blok priročnika.
Če podedovani ali odloženi primer nima ustrezne povezave, v njegov revizijski
zapis vnesite potrebni nadaljnji poseg, namesto da dodate le ohlapno
sorodno stran.

## Omejena učna naloga

Določite eno vprašanje, majhen dovoljeni vhod ali enoto za pregled, časovno
omejitev in konkreten študentski izdelek. Vključite preverjanje vira, eno
zahtevno odločitev in premislek o tem, česa ni mogoče skleniti. Če bi račun,
strošek, manjkajoča odvisnost ali omejeni podatki preprečili sodelovanje,
ponudite dostopno možnost brez zagona. Ocenjujte kakovost dokazov in
utemeljevanja, ne zmožnosti reprodukcije celotnega projekta.

Pred oddajo preverite vsebinsko usklajenost angleške in slovenske strani,
dopolnite datirani revizijski ter metapodatkovni zapis, ponovno ustvarite
kataloga in zaženite `make check` ter `git diff --check`. Uspešna gradnja
preverja strukturo in skladnost, ne pravilnosti virov, etične dopustnosti
ali opravljenega človeškega pregleda.
