---
title: "Modeli, dokazno gradivo in interpretacija"
description: "Kako z izborom, predstavljanjem, operacionalizacijo in preverjanjem kulturne vire pretvorimo v dokazno gradivo za humanistični argument."
tags: [temelji, modeliranje, dokazno-gradivo, interpretacija, negotovost]
status: draft
---

# Modeli, dokazno gradivo in interpretacija

## Učni cilji

Po tem poglavju boste znali:

- pojasniti pot od kulturnega vira prek izbora, konstruiranja podatkov in modeliranja do dokaznega gradiva in interpretacije;
- razlikovati med modeliranjem v širšem humanističnem pomenu ter statističnimi modeli in modeli strojnega učenja;
- pojasniti kritični namen pojma *capta*, ne da bi običajno rabo besede *podatki* razglasili za napačno;
- koncept operacionalizirati z enotami, indikatorji, pravili vključevanja in načrtom validacije;
- ločiti neposredni rezultat postopka od dokaznega gradiva ter dokazno gradivo od interpretacije;
- povezati natančno in oddaljeno branje z branjem napak, branjem odstopajočih primerov in vrnitvijo v kontekst;
- dva modela istega kulturnega vprašanja primerjati po tem, kaj pridobita, izgubita, podpreta in česa ne moreta ugotoviti;
- prepoznati negotovost v virih, merjenju, modelu, vizualizaciji in interpretaciji.

## Pred začetkom: kdaj nastane dokazno gradivo?

Zamislite si časopisni članek: minister gospodarsko napoved imenuje »spodbudna«, opozicijska govorka javnosti pripiše »strah«, karikatura pa celotno razpravo prikaže kot nesmiselno. Kaj bi bilo dokazno gradivo o čustvih: navedeni besedi, čustva, ki jih govorci pripisujejo političnim akterjem, karikatura, odzivi občinstva ali raziskovalčeva poznejša klasifikacija? Z vsakim odgovorom ustvarimo drug raziskovalni predmet.

**Predznanje:** preberite [Kaj je digitalna humanistika?](what-is-digital-humanities.md) in predhodno poglavje o [zgodovinah digitalne humanistike](history-of-digital-humanities.md). Programiranje in statistika nista potrebna. **Vhod za vajo:** omejeno humanistično vprašanje in manjši sklop kulturnih virov, ki jih smete raziskovalno uporabiti. **Rezultat:** dva konkurenčna modela z opisom njunih spoznavnih meja. **Preverjanje:** drugi bralec mora prepoznati vsako enoto, kategorijo, preoblikovanje in korak sklepanja. **Pogoste napake:** priročni zapisi veljajo za popoln arhiv, metoda dobi ime pred natančno opredelitvijo vprašanja ali pa rezultat postopka nastopa kot lastna razlaga. **Etične in licenčne omejitve:** spoštujte avtorsko pravo, zasebnost in pravico skupnosti do odločanja; iz javne govorice brez utemeljene raziskovalne zasnove ne sklepajte o notranjem stanju posameznika.

Poglavje sledi analitični verigi:

> **kulturni vir → izbor in predstavitev → podatki oziroma *capta* → model → rezultat → dokazno gradivo → interpretacija**

Puščice ne pomenijo nepovratnega časovnega zaporedja. Interpretacija usmerja izbor, odstopajoči primer nas vrne k viru, neuspešna validacija pa zahteva popravek modela. Veriga je koristna predvsem zato, ker preprečuje zamenjevanje različnih spoznavnih vlog.

## Terminološka opomba

V slovenščini je **modeliranje** ustaljeno za postopek oblikovanja in preizkušanja modela, **operacionalizacija** pa za povezavo pojma z opazljivimi postopki. Ni sopomenka tehnične izvedbe. **Formalizacija** pomeni, da izbrana razmerja izrazimo dovolj izrecno za dosledno uporabo. Za *distant reading* uporabljamo **oddaljeno branje**, za *close reading* pa **natančno branje**.

Angleški *output* prevajamo z **rezultat**, kadar je pomemben neposredni proizvod postopka; **izhod** ohranjamo za ožjo tehnično rabo. *Evidence* je v tem poglavju **dokazno gradivo**, saj slovenska **evidenca** pomeni urejen popis ali register in ne spoznavne vloge gradiva v argumentu. *Capta* ohranjamo kot avtorski pojem Johanne Drucker in ga pojasnjujemo kot **zajete oziroma konstruirane podatke**. Ti izrazi v slovenski humanistični rabi niso povsod ustaljeni, zato je pomembnejša dosledna razlaga od navidezne terminološke enotnosti.

## Predstavljanje in modeliranje: namenska nepopolnost

