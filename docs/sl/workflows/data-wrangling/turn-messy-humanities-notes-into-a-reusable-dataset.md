---
title: "Kako neurejene humanistične zapiske pretvorim v ponovno uporabno zbirko podatkov?"
description: "Iz zapiskov, ki ostanejo povezani z viri, izdelajte dokumentirane odločitve, urejene zapise in preverljivo zbirko, ne da bi izbrisali negotovost."
category: "Urejanje podatkov"
category_id: "data-wrangling"
difficulty: "začetno"
time: "60–90 min"
tags: [podatkovni-model, metapodatki, neurejeni-podatki, provenienca, preverjanje]
---

# Kako neurejene humanistične zapiske pretvorim v ponovno uporabno zbirko podatkov?

<div class="answer-meta" markdown>
<span>Urejanje podatkov</span><span>začetno</span><span>60–90 min</span>
</div>

## Kaj želite doseči

Imate arhivske zapiske, bibliografijo, rodoslovje, kataloški izvoz ali terenska opažanja. Iz njih želite izdelati tabelo za primerjanje, ne da bi dvoumne dokaze spremenili v navidezno urejena dejstva.

Sledili boste verigi **vir → surovi zapis → odločitev → urejeni zapis → rezultat → preverjanje**. Vsaka plast ima drugačno nalogo. Vajo lahko opravite v Excelu, LibreOffice Calcu ali drugi preglednici; programiranje je samo izbirna razširitev.

!!! quote "V eni povedi"
    Ohranite navedbe vira in ponudnika, vsako interpretativno odločitev zabeležite posebej ter pred uporabo urejene tabele preverite identifikatorje, število vrstic in provenienco.

## Potrebujete

- raziskovalno vprašanje in poved, ki opredeljuje enoto ene vrstice;
- izvorne zapiske ali izvoz in natančne oznake mest v viru;
- preglednico ali urejevalnik datotek CSV;
- izjavo o pravicah, zasebnosti in možnosti nadaljnjega razširjanja; ter
- po želji odprto [učno gradivo Arhivsko trenje](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction), zlasti `raw/messy-records.csv`.

Pripravite delovno kopijo. Edine kopije svojih zapiskov ter plasti `source/` in `raw/` v učnem gradivu ne spreminjajte.

## Postopek

### 1. Opredelite vprašanje in vrstico

Vprašanje zapišite nad tabelo. Nato dokončajte poved: »Ena vrstica predstavlja en/eno …« Dokument, oseba, dogodek, izjava in napis pod sliko so različne enote. Če napis poimenuje osem oseb, ga ohranite kot vrstico in dodajte povezano tabelo oseb ali pa vsako razmerje med osebo in napisom zapišite v svoji vrstici. Različnih entitet ne stisnite v eno celico.

Vsakemu zapisu dodelite stabilni identifikator, ki ni odvisen od imena, ki ga boste morda popravili. Natančno mesto v viru — stran, folij, območje slike, signaturo ali spletni naslov — shranite v svojem polju.

### 2. Zamrznite in opišite izvorno plast

Prejeto datoteko ali zapiske ohranite nespremenjene. Zabeležite repozitorij, zbirko, ustvarjalca, identifikator vira, datum dostopa, izjavo o pravicah, ime datoteke in zgoščeno vrednost, kadar je na voljo. Ločite svoj prepis, ponudnikove metapodatke in poznejše sklepanje.

Ustavite se, če ne morete ugotoviti izvora ali dovoljenosti načrtovane uporabe. Urejena tabela brez identitete vira ni ponovno uporaben dokaz.

### 3. Pripravite surovo delovno tabelo

Vrednosti prekopirajte v plast `raw`, ne da bi potiho popravljali zapis, datume ali imena. Koristna polja so:

| Polje | Namen |
| --- | --- |
| `record_id` | stabilni identifikator vrstice |
| `source_locator` | natančna pot nazaj do dokumenta |
| `value_as_printed` | prepis vidnega dokaza |
| `provider_value` | kataloška vrednost ali OCR, če se razlikuje |
| `normalized_value` | poznejša vrednost za raziskovalno rabo |
| `certainty` | točno, izpeljano, približno, nerešeno ali ni relevantno |
| `evidence_note` | utemeljitev in mesto dokaza |
| `synthetic` | oznaka namerno dodane učne motnje |

