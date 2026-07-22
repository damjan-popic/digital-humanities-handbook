---
title: "Kritične infrastrukture: moč, dostop in vzdrževanje"
description: "Kako zbirke, standardi, vmesniki, delo in vzdrževanje oblikujejo digitalnohumanistično dokazno gradivo še pred analizo."
tags: [temelji, infrastruktura, moč, dostop, vzdrževanje]
status: draft
---

# Kritične infrastrukture: moč, dostop in vzdrževanje

## Učni cilji

Po tem poglavju boste znali:

- infrastrukturo opredeliti kot mrežo razmerij in ne kot seznam naprav;
- razlikovati med raziskovalno, projektno, informacijsko oziroma vmesniško in družbeno infrastrukturo;
- pojasniti, kako odločitve o arhivu, opisu, tehnologiji in dostopu vplivajo na humanistično trditev;
- pokazati, da standardi sodelovanje hkrati omogočajo in omejujejo predstavljanje gradiva;
- prepoznati vzdrževalno delo ter presoditi, kako upravljanje razporeja priznanje, pristojnost in tveganje;
- razlikovati med dostopom in dostopnostjo ter med več pomeni odprtosti;
- pojasniti različna namena načel FAIR in CARE;
- pripraviti ponovljivo presojo infrastrukture digitalne zbirke ali orodja.

## Pred začetkom: kaj omogoča navidezno preprosto iskanje?

V iskalno polje zgodovinskega korpusa vpišemo besedo in v nekaj sekundah dobimo zadetke. Videti je, kakor da postopek vključuje le bralca, polje in indeks. V resnici je odvisen od nastanka in ohranitve zapisov, institucionalnega izbora in financiranja, katalogizacije, skeniranja, optičnega razpoznavanja znakov (OCR), členjenja člankov, identifikatorjev, metapodatkov, strežnikov, programske opreme, razvrščanja, odločitev o pravicah ter ljudi, ki vse našteto vzdržujejo. Kaj bi lahko spremenilo rezultat, ne da bi spremenili poizvedbo?

**Predznanje:** preberite poglavje [Modeli, dokazno gradivo in interpretacija](models-evidence-interpretation.md), zlasti razpravo o izboru, kategorijah in negotovosti. Programiranje ni potrebno. **Vhod za vajo:** digitalna zbirka ali raziskovalna storitev, ki jo smete javno opisati, ter predlagana humanistična trditev. **Rezultat:** presoja infrastrukture z razločenimi vrstami dokaznega gradiva. **Preverjanje:** drugi bralec mora ločiti vaša opažanja, navedbe ustanove, lastne preizkuse in interpretacije. **Omejitve:** ne obidite nadzora dostopa, ne razkrivajte občutljivih zapisov in pravne dostopnosti ne zamenjujte z etičnim dovoljenjem.

Osrednja trditev poglavja je preprosta, vendar zahtevna: **še preden izberemo algoritem, infrastruktura vpliva na to, kaj se ohrani in digitalizira, kako je gradivo opisano, kdo ga lahko uporablja, kateri jeziki so podprti, čigavo delo je vidno in katere trditve so utemeljive.**

## Infrastruktura postane opazna ob okvari

Infrastruktura ni zgolj strojna ali programska oprema, prav tako ne pomeni samo velike ustanove. Je **relacijska ureditev** ljudi, organizacij, standardov, financiranja, utečenih postopkov, znanja, identifikatorjev, vmesnikov, repozitorijev, omrežij, materialnih sistemov in vzdrževanja. Neka ureditev postane infrastruktura v razmerju do prakse: trajni identifikator podpira navajanje le, dokler delujejo registri, storitve za razreševanje povezav, metapodatki, pogodbe in lokalni postopki.

Star in Ruhleder infrastrukturo opišeta kot vpetost v druge ureditve in zgrajenost na podedovani osnovi; njena uporaba je odvisna od pripadnosti skupnosti in poznavanja dogovorov. Okvara lahko običajno neopazne odvisnosti privede v ospredje.[^star-ruhleder] Trditev, da infrastruktura postane vidna ob okvari, je uporabno raziskovalno vodilo, ne splošni zakon. Administrator, ki sistem popravlja, katalogizatorka, ki vnaša podatke, ali bralec z oviranostjo, ki naleti na nedostopen vmesnik, jo lahko dobro vidijo tudi takrat, ko za privilegiranega uporabnika deluje brezhibno. Načrtovana presoja lahko odvisnosti pokaže, preden nastopi okvara.

Odgovornost lažje umestimo, če ločimo štiri prekrivajoče se ravni:

| Raven | Primeri | Ključno vprašanje |
| --- | --- | --- |
| **Raziskovalna infrastruktura** | repozitoriji, standardi, skupne storitve, centri, omrežja in sistemi ohranjanja | Katere skupnosti lahko raziskovalno gradivo oddajo, odkrijejo in dolgoročno ohranijo? |
| **Projektna infrastruktura** | koda, sheme, strežniki, postopki, kadri, dokumentacija in upravljanje | Kdo lahko projekt razume, uporablja in spreminja? |
| **Informacijska oziroma vmesniška infrastruktura** | iskanje, razvrščanje, prikaz metapodatkov, API-ji, identifikatorji in privzeti pogledi | Kaj je mogoče najti, primerjati ali izvoziti? |
| **Družbena infrastruktura** | strokovno znanje, izobraževanje, zaupanje, financiranje, institucionalni spomin in vzdrževalno delo | Katera razmerja ohranjajo druge ravni uporabne? |

