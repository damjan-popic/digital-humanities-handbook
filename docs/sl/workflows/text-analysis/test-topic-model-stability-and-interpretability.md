---
title: "Kako preverim stabilnost in interpretabilnost tematskega modela?"
description: "Sestavine NMF povežite med semeni in številom tem, ohranite nestabilnost ter vsako oznako preverite ob dokumentih."
category: "Analiza besedil"
difficulty: "srednje"
time: "75–120 min"
tags: [NMF, tematsko-modeliranje, stabilnost, Jaccard, interpretacija]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Kako preverim stabilnost in interpretabilnost tematskega modela?

!!! warning "Stanje prevoda in učna meja"
    Slovensko besedilo je strojno podprti uredniški osnutek. Dvanajst kratkih
    sintetičnih dokumentov ne more določiti splošne tematske strukture. Namenoma
    nestabilen primer uči primerjanje in zavrnitev, ne vsebinskega sklepanja.

<div class="answer-meta" markdown>
<span>Analiza besedil</span><span>srednje</span><span>75–120 min</span>
</div>

## Kaj želite doseči

Imate sestavine NMF, ki se zdijo razložljive. Ugotoviti želite, ali se sorodni
leksikalni vzorci ohranijo med naključnimi semeni in številom sestavin ter ali
dokumenti podpirajo oznake, ki bi jih radi pripisali.

## Potrebujete

- kopijo repozitorija ali
  [učni paket za preverjanje besedilnih analiz in NLP](../../../assets/downloads/text-nlp-validation-v1.zip);
- pregledovalnik preglednic oziroma Python za neobvezno raziskovanje;
- pojmovne razlike iz poglavja
  [Teme, sentiment in čustva](../../chapters/topics-emotions-classification.md).

Običajna vaja uporablja zamrznjeni rezultat. Paketa scikit-learn ne potrebujete.

## Zamrznjena zasnova

Model uporabi vseh dvanajst sintetičnih dokumentov, ki jih je napisal priročnik.
Vektorizator TF-IDF besedilo pretvori v male črke, uporabi prijavljeni slovenski
seznam nepolnopomenskih besed, ohrani zaporedja najmanj dveh črk ter nastavi
`min_df=1` in `max_df=1.0`. NMF uporabi naključno inicializacijo, multiplikativne
posodobitve, Kullback-Leiblerjevo izgubo, največ 1.000 iteracij, 2, 3 in 4
sestavine ter semena 7, 19 in 31. Za sestavino ohrani osem izrazov in tri
dokumente z najvišjo utežjo. Različice ter kontrolne vsote SHA-256 korpusa in seznama
so v `interim/topics/model-run.json`.

Tako prepustne nastavitve besedišča so utemeljene le za prikaz nestabilnosti v
majhnem naboru. Vsebinska raziskava potrebuje več dokumentov, utemeljene pragove
frekvence, preizkus segmentacije in neodvisno interpretacijo.

## Vhodi in rezultati

| Datoteka | Vloga |
| --- | --- |
| `interim/topics/topic-components.csv` | izrazi, konvergenca in rekonstrukcija vsake izvedbe |
| `interim/topics/topic-documents.csv` | trije najmočneje uteženi dokumenti na sestavino |
| `output/topic-stability.csv` | enolične povezave tem med semeni pri istem številu sestavin |
| `output/topic-count-sensitivity.csv` | najboljša prekrivanja, ki pokažejo razcepe in spoje med 2, 3 in 4 sestavinami |
| `reference/topic-interpretation.sl.csv` | na povedi vezani strojno podprti interpretacijski osnutek, ki čaka na človeški pregled, z začasnimi oznakami in nasprotji |

## Postopek

### 1. Preverite mrežo izvedb

Zaženite `make text-nlp-validation`, nato `topic-components.csv` združite po
`component_count` in `seed`. Vsaka kombinacija mora vsebovati prijavljeno število
sestavin. Identifikatorjev med izvedbami še ne primerjajte, saj so poljubni.

### 2. Pri stalnem številu sestavin povežite semena

Paket pri posameznem številu za poravnavo uporabi seme 7, vendar ga ne razglasi
za pravo rešitev. Osem glavnih izrazov sestavine pretvori v množico in izračuna
Jaccardovo prekrivanje z vsako sestavino semena 19 ali 31:

```text
J(A, B) = |A ∩ B| / |A ∪ B|
```

Preizkusi vsako enolično prireditev in ohrani tisto z največjim skupnim
prekrivanjem; ob popolnem izenačenju izbere leksikografsko manjše zaporedje
identifikatorjev. Odprite `output/topic-stability.csv` ter ročno preverite en
presek in unijo. Vrstica pod učnim pragom ostane označena kot `unstable`.