Model je selektivna predstavitev za določen namen. Kronologija modelira sosledje, znanstvena izdaja besedilo in njegove različice, katalog zbirko, zemljevid prostorska razmerja, shema podatkovne zbirke pa entitete in njihove povezave. Tudi pojem zgodovinskega obdobja modelira razlike v času. Ni nujno, da je model številski. McCarty modeliranje opredeli kot hevristično prakso: predstavitev oblikujemo in z njo ravnamo zaradi proučevanja ali pa zasnujemo nekaj, kar želimo šele uresničiti. Modeliranje je zanj dejaven in ponavljajoč se postopek, v katerem odpor gradiva spreminja začetno zasnovo.[^modeliranje]

Selektivnosti ni mogoče preprosto odpraviti. Zemljevid, ki bi ohranil prav vse materialne značilnosti pokrajine, ne bi več opravljal naloge zemljevida. Zato sprašujemo natančneje: **katere razlike model ohrani, katere potisne ob stran, za čigav namen in s kakšnimi posledicami?** Model korespondence, urejen po pošiljatelju in prejemniku, omogoča analizo omrežja, vendar lahko zakrije osnutke, tajniško delo, negotovo avtorstvo in materialno zaporedje mape. Model, ki izhaja iz arhivske mape, bi razkril druga razmerja.

Beseda *model* ima tudi ožje tehnične pomene, ki jih je treba razločiti:

1. **Humanistični oziroma pojmovni model** predmet vzpostavi z izborom entitet, odnosov, mej, zaporedij ali gledišč. Argument ali vmesnik lahko modelira področje brez enačbe.
2. **Statistični model** izrazi razmerja med spremenljivkami in ob navedenih predpostavkah navadno predstavi tudi variabilnost ali negotovost. Lahko je opisen, napoveden ali namenjen sklepanju.
3. **Model strojnega učenja** je naučen iz primerov za nalogo, kakršne so klasifikacija, razvrščanje, napovedovanje ali učenje predstavitev. Mednje sodijo nadzorovani klasifikatorji in modeli vektorskih predstavitev, vendar z njimi ne izčrpamo modeliranja.

Ožja modela sta vključena v širšo raziskovalno zasnovo. Pred učenjem klasifikatorja je skupina že modelirala arhiv: izbrala je dokumente, opredelila oznako in enoto ter določila lastnosti, ki jih bo mogoče obdelati. Underwood poudarja statistične modele, ker je z njimi mogoče povezati jezikovne meritve z družbeno ali literarno pomenljivimi kategorijami; McCarty pa širši hevristični pomen izrecnega predstavljanja.[^vrste-modelov] Ne gre za soglasno definicijo, temveč za dve ravni modeliranja.

## Od kulturnega vira do podatkov oziroma *capta*

Kulturni vir ni prozorna posoda dejstev. Ima zgodovino nastanka, materialno obliko, institucionalno mesto in starejše načine uporabe. Korpus parlamentarnih govorov je odvisen od pravil razprave, načina zapisovanja in arhivskega ohranjanja, še preden ga raziskovalec prenese. Pri pripravi analitičnih zapisov se dodajo nove odločitve: katere seje vključiti, ali medklice šteti kot govor, kako razrešiti govorce, kaj velja za poved in kako predstaviti poznejše popravke.

Drucker je predlagala izraz *capta*—nekaj zajetega, ne preprosto danega—da bi poudarila ta konstitutivna dejanja. Njen poseg je posebej prepričljiv pri vizualizacijah, v katerih so izbrane, očiščene in zbirno prikazane vrednosti videti kot neposredna slika neodvisne resničnosti. Pred grafom vedno stoji parametrizacija.[^capta] Vendar *capta* ni obvezna zamenjava za vsako rabo besede *podatki*. Lavin sprejme umeščenost in konstruiranost vednosti, zavrne pa trditev, da nas beseda *data* nujno zavezuje naivnemu realizmu. Podatki so lahko nepopolni in namensko zbrani, vendar še vedno empirično uporabni.[^umesceni-podatki]

V nadaljevanju so **podatki** krovni izraz, ***capta***, **zajeti podatki** ali **konstruirani podatki** pa poudarijo dejanje izbora. Od poimenovanja je pomembnejše, ali projekt dokumentira:

- povezavo med kulturnim virom in analitičnim zapisom;
- vzorčni okvir, izpuste in pogoje dostopa;
- prepis, OCR, normalizacijo in anotiranje;
- zgodovinske kategorije ob kategorijah raziskovalne zasnove;
- provenienco, pravice, različice in odgovorno delo;
- ljudi ali skupnosti, ki jih zbiranje in klasifikacija lahko izpostavita škodi.

D'Ignazio in Klein podatkovno delo obravnavata kot razporeditev moči: kdo določa, kaj bo štelo, čigavo znanje ima avtoriteto, kdo prejme priznanje in kdo utrpi posledice.[^moc] Ta argument empiričnega raziskovanja ne razvrednoti, ampak položaj raziskovalca, delo in učinke konstruiranja podatkov vključi v metodo. Praktična navodila za vrstice, identifikatorje, manjkajoče vrednosti in provenienco so v poglavju [Podatki, metapodatki in modeli](data-metadata-models.md); tukaj sprašujemo, katere trditve takšni postopki sploh dopuščajo.

