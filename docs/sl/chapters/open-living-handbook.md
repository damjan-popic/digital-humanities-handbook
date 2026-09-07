---
title: "Živi odprti priročnik"
description: "Kako recenzirane izdaje, sprotno popravljanje, skupno vzdrževanje in dolgoročna hramba podpirajo odgovorno znanstveno objavljanje."
tags: [odprto-izobraževanje, verzioniranje, recenziranje, prispevki, založništvo]
status: draft
translation_status: "machine-assisted draft; requires human language review"
---

# Živi odprti priročnik

!!! warning "Uredniški status"
    Razširjeno poglavje je osnutek, pripravljen s strojno pomočjo. Čaka na celovit strokovni pregled in pregled usposobljenega človeškega pregledovalca slovenskega jezika. Primeri prikazujejo odločitve o objavljanju, ne že objavljenih izdaj ali dodeljenih identifikatorjev.

## Učni cilji

Po tem poglavju boste znali:

- razlikovati med zgodovino izvornih datotek, ustvarjeno bralno izdajo, paketom izdaje in bibliografskim zapisom;
- pojasniti obseg recenzije in omejitve sklepanja na podlagi številke različice;
- slediti popravku od dokazila prek objave do poznejšega navajanja;
- pripraviti seznam vsebine izdaje z recenzijskim, prevodnim, licenčnim in dostopnostnim statusom;
- ločiti ocenjevanje študentskega dela, soglasje k objavi in priznanje prispevka;
- načrtovati dolgoročno hrambo, vzdrževanje in nasledstvo v okviru razpoložljivih sredstev.

## Pred začetkom

Kako lahko bralec kritično presodi interpretacijo, če se njena dokazila in besedilo med branjem in navajanjem spremenijo? Kakšna pa je urednikova odgovornost, ko odkrije napako v pogosto navajanem učnem viru? Vprašanji povezujeta preučevanje besedil s praktično organizacijo digitalnega založništva. Živa publikacija mora spremembe pojasniti, ne da bi včerajšnjo trditev predstavljala kot današnje spoznanje.

Spomnite se digitalne izdaje ali učnega spletnega mesta, ki ste ga uporabili. Ali ste lahko ugotovili, kdo ga je pripravil, katero različico ste brali, kdaj je bil opravljen zadnji vsebinski pregled in kako je urejena hramba? Ločite objavljene podatke od sklepov, ki ste jih izpeljali iz logotipa ustanove. Za vaje potrebujete osnovno razumevanje izvornih datotek ter razlikovanja med dokazilom in interpretacijo. Skrbniška dovoljenja niso potrebna. Vhodno gradivo sestavljata majhen popis publikacije in scenarij popravka; rezultat so zapisi, ki jih lahko presodi drug urednik.

## Dva ritma in omejen obseg strokovne avtoritete

Recenzirana izdaja določi omejen znanstveni predmet: navedena poglavja, jeziki in primeri so bili pregledani pri določeni reviziji. Živa izdaja omogoča nadaljnje popravke in razvoj gradiva. Razmerje med njima je uredniško, ne zgolj časovno. Nedavno dodan postopek je lahko uporaben, vendar še poskusno preverjen; starejše recenzirano poglavje lahko ohrani pojmovno vrednost kljub zastareli sliki vmesnika. Niti novost niti številka različice ne nadomestita podatka o obsegu pregleda.

Priročnik povezuje počasneje spreminjajoča se poglavja in učni poti s hitreje razvijajočo se zbirko postopkov. Privzeta veja `main` podpira živo izdajo; oštevilčene izdaje so zamišljene kot zamrznjeni recenzirani posnetki. Seznam vsebine izdaje oziroma manifest mora povedati, kateri praktični prispevki sodijo v recenzirano izdajo in kateri ostajajo spremljevalno gradivo. Angleška nadomestna stran v slovenski zbirki omogoča dostop, ni pa končan prevod. Trditev, da je celoten repozitorij recenziran ali v celoti preveden, bi presegla tako določen obseg.

Tako lahko presodimo tudi odprtost. Unescovo priporočilo o odprtih učnih virih iz leta 2019 povezuje odprte licence z usposobljenostjo, vključevanjem in vzdržnim zagotavljanjem virov. Za uredniško delo pri tem priročniku iz tega izpeljujemo potrebo, da poleg nove vsebine načrtujemo pregled in vzdrževanje. Če nadaljnji razvoj ni izvedljiv, naj ostane na voljo stabilna bralna izdaja.[^living-oer]

