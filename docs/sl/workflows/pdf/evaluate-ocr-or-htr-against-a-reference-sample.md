---
title: "Kako ovrednotim OCR ali HTR na referenčnem vzorcu?"
description: "Pripravite preverjeni vzorec, izračunajte CER in WER, razvrstite napake ter preverite, ali spremenijo humanistično trditev."
category: "PDF in OCR"
category_id: "pdf"
difficulty: "začetno"
time: "60–90 min"
tags: [OCR, HTR, CER, WER, prepisovanje, vrednotenje]
---

# Kako ovrednotim OCR ali HTR na referenčnem vzorcu?

<div class="answer-meta" markdown>
<span>PDF in OCR</span><span>začetno</span><span>60–90 min</span>
</div>

## Kaj želite doseči

Imate rezultat optičnega prepoznavanja znakov (OCR) za tisk ali prepoznavanja rokopisnega besedila (HTR) in želite presoditi njegovo uporabnost. Nekaj prepričljivih vrstic ali ponudnikova skupna ocena zaupanja ne zadošča. Rezultat na vnaprej določenem vzorcu primerjajte s človeško preverjenim referenčnim prepisom, izmerite urejevalno razdaljo, razvrstite napake in preizkusite raziskovalno nalogo, ki je odvisna od besedila.

Programiranje ni potrebno. Učno gradivo vsebuje manjši par kandidatnega in referenčnega prepisa ter izračunane rezultate. Pregledate in pojasnite jih lahko z urejevalnikom besedila in preglednico; ukaz za preverjanje je izbirna razširitev za vzdrževalce.

## Potrebujete

- posnetke strani in nespremenjen izvoz prepoznavanja;
- napisana pravila prepisovanja;
- človeško preverjeni referenčni prepis vnaprej določenega vzorca;
- preglednico ali orodje za urejevalno razdaljo, ki navede zamenjave, izpuste in vstavke; ter
- po želji prenesite [ZIP učnega gradiva Arhivsko trenje](../../../assets/downloads/archival-friction-v1.zip): `source/provider-ocr.txt` ohranja natančni izvoz TXT iz dLib, vaja pa uporablja njegovo dokumentirano izpeljanko `raw/provider-ocr.txt` skupaj z `reference/reference-transcription.txt`, `reference/transcription-policy.sl.md`, `output/ocr-evaluation.csv` in `output/ocr-error-audit.csv`; vzdrževalci lahko pregledate tudi [izvorno drevo paketa](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction).

Pred kopiranjem slik ali besedila preverite zapis o viru, pravicah in provenienci. Kandidatni in referenčni prepis hranite v ločenih datotekah.

## Postopek

### 1. Opredelite načrtovano trditev

Zapišite eno uporabo: iskanje osebnega imena, štetje besede, primerjanje besednih pogostnosti, izluščanje datumov ali navajanje odlomka. Naštejte besedilne lastnosti, od katerih je odvisna. Tako izraz »dovolj dobro« postane preverljiv: rezultat lahko zadošča za okvirno iskanje, ne pa za natančen navedek.

### 2. Določite populacijo in vzorec vrednotenja

Navedite zbirko, naslove, datume, vrste dokumentov in način prepoznavanja, za katere naj bi rezultat veljal. Nato izberite strani ali vrstice po pomembnih slojih, kot so več pisav oziroma rokopisnih rok, kakovost posnetka, postavitev, jezik, napisi, tabele in osebna imena.

Del vzorca izberite naključno ali sistematično. Namenski nabor posebno zahtevnih primerov poročajte ločeno. Zapišite pravilo izbora ter število strani, vrstic, referenčnih znakov in besed. Priročen čisti odlomek lahko ponazori računanje, ne more pa oceniti zbirke.

### 3. Shranite in presodite prvi nezadostni rezultat

Prvi rezultat OCR ali HTR obravnavajte kot nezadostnega kandidata, dokler ga ne preizkusite, nato pa ga shranite natanko tako, kot ste ga prejeli. Zabeležite ponudnika, storitev ali program, različico oziroma datum dostopa, identifikator modela, jezikovne in postavitvene nastavitve, izvozni format in datum izvedbe. Vmesniki in gostovani modeli se spreminjajo, zato ohranite prav tisti izvoz, ki ga vrednotite.

