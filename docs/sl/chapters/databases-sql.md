---
title: "Podatkovne zbirke in SQL"
description: "Relacijski modeli, časovno opredeljene trditve in ponovljive poizvedbe za spreminjajoče se in nasprotujoče si zgodovinsko gradivo."
tags: [podatkovna-zbirka, SQL, relacijski-model, identifikatorji, provenienca]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Podatkovne zbirke in SQL

## Učni cilji

Po tem poglavju boste znali:

- razlikovati med entiteto, lastnostjo, razmerjem, opazovanjem, trditvijo in dogodkom;
- primerjati ravno tabelo, normalizirano shemo in model trditev, povezanih z viri;
- predstaviti spremembe imen, statusov, jezikovnih razmerij in ozemeljske pripadnosti;
- ločiti čas veljavnosti od časa zapisa oziroma spremembe uredniške trditve;
- izvesti in preveriti časovno občutljive poizvedbe SQL, tudi ob nesoglasju med viri;
- pojasniti, česa omejitve zbirke, normalizacija in izvoz ne morejo zagotoviti.

## Pred začetkom

Ali lahko oseba zamenja državo, ne da bi se preselila? Ali lahko uporablja dva
jezika, ne da bi ji zato pripisali en sam trajni »jezik«? Kaj pomeni, če jo en
vir označi za služkinjo, drugi pa za šiviljo? Zbirka s polji `person.status`,
`person.language` in `place.country` lahko ponudi nedvoumen odgovor zato, ker
je razlike, potrebne za dobro vprašanje, že odstranila. Pred uporabo programske
opreme zapišite eno želeno poizvedbo in eno razlikovanje, ki ga ne želite izgubiti.

Predpostavljeno je osnovno poznavanje vrstic, stolpcev in navajanja virov. Znanje
SQL je koristno, za konceptualno primerjavo pa ni nujno. Najprej preberite poglavje
[Modeli, dokazno gradivo in interpretacija](models-evidence-interpretation.md).
Za izvedbo vaje morate znati ohraniti vhodno datoteko in zagnati priloženo skripto
Python. Strežnika, plačljive storitve ali osebnih podatkov ne potrebujete.
Besedilo je strojno podprt osnutek; pred potrditvijo je potreben jezikovni pregled.

## Podatkovna zbirka je trditev o svetu