## Izvor, izdaje in distribucijske datoteke

Uredljivi izvor vsebuje argumentacijo, primere, metapodatke, licence in navodila za gradnjo. Ustvarjeni HTML ali recenzijski rokopis ta izvor predstavi določenim bralcem. Distribucijske datoteke, denimo izvorni arhiv ZIP ali arhiv statičnega mesta, so konkretna zaporedja bajtov. Morda ne vključujejo živih storitev, oddaljenih medijev ali zunanjih podatkov. Preden obljubite uporabo brez povezave, paket razširite na drugem računalniku, prekinite omrežno povezavo in preizkusite bistvene bralne poti.

Zapis spremembe Git oziroma commit identificira revizijo in povezave do njene zgodovine. Oznaka Git oziroma tag poimenuje točko v zgodovini; opremljena oznaka lahko vsebuje še sporočilo in podatke o avtorju. Dovoljenja lahko dopuščajo zamenjavo ali izbris oznake. Objava GitHub release poveže oznako z opombami in datotekami, vendar je samostojen predmet platforme. Dokumentirana možnost nespremenljivih izdaj varuje pripadajoče oznake in datoteke, če je vključena; opombe ob izdaji ostajajo uredljive. Podatke smo preverili 7. septembra 2026, ne trdimo pa, da je možnost vključena v tem repozitoriju.[^living-git][^living-github]

Stalni znanstveni identifikator ima drugačno nalogo. DOI ali repozitorijski identifikator povezuje publikacijo z vzdrževanimi metapodatki in pristajalnim zapisom; ISBN sodi v založnikovo bibliografsko ureditev. Nobeden ni kontrolna vsota ali dokaz recenzije. Z založnikom in ustanovo za hrambo določite predmet posameznega identifikatorja, razmerje med jezikovnima izdajama in povezovanje različic. Zenodo loči uporabo obstoječega DOI od registracije novega; možnost registracije še ne utemeljuje vzporednega zapisa za isto izdajo.[^living-zenodo]

Koristne ostajajo štiri razlike iz poglavja [UI, etika in ponovljivost](ai-ethics-reproducibility.md). Tehnična ponovljivost zadeva ponovitev dejanja v določenih pogojih. Računalniška reproducibilnost zadeva rekonstrukcijo s pomočjo ohranjenih izvornih datotek, kode, podatkov in okolja. Preverljivost dokazne poti omogoča sledenje trditvi do virov in popravkov. Interpretativna odgovornost zahteva utemeljitev izbire virov in presojo še zagovarjanih alternativnih branj. Enaki bajti ne odgovorijo na zadnje vprašanje. Arhivirani PDF lahko omogoča preverjanje dokazil, čeprav izvedbeno okolje ni ohranjeno.

## Različice zahtevajo uredniško presojo

Semantično verzioniranje opredeli večje, manjše in popravljene različice glede na pogodbo programskega vmesnika. Humanistična argumentacija nima enakovrednega samodejnega preizkusa združljivosti. Poimenovalno načelo zato prevzemajte previdno: zapišite lokalna pravila in utemeljite odločitev.[^living-semver]

Po pravilih priročnika izdaja popravka odpravi tipkarsko napako, napako v navodilih ali metapodatkih brez spremembe učne argumentacije. Manjša izdaja doda obsežnejše pregledano gradivo znotraj obstoječe zgradbe. Večja izdaja označuje bistveno spremenjeno metodo, preurejeno argumentacijo ali novo recenzirano izdajo. Zamenjava besede »podpira« z »izpodbija« lahko zahteva več presoje kot sto popravljenih povezav. Presojajte posledico za bralca, ne števila spremenjenih vrstic. Spremembe učne argumentacije ne označite kot navaden popravek zgolj zato, ker je kratka.

Tudi datumi potrebujejo jasno opredelitev: izvorna revizija, končana recenzija, objava izdaje in poznejše popravilo metapodatkov imajo lahko različne datume. Manifest naj navede commit, vključene poti, jezike, stanje prevodov, obseg pregledov, licence, izvorne kontrolne vsote, zunanje odvisnosti in ugotovitve o dostopnosti. Ločeno zabeležite okolje za gradnjo in kontrolne vsote distribucijskih datotek. Nedodeljeni identifikatorji ostanejo izrecno v čakanju; uspešna gradnja jih ne more določiti. Kadar načrtovana izdaja zahteva še nedokončano recenzijo ali založnikovo potrditev, objava počaka.

