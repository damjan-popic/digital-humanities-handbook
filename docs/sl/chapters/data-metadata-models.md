---
title: "Podatki, metapodatki in modeli"
description: "Kako humanistično gradivo postane sledljiv zapis, ne da bi izbrisali besedilo vira, negotovost, različice ali interpretativne odločitve."
tags: [podatki, metapodatki, modeliranje, provenienca, negotovost]
status: draft
---

# Podatki, metapodatki in modeli

## Učni cilji

Po tem poglavju boste znali:

- razlikovati med izvornimi predmeti, metapodatki ponudnika, raziskovalnimi podatki, metapodatki in dokumentacijo;
- pojasniti, zakaj je podatkovni model interpretacija in ne nevtralno skladišče;
- oblikovati stabilne identifikatorje, natančne navedbe mesta v viru in preprosto relacijsko zgradbo;
- poleg normaliziranih datumov, imen in nadzorovanih izrazov ohraniti zapis iz vira;
- izrecno predstaviti negotovost, manjkajoče vrednosti, dvojnike, ponatise in različice;
- izdelati preverljivo sled provenience in popravkov;
- izbrati metapodatkovni standard ali slovar za jasno določen namen in preizkusiti njegovo ustreznost.

## Pred začetkom

Odprite tabelo, ki ste jo že uporabili pri raziskavi. Ali lahko brez vprašanja
avtorju ugotovite, kaj predstavlja ena vrstica, kateri stolpci so obvezni, kaj
pomeni prazna celica, od kod prihaja posamezna vrednost ter ali je ime
prepisano ali normalizirano? Se lahko iz vrstice vrnete k strani, vrstici,
delu slike ali kataloškemu zapisu? Če ne, tabeli ne manjka samo urejenost,
temveč tudi pomen in provenienca.

Poznavanje podatkovnih zbirk ali programiranja ni potrebno. Potrebujete majhno
zbirko ali [ZIP učnega paketa *Arhivsko
trenje*](../../assets/downloads/archival-friction-v1.zip); za pregled zgradbe
je na voljo tudi [izvorno drevo paketa](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction).
Pripravili boste model zapisov, podatkovni slovar, dnevnik popravkov in
poročilo o kakovosti. Dober rezultat ohrani dokazno gradivo tudi tedaj, ko
vrednost normalizirate ali pustite nerazrešeno. Osrednja napaka je tiho
nadomeščanje: tabela postane navidezno dosledna, vendar izbriše, kaj so
dejansko navedli vir, ponudnik ali raziskovalec.

Vprašanje in vzorčni okvir najprej opredelite v poglavju [Od vprašanja do
metode](research-design.md). Širšo razmejitev virov, predstavitev, rezultatov
in dokaznega gradiva pojasnjujejo [Modeli, dokazno gradivo in
interpretacija](models-evidence-interpretation.md). Preglednični postopki v
[Temeljih znanstvenega dela](../foundations/scholarly-work.md)
prikazujejo, kako brez programiranja ločite izvorno, očiščeno, odločevalsko in
izhodno raven.

## Podatki nastanejo za določen namen

V humanistični raziskavi so **podatki** zabeležena opazovanja ali predstavitve,
ki jih uporabljamo pri raziskovanju. **Metapodatki** opisujejo predmete,
zapise ali postopke: naslov, datum, ustvarjalca, jezik, pravice, zbirko, mesto
v viru, stanje prepisa ali preoblikovanje. **Dokumentacija** razloži model,
pravila, zgodovino in omejitve, ki jih iz samih celic ni mogoče razbrati.

Vloge so odvisne od vprašanja. Datum objave je pri iskanju besedila
metapodatek, v zgodovini založništva pa analizirani podatek. Kataloški opis je
metapodatek o predmetu in hkrati zgodovinski vir o ustanovi, ki ga je
izdelala.

Johanna Drucker z izrazom *capta* — kar je bilo zajeto — poudari, da
humanistični podatki nastajajo z izbiranjem in določanjem parametrov, namesto
da bi jih našli že pripravljene.[^drucker] Izraz je koristno vprašanje in ne
zahteva, da preimenujete vsako datoteko. Vprašajte: kdo je izbral enoto, po
katerem modelu, iz katerega ohranjenega gradiva in s katero izgubo?

