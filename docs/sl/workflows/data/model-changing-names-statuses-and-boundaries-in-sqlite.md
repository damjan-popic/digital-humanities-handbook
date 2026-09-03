---
title: "Kako modeliram spreminjajoča se imena, statuse in meje v SQLite?"
description: "Preverljiv postopek z izrecnimi viri, modelnimi odločitvami in negotovostjo."
category: "Podatki"
category_id: "Data"
difficulty: "srednje"
time: "60–90 min"
tags: [modeliranje, provenienca, negotovost]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Kako modeliram spreminjajoča se imena, statuse in meje v SQLite?

Strojno podprt prevodni osnutek; potreben je strokovni jezikovni pregled.

## Kaj želite doseči

Ugotovite, kaj določen vir trdi o osebi v določenem času, ne da bi večjezična imena, konkurenčne poklicne oznake in spreminjajočo se ozemeljsko pripadnost združili v eno brezčasno vrstico. Sintetični dosje pokaže izgubo pri modeliranju; ne dokumentira resničnih prebivalcev. Primerjavo modelov pojasnjuje poglavje [Podatkovne zbirke in SQL](../../chapters/databases-sql.md).

## Potrebujete

Prenesite in razpakirajte [spremljevalni ZIP](../../../assets/downloads/contested-models-v1.zip). Uporabite Python 3.10 ali novejši z modulom SQLite iz standardne knjižnice, terminal in urejevalnik besedila. Nameščanje paketov ali ukaznega odjemalca SQLite ni potrebno. Najprej preberite `README.sl.md`, `input/dossier.sl.md` in `rights-and-provenance.sl.md`. Delajte na kopiji in ohranite izvorne podatke.

## Postopek

### 1. Preglejte trditve

Odprite `input/assertions.csv` in `schema.sql`. Trditev poveže subjekt z besedilom ali drugo entiteto ter ohrani izvorno besedilo, kontekst, interval veljavnosti, čas zapisa in zanesljivost. Intervali so polodprti: začetek je vključen, konec izključen. `event_window` pomeni možni datum dogodka, ne neprekinjenega trajanja.

Primerjajte A04 in A05: služkinja v institucionalnem besednjaku in šivilja v samoopisu se časovno prekrivata v letu 1910. Ne odločite z večinskim glasovanjem in obeh ne zamenjajte z navidezno nevtralnim poklicem. A02 in A03 pa predstavljata popravek prepisa; A03 izrecno nadomesti A02. Shema ohrani oba zapisa.

### 2. Zgradite zbirko in jo preglejte

V razpakirani mapi izvedite:

```bash
python run.py --output output-first
python query.py --database output-first/dossier.sqlite --subject SYN-A --as-of 1910-06-15 --known-at 2026-09-03T00:00:00Z
python query.py --database output-first/dossier.sqlite --conflicts
```

Nastane 13 trditev, od katerih je 12 trenutno veljavnih v uredniškem pogledu, ter en par za pregled statusnega neskladja. Preglejte `status-conflicts.csv` in `assertions-1910_corrected.csv`. Uspešna omejitev potrjuje notranjo skladnost, ne zgodovinske resnice.

### 3. Ločeno spremenite obe vrsti časa

Poizvedbo ponovite z `--known-at 2026-09-01T23:59:59Z`. Junijski podpis iz leta 1910 se zdaj glasi Ana Kovać, kot v zgodnejšem uredniškem prepisu, namesto Ana Kovač. Vrnite poznejši čas zapisa in `--as-of` spremenite v `1925-01-25`; preglejte status in jezikovno rabo.

V `queries/at-date.sql` preverite vezane parametre. Poizvedba izključi nadomeščeno trditev le, če je bil popravek že zapisan do izbranega uredniškega časa. Gre za majhen učni dnevnik z dodajanjem zapisov, ne za celovit sistem transakcijskega časa, ki bi ga upravljala podatkovna zbirka.

### 4. Sledite ozemeljski pripadnosti

Uporabite `--subject SYN-L1` z datumoma `1919-12-31` in `1920-01-01`. Pripadnost na meji intervala preide iz `SYN-EAST` v `SYN-W`. Izmišljeno bivališče ostane isto; to ni dokaz selitve. [Prostorski postopek](../mapping/model-changing-place-names-and-boundaries.md) ločeno preveri položajno negotovost.

### 5. Opišite izgubo pri izvozu

Tabelo trditev primerjajte z eno vrstico na osebo. Naštejte izgubljene razlike: ime posameznega vira, kontekst statusa, jezikovni pripis in rabo, zgodovino zapisov ter konkurenčne intervale. Priročen analitični CSV je dopusten, če ostanejo pravilo izbora in identifikatorji virov obnovljivi.

## Rezultat

Ohranite zbirko SQLite, izvorne CSV-je, rezultata za dva uredniška časa, tabelo neskladij in opombo o odločitvah. Zabeležite različici Python in SQLite, zgodovinski datum, uredniško časovno mejo ter ukaz. Seznama za pregled ne opisujte kot seznama dokazanih protislovij.

## Preverite se

- Je ohranjenih 13 trditev in v trenutnem pogledu 12?
- Se pri zgodnejšem času zapisa pojavi prejšnji prepis podpisa?
- Ali 1920-01-01 pripada samo novemu intervalu?
- Lahko vsako vrednost povežete z besedilom vira in kontekstom?

## Pogoste pasti

Prepisovanje imen, enačenje pripisanega jezika z dokazanim znanjem, razlaga letnega časovnega okna kot trajanja in obravnava tujih ključev kot dokazov so različne napake. Popravke opredelite. Paket datume preveri pred uvozom; sama shema SQL ne preveri vsakega koledarskega niza.

## Naloga

Oddajte primerjavo ploščatega, normaliziranega in trditvenega modela v treh vrsticah. Pojasnite eno neskladje in eno nadomestitev. Določite, katera razlika mora biti poizvedljiva in katera ostane v viru ali prozni opombi.
