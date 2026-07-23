---
title: "Kako namestim pakete Python s pipom?"
description: "Pakete namestite v virtualno okolje in odvisnosti premišljeno zabeležite v requirements.txt."
category: "NLP"
difficulty: "začetno"
time: "15–30 min"
tags: [Python, pip, paketi, requirements, začetniki]
---

# Kako namestim pakete Python s pipom?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>začetno</span>
<span>15–30 min</span>
</div>

## Kaj želite doseči

Paketi Python dodajo funkcije, kot so tabele, jezikoslovna anotacija ali vizualizacija. Namestite jih v aktivirano virtualno okolje, ne globalno. Z `python -m pip` zagotovite, da pip pripada istemu tolmaču, s katerim boste zagnali skripto.

!!! quote "V enem stavku"
    Aktivirajte `.venv`, namestite pregledane zahteve z `python -m pip`, preverite uvoz in zabeležite odvisnosti.

## Kaj potrebujete

- Python 3.12 in aktivirano `.venv`;
- terminal in internetno povezavo;
- ime paketa ali pregledani `requirements.txt`;
- pravico do prenosa paketa in podatkov, ki jih boste obdelovali.

## Postopek

### 1. Aktivirajte okolje

=== "Windows PowerShell"

    ```powershell
    .\.venv\Scripts\Activate.ps1
    ```

=== "Bash (macOS/Linux/WSL)"

    ```bash
    source .venv/bin/activate
    ```

### 2. Preverite Python in pip

```bash
python --version
python -m pip --version
```

Različica Pythona naj se začne s `3.12`, pot do pipa pa naj vsebuje `.venv`.

### 3. Namestite en manjši paket

```bash
python -m pip install pandas
```

Namestitev paketa pridobi in lahko izvede namestitveno kodo. Preverite pravilno ime paketa, njegov izvor, licenco in projektne zahteve; ne ugibajte imen podobnih paketov.

### 4. Preverite uvoz

```bash
python -c "import pandas as pd; print(pd.__version__)"
```

Če se izpiše različica, je paket dostopen aktivnemu tolmaču.

### 5. Ustvarite kratek seznam neposrednih zahtev

Za začetni projekt pripravite pregledani `requirements.txt`:

```text
pandas
classla
```

Vse zahteve namestite z:

```bash
python -m pip install -r requirements.txt
```

Datoteka je navodilo pipu, ne dokaz, da je projekt ponovljiv. Zabeležite tudi različico Pythona, platformo, vhod in ukaz za zagon.

### 6. Po potrebi zabeležite natančni posnetek

Za diagnozo ali posnetek trenutnega okolja:

```bash
python -m pip freeze > requirements.txt
```

Ukaz zabeleži vse nameščene distribucije, tudi posredne, platformno odvisne in poskusne. Rezultat pred potrditvijo preglejte. Surovi `freeze` je dokaz o enem okolju in ni samodejno idealna zaklepna datoteka za objavo na več platformah.

## Rezultat

Nameščen in preverjen paket ter `requirements.txt`, ki dokumentira projektne potrebe.

## Preverite se

- Ali je `.venv` aktivna?
- Ali `python -m pip --version` kaže vanjo?
- Ali uvoz izpiše različico paketa?
- Ali `requirements.txt` vsebuje samo nameravane zahteve?
- Ali drug uporabnik pozna tudi različico Pythona in ukaz za zagon?

## Pogoste pasti

- uporabite pip drugega tolmača;
- pakete namestite globalno ali z `sudo pip`;
- namestite napačno podobno ime iz javnega indeksa;
- delite kodo brez odvisnosti;
- nepregledan izpis `freeze` predstavite kot idealno večplatformno specifikacijo;
- paket namestite v enem terminalu, skripto pa zaženete v drugem neaktiviranem okolju.

## Naloga

V zavržljivem projektu:

1. ustvarite in aktivirajte `.venv`;
2. namestite `pandas`;
3. preverite uvoz;
4. napišite kratek `requirements.txt`;
5. v ločenem novem zavržljivem okolju znova namestite zahteve.

Za odstranjevanje okolja ne uporabljajte rekurzivnih ukazov na nepregledani poti. Najprej ga deaktivirajte, preverite projektno lokacijo in sledite postopku za diagnosticiranje.

## Del README

````markdown
## Namestitev

Uporabite Python 3.12.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```
````

Za Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Preverjeni viri

Dostopano **23. julija 2026**:

- [Python Packaging User Guide: nameščanje paketov](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [pip: oblika datotek z zahtevami](https://pip.pypa.io/en/stable/reference/requirements-file-format/)
- [pip: `pip freeze`](https://pip.pypa.io/en/stable/cli/pip_freeze/)

Namestitev, preverjanje uvoza in namestitev iz `requirements.txt` so bili preizkušeni v zavržljivem virtualnem okolju Python 3.12 v Ubuntuju 24.04 pod WSL 2. Globalnega ali `sudo pip` nismo uporabili.