## Model je skupek odločitev

**Podatkovni model** določa, katere vrste stvari v projektu obstajajo, katere
lastnosti jih opisujejo, kako so povezane in katere omejitve veljajo.
Preglednica z eno vrstico za vsak slikovni napis je že model. Napis obravnava
kot samostojno enoto, izbere polja in odloči, katere podrobnosti bodo ostale v
opombah.

Razlikujte tri ravni:

1. **Konceptualni model** v jeziku stroke poimenuje entitete in razmerja:
   številko, stran, sliko, napis, osebo, dogodek, različico in vir.
2. **Logični model** jih prevede v tabele, polja, identifikatorje, nadzorovane
   vrednosti in omejitve.
3. **Fizična predstavitev** jih shrani v CSV, preglednico, XML, JSON,
   relacijsko podatkovno zbirko ali drugo obliko.

Menjava programske opreme ne bo popravila slabega modela, če prvih dveh ravni
ne premislite znova. Po drugi strani lahko premišljena majhna datoteka CSV
uresniči povsem utemeljen model.

Geoffrey Bowker in Susan Leigh Star pokažeta, da klasifikacije organizirajo
delo in razporejajo posledice, pri tem pa kot infrastruktura postanejo komaj
opazne.[^bowker-star] Zato ločite kategorije vira, kategorije ponudnika in
svoje analitične kategorije. Zgodovinska polemična oznaka je dokaz o stališču
publikacije, ne samodejno sprejemljiva sodobna predmetna oznaka.

## Najprej določite pomen zapisa, nato polja

Dopolnite poved:

> Vsaka vrstica predstavlja natanko en/eno ________.

Če je možnih več odgovorov, tabela meša ravni. Ena vrstica ne more varno
predstavljati tako časopisne številke kot vseh oseb na slikah. Ponavljanje
metapodatkov o številki v vsaki vrstici za osebo je pri majhnem izvozu lahko
sprejemljivo, vendar so v osnovnem modelu to še vedno ločene entitete.

Za ilustrirano periodiko bi lahko izdelali skromen relacijski model:

- `stevilke(stevilka_id, naslov_iz_vira, datum_stevilke, vir_id, pravni_status)`;
- `strani(stran_id, stevilka_id, oznaka_strani, datoteka_id)`;
- `enote(enota_id, stran_id, vrsta_enote, napis_iz_vira, obmocje)`;
- `osebe(oseba_id, prednostna_oznaka, normativni_uri, stanje_povezave)`;
- `osebe_enot(enota_id, oseba_id, vloga, gotovost)`;
- `odlocitve(odlocitev_id, zapis_id, polje, stara_vrednost, nova_vrednost, dokaz)`.

Obe zasnovi sta utemeljeni, vendar nista enakovredni:

| Shema | Kaj omogoča | Kaj zabriše ali podraži |
| --- | --- | --- |
| Ravna tabela enot | Hitro primerjavo z virom in nizko vstopno oviro pri učenju s CSV | Ponavlja podatke o številki; oteži skupinske portrete, različice in konkurenčne identifikacije |
| Zgornje relacijske tabele | Poizvedbe po osebah, enotah in različicah ter zapisano negotovost | Zahteva povezovanje tabel in oteži neposredno branje po straneh vira |

## Identifikatorji pred oznakami

Imena in naslovi so oznake, ne zanesljivi identifikatorji. Spreminjajo se,
ponavljajo, uporabljajo različne pisave in vsebujejo zgodovinske zapisne
različice. Vsakemu zapisu dodelite stabilen, vsebinsko nevtralen projektni
identifikator, denimo `AF-P2-003`. Nikoli ga ne uporabite za drug predmet.
Identifikatorje ponudnika in URI-je zunanjih normativnih zbirk hranite v
ločenih poljih.

