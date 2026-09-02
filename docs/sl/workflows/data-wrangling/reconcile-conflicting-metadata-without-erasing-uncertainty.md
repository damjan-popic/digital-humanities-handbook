---
title: "Kako uskladim nasprotujoče si metapodatke, ne da bi izbrisal/-a negotovost?"
description: "Primerjajte navedbe vira, ponudnikove zapise in kandidate v normativnih zbirkah ter ohranite dokaze in dokumentirano odločitev."
category: "Urejanje podatkov"
category_id: "data-wrangling"
difficulty: "začetno"
time: "60–90 min"
tags: [metapodatki, provenienca, normativna-kontrola, negotovost, usklajevanje]
---

# Kako uskladim nasprotujoče si metapodatke, ne da bi izbrisal/-a negotovost?

<div class="answer-meta" markdown>
<span>Urejanje podatkov</span><span>začetno</span><span>60–90 min</span>
</div>

## Kaj želite doseči

Natisnjeni napis, kataloški zapis, OCR in normativna zbirka se ne ujemajo pri imenu ali datumu. Prvi rezultat, ki se opira samo na ponudnikov zapis, je nezadosten: z njegovim sprejetjem ali izborom najbolj urejene vrednosti bi prikrili, kaj dokazi podpirajo.

Usklajevanje ni glasovanje z večino. Je dokumentirana primerjava trditev iz virov z različnimi nameni, bližino predmetu in pristojnostjo. V urejenem zapisu ohranite izvorne oblike, normalizirano vrednost navedite le tako natančno, kot dopuščajo dokazi, identiteto pa pustite nerešeno, kadar dokazov ni dovolj.

## Potrebujete

- izvorni predmet ali zvest posnetek in natančno oznako mesta;
- vse ponudnikove zapise ali izvoze, ki jih želite primerjati;
- stalne povezave do pregledanih normativnih zapisov;
- preglednico ali urejevalnik besedila; ter
- po želji datoteke `raw/messy-records.csv`, `source/source-records.csv` in `cleaned/decisions.csv` iz odprtega [učnega gradiva Arhivsko trenje](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction).

Pred začetkom zabeležite vir in pravice. Ponudnikove izvoze ohranite nespremenjene.

## Postopek

### 1. Natančno opredelite neskladje

Zapisu in polju dodelite stabilna identifikatorja. Vsako vrednost prekopirajte dobesedno in označite njeno vrsto:

- vidni dokaz, ki ste ga prepisali s predmeta;
- ponudnikov opisni metapodatek;
- ponudnikov OCR ali HTR;
- vašo izpeljavo iz druge podprte vrednosti;
- kandidatni zapis zunanje normativne zbirke; ali
- namerno dodano sintetično učno motnjo.

Vseh ne združite v eno polje za »ime« ali »datum«. Isti niz je lahko v enem viru prepis, v drugem pa domnevna identiteta.

### 2. Sestavite preglednico dokazov

Za vsako povezavo med trditvijo in virom ustvarite vrstico:

| Polje | Namen |
| --- | --- |
| `claim_id` | stabilni identifikator trditve |
| `record_id` | opisani predmet ali opažanje |
| `field` | ime, datum, kraj, naslov ali razmerje |
| `value` | natančna zatrjevana vrednost |
| `source_type` | faksimile, katalog, OCR, izpeljava ali normativni vir |
| `source_locator` | stran, območje, spletni naslov ali identifikator zapisa |
| `accessed` | čas pregleda spremenljivega zapisa |
| `evidence_scope` | kaj vir neposredno dokazuje |
| `notes` | dvoumnost, poškodba, neujemanje ali omejitev |

Faksimile lahko dokazuje zapis imena v tisku, ne pa tudi sodobne normativne identitete osebe. Normativna zbirka lahko dokazuje življenjske datume osebe, ne pa, da fotografija prikazuje prav njo. Presojajte obseg dokaza, ne le ugleda vira.

### 3. Pred vrednostmi polj preverite identiteto zapisa

Potrdite, ali primerjani zapisi opisujejo isti predmet, pojavitev ali osebo. Primerjajte stabilne identifikatorje, naslov, številko, stran, ustvarjalca, datum, fizični opis in zgodovino izvora. Podobno ime ne zadošča.

Razmerja poimenujte izrecno: `same_as` uporabite samo ob zadostnih dokazih, `duplicate_of` za podvojeni zapis, `reprint_of` za ponovljeno objavo, `version_of` za spremenjeno pojavitev in `possible_match` za nepotrjenega kandidata. Ohranite dokaz za vsako razmerje.

### 4. Uporabite pravila za posamezno polje

Pravilo napišite pred izborom vrednosti. Na primer:

- **prepis:** kadar je zapis čitljiv, dajte prednost vidni obliki; nejasnih znakov ne posodabljajte;
- **ponudnikovi metapodatki:** ohranite jih kot ponudnikovo trditev tudi takrat, ko jim predmet nasprotuje;
- **datum:** ohranite natisnjeni izraz ter dodajte točno, izpeljano, približno ali nerešeno normalizirano vrednost;
- **oseba:** pred povezavo z normativnim identifikatorjem zahtevajte skladnost kraja, vloge, dogodka, datuma ali razmerja;
- **naslov:** ločite naslov na predmetu od naslova, ki ga je dodal repozitorij; ter
- **jezik ali žanr:** navedite besednjak in čigavo razvrstitev predstavlja.