Z ločenimi oznakami razlikujte neznano, nečitljivo, neustrezno in še nepregledano. Prazna celica tega ne pove. Barva celice ali komentar naj ne bo edini nosilec podatka.

### 4. Preglejte prvi nezadostni rezultat

Prva surova tabela je namenoma nezadostna, ne končni neuspeh. V kopiji s filtriranjem in razvrščanjem poiščite manjkajoče identifikatorje, različne zapise imen, mešane datumske oblike, ponovljene zapise, več vrednosti v eni celici in dvomljive povezave z normativnimi zapisi. Pri vsakem kandidatu preglejte vir. Večina kataloških zapisov ne odtehta samodejno najbližjega dokaza.

Težavo pred ukrepanjem razvrstite: napaka prepisa, razlika v ponudnikovem zapisu, normalizacija, negotova identifikacija, bitno enaka datoteka, ponovljena intelektualna vsebina, ponatis, različica ali namerno dodana učna motnja.

### 5. Ločite samodejna dejanja od ročnih odločitev

Samodejno lahko označite bitno enake datoteke, neveljavne formate, manjkajoče identifikatorje in vrednosti zunaj nadzorovanega seznama. Orodje ne more odločiti, ali je ponatis pomemben, prepoznati osebe po podobnosti ali razložiti arhivske tišine. Vsako opozorilo ročno preverite ob viru. Za vsako vsebinsko spremembo dodajte vrstico:

```text
decision_id, record_id, field, raw_value, clean_value,
action, evidence, decision_by, decision_date, rule_version
```

Izberite ukrep, kot je `correct_from_facsimile`, `normalize_with_rule`, `retain_variant`, `leave_unresolved`, `link_authority`, `reject_authority_candidate` ali `exclude_declared_synthetic_duplicate`. Osebe ne identificirajte zgolj zato, ker je zadetek iskalnika videti verjeten. Ločeno ohranite natisnjeno obliko, kandidatni identifikator, dokaz in status.

Če datum izpeljete iz zapisa »prejšnjo nedeljo«, ohranite izvorno besedilo, normalizirano vrednost, natančnost oziroma gotovost in pojasnilo izpeljave. Če je podprto samo leto, ne izmišljajte meseca in dneva.

### 6. Sestavite urejeno plast in ohranite nerešene primere

Datoteko `cleaned/records.csv` sestavite iz surove tabele in dnevnika odločitev. Surovih vrednosti ne prepisujte. Izvorno besedilo ohranite, kadar je samo predmet raziskave, analitične kategorije pa zapišite v ločena polja. Če več vrstic opisuje isto entiteto, namesto brisanja različnih mest v viru izdelajte tabelo razmerij.

Popolnoma enako dodatno vrstico odstranite šele, ko lahko navedete, zakaj je enaka. Če se kandidati razlikujejo, pred izborom napišite določljivo pravilo prednosti oziroma vključitve in izločitve. Vidni vrstni red razvrščanja ni tako pravilo. Kadar je ponavljanje zgodovinsko pomembno, ohranite razmerja `duplicate_of`, `reprint_of` ali `version_of`.

### 7. Pripravite rezultat, prilagojen vprašanju

Izpeljite samo tabelo ali povzetek, ki ga potrebujete: število po vrstah zapisov, seznam nerešenih identitet, datume po stopnji gotovosti ali pokritost virov po straneh. Rezultat naj bo ločen od urejenih zapisov. Grafikon ali povzetek je interpretacija izbranih polj, ne njihovo nadomestilo.

V učnem gradivu `output/record-summary.csv` povzema vrste urejenih zapisov in stopnje negotovosti. Če se odločitve spremenijo, ga izdelajte znova; ne popravljajte ga ročno.

### 8. Preverite celotno sled