Dober identifikator ne trdi, da dva zapisa označujeta isto osebo. Zagotavlja
samo stabilnost vaših zapisov. Identiteta je dokazna odločitev, ki jo izrazite
z razmerjem `same_as`, `possible_match`, `duplicate_of`, `reprint_of` ali
`version_of` ter ji dodate stanje in utemeljitev.

Vsak vsebinski zapis potrebuje tudi **natančno mesto v viru**: stran, stolpec,
slikovno območje, folij, časovno oznako ali arhivsko signaturo, na podlagi
katere lahko drugi bralec preveri trditev. Splošna povezava na domačo stran
zbirke ni zadosten lokator.

## Plasti ohranite, ne prepisujte

Utemeljeno se lahko razlikujejo vsaj štiri vrednosti:

1. **oblika v viru** — vidna v zgodovinskem predmetu;
2. **vrednost ponudnika** — kataloški metapodatek ali strojni OCR;
3. **raziskovalčev prepis ali normalizacija** — dokumentiran popravek;
4. **analitična kategorija** — vrednost, ustvarjena za določeno primerjavo.

Hranite jih v različnih poljih ali tabelah. Če v napisu piše »Mr. Meker«, se
lahko besedilo OCR z njim ujema, iskanje po normativnih zbirkah pa predlaga
»Ezra Meeker«. Pregledano stanje povezave je lahko `candidate_rejected`. Če
natisnjeno obliko nadomestite s kandidatom, je vir videti gotovejši, kot je v
resnici, in poznejše preverjanje ni več mogoče.

Tudi kadar vrednosti ločite po poljih, ohranite štiri datotečne ali
podatkovne plasti: nespremenljivo **izvorno oziroma surovo plast**;
**vmesno plast** s kandidati in ponovljivimi pretvorbami; **obdelano oziroma
modelirano plast** s sprejeto razlago za določen namen; ter **odločitveno
plast**, v kateri beležite posege, zavrnitve in nerešene primere. Vmesna plast
ni dokaz že zato, ker jo je izdelalo orodje, obdelana plast pa ne nadomesti
vira.

Učni paket vloge map opredeli še natančneje. `source/` vsebuje samo
nespremenjeni PDF, zajeta zapisa ponudnikov in nespremenjeni ponudnikov OCR;
`reference/` vsebuje priročniška opazovanja, uredniške odločitve in
referenčni prepis; `teaching/` prijavlja sintetične motnje; `raw/`,
`interim/`, `cleaned/`, `output/`, `validation/` in `known-problems/` pa
ohranjajo nadaljnjo sled dokazov.

Dnevnik popravkov naj vsebuje vsaj identifikator odločitve, zapis in polje,
prejšnjo in novo vrednost, dejanje, dokaz, odgovorno osebo ali postopek, datum
ter različico pravila. Sistematične težave odpravite s ponovljivim
preoblikovanjem, odločitve o posameznih virih pa vpišite v dnevnik. Nikoli ne
»čistite« edinega izvoda.

## Provenienca je veriga odgovornosti

**Provenienca** zapisuje, od kod je predstavitev prišla in kako se je
spreminjala. Skupina standardov W3C PROV razlikuje entitete, dejavnosti in
akterje, vendar majhnemu projektu za koristno uporabo te razlike ni treba
vzpostaviti celotnega sistema RDF.[^prov] Razumljiv dnevnik lahko vsebuje:

| Nastala entiteta | Dejavnost | Uporabljena entiteta | Odgovorni akter | Čas/različica |
| --- | --- | --- | --- | --- |
| shranjeni PDF | prenos brez spremembe bajtov | spletni naslov datoteke ponudnika | skrbnik učnega paketa | datum dostopa in kontrolna vsota |
| izvorni zapis | ročni izbor in prepis | stran in območje v PDF-ju | raziskovalec | šifrant v1 |
| očiščeni zapis | dokumentiran popravek | surovi zapis in odločitev | raziskovalec ali program | datum/različica izvedbe |
| grafikon | združevanje | očiščena objava podatkov | poimenovani postopek | programska oprema in nastavitve |

Kontrolne vsote dokazujejo enakost bajtov, ne pristnosti ali pravilnosti.
Ujemajoči se zgoščeni vrednosti potrjujeta, da sta datoteki enaki. Ne
potrjujeta, da je ponudnik predmet pravilno opisal ali da je vaš prepis zvest.