Kandidatu dodelite identifikator vzorca in ga povežite z natančnimi koordinatami ali stalno oznako slike. Datoteke ne popravljajte.

### 4. Referenčni prepis pripravite po izrecnih pravilih

Ista območja naj nekdo prepiše in preveri ob sliki. Vnaprej določite:

- vrstni red branja in vključena območja;
- obravnavo prelomov vrstic ter deljenja besed;
- zgodovinski zapis, ligature, okrajšave, velike začetnice in ločila;
- normalizacijo Unicode in presledke;
- oznake za nečitljivo ali manjkajoče besedilo; ter
- ločeno predstavljanje popravkov in normaliziranih oblik.

Zabeležite prepisovalca, pregledovalca, datume in različico pravil. Nesoglasje rešite po pravilih ali ga označite kot nerešeno. Reference potiho ne prilagajajte kandidatu.

### 5. Normalizirajte samo tisto, kar preskus izključuje

Za kandidata in referenco uporabite povsem enaka, vnaprej določena pravila primerjave. Če velikost črk ni pomembna, jo poenotite v obeh; če so ločila pomembna, jih v obeh ohranite. Gradilnik paketa najprej dekodira ohranjeni izvoz iz dLib kot Windows-1250, izbere izvorne vrstice 1–4, združi vrstici v glavi ter strne zaporedne presledke v enako trivrstično zgradbo, kot jo uporablja referenčni prepis. Primerjava nato uporabi Unicode NFC, odstrani začetne in končne presledke ter ohrani druge znakovne razlike. Pri WER besede razmeji s presledki.

Pravila izbora, normalizacije in razmejevanja pojavnic shranite ob rezultatu. CER brez njih je dvoumen. V paketu se izračun CER in WER začne po dokumentiranem izboru in normalizaciji presledkov, zato ne meri izpuščenih presledkov postavitve drugod v izvornem izvozu.

### 6. Samodejno poravnajte in izračunajte

Z najmanjšo urejevalno razdaljo preštejte zamenjave \(S\), izpuste \(D\) in vstavke \(I\) glede na \(N\) referenčnih enot:

\[
\mathrm{stopnja\ napak}=\frac{S+D+I}{N}
\]

Enkrat uporabite znake za CER, drugič pa svoje vnaprej določene besedne pojavnice za WER. Ločeno shranite zamenjave, izpuste in vstavke, njihove vsote ter stopnji. Določite tudi pravilo za izbiro med več enako ugodnimi poravnavami. Paket daje prednost ujemanju, nato zamenjavi, izpustu in vstavku. Vrednosti \(1-\mathrm{CER}\) ne imenujte »natančnost«, ne da bi jo opredelili; zaradi vstavkov je lahko stopnja napak večja od 1.

Vzorec `AF-OCR-P1-INTRO` vsebuje 591 referenčnih znakov in 93 referenčnih besed. Po dokumentirani normalizaciji pri pripravi odlomka deterministična poravnava pokaže 7 zamenjav, 5 izpustov in 0 vstavkov znakov (skupaj 12) ter 7 zamenjav, 2 izpusta in 0 vstavkov besed (skupaj 9). Zato velja:

- CER = `12 / 591 = 0,020305` (približno 2,03 %);
- WER = `9 / 93 = 0,096774` (približno 9,68 %).

Števce in imenovalce vnesite v ločene celice preglednice. Preverite natančna števila S/D/I, nato vsako stopnjo izračunajte kot vsoto sprememb, deljeno z navedenim referenčnim imenovalcem. Rezultat številčno primerjajte po zaokroževanju polovice k sodemu številu na šest decimalk; bajtna enakost datotek CSV ni merilo številčne pravilnosti.

### 7. Ročno presodite napake, ki vplivajo na raziskavo

Za vsako razliko ustvarite vrstico z identifikatorjem in mestom vzorca, referenčnim in kandidatnim nizom, vrsto posega, kategorijo ter verjetno posledico. Uporabite kategorije, kot so zamenjava znaka, diakritika, združevanje in razdruževanje, deljenje ob koncu vrstice, ločilo, ime, število, izpuščeno ali podvojeno območje, vrstni red branja in razlika med pravili prepisovanja. Datoteka `output/ocr-error-audit.csv` vsebuje vseh devet neujemajočih se besednih operacij; njihovo število se ujema z zbirno tabelo. Znakovne S/D/I nastanejo z ločeno poravnavo celotnega niza in niso umetno razdeljene med besedne vrstice.

