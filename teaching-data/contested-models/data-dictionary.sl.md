# Podatkovni slovar in omejitve modela

CSV uporablja UTF-8, glavo in vejice. Identifikatorji razlikujejo velikost črk.
Prazna polja trditev postanejo SQL NULL; drugih praznin ne razlagajte kot ničle.
Datumi so gregorijanski YYYY-MM-DD, intervali polodprti [začetek,konec), časi
zapisa pa v kanoničnem UTC. Besedilo je strojno podprt prevodni osnutek,
ki potrebuje strokovni jezikovni pregled.

| Vhod | Vrstica in pomembna polja |
|---|---|
| `entities.csv` | oseba, kraj ali ozemlje; stabilni ID, prikazna oznaka, sintetičnost |
| `documents.csv` | izbrani omrežni dokument; vrsta, časovno okno in lokator vira |
| `participation.csv` | enolični par osebe in dokumenta; vloga, zanesljivost, sintetičnost |
| `assertions.csv` | subjekt, predikat, besedilo ALI objekt, kontekst, interval, čas zapisa, nadomeščena trditev, izvorno besedilo in zanesljivost |
| `candidates.csv` | par omembe in kandidata; izvirna oblika, vir, odprta odločitev in razlog |
| `toponyms.csv` | imenska različica z jezikom, kontekstom, intervalom in virom; vse izmišljeno |
| `places.csv` | izmišljena točka v lokalnem kvadratu; metri in predpostavljena negotovost ±75 m |
| `boundaries.csv` | datirana ločnica; zahod je pod njeno vrednostjo x, vzhod vključuje ločnico |
| `landmarks.csv` | slikovni kandidat pravega načrta in današnja koordinata/različica Wikidata; navedena natančnost ni potrjena točnost |
| `gcps.csv` | iste točke s predpomnjenima koordinatama EPSG:3794 v metrih |

`source_wording` je lahko prevedeni povzetek izmišljenega zapisa, ne arhivski
citat. Berljivi dosje določa pogoje. Vrednost A02 vsebuje namerno napačni prepis,
izvorno besedilo pa ohrani predpostavljeni podpis. A03 nadomesti A02; statusni
trditvi A04 in A05 ostaneta vzporedni. Okrajšanim ID-jem dodajte SYN-.

Shema preveri reference in trditve samo z dodajanjem, uvoznik pa datume ter
enolično udeležbo. To ni celovita časovna ontologija: neznana krajišča, pretvorbe
koledarjev in varovani transakcijski časi niso izvedeni. Združljivost predikata
in vrste objekta zahteva strokovni pregled. Poizvedba neskladij pokaže različne
prekrivajoče se statusne oznake, ne logičnih protislovij. `--conflicts` vrne
celotno trenutno čakalno vrsto za pregled in ne uporabi filtrov osebe/datuma.

## Izhodne konvencije

- `assertions-*.csv`: časovni posnetki z viri in datumi.
- `membership.csv`: štiri vrstice središčne in možne pripadnosti.
- `candidate-places.csv`: ista obdobja z nerazrešenimi kandidati in datiranimi
  večjezičnimi imeni; vrstice niso prebivalci.
- `authentic-issue-cooccurrence.csv`: šest parov štirih posamično poimenovanih
  oseb z lokatorji. Interakcija ni izpeljana.
- `projection-evidence.csv`: vrstica za par in podporni dokument. Uteži štejejo
  dokumente, ne neodvisnih zgodovinskih pričevanj.
- `*-metrics.csv`: stopnja, vhodna/izhodna stopnja, surova vmesnost in izhodna
  harmonična bližina, deljena z N−1. Pri neusmerjenem grafu vhodni in izhodni
  stolpec pomenita običajno stopnjo. Po izboru imajo vse poti enotske dolžine.
- `correspondence-edges.csv`: pošiljatelj, prejemnik, vir, interval in zanesljivost.
  Časovno okno ni trajanje. Ponovljeni dogodki bi imeli ločene dokazne vrstice;
  grafovske mere podvojene pare krajišč združijo.
- `fractional-weights.csv`: vsota prispevkov 1/(k−1) za skupni dokument velikosti k.
- `gcp-residuals.csv`: evklidsko odstopanje v ciljnih metrih, tudi za izločene
  kontrole. Slikovni y je v vhodu pozitiven navzdol, izvoz QGIS obrne predznak.
- `gcp-leave-one-out.csv`: prilagoditev trem kontrolam, preverjanje četrte.
- `results.json`: mere, šibke komponente pri usmerjenih grafih in vsi maksimumi
  neutežene neusmerjene modularnosti pri ločljivosti 1. Skupnosti se računajo
  samo za šest oseb; smer korespondence se zanemari samo pri skupnostih.
  Izolirana vozlišča lahko povzročijo izenačene razdelitve.

Avtentični časopisni izvleček je nespremenjen in ima slovar v izvirnem paketu.
Njegov `synthetic=false` označuje uredniško opazovanje avtentičnega predmeta,
ne potrjene identitete osebe.