## Enote, kategorije in operacionalizacija

Humanistični pojmi, kakršni so žanr, vpliv, strah, javni spomin ali obrobnost, v analizo ne vstopijo že s poimenovanjem. **Operacionalizacija** pojem poveže z opazovanjem: določi, kaj bomo pregledovali in po katerih pravilih. Uporabna operacionalna definicija vsebuje vsaj:

- **pojem** in tisti njegov vidik, ki ga vprašanje zadeva;
- **enoto**, na primer pojavnico, odlomek, govor, knjigo, osebo, dogodek ali kraj;
- enega ali več **indikatorjev**, torej opazljivih značilnosti, pomembnih za pojem;
- **pravila vključevanja in izključevanja** za mešane, odsotne in negotove primere;
- **postopek**, po katerem nastane vrednost ali kategorija;
- **načrt validacije**, s katerim preverimo, ali postopek v danem kontekstu meri predvideni pojem.

Moretti operacionalizacijo predstavi kot most od pojma k merjenju. Ko pomembnost dramskega lika enkrat meri s številom izgovorjenih besed, drugič pa s številom povezav med liki, dobi različna protagonista. Prav razlika je spoznavno koristna, saj vsak postopek razkrije drugo razsežnost pomembnosti.[^operacionalizacija] Sama natančnost pa ne zagotavlja veljavnosti. Adcock in Collier ločita spor o pojmu od napak v opazovanjih, s katerimi ga merimo, ter validacijo navežeta na kontekst trditve.[^veljavnost] Operacionalizacija zato ni zgolj krčenje bogatega pojma. Je tudi razjasnitev, primerjava in preizkus njegovega stika z viri.

»Strah v političnem jeziku« lahko operacionaliziramo vsaj s štetjem besed, povezanih s strahom; z označevanjem mest, kjer govorec strah izrazi; z označevanjem strahu, ki ga pripiše drugemu; ali z odzivi bralcev na zastrašujoče uokvirjanje. To niso različne meritve ene skrite količine, temveč različna razmerja med jezikom, govorcem, tarčo in občinstvom.

Pri kategoriji zabeležimo, ali izvira iz zgodovinskega vira, jo je uvedel raziskovalec ali pa se je model nauči iz označenih primerov. Kataloška oznaka iz 19. stoletja in sodobni normalizirani žanr sta dva podatka, ne sopomenki. Kategorije omogočajo primerjavo, lahko pa reproducirajo institucionalna izključevanja. Kjer je mogoče, ohranimo izvirno poimenovanje, za resnično dvoumne pojave predvidimo mešano ali negotovo vrednost, kategorijo »drugo« pa pregledujemo.

## Formalizacija, pridobitve in izgube

S **formalizacijo** izbrana razmerja izrazimo tako izrecno, da jih lahko uporabljamo dosledno. Kodirni priročnik določi oznake, TEI razlikuje sestavine besedila, graf predstavi osebe kot vozlišča in odnose kot povezave, enačba pa navede razmerje med spremenljivkami. Računalniška obdelava zahteva posebno vrsto izrecnosti in doslednosti, zato lahko razkrije predpostavke, ki so v prozi ostale tihe. McCarty nepričakovani rezultat in neuspeh modela razume kot osrednjo spoznavno možnost, ne le kot tehnično motnjo.[^modeliranje]

Vsaka formalizacija ima razmerje med pridobitvami in izgubami:

| Formalna odločitev | Možna pridobitev | Možna izguba ali odmik |
| --- | --- | --- |
| Ena vrstica za vsak govor | primerljive enote in povezava z metapodatki | medklici, postavitev strani in izmenjava med govorci se umaknejo |
| Vnaprej določene oznake čustev | dosledno označevanje in štetje | mešani, zgodovinsko posebni ali nepoimenovani afekti se prisilno ločijo |
| Omrežne povezave za korespondenco | relacijski vzorci postanejo izračunljivi | materialnost pisma in pomen razmerja se skrčita |
| Dvorazsežni grafikon | spremembe so hitro primerljive | manjkajočnost, agregiranje in druge lestvice izginejo |

Izguba še ne dokazuje neuspeha, tako kot formalna urejenost ne dokazuje veljavnosti. Presoditi moramo, ali pridobitev odgovarja na vprašanje, ali izguba ogroža trditev in ali lahko pomembni vidik povrne druga predstavitev. Nekatere izgube so popravljive, ker zapis vodi nazaj k viru; druge so strukturne, denimo kadar ustanova ustnega pričevanja nikoli ni zbrala.

