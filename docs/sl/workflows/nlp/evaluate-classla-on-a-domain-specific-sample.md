---
title: "Kako CLASSLA ovrednotim na domensko specifičnem vzorcu?"
description: "Napovedi povedi, pojavnic, lem, oblikoslovja, odvisnosti in entitet preverite ob dokumentirani slovenski referenci."
category: "NLP"
difficulty: "srednje"
time: "60–90 min"
tags: [CLASSLA, slovenščina, preverjanje, CoNLL-U, analiza-napak]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Kako CLASSLA ovrednotim na domensko specifičnem vzorcu?

!!! warning "Stanje prevoda"
    Slovensko besedilo je strojno podprti uredniški osnutek. Pred formalno
    objavo potrebuje vsebinski in jezikovni pregled strokovnjaka za slovenščino.

<div class="answer-meta" markdown>
<span>NLP</span><span>srednje</span><span>60–90 min</span>
</div>

## Kaj želite doseči

Ugotoviti želite, ali je jezikoslovna anotacija uporabna za določeno
humanistično vprašanje, ne pa potrditi splošnega ugleda procesne verige. Eno
zamrznjeno izvedbo CLASSLA boste primerjali s strojno podprtim slovenskim
referenčnim osnutkom, ki čaka na človeški pregled, na sodobnem besedilu,
zgodovinskem prepisu in ponudnikovem OCR. Za
vsako plast boste navedli poseben imenovalec in napake povezali z njihovim
verjetnim učinkom na interpretacijo.

!!! quote "V eni povedi"
    Plast, ki jo uporablja vaša trditev, ovrednotite na gradivu z ustrezno
    zahtevnostjo in pred zaupanjem meri preberite napake.

Gre za diagnostično vajo. Štiri izbrane povedi ne ocenjujejo splošne kakovosti
CLASSLA.

## Potrebujete

- kopijo repozitorija ali
  [učni paket za preverjanje besedilnih analiz in NLP](../../../assets/downloads/text-nlp-validation-v1.zip);
- Python 3.12 za ponovno gradnjo determinističnih tabel;
- pregledovalnik preglednic ali urejevalnik besedila;
- poznavanje plasti iz poglavja
  [Jezikoslovna anotacija in CLASSLA](../../chapters/linguistic-annotation-classla.md).

Namestitev CLASSLA in prenos modelov **nista** potrebna. Paket vsebuje
zamrznjeni rezultat in natančne metapodatke o izvedbi.

## Vhodi in rezultati

| Vloga | Datoteka | Pomen |
| --- | --- | --- |
| pravila izvlečka | `source/extraction-registry.json` | določa izvorno plast, zapis in izbirnik povedi |
| raziskovalni vhodi | `raw/annotation-samples.csv` | navaja normalizirano besedilo ter kontrolne vsote SHA-256 |
| referenčni osnutek | `reference/classla/*.conllu` | razkrije sporne strojno podprte odločitve, ki čakajo na človeški pregled |
| vzročne odločitve | `reference/classla-causal-decisions.csv` | med izvornimi plastmi loči neposredno nestrinjanje od verjetnega vzroka |
| modelske napovedi | `interim/classla/*.conllu` | nespremenjeno ohrani zamrznjeno izvedbo |
| identiteta izvedbe | `interim/classla/model-run.json` | navaja paket, procesorje, okolje, vire in kontrolne vsote SHA-256 |
| mere | `output/classla-evaluation.csv` | za vsako plast razkrije števec, imenovalec in upravičeni nabor |
| nestrinjanja | `output/classla-error-log.csv` | razlike v oznakah poveže z družino napake in tveganjem |

Pred interpretacijo preberite `rights-and-provenance.sl.md`,
`data-dictionary.sl.md` in `reference/classla-reference-policy.sl.md`.

## Postopek

### 0. Napišite razslojeni vzorčni in odločitveni načrt

Pred ogledom modela določite raziskovalno operacijo, potrebne plasti, vzorčni
okvir in verjetne skupine težavnosti. Po potrebi navedite ciljna števila po
žanru, obdobju, stanju vira, kodnem preklapljanju, nestandardnem jeziku,
krajšavah in imenih. Določite pregled reference, shranjevanje nestrinjanj in
nerazrešenih primerov ter nadaljnje število, ki ga boste ponovno izračunali.

Vnaprej določite merilo za uspeh, pogojni uspeh ali neuspeh, vezano na trditev.
Raziskava govorcev je na primer neuspešna, če napaka osebka spremeni vrstni red
skupin; pogojno uspešna, če ročno pregledate vse kandidate; za raziskovalno
iskanje pa uspešna ob zadostnem priklicu po prijavljenem pragu. Ne izmišljajte si
univerzalnega praga CLASSLA.

### 1. Paket zgradite brez prenosa modelov

V korenu repozitorija zaženite:

```bash
make text-nlp-validation
```