Razločki so analitični, ne organizacijske pregrade. API je hkrati tehnična, pogodbena in družbena ureditev. Namesto splošne sodbe, da je »tehnologija pristranska«, pri pomembni odločitvi vprašajmo: **kdo odloča; kaj odločitev omogoči; kaj oteži ali skrije; kdo opravi in vzdržuje delo; kdo prejme priznanje in dostop oziroma prevzame tveganje; kaj bi lahko dokumentirali, preoblikovali ali upravljali drugače?**

## Arhivi in digitalizacija nastajajo z zaporednimi izbori

Digitalna zbirka ni preteklost in ni neposredna kopija arhiva. Pred poznejšim korpusom se zvrsti najmanj devet izborov:

1. ljudje in ustanove nekatere zapise ustvarijo, druge dejavnosti pa pustijo malo ali nič dokumentov;
2. gradivo preživi uporabo, zanemarjanje, namerno uničenje in nesreče;
3. arhivi ovrednotijo in pridobijo le del ohranjenega gradiva;
4. ohranjanje in katalogizacija razporedita pozornost in opis;
5. ustanove in financerji izberejo gradivo za digitalizacijo;
6. skeniranje, prepis in OCR nekatere lastnosti zajamejo natančneje od drugih;
7. členjenje in metapodatki določijo dokumente, datume, žanre, osebe in razmerja;
8. avtorske pravice, zasebnost in kulturna pristojnost opredelijo pogoje dostopa;
9. vmesniki razvrstijo zadetke, raziskovalci pa nato vzorčijo in očistijo še eno podmnožico.

Arhivistika opozarja, da nastanek, vrednotenje in opis zapisov dejavno oblikujejo družbeni spomin; arhiv preteklosti ne skladišči nevtralno.[^moc-arhiva] Klein v raziskavi o Jamesu Hemingsu pokaže specifično digitalno težavo: vizualizacija lahko vrzel v arhivu ponovi kot prazen prostor, premišljeno oblikovanje in branje pa razmere te odsotnosti spremenita v predmet interpretacije.[^klein-odsotnost] Vendar odsotnost ne pojasni lastnega vzroka. Prazen zadetek lahko nastane zaradi neustvarjenega ali izgubljenega zapisa, izključevanja, arhivskega vrednotenja, neobdelanega gradiva, pravic, neuspešnega OCR ali zasnove iskalnika. Odgovorna trditev navede znani mehanizem, domnevo loči od dokaznega gradiva in pojasni, kaj bi bilo še treba raziskati.

Izbor moč razporeja na konkretnih mestih. Kolonialna uprava je lahko izčrpno dokumentirala prebivalstvo, ki mu je vladala, vendar ohranila le malo gradiva, v katerem bi ljudje govorili sami zase. Odbor za digitalizacijo morda da prednost slavnemu fondu, ker zanj pričakuje več uporabe in sredstev. Služba, pristojna za pravice, lahko zaradi varstva živečih oseb upravičeno omeji dostop do občutljivega gradiva. Posamezna odločitev je lahko utemeljena, njihove posledice pa se seštevajo. Zato dokumentiramo obseg zbirke, pravila izbora, znane vrzeli in negotovost; velikega prenosa ne razglasimo za popolno populacijo.

## Standardi in klasifikacije usmerjajo interpretacijo

Skupne strukture omogočajo izmenjavo. Dokumentirano prilagoditev TEI lahko validiramo, delimo in pretvorimo; metapodatkovna shema uskladi polja; identifikatorji povežejo različice; normativni zapisi združijo imenske variante; **kontrolirani slovar**, torej dogovorjeni nabor prednostnih izrazov in razmerij med njimi, pa omogoči doslednejše iskanje. Smernice TEI združujejo skladnost standarda z dokumentiranimi prilagoditvami in s tem priznavajo, da je treba široko zasnovo prilagoditi posameznemu gradivu.[^tei]

Iste ureditve tudi omejujejo. Obvezno polje z enim datumom ne more ustrezno predstaviti »pomladi 1898«; ločevanje osebe in kraja morda popači sveto pokrajino; normativni zapis lahko uveljavi kolonialno ime; prednostni izraz pa utrdi kategorijo, o kateri so se že zgodovinski akterji prepirali. Posner opozarja, da polja o identiteti niso nevtralne posode: njihova zgradba sodeluje pri konstruiranju podatkov, ki naj bi jih zgolj shranjevala.[^posner] Bowker in Star podobno pokažeta, da standardi in klasifikacije usklajujejo delo, vendar nekatera gledišča spremenijo v rutino, druga pa težje izrazimo.[^bowker-star]

Interoperabilnost zato ni niti nevtralna rešitev niti že sama po sebi kulturno nasilje. Vprašati moramo, katero skupno jedro sodelovanje zahteva, katere krajevne razlike je treba ohraniti ter kako dokumentirati izvorno izrazje, dvoumnost, negotovost in razširitve. Če je mogoče, ob normalizirani kategoriji ohranimo zgodovinsko poimenovanje. Preverimo, ali se v kategoriji »drugo« sistematično kopičijo izključene skupine. Objavimo različico sheme in pravila preslikave. Validna datoteka lahko še vedno vsebuje slab zgodovinski model; enkratna lokalna struktura lahko ohrani odtenke, a prepreči ponovno uporabo.