Formalizacija obsega tudi prikaz. Burdick in soavtorji opozarjajo, da vmesnik, podatkovna zbirka, navigacija, dostop in ohranjanje sodelujejo pri uprizarjanju digitalnega znanstvenega argumenta.[^vmesnik] Razvrstitev zadetkov, začetni izrez zemljevida ali skrita kategorija »neznano« zato niso le embalaža po analizi. So nadaljnji modeli, ki usmerjajo pozornost in omejujejo možnosti pregleda.

## Prehajanje med merili: natančno, oddaljeno in diagnostično branje

Morettijevo **oddaljeno branje** je vpliven poskus proučevanja literarnih sistemov in obsežnih množic besedil zunaj meja kanona. S polemično ostrino je zavrnilo domnevo, da lahko nekaj intenzivno branih del zastopa literarno zgodovino.[^oddaljeno] Izraz pa je utrdil tudi nerodno nasprotje: natančno branje naj bi pomenilo interpretacijo, oddaljeno pa številke. Underwood makroskopsko literarno zgodovino poveže s knjižno zgodovino in družboslovjem ter poudari, da je od gole velikosti korpusa pomembnejši model povezovanja jezikovnega in družbenega gradiva.[^underwood]

Oba načina je bolje razumeti kot gibanje med ravnmi:

1. **Oddaljena orientacija** primerja porazdelitve v zbirki in poišče vzorec, ki ga en sam odlomek ne more potrditi.
2. **Natančno branje** razčleni obliko, retoriko in dvoumnost izbranih odlomkov ter pomaga kategorije zasnovati ali izpodbijati.
3. **Branje napak** pregleda lažno pozitivne in negativne rezultate, napake OCR ter nesoglasja označevalcev, da bi odkrili meje podatkov ali operacionalizacije.
4. **Branje odstopajočih primerov** obravnava nenavadne, vendar ne nujno napačne vire, ki lahko pokažejo drug žanr, obdobje, arhivsko prakso ali razlago.
5. **Vrnitev v kontekst** vzorec pred oblikovanjem trditve poveže z nastankom in kroženjem virov, ustanovami, zgodovino jezika ter dosedanjimi raziskavami.

Izraza **branje napak** in **branje odstopajočih primerov** sta v tem poglavju pedagoški poimenovanji praks, ne ustaljeni raziskovalni šoli. Napaka je odmik glede na določeno nalogo ali referenčni standard; odstopajoči primer pa je nenavaden glede na porazdelitev in je lahko najzanimivejši vir v zbirki. Nobenega ne izbrišemo brez pojasnila. Natančno branje sodeluje že pri pripravi kodirnega priročnika in kritiki vizualizacije. Oddaljeno raziskovanje lahko zajame petdeset premišljeno izbranih besedil, ne nujno milijonov. Merilo določa razmerje med vprašanjem, enoto, dostopno populacijo in obstoječim znanjem.

Ramsay v algoritemski preobrazbi vidi povod za kritično branje, ne postopek, ki bi določil končni pomen.[^ramsay] Raziskovalni krog je zato **vir → model → rezultat → izbrani odlomki → popravljen model**. Prehajanje med merili je hkrati validacija in odkrivanje.

## Rezultat še ni dokazno gradivo

Tri izraze moramo razmejiti:

- **Rezultat** oziroma v ožji tehnični rabi **izhod** je neposredni proizvod postopka: število, oznaka, verjetnost, tema, gruča, vektorska predstavitev, zemljevid ali grafikon.
- **Dokazno gradivo** je vir ali rezultat, ki ga s provenienco, validacijo, primerjavo in omejitvijo trditve utemeljeno vključimo v argument.
- **Interpretacija** je obrazložena povezava med dokaznim gradivom, humanističnim vprašanjem, kontekstom in drugimi možnimi razlagami.

Vloga istega predmeta se lahko spremeni. Verjetnost klasifikatorja je med preverjanjem sistema rezultat. Ko dokumentiramo korpus, oznake, preizkus in napake, lahko porazdelitev napovedi postane dokazno gradivo za trditev o jeziku znotraj izbrane operacionalizacije. S tem še ne dokazuje notranjih občutij avtorjev ali odzivov občinstva. Presenetljiv odlomek med lažno pozitivnimi rezultati lahko pozneje podpre povsem drugačen argument natančnega branja.

Prehod od rezultata k dokaznemu gradivu zahteva vsaj štiri preverjanja:

1. **Provenienca:** ali lahko rezultat povežemo z viri, preoblikovanji, različicami in odgovornimi osebami?
2. **Veljavnost:** ali postopek res zadeva predvideni pojem in s katerim neodvisnim virom, strokovno presojo ali zadržanimi primeri smo to preverili?
3. **Primerjava:** ali vzorec obstane ob preprostem izhodišču, drugem vzorcu, drugi operacionalizaciji ali verjetni alternativni razlagi?
4. **Sorazmernost trditve:** ali sklep ostaja znotraj dejansko proučene populacije, obdobja, jezika in vrste razmerja?