Pri oštevilčeni izdaji navedite avtorja oziroma urednika, naslov publikacije, različico in datum izdaje, lokator poglavja ali postopka ter dodeljeni identifikator oziroma stabilno pot do te izdaje. Navedite dejansko uporabljeno različico, tudi če obstaja novejša. Če namerno obravnavate živo vejo `main`, zapišite »živa izdaja«, celotni commit izvora, natančno stran in datum dostopa. Bralnemu naslovu dodajte povezavo do izvora pri tem commitu. Sam datum dostopa ne določi, katera od več revizij istega dne je podpirala trditev. Načelo velja tudi za navedke pri predmetu, ne da bi semestrski posnetek zato predstavljali kot formalno recenzirano izdajo.

## Kaj priročnik že podpira

Ob pregledu repozitorija za to poglavje 7. septembra 2026 so bili na voljo vzporedni izvorni dokumenti Markdown, uredniška pravila, poročanje o prevodih, ustvarjeni recenzijski rokopisi in strogo preverjanje spletne gradnje. Postopek, ki ga sproži oznaka izdaje, pripravi izvorni in spletni arhiv, kopira rokopisa in poročilo o prevodih, izračuna kontrolne vsote ter datoteke naloži kot artefakt GitHub Actions. Sam po sebi ne dokazuje trajnega depozita, pripetja datotek javni objavi GitHub release, založniške potrditve ali dodelitve DOI oziroma ISBN. Tudi podatki za navajanje ne dokazujejo, da je bila vsaka datoteka formalno recenzirana.

