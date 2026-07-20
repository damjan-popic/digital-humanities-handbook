---
title: "GIS in prostorska humanistika"
description: "Kako krajevna imena, koordinate, zgodovinski imeniki in prostorska negotovost postanejo zemljevidi, ki interpretacijo podprejo in je ne nadomestijo."
tags: [GIS, kartiranje, geokodiranje, kraj, negotovost]
status: draft
---

# GIS in prostorska humanistika

## Učni cilji

Po tem poglavju boste znali:

- razlikovati med omembo kraja, identiteto kraja in koordinato;
- pojasniti geokodiranje, koordinatne referenčne sisteme, sloje in prostorsko povezovanje;
- zasnovati tabelo krajev, ki ohranja imena, čas in negotovost;
- prepoznati, kako digitalizacija, merilo in kartografska zasnova oblikujejo prostorske trditve;
- zemljevid ovrednotiti kot analitično trditev in ne zgolj ilustracijo.

## Pred začetkom

Dnevnik iz 19. stoletja pravi, da je avtor potoval v *Sveti Peter*. Kateri kraj je mišljen? Odgovor je lahko odvisen od jezika, obdobja, poti, upravnih meja in pisčevih navad. Dodelitev koordinat ni pisarniško opravilo, temveč interpretacija, ki potrebuje dokaze.

## Prostor je več kot zemljepisna širina in dolžina

Humanistični viri kraje omenjajo z imeni, opisi, ustanovami, pokrajinami, potmi in zamišljenimi geografijami. Kraj lahko spremeni ime, meje, funkcijo in politično pripadnost. Eno ime lahko označuje več lokacij, ena lokacija pa ima več imen.

Ločeno hranite:

- **omembo**, kot se pojavi v viru;
- **normalizirano ime** za iskanje ali prikaz;
- **entiteto kraja** s stabilnim projektnim identifikatorjem;
- **geometrijo**, uporabljeno na zemljevidu;
- **časovno obdobje**, za katero identifikacija velja;
- **dokaz in stopnjo gotovosti**, ki povezavo podpirata.

Ločitev omogoča popravek identifikacije, ne da bi spreminjali prepis vira.

## Imeniki krajev in geokodiranje

**Imenik krajev** je strukturiran vir z identifikatorji, imeni, tipi, koordinatami ter pogosto zgodovinskimi ali upravnimi podatki. **Geokodiranje** naslov ali krajevni niz poveže s prostorsko lokacijo.

Komercialni in sodobni geokodirniki so prilagojeni današnjim naslovom. Zgodovinska imena lahko tiho povežejo s sodobnimi središči, izberejo najbolj naseljeni kraj ali odpovejo pri narečnih in večjezičnih oblikah. Zabeležite storitev, datum, poizvedbeni niz, vrnjeni identifikator, oceno in ročno odločitev. Kjer licenca dopušča, rezultate shranite, da projekt ni odvisen od spremenljivega zunanjega odziva.

## Geometrija in negotovost

Točka ni vedno prava predstavitev. Zgodovinska pokrajina lahko zahteva poligon, potovanje črto, negotova lokacija pa več kandidatov ali približno območje.

Uporabna polja so:

| mention_id | place_id | geometry_type | certainty | start_date | end_date | source |
|---|---|---|---|---|---|---|
| m18 | p204 | point | verjetno | 1849 | 1851 | diary_7_f12 |

Ne izmišljajte si natančnosti. Koordinata s šestimi decimalkami namiguje na metrsko gotovost, čeprav vir morda določa le dolino. Negotovost predstavite z razponi, stopnjami gotovosti, več kandidati, pasovi ali opisnimi opombami ter konvencijo pojasnite v legendi.

## Koordinatni referenčni sistemi

Koordinate razlagamo znotraj **koordinatnega referenčnega sistema** (CRS). Geografske koordinate, kot je WGS 84, uporabljajo zemljepisno širino in dolžino; projicirani sistemi zemeljsko površje preslikajo na ravnino za določena območja in meritve.

Zemljevid je lahko videti verjeten tudi ob neujemajočih se sistemih slojev. Za vsak prostorski nabor zabeležite CRS. Pred merjenjem razdalje ali površine sloje zavestno pretvorite in izberite projekcijo, primerno obsegu območja in analitičnemu cilju.