Dokazno gradivo interpretacijo omejuje, vendar je ne izbere mehansko. Enako spremembo frekvence je mogoče razložiti s sestavo žanrov, političnim dogodkom ali pomenskim premikom. Razlage niso enako močne, če ena spregleda znano manjkajočnost ali nasprotuje odlomkom iz virov. Pluralnost humanistične interpretacije ne pomeni poljubnosti.

Underwood z modelom povezuje jezikovne spremenljivke z že pomenljivimi družbenimi ali literarnimi kategorijami; Ramsay odpira interpretativne možnosti; Drucker poudarja, da predstavitev sodeluje pri vzpostavitvi predmeta.[^spoznavna-razhajanja] Njihovi poudarki niso soglasen program. Skupna zahteva, ki jo lahko izpeljemo, je skromnejša: pokažimo, kako je rezultat postal dokazno gradivo in zakaj je predlagana interpretacija boljša od drugih.

## Negotovost, dvoumnost in vizualna oblika

Negotovosti z različnih ravni niso zamenljive:

| Mesto negotovosti | Ključno vprašanje | Primeren odziv |
| --- | --- | --- |
| Vir in korpus | Kaj manjka, je poškodovano, nedostopno ali čezmerno zastopano? | dokumentiramo vzorčni okvir, vrzeli in pogoje ohranitve |
| Predstavitev in merjenje | Katera enota ali kategorija je dvoumna in kako pogosto se presoje razlikujejo? | ohranimo alternative, nesoglasje ali stopnjo zaupanja ter popravimo navodila |
| Model in rezultat | Kako je rezultat občutljiv na podatke, parametre, naključje ali premik področja? | uporabimo zadržani preizkus, izhodišča, umerjanje in analizo občutljivosti |
| Vizualizacija | Katera privzeta izbira, razred, lestvica ali grafični znak prikazuje preveliko gotovost? | pokažemo imenovalce, manjkajočnost, intervale in pomembne oblikovalske izbire |
| Interpretacija | Katere kontekstualne razlage iz zbranega gradiva ne moremo razrešiti? | omejimo trditev in navedemo konkurenčne razlage ali potrebno novo gradivo |

Interval zaupanja lahko ob upravičenih predpostavkah izrazi vzorčno ali modelsko negotovost. Ne more nadomestiti manjkajočega arhiva, odločiti, ali je ironija strah, ali zajeti vsega interpretativnega nesoglasja. Tudi prosojnost sama ne odpravi negotovosti: objavljena koda razkrije postopek, ne pa ustreznosti pojma.

Drucker zahteva vizualne oblike za umeščeno in interpretativno vednost, *Digital_Humanities* pa oblikovanje vmesnika in prikaza vključi v znanstveni argument.[^vizualna-negotovost] Iz tega ne sledi, da je vsak stolpčni graf naiven ali da dekorativna zameglitev predstavlja dvoumnost. Prikaz mora ustrezati vrsti negotovosti. Včasih potrebujemo interval, drugič vrzel, več vzporednih razvrstitev, povezavo na odlomek ali izrecno priznanje, da gradivo vprašanja ne more razrešiti. Zadnje je **interpretativna negotovost**, ne grafična napaka.

## Razdelan primer: trije modeli čustev v parlamentarni razpravi

Predpostavimo vprašanje: **Kako so govorci med letoma 2000 in 2025 v slovenskih parlamentarnih razpravah o podnebni politiki uporabljali strah in upanje?** Korpus je licenciran, seje in govorci so dokumentirani, OCR pa ni del postopka; raziskujemo javni jezik, ne zasebnih duševnih stanj. Tri skupine lahko isto izhodišče operacionalizirajo različno.

