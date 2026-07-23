---
title: "Podatkovne zbirke in SQL"
description: "Kako relacijsko modeliranje ljudi, besedila, kraje in dogodke spremeni v poizvedljive humanistične podatke, ne da bi izbrisalo negotovost."
tags: [podatkovna-zbirka, SQL, relacijski-model, identifikatorji, provenienca]
status: draft
---

# Podatkovne zbirke in SQL

## Učni cilji

Po tem poglavju boste znali:

- razlikovati med preglednico in relacijsko podatkovno zbirko;
- prepoznati entitete, lastnosti, razmerja, ključe in kardinalnosti;
- zasnovati normalizirano shemo za manjši humanistični projekt;
- napisati osnovne poizvedbe SQL za filtriranje, povezovanje, združevanje in štetje zapisov;
- izrecno predstaviti negotovost, provenienco in spreminjajoče se interpretacije.

## Pred začetkom

Predstavljajte si tabelo s stolpci `avtor_1`, `avtor_2`, `avtor_3`, `kraj_1`, `kraj_2` in več celicami, v katerih so imena ločena z vejicami. Morda je videti priročno, toda kako bi zanesljivo vprašali, kateri avtorji so objavljali v istem kraju, ali eno ime popravili povsod? Struktura določa, katera vprašanja ostanejo mogoča.

Shema je model izbranih entitet in razmerij, ne nevtralna posoda. Poglavje [Modeli, dokazno gradivo in interpretacija](models-evidence-interpretation.md) pomaga razkriti te odločitve, poglavje [Infrastrukture digitalne humanistike](critical-infrastructures.md) pa je pomembno, kadar so dostop do zbirke, identifikatorji ali vzdrževanje odvisni od zunanje storitve.

## Podatkovna zbirka je trditev o svetu

Podatkovna zbirka ne hrani samo dejstev. Njena shema določi, katere vrste stvari v projektu obstajajo in kako so povezane. Pri projektu literarne zgodovine lahko modeliramo osebe, dela, izdaje, založnike, kraje in dogodke. Že ločitev *dela* od *izdaje* je interpretativna odločitev.

Relacijsko modeliranje sprašuje:

- Kaj je ena prepoznavna stvar?
- Katere lastnosti ji pripadajo?
- Ali ima lahko ena stvar več vrednosti iste lastnosti?
- Katera razmerja povezujejo entitete?
- Kateri dokaz podpira posamezno trditev?

Shema naj sledi raziskovalnim potrebam in hkrati ostane dovolj izrecna, da jo lahko popravimo.

## Tabele, vrstice, stolpci in ključi

Relacijska zbirka zapise hrani v tabelah:

- **vrstica** predstavlja en zapis;
- **stolpec** predstavlja eno opredeljeno lastnost;
- **primarni ključ** enolično določi vrstico;
- **tuji ključ** kaže na vrstico v drugi tabeli.

Kot ključe uporabljajte stabilne notranje identifikatorje in ne imen. Imena se spreminjajo, podvajajo in zapisujejo različno. `person_id = 1042` lahko ostane stabilen, medtem ko zbirka hrani več oblik imena in njihove vire.

## Razmerja in kardinalnost

Pogosta razmerja so:

- ena proti mnogo: en časopis ima veliko številk;
- mnogo proti mnogo: veliko oseb sodeluje pri veliko delih;
- ena proti ena: redkejše in pogosto znak, da bi lahko dve tabeli združili.

Razmerje mnogo proti mnogo zahteva povezovalno tabelo. Namesto stolpcev `avtor_1`, `avtor_2` in `avtor_3` uporabimo tabelo `sodelovanje` s polji `person_id`, `work_id`, vloga, vrstni red in dokaz. Razmerje samo lahko tako nosi zgodovinsko pomembne podatke.

## Normalizacija brez dogmatizma

Normalizacija zmanjša podvajanje in protislovne popravke. Uporabno osnovno pravilo je: ena celica, ena vrednost; ena tabela, ena vrsta entitete; vsako dejstvo shranimo tam, kamor sodi.

Naslova založnika ne ponavljajte v vsaki vrstici izdaje. Založnika shranite enkrat in izdaje povežite z njim. Leta rojstva osebe ne hranite hkrati v tabeli oseb in v vsakem zapisu avtorstva.

Humanistični podatki vendar niso vedno urejeni. Negotovega datuma »med 1848 in 1851« ne smemo prisiliti v eno natančno leto. Ločeno modelirajte najzgodnejši in najpoznejši datum, prikazno besedilo in stopnjo gotovosti ali ustvarite tabelo datumskih trditev z dokazi.