### 3. Primerjajte število sestavin

Različno število tem ni povezljivo ena proti ena: vzorec se lahko razcepi ali
spoji. Tabela občutljivosti zato za vsako trikomponentno sestavino semena 7
zabeleži najboljše prekrivanje z vsako sestavino dvo- in štirikomponentne izvedbe
istega semena. Več izvornih sestavin lahko izbere isti cilj. To kaže spoj in ni
podvojena vrstica za brisanje.

Navedite navidezni razcep, spoj ali izginotje. Poleg izrazov preglejte dokumente z
visoko utežjo. Manjša rekonstrukcijska napaka pri več sestavinah ne dokaže bolj
veljavne humanistične razlage.

### 4. Preglejte dokumente in odlomke

Odprite `reference/topic-interpretation.sl.csv`. Pri vsaki trikomponentni
sestavini preberite imenovane dokumente v `source/contemporary-sample.csv` ter
nasprotujoči dokument. Začasno oznako primerjajte z dejanskimi odlomki.

Interpretacijski osnutek namenoma zavrne čisto oznako avtorske teme, ker sestavine
mešajo arhivske, muzejske, jezikovne, časopisne in čustvene namige. Predlagate
lahko drugo oznako, vendar navedite identifikatorje in nasprotujoči odlomek.
Osmih besed ne poimenujte brez branja.

### 5. Ločite številsko in interpretativno odločitev

Pripravite kratko tabelo z vrstico za vsak objavljeni vzorec:

| Polje | Vprašanje |
| --- | --- |
| dokaz prekrivanja | Se množice izrazov in močno uteženi dokumenti ponovijo? |
| občutljivost na število | Se vzorec razcepi, spoji ali izgine? |
| izvorni dokaz | Kateri odlomki podpirajo začasno oznako? |
| nasprotje | Kateri odlomek jo oslabi ali spremeni? |
| odločitev | objavi, objavi kot nestabilno ali zadrži |

Visoko prekrivanje lahko ohrani nerazložljivo sestavino. Nizko prekrivanje lahko
še vedno ponudi uporabno pot iskanja. Nobeno brez branja ne poimenuje zgodovinske
teme.

### 6. Preizkusite eno modelsko izbiro

Napovejte učinek spremembe segmentacije, seznama nepolnopomenskih besed,
lematizacije, vrednosti `min_df` ali popravkov OCR. Če zaženete nov model, ga
shranite kot kandidata z novimi metapodatki in ne prepišite zamrznjene izvedbe.
Znova primerjajte vso mrežo, ne le najprivlačnejšega rezultata.

## Neobvezna ponovitev modela

Vzdrževalci lahko namestijo pripeto okolje in zaženejo
`make text-nlp-validation-models`. Ukaz zapiše v novo mapo `.cache/` in zavrne
prepis. Običajni CI modela ne ustvarja; preverja zamrznjene rezultate, dokumentirano provenienco
in deterministične povzetke.

## Rezultat

Napišite beležko, ki navede korpus, segmentacijo, vektorizacijo, nastavitve NMF,
semena, števila, pravilo povezovanja, dokaz prekrivanja, pregledane identifikatorje
dokumentov, nasprotujoči odlomek in odločitev. Vključite nestabilne ali nepovezane
vzorce ter povejte, da majhni sintetični korpus ne določa tematske strukture.

## Preverite se

- Ste primerjali vsaj tri semena in tri števila sestavin?
- Ste teme povezali, namesto da bi primerjali poljubne številke?
- So slabo ujemajoče se in podvojene ciljne povezave še vidne?
- Ste prebrali celotne sintetične dokumente in nasprotje?
- Ste ločili številsko ponovitev od interpretativne veljavnosti?

## Pogoste pasti

- Nastavljeno seme razglasite za dokaz stabilnosti.
- Število sestavin izberete samo po napaki rekonstrukcije.
- Teme povezujete požrešno in pri istem številu ustvarite podvojene povezave.
- Nestabilne teme izbrišete iz poročila.
- Avtorsko temo v metapodatkih obravnavate kot skriti ključ odgovorov.
- Sintetično miniaturo posplošite na zgodovinski diskurz.

## Naloga

Izberite eno izhodiščno sestavino. Sledite njenim povezavam pri drugih semenih in
številu sestavin, nato napišite 250-besedno razlago z dvema podpornima odlomkoma
in enim nasprotjem. Končajte z odločitvijo objavi/nestabilno/zadrži ter navedite,
katero dodatno korpusno gradivo bi odločitev spremenilo.