| Model | Enota in kategorije | Rezultat in validacija | Kaj lahko podpre / česa ne more ugotoviti | Pridobitev / izguba |
| --- | --- | --- | --- | --- |
| **Leksikonsko štetje** | Enota: lematizirana pojavnica v govoru. Kategoriji: besede, povezane s strahom ali upanjem; zadetki v zanikanju so dodatno označeni. | Rezultat: zadetki na 1.000 pojavnic po obdobju in vlogi govorca. Na stratificiranem vzorcu konkordanc preverimo zanikanje, navedke, pregibanje in zgodovinske pomene ter primerjamo izhodišče brez lematizacije. | Podpre porazdelitev besedišča, povezanega z leksikonskima kategorijama. Ne pokaže, kdo čustvo doživlja, ali je odlomek ironičen in kako se je odzvalo občinstvo. | Pridobimo obseg, hitrost in pregledna pravila; izgubimo skladnjo, pripisovanje, implicitni izraz in del zgodovinske semantike. |
| **Ročno označevanje izraženega in pripisanega čustva** | Enota: stavek ali del povedi skupaj z govorcem, morebitnim nosilcem čustva in tarčo. Kategorije: govorec izraža strah/upanje; čustvo pripiše drugemu; citira izraz; mešano/negotovo; odsotno. | Rezultat: označeni odlomki, deleži kategorij in nesoglasja označevalcev. Preverimo s poskusnim označevanjem, neodvisnim dvojnim kodiranjem, zapisnikom razreševanja, nasprotnimi primeri in branjem celotnih govornih izmenjav. | Podpre razlago, kako govor razporeja čustva med akterje. Ne razkrije zasebnega stanja in le stežka zajame ves korpus; visoko ujemanje samo še ne dokazuje pojmovne veljavnosti. | Pridobimo vloge, tarče, implicitne izraze in kontekst; izgubimo obseg in povečamo količino dokumentiranega interpretativnega dela. |
| **Nadzorovani klasifikator z vektorskimi predstavitvami** | Enota: poved ali kratek govorni obrat. Kategorije prevzame iz ročne sheme; vektorska predstavitev (*embedding*) kodira kontekstualno podobnost, klasifikator pa oceni oznako ali verjetnost. | Rezultat: napovedi na zadržanem sklopu in zbirne ocene. Delitev opravimo po sejah in obdobjih; navedemo preciznost, priklic, umerjenost in zamenjave po razredih; pregledamo zgodovinska obdobja, napake in najbližje primere ter primerjamo z leksikonskim in večinskim osnovnim modelom. | Podpre oceno porazdelitve anotacijske sheme, če sta uspešnost in časovna stabilnost zadostni. Kategorij ne spremeni v naravne vrste, ne povrne izpuščenih arhivov in ne dokaže učinka na občinstvo. | Pridobimo obseg in občutljivost za širši kontekst; izgubimo neposredno preglednost pravil, jezik skrčimo v naučene razsežnosti ter tvegamo premik obdobja ali vira. |

Besedno-čustveni leksikon izraze povezuje s kategorijami; že njegovi avtorji razlikujejo med povezavo besede s čustvom in čustvom, ki ga beseda vzbudi v bralcu.[^leksikon] Sodobna računalniška analiza čustev obsega klasifikacijo, regresijo in označevanje udeleženskih vlog, zato »analiza čustev« ni enoten postopek.[^analiza-custev] Modeli se lahko razhajajo, ne da bi bil eden tehnično pokvarjen. Beseda *strah* znotraj navedkov lahko dvigne leksikonsko krivuljo, pri ročnem delu dobi oznako pripisanega čustva, klasifikator, naučen pretežno na neposrednih izrazih, pa jo napačno razvrsti. Razlika je dokazno gradivo o operacionalizacijah.

Odgovorna interpretacija bi se lahko glasila: *v licenciranem korpusu sej so po določenem letu pogostejši neposredni in citirani izrazi, povezani s strahom, medtem ko se delež ročno označenih primerov, v katerih strah izraža sam govorec, ni povečal enako*. Za zgodovinsko razlago bi morali natančno prebrati odlomke ter proučiti politične dogodke, parlamentarno retoriko in sestavo korpusa. Preglednica sama spremembe ne pojasni.

## Vaja: oblikujte dva konkurenčna modela

Izberite vprašanje o kulturni zbirki—avtoriteto v pismih, mobilnost v časopisju, pripadnost v ustnih pričevanjih, žanr v knjižnem katalogu ali čustvo v pripovedništvu—in oblikujte **dva dejansko konkurenčna modela**.

Za vsakega navedite:

1. omejeno raziskovalno vprašanje in populacijo virov;
2. pravilo izbora in eno pomembno opustitev;
3. enoto, kategorije oziroma spremenljivke in indikatorje;
4. pravila za vključitev, izključitev, mešane in manjkajoče primere;
5. pričakovani rezultat in načrt validacije;
6. eno trditev, ki jo rezultat lahko podpre, in eno, ki je ne more;
7. razmerje med pridobitvijo in izgubo;
8. načrt za branje napak, odstopajočih primerov in vrnitev v kontekst;
9. omejitve glede pravic, zasebnosti, škodljivega predstavljanja in dela.

**Rezultat:** primerjalna tabela in utemeljitev v 500 besedah. **Preverjanje:** modela zamenjajte z drugim bralcem, ki naj napove vsaj en odlomek, pri katerem bi se rezultata razlikovala. **Pogosta napaka:** če modela uporabljata isto enoto, kategorije in indikator, razlikuje pa se le programska oprema, gre verjetno za dve izvedbi iste operacionalizacije, ne za konkurenčna modela.

## Refleksija