## Provenienca in trditve

Vrednost je lahko prepisana iz arhiva, sklep urednika, uvožena iz Wikidate ali predlog študenta. Provenienco hranite na ravni, ki jo zahteva trditev.

Pri spornih podatkih modelirajte **trditve**, namesto da bi eno vrednost prepisali:

| assertion_id | subject | property | value | source | certainty | contributor |
|---:|---|---|---|---|---|---|
| 81 | person_1042 | birth_place | place_17 | archive_A_52 | verjetno | dp |

Tako nesoglasje postane poizvedljivo, zgodovina uredniških odločitev pa ostane ohranjena.

## SQL kot raziskovalni jezik

Structured Query Language izraža vprašanja o tabelah. Nekaj osnovnih vzorcev zadostuje za veliko nalog:

```sql
SELECT title, year
FROM work
WHERE year BETWEEN 1900 AND 1918
ORDER BY year;
```

Povezovanje sledi razmerjem:

```sql
SELECT p.preferred_name, COUNT(*) AS works
FROM person AS p
JOIN contribution AS c ON c.person_id = p.person_id
WHERE c.role = 'author'
GROUP BY p.person_id
ORDER BY works DESC;
```

Poizvedbe shranjujte kot projektne datoteke in jih ne sestavljajte ročno za vsako objavo. Poizvedba je del analitične metode.

## Celovitost in preverjanje

Podatkovne zbirke lahko uveljavijo koristne omejitve:

- ključi morajo biti enolični;
- obvezna polja ne smejo biti prazna;
- tuji ključi morajo kazati na obstoječe zapise;
- kategorije lahko omejimo na nadzorovane vrednosti;
- datume in številske razpone lahko preverimo.

Omejitve preprečujejo naključno nedoslednost, ne morejo pa odločiti, ali je zgodovinska trditev pravilna. Preverjanje zahteva tudi pregled virov, odkrivanje dvojnikov, normativno kontrolo imen in dokumentirano uredniško politiko.

## SQLite za manjše humanistične projekte

SQLite celotno relacijsko zbirko shrani v eni prenosljivi datoteki in podpira običajni SQL brez strežnika. Je odličen korak naprej od preglednic za poučevanje, prototipe in številne raziskovalne zbirke.

Ob njej hranite:

- datoteko sheme, ki zbirko ponovno ustvari;
- uvozne skripte ali dokumentirane postopke;
- nadzorovane slovarje;
- podatkovni slovar in definicije polj;
- shranjene analitične poizvedbe;
- verzionirane izvoze v odprtih formatih, kot je CSV.

Datoteka zbirke je priročna; dokumentiran postopek jo naredi ponovljivo.

## Razdelan primer: omrežje korespondence

Za raziskavo dopisovanja ustvarimo tabele za osebe, pisma, kraje in sodelovanje. Pismo ima datum, arhivski identifikator in morda negotovost. Tabela sodelovanja osebo poveže s pismom v vlogi pošiljatelja, prejemnika, omenjene osebe ali urednika. Povezava s krajem lahko določi izvor, cilj ali omenjeni kraj.

Struktura podpira vprašanja o izmenjavi, mobilnosti in posredovanju, ne da bi vsa razmerja skrčila na eno samo povezavo. Jasno tudi loči razmerja iz metapodatkov dokumenta od tistih, ki so bila izluščena iz besedila pisma.

## Vaja

Zasnovajte shemo za en projekt: bibliografijo, arhiv ustne zgodovine, literarni korpus, popis kulturne dediščine ali zbirko korespondence. Narišite entitete in razmerja, določite ključe, poiščite eno razmerje mnogo proti mnogo ter pokažite, kako boste zabeležili negotovost in provenienco.

## Refleksija

- Katere kategorije v vaši shemi so analitične interpretacije in ne dejstva iz vira?
- Katere informacije bi izgubili z izvozom zbirke v eno samo ravno tabelo?
- Katera poizvedba bi razkrila največjo slabost pokritosti vaših podatkov?

## Povzetek

Relacijska podatkovna zbirka je formalen in popravljiv model entitet in razmerij. Ključi in normalizirane tabele zmanjšajo dvoumnost, povezovalne tabele izrazijo razmerja mnogo proti mnogo, SQL pa analitične korake naredi izrecne. Humanistična zbirka postane zaupanja vredna, ko ohranja tudi negotovost, provenienco, sporne trditve, uredniška pravila in ponovno ustvarljivo strukturo.
