---
translation_status: machine-assisted draft; requires human language review
---

# Pravice in provenienca

Datum pregleda: **7. september 2026**.

## Sodobni vzorec, ki ga je napisal priročnik

`source/contemporary-sample.csv` vsebuje dvanajst besedil, napisanih za ta
paket. Namenoma so sintetična in imajo vrednost `synthetic=true`. Ne poročajo o
resničnih dogodkih, osebah ali delovanju ustanov. Izvirno besedilo, izbor,
anotacije in dokumentacija priročnika so objavljeni pod CC BY 4.0, izvirna koda
pa pod MIT v skladu z licenco repozitorija.

## Arhivska odlomka prek sklica

`source/extraction-registry.json` kaže na dve datoteki v
`teaching-data/archival-friction/`:

- `reference/reference-transcription.txt`, priročniški ročno preverjeni prepis
  območja v *Ilustriranem Slovencu* z dne 7. februarja 1925; in
- `raw/provider-ocr.txt`, dokumentirano izpeljanko UTF-8 iz bajtno ohranjenega
  izvoza TXT portala dLib.

Gradilnik iz obeh izloči poved, ki se začne z `Tudi danes`, ter zabeleži poti in
vrednosti SHA-256. Besedila ne podvoji v novi plasti `source/`. Ustvarjeni
`raw/annotation-samples.csv` je izpeljanka za vajo in ne drugi pristen izvoz
ponudnika. Pred ponovno rabo preberite `SOURCE_CITATION.sl.md`,
`rights-and-provenance.sl.md` in pravila prepisa v arhivskem paketu. Identifikator
dLib je `URN:NBN:SI:doc-YPI8OFSU`.

## Rezultati modelov

Zamrznjeni rezultat v `interim/classla/` je ustvarjena anotacija, ne izvorni
dokaz. `interim/classla/model-run.json` navaja paket CLASSLA, procesorje,
manifest virov in zgoščene vrednosti modelskih datotek, okolje, ukaz ter
zgoščene vrednosti vhodov in izhodov. CLASSLA je objavljena pod Apache-2.0;
modeli in njihovi izvorni viri imajo lahko druge licence. Paket modelskih
datotek ne razširja. Pred razširjanjem ali produkcijsko rabo preglejte repozitorij
CLASSLA in metapodatke vsakega prenesenega vira.

Zamrznjeni rezultat NMF v `interim/topics/` je nastal iz sintetičnih učnih
dokumentov s paketom scikit-learn, objavljenim pod BSD-3-Clause. Zunanji korpus
ni vključen.

## Gradivo o čustvih

`reference/teaching-emotion-lexicon.csv` je majhen avtorski nabor pravil.
Ne prepisuje leksikona NRC ali drugega zunanjega vira. To je pomembno, ker
pogoji NRC prepovedujejo nadaljnje razširjanje podatkov; morebitni uporabniki
morajo vir pridobiti na uradni strani in presoditi veljavno licenco.

## Kontrolni seznam ponovne rabe

- Pri vseh sodobnih učnih dokumentih ohranite `synthetic=true`.
- Navedite zgodovinsko številko ter ločite ponudnikov OCR, referenčni prepis,
  ročno anotacijo in rezultat modela.
- Ročne anotacije ne obravnavajte kot nevtralno temeljno resnico.
- Zamrznjene izvedbe ne predstavljajte kot trenutno kakovost modela.
- Pred novo izdajo ponovno preverite licence paketov, modelov in zunanjih virov.