## Delo, sodelovanje in priznanje

Digitalno znanstveno delo omogočajo knjižničarji, arhivisti, konservatorji, katalogizatorji, anotatorji, razvijalci, inženirji raziskovalne programske opreme, oblikovalci, sistemski administratorji, študenti, izvajalci množičnega dela, strokovnjaki za pravice, projektni vodje in dolgoročni vzdrževalci. Njihovo delo je lahko hkrati intelektualno, tehnično, pisarniško, administrativno in čustveno. Za urejenim podatkovnim nizom se skrivajo odločitve o nečitljivem besedilu, žaljivih opisih, negotovih identitetah in pogovoru s predstavljenimi skupnostmi. D'Ignazio in Klein delo ter razporeditev njegovih koristi obravnavata kot del podatkovne metode, ne kot logistično ozadje.[^podatkovni-feminizem]

Vsako sodelovanje ni izkoriščanje. Razlika je v materialnih pogojih in upravljanju. So bile vloge in plačilo dogovorjeni pred začetkom? Lahko anotatorji oporekajo škodljivi kategoriji? So pogodbeni izvajalci zaščiteni in prejmejo uporabno dokumentacijo? Ali financiranje vključuje vzdrževanje in posvetovanje s skupnostmi? Kdo odloča o lastništvu in dostopu? Kdo je naveden kot avtor, sodelavec ali priznani izvajalec in kdo odgovarja ob napaki?

Avtorstvo samo ne more opisati vseh prispevkov. Pogodbe, pravila upravljanja, dnevniki odločitev, zahvale in strukturirane izjave o prispevkih lahko natančneje porazdelijo priznanje in odgovornost. Taksonomija CRediT opredeljuje štirinajst standardiziranih vlog, med njimi skrbništvo nad podatki, programsko opremo, validacijo in projektno administracijo, pri tem pa izrecno ne določa meril za avtorstvo.[^credit] Vsak projekt mora taksonomijo prilagoditi disciplini in zabeležiti delo, ki ga ta izpušča. Priznanje brez možnosti odločanja in pravičnega plačila ne nadomesti pravičnega sodelovanja.

Vzdrževanje je znanstveno delo, ker ohranja razmere, v katerih je mogoče dokazno gradivo pregledati. Posodobljena odvisnost lahko spremeni tokenizacijo, selitev strežnika pokvari identifikatorje, nedokumentirano moderiranje spremeni zbirko, odhod sodelavca pa izbriše znanje o metapodatkovni shemi. Financiranje novosti brez selitev, dokumentacije in nasledstva je spoznavna slabost, ne samo neprijetnost za informacijsko službo.

## Jezik, geografija in domnevno »globalno« področje

Izraz **jezik z manj viri** naj opisuje razmerje, ne pomanjkljivosti jezika ali njegovih govorcev. Razpoložljivost je odvisna od naloge, žanra, obdobja in področja, pa tudi od obsega in licenciranja korpusov, slovarjev, označenih primerov, modelov, računske zmogljivosti, vmesnikov in strokovnega časa. Jezik je lahko dobro podprt za prevajanje sodobnih novic, precej slabše pa za OCR tiska iz 18. stoletja ali razpoznavanje imen v narečnih besedilih. Pregled dejanske rabe poimenovanja *low-resource* ugotavlja več medsebojno povezanih osi in le malo soglasja o enem pragu.[^manj-virov]

Orodje, naučeno na sodobni knjižni slovenščini, se morda ne bo zanesljivo preneslo na starejšo tipografijo, zgodovinsko oblikoslovje ali časopisje z regionalno mešanico jezikov. Večjezični katalog lahko prikazuje slovenske opise, zadetke pa razvršča z indeksom, osredinjenim na angleščino. To so preverljive infrastrukturne odvisnosti, ne trditve, da slovenščina ni dovolj razvita ali da vsa orodja delujejo slabo. Uspešnost merimo za dejansko obdobje, žanr in jezikovno različico, ohranimo jezikovne oznake in izvirno izrazje, vključimo ustrezno strokovno znanje ter primerjamo smiselna izhodišča.

Risam opozarja, da lahko na videz globalna digitalna vednost reproducira kolonialne kulturne zapise in osrednje ustanove, krajevne prakse pa prikaže kot obrobne.[^risam] Geografija učinkuje skozi pogoje financiranja, zanesljivost omrežja, gostovanje, potovanja, jezik objavljanja in avtoriteto standardov. Krajevno vzdržljiva metoda je lahko znanstveno trdnejša od prestižne storitve, pri kateri ne moremo pregledati učnih podatkov, pogodbene prihodnosti ali kakovosti za izbrani jezik.

## Rasa, spol, kolonialnost in invalidnost so del infrastrukture

