---
title: "Kako analiziram čustva z leksikonom in ročnim preverjanjem?"
description: "Pregledne besedne asociacije primerjajte s kontekstualnimi oznakami nosilca, cilja, glasu, zanikanja in ironije."
category: "Analiza besedil"
difficulty: "srednje"
time: "75–120 min"
tags: [čustva, leksikon, pripisovanje, navedek, zanikanje, ironija, preverjanje]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Kako analiziram čustva z leksikonom in ročnim preverjanjem?

!!! warning "Stanje prevoda"
    Slovensko besedilo je strojno podprti uredniški osnutek. Pred formalno
    objavo potrebuje vsebinski in jezikovni pregled strokovnjaka za slovenščino.

<div class="answer-meta" markdown>
<span>Analiza besedil</span><span>srednje</span><span>75–120 min</span>
</div>

## Kaj želite doseči

Pregledni leksikalni signal želite primerjati s kontekstualno trditvijo o
čustvu. Ohranili boste podatek, kdo je predstavljen kot nosilec čustva, kaj je
njegov cilj, čigav glas nosi besede in ali zanikanje ali ironija prepreči
dobesedno branje. Vidni ostanejo primeri brez ujemanja, lažno pozitivne in
negativne napovedi ter nerazrešeni primeri.

!!! quote "V eni povedi"
    Beseda ima lahko čustveno asociacijo, ne da bi dokazovala, da jo občuti
    avtor, govorec, pripovedovalec ali kdo drug.

## Potrebujete

- kopijo repozitorija ali
  [učni paket za preverjanje besedilnih analiz in NLP](../../../assets/downloads/text-nlp-validation-v1.zip);
- pregledovalnik preglednic in po želji Python 3.12;
- razlike iz poglavja
  [Teme, sentiment in čustva](../../chapters/topics-emotions-classification.md).

Vseh osem povedi je sintetičnih. S stabilnima vrednostma `doc_id` in
`sentence_index` kažejo v `source/contemporary-sample.csv`. Namenjene so prikazu
vedenja metode in niso zgodovinski dokaz o čustvih.

## Provenienca leksikona in pravice

`reference/teaching-emotion-lexicon.csv` vsebuje osem natančnih slovenskih
površinskih oblik, ki so bile napisane za priročnik in so kot njegovo besedilo
objavljene pod CC BY 4.0. Gre za namenoma nepopolni učni nabor pravil in ne za
jezikovni vir. Ne prepisuje NRC ali drugega tujega leksikona, zato paket ne
razširja zunanjega leksikona s prepovedjo nadaljnjega razširjanja.

Kategorija `fear` zaradi vaje namenoma združi skrb in strah. Vsaka vrstica je
označena kot sintetična ter ima področje in opombo. Pri ponovni rabi ohranite
provenienco in seznama ne predstavljajte kot preverjeno pokritost slovenščine.

## Vhodi in rezultati

| Datoteka | Vloga |
| --- | --- |
| `reference/teaching-emotion-lexicon.csv` | izvirno izhodišče natančnih oblik |
| `reference/emotion-sensitivity-additions.csv` | ena dokumentirana oblika po osnovnem preizkusu |
| `reference/emotion-annotations.csv` | ročno pregledane kontekstualne oznake in lokatorji |
| `reference/emotion-codebook.sl.md` | pravila navzočnosti, nosilca, cilja, glasu in negotovosti |
| `output/emotion-baseline.csv` | ujemanja, ročna oznaka in izid TP/FP/TN/FN po povedi |
| `output/emotion-sensitivity.csv` | primerjava izhodišča z enovrstično razširitvijo |
| `output/emotion-method-comparison.csv` | enota, predstavitev, dokazno gradivo in meje trditve |

## Postopek

### 1. Trditev opredelite pred ujemanjem

Izberite enoto in cilj. Vaja preverja, ali poved kontekstualno predstavlja grobo
čustveno kategorijo za določljivega nosilca. Ne klasificira splošne polarnosti,
stališča pripovedovalca ali odziva bralca. Poved lahko izvaja negativno
vrednotenje in vseeno dobi `emotion_present=false`.

Preberite `reference/emotion-codebook.sl.md`. Vrednost `uncertain=true` ohrani
presojo, namesto da bi jo prisilila v gotovost. Učni vzorec je pregledal en
vzdrževalec, zato mere ujemanja označevalcev ni.

### 2. Ponovno zgradite pregledno izhodišče

Zaženite:

```bash
make text-nlp-validation
```

Gradilnik standardne knjižnice uporabi Unicode NFC, za iskanje male črke in
natančno ujemanje prijavljenih oblik. Zabeleži vsako obliko ter kategorijo.
Najmanj eno ujemanje napove `emotion_present=true`, nič ujemanj pa `false`.
Pravilo ne lematizira ter ne razrešuje zanikanja, glasu ali ironije.

### 3. Sledite primerom do vira

Odprite `reference/emotion-annotations.csv` in poiščite:

- `TNLP-E03` → `TNLP-C06`, poved 1: strah je v navedku pripisan
  *obiskovalcem* in ni čustvo poročevalca;
- `TNLP-E05` → `TNLP-C06`, poved 3: *jeza* je metajezikovna omemba, zanikanje pa
  zavrne sklep o avtorju poročila;
- `TNLP-E07` → `TNLP-C12`, poved 1: žalost je zanikana, skrb pa pripisana
  urednici in usmerjena k manjkajočemu viru;
- `TNLP-E08` → `TNLP-C12`, poved 2: navedeni *čudovito* je ironično negativno
  vrednotenje, posamezno čustvo pa ostane nerazrešeno.

