---
title: "Kako primerjam dvodelna in projicirana omrežja?"
description: "Primerjajte dokaze o osebah in dokumentih s projekcijami, pragovi ter utežmi, ki ohranijo povezavo z viri."
category: "Omrežja"
category_id: "Networks"
difficulty: "srednje"
time: "60–90 min"
tags: [dvodelna-omrežja, projekcija, pragovi, središčnost, provenienca]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Kako primerjam dvodelna in projicirana omrežja?

<div class="answer-meta" markdown>
<span>Omrežja</span><span>srednje</span><span>60–90 min</span>
</div>

Strojno podprt prevodni osnutek; potreben je strokovni jezikovni pregled.

## Kaj želite doseči

Preverite, kako pravilo skupnega dokumenta spremeni pomen povezanosti. Dokaz o udeležbi osebe v dokumentu ohranite ob primerjavi projekcij, pragov in korespondence z viri. Poglavje [Omrežja in vizualizacija](../../chapters/networks-visualization.md) vsebuje pojme in razlago.

## Potrebujete

Razpakirajte [spremljevalni ZIP](../../../assets/downloads/contested-models-v1.zip). Uporabite Python 3.10+ in pregledovalnik CSV. Grafovska knjižnica ali risarski program nista potrebna. Preberite `input/dossier.sl.md`: vseh šest oseb in šest omrežnih dokumentov je sintetičnih. Primerjava z avtentičnim časopisom ostaja ločeno označena.

## Postopek

### 1. Določite populacijo in izbor

Preglejte `input/participation.csv` in `input/documents.csv`. V njih je šest oseb, šest dokumentov in 18 vrstic udeležbe. Osebo v dokumentu štejte enkrat. Ohranite vloge pošiljatelja in prejemnika ter lokatorje virov. Opombi SYN-N1 in SYN-N2 sodita v podatkovno vajo, ne v ta omrežni izbor.

### 2. Ustvarite vse poglede

```bash
python run.py --output output-first
```

Dvodelni graf povezuje osebe samo z dokumenti. Projicirani graf poveže pare s skupnim dokumentom; utež je število različnih skupnih dokumentov. Korespondenčni graf uporablja samo pisma z izrecno določenimi vlogami pošiljatelja in prejemnika.

Odprite `bipartite-edges.csv`, `projection-evidence.csv` in `correspondence-edges.csv`. Projicirani par ohrani vsak dokument, ki ga utemeljuje; ne postane nov neodvisni vir.

Preglejte tudi `projection-singletons.csv`. Dokument z eno izbrano osebo mora
ostati v dvodelnem seznamu povezav, ne sme ustvariti projiciranega para in ne sme
prispevati imenovalca za utež. Sedanja učna množica nima takega dokumenta,
zato datoteka vsebuje preverljivo glavo; regresijski preizkus pravilo preveri
neposredno.

### 3. Primerjajte pragove in vrstni red

| Pravilo | Povezave | Največja stopnja med osebami |
|---|---:|---|
| Dvodelno omrežje | 18 | E, 4 dokumenti |
| Projekcija, vsaj 1 dokument | 15 | vseh šest, 5 oseb |
| Projekcija, vsaj 2 dokumenta | 7 | C, 4 osebe |
| Projekcija, vsaj 3 dokumenti | 2 | A, B, D, E, 1 oseba |
| Korespondenca | 3 | E, skupna stopnja 2 |

Primerjajte pripadajoče datoteke `*-metrics.csv`. Izolirane osebe ohranite v imenovalcu. Dvodelna stopnja šteje dokumente, projicirana pa ljudi. Koda po pragu uporablja neutežene enotske poti, nenormalizirano središčnost po vmesnosti in normalizirano harmonično bližino po izhodnih poteh. Utež pomeni dokazno podlago, ne razdalje.

### 4. Pojasnite projekcijsko napihovanje

SYN-D5 našteva šest ljudi in ustvari petnajst možnih parov. Preglejte AB, ki ga podpirajo D1, D2 in D5, ter CE, ki ga podpirata D3 in D5. Ponavljajoča se skupna dokumentiranost ne dokazuje prijateljstva.

Preglejte `fractional-weights.csv` in `results.json`. Če vsakemu dokumentu dodelite prispevek 1/(k−1) za par in zahtevate utež vsaj 1, ostanejo AB, DE in EF. Odstranitev D5 pri običajnem pragu 1 ohrani sedem parov. Pojasnite, zakaj se alternativi razlikujeta.

### 5. Preverite skupnosti in manjkajoče zapise

V `results.json` je optimum pri pragu 2 ABC | DEF, prag 1 pa vse združi. Koda izčrpno preveri neuteženo neusmerjeno modularnost pri ločljivosti 1 in ohrani izenačenja; namenjena je samo šestim osebam. Pri korespondenčnih skupnostih izrecno zanemari smer.

Pred pragom 2 izločite D6: EF izgine, nenormalizirana središčnost E po vmesnosti pa pade s 4 na 0. Primerjajte `missing_D6-metrics.csv`. Ta ciljni scenarij izgube ni ocena naključnega ohranjanja arhivov.

## Rezultat

Oddajte primerjavo treh modelov, najmanj dva pragova, mere vozlišč, tabelo provenience in interpretacijo občutljivosti. Risba ni obvezna. Komponente in izolirana vozlišča opišite tudi v besedilu, da bodo rezultati dostopni brez ogleda slike.

## Preverite se

Lahko vsak par povežete z dokumenti? Primerjate istih šest oseb? Ste navedli enote, smer in normalizacijo? Je programska razdelitev brez potrditve postala zgodovinska politična skupina?

## Pogoste pasti

Seznam šestih ljudi obravnavate kot petnajst neodvisnih pričevanj; primerjate stopnje z različnimi enotami; skrijete izolirana vozlišča; število podpor uporabite kot dolžino poti; poročate samo o pragu, ki potrdi pričakovani vrstni red.

## Naloga

Navedite trditev, ki ostane veljavna, in trditev, ki med gradnjami odpove. AB in CE preverite s [postopkom vračanja k virom](audit-a-network-claim-against-source-records.md). Pravilo gradnje ohranite tudi v končnem sklepu.