Založniško usklajena izdaja je ločeno opredeljena v [nalogi #30](https://github.com/damjan-popic/digital-humanities-handbook/issues/30). Pred trditvijo o formalni izdaji mora urediti pisne založnikove zahteve, pristojnosti za identifikatorje, vsebino paketa in preverjanje depozita. [Postopek načrtovanja izdaje](../workflows/publishing/create-a-versioned-scholarly-release.md) pripravi dokazila, teh dejanj pa ne izvede. Obstoječi gradbeni postopek je uporabna sestavina; celotno založniško storitev je treba šele vzpostaviti in preveriti.

## Razdelan primer: običajen prispevek z izrecnim soglasjem

Zamislite si študentski prispevek: dvojezično razlago razlikovanja med omembo kraja in prebivališčem osebe v kazalu ustne zgodovine. Izmišljeni intervjujski odlomki preprečijo razkritje udeležencev pri vaji. Omejena trditev prispevka je, da podano kodirno pravilo loči dve razmerji v izbranih primerih, ne da je mogoče samodejno razvrstiti vse ustne zgodovine.

Študentka priloži primere, odločitve, nasprotni primer in želeno obliko navedbe prispevka. Kolega preveri, ali po navodilih dobi pričakovano tabelo. Urednik presodi zgodovinsko sklepanje, slovenski pregledovalec terminologijo in enakovrednost navodil, pregledovalec dostopnosti pa naslove in vrstni red branja. Zapisi opredelijo revizijo in obseg dela. Strojno podprt jezikovni pregled pri tem pomaga pripraviti osnutek, ne šteje pa kot končan človeški pregled.

Ocenjevanje zasebno presoja oddano raziskovalno delo. Objava je ponujena ločeno, z enakovredno možnostjo nejavne oddaje, razlago licence in javne zgodovine ter jasnim rokom pred objavo. Zavrnitev objave ne sme znižati ocene. Študentka lahko skladno s pravili ustanove predlaga dogovorjeno javno navedbo prispevka. Poleg njenega soglasja sta potrebna uredniški sprejem in razjasnitev pravic. Poznejši izbris ne more zanesljivo odpoklicati kopij, ki so jih drugi že razširili pod odprto licenco.

Ko so pogoji izpolnjeni, urednik prispevek sprejme v živo izdajo in ga predlaga za poznejšo manjšo izdajo. Manifest pokaže, kateri pregled se nanaša tudi nanjo. Prevajanje, urejanje podatkov, razvoj kode in preverjanje zaslužijo priznanje ob pisanju besedila. CRediT ponuja izraze za več raziskovalnih vlog, projekt pa mora posebej opisati tudi uredniško in prevodno delo. Klasifikacija sama ne razreši spora o avtorstvu.[^living-credit]

## Zahtevnejši primer: popravek po navajanju

Naslednji scenarij je izmišljen; številke izdaj in podatki ne opisujejo že objavljene izdaje priročnika. Predpostavimo, da hipotetična izdaja `1.0.0` učno tabelo opisuje kot zbirko 40 različnih zgodovinskih pisem. Izkaže se, da štiri vrstice podvajajo predstavitve istih dokumentov, zato zbirka vsebuje 36 različnih pisem. Vaja uči štetje virov: njen sklep se spremeni, čeprav zgradba poglavja ostane uporabna.

Urednik ponovi preverjanje, določi prizadete odlomke in tabele ter pregleda oba jezika in datoteke za prenos. Primerjavo ponovno izračuna; popravek pove, da je bil imenovalec napačen. V tem scenariju izbere hipotetično manjšo izdajo `1.1.0`, ker vsebinsko popravljeno učno gradivo ostaja znotraj obstoječe zgradbe. Če bi popravek ovrgel metodo poglavja, bi lahko zahteval večjo recenzirano izdajo. Številka dokumentira presojo, ne nadomešča ugotovitve.

| Mesto v publikaciji | Vidni zapis v tem scenariju |
| --- | --- |
| Izvorna sprememba | Pregledana dvojezična sprememba pojasni merilo podvajanja, zamenja 40 s 36 in popravi sklep. |
| Dnevnik sprememb | Vnos določi prizadeti razdelek `1.0.0`, vsebinski popravek in načrtovano `1.1.0`. |
| Obvestilo o popravku oziroma erratum | Datirano obvestilo navede napako, dokazilo, posledico in nadomestitev; identifikator povezuje zapise. |
| Opombe ob izdaji | `1.1.0` poveže erratum ter opiše pregled, znova ustvarjene tabele in dvojezične spremembe. |
| Stabilna izdaja | Datoteke `1.0.0` ohranijo identiteto; pristajalni zapis vidno poveže erratum in naslednjo izdajo. Nove datoteke pripadajo `1.1.0`. |
| Poznejši navedek | Analiza s popravljenim številom navede `1.1.0` in razdelek; zgodovina napake navede `1.0.0` skupaj z erratumom. |

Prejemniki prenesenih kopij se morda nikoli ne vrnejo na spletno mesto. Kadar je sorazmerno, po ustaljenih poteh obvestite znane izvajalce predmetov in ustanove za hrambo. Obvestilo naj posledice pojasni brez zahteve, da bralec razume razliko med revizijama Git. [Postopek popravljanja objavljenega vira](../workflows/publishing/correct-a-published-digital-resource-without-erasing-history.md) to zaporedje pretvori v zapis, primeren za presojo.

## Popravek, umik in meje javne zgodovine

Popravek odpravi določeno napako. Erratum je vidno obvestilo o njej; poimenovanje naj sledi založnikovim pravilom. Oznaka zastaranja opozarja, da sicer berljivega postopka ne priporočamo več, denimo zaradi spremenjene storitve. Nadomestitev določi naslednika, ne da bi vse prejšnje trditve razglasila za napačne. Umik prek uredniške obravnave prekliče zanašanje na resno nezanesljivo ali drugače nesprejemljivo delo. Teh dejanj ne združujte pod nejasno oznako »posodobljeno«. COPE poudarja namen in vidnost obvestil o umiku; smernice za revije je treba premišljeno prilagoditi digitalnemu predmetu.[^living-cope]

Ohranjanje navedenih različic je običajno znanstveno pravilo, ne zahteva po neskončnem javnem izpostavljanju zasebnih podatkov. Če objavite prepoznavne intervjujske podatke ali skrivno poverilnico, po pristojnem institucionalnem postopku ustavite nadaljnje razširjanje. Neškodljivo obvestilo lahko ohrani dejstvo, datum in obseg odstranitve brez ponovitve sporne vsebine. Zgodovina, predpomnilniki, depoziti in zrcala utegnejo zahtevati usklajeno omejitev ali odstranitev; nov commit ne zadostuje. Nujna dokazila ohranite le pod odobrenim omejenim dostopom in po veljavnih pravilih hrambe. Ne obljubljajte popolnega izbrisa tujih kopij ali pravnega izida brez institucionalnega nasveta.

## Pravice in upravljanje so založniška infrastruktura

Izvirno besedilo priročnika uporablja CC BY 4.0, izvirna koda pa MIT. Za tuje gradivo veljajo njegovi pogoji. Ločite odprto licencirano razlago od reproducirane slike, navedka ali pridobljene podatkovne zbirke. CC BY 4.0 zahteva pripis zaslug in označitev sprememb; ne razrešuje vseh vprašanj zasebnosti, osebnostnih ali moralnih pravic. Izjeme označite ob predmetu, ne le v oddaljeni datoteki repozitorija.[^living-cc]

Morebitna neizključna založniška pogodba naj ohrani dogovorjeno možnost vzdrževanja in razširjanja odprte izdaje ter določi obveznosti glede produkcije, depozita in popravkov. Besedilo zahteva dogovor; poglavje ne potrjuje podpisane pogodbe in ne daje pravnega soglasja. Založniško priznanje, gostovanje, imetništvo pravic in skrbništvo repozitorija lahko pripadajo različnim stranem. Določite, kdo odloča o strokovnih sporih, pregleduje prevode, obravnava nujne odstranitve in potrjuje izdaje, ter kdo ga nadomesti ob navzkrižju interesov.

## Vzdrževanje, dolgoročna hramba in nasledstvo

Delujoče spletno mesto ustvarja obveznosti: odvisnosti se starajo, povezave selijo, poverilnice potečejo, primeri pa prenehajo delovati po opisu. Tehnični dolg poleg kode zajema nedokumentirane uredniške izjeme in razhajanje prevodov. Prednost določite po vplivu na dokazila, dostop in varnost. Spremenjen vmesnik lahko zahteva datirano opozorilo in preverjeno alternativo. Pri nedelujočem zgodovinskem viru morate ugotoviti, ali nadomestni naslov še podpira trditev; uspešen odziv HTTP tega ne potrdi.

Hramba zahteva več kot dodatno povezavo za prenos. Z repozitorijem se dogovorite, katere datoteke sprejme in ohranja, kdo vzdržuje pristajalne metapodatke in kako obravnava nove izdaje. Po prenosu preverite vrednosti SHA-256 ter preizkusite ponovni prevzem. Kontrolna vsota pomaga zaznati spremembo bajtov glede na zaupanja vredno izhodišče, ne potrdi pa pravilnosti interpretacije. Kjer pravice dopuščajo, poleg bralnih kopij ohranite izvor in pomembne odvisnosti. Manjkajoče zunanje sestavine navedite kot omejitev.[^living-fixity]

Migracija formata ustvari novo dokumentirano pretvorbo. Določite, kaj mora preživeti: kodiranje, cilji opomb, naslovi, odnosi v tabelah in lokatorji virov so lahko pomembnejši od enakih prelomov vrstic. Primerjajte pretvorjeno kopijo z izvirnikom, zapišite okolje, ohranite ustrezni izvirnik in izračunajte nove kontrolne vsote. Digital Preservation Coalition pri izbiri formatov in migracije poudarja bistvene lastnosti in preverjanje; končnica datoteke ni jamstvo.[^living-formats]

Dostopnost se nadaljuje po začetnem pregledu. Tipkovniški dostop, zaporedje naslovov, besedilne alternative, jezikovni metapodatki in berljive tabele se lahko ob spremembi gradiva ali orodij poslabšajo. WCAG 2.2 ponuja preverljiva merila, vendar avtomatizacija pokrije le del presoje. Navedite pregledane strani, formate, merila, podporne tehnologije in znane izjeme. Dostopni HTML ne dokazuje pravilnega bralnega zaporedja v ustvarjenem PDF.[^living-wcag]

Odhod ustanovnega urednika naj sproži postopek, ne iskanja po zasebni pošti. Določite organizacijskega nosilca, uredniškega naslednika in tehnični stik. Dokumentirajte nadzor nad repozitorijem in domeno, podaljševanja, odvisnosti, sklice na zaščitene poverilnice, varnostne kopije in preizkus obnove. Gesel ne objavljajte. Naslednik naj pred prenosom poskusno izvede gradnjo in popravek. Če ni naslednika ali sredstev, zaprite sprejem prispevkov, navedite konec vzdrževanja, oddajte zadnjo ustrezno izdajo v hrambo in označite nepodprte postopke. Jasno zaključen vir je lahko uporabnejši od navidez živega mesta brez odgovornega vzdrževalca. [Postopek načrtovanja vzdrževanja in nasledstva](../workflows/publishing/prepare-a-maintenance-and-succession-plan.md) omogoča preverjanje teh obveznosti.

## Vaja

V paru popišite šest predmetov majhnega učnega projekta: jezikovni različici poglavja, postopek, podatkovno zbirko, ustvarjeno bralno kopijo in gradbena navodila. Pripravite zapise v treh povezanih postopkih. Identifikatorje in kontrolne vsote pustite izrecno v čakanju, dokler jih ne pridobite; javne izdaje ne ustvarjajte. Razporedite realistični mesečni okvir dveh ur vzdrževanja in pojasnite, česa z njim ne morete zagotoviti.

Izmenjajte zapise. Eden prevzame vlogo bralca s preneseno starejšo izdajo, drugi uvede napako podvojenih pisem ali nenamerno razkritje osebnih podatkov. Sledite odkritju, pregledu, obvestilu, nadomestitvi in navedku. Preverite, ali ima vsaka obljubljena datoteka odgovorno osebo, vsaka recenzijska trditev opredeljen obseg in zasebnostni primer rešitev brez ponovnega razkritja. Oddajte popravljene zapise in utemeljitev sporne odločitve. Presojajte dokaze in argumentacijo, ne pripravljenosti na objavo.

## Refleksija

- Katere založniške trditve izhajajo iz datotek in katere zahtevajo institucionalne zaveze?
- Kdaj odgovornost do zgodovinskega zapisa zahteva omejitev javnega dostopa?
- Kaj bi slovenski bralec izgubil, če bi objavili le angleški popravek?
- Katera naloga bi ostala brez nosilca, če vzdrževalec jutri odide?

## Povzetek

Živa znanstvena publikacija omogoča preverjanje svoje spreminjajoče se avtoritete. Obseg recenzije, določljive izdaje, sled popravkov in skrbno navajanje povezujejo dokazila skozi čas. Upravljanje, soglasje, pravice, dostopnost in preverjena hramba omogočajo uporabo teh zapisov. Bralec naj ugotovi, kaj je bilo objavljeno, kaj in zakaj se je spremenilo ter kdo še odgovarja za skrb za publikacijo.

## Nadaljnje branje

- UNESCO. 2019. [Recommendation on Open Educational Resources (OER)](https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer). Določila o vzdržnosti primerjajte s proračunom publikacije.
- Digital Preservation Coalition. [Fixity and checksums](https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums) in [File formats and standards](https://www.dpconline.org/handbook/technical-solutions-and-tools/file-formats-and-standards), *Digital Preservation Handbook*. Opredelite odgovornost za preverjanje in migracijo.
- COPE. [Retraction guidelines](https://doi.org/10.24318/cope.2019.1.4), različica 3, 2025. Ločite nezanesljive ugotovitve od pregledno popravljene omejene napake.
- GitHub. [Immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases). Preverite, katere predmete varuje zaščita.
- W3C. [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/). Avtomatizacijo povežite z ročno presojo.

Zunanjo dokumentacijo spodaj smo preverili **7. septembra 2026**. Aktualne smernice COPE smo preverili v indeksirani uradni vsebini; neposredni prevzem strani ni bil na voljo. Pred dejansko izdajo znova preverite delovanje storitev in institucionalne dogovore.

[^living-oer]: UNESCO, [Recommendation on Open Educational Resources (OER)](https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer), sprejeto 25. novembra 2019.
[^living-git]: Scott Chacon in Ben Straub, *Pro Git*, druga izdaja, [Git Basics—Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging).
[^living-github]: GitHub Docs, [About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) in [Immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases).
[^living-zenodo]: Zenodo, [Digital Object Identifier (DOI)](https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/).
[^living-semver]: Tom Preston-Werner, [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).
[^living-credit]: NISO, [CRediT—Contributor Role Taxonomy](https://credit.niso.org/).
[^living-cope]: COPE, [Retraction guidelines](https://doi.org/10.24318/cope.2019.1.4), različica 3, avgust 2025.
[^living-cc]: Creative Commons, [Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).
[^living-fixity]: Digital Preservation Coalition, [Fixity and checksums](https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums).
[^living-formats]: Digital Preservation Coalition, [File formats and standards](https://www.dpconline.org/handbook/technical-solutions-and-tools/file-formats-and-standards).
[^living-wcag]: W3C, [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/).