Vsako poved poiščite v `source/contemporary-sample.csv`. Preverite polja za
nosilca, cilj, `voice`, `quotation`, `negation`, `irony`, `uncertain` in razlog.
Iz izdelanih učnih povedi ne sklepajte o psihologiji avtorja.

### 4. Poiščite ničelno ujemanje in lažno negativno napoved

V `output/emotion-baseline.csv` poiščite `TNLP-E06`. Poved predstavlja strah,
pripisan meščanom, s površinsko obliko *bali*, vendar natančni leksikon vsebuje
*bojijo* in ne *bali*. Zato nima ujemanja in je po dvojiškem pravilu navzočnosti
lažno negativna.

To je dokaz o pravilu ujemanja. Ne dokazuje, da je *bali* v vsakem kontekstu
nedvoumno čustveno ali da lematizacija sama reši nalogo.

### 5. Preberite lažno pozitivne napovedi

Preglejte vsaj naslednje vrstice:

- `TNLP-E04`: *čudovita* se ujema z veseljem, vendar je poved ironična in ne
  upraviči varne oznake posameznega čustva;
- `TNLP-E05`: dve pojavitvi *jeza* se ujemata z jezo, toda poved razpravlja o
  pripisovanju in izrecno prepreči sklep o avtorju;
- `TNLP-E08`: navedeni *čudovito* se ujema z veseljem, ročna oznaka pa čustvo
  pusti odsotno in ironično branje negotovo.

Dvojiški izid poenostavi bogatejša nestrinjanja. Seznam ujemanj, ročni razlog in
negotovost ohranite ob TP/FP/TN/FN; kratica ni popolna interpretacija.

### 6. Primerjajte izraženo in pripisano čustvo

Primerjajte `TNLP-E02`, kjer pripovedovalec kustosinjo izrecno opiše kot
navdušeno, z `TNLP-E03` in `TNLP-E06`, kjer poročevalske konstrukcije strah
pripišejo obiskovalcem oziroma meščanom. Določite slovnični ali diskurzni namig
za nosilca ter cilj: obnovljeni plakat, zaprtje zbirke ali spremembo.

Čustva ne prenesite z navedenega govorca na poročevalca, z literarnega lika na
avtorja ali z leksikalne oblike na bralca. Kadar nosilec ali cilj nista podprta,
uporabite `unresolved`.

### 7. Primerjajte občutljivost

`reference/emotion-sensitivity-additions.csv` izhodišču doda samo obliko *bali*.
V `output/emotion-sensitivity.csv` primerjajte `baseline_exact_form` in
`add_documented_bali_form`.

Dodana oblika popravi znano lažno negativno napoved v tem vzorcu. Ne odpravi
lažno pozitivnih napovedi zaradi zanikanja, metajezikovne omembe ali ironije.
Tako vidite pridobitev in izgubo ene leksikonske spremembe: priklic se lahko
izboljša, kontekstualna veljavnost pa ne. Resnična lematizacijska različica bi
zahtevala dokumentirano lematizacijo in lastni pregled napak.

Ker je dodatek nastal po pregledu izhodiščnih napak, izboljšana mera opisuje
razvoj. Pred trditvijo o pričakovani kakovosti jo preverite na novem gradivu.

### 8. Napišite omejeno primerjavo metod

Uporabite `output/emotion-method-comparison.csv`. Za leksikonsko ujemanje in
ročno anotacijo navedite enoto, vhodno predstavitev, rezultat, dokazno gradivo,
podprto in nepodprto trditev, pridobitev, izgubo in znano odpoved. Paket ne
prilagodi nadzorovanega klasifikatorja: osem namenskih primerov ne dopušča
ločitve učnih, validacijskih in testnih podatkov. Opustitev je metodološka
odločitev, ne manjkajoči okras.

## Rezultat

Pripravite dokazno beležko s provenienco in pravicami leksikona, pravilom
ujemanja, števci in imenovalci matrike zamenjav, ničelnim ujemanjem, lažno
pozitivno in negativno napovedjo, navedenim ali pripisanim primerom, zanikanjem,
nerazrešeno ironijo, izvornimi identifikatorji, rezultatom občutljivosti ter
podprto trditvijo. Končajte z nepodprto trditvijo o notranjem stanju ali
populacijski razširjenosti.

## Preverite se

- Lahko vsako oznako povežete s stabilnim dokumentom in povedjo?
- Ste nosilca, cilj in glas poimenovali ločeno?
- So navedek, zanikanje in ironija polja in ne zgolj vtisi?
- So ničelno ujemanje ter FP in FN ohranjeni?
- Ste ohranili pravice in omejeni namen izvirnega mikroleksikona?
- Ste se izognili trditvi o nadzorovani kakovosti na osmih povedih?

## Pogoste pasti

- Vsako leksikalno asociacijo imenujete izraženo čustvo.
- Navedeni strah pripišete poročevalcu ali avtorju.
- Zanikano žalost štejete kot doživeto žalost.
- Ironično negativno vrednotenje pretvorite v izmišljeno posamezno čustvo.
- Leksikon izboljšate na evalvacijskih primerih in iste primere razglasite za
  pošten preizkus.
- Prepišete tuj leksikon brez pregleda pogojev razširjanja.

## Naloga

Napišite štiri sintetične povedi: izrecno čustvo, pripis, zanikanje in
nerazrešeno ironijo. Dodajte stabilne identifikatorje in provenienco. Drug bralec
naj uporabi kodirni priročnik, ne da bi videl nameravane oznake. Ohranite
nestrinjanje, preizkusite obe leksikonski različici ter pojasnite, katera napaka
bi bila najpomembnejša za vaše raziskovalno vprašanje.
