---
title: "Kako diagnosticiram težave s Pythonom, venv in pipom?"
description: "Pred spreminjanjem kode diagnosticirajte običajne začetniške težave z okoljem Python."
category: "NLP"
difficulty: "začetno"
time: "15–45 min"
tags: [Python, venv, pip, diagnosticiranje, začetniki]
---

# Kako diagnosticiram težave s Pythonom, venv in pipom?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>začetno</span>
<span>15–45 min</span>
</div>

## Kaj želite doseči

Številne začetniške napake niso napake algoritma, temveč napačen tolmač, neaktivno okolje, pip drugega Pythona, napačna delovna mapa, manjkajoč paket ali napačna pot do skripte. Pred popravljanjem kode zberite dokaze o okolju.

!!! quote "V enem stavku"
    Preverite različico Pythona, aktiviranje, trenutni imenik, mesto paketa in celotno napako, preden spreminjate kodo.

## Kaj potrebujete

- terminal in projektno mapo;
- preizkušeno predmetno izhodišče Python 3.12;
- celotno sporočilo o napaki brez žetonov ali zasebnih podatkov.

## Postopek

### 1. Preverite različico Pythona

```bash
python --version
```

V predmetnem okolju pričakujete:

```text
Python 3.12.x
```

Če različica ni 3.12, ste zunaj preizkušenega predmetnega izhodišča. To ne pomeni, da je druga različica sama po sebi neuporabna; za ponovitev te poti ustvarite okolje z 3.12.

### 2. Preverite aktiviranje in pip

Poziv pogosto vsebuje `(.venv)`, vendar se ne zanašajte samo nanj:

```bash
python -m pip --version
python -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
```

Pot do pipa in tolmača naj vsebujeta `.venv`, zadnja vrednost pa naj bo `True`.

### 3. Preverite trenutno mapo

=== "Windows PowerShell"

    ```powershell
    Get-Location
    Get-ChildItem
    ```

=== "Bash (macOS/Linux/WSL)"

    ```bash
    pwd
    ls
    ```

Morali bi biti v korenu projekta, kjer so `data/`, `scripts/`, `output/` in `requirements.txt`.

### 4. Preverite, ali skripta obstaja

=== "Windows PowerShell"

    ```powershell
    Get-ChildItem scripts
    ```

=== "Bash (macOS/Linux/WSL)"

    ```bash
    ls scripts
    ```

Če datoteke ni na izpisani poti, je ukaz ne more zagnati. Ne ustvarite nove datoteke samo zato, da bi utišali napako; preverite navodila in črkovanje.

### 5. Preverite paket z aktivnim tolmačem

Za pandas:

```bash
python -c "import pandas; print(pandas.__version__)"
```

Za CLASSLA:

```bash
python -c "import classla; print('CLASSLA import OK')"
```

Če uvoz ne uspe in je okolje pravo, namestite pregledano zahtevo:

```bash
python -m pip install -r requirements.txt
```

Posameznega paketa ne nameščajte na slepo, če projekt že ima datoteko z zahtevami.

### 6. Uporabite diagnostično skripto

Ustvarite `scripts/check_environment.py`:

```python
import sys
from pathlib import Path

print("Python version:", sys.version)
print("Python executable:", sys.executable)
print("Current folder:", Path.cwd())
print("Inside virtual environment:", sys.prefix != sys.base_prefix)
```

Zaženite jo iz projektnega korena:

```bash
python scripts/check_environment.py
```

Pred objavo izpisa odstranite občutljivo uporabniško ime ali zasebno absolutno pot.

### 7. Zgradite drugo okolje ob starem

Če je `.venv/` nejasna, je sprva ne izbrišite. Ob njej ustvarite drugo zavržljivo okolje; tako ohranite dokaz in se izognete rekurzivnemu brisanju kot začetniški bližnjici.

=== "Windows PowerShell"

    ```powershell
    py -3.12 -m venv .venv-rebuilt
    .\.venv-rebuilt\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    ```

=== "Bash (macOS/Linux/WSL)"

    ```bash
    python3.12 -m venv .venv-rebuilt
    source .venv-rebuilt/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    ```

Med diagnosticiranjem dodajte `.venv*/` v `.gitignore`. Če novo okolje deluje, ga deaktivirajte. Staro okolje odstranite šele po preverjanju natančne projektne poti in potrditvi, da ne vsebuje projektne kode. Virtualna okolja so zavržljiva, brisanje pa je še vedno uničujoče.

## Rezultat

Utemeljena diagnoza: napačen tolmač, neaktivno okolje, napačen pip, napačna mapa, manjkajoča skripta, manjkajoča zahteva ali prava napaka v kodi.

## Preverite se

- Ali `python --version` pokaže predmetni 3.12?
- Ali pot do pipa kaže v aktivno okolje?
- Ali ste ukaz zagnali iz projektnega korena?
- Ali skripta obstaja na zapisani poti?
- Ali ste ohranili celotno sled napake?
- Ali ste novo okolje preizkusili, preden ste odstranili staro?

## Pogoste pasti

- po spletu iščete samo zadnjo vrstico napake;
- paket namestite z enim Pythonom in kodo zaženete z drugim;
- aktivirate napačno od več okolij;
- težavo pripišete CLASSLA, čeprav je napačna pot;
- uporabljate `sudo pip` ali trajno spreminjate pravilnik izvajanja;
- `.venv/` rekurzivno izbrišete, preden preverite pot in vsebino;
- v poročilo prilepite žeton ali občutljivo absolutno pot.

## Naloga

V zavržljivem projektu okolje deaktivirajte in poskusite uvoz:

```bash
deactivate
python -c "import pandas"
```

Nato aktivirajte pravo okolje in poskusite znova. Zabeležite oba izida ter pojasnite, kateri tolmač in mesto paketa sta povzročila razliko. Če `pandas` obstaja tudi globalno, uporabite `sys.executable` in poti do pipa namesto domneve.

## Hitra razpredelnica

| Napaka ali znak | Verjetni vzrok | Prvi varen pregled |
| --- | --- | --- |
| `ModuleNotFoundError` | Paket ni v aktivnem okolju | `python -m pip --version` in pregled `requirements.txt` |
| Različica ni Python 3.12 | Zunaj predmetnega izhodišča | Preverite tolmač in ustvarite ločeno okolje 3.12 |
| `No such file or directory` | Napačna mapa ali pot | `pwd`/`Get-Location` in `ls`/`Get-ChildItem` |
| Izhod je drugje | Druga delovna mapa | Izpišite `Path.cwd()` |
| PowerShell blokira aktiviranje | Pravilnik izvajanja | Preglejte `Get-ExecutionPolicy -List`; po dovoljenju uporabite samo `-Scope Process` |

## Preverjeni viri

Dostopano **23. julija 2026**:

- [Python 3.12: `venv`](https://docs.python.org/3.12/library/venv.html)
- [Python Packaging User Guide: nameščanje paketov](https://packaging.python.org/en/latest/tutorials/installing-packages/)

Diagnostično zaporedje in vzporedno ponovno izdelavo smo preizkusili v zavržljivem projektu Python 3.12 v Ubuntuju 24.04 pod WSL 2. Ukaze PowerShell smo skladenjsko preverili v zavržljivi mapi Windows; trajnega pravilnika izvajanja nismo spreminjali in okolja nismo rekurzivno izbrisali.
