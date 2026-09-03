# Učni paket o trenju pri delu z arhivskim gradivom

Dvojezični paket spremlja priročniško pot skozi raziskovalni načrt, podatke
in metapodatke ter delo z besedilom in OCR-jem. Jasno ločuje ohranjeno
gradivo ponudnika, priročniško referenčno delo, izrecno označene sintetične
učne motnje in izpeljane rezultate.

## Raziskovalno vprašanje

Kako politično opredeljena ilustrirana priloga spreminja ljudi, kraje in
nedavne dogodke v dokaze ter kaj izgubite, če njene napise obravnavate kot
nevtralne metapodatke?

Popis vsebuje **en pristen zgodovinski predmet**: 7. številko
*Ilustriranega Slovenca* z dne 7. februarja 1925, ki jo predstavlja
nespremenjen dvostranski PDF. Priročnik je iz nje pripravil **osem na viru
utemeljenih referenčnih opazovanj**: en zapis o številki in sedem zapisov o
posameznih prispevkih. Učna plast vsebuje **štiri izrecno označene sintetične
motnje**. Referenčna opazovanja in motnje niso dodatni pristni arhivski
zapisi.

## Plasti paketa

| Plast | Namen | Pravilo pri vaji |
| --- | --- | --- |
| `source/` | Nespremenjeni PDF, zajeta zapisa dLib in Commons ter bajtno nespremenjen izvoz TXT iz dLib | Ne urejajte; gradivo kopirajte v naslednjo plast |
| `reference/` | Priročniška opazovanja, uredniške odločitve, referenčni prepis in pravila prepisa | Uporabite kot preverljivo referenco, ne kot »temeljno resnico« |
| `teaching/` | Štiri izrecno označene sintetične motnje | Uporabite samo za pripravo vaje |
| `raw/` | Namenoma neurejene vrstice ter izbrani, dekodirani in presledkovno normalizirani odlomek OCR-ja ponudnika | Ohranite; kopirajte v `interim/` |
| `interim/` | Kandidati, ki čakajo na preverjanje ob viru ali referenci | Preverite jih in zapišite odločitev |
| `cleaned/` | Preverjena opazovanja, referenčni prepis in odločitve | Primerjajte s svojim rezultatom |
| `output/` | Štetje napak OCR, pregled napak in povzetki zapisov | Ponovno ustvarite; ne urejajte ročno |
| `validation/` | Pričakovani rezultati in zgoščene vrednosti datotek | Ponovno ustvarite po odobreni spremembi |
| `known-problems/` | Namerno odprte omejitve | Dopolnite, ko dokumentirate novo omejitev |

Datoteki `metadata-raw.csv` in `metadata-clean.csv` na vrhnji ravni sta
deterministični kopiji ustreznih tabel v plasteh. `correction-log.csv`
združuje devet na viru utemeljenih uredniških odločitev (`synthetic=false`)
in štiri razveljavitve izrecno označenih učnih motenj (`synthetic=true`). Ena
odločitev opisuje, kako so vrstice 1–4 izvoza TXT iz dLib dekodirane, izbrane
in normalizirane v `raw/provider-ocr.txt`.

## Dostopna učna pot

1. Preberite `rights-and-provenance.sl.md`, nato odprite PDF.
2. Preglejte `raw/messy-records.csv`. Ločeno označite opazovanje iz vira,
   metapodatke ponudnika, sklep in sintetično motnjo.
3. Primerjajte tabelo z `reference/observations.csv`. Datuma nastanka
   fotografije ne sklepajte iz datuma številke.
4. Ločeno ohranite natisnjeno oznako osebe ali skupine, strukturo enote
   `entity_structure`, zunanjega kandidata `authority_candidate` in stanje
   povezave `authority_link_status`.
5. Primerjajte `raw/provider-ocr.txt` in
   `reference/reference-transcription.txt`. Napake razvrstite, preden
   pogledate `output/ocr-error-audit.csv`.
6. Preglejte `correction-log.csv`, `unresolved-cases.csv` in povzetke v
   `output/`. Pojasnite, kako negotovost vpliva na raziskovalno trditev.

Za študentsko vajo ukazna vrstica ni potrebna. Vzdrževalci vse izpeljane
datoteke, deterministični ZIP in njegovo zgoščeno vrednost SHA-256 ponovno
ustvarite z ukazom:

```text
make archival-friction-packet
```

Gradilnik uporablja standardno knjižnico Python in javna avtorska orodja
repozitorija; shranjenega posnetka in izvoza TXT ne prenaša in ne zamenjuje.
Izračun CER in WER se začne po dokumentiranem izboru in normalizaciji
presledkov, zato ne meri izgube presledkov postavitve zunaj izbranega odlomka.

## Dostopna opisa strani

**1. stran.** Sivinska ilustrirana naslovna stran z glavo *Ilustrirani
Slovenec*. Nad fotografijami množice pred ljubljanskim hotelom Union, struge
Ljubljanice in štirih poimenovanih moških je velika politična karikatura.
Napisi fotografije uokvirjajo z odkrito strankarskim jezikom.

**2. stran.** Sivinska montaža z naslovom »Iz razpuščene narodne skupščine«.
Vsebuje skupinski portret nemških poslancev, fotografije Ljubljane in ulične
prizore, označene kot nemška in ameriška volilna kampanja. Gosti napisi in
neenakomerni stolpci otežujejo določanje vrstnega reda branja v OCR-ju
ponudnika.

## Etična raba

Številka je politično opredeljena zgodovinska publikacija. Njeni opisi ljudi
in političnih skupin so dokaz retorike publikacije, ne nevtralni opisi, ki bi
jih priročnik potrjeval. Razlikujte med podobo, napisom, OCR-jem ponudnika,
referenčnim prepisom in poznejšimi trditvami o normativnih zapisih. Vzorec ne
vsebuje sodobnih osebnih podatkov.