Moč deluje skozi že obravnavane mehanizme: kolonialna oblast vpliva na nastanek in ohranitev zapisov; rasizirana imena in kategorije vstopijo v katalog; spolno zaznamovana delitev dela pri čiščenju podatkov izgine za podpisanim člankom; iskalnik razvršča tržno in družbeno prevladujoče predstave; vmesnik predvideva določeno telo, jezik in napravo. McPherson ločevanje tehničnega dela od vprašanj rase poveže z zgodovino računalniških in akademskih ureditev, Noble pa na primeru komercialnega iskanja pokaže, da razvrščanje in poslovni modeli strukturirajo rasizirano in spolno zaznamovano vidnost.[^mcpherson][^noble] Gre za razlagi določenih zgodovin in sistemov, ne za dokaz, da vsak algoritem deluje enako.

Kritično preoblikovanje poseže v mesta odločanja. Skupnosti lahko sodelujejo pri opisu in upravljanju podatkov; ob posodobljenem iskalnem izrazu lahko ohranimo izvorno izrazje; škodljivo oznako pojasnimo, namesto da jo brez sledu normaliziramo; napake merimo po skupinah in jezikih; izvajalci podatkovnega dela pa lahko kategorijam oporekajo in prejmejo priznanje. Ukrepi ne povrnejo gradiva, ki nikoli ni bilo zbrano, spremenijo pa prikaz omejitev in krog ljudi, ki lahko ukrepajo.

**Dostop** pomeni, da je vir dosegljiv pod določenimi dovoljenji in materialnimi pogoji. **Dostopnost** pove, ali ga ljudje z različnimi telesi, čuti in kognitivnimi načini ter uporabniki podpornih tehnologij lahko dejansko uporabljajo. Odprto licencirani PDF, ki vsebuje le slike brez strukture in besedilnih ustreznic, omogoča dostop, uporabniku bralnika zaslona pa gradivo zapre. Williams zagovarja univerzalno oblikovanje v digitalni humanistiki: dostopnost mora voditi nastanek, urejanje, prikaz in ohranjanje virov, ne pa nastopiti kot pozna prilagoditev.[^williams] Univerzalno oblikovanje si prizadeva za čim širšo uporabo, vendar ne odpravlja posebnih prilagoditev ali posvetovanja z ljudmi z različnimi invalidnostmi in oviranostmi. Upravljanje s tipkovnico, smiselna struktura naslovov, podnapisi, prepisi, zadosten kontrast, znaki, ki niso samo barvni, in dokumentirane alternativne oblike so pogoji znanstvene preglednosti.

## Dostop, odprtost in pravice

Beseda »odprto« označuje več različnih lastnosti:

- **odprti dostop** zadeva dostop do publikacije;
- **odprti podatki** dovoljujejo dostop in ponovno uporabo pod navedeno odprto licenco;
- **odprtokodna programska oprema** daje izvorno kodo na voljo pod ustrezno licenco;
- **interoperabilni oziroma ponovno uporabni podatki** so strukturirani in dokumentirani za nadaljnjo rabo;
- **gradivo v javni domeni** ni omejeno z avtorsko pravico, še vedno pa so lahko pomembne zasebnost in kulturne odgovornosti;
- **nadzorovani ali posredovani dostop** omogoča rabo po avtorizaciji, v varnem okolju ali skladno s protokoli skupnosti.

Lastnost ene sestavine ne določa drugih. Odprtokodna koda lahko obdeluje omejene zapise; posnetek v javni domeni je lahko objavljen v nedostopnem vmesniku; metapodatki so lahko ponovno uporabni, slike pa licencirane. Načelo čim večje odprtosti ne sme izključiti ljudi, ki jih gradivo predstavlja; zaprtost pa ne postane samodejno upravičena samo zato, ker jo ustanova razglasi za varovalno.

Načela FAIR iz leta 2016 zahtevajo, da so digitalni raziskovalni objekti **Findable (najdljivi), Accessible (dostopni), Interoperable (interoperabilni) in Reusable (ponovno uporabni)**. Dostop lahko po potrebi vključuje avtentikacijo in avtorizacijo; FAIR torej ne zahteva neomejenega javnega prenosa in samo po sebi ne zagotavlja kakovosti ali etične upravičenosti.[^fair] Načela CARE za upravljanje podatkov domorodnih skupnosti poudarjajo **Collective Benefit (kolektivno korist), Authority to Control (pristojnost za nadzor oziroma odločanje), Responsibility (odgovornost) in Ethics (etiko)**. Nastala so v mrežah za podatkovno suverenost domorodnih ljudstev in zadevajo njihove pravice ter interese v podatkih o njihovih skupnostih, ozemljih, znanju in kulturah.[^care][^gida]

FAIR predvsem sprašuje, ali je podatke in metapodatke mogoče najti, pridobiti pod jasnimi pogoji, povezovati in ponovno uporabiti. CARE sprašuje, kdo ima korist, kdo odloča in katere odgovornosti veljajo v specifičnem kontekstu podatkov domorodnih ljudstev. Pristopa se lahko dopolnjujeta, vendar tehnično skladen objekt FAIR lahko krši CARE, legitimna pristojnost za nadzor pa lahko omeji ponovno uporabo. CARE ni vezan na eno državo, prav tako ni splošna etična kratica, ki bi jo smeli ločiti od domorodnega upravljanja podatkov. Drugi projekti se lahko iz teh načel učijo vprašanj o koristih in pristojnostih, ne da bi si prisvojili njihov izvor ali neutemeljeno zatrjevali skladnost.