Ukaz uporablja standardno knjižnico Python. Izloči prijavljene odlomke, preveri
kontrolne vsote SHA-256 zamrznjenih datotek, izračuna rezultate, pripravi študentski
ZIP in preveri njegovo kontrolno vsoto. Sprememba vira, modelskega artefakta ali
pričakovane vrednosti mora povzročiti vidno napako, ne prikrite posodobitve.

### 2. Preglejte razliko med izvornimi plastmi

Odprite `raw/annotation-samples.csv`. Preverite, da sta sodobni vrstici označeni
kot sintetični. Zgodovinski prepis in ponudnikov OCR kažeta na različni datoteki,
vendar si delita identifikator arhivskega zapisa. Gre za besedilni plasti istega
časopisnega odlomka in ne za dva dokumenta.

Zgodovinski besedili primerjajte znak za znakom. V OCR poiščite zlepljeni
`narodain`, poškodovani obliki `stavovske` in `kultrunega` ter oziralni `i`.
Surove vrstice ne popravljajte. Referenčna pravila razložijo, katere oblike FORM
ostanejo opažene in katera meja besede ali lema izhaja iz preverjenega prepisa.

### 3. Določite zamrznjeno izvedbo

Odprite `interim/classla/model-run.json` in odgovorite:

- Kateri različici CLASSLA in Pythona sta ustvarili datoteke?
- Kateri procesorji so se izvedli in ali je bil uporabljen grafični procesor?
- Katere kontrolne vsote SHA-256 določajo normalizirane vhode in rezultate?
- Kateri SHA-256 in velikosti določajo lokalne modelske vire ter kdaj je bil
  zapisan manifest virov?
- Kateri posnetek okolja določa Python, Torch, NumPy, SciPy, scikit-learn,
  CLASSLA, Stanza in Obeliks?

Metapodatki identificirajo eno izvedbo. Modelske napovedi ne spremenijo v
referenčno oznako in ne jamčijo enakega vedenja prihodnjih namestitev.

### 4. Pred računanjem preberite eno poved

Datoteki `reference/classla/TNLP-AF-OCR.conllu` in
`interim/classla/TNLP-AF-OCR.conllu` postavite drugo ob drugo. Začasno prezrite
komentarje in preberite deset stolpcev CoNLL-U. Poiščite referenčno večbesedno
pojavnico `27-28 narodain` in njene sestavne besede. Nato poiščite `i` ter
primerjajte FORM, LEMMA, UPOS, HEAD in DEPREL.

Vrnite se k povedi in pojasnite, kako napaka razpoznavanja postane leksikalno ter
odvisnostno nestrinjanje. S tem mera ostane povezana z virom.

### 5. Ponovno izračunajte imenovalec ene plasti

Odprite `output/classla-evaluation.csv` ter izberite vzorec in plast. Preverite:

```text
value = numerator / denominator
```

S stolpcem `eligible_rule` pojasnite, kaj je vstopilo v imenovalec. Lema, UPOS in
oblikoslovje uporabljajo besedne pojavnice z enakovredno poravnavo. Odvisnostne
mere uporabljajo poravnane skladenjske besede, katerih referenčna glava je prav
tako poravnana. Preciznost in priklic NER namenoma uporabljata različna
imenovalca. Vstavki in izpusti pojavnic ne smejo izginiti v odstotku druge plasti.
Imenovalec uskladite z izrecnimi števili referenčnih, napovedanih, poravnanih,
zamenjanih, vstavljenih, izpuščenih in izločenih enot. `excluded` ni splošni
preostanek: izločitve na vsaki strani in pravilo izločitve so navedeni ločeno.

Popravljene vrstice odvisnostnega vrednotenja morajo vsebovati:

| Vzorec | UAS | LAS |
| --- | ---: | ---: |
| `TNLP-CLEAN-01` | 11/11 | 11/11 |
| `TNLP-CLEAN-02` | 9/9 | 9/9 |
| `TNLP-AF-REF` | 50/52 | 50/52 |
| `TNLP-AF-OCR` | 43/46 | 42/46 |

Mere obravnavajte kot ujemanje s sedanjim strojno podprtim osnutkom in ne kot
oceno točnosti glede na človeško razsojeno referenco.

### 6. Dnevnik napak preberite po družinah

`output/classla-error-log.csv` filtrirajte najprej po `sample_id`, nato po
`error_family`. Za dve vrstici zapišite:

1. izvorno obliko in plast;
2. referenčno ter napovedano vrednost;
3. neposredno nestrinjanje med modelom in referenco;
4. verjetni vzrok, vključno s podatkom, ali se pojavi tudi v referenčnem
   prepisu;
5. raziskovalno operacijo, ki bi se lahko spremenila.

