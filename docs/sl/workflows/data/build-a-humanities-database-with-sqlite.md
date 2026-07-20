---
title: "Kako zgradim manjšo humanistično podatkovno zbirko s SQLite?"
description: "Osebe, dela in sodelovanja pretvorite v povezane tabele s ključi, provenienco in shranjenimi raziskovalnimi poizvedbami."
category: "Podatki"
difficulty: "srednje"
time: "90–180 min"
tags: [SQLite, SQL, podatkovna-zbirka, provenienca]
---

# Kako zgradim manjšo humanistično podatkovno zbirko s SQLite?

<div class="answer-meta" markdown>
<span>Podatki</span><span>srednje</span><span>90–180 min</span>
</div>

## Kaj želite doseči

V preglednici imate ponavljajoče se osebe, dela in vloge ter potrebujete strukturo za zanesljive popravke in poizvedbe. SQLite povezane tabele shrani v eni prenosljivi datoteki.

!!! quote "V eni povedi"
    Najprej modelirajte entitete in razmerja, zbirko ustvarite iz shranjene sheme, nato pa vsako raziskovalno vprašanje ohranite kot datoteko SQL.

## Potrebujete

- majhen očiščen vzorec CSV;
- SQLite ali vgrajeni modul Python `sqlite3`;
- skico entitet in razmerij;
- stabilne projektne identifikatorje ter sklice na vire.

## Postopek

### 1. Določite shemo

Ustvarite `schema.sql`:

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE person (
  person_id TEXT PRIMARY KEY,
  preferred_name TEXT NOT NULL,
  source_note TEXT
);

CREATE TABLE work (
  work_id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  year_start INTEGER,
  year_end INTEGER,
  date_note TEXT
);

CREATE TABLE contribution (
  person_id TEXT NOT NULL REFERENCES person(person_id),
  work_id TEXT NOT NULL REFERENCES work(work_id),
  role TEXT NOT NULL,
  source_id TEXT NOT NULL,
  certainty TEXT NOT NULL DEFAULT 'certain',
  PRIMARY KEY (person_id, work_id, role, source_id)
);
```

### 2. Ustvarite zbirko

```bash
sqlite3 data/project.sqlite < schema.sql
```

Če ukaz ni na voljo, uporabite Python.

### 3. Uvozite majhen vzorec

Osebe in dela uvozite pred vrsticami razmerij. Vključite preverjanje tujih ključev in se ob neveljavnih identifikatorjih ustavite, namesto da ustvarite osirotele zapise.

### 4. Shranite raziskovalne poizvedbe

Ustvarite `queries/works-per-person.sql`:

```sql
SELECT p.preferred_name, COUNT(DISTINCT c.work_id) AS work_count
FROM person AS p
LEFT JOIN contribution AS c USING (person_id)
GROUP BY p.person_id
ORDER BY work_count DESC, p.preferred_name;
```

Zaženite:

```bash
sqlite3 -header -csv data/project.sqlite < queries/works-per-person.sql \
  > output/works-per-person.csv
```

### 5. Preverite

Poiščite podvojena imena, prazne vire, nemogoče datumske razpone, osirotele ključe in različno zapisane kategorije. Naključni vzorec primerjajte z izvornimi dokumenti.

## Rezultat

Ponovno ustvarljiva zbirka SQLite, `schema.sql`, postopek uvoza, shranjene poizvedbe, podatkovni slovar in izvozi v odprtih formatih.

## Preverite se

- Lahko zbirko ponovno zgradite iz datotek v repozitoriju?
- Ima vsako razmerje dokaz?
- So negotovi datumi predstavljeni brez izmišljene natančnosti?
- Identifikatorji ostanejo stabilni, ko popravite ime?
- Levo povezovanje pokaže zapise brez razmerij?

## Pogoste pasti

- zbirko urejamo ročno, ne da bi zabeležili spremembe;
- imena uporabljamo kot primarne ključe;
- v eni celici hranimo več oseb;
- razmerja uvozimo pred preverjanjem entitet;
- objavimo samo datoteko `.sqlite` brez sheme ali podatkovnega slovarja.

## Naloga

Ustvarite tri tabele z najmanj desetimi osebami, desetimi deli in petnajstimi sodelovanji. Napišite eno poizvedbo, ki odgovori na vsebinsko vprašanje, in eno, ki odkrije manjkajoče podatke.