## Datum potrebuje obliko, vrednost in stopnjo gotovosti

Datumi v humanističnem gradivu so pogosto relativni, približni, sporni ali
nepopolni. Ohranite vsaj:

- zapis v viru, na primer `dne 1. t. m.`;
- normalizirano vrednost, na primer `1925-02-01`;
- stanje, kot je `exact`, `derived_from_relative_date`, `approximate`,
  `uncertain` ali `unknown`;
- pravilo in kontekstualni dokaz, uporabljena pri normalizaciji.

Specifikacija Extended Date/Time Format (EDTF) Kongresne knjižnice ponuja
zapis za negotove (`1984?`), približne (`2004-06~`), nedoločene datume in
intervale.[^edtf] Uporabite jo samo, če programska oprema podpira navedeno
raven specifikacije in lahko bralci obnovijo izvirno obliko. Pri majhnem
projektu je lahko preprost interval z ločenim poljem gotovosti bolj
interoperabilen. Zapisa »verjetno 1925« nikoli ne spreminjajte v natančni datum
`1925-01-01` zgolj zato, ker preglednica zahteva dan.

## Natisnjena identiteta, struktura enote in povezovanje z normativnimi zbirkami

Normativne zbirke lahko povežejo zapisne različice in ponudijo trajne
identifikatorje, vendar je vsaka povezava raziskovalna trditev. Ločeno
ohranite:

- `printed_person_or_group`, oznako osebe ali skupine iz vira;
- `entity_structure` (`zero_people`, `one_person` ali `multiple_people`);
- normalizirano prikazno ime, če ga potrebujete;
- ime normativne zbirke in `authority_candidate`, kandidatni URI ali oznako;
- `authority_link_status` (`not_attempted`, `not_reconciled`,
  `candidate_rejected`, `accepted`, `unresolved` ali `not_applicable`);
- dokaze za povezavo, odločitev in ime pregledovalca;
- datum dostopa, saj se vmesniki in zapisi spreminjajo.

Ne sprejmite prvega iskalnega zadetka samo zato, ker se ime ujema. Preverite
datume, vloge, kraje, povezane osebe in kontekst vira. Zgodovinski časopis je
lahko ime zapisal narobe; dve osebi v istem času sta ga lahko delili;
normativni zapis je lahko nepopoln. Gettyjevi slovarji na primer ponujajo
trajne identifikatorje in zapisne različice, vendar sami sebe opisujejo kot
spreminjajoč se in področno omejen vir, ne kot univerzalni seznam oseb in
krajev.[^getty]

Povezovanje razumite kot **dodajanje povezave z dokazom**, ne kot
nadomeščanje zapisa iz vira. Jasno natisnjeno ime ni nerešena identiteta samo
zato, ker mu niste dodali URI-ja, skupinski portret pa ni ena nerešena oseba.
Če preizkušeni kandidat nima dovolj podpore, je `candidate_rejected`
veljaven in preverljiv rezultat.

## Manjkajoče vrednosti imajo različne pomene

Prazna celica lahko pomeni: ni znano, ni zapisano, ni relevantno, ni čitljivo,
je zadržano, še ni pregledano ali se je izgubilo med obdelavo. Ta stanja imajo
različne zgodovinske in etične posledice. Dovoljene oznake manjkajočih
vrednosti določite v podatkovnem slovarju in po potrebi dodajte ločeno opombo.

Neznanih vrednosti ne nadomeščajte z ničlo. »Nismo našli ohranjenega zapisa«
ni isto kot »dogodkov je bilo nič«. Zadržane vrednosti ne objavite kot
`unknown`, če s tem izbrišete odločitev skupnosti ali pravilo varovanja
zasebnosti. Na primerni ravni zapišite vrsto omejitve, ne da bi razkrili
varovano vsebino.

## Dvojniki, ponatisi in različice so razmerja