## Vzdrževanje in okoljski stroški

Digitalno ohranjanje je dejaven proces. Nosilci odpovedujejo; varnostne in podvojene kopije zahtevajo opremo, energijo in preverjanje; formate in programske odvisnosti je treba seliti; certifikati, domene in identifikatorji potečejo; modeli potrebujejo računsko obdelavo; naprave je treba izdelati, prepeljati in nazadnje zamenjati. Jackson z glediščem »pokvarjenega sveta« popravilo obravnava kot mesto znanja, skrbi in moči, ne kot manjvredno delo po inovaciji.[^jackson] Pendergrass in sodelavci pokažejo, da moramo pri okoljsko vzdržnem digitalnem ohranjanju znova premisliti vrednotenje, trajnost hrambe in razpoložljivost.[^trajnost]

Za »digitalni projekt« ni enega primerljivega podatka o izpustih. Vpliv je odvisen od vira elektrike, strojne opreme, kraja, pravil hrambe, prometa, modela, možnosti ponovne uporabe in meje izračuna. Senzacionalne številke odločitve prej zakrijejo kot pojasnijo. Smiselnejša so vprašanja: Katero hrambo, podvajanje in računanje upravičuje znanstveni oziroma ohranitveni namen? Je mogoče ponovno uporabiti posnetke, modele ali postopke? Bi na vprašanje odgovorila manj zahtevna metoda? Katere datoteke potrebujejo katero raven ohranjanja? Kdo bo po koncu financiranja plačeval selitve, dokumentacijo, varnost, dostopnost in odgovorno ukinitev?

**Tehnični dolg** je prihodnje delo, ki nastane, ko kratkoročna zasnova oteži poznejše spremembe. Del dolga je zavesten in dokumentiran; skriti dolg stroške prenese na vzdrževalce ali uporabnike. Načrt trajnosti naj navede skrbnike, raven storitve, odvisnosti, izvozne poti, cilje ohranjanja, predpostavke o financiranju in odgovorno pot ob koncu delovanja. Trajno hranjenje vsega na spletu ni edina oblika skrbi, tiho izginotje pa ni politika ohranjanja.

## Razdelan primer: zgodovinski časopisni korpus v jeziku z manj viri

Zamislimo si raziskavo uokvirjanja javnega strahu v stoletju časopisja v jeziku z manj viri. Infrastrukturne odvisnosti se nalagajo v verigo:

1. **Ohranjenost:** ostali so le nekateri naslovi, letniki in fizični izvodi, pri čemer se stanje lahko razlikuje po regijah in založnikih.
2. **Izbor in financiranje digitalizacije:** ustanova izbere podmnožico glede na stanje, uporabo, pomen, pravice ali sredstva; razloge in zavrnjeno gradivo naj dokumentira.
3. **Skeniranje:** vezani letniki, presevanje tiska, poškodbe, stolpci in oglasi vplivajo na kakovost slike ter razpoznavanje postavitve.
4. **OCR:** natančnost se spreminja z obdobjem, tipografijo, pravopisom, jezikovno različico in stanjem strani; ovrednotiti jo moramo po slojih, ne z eno skupno oceno.
5. **Členjenje in metapodatki:** meje člankov, datumi, žanri, naslovi in identiteta časopisa so rezultat samodejnega sklepanja ali vnosa; stran še ni samodejno članek.
6. **Pravice in posredovanje:** avtorske pravice, zasebnost ali pogodbe lahko dovolijo branje, ne pa množičnega prenosa, ali pa omejijo API; to vpliva na ponovljivost in vzorčenje.
7. **Iskanje in razvrščanje:** privzeti datumski obseg, krnjenje, izseki in ocena relevantnosti vplivajo na odkritje; seznam zadetkov ni naključni vzorec.
8. **Raziskovalna priprava:** skupina določi merila vključevanja, odstrani dvojnike, očisti OCR in zabeleži izločitve; vsaka sprememba dobi različico in revizijsko sled.
9. **Analiza:** tematski ali čustveni model operacionalizira »strah« z besedami, odlomki ali oznakami; kategorije in jezikovni viri dodajo novo raven.
10. **Validacija:** raziskovalci OCR primerjajo s slikami strani po časopisih, obdobjih in postavitvah, pregledajo meje člankov, ročno kodirajo stratificirani vzorec ter preverijo občutljivost rezultata na čiščenje in pokritost.
11. **Objava in ohranjanje:** objavijo dovoljene podatke, identifikatorje, kodo, model in povzetek napak; opišejo omejene vhode, oddajo verzionirani paket v repozitorij ter določijo odgovornost za vzdrževanje.

Poglejmo dve možni popačenji. Če je OCR starejših strani slabši, sistem prepozna manj izrazov za strah in ustvari navidezen zgodovinski porast, čeprav je tiskana raba nespremenjena. Ocena OCR po obdobjih, preverjanje slik in analiza občutljivosti lahko trditev omejijo. Drugič, napačne meje članka lahko poročilo o kaznivem dejanju združijo s sosednjim političnim komentarjem, neenakomerna pokritost časopisov pa spremeni razmerje žanrov in političnih usmeritev. Premik v »čustvenem uokvirjanju« je tedaj lahko posledica sestave korpusa, ne jezikovne spremembe. Pomagajo pregled meja, porazdelitve naslovov in žanrov ter primerjave znotraj posameznih slojev.