Napako razpoznavanja vira ločite od odziva označevalnika. Če trditev obravnava
le natančne razpone krajev, je nestrinjanje o lemi morda nepomembno. Pri
osebkih stavkov pa je odvisnostno nestrinjanje istega odlomka osrednje.
V `reference/classla-causal-decisions.csv` preverite ponavljajoče se primere v
prepisu in OCR. Nestrinjanja, ki se pojavijo v obeh plasteh, denimo vseh pet
polj za `vse` v vsakem zgodovinskem vzorcu, ni povzročil OCR.
Ponovno ustvarjeni dnevnik vsebuje 24 nestrinjanj: 14 ujemajočih se primerov med
plastmi (deset polj za `vse` in štiri odvisnostna polja za `stranko`) ter deset
primerov, povezanih s stanjem ponudnikovega OCR.

### 7. Plasti primerjajte brez pretiranega sklepa

Vrstice vrednotenja združite po `stratum`. Opišete lahko nestrinjanja v teh
izbranih sodobnih, zgodovinskih in OCR-vzorcih. Ne smete sklepati o povprečni
napaki sodobne ali zgodovinske slovenščine. Vzorec je majhen, namenski in deloma
izbran tako, da pokaže odpoved.

Oblikujte omejeno odločitev, na primer: »Pred združevanjem ročno preglejte vsa
osebkova razmerja v ponudnikovem OCR.« Navedite preverjanje, ki bi ga potrebovali
za posplošitev.

### 8. Uporabite načrtovano merilo in ohranite nerazrešene primere

Z `output/downstream-consequences.csv` primerjajte samodejno in referenčno
število ter uporabite pravilo iz koraka 0. Zapišite `pass`, `conditional_pass`
ali `fail`, opažena števila, zahtevani poseg in obseg. Dodajte tabelo nerazrešenih
primerov z identifikatorjem vzorca, lokatorjem vira, plastjo, možnimi analizami,
potrebnim dokazom in odločitvijo o izločitvi, ročnem pregledu ali ohranjeni
negotovosti. Majhen imenovalec ali resnično jezikoslovno nestrinjanje naj ne
postane gotova oznaka zgolj zato, da končate vajo.

## Neobvezna osvežitev modela za vzdrževalce

Ponovni zagon je ločen od vaje, ker prenaša velike vire in se med izdajami lahko
spremeni:

```bash
python3.12 -m venv .venv-text-nlp
source .venv-text-nlp/bin/activate
python -m pip install -r teaching-data/text-nlp-validation/requirements-text-nlp.txt
make text-nlp-validation-models
```

Ukaz zapiše novega kandidata v `.cache/` in zavrne prepis potrjene izvedbe.
Vzdrževalec mora primerjati metapodatke in anotacije, pregledati vsako spremembo
ter pričakovane vrednosti posodobiti zavestno. Običajni CI modelov ne prenaša.

## Rezultat

Pripravite kratko poročilo o preverjanju, ki vsebuje razslojeni vzorčni načrt,
identifikator zamrznjene izvedbe, preverjeni imenovalec ene plasti, dve analizi
napak s povezavo do vira, ponovno izračunano nadaljnjo posledico, odločitev
`pass`, `conditional_pass` ali `fail` ter tabelo nerazrešenih primerov. Končajte
z omejeno trditvijo in pogoji za njen ponovni pregled. Rezultatov v paketu ne
spreminjajte, razen pri dokumentirani vzdrževalski osvežitvi.

## Preverite se

Postopek ste opravili, ko lahko:

- vsak vzorec povežete z izvorno potjo in vrednostjo SHA-256;
- pojasnite, zakaj je strojno podprti referenčni osnutek odprt za nestrinjanje
  in še čaka na človeški pregled;
- eno objavljeno mero ponovno izračunate iz njenih števcev;
- pojasnite razliko med imenovalcema za odvisnosti in NER;
- dve napaki povežete s konkretnim interpretativnim tveganjem; in
- oblikujete sklep znotraj omejitev vzorca.

## Pogoste pasti

- Primerjate odstotke, vendar prezrete neenake ali zelo majhne imenovalce.
- Poškodbo OCR imenujete napaka CLASSLA ali prezrete njeno širjenje skozi model.
- Ocenite le zlahka poravnane pojavnice, izločenih pa ne navedete.
- Številne oznake `O` razglasite za dokaz dobrega razpoznavanja entitet.
- Med običajno vajo ali CI zamenjate zamrznjeno izvedbo.
- Izvorno plast popravite prikrito, namesto da bi dokumentirali drugo plast.
- Štiri namenske povedi posplošite na jezik, obdobje ali žanr.

## Naloga

Za svoje vprašanje načrtujte 30-povedni referenčni vzorec. Določite stratume,
pravilo vzorčenja, potrebne anotacijske plasti, navodila pregledovalcu, postopek
ob nestrinjanju, mere, imenovalce in odločitev, ki bi jo sprožil posamezni
rezultat. Zapišite etično ali licenčno omejitev in razlog, zakaj vzorec kljub
temu morda ne bi bil reprezentativen.
