---
title: "Kako uredim manjši projekt Python za NLP?"
description: "Uporabite preprosto zgradbo, ki loči podatke, skripte, rezultate in specifikacijo okolja."
category: "NLP"
difficulty: "začetno"
time: "20–40 min"
tags: [Python, projektna zgradba, ponovljivost, NLP]
---

# Kako uredim manjši projekt Python za NLP?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>začetno</span>
<span>20–40 min</span>
</div>

## Kaj želite doseči

Majhen projekt hitro postane nepregleden, če so izvorni podatki, skripte, rezultati, zapiski in virtualno okolje v isti mapi. Zgradili boste preprosto privzeto ureditev za manjši projekt NLP.

!!! quote "V enem stavku"
    Od začetka ločite surove podatke, obdelane podatke, skripte, rezultate, dokumentacijo in specifikacijo okolja.

## Kaj potrebujete

- Python 3.12 in projektno mapo;
- terminal ter urejevalnik besedila;
- pojasnjene pravice do vhodnih podatkov.

## Postopek

### 1. Ustvarite zgradbo map

```text
my-nlp-project/
├── data/
│   ├── raw/
│   └── processed/
├── output/
├── scripts/
├── README.md
├── requirements.txt
└── .gitignore
```

=== "Windows PowerShell"

    ```powershell
    New-Item -ItemType Directory -Name my-nlp-project
    Set-Location my-nlp-project
    New-Item -ItemType Directory -Path data, data\raw, data\processed, output, scripts
    New-Item -ItemType File -Path README.md, requirements.txt, .gitignore
    ```

=== "Bash (macOS/Linux/WSL)"

    ```bash
    mkdir -p my-nlp-project/data/raw my-nlp-project/data/processed my-nlp-project/output my-nlp-project/scripts
    cd my-nlp-project
    touch README.md requirements.txt .gitignore
    ```

### 2. Vsakemu delu določite vlogo

| Mapa ali datoteka | Namen |
| --- | --- |
| `data/raw/` | Izvirne vhodne datoteke; ne urejajte jih neposredno. |
| `data/processed/` | Očiščene ali pretvorjene datoteke. |
| `scripts/` | Skripte Python. |
| `output/` | Ustvarjene tabele, poročila, grafi, dnevniki in izvozi. |
| `README.md` | Človeku razumljiva razlaga vprašanja, virov, postopka in omejitev. |
| `requirements.txt` | Pregledane zahteve Python za ponovno izdelavo okolja. |
| `.gitignore` | Krajevne datoteke, ki jih Git ne sme ponuditi za potrditev. |

`.venv/` namenoma ni v drevesu. Ustvarite jo krajevno in prezrite. Je zavržljivo izvajalno okolje, ne specifikacija okolja; način obnove dokumentirata README in `requirements.txt`.

### 3. Dodajte osnovni `.gitignore`

```text
.venv/
.venv-rebuilt/
__pycache__/
*.pyc
.DS_Store
output/*.tmp
```

Celotne `output/` ne prezrite samodejno. Majhni rezultati so lahko pomembni za pregled. Prav tako ne prezrite izvornih podatkov, dokler niste odločili, ali jih je zaradi velikosti, licence, zasebnosti ali etike sploh dovoljeno vključiti.

### 4. Napišite kratek README

````markdown
# My NLP project

## Research question

Opišite eno omejeno humanistično vprašanje.

## Sources and rights

Opišite vhod, provenienco, licenco, zasebnost in omejitve.

## Python version

Use Python 3.12.

## Install with Bash

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

```bash
python scripts/name-of-script.py
```

## Data and output

- `data/raw/`: original files
- `data/processed/`: transformed files
- `output/`: generated results
````

Za Windows PowerShell navedite ločena ukaza:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### 5. Dodajte neposredne zahteve

Primer `requirements.txt`:

```text
pandas
classla
```

Med razvojem raje vzdržujte kratek pregledani seznam neposrednih zahtev. `python -m pip freeze` lahko zabeleži celotno trenutno okolje za diagnozo ali preizkušen posnetek, vendar izpis preglejte, preden ga obravnavate kot objavno datoteko odvisnosti.

## Rezultat

Projektna mapa, v kateri lahko druga oseba najde vir, skripto, rezultat, navodila in omejitve ter obnovi okolje brez vaše `.venv/`.

## Preverite se

- Ali je izvirni vhod ločen od obdelanega?
- Ali README pojasni vprašanje, pravice, namestitev in zagon?
- Ali je `.venv/` izključena iz Gita?
- Ali so majhni pregledni rezultati sledljivi do skripte?
- Ali absolutne poti in osebni podatki niso po pomoti zapisani v projektu?

## Pogoste pasti

- izvirne podatke urejate neposredno;
- skripte poimenujete `final_final_really_final.py`;
- rezultate pomešate z vhodom;
- `.venv/` ali krajevni predpomnilnik modela vključite v Git;
- surovi `freeze` brez pregleda razglasite za univerzalno specifikacijo;
- licenco ali etično omejitev obravnavate kot tehnično podrobnost.

## Naloga

Zgradbo uporabite za tri kratka, dovoljena besedila. V README zapišite:

- raziskovalno vprašanje;
- izvor in pravice;
- različico Pythona;
- prvo skripto za zagon;
- mesto nastanka rezultata;
- eno omejitev interpretacije.

## Razširitev

Ko postopek vsebuje več ponavljajočih se ukazov, dodajte `Makefile` ali majhno zagonsko skripto. Avtomatizacije ne dodajte, preden razumete ročne korake.

## Preverjeni viri

Dostopano **23. julija 2026**:

- [Python 3.12: `venv`](https://docs.python.org/3.12/library/venv.html)
- [Python Packaging User Guide: nameščanje paketov](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [Git: `.gitignore`](https://git-scm.com/docs/gitignore)

Ukaze za zgradbo map in vedenje `.gitignore` smo preizkusili v zavržljivih mapah PowerShella in Basha; okolje Python smo znova izdelali s Pythonom 3.12.3 v Ubuntuju 24.04 pod WSL 2.