- Pri kateri puščici v verigi od vira do interpretacije vstopi vaša najpomembnejša interpretativna odločitev?
- Katero izgubo formalizacije lahko popravite s povezavo nazaj na vir in katera je vgrajena že v arhiv?
- Je nesoglasje dveh označevalcev šum, dokaz slabih navodil ali dokaz spornosti pojma?
- Katero dodatno gradivo bi lahko odločilo med razlagama istega rezultata in katera razlika bi kljub temu ostala interpretativna?
- Ali vizualizacija prikazuje izmerjeno negotovost, zgolj simbolizira dvom ali težavo zakrije?

## Povzetek

Digitalnohumanistično dokazno gradivo nastane v popravljivi verigi od kulturnih virov do trditev. Izbor in predstavitev konstruirata podatke; *capta* poudari to dejavno zajemanje, vendar je tudi običajni izraz *podatki* povsem ustrezen, če je njihova umeščenost dokumentirana. Humanistično modeliranje zajema pojmovne, materialne in vmesniške predstavitve, ne le statističnih modelov in strojnega učenja. Operacionalizacija poveže pojem z enotami, indikatorji, pravili in validacijo. Formalizacija prinaša pridobitve in izgube, ki jih moramo navesti, ne vnaprej slaviti ali obsojati.

Rezultat postane dokazno gradivo šele s preverjeno provenienco, veljavnostjo, primerjavo in sorazmerno trditvijo. Dokazno gradivo interpretacijo omejuje, ne avtomatizira. Natančno in oddaljeno branje, branje napak in odstopajočih primerov ter vrnitev v kontekst omogočajo ponavljajoče se prehajanje med merili. Manjkajoči arhiv, dvoumna kategorija, napaka merjenja, nestabilen model, retorika vizualizacije in več možnih razlag so različne negotovosti, ki zahtevajo različne odzive. Cilj ni brezhiben cevovod, temveč pregleden argument: drugi raziskovalec mora videti, kaj smo zajeli, preoblikovali in preverili, kaj smo ugotovili in kaj ostaja odprto.

## Nadaljnje branje in viri

