# Sporni modeli: spremljevalno gradivo k arhivskemu trenju

Raziskovalno vprašanje: kako dokumentarne oznake pri uredniškem modeliranju
postanejo identitete, ozemeljska pripadnost in navidezne povezave?

Izvirni paket o arhivskem trenju ostaja nespremenjen. Njegovih osem referenčnih
opazovanj opisuje avtentično številko *Ilustriranega Slovenca* z dne 1925-02-07.
Skripta izbere štiri posamično poimenovane osebe in pokaže šest parov sopojavljanja
v isti številki. To ne dokazuje korespondence.

Šest oseb A–F, šest dokumentov D1–D6, opombe o statusu, imenske različice in meje
v `input/` so **v celoti sintetični**, označeni z identifikatorji `SYN-`.
Ana Kovač / Anna Kovatsch je izmišljena, ne identificirana časopisna oseba.
Pred tabelami preberite `input/dossier.sl.md`. Berljivi izvorni zapisi omogočajo,
da rezultate preverite tudi drugače kot s ponovno ustvarjenimi podatki.

Avtentični `source/ljubljana-1910.jpg` služi ločeni vaji georeferenciranja.
Ne potrjuje izmišljene meje. Pred ponovno uporabo preberite
`rights-and-provenance.sl.md`. Slovenska besedila so strojno podprti osnutki,
ki še potrebujejo strokovni jezikovni pregled.

## Zagon prenesenega paketa

Uporabite Python 3.10 ali novejši (preizkušeno z 3.12), samo standardno knjižnico:

```bash
python run.py --output output-first
python query.py --database output-first/dossier.sqlite --subject SYN-A --as-of 1910-06-15
python query.py --database output-first/dossier.sqlite --conflicts
```

Za vsak poskus uporabite novo izhodno mapo; obstoječe skripta ne prepiše.
Rezultati vsebujejo zbirko SQLite, CSV-je z viri, mere in `results.json`.
Primerjajte jih z `expected/`. Skripta ne pošilja omrežnih zahtev.
Prenos vključuje nespremenjeni izvleček opazovanj z opombami o virih in pravicah;
celotni časopisni faksimile ostaja v
[izvirnem paketu](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction).

## Vzdrževanje v repozitoriju

V korenu repozitorija izvedite:

```bash
python teaching-data/contested-models/run.py --output .cache/contested-models
python scripts/build_contested_models_packet.py
python scripts/check_contested_models.py
make check
```

Graditelj ponovno izdela pričakovane rezultate in deterministični prenos.
Način `--check` ponovi izračune in primerja datoteke brez nadomestitve shranjenih
izdelkov. ZIP vsebuje manifest SHA256 in stalne datume datotek.
Pričakovanih rezultatov ne popravljajte ročno.

## Neobvezna priprava GIS

Predpomnjene koordinate v `input/gcps.csv` so že projicirane. Za obnovitev
v ločenem okolju namestite pripeto neobvezno odvisnost:

```bash
python -m pip install -r requirements-gis.txt
python prepare_georeferencing.py --check
```

Postopek uporablja shranjeno zemljepisno dolžino in širino iz Wikidata,
brez sprotnega iskanja, ter EPSG:3794. Slika ima 5747 × 7287 pikslov.
V CSV je slikovni y pozitiven navzdol, v ustvarjeni datoteki QGIS pa negativen.
Začetne ničle odstopanj so nadomestne vrednosti. Afini številski preskus
ne prevzorči rastra.

## Interpretacija in dostopnost

Vse vaje imajo tabelarično pot. Barva, razporeditev in miška niso potrebne
za razlago osnovnih primerjav. QGIS je ločena ročna vaja: številska prilagoditev
in pregled tabel ne potrjujeta vizualno pregledane poravnave. Prve kontrole
ne prestanejo neodvisnega preverjanja in ostajajo vaja za pregled, ne potrjen
georeferencirani zemljevid.

Lokalni inženirski kvadrat in večjezična imenska opomba sta izmišljena.
Koordinat ne prenašajte na pravo podlago in oseb ne združujte z avtentičnimi
opazovanji. Pomen polj pojasnjuje `data-dictionary.sl.md`, celotne rezultate
pa `expected/results.json`. Metodološki in slovenski jezikovni pregled
ostajata potrebna.