Povsem enake datoteke lahko odkrijete s kontrolnimi vsotami, toda identiteta
dokumenta ni zgolj enakost bajtov. Ponatisnjen članek, popravljena izdaja,
izvoz OCR in nov posnetek iste strani imajo lahko skupno vsebino, vendar v
raziskavi opravljajo različne naloge.

Namesto enega preobremenjenega polja `duplicate` uporabite razmerja z
določenim pomenom:

- `duplicate_of`: isti zapis je bil vnesen dvakrat;
- `copy_of`: drug nosilec v bistvenem istega predmeta;
- `reprint_of`: ponovna objava v novi številki ali publikaciji;
- `version_of`: povezano stanje s pomembno spremembo;
- `derived_from`: OCR, normalizacija, izrez ali analiza, izdelani na podlagi
  druge predstavitve.

Nato določite analitično pravilo. Raziskava širjenja besedila lahko šteje
ponatise; besedna analiza morda ohrani samo eno besedilno različico;
raziskava OCR lahko primerja več posnetkov iste strani. Ne brišite razmerij,
ki jih bodo drugi raziskovalci potrebovali za rekonstrukcijo vaše odločitve.

## Standard je orodje, ne samodejno jamstvo kakovosti

Standard ponudi skupne izraze ali strukture, ne more pa odločiti, kaj mora vaš
projekt opazovati. Izhajajte iz zahtev, nato pa izberite majhen **aplikacijski
profil**: polja, obveznosti, slovarje in lokalna pravila, ki jih boste dejansko
uporabljali.

- [DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)
  ponujajo splošne medpodročne lastnosti in trajne URI-je izrazov.
- [TEI P5](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/) predstavlja
  zgradbo besedil in uredniške alternative; element `<choice>` lahko združi
  izvirno in popravljeno obliko, ne da bi eno izbrisal.[^tei]