Iz tega ne sledi, da računalniška analiza ni mogoča. Infrastruktura določa njeno dokazno podlago. Utemeljena ugotovitev se lahko nanaša na **digitalizirano, licencirano in validirano podmnožico pod dokumentiranimi pogoji napak in pokritosti**, ne brez omejitve na »nacionalni tisk«.

## Vaja: ponovljiva presoja infrastrukture

Izberite digitalno zbirko, repozitorij, korpus ali znanstveno orodje ter eno predlagano humanistično trditev. Pripravite tabelo ali dosje, ki zajema:

| Področje presoje | Najmanjši obseg dokaznega gradiva |
| --- | --- |
| Odgovornost in obseg | odgovorna ustanova oziroma skupnost, deklarirani obseg, dokumentirani izpusti in vrzeli, ki ste jih opazili sami |
| Predmeti in opis | formati, identifikatorji, metapodatkovna shema, klasifikacije, kontrolirani slovarji, izvorno izrazje in negotovost |
| Preoblikovanje | digitalizacija, OCR ali prepis, jezikovna podpora, objavljene trditve o kakovosti in vaši dovoljeni vzorčni preizkusi |
| Uporaba | dostopnost s tipkovnico oziroma podporno tehnologijo, kjer jo lahko preverite; pravice, zasebnost, kulturna pristojnost; iskanje, razvrščanje, API in izvoz |
| Ljudje in pristojnosti | delo in vloge sodelujočih, upravljanje, priznanje, financiranje ter možnost popravka ali umika |
| Kontinuiteta in materialnost | odgovornost za vzdrževanje, načrt ohranjanja, odvisnosti, hramba oziroma računanje ter objavljena okoljska politika ali njena nedokumentiranost |
| Posledica | način, kako vsaka ugotovitev omogoči, omeji ali spremeni trditev, ter odziv z validacijo ali preoblikovanjem |

Vsak vnos označite z enim od štirih dokaznih statusov: **opaženo dejstvo** (kar lahko pregledate), **trditev ustanove** (s stranjo in datumom dostopa), **rezultat lastnega preizkusa** (z metodo, vzorcem in datumom) ali **vaša interpretacija** (s sklepanjem in drugimi možnostmi). Nedokumentirane lastnosti ne spremenite v obtožbo. Namesto »ne obstaja« napišite »podatka po pregledu strani X in Y nisem našel/-la«.

**Rezultat:** izpolnjena presoja, diagram odvisnosti oziroma urejena veriga in 500-besedna ocena trditve. **Preverjanje:** kolega naj po vašem zapisu ponovi dve opažanji in en preizkus. **Pogoste napake:** uporaba samo predstavitvene strani zbirke; zamenjava praznega iskalnega rezultata za neobstoj zgodovinskega zapisa; preizkus le najlažjega dokumenta; priporočilo odprtosti brez preverjanja pravic in pristojnosti.

## Refleksija

- Katere infrastrukturne odvisnosti pred presojo niste videli in komu so bile verjetno ves čas očitne?
- Kje standard omogoči primerjavo in kateri razloček pri tem odrine?
- Kdo sme spremeniti škodljivo kategorijo ali nedostopen vmesnik in kdo do tedaj nosi stroške?
- Katera vrzel v zbirki ima dokumentiran vzrok, katera več možnih vzrokov in katere sploh še ne morete razložiti?
- Kakšen obseg vzdrževanja in okoljskih stroškov je sorazmeren s trditvijo in prihodnjo ponovno uporabo?

## Povzetek

Infrastruktura je relacijski pogoj nastajanja vednosti. Arhivi, digitalizacija, metapodatki, klasifikacije, vmesniki, pravice, jezikovna podpora in ohranjanje zaporedoma izbirajo, kaj lahko postane dokazno gradivo. Ob tem razporejajo vidnost, delo, priznanje, pristojnost, dostop in tveganje. Učinke moramo izslediti skozi odločitve, ne pa jih stisniti v splošno sodbo o pristranski tehnologiji.

Standardi lahko omogočijo validacijo, izmenjavo in ohranjanje, obenem pa omejijo krajevne ali dvoumne pomene. Sodelovanje je pravičnejše, kadar vključuje ustrezno upravljanje, plačilo, možnost ugovora kategorijam in natančno priznanje; vzdrževanje varuje preglednost dokaznega gradiva. Podpora jeziku je odvisna od naloge, obdobja, žanra in infrastrukture. Dostop ni isto kot dostopnost, odprtost, skladnost z načeli FAIR in odgovorno upravljanje pa so ločena vprašanja. CARE ostaja umeščen v upravljanje podatkov domorodnih ljudstev. Okoljsko odgovornost presojamo s sorazmernostjo, ponovno uporabo in jasno določenim dolgoročnim skrbništvom.

Presoja infrastrukture ni zunaj interpretacije. Določi populacijo, preoblikovanja, dovoljenja in negotovosti, ki interpretacijo omejujejo in ji dajejo težo. Poznejše poglavje [UI, etika in ponovljivost](ai-ethics-reproducibility.md) številna strukturna vprašanja pretvori v praktična varovala in dokumentiranje posameznega projekta.

