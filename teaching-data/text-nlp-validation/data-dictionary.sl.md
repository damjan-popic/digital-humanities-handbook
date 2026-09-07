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
| `alignment_status` | Natančno ujemanje, zamenjava, vstavljanje ali brisanje pojavnice |
| `reference_value` / `predicted_value` | Primerjani oznaki ali strukturi |
| `error_family` | `source`, `segmentation`, `lexical`, `morphosyntactic`, `dependency`, `entity`, `ambiguity` |
| `interpretive_risk` | Raziskovalna posledica morebitno prezrte napake |

Ročne datoteke so pregledana učna referenca. Politika anotiranja in zapisana
nesoglasja so del podatkov in morajo spremljati rezultate.

## Polja besedilne analize, tem in čustev

`frequency-dispersion.csv` navaja frekvenco pojavnice, dokumentno frekvenco,
delež vseh dokumentov, Juillandov D po štirih enako velikih avtorskih tematskih
skupinah in števila po skupinah. `concordance.csv` navaja omejeni levi in desni
kontekst, zato ne nadomesti branja dokumenta.

Datoteke o temah navajajo število sestavin, seme, identifikator teme, urejene
ključne izraze, najpomembnejše dokumente, ujemajočo osnovno temo, Jaccardovo
prekrivanje in odločitev o stabilnosti. Številke tem med izvedbami nimajo
identitete, dokler jih ne povežete.

Anotacije čustev ločijo kontekstualno navzočnost čustva, kategorijo, nosilca,
tarčo, glas, zanikanje, ironijo in negotovost. Izhodišče poroča o natančnem
ujemanju oblik z leksikonom in ne sklepa o duševnem stanju osebe. Pravila so v
`reference/emotion-codebook.sl.md`.