V kontrolni preglednici primerjajte pričakovane in dejanske vrednosti. Preverite, ali:

- so identifikatorji v urejeni tabeli enolični;
- ima vsaka urejena vrstica navedeno mesto v viru;
- ima vsaka spremenjena vrednost zapisano odločitev;
- so sprejeti izvorni zapisi ohranjeni, razen kadar dokumentirano pravilo določa izločitev;
- so sintetične vrstice označene in izključene iz stvarnih rezultatov;
- točne, izpeljane, približne in nerešene vrednosti ostanejo razločljive;
- se vsote v rezultatu ujemajo z urejeno tabelo; ter
- lahko pet izbranih vrstic prek dnevnika odločitev povežete z virom.

Po vsakem delu z dvojniki ponovno preverite ohranjene identifikatorje in število vrstic. Shranite rezultat in datum preverjanja. »Napak ni bilo« ni rezultat, če ne navedete preskusov.

## Rezultat

Oddajte nespremenjeni vir ali navedbo vira, surovo tabelo, dnevnik odločitev, urejene zapise, rezultat za raziskovalno vprašanje, poročilo o preverjanju in seznam znanih težav. Dodajte kratek podatkovni slovar z opredelitvijo polj in dovoljenih oznak.

Postopek je uspešen, če lahko druga oseba pojasni eno vrstico od vira do rezultata, rekonstruira vse vsebinske popravke, ponovi štetje vrstic in prepozna nerešena vprašanja. Preverjeni rezultat učnega gradiva ima osem urejenih zapisov; deveta surova vrstica je ločeno označen sintetični dvojnik.

## Preverite se

- Ali ena vrstica povsod predstavlja isto vrsto stvari?
- Lahko razlikujete svoj prepis, ponudnikovo vrednost in sklepanje?
- Ali vsaka normalizirana vrednost ohrani izvorno obliko in odločitev?
- So identifikatorji stabilni tudi po spremembi imena?
- Ste po obravnavi dvojnikov preverili ohranjene identifikatorje in število vrstic?
- Lahko bralec loči negotovost v dokazih od še nedokončanega dela?

## Pogoste pasti

- Popravite edino kopijo vira ali surove tabele.
- Ponudnikovo kataloško polje obravnavate, kot da je natisnjeno na predmetu.
- Več oseb, datumov ali krajev združite v eni celici.
- Normativni zapis sprejmete, ker je znan ali visoko med zadetki.
- Približno leto spremenite v lažno natančen datum.
- O tem, katera od različnih podvojenih vrstic ostane, odloči vidni vrstni red v preglednici.
- Ponovljeno objavo izbrišete, čeprav raziskujete širjenje besedila.
- Povzetek po spremembi urejene tabele popravite ročno.

## Naloga

Odprite `raw/messy-records.csv` in PDF iz učnega gradiva. Preden pogledate plast `cleaned/`, poiščite štiri označene sintetične motnje, za vsako zapišite odločitev in izdelajte urejeno tabelo. Rezultat primerjajte z `cleaned/records.csv` in `cleaned/decisions.csv`. Pojasnite, zakaj verjetna povezava osebe »Mr. Meker« ostane nerešena in zakaj je leto 1925 pri sliki struge Ljubljanice samo približno.

Nato zasnujte drugo shemo, v kateri ena vrstica predstavlja osebo in ne gradiva z napisom. Opišite, katera vprašanja postanejo lažja in za katera razmerja potrebujete dodatno tabelo.

## Povezana navodila

Konceptualne razlike pojasnjujeta poglavji [Podatki, metapodatki in modeli](../../chapters/data-metadata-models.md) ter [Načrtovanje raziskave](../../chapters/research-design.md). Kadar se več virov ne ujema, nadaljujte z [usklajevanjem nasprotujočih si metapodatkov](reconcile-conflicting-metadata-without-erasing-uncertainty.md), za preverjanje uvoza v programskem vmesniku pa uporabite navodila za [uvoz in čiščenje manjše zbirke v Excelu](import-and-clean-a-small-dataset-in-excel.md).