- Adcock, Robert, in David Collier. »[Measurement Validity: A Shared Standard for Qualitative and Quantitative Research](https://doi.org/10.1017/S0003055401003100)«. *American Political Science Review* 95, št. 3 (2001): 529–546. DOI: `10.1017/S0003055401003100`.
- Burdick, Anne, Johanna Drucker, Peter Lunenfeld, Todd Presner in Jeffrey Schnapp. [*Digital_Humanities*](https://doi.org/10.7551/mitpress/9248.001.0001). MIT Press, 2012. DOI: `10.7551/mitpress/9248.001.0001`.
- D'Ignazio, Catherine, in Lauren F. Klein. [*Data Feminism*](https://doi.org/10.7551/mitpress/11805.001.0001). MIT Press, 2020. DOI: `10.7551/mitpress/11805.001.0001`.
- Drucker, Johanna. »[Humanities Approaches to Graphical Display](https://digitalhumanities.org/dhq/vol/5/1/000091/000091.html)«. *Digital Humanities Quarterly* 5, št. 1 (2011). Spletno mesto *Digital Humanities Quarterly*, ki ga objavljata Alliance of Digital Humanities Organizations in Association for Computers and the Humanities. Dostop 22. julija 2026.
- Lavin, Matthew. »[Why Digital Humanists Should Emphasize Situated Data over Capta](https://doi.org/10.63744/r8bk8knh3wbk)«. *Digital Humanities Quarterly* 15, št. 2 (2021). DOI: `10.63744/r8bk8knh3wbk`.
- McCarty, Willard. »[Modeling: A Study in Words and Meanings](https://doi.org/10.1002/9780470999875.ch19)«. V *A Companion to Digital Humanities*, ur. Susan Schreibman, Ray Siemens in John Unsworth, 254–270. Blackwell, 2004. DOI: `10.1002/9780470999875.ch19`.
- Mohammad, Saif M., in Peter D. Turney. »[Crowdsourcing a Word–Emotion Association Lexicon](https://doi.org/10.1111/j.1467-8640.2012.00460.x)«. *Computational Intelligence* 29, št. 3 (2013): 436–465. DOI: `10.1111/j.1467-8640.2012.00460.x`.
- Moretti, Franco. [*Distant Reading*](https://www.versobooks.com/products/2309-distant-reading). Verso, 2013. Spletno mesto *Verso Books*. Dostop 22. julija 2026.
- Moretti, Franco. »[Operationalizing: Or, the Function of Measurement in Literary Theory](https://doi.org/10.64590/daw)«. *New Left Review* 84 (november–december 2013): 103–119. DOI: `10.64590/daw`.
- Ramsay, Stephen. [*Reading Machines: Toward an Algorithmic Criticism*](https://www.press.uillinois.edu/books/?id=p078200). University of Illinois Press, 2011. Spletno mesto *University of Illinois Press*. Dostop 22. julija 2026.
- Štajner, Sanja, in Roman Klinger. »[Emotion Analysis from Texts](https://doi.org/10.18653/v1/2023.eacl-tutorials.2)«. V *Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics: Tutorial Abstracts*, 7–12. Association for Computational Linguistics, 2023. DOI: `10.18653/v1/2023.eacl-tutorials.2`.
- Underwood, Ted. [*Distant Horizons: Digital Evidence and Literary Change*](https://doi.org/10.7208/chicago/9780226612973.001.0001). University of Chicago Press, 2019. DOI: `10.7208/chicago/9780226612973.001.0001`.

[^modeliranje]: McCarty, »Modeling«, zlasti delovna opredelitev modeliranja, razlika med modelom nečesa in modelom za nekaj ter vloga ponavljajočega se neuspeha. Njegova opredelitev je predlog skupnega intelektualnega jedra *humanities computing*, ne splošno sprejeta definicija vseh humanističnih metod.
[^vrste-modelov]: McCarty, »Modeling«, o širšem hevrističnem predstavljanju; Underwood, *Distant Horizons*, zlasti prvo poglavje, o statističnih modelih, ki jezikovne meritve povežejo z družbeno pomenljivimi kategorijami. Tukajšnja razlika med pojmovnim, statističnim in strojno naučenim modelom je analitična; dejanska raba se prekriva.
[^capta]: Drucker, »Humanities Approaches«, zlasti kritika vizualizacij, ki zakrijejo interpretativni okvir izbora in parametrizacije pojavov.
[^umesceni-podatki]: Lavin, »Why Digital Humanists«, sprejme konstruiranost in umeščenost vednosti, zavrne pa splošno pravilo, po katerem bi morali besedo *data* zamenjati s *capta*. Poglavje sledi tej kvalificirani drži.
[^moc]: D'Ignazio in Klein, *Data Feminism*, zlasti poglavja 1, 4, 5 in 6 o moči, klasifikaciji, delu in dejstvu, da številke niso lastna interpretacija.
[^operacionalizacija]: Moretti, »Operationalizing«, 103–119. Meri besedni prostor in omrežne povezave dramskih oseb; različni meritvi razkrijeta različni, hkrati relevantni razsežnosti literarne pomembnosti.
[^veljavnost]: Adcock in Collier, »Measurement Validity«, 529–546, o povezavi med izhodiščnim in sistematiziranim pojmom, indikatorji in rezultati merjenja ter o kontekstualni validaciji v kvalitativnem in kvantitativnem raziskovanju.
[^vmesnik]: Burdick idr., *Digital_Humanities*, zlasti razprava o tem, kako vmesnik, interaktivnost, podatkovna zbirka, označevanje, navigacija, dostop, razširjanje in arhiviranje uprizarjajo digitalni znanstveni argument. Knjiga je programski in oblikovalsko usmerjen predlog, ne dogovorjeni standard.
[^oddaljeno]: Moretti, *Distant Reading*. Knjiga združuje eseje iz dveh desetletij in razvija zavestno polemično alternativo literarni zgodovini, omejeni s kanonom; ni edina definicija obsežnega literarnega raziskovanja.
[^underwood]: Underwood, *Distant Horizons*, predgovor ter prvo in peto poglavje o makroskopski literarni zgodovini, statističnih modelih in tveganjih oddaljenega branja. Od gole velikosti korpusa razlikuje spoznavno nalogo modela.
[^ramsay]: Ramsay, *Reading Machines*, zlasti razumevanje algoritemske preobrazbe kot omejitve, ki ustvari predmet kritike, ne kot mehanizem dokončne interpretacije.
[^spoznavna-razhajanja]: Underwood, *Distant Horizons*; Ramsay, *Reading Machines*; Drucker, »Humanities Approaches«. Underwood poudari empirično validirane statistične modele, Ramsay generativno preoblikovanje in subjektivno kritiko, Drucker pa konstitutivno interpretacijo in vizualne oblike. V posameznem projektu jih je mogoče povezati, niso pa ista spoznavna drža.
[^vizualna-negotovost]: Drucker, »Humanities Approaches«; Burdick idr., *Digital_Humanities*. Drucker predlaga humanistično utemeljene grafične oblike, vendar iz njenega posega ne sledi, da lahko posamezen grafični prijem izrazi vse vrste dvoumnosti.
[^leksikon]: Mohammad in Turney, »Crowdsourcing«, 436–465. Raziskava razlikuje med vprašanjem, ali je izraz povezan s čustvom, in vprašanjem, ali ga pri bralcu vzbudi; besedno-čustveni leksikon ne določi psihološkega stanja govorca.
[^analiza-custev]: Štajner in Klinger, »Emotion Analysis from Texts«, 7–12, pregledata klasifikacijo, regresijo, označevanje udeleženskih vlog, jezikovne vire, družbene učinke in metodološke težave.