Števila ujemajočih se virov ne uporabljajte kot pravilo, dokler ne ugotovite njihove neodvisnosti in relevantnosti. Več katalogov lahko prepiše isto starejšo napako.

### 5. Odločitev zabeležite, različic pa ne izbrišite

V dnevnik dodajte zapis, ki vsebuje identifikator zapisa, polje, surovo in sprejeto vrednost, ukrep, dokaz, odločevalca, datum ter različico pravila. Uporabite nadzorovan ukrep, na primer `correct_from_facsimile`, `retain_provider_variant`, `derive_date`, `accept_authority_match`, `reject_authority_match` ali `leave_unresolved`.

Na sliki v *Ilustriranem Slovencu* je natisnjeno »Mr. Meker«. Sintetična učna vrstica zapis spremeni v »Mr. Meeker« in predlaga Ezro Meekerja. Podobnost imena, starosti in javne vloge je vabljiva, vendar gradivo ne vsebuje neodvisnega dokaza, ki bi fotografijo povezal s to osebo. Utemeljeni urejeni zapis obnovi natisnjeno obliko, kandidatno normativno polje pusti prazno, identiteto pa označi kot nerešeno.

### 6. Ohranite natančnost, negativne odločitve in nerešene primere

Leta, izpeljanega iz konteksta številke, ne spremenite v popolni koledarski datum. Ohranite polja `date_as_printed`, `date_normalized`, `date_certainty` in `derivation_note`. Pri neuspešnem preverjanju identitete shranite zavrnjenega kandidata in razlog, da druga oseba brez novih dokazov ne ponovi istega iskanja.

Oznako `unknown` uporabite, kadar vrednost ni znana, `unresolved`, kadar si dokazi nasprotujejo, in `not_applicable`, kadar polje za zapis ni smiselno. Prazna celica teh razlik ne ohrani.

### 7. Po ročnem usklajevanju izvedite samodejne preskuse

Z ročnim usklajevanjem določite obseg dokaza in identiteto. Nato s samodejnimi preskusi preverite, ali ima vsaka sprejeta vrednost dokaz ali izrecno pravilo, vsak popravek svojo odločitev, vsak normativni identifikator vodi do nameravanega zapisa, natančnost ni neupravičeno večja in nerešeni kandidati ostajajo vidni v revizijski plasti.

Po obravnavi dvojnikov preverite natančne ohranjene identifikatorje ter število vrstic pred posegom in po njem. Popolnoma enake vrstice lahko odstranite po dokumentiranem pravilu. Če se kandidati razlikujejo, uporabite vnaprej določeno pravilo prednosti oziroma vključitve in izločitve; ne zanašajte se na vidni vrstni red razvrščanja.

## Rezultat

Pripravite preglednico dokazov, tabelo usklajenih zapisov, po potrebi tabelo razmerij, dnevnik odločitev in seznam znanih težav. Pri spremenljivih katalogih in normativnih storitvah navedite različico pravila in datum dostopa.

Postopek je uspešen, če lahko druga oseba najde vse različne vrednosti, razume, zakaj ste eno sprejeli ali nobene, odpre natančno mesto v viru in ponovi končno štetje zapisov. Uporabna nerešena identiteta je boljša od samozavestne napačne povezave.

## Preverite se

- Ste ločili natisnjeno obliko, ponudnikovo trditev, normalizirano vrednost in normativno identiteto?
- Ali vsak vir podpira prav tisti obseg, ki ste mu ga pripisali?
- Bi lahko navidez neodvisni zapisi izhajali iz istega kataloga?
- Ste ohranili zavrnjene kandidate in razloge?
- Je kateri normalizirani datum natančnejši od svojega dokaza?
- Lahko potrdite ohranjene identifikatorje in število vrstic?

## Pogoste pasti

- Najpogostejši zapis izberete z glasovanjem.
- OCR obravnavate kot besedilo na predmetu.
- Kandidata v normativni zbirki obravnavate kot potrjeno identiteto.
- Ponudnikovo polje potiho zamenjate, namesto da bi ohranili obe trditvi.
- Približne ali izpeljane datume spremenite v lažno natančne.
- Ponatise razglasite za dvojnike in izbrišete dokaz o širjenju.
- Med različnimi vrsticami izbirate po trenutnem vrstnem redu preglednice.

## Naloga

V učnem gradivu uporabite zapise `AF-P1-001`, `AF-P1-002`, `AF-P1-003` in `AF-P2-003`. Pri vsakem ločite natisnjeni izraz, ponudnikovo vrednost, normalizacijo ali izpeljavo, gotovost in status normativne povezave. Za vsako neskladje napišite eno odločitev. Rezultat primerjajte z `cleaned/decisions.csv` in navedite dokaze, ki bi jih potrebovali za potrditev nerešenih identitet.

Za celotni večplastni postopek nadaljujte z navodili [za pretvorbo neurejenih zapiskov v ponovno uporabne podatke](turn-messy-humanities-notes-into-a-reusable-dataset.md). Poglavje [Podatki, metapodatki in modeli](../../chapters/data-metadata-models.md) pojasnjuje, zakaj so te odločitve modeliranje, ne nevtralno čiščenje.