## Nadaljnje branje in viri

- Bowker, Geoffrey C., in Susan Leigh Star. [*Sorting Things Out: Classification and Its Consequences*](https://mitpress.mit.edu/9780262522953/sorting-things-out/). MIT Press, 1999. Spletno mesto *MIT Press*. Dostop 22. julija 2026.
- Carroll, Stephanie Russo, Ibrahim Garba, Oscar L. Figueroa-Rodríguez idr. »[The CARE Principles for Indigenous Data Governance](https://doi.org/10.5334/dsj-2020-043)«. *Data Science Journal* 19 (2020): 43. DOI: `10.5334/dsj-2020-043`.
- D'Ignazio, Catherine, in Lauren F. Klein. [*Data Feminism*](https://doi.org/10.7551/mitpress/11805.001.0001). MIT Press, 2020. DOI: `10.7551/mitpress/11805.001.0001`.
- Global Indigenous Data Alliance. »[CARE Principles for Indigenous Data Governance](https://www.gida-global.org/careprinciples)«. Spletno mesto *Global Indigenous Data Alliance*. Dostop 22. julija 2026.
- Jackson, Steven J. »[Rethinking Repair](https://doi.org/10.7551/mitpress/9780262525374.003.0011)«. V *Media Technologies: Essays on Communication, Materiality, and Society*, ur. Tarleton Gillespie, Pablo J. Boczkowski in Kirsten A. Foot, 221–240. MIT Press, 2014. DOI: `10.7551/mitpress/9780262525374.003.0011`.
- Klein, Lauren F. »[The Image of Absence: Archival Silence, Data Visualization, and James Hemings](https://doi.org/10.1215/00029831-2367310)«. *American Literature* 85, št. 4 (2013): 661–688. DOI: `10.1215/00029831-2367310`.
- McPherson, Tara. »[Why Are the Digital Humanities So White? or Thinking the Histories of Race and Computation](https://doi.org/10.5749/minnesota/9780816677948.003.0017)«. V *Debates in the Digital Humanities*, ur. Matthew K. Gold, 139–160. University of Minnesota Press, 2012. DOI: `10.5749/minnesota/9780816677948.003.0017`.
- National Information Standards Organization. »[ANSI/NISO Z39.104-2022, CRediT, Contributor Roles Taxonomy](https://doi.org/10.3789/ansi.niso.z39.104-2022)«. NISO, 2022. DOI: `10.3789/ansi.niso.z39.104-2022`.
- Nigatu, Hellina Hailu, Atnafu Lambebo Tonja, Benjamin Rosman, Thamar Solorio in Monojit Choudhury. »[The Zeno’s Paradox of ‘Low-Resource’ Languages](https://doi.org/10.18653/v1/2024.emnlp-main.983)«. V *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*, 17753–17774. Association for Computational Linguistics, 2024. DOI: `10.18653/v1/2024.emnlp-main.983`.
- Noble, Safiya Umoja. [*Algorithms of Oppression: How Search Engines Reinforce Racism*](https://nyupress.org/9781479866762/algorithms-of-oppression/). NYU Press, 2018. Spletno mesto *NYU Press*. Dostop 22. julija 2026.
- Pendergrass, Keith L., Walker Sampson, Tim Walsh in Laura Alagna. »[Toward Environmentally Sustainable Digital Preservation](https://doi.org/10.17723/0360-9081-82.1.165)«. *The American Archivist* 82, št. 1 (2019): 165–206. DOI: `10.17723/0360-9081-82.1.165`.
- Posner, Miriam. »[What’s Next: The Radical, Unrealized Potential of Digital Humanities](https://doi.org/10.5749/j.ctt1cn6thb.6)«. V *Debates in the Digital Humanities 2016*, ur. Matthew K. Gold in Lauren F. Klein, 32–41. University of Minnesota Press, 2016. DOI: `10.5749/j.ctt1cn6thb.6`.
- Risam, Roopika. [*New Digital Worlds: Postcolonial Digital Humanities in Theory, Praxis, and Pedagogy*](https://nupress.northwestern.edu/9780810138865/new-digital-worlds/). Northwestern University Press, 2018. Spletno mesto *Northwestern University Press*. Dostop 22. julija 2026.
- Schwartz, Joan M., in Terry Cook. »[Archives, Records, and Power: The Making of Modern Memory](https://doi.org/10.1007/BF02435628)«. *Archival Science* 2 (2002): 1–19. DOI: `10.1007/BF02435628`.
- Star, Susan Leigh, in Karen Ruhleder. »[Steps Toward an Ecology of Infrastructure: Design and Access for Large Information Spaces](https://doi.org/10.1287/isre.7.1.111)«. *Information Systems Research* 7, št. 1 (1996): 111–134. DOI: `10.1287/isre.7.1.111`.
- Text Encoding Initiative Consortium. »[TEI: Guidelines for Electronic Text Encoding and Interchange](https://tei-c.org/release/doc/tei-p5-doc/en/html/)«. P5, različica 4.11.0, zadnja posodobitev 18. februarja 2026. Spletno mesto *Text Encoding Initiative*. Dostop 22. julija 2026.
- Wilkinson, Mark D., Michel Dumontier, IJsbrand Jan Aalbersberg idr. »[The FAIR Guiding Principles for Scientific Data Management and Stewardship](https://doi.org/10.1038/sdata.2016.18)«. *Scientific Data* 3 (2016): 160018. DOI: `10.1038/sdata.2016.18`.
- Williams, George H. »[Disability, Universal Design, and the Digital Humanities](https://doi.org/10.5749/minnesota/9780816677948.003.0020)«. V *Debates in the Digital Humanities*, ur. Matthew K. Gold, 202–212. University of Minnesota Press, 2012. DOI: `10.5749/minnesota/9780816677948.003.0020`.

[^star-ruhleder]: Star in Ruhleder, »Steps Toward an Ecology of Infrastructure«, 111–134. Njuna analiza izhaja iz določene porazdeljene znanstvene skupnosti; lastnosti infrastrukture so analitična izhodišča, ne splošen seznam, ki bi povsod veljal enako.
[^moc-arhiva]: Schwartz in Cook, »Archives, Records, and Power«, 1–19, o zapisih in arhivih kot dejavnih soustvarjalcih spomina in identitete. Devetstopenjsko zaporedje v tem poglavju razširi razpravo še na digitalizacijo, vmesnike in poznejšo raziskovalno rabo.
[^klein-odsotnost]: Klein, »The Image of Absence«, 661–688. Primer obravnava arhiv suženjstva in Jamesa Hemingsa; utemeljuje kritično obravnavo odsotnosti v vizualizaciji, ne splošnega sklepanja o vzroku vsake manjkajoče sledi.
[^tei]: Text Encoding Initiative Consortium, *TEI Guidelines*, zlasti prvo in štiriindvajseto poglavje o shemah, validaciji, prilagajanju, skladnosti in dokumentiranju.
[^posner]: Posner, »What’s Next«, 32–41. Besedilo je programski poseg o podatkovnih modelih, razlikah in moči, ne poziv k opustitvi formalizacije.
[^bowker-star]: Bowker in Star, *Sorting Things Out*, o klasifikacijah in standardih kot informacijski infrastrukturi s praktičnimi in porazdelitvenimi posledicami.
[^podatkovni-feminizem]: D'Ignazio in Klein, *Data Feminism*, zlasti načela o analizi moči, izpodbijanju binarnosti, utelešenju, pluralnosti, kontekstu in vidnosti dela. Z izrazom **umeščeno znanje** poudarjamo, da spoznanje nastaja iz določenega položaja, odnosov in pogojev.
[^credit]: National Information Standards Organization, *ANSI/NISO Z39.104-2022*. Standard opisuje prispevke, ne določa pa meril za avtorstvo.
[^manj-virov]: Nigatu idr., »Zeno’s Paradox«, 17753–17774. Pregled 150 objav prepozna več medsebojno povezanih osi in omejeno soglasje pri rabi izraza *low-resource*.
[^risam]: Risam, *New Digital Worlds*, zlasti drugo in tretje poglavje o kolonialnem nasilju v digitalnem kulturnem zapisu ter razmerju med krajevnimi praksami in globalnimi ureditvami.
[^mcpherson]: McPherson, »Why Are the Digital Humanities So White?«, 139–160. Zgodovinska analogija med modularnostjo in rasnimi ureditvami nasprotuje ločevanju kulturne kritike od tehničnega dela; avtorica je ne predstavi kot neposrednega tehnološkega determinizma.
[^noble]: Noble, *Algorithms of Oppression*, o komercialnem iskanju, razvrščanju, oglaševanju ter rasiziranih in spolno zaznamovanih predstavah. Tukaj njene ugotovitve uporabljamo samo za razlago moči vmesnika in vidnosti, ne za vse znanstvene iskalnike.
[^williams]: Williams, »Disability, Universal Design«, 202–212. Avtor pokaže, da lahko digitalnohumanistično oblikovanje uporabnike ovira, ter zagovarja vključitev dostopnosti od začetka.
[^fair]: Wilkinson idr., »FAIR Guiding Principles«, zlasti načelo A1.2, ki dopušča avtentikacijo in avtorizacijo. FAIR opredeljuje lastnosti za strojno podprto odkrivanje in ponovno uporabo, ni sopomenka odprtih podatkov.
[^care]: Carroll idr., »CARE Principles«, članek 43, o kolektivni koristi, pristojnosti za nadzor, odgovornosti in etiki kot načelih upravljanja podatkov domorodnih ljudstev, usmerjenih v ljudi in namen.
[^gida]: Global Indigenous Data Alliance, »CARE Principles«, o delavnici v Gaboronu leta 2018, mrežah podatkovne suverenosti domorodnih ljudstev in dopolnjevanju s FAIR. Spletna stran se spreminja, zato je naveden datum dostopa.
[^jackson]: Jackson, »Rethinking Repair«, 221–240, o okvari, vzdrževanju in popravilu kot mestih ustvarjalnosti, znanja, moči in skrbi.
[^trajnost]: Pendergrass idr., »Toward Environmentally Sustainable Digital Preservation«, 165–206, o vključevanju okoljskih meril v vrednotenje, trajnost in razpoložljivost namesto zanašanja zgolj na tehnično učinkovitost.
