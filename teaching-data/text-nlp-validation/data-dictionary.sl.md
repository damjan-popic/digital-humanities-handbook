---
translation_status: machine-assisted draft; requires human language review
---

# Podatkovni slovar

Paket uporablja UTF-8, Unicode NFC in konce vrstic LF. Datoteke CSV imajo eno
glavo ter navajanje po načelih RFC 4180. Stabilni identifikatorji se začnejo z
`TNLP-`. Ustvarjene datoteke so urejene po identifikatorjih; prazno polje
pomeni »ni uporabljivo« in ne domnevne ničle.

## Polja vira in izvlečka

| Polje | Pomen |
| --- | --- |
| `doc_id` | Stabilni identifikator sintetičnega dokumenta |
| `title` | Prikazni naslov, ki ga je napisal priročnik |
| `theme` | Avtorska skupina samo za vajo razpršenosti |
| `text` | Celotni sintetični učni dokument |
| `synthetic` | Dobesedno `true` pri vsakem sodobnem zapisu |
| `rights_status` | Izjava o pravicah, povezana z zapisom |
| `sample_id` | Stabilni identifikator anotacijskega vzorca |
| `stratum` | `contemporary_clean`, `historical_reference` ali `provider_ocr` |
| `source_path` | Pot do izbrane izvorne plasti glede na koren repozitorija |
| `source_record_id` | Stabilni identifikator v izvornem paketu |
| `selector` | Ponovljivo pravilo za izbor povedi |
| `source_sha256` | SHA-256 celotne izbrane izvorne datoteke |
| `text_sha256` | SHA-256 normaliziranega izvlečka |

## Polja vrednotenja CLASSLA

Referenčne in napovedne datoteke uporabljajo CoNLL-U. Vrednosti `NER=B-PER` in
podobne so v stolpcu MISC, ker jih tako zapiše CLASSLA. Vrstice večbesednih
pojavnic ostanejo v referenci, skladenjske mere pa uporabljajo le besedne
vrstice s celoštevilčnim identifikatorjem.

| Polje | Pomen |
| --- | --- |
| `layer` | Plast povedi, tokenizacije, leme, UPOS, oblikoslovja, odvisnosti ali entitete |
| `numerator` / `denominator` | Natančna števca za izračun objavljene mere |
| `metric` | Ime mere; odstotkov ne primerjajte brez imenovalca |
| `value` | Mera, zaokrožena na šest decimalk |
| `eligible_rule` | Pravilo, po katerem so referenčni elementi vstopili v imenovalec |
| `alignment_unit` | Besedilo povedi, oblika pojavnice ali označeni entitetni razpon za štetje |
| `reference_item_count` / `predicted_item_count` | Skupno število elementov na vsaki strani pred poravnavo in izločitvami |
| `aligned_reference_items` / `aligned_predicted_items` | Elementi, ki ustrezajo navedenemu predpogoju poravnave |
| `substitutions` / `insertions` / `deletions` | Izrecna števila zamenjav, vstavkov in izpustov v navedeni enoti |
| `excluded_reference_items` / `excluded_predicted_items` | Ločeni števili izločenih referenčnih in napovedanih elementov |
| `exclusion_rule` | Razlog, da elementi ne vstopijo v vrednotenje plasti |
| `alignment_status` | Natančno ujemanje, zamenjava, vstavljanje ali brisanje pojavnice |
| `reference_value` / `predicted_value` | Primerjani oznaki ali strukturi |
| `error_family` | `source`, `segmentation`, `lexical`, `morphosyntactic`, `dependency`, `entity`, `ambiguity` |
| `input_stratum` | Stanje vhodnega vira, ki samo po sebi ni vzročni sklep |
| `immediate_disagreement` | Neposredna razlika v poravnavi ali oznaki pred vzročno razlago |
| `likely_causal_origin` | Strojno podprti osnutek vzročne razvrstitve iz izrecne odločitvene tabele |
| `also_occurs_in_reference_transcription` | Ali je isto nestrinjanje oblike in plasti navzoče tudi brez ponudnikovega OCR |
| `review_status` | Trenutno stanje pregleda vzročne oziroma referenčne odločitve |
| `reviewer` / `reviewed_on` / `review_scope` | Prazno, dokler pregled ni opravljen; za prihodnje stanje `human-reviewed` so obvezni ime, datum ISO in obseg |
| `interpretive_risk` | Raziskovalna posledica morebitno prezrte napake |

Referenčne datoteke so strojno podprti osnutek, ki čaka na strokovni človeški
pregled. Pravila anotiranja, tabela vzročnih odločitev in zapisana nestrinjanja
so del podatkov ter morajo spremljati rezultate. Datoteka
`validation/expected-values.json` prav tako vsebuje trenutno stanje ter polja za
ime pregledovalca, datum in obseg, ki so obvezna ob prihodnjem stanju
`human-reviewed`.

## Polja besedilne analize, tem in čustev

`frequency-dispersion.csv` navaja frekvenco pojavnice, dokumentno frekvenco,
delež vseh dokumentov in Griesov DP po štirih avtorskih tematskih skupinah.
Skupine vsebujejo 83, 68, 66 in 113 upravičenih pojavnic, zato vsaka vrstica
objavi velikosti delov in števila izraza po delih. Za skupno frekvenco (F>0),
velikost dela (N_i), velikost korpusa (N) in število izraza (f_i) velja:

```text
DP = 0.5 * sum_i(abs(f_i / F - N_i / N))
```

Pri `F=0` DP ni določen. Nižja vrednost pomeni porazdelitev bliže pričakovanju
glede na velikost delov, višja pa večjo koncentracijo. `concordance.csv` navaja
omejeni levi in desni sobesedilni kontekst, zato ne nadomesti branja dokumenta.

Datoteke o temah navajajo število sestavin, seme, identifikator teme, urejene
ključne izraze, najpomembnejše dokumente, ujemajočo osnovno temo, Jaccardovo
prekrivanje in odločitev o stabilnosti. Številke tem med izvedbami nimajo
identitete, dokler jih ne povežete. Razlage uporabljajo stabilne identifikatorje
povedi, na primer `TNLP-C11.s1`; gradilnik zahteva, da se vsak identifikator ter
vsi pomembni in nasprotujoči dokumenti razrešijo v izvornem korpusu.

Anotacije čustev izvorno poved določijo samo z `doc_id` in `sentence_index`;
ustvarjeni rezultat razreši ter prenese točno izvorno besedilo, zato se podvojena
različica ne more neopazno spremeniti. Anotacije ločijo kontekstualno navzočnost
čustva, kategorijo, nosilca, cilj, glas, zanikanje, ironijo in negotovost. Izhodišče poroča o natančnem
ujemanju oblik z leksikonom in ne sklepa o duševnem stanju osebe. Pravila so v
`reference/emotion-codebook.sl.md`.

Datoteki `interim/model-environment.json` in `model-environment.lock.txt`
določata dejansko okolje neobvezne izvedbe. Datoteka
`interim/classla/resource-acquisition.json` loči seznam modelskih virov od časa
izvedbe modela; čas pridobitve je `unknown`, ker ga prejšnji zaganjalnik ni zanesljivo
zabeležil.