## Sloji in prostorsko povezovanje

GIS informacije organizira v sloje: kraje, meje, ceste, rabo tal, dogodke, dokumente ali demografske kazalnike. **Prostorsko povezovanje** zapise poveže po razmerjih, kot so znotraj, seka ali najbližje.

Tako lahko vprašamo:

- Katera pisma so nastala znotraj zgodovinske meje?
- Katera arheološka najdišča ležijo blizu rimske ceste?
- Katera narečna opazovanja sodijo v današnje in zgodovinske upravne regije?

Razmerje je smiselno le toliko, kolikor so smiselne geometrije in časovna uskladitev. Povezava dogodka iz leta 1850 z občinsko mejo iz leta 2026 lahko odgovori na upravno priročnost, ne na zgodovinsko vprašanje.

## Zemljevidi so argumenti

Vsak zemljevid izbere obseg, merilo, projekcijo, razrede, simbole, oznake in izpuste. Točke lahko prikrijejo gostoto, veliki poligoni vizualno prevladajo, razredi barv lahko napihnejo prag, manjkajoči podatki pa so videti kot odsotnost.

Znanstveni zemljevid naj navede:

- vir podatkov in pokritost;
- enoto analize;
- časovni obseg;
- prostorsko ločljivost in negotovost;
- pravila pretvorbe in razvrščanja;
- manjkajoče ali izločene zapise;
- ali je zemljevid raziskovalen, opisen ali inferenčen.

Toplotnega zemljevida ne uporabite samo zato, ker je dramatičen. Ocena gostote uvede širino pasu in robne odločitve, ki jih je treba razložiti.

## Besedila in prostorsko izluščanje

Za kartiranje krajev v besedilih postopek navadno združi razpoznavanje imenskih entitet, ročni pregled, razreševanje identitet in geokodiranje. Frekvenca omemb ni prisotnost, bivanje ali pomembnost. Časopis lahko pogosto omenja prestolnico, ker je politično središče; potopis lahko poimenuje le nenavadne postanke, domače kraje pa izpusti.

Vsako točko povežite z odlomkom in dokumentom. Bralec lahko tako preveri, ali je kraj dobeseden, metaforičen, poročan, zamišljen ali negotov.

## Razdelan primer: literarna mobilnost

Predpostavimo, da raziskujemo gibanje v romanu in njegovem zgodovinskem kontekstu.

1. Določimo, ali je enota omemba, prizor, odsek poti ali prisotnost literarnega lika.
2. Izluščimo možne krajevne omembe in ohranimo identifikatorje odlomkov.
3. Imena razrešimo z obdobju primernimi imeniki in strokovnimi viri.
4. Dodelimo geometrijo in gotovost, ne da bi prisilno razrešili dvoumne primere.
5. Ločimo pripovedovane, spominjane, zamišljene in zgolj omenjene kraje.
6. Poti zgradimo le, kjer besedilo podpira zaporedje in gibanje.
7. Literarno geografijo previdno primerjamo z zgodovinskim prometom ali mejami.
8. Objavimo zemljevid s filtri, izvornimi odlomki in legendo negotovosti.
9. Odsotnosti razlagamo kot možne pripovedne izbire in ne samodejen dokaz nepomembnosti.

## Vaja

Iz besedila ali seznama dediščine pripravite tabelo desetih krajev. Ohranite izvorno obliko, normalizirano ime, identifikator, koordinate ali geometrijo, datum, gotovost, dokaz in opombe. Tabelo prikažite na zemljevidu, nato poiščite tri načine, kako bi zemljevid lahko zavedel bralca.

## Refleksija

- Zemljevid predstavlja omembe, dogodke, ljudi, dokumente ali sklepano gibanje?
- Katera zgodovinska meja ali odločitev o krajevnem imenu je najbolj sporna?
- Kaj je videti prazno zato, ker vaši viri ali geokodirnik tega ne pokrivajo?

## Povzetek

Prostorska humanistika dokaze o krajih pretvori v povezane, časovno občutljive in interpretabilne prostorske podatke. Omemba ni koordinata, sodobno geokodiranje ni zgodovinska identifikacija, zemljevid pa ni nevtralno okno. Imeniki, stabilni identifikatorji, koordinatni sistemi, provenienca in izrecna negotovost prostorske prikaze spremenijo v uporabne humanistične argumente.