Shema določi, kaj šteje za stvar, katere razlike je mogoče ponavljajoče opisovati
in po katerih razmerjih lahko poizvedujemo. Coddov relacijski model loči logično
organizacijo podatkov od njihovega fizičnega shranjevanja ter obravnava podvajanje
in skladnost. Ne določi pa, kaj je zgodovinska oseba, skupnost ali dogodek.
To ostajajo raziskovalne odločitve. [Codd 1970](https://doi.org/10.1145/362384.362685)
je tehnično izhodišče, ne zagotovilo, da je uspešna poizvedba tudi zgodovinski dokaz.

V avtentičnem [paketu arhivskih zapletov](../../assets/downloads/archival-friction-v1.zip)
referenčno opazovanje `AF-P1-003` prepiše natisnjeno oznako »Dr. Ante Trumbić«.
Najprej gre za opazovanje napisa v določeni časopisni številki, ne za neodvisno
potrjeno biografijo. Zapis `AF-P2-003` ohrani »Mr. Meker«, čeprav je bil predlagani
normativni kandidat zavrnjen. Zbirka mora omogočiti, da zavrnitev ostane vidna,
ne da bi s tem izbrisala osebo, ki jo vir poimenuje.

Uporaben zgled ponuja prozopografija, usmerjena k virom: razmerje med virom, osebo
in trditvijo postane predmet raziskovanja. Bradley in Short utemeljujeta razlikovanje
med strukturiranim delom zgodovinarja in zgodovinskim svetom, ki ga opisuje.
Učna shema prevzame to razlikovanje, ne predstavlja pa izvedbe celotne
prozopografske ontologije. [Bradley in Short 2005](https://doi.org/10.1093/llc/fqi022).

## Entitete, razmerja in raven trditve

**Entiteta** ima projektno identiteto: lahko je oseba, dokument, kraj ali ustanova.
**Lastnost** opisuje zapis v opredeljenem okviru. **Razmerje** poveže entitete,
na primer osebo in dokument. **Opazovanje** zabeleži, kaj je raziskovalec pregledal.
**Trditev** nekaj pove o entiteti in navede dokazno podlago. **Dogodek** modelira
pojav z udeleženci, vlogami in časom. To so različne odločitve pri modeliranju, ne stopnje
na poti do vse bolj resnične predstavitve.

Pismo je dokument, njegovo pošiljanje dogodek, zapisano naslovnikovo ime opazovanje,
identifikacija naslovnika pa trditev. Pismo je lahko ohranjeno brez dokaza, da je
bilo dostavljeno. Povezava pošiljatelj–prejemnik zato še ne pomeni uspešne komunikacije.
Tabela dogodkov omogoči takšna razlikovanja, vendar zahteva dodatno odločitev:
kaj v projektu sploh šteje za en dogodek in po katerih virih ga prepoznamo?

Primarni ključ enolično določi vrstico, tuji ključ pa kaže na drugo vrstico.
Imena so slabi ključi, saj se zapis, jezik in identifikacija spreminjajo. Za
razmerje mnogo proti mnogo uporabite **povezovalno tabelo**:
`participation(document_id, person_id, role)` omogoča več oseb v enem dokumentu
in več dokumentov pri eni osebi. Tudi vloga ima lahko svoj dokaz. Skupinski portret
ni ena neidentificirana oseba, ustanove pa ne shranjujte med osebe samo zato,
da bi poenostavili povezovanje tabel.

## Razdelan primer: en dosje, trije modeli

[Učni dodatek o spornih modelih](../../assets/downloads/contested-models-v1.zip)
vsebuje namenoma **sintetični** dosje za daljše obdobje. Ana Kovač oziroma Anna
Kovatsch (`SYN-A`) je izmišljena oseba, ne identifikacija osebe iz časopisa.
Paket arhivskih zapletov, ki temelji na avtentični časopisni številki, ostaja
nespremenjen. Dodatek preizkuša težave, ki jih ena sama številka ne more
dokumentirati. Pred tabelami preberite dvojezični dosje.
Če izhod preverjamo samo proti drugi izpeljani tabeli, lahko zgolj ponavljamo
iste predpostavke; zato potrebujemo tudi berljive izvorne zapise preizkusa.

V izmišljenem dokumentu D1 upravni seznam uporabi obliko Anna Kovatsch in osebo
A razvrsti med služkinje. V D2, slovenskem pismu s podpisom Ana Kovač, se oseba
opiše kot šivilja in navede, da bere nemško. Poznejša društvena opomba jo opredeli
kot samostojno obrtnico; institucionalna vloga iz leta 1925 beleži rabo nemščine.
Njeno po predpostavki nespremenjeno bivališče zamenja okraj, ko se premakne
sintetična meja. To so pogoji preizkusa, ne rekonstrukcija slovenske upravne zgodovine.

### Model 1: priročna ravna preglednica

| Oseba | Ime | Status | Jezik | Okraj |
| --- | --- | --- | --- | --- |
| SYN-A | Ana Kovač | šivilja | slovenščina | Zahod |

Za ozko določen prikaz je vrstica pregledna, za glavni raziskovalni zapis pa je
nevarna. Prikrije zgodnejšo obliko imena, upravno kategorijo, nemško vlogo in obdobje
ozemeljske pripadnosti. Če vrednosti v celicah razširimo z vejicami, dobimo nazaj
nekaj besedila, ne pa razmerij: kateri jezik je bil uporabljen kdaj in kdo je
pripisal posamezni status? Imena stolpcev sama ne odpravijo te izgube.

Ravni model omogoča hitro razvrščanje in berljiv učni list. Spremembe zakrije,
nesoglasje med viri pa podraži: raziskovalec mora za vsako štetje znova prebrati
opombe. Preglednica ni neustrezna zato, ker je preglednica. Neustrezna je takrat,
ko opredelitev ene vrstice ne more izraziti zastavljenega raziskovalnega vprašanja.

### Model 2: normalizirane entitete in razmerja

Ločite osebe, imena, kraje, dokumente in sodelovanja. Imensko različico shranite
za posamezno pojavitev ali poimenovalni kontekst ter jo povežite z osebo in virom.
Tako odpravite ponavljajoče se stolpce za osebe in lahko poiščete vse dokumente,
povezane z A. Tudi normaliziran model je lahko časoven: normalizacija ne prepoveduje
datumov ali nasprotujočih si trditev. Omejitev v tej primerjavi je zavestno preprosta
shema, ki razmerja še vedno obravnava kot dejstva brez dodatnih opredelitev.

```text
person 1 -- mnogo name_attestation mnogo -- 1 document
person 1 -- mnogo participation    mnogo -- 1 document
person 1 -- mnogo residence        mnogo -- 1 place
```

Ta predstavitev olajša vzdrževanje identifikatorjev in preprečevanje nedoslednih
popravkov. Sama po sebi pa ne loči uredniške identifikacije od samoopisa v viru.
Provenienca, pripeta zgolj celotnemu dokumentu, ni dovolj, kadar dve trditvi v istem
dokumentu dobita različni uredniški oceni. Razmislite, na kateri ravni potrebujete
avtorja odločitve, datum pregleda in utemeljitev povezave.

### Model 3: trditve in dogodki

Izvedljiva shema loči `entity`, `source` in `assertion`. Vsaka trditev vsebuje
subjekt, predikat, besedilno vrednost ali povezano entiteto, kontekst, zgodovinski
interval, vrsto intervala, čas zapisa, izvorno besedilo, opredeljeno razmerje do
vira (`exact`, `translation` ali `summary`) in stopnjo gotovosti. Popis
desetih virov D1–D6, N1, N2, BORDER in NAMES kaže na označene odseke berljivega
dosjeja. Ločena tabela sodelovanja hrani dokumentne vloge za poznejše grafe
dogodkov. Koda uporablja enake identifikatorje v obeh jezikovnih izdajah.

```text
entity 1 -- mnogo assertion mnogo -- 1 source
entity 1 -- mnogo assertion.object_id      (trditve o entitetah)
assertion 1 -- nič-ali-ena assertion.supersedes (uredniški popravek)
```

| Model | Kaj omogoči | Kaj zakrije ali podraži |
| --- | --- | --- |
| Ravna tabela za prikaz | Berljiv posnetek; preprosto razvrščanje | Časovno in izvorno opredeljeno povezovanje |
| Normalizirane entitete in razmerja | Ponovno uporabo istih identifikatorjev; poizvedbe o razmerjih mnogo proti mnogo | Nesoglasje, če razmerja niso dodatno opredeljena |
| Opredeljene trditve in dogodki | Časovne poizvedbe; pretekle različice uredniškega zapisa | Več povezovanj; zahtevnejšo interpretacijo in vzdrževanje besednjakov |

Tretji model ohrani več razlik, vendar brez povezave s faksimilom in prozo izgubi
postavitev, ton in zaporedje dokumenta. Splošni stolpec za predikat oteži tudi
nekatere omejitve tipov, ki bi jih v specializiranih tabelah lažje uveljavili.
To ceno sprejmite zavestno. Tabela trditev ni univerzalno nadomestilo za premišljeno
modeliranje posameznega raziskovalnega področja in njegovega gradiva.

## Imena, status in jezik kot kontekstualna razmerja

**Večjezična različica imena** naj ohrani izvorni zapis, jezik, kadar je znan,
pisavo, kontekst in datum izpričanosti. Upravni zapis ne sme samodejno nadomestiti
podpisa. Prednostno ime za prikaz je uredniško pravilo vmesnika ali izdaje, ne
brezčasna lastnost osebe. Normalizacijo za iskanje hranite ločeno: odstranjevanje
diakritičnih znamenj pomaga najti kandidate, ne upraviči pa združitve identitet
ali tihega posega v citirano besedilo.

Družbeni, pravni in institucionalni status zahtevajo različne predikate ali
opredeljen besednjak. Poklic, državljanstvo, članstvo in institucionalna kategorija
upravičenosti niso zamenljivi. V dosjeju se oznaki služkinja in šivilja časovno
prekrivata. Razlog je lahko sočasno delo, samopredstavitev ali razlika med sistemi
razvrščanja. Zbirka razliko izpiše, ne more pa je razsoditi. Oznaka `certain`
pomeni, da sintetični dokument jasno vsebuje navedbo; ne pomeni, da navedba
izčrpno in nevtralno opiše človeka.

Prav tako ločite **znanje jezika**, **rabo jezika** in **jezik, ki ga pripiše
ustanova**. Nemška kategorija v registru, slovensko pismo in navedba o branju
nemščine lahko veljajo hkrati. Nobena ne določi maternega jezika, nacionalne
identitete ali izključnega znanja. Institucionalno vlogo je lahko prevedel ali
napisal posrednik; jezik dokumenta sam zato ne dokazuje osebnega avtorstva.
Učni dosje rabo določi kot pogoj preizkusa, pravi projekt pa bi potreboval
preverljivo podlago o nastanku vsakega dokumenta.

Spreminjajo se tudi besednjaki vlog. Član, poslanec ali samostojni delavec ima
lahko v različnih obdobjih in ustanovah različne pogoje pripadnosti. Ohranite
izvorno izrazje in verzionirajte preslikavo v analitične kategorije. Povezovalni
slovar lahko označi delno ustreznost ali odsotnost ustreznice. Zgodovinskih oznak
ne silite v najbližji sodobni poklic samo zato, da bo graf brez praznih kategorij.

## Zgodovinski čas in čas zapisa

**Čas veljavnosti** se nanaša na obdobje, ki ga trditev opisuje. **Čas zapisa oziroma
spremembe** pove, kdaj je trditev vstopila v zbirko ali se v njej spremenila.
Današnji popravek imena iz leta 1910 spremeni uredniški zapis, ne zgodovinskega
imena na današnji dan. Izhodišče za to razlikovanje pojasnita
[Snodgrass in Ahn 1986](https://doi.org/10.1109/MC.1986.1663327).

Dodatek uporablja polodprte intervale `[start,end)`: leto 1910 je predstavljeno
od `1910-01-01` do `1911-01-01`, pri čemer zadnji datum ni vključen. Tako mejnega
dneva ne štejemo dvakrat v zaporednih obdobjih. Datumi ISO v vaji so gregorijanska
učna konvencija. V pravem projektu zabeležite koledar, pravilo pretvorbe in izvorni
datumski izraz; ne predpostavite, da so vsi viri uporabljali isti koledar.

**Časovno okno dogodka** ni trajanje. Izraz nekega dne v februarju pomeni en
dogodek znotraj razpona, zaposlena ves februar pa stanje skozi razpon. Poizvedba
za dan znotraj prvega intervala najde možni dogodek, ne dokaza, da se je zgodil
prav takrat. Približen datum zahteva izrecno pravilo in ohranjen izvorni izraz.
Neznanih meja ne nadomeščajte z izmišljenimi zgodnjimi ali poznimi datumi.
Izvedljivi vzorec namenoma uporablja omejene intervale; produkcijska shema mora
posebej obravnavati odprte, neznane in sporne časovne meje.

Pri uredniškem popravku dodajte novo trditev s povezavo `supersedes`. Vzorec ohrani
napačni prepis Ana Kovać in popravljeno obliko Ana Kovač. Popravek je dovoljen le,
če ohrani isti vir, subjekt, predikat, kontekst, interval
veljavnosti in vrsto intervala; ena trditev ima lahko največ enega neposrednega
naslednika. Ozko pravilo predstavlja zamenjavo iste uredniške trditve, ne spremembe
zgodovinskega obdobja. Poklicni oznaki pa nista
popravek druga druge, zato nobena ne nadomesti druge. Dnevnik z dodajanjem
novih zapisov omogoča stare poglede, vendar mora za zaupanja vreden časovni žig
skrbeti aplikacija. Ročno vneseni datum ni neodvisno zavarovana revizijska sled
transakcij; zbirka sama ne potrdi, kdo ga je vnesel.

## Poizvedovanje za določen datum

SQL naredi izbirna pravila izrecna. Shranjena poizvedba `queries/at-date.sql`
sprejme subjekt, zgodovinski datum in čas uredniškega posnetka. Osrednji pogoj je:

```sql
a.valid_start <= :as_of AND :as_of < a.valid_end
AND a.recorded_at <= :known_at
```

Izloči tudi trditve, ki so bile do izbranega uredniškega trenutka že nadomeščene.
Branje samo trenutnega pogleda bi bilo napačno pri vprašanju, kaj je zbirka
trdila prejšnji teden. Python posreduje parametre; SQL ne sestavljajte z neposrednim
lepljenjem nepreverjenega imena v ukaz. Skupaj z rezultatom shranite poizvedbo
in različico vhodnih podatkov, da bo izbor mogoče ponoviti.

Dodatek ustvari trinajst vrstic trditev, dvanajst v trenutnem pogledu in en par
potencialno nasprotujočih si statusov, `SYN-A04` / `SYN-A05`. Zgodnejši uredniški
posnetek za leto 1910 pokaže Ana Kovać, popravljeni pa Ana Kovač. Oba še vedno
vsebujeta poklicni oznaki. Poizvedba za leto 1925 pokaže poznejši status in dogodek
rabe nemščine; pisma iz leta 1910 ne spremeni v trajno jezikovno oznako osebe.

Tudi štetje zahteva natančno enoto. Povezovanje ene osebe s tremi imenskimi
izpričbami in dvema vlogama lahko vrne šest vrstic. `COUNT(*)` tedaj šteje
kombinacije povezovanja, ne šestih oseb. Pred uporabo `COUNT(DISTINCT person_id)`
preglejte povezane vrstice. Z levim povezovanjem ohranite entitete brez dokaza
za izbrano razmerje. Nič opažanj razlikujte od opažene ničle: prvo je lahko
posledica vrzeli v dokumentaciji, drugo pa trditev določenega vira.

## Meje, hierarhije in razreševanje entitet

Ozemeljsko pripadnost shranite kot razmerje med krajem in upravno enoto, opredeljeno
s časom in virom. V sintetični vaji nespremenjeno bivališče pri x=550 najprej leži
vzhodno od meje pri x=500, pozneje pa zahodno od meje pri x=600. Gre za spremembo
pristojnosti brez selitve. Tudi resnični ljubljanski kontekst sega čez razpad
Avstro-Ogrske leta 1918, toda izmišljene okrajne črte niso dokaz za ta prehod.
[Zgodovina Mestne občine Ljubljana](https://www.ljubljana.si/sl/mestna-obcina/o-ljubljani/zgodovina-ljubljane/nemirno-20-stoletje).

Upravna pripadnost je lahko hierarhična: župnija znotraj okraja znotraj dežele.
Rekurzivna poizvedba sledi nadrejenim razmerjem, vendar mora vsaka povezava veljati
za izbrano obdobje. Današnja hierarhija ni bližnjica do zgodovinske. Preverjajte
cikle in več nadrejenih enot; prekrivanje civilnih in cerkvenih pristojnosti je
lahko pomembna lastnost gradiva, ne napaka za izbris.
[Rekurzivne poizvedbe SQLite](https://www.sqlite.org/lang_with.html).

**Razreševanje entitet** presoja, kateri zapisi se nanašajo na isto entiteto.
Namesto združevanja po podobnosti imen ohranite kandidate, dokaze in odločitve.
Predlagano združitev preverite z datumi, kraji, vlogami in neodvisnostjo virov.
Napačna združitev poveže dve biografiji ter prenese napako v zemljevide in omrežja.
Zavrnjena povezava Meker/Meeker iz referenčne plasti paketa arhivskih zapletov je
uporaben opomin, da
podobnost zapisa ni dovolj za identifikacijo. Tudi nezdružitev naj ima utemeljitev.

## Preverjanje, občutljivost in izgube pri izvozu

Normalizacija zmanjša anomalije pri popravljanju; namerna denormalizacija lahko
ustvari dokumentiran analitični posnetek. Izvedite jo s shranjeno poizvedbo, ki
navede datum, pravilo izbire in različico vhodov. Normalizirane tabele oziroma
raven trditev naj ostanejo izhodišče. Sicer ročno spremenjeni izvoz in zbirka
postopoma postaneta dve tekmovalni izdaji brez pojasnjene uredniške odgovornosti.

Omejitve zaznajo podvojene ključe, manjkajoče sklice in obrnjene intervale.
Pri vsaki povezavi s SQLite pred uvozom vključite tuje ključe in preverite,
ali nastavitev učinkuje. Nato preverite celovitost zbirke in sklice tujih ključev.
Ti testi ne preverijo resničnosti napisa pod fotografijo ali ustreznosti kategorije.
[Dokumentacija tujih ključev SQLite](https://www.sqlite.org/foreignkeys.html).

Za analizo občutljivosti primerjajte vse prekrivajoče se trditve o statusu s
pravilom, ki izbere samo občinski register. Za 1910-06-15 prvo pravilo vrne dve
oznaki, drugo eno. Število oseb ostane ena. Poklicna porazdelitev se spremeni
zaradi drugačnega pravila izbire dokazov, ne zato, ker bi oseba zamenjala delo.
Objavite oba rezultata in identifikator izločene trditve. Poizvedbo o ozemeljski
pripadnosti ponovite tik pred 1920-01-01 in na ta dan, da preverite meji intervalov.

Ravni CSV ne more uveljavljati tujih ključev, ohraniti pogledov zbirke ali vseh
razmerij mnogo proti mnogo spraviti v eno osebno vrstico brez podvajanja oziroma
združevanja. Izvozite povezane tabele s stabilnimi identifikatorji, slovarjem in
poizvedbami. Kjer je pomembno, vključite izvorno besedilo in uredniške časovne žige.
Ločite prazno, neznano, neuporabljivo in zadržano vrednost. Na majhnem vzorcu
preverite ponovni uvoz. Dostopna tabela za branje je analitični izdelek, ne
varnostna kopija brez izgub.

## Hibridno modeliranje

Vsega ni treba zaupati eni predstavitvi. Relacijske tabele hranijo entitete in
poizvedljive trditve; TEI/XML besedilne različice in uredniško zgradbo; GeoPackage
časovno opredeljene geometrije; graf pa omogoči raziskovanje razmerij. Faksimili
in diplomatski prepis ohranijo dokazno gradivo, prozne opombe pa razlike, ki jih
ni smiselno siliti v nadzorovana polja. Predstavitve povežite s skupnimi identifikatorji
in verzioniranimi povezavami. Vprašajte se: katere razlike morajo biti poizvedljive,
katere morajo ostati obnovljive iz gradiva in katere naj se uprejo formalizaciji?
Isti dosje nadaljujeta poglavji [GIS](gis-spatial-humanities.md) in
[Omrežja](networks-visualization.md).

## Vaja

Uporabite parni [postopek za trditve v SQLite](../workflows/data/model-changing-names-statuses-and-boundaries-in-sqlite.md).
Prenesite dodatek, preberite pregled pravic in v razširjeni mapi zaženite
`python run.py --output output`. Pri ponovitvi izberite novo izhodno mapo.
Datoteke `assertions-1910_early.csv`, `assertions-1910_corrected.csv` in
`status-conflicts.csv` primerjajte z dosjejem. Ločeno pojasnite popravek zapisa
in nesoglasje, ki po popravku ostaja. Pri tem izrecno navedite oba časa poizvedbe.

Oddajte skico sheme, obe štetji statusov, tabelo rezultatov s sklici na vire in
kratko pojasnilo izvoznih izgub. Ročno sledite vsakemu rezultatu za A do dokumenta
ali opombe. V ločeni delovni kopiji kot negativni preizkus poskusite vnesti
osiroteli tuji ključ. Ne spreminjajte ohranjenega vira in izmišljenih identitet
ne objavljajte kot zgodovinske ugotovitve. Tudi po uspešnih samodejnih testih
ostajata potrebna človeški metodološki in slovenski jezikovni pregled.

## Refleksija

- Katera navidezna protislovja izvirajo iz različnih kontekstov in ne napačnih navedb?
- Kaj vaša poizvedba pomeni za dogodek z negotovim datumom?
- Katera oseba izgine, če levo povezovanje zamenjate z notranjim?
- Ali lahko bralec samo iz izvoza razbere pravilo izbire dokazov?

## Povzetek

Relacijska zbirka omogoči poizvedovanje po izbranih razlikah, trditev pa ne spremeni
v resnico. Stabilni identifikatorji, kontekstualna imena, opredeljena razmerja,
zgodovinski intervali in uredniška zgodovina pomagajo ohraniti spremembe in nesoglasja.
Prepričljiv argument vključuje poizvedbo, sled do vira, primerjavo občutljivosti
in izrecno pojasnilo, kaj ostaja zunaj sheme.

## Nadaljnje branje

- Codd, E. F. 1970. »A Relational Model of Data for Large Shared Data Banks.« *Communications of the ACM* 13(6): 377–387. [DOI](https://doi.org/10.1145/362384.362685). Relacijska organizacija in skladnost.
- Bradley, John, in Harold Short. 2005. »Texts into Databases: The Evolving Field of New-style Prosopography.« *Literary and Linguistic Computing* 20(Suppl): 3–24. [DOI](https://doi.org/10.1093/llc/fqi022). Trditve, povezane z zgodovinskimi viri.
- Snodgrass, Richard, in Ilsoo Ahn. 1986. »Temporal Databases.« *Computer* 19(9): 35–42. [DOI](https://doi.org/10.1109/MC.1986.1663327). Različne časovne razsežnosti.
- SQLite. [Tuji ključi](https://www.sqlite.org/foreignkeys.html), [datumske funkcije](https://www.sqlite.org/lang_datefunc.html) in [WITH oziroma rekurzivne poizvedbe](https://www.sqlite.org/lang_with.html). Operativni viri preverjeni 3. septembra 2026; vzorec uporablja lastno pravilo omejenih intervalov.