- [CIDOC CRM](https://cidoc-crm.org/get-last-official-release) ponuja
  konceptualni model za kulturnodediščinske entitete in razmerja, osredinjena
  na dogodke. Zadnja uradna različica, navedena 2. septembra 2026, je bila
  7.1.3; novejše različice na seznamu so bile osnutki.[^cidoc]

Spletne strani vmesnikov in specifikacij so spremenljive, zato zapišite datum
dostopa in ob zahtevi po natančni skladnosti določite različico. Majhna
lokalna shema z jasnimi preslikavami je lahko boljša od trditve o popolni
skladnosti z obsežnim standardom, ki ga uporabljate le površno.

Ustreznost preizkusite s konkretnimi vprašanji. Ali profil ohrani zapis iz
vira in normalizirano vrednost? Ali loči negotovo identiteto od potrjene? Ali
lahko zapiše pravice za vir in za vaše anotacije? Ali izvoz in ponovni uvoz
ohranita jezik, ločevalna znamenja, identifikatorje in razmerja?

## Preverjanje kakovosti majhnega raziskovalnega nabora

Združite strukturno in interpretativno preverjanje:

- identifikatorji so enkratni, neprazni in stabilni;
- tuji ključi kažejo na obstoječe zapise;
- obvezna mesta v viru in podatki o pravicah so navzoči;
- nadzorovane vrednosti so vključene v ustrezno različico slovarja;
- normalizirani datumi ustrezajo navedeni natančnosti in gotovosti;
- izvirni nizi ostanejo nespremenjeni;
- sprejete povezave z normativnimi zbirkami imajo zabeležen dokaz;
- razmerja med dvojniki in različicami so določena ter ne tvorijo kroga;
- število vrstic in ohranjeni identifikatorji se ujemajo z dnevnikom
  odločitev;
- stratificirani vzorec pravilno vodi nazaj k faksimilu;
- izvozi ohranijo besedilo UTF-8 in začetne znake identifikatorjev.

Samodejno preverjanje najde strukturna protislovja. Ne more odločiti, ali je
slikovni napis politično nevtralen, povezava osebe zgodovinsko prepričljiva
ali kategorija primerna. Združite ga s pregledom virov.

## Razdelan primer: en predmet in osem referenčnih opazovanj

Učni paket vsebuje en pristen predmet, dvostransko časopisno številko. V mapi
`reference/` je osem priročniških, na viru utemeljenih opazovanj: eno o
številki in sedem o prispevkih. Tabela hrani prepise oznak, OCR ponudnika,
obseg in stanje datumov, ločeni datum številke, natisnjene oznake oseb ali
skupin, strukturo enote, normativne kandidate in stanja povezav, mesta v viru
ter opombe o dokazih. Mapa `teaching/` uvede štiri prijavljene učne težave.
Izdelana surova tabela ima zato devet vrstic: tri spremenjena polja in eno
podvojeno vrstico.

Pregled opravite tako:

1. Shranjeni PDF preverite pri ponudniku in s kontrolno vsoto SHA-256.
2. Potrdite, da vseh osem oznak referenčnih opazovanj vodi do strani in območja.
3. Vsako spremenjeno surovo polje primerjajte s faksimilom, ne samo s tabelo
   pravilnih odgovorov.
4. Velikost začetnice v slikovnem napisu popravite, kadar je podoba jasna.
5. Izločite samo vrstico, ki je izrecno označena kot sintetični dvojnik;
   izvorno enoto ohranite.
6. Zavrnite tiho spremembo »Meker« v »Meeker«; Ezro Meekerja ohranite kot
   pregledanega kandidata s stanjem `candidate_rejected`, ne kot sprejeto
   identiteto.
7. Datuma 1925-02-01 in 1925-01-27 izpeljite po izrecnih pravilih, datum
   nastanka fotografije struge pa pustite prazen oziroma `unknown`; datum
   številke je samo kontekst.
8. Preverite osem očiščenih oznak, osem pristnih uredniških odločitev, štiri
   razveljavitve sintetičnih motenj in nespremenjene bajte izvorne datoteke.

Očiščeni rezultat ne trdi, da je vseh osem zapisov popolnih. Trdi, da ima
vsaka ohranjena vrednost določeno dokazno stanje in da jo je mogoče
preveriti.

## Vaja: izdelajte in preverite model zapisov

Uporabite [ZIP učnega paketa](../../assets/downloads/archival-friction-v1.zip),
katerega [izvorno drevo je na voljo za pregled](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction),
ali pet do deset zapisov s svojega področja. Pripravite:

1. konceptualno skico entitet in razmerij;
2. eno ali več tabel, v katerih ima vsaka vrstica en sam pomen;
3. stabilne notranje identifikatorje in natančna mesta v viru;
4. ločene izvorne, ponudnikove, normalizirane in analitične vrednosti, kadar
   se razlikujejo;
5. podatkovni slovar, ki za vsako polje določa vrsto, dovoljene vrednosti,
   manjkajočnost in obveznost;
6. en negotov datum, enega nerazrešenega kandidata iz normativne zbirke in eno
   opredeljeno razmerje dvojnika ali različice;
7. dnevnik popravkov in provenience;
8. poročilo o kakovosti s številom vrstic, preverjanjem identifikatorjev in
   dvema ročnima primerjavama z virom.

**Preverjanje:** drug bralec naj brez dodatnih vprašanj rekonstruira eno
normalizirano vrednost in pojasni eno nerazrešeno vrednost. **Pogosta
napaka:** če je očiščena tabela gotovejša od vira, dnevnik odločitev pa ne
pojasni, zakaj, pred analizo znova vzpostavite ločene ravni.

## Refleksija

- Katera polja opisujejo zgodovinski predmet in katera vaše srečanje z njim?
- Katera kategorija prihaja iz vira, od ponudnika, iz standarda ali iz
  raziskovalnega vprašanja?
- Ali lahko povezava z zunanjo normativno zbirko v zgodovinsko dvoumen zapis
  vnese sodobno ali področno omejeno identiteto?
- Katere prazne vrednosti kažejo na arhivski molk in katere na nedokončano
  delo?
- Kaj bi izgubili, če bi vse ponatise ali različice združili v en »glavni«
  zapis?

## Povzetek

Humanistični podatki so strukturirane predstavitve, izdelane za določen
namen. Model opredeli entitete, lastnosti, razmerja in omejitve, preden jih
datotečna oblika uresniči. Stabilni identifikatorji ohranijo kontinuiteto
zapisov; natančna mesta v viru vrnejo trditve k dokaznemu gradivu. Izvorne,
ponudnikove, normalizirane in analitične vrednosti morajo ostati ločljive.

Datum zahteva zapis iz vira, normalizirano vrednost in stopnjo gotovosti. Ime
zahteva z dokazom podprto povezovanje, ne samodejnega nadomeščanja.
Manjkajoče vrednosti, dvojniki, ponatisi in različice nosijo pomen, zato jih
modelirajte, namesto da bi jih izbrisali. Dnevniki provenience in popravkov
določijo odgovornost za vsako preoblikovanje. Standard lahko izboljša
izmenjavo, če ga uporabite v jasno opredeljenem in različico označenem
aplikacijskem profilu, vendar skladnost ne nadomesti kritike virov. Dobri
podatki niso dejstva brez trenja, temveč zapisi, katerih nastanek, negotovost
in omejitve lahko vedno pregledate.

## Nadaljnje branje in viri

- Bowker, Geoffrey C., in Susan Leigh Star. [*Sorting Things Out:
  Classification and Its
  Consequences*](https://mitpress.mit.edu/9780262024617/sorting-things-out/).
  MIT Press, 1999. Spletna stran založnika, dostop 2. septembra 2026.
- CIDOC CRM Special Interest Group. [*Definition of the CIDOC Conceptual
  Reference Model*, različica
  7.1.3](https://cidoc-crm.org/get-last-official-release). Februar 2024.
  Dostop 2. septembra 2026.
- Dublin Core Metadata Initiative. »[DCMI Metadata
  Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/).«
  Priporočilo DCMI, objavljeno 20. januarja 2020. Dostop 2. septembra 2026.
- Drucker, Johanna. »[Humanities Approaches to Graphical
  Display](https://dhq.digitalhumanities.org/vol/5/1/000091/000091.html).«
  *Digital Humanities Quarterly* 5, št. 1 (2011). Dostop 2. septembra 2026.
- Library of Congress. »[Extended Date/Time Format (EDTF)
  Specification](https://www.loc.gov/standards/datetime/).« 4. februar 2019.
  Dostop 2. septembra 2026.
- Moreau, Luc, in Paolo Missier, ur. »[PROV-DM: The PROV Data
  Model](https://www.w3.org/TR/prov-dm/).« Priporočilo W3C, 30. april 2013.
  Dostop 2. septembra 2026.
- TEI Consortium. [*TEI P5: Guidelines for Electronic Text Encoding and
  Interchange*](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/),
  različica 4.11.0, 18. februar 2026. Dostop 2. septembra 2026.

[^drucker]: Drucker, »Humanities Approaches to Graphical Display«, o podatkih
    kot *capta* in interpretativnem značaju določanja parametrov.
[^bowker-star]: Bowker in Star, *Sorting Things Out*, zlasti njuna analiza
    klasifikacijskih sistemov kot infrastrukture s konkretnimi posledicami.
[^prov]: W3C, »PROV-DM«. Formalni model tu ni obvezen; pomembna minimalna
    zahteva je praktično razlikovanje med entiteto, dejavnostjo in odgovornim
    akterjem.
[^edtf]: Library of Congress, »EDTF Specification«. Specifikacija iz leta
    2019 določa ravni skladnosti ter zapis za zmanjšano natančnost, negotovost,
    približnost in intervale.
[^getty]: Getty Research Institute, »[Obtain the Getty
    Vocabularies](https://www.getty.edu/research/tools/vocabularies/obtain/).«
    Stran dokumentira identifikatorje, pogoje odprtih podatkov in spreminjajoče
    se načine dostopa. Dostop 2. septembra 2026.
[^tei]: TEI Consortium, »[`<choice>`](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-choice.html)«,
    P5, različica 4.11.0. Dostop 2. septembra 2026.
[^cidoc]: CIDOC CRM Special Interest Group, »[Versions of the
    CIDOC-CRM](https://cidoc-crm.org/versions-of-the-cidoc-crm).« Dostop 2.
    septembra 2026.
