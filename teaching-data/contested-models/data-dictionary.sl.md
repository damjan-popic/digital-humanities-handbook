---
translation_status: machine-assisted draft; requires human language review
---

# Podatkovni slovar in omejitve modela

CSV uporablja UTF-8, glavo in vejice. Identifikatorji razlikujejo velikost črk.
Prazna polja trditev postanejo SQL NULL; drugih praznin ne razlagajte kot ničle.
Datumi so gregorijanski YYYY-MM-DD, intervali polodprti [začetek,konec), časi
zapisa pa v kanoničnem UTC. Besedilo je strojno podprt prevodni osnutek,
ki potrebuje strokovni jezikovni pregled.

| Vhod | Vrstica in pomembna polja |
|---|---|
| `entities.csv` | oseba, kraj ali ozemlje; stabilni ID, prikazna oznaka, sintetičnost |
| `sources.csv` | natančen popis desetih virov D1–D6, N1, N2, BORDER in NAMES; vrsta vira, lokator označenega odseka dosjeja in stanje vsebine |
| `documents.csv` | izbrani omrežni dokument; vrsta, časovno okno, ID in lokator vira |
| `participation.csv` | enolični par osebe in dokumenta; vloga, zanesljivost, ID vira in sintetičnost |
| `assertions.csv` | subjekt, predikat, besedilo ALI objekt, kontekst, interval, čas zapisa, nadomeščena trditev, izvorno besedilo, razmerje besedila do vira in zanesljivost |
| `candidates.csv` | par omembe in kandidata; izvirna oblika, vir, odprta odločitev in razlog |
| `toponyms.csv` | imenska različica z jezikom, kontekstom, intervalom in virom; vse izmišljeno |
| `places.csv` | izmišljena točka v lokalnem kvadratu; metri in predpostavljena negotovost ±75 m |
| `boundaries.csv` | z virom opredeljena datirana ločnica; zahod je pod njeno vrednostjo x, vzhod vključuje ločnico |
| `landmarks.csv` | slikovni kandidat pravega načrta in današnja koordinata/različica Wikidata; navedena natančnost ni potrjena točnost |
| `gcps.csv` | iste točke s predpomnjenima koordinatama EPSG:3794 v metrih |

`source_wording_relation` izrecno pove, ali je `source_wording` označen kot
`exact`, `translation` ali `summary`; tega ne sklepajte iz samega
besedila. Vsa polja opisujejo izmišljeni dosje, ne arhivskega citata. Vrednost A02 vsebuje namerno napačni prepis,
izvorno besedilo pa ohrani predpostavljeni podpis. A03 nadomesti A02; statusni
trditvi A04 in A05 ostaneta vzporedni. Okrajšanim ID-jem dodajte SYN-.

Shema preveri reference in trditve samo z dodajanjem, uvoznik pa datume, natančen
popis virov z označenimi odseki in enolično udeležbo. Nadomestna vrstica mora
ohraniti subjekt, predikat, kontekst, vir, interval in vrsto intervala prvotne
trditve; ena vrstica ima lahko največ enega neposrednega naslednika. To ni
celovita časovna ontologija: neznana krajišča, pretvorbe
koledarjev in varovani transakcijski časi niso izvedeni. Združljivost predikata
in vrste objekta zahteva strokovni pregled. Poizvedba neskladij pokaže različne
prekrivajoče se statusne oznake, ne logičnih protislovij. `--conflicts` vrne
celotno trenutno čakalno vrsto za pregled in ne uporabi filtrov osebe/datuma.

## Pomen izhodnih datotek

- `assertions-*.csv`: časovni posnetki z viri in datumi.
- `membership.csv`: štiri vrstice središčne in možne pripadnosti z izrecno
  poimenovanimi polji veljavnosti meje.
- `candidate-places.csv`: nerazrešeni kandidati, povezani z zgodovinskimi stanji
  možnega kraja. Datumi omembe, meje in imena ostanejo ločeni;
  `comparison_interval_*` je dejanski polodprti presek različice meje in imena,
  ne trajanje omembe. Vrstice niso prebivalci.
- `authentic-issue-cooccurrence.csv`: šest parov štirih posamično poimenovanih
  oseb z lokatorji. Interakcija ni izpeljana.
- `projection-evidence.csv`: vrstica za par in dokument, ki ga utemeljuje. Uteži štejejo
  dokumente, ne neodvisnih zgodovinskih pričevanj.
- `projection-singletons.csv`: dokumenti z natanko eno osebo. Ostanejo v
  `bipartite-edges.csv`, ne ustvarijo pa projiciranega para ali imenovalca uteži.
- `*-metrics.csv`: stopnja, vhodna/izhodna stopnja, nenormalizirana središčnost
  po vmesnosti in harmonična bližina po izhodnih poteh, deljena z N−1. Pri neusmerjenem grafu vhodni in izhodni
  stolpec pomenita običajno stopnjo. Po izboru imajo vse poti enotske dolžine.
- `correspondence-edges.csv`: pošiljatelj, prejemnik, vir, interval in zanesljivost.
  Časovno okno ni trajanje. Ponovljeni dogodki bi imeli ločene dokazne vrstice;
  grafovske mere podvojene pare krajišč združijo.
- `fractional-weights.csv`: vsota prispevkov 1/(k−1) za skupni dokument velikosti k.
- `gcp-residuals.csv`: evklidsko odstopanje v ciljnih metrih, tudi za izločene
  kontrole. Slikovni y je v vhodu pozitiven navzdol, izvoz QGIS obrne predznak.
- `gcp-leave-one-out.csv`: prileganje trem oslonilnim točkam, preverjanje četrte.
- `results.json`: mere, šibke komponente pri usmerjenih grafih in vsi maksimumi
  neutežene neusmerjene modularnosti pri ločljivosti 1. Skupnosti se računajo
  samo za šest oseb; smer korespondence se zanemari samo pri skupnostih.
  Izolirana vozlišča lahko povzročijo izenačene razdelitve.

Avtentični časopisni izvleček je nespremenjen in ima slovar v izvirnem paketu.
Njegov `synthetic=false` označuje uredniško opazovanje avtentičnega predmeta,
ne potrjene identitete osebe.
