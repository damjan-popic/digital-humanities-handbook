---
title: "Kako georeferenciram in preverim zgodovinski zemljevid v QGIS?"
description: "Georeferencirajte zgodovinski načrt z dokumentiranimi pravicami, izločite točke za preverjanje in poročajte o negotovosti."
category: "Kartiranje"
category_id: "Mapping"
difficulty: "srednje"
time: "90–120 min"
tags: [QGIS, georeferenciranje, oslonilne-točke, CRS, prostorska-negotovost]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Kako georeferenciram in preverim zgodovinski zemljevid v QGIS?

<div class="answer-meta" markdown>
<span>Kartiranje</span><span>srednje</span><span>90–120 min</span>
</div>

Strojno podprt prevodni osnutek; potreben je strokovni jezikovni pregled.

## Kaj želite doseči

Preverite, ali zgodovinski načrt in današnji referenčni sloj iste pojave umestita dovolj skladno za vaše raziskovalno vprašanje. Majhna napaka prileganja ni potrdilo o točnosti. Poglavje [GIS in prostorska humanistika](../../chapters/gis-spatial-humanities.md) loči prileganje, neodvisno preverjanje in zgodovinsko interpretacijo.

## Potrebujete

Razpakirajte [spremljevalni ZIP](../../../assets/downloads/contested-models-v1.zip) s Kochovim načrtom Ljubljane iz leta 1910, opombami o pravicah in predpomnjenimi današnjimi koordinatami. dLib sken označuje kot javno domeno; strukturirane koordinate izvirajo iz podatkov Wikidata pod CC0. Natančno navedbo in omejitve preberite v `rights-and-provenance.sl.md`.

Za številsko pot uporabite Python 3.10+, za rastrski del pa QGIS. Koraki vmesnika sledijo [priročniku QGIS 3.40](https://docs.qgis.org/3.40/en/docs/user_manual/managing_data_source/georeferencer.html). Številski pilot je preizkušen; postopek v grafičnem vmesniku še nima dokumentiranega pregleda v QGIS. Zabeležite nameščeno različico in razlike menijev. Različice 3.40 ne obravnavajte kot najnovejše.

Vzdrževalci naj izpolnijo `release/issue-25-qgis-review-checklist.md`, ki natančno
določa polja za okolje, točke, odstopanja, vizualni pregled in odločitev. Oznaka
»nedokončano« ne dokazuje, da je bil postopek izveden.

## Postopek

### 1. Ponovite izhodiščni izračun

```bash
python run.py --output output-first
```

Preglejte `gcp-residuals.csv`, `gcp-leave-one-out.csv` in `current-landmarks.csv`. Vhodi uporabljajo izvorno sliko velikosti 5747 × 7287 pikslov. Drugače obrezana ali spremenjena kopija potrebuje nove slikovne izbire. Šest priloženih točk so prvi kandidati, ne potrjene kontrole.

### 2. Pred prilagoditvijo preverite pojave

Odprite `source/ljubljana-1910.jpg`. Vsakega kandidata primerjajte z identifikatorjem Wikidata, koordinatami in opisom v `input/landmarks.csv`. Središče mostu, središče stavbe in geodetski vogal niso zamenljivi. G5 in G6 izločite za neodvisno preverjanje; ne vključite ju v izračun transformacije, da bi izboljšali ujemanje.

V QGIS odprite Georeferencer v meniju Layer in naložite sliko. Naložite ustvarjeno datoteko `output-first/ljubljana-1910.points`. Njene izvorne koordinate y so negativne po konvenciji georeferencerja; vhodni CSV meri pozitivni y navzdol po sliki. Preverite, ali so točke na predvidenih pojavih. Če niso, delo ustavite in zabeležite neskladje.

### 3. Nastavite in dokumentirajte transformacijo

Izberite Polynomial 1, torej afino transformacijo, ciljni sistem EPSG:3794, prevzorčenje po najbližjem sosedu in novo izhodno datoteko GeoTIFF. G1–G4 naj bodo vključene, G5–G6 izključene. Shranite oslonilne točke in nastavitve ter zaženite georeferenciranje. Izvorne slike ne spreminjajte.

Stolpci odstopanj v ustvarjeni datoteki points vsebujejo začetne ničelne nadomestne vrednosti, ne izmerjenih napak. Na novo izračunana odstopanja QGIS primerjajte šele po preverjanju enot in nastavitev. Prevzorčenje spremeni videz pikslov, ne veljavnosti identifikacije objekta.

### 4. Primerjajte s sodobnim slojem

Dodajte `current-landmarks.csv` kot točkovni sloj ločenega besedila: x=`target_e_m`, y=`target_n_m`, sistem EPSG:3794. Prikažite ga nad izhodnim rastrom. Preglejte vseh šest točk, posebej izključeni postajo in stolnico. Shranite projekt in po potrebi referenčni sloj izvozite v GeoPackage. Oddaljena kartografska podlaga ni potrebna.

| Številsko izhodišče | RMSE v metrih |
|---|---:|
| Štiri uporabljene kontrole | 15,231 |
| Dve neodvisni točki | 220,063 |

Neodvisni rezultat ne podpira trditve o približno 15-metrski točnosti. Preverite razporeditev: izločitev zahodne kontrolne točke povzroči 1.090,241 m odstopanja pri tej točki. To je opozorilo analize občutljivosti, ne priporočena položajna toleranca.

### 5. Neskladje preglejte, ne prikrijte

Raziščite eno neuspešno točko. Je bila izbrana napačna stavba, se je referent spremenil ali je današnja koordinata preveč groba? Zapišite staro in popravljeno točko, dokaz ter razlog. Popravljeni CSV in rezultate shranite pod novimi imeni. Pred spremembo in po njej primerjajte iste neodvisne kontrole; neugodne točke nikoli neopazno ne odstranite.

Pri prilagoditvi vaje varujte občutljive lokacije. Kjer je utemeljeno, jih posplošite ali omejite dostop. Ohranite varno revizijsko sled brez objave varovanih koordinat.

## Rezultat

Oddajte navedbo vira, pravice, različico QGIS, sistem, transformacijo, prevzorčenje, točke z oznakami vključitve, GeoTIFF in projekt, kadar sta na voljo, tabelo odstopanj ter dnevnik neskladij. Dodajte besedilni opis prekrivanja. Tabele omogočajo številsko alternativo, ne pomenijo pa opravljenega rastrskega oziroma vmesniškega pregleda.

## Preverite se

Lahko druga oseba prepozna isti pojav v obeh virih? So neodvisne kontrolne točke res izključene iz izračuna transformacije? So enote metri in ne piksli? Ali trditev prestane neodvisni rezultat?

## Pogoste pasti

Dodelitev sistema namesto transformacije koordinat; spremenjena velikost skena ob starih slikovnih točkah; štetje začetnih ničel kot uspešnih kontrol; in razlaga gladkega prekrivanja kot dokaza zgodovinske točnosti.

## Naloga

Preverite eno uporabljeno in eno izločeno točko. Oddajte nespremenjeno izhodišče ter utemeljeni popravek ali dokumentirano odločitev, da primer ostane odprt. Pojasnite, zakaj sintetične meje ne smete prikazati kot avtentične ljubljanske meje.