Izpuste preverite tudi na sliki. Gola besedilna poravnava ne more ovrednotiti napisa, ki manjka v obeh datotekah. Kadar je vzorec dovolj velik, število napak poročajte po slojih.

### 8. Preizkusite nadaljnjo raziskovalno nalogo

Uporabo iz prvega koraka izvedite na obeh prepisih. Pri iskanju primerjajte pravilne in zgrešene zadetke. Pri štetju navedite spremenjene oblike in vsote. Pri izluščanju entitet primerjajte pravilne, zgrešene in lažne entitete. Vsak navedek preverite neposredno ob sliki.

Zapišite odločitev:

- **nadaljujte**, kadar izmerjene napake bistveno ne spremenijo ozke trditve;
- **popravite načrt**, kadar lahko pomaga ciljno popravljanje, drug model, boljša segmentacija ali ožja trditev; ali
- **ustavite se**, kadar manjkajoče strani, nezdružljiva pravila, nepreverljiva referenca ali sistematična napaka onemogočajo primerjavo.

### 9. Ohranite nerešene primere, rezultat in njegove meje

Sliko, kandidatni in referenčni prepis, pravila, metrike, revizijsko tabelo ter odločitev hranite kot povezane, vendar ločene predmete. Dodajte zgoščene vrednosti in seznam znanih težav. Natančno navedite populacijo in sloje, ki jih ocena pokriva ali izpušča, ter način izbora vzorca.

## Rezultat

Oddajte manifest vzorca, zamrznjeni kandidatni prepis, preverjeno referenco, pravila prepisovanja, tabelo CER/WER, revizijo napak, primerjavo nadaljnje naloge in odločitev o nadaljevanju, popravku ali ustavitvi.

Postopek je uspešen, če lahko druga oseba poišče isti vzorec, uporabi navedeno normalizacijo, ponovi števce in imenovalce, na sliki poišče vsaj pet napak ter razume omejenost sklepa. Ujemanje s številkami iz učnega gradiva brez razlage njihovega obsega ne zadošča.

## Preverite se

- Ali vzorec vključuje postavitve in besedilne lastnosti, ki so bistvene za trditev?
- Sta kandidat in referenca ločeni, nespremenjeni datoteki?
- Ste uporabili enako, dokumentirano normalizacijo?
- Lahko pojasnite vsak imenovalec in število posegov?
- Ste poleg zamenjav znakov pregledali izpuščena območja in vrstni red branja?
- Ste primerjali dejanski rezultat nadaljnje analize?

## Pogoste pasti

- Ovrednotite samo čisto ali priročno stran.
- Človeški prepis brez pravil razglasite za nevtralno »resnico«.
- Kandidatni prepis popravite, preden ga ohranite.
- Primerjate datoteki z različnimi pravili za prelome, velikost črk ali Unicode.
- En skupni CER obravnavate kot splošni prag kakovosti.
- Imena, napise ali tabele prezrete, ker je tekoče besedilo dobro prepoznano.
- Sklep iz enega odlomka posplošite na publikacijo, portal ali model.

## Naloga

Z učnim gradivom preverite vsako objavljeno število zamenjav, izpustov in vstavkov znakov ter besed, nato po navedenem pravilu ponovno izračunajte CER in WER. Pet razlik razvrstite, preden svoje delo primerjate z `output/ocr-error-audit.csv`, in v obeh prepisih preizkusite eno iskanje. Rezultat zapišite v dveh povedih: prva naj vsebuje izmerjeno ugotovitev za vzorec `AF-OCR-P1-INTRO`, druga pa mejo, čez katero ugotovitve ne morete posplošiti.

Konceptualno ozadje in vire najdete v poglavju [Besedila, korpusi in OCR](../../chapters/texts-corpora-ocr.md). Veljavne tehnične opredelitve so v [dokumentaciji OCR-D za zagotavljanje kakovosti](https://ocr-d.de/en/spec/ocrd_eval.html) in [smernicah za referenčne prepise](https://ocr-d.de/en/gt-guidelines/trans/) (sprotno posodobljena dokumentacija; dostop 2. septembra 2026).
