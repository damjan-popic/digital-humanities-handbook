---
title: "Kako ustvarim virtualno okolje Python 3.12?"
description: "Ustvarite in aktivirajte projektno omejeno virtualno okolje Python 3.12."
category: "NLP"
difficulty: "začetno"
time: "15–30 min"
tags: [Python, venv, virtualno okolje, namestitev, začetniki]
---

# Kako ustvarim virtualno okolje Python 3.12?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>začetno</span>
<span>15–30 min</span>
</div>

## Kaj želite doseči

Virtualno okolje je izoliran prostor Python za en projekt. Pakete loči od drugih projektov in sistemskega Pythona.

Na tej poti okolje ustvarite s **Pythonom 3.12**, ker je to preizkušeno predmetno izhodišče. To ne pomeni, da novejše različice ne morejo delovati. Po aktiviranju uporabljajte `python`, ki mora kazati na tolmač v `.venv/`.

!!! quote "V enem stavku"
    Vsak projekt dobi svojo `.venv/`; pred nameščanjem paketov ali zagonom skript jo aktivirajte.

## Kaj potrebujete

- nameščen Python 3.12;
- terminal in projektno mapo, na primer `nlp-first-steps`;
- `.gitignore`, ki vsebuje `.venv/`.

## Postopek

### 1. Vstopite v projektno mapo

=== "Windows PowerShell"

    ```powershell
    Set-Location nlp-first-steps
    ```

=== "Bash (macOS/Linux/WSL)"

    ```bash
    cd nlp-first-steps
    ```

Pred ustvarjanjem preverite lokacijo z `Get-Location` v PowerShellu ali `pwd` v Bashu.

### 2. Ustvarite okolje s Pythonom 3.12

=== "Windows PowerShell"

    ```powershell
    py -3.12 -m venv .venv
    ```

=== "Bash (macOS/Linux/WSL)"

    ```bash
    python3.12 -m venv .venv
    ```

Nastane mapa `.venv/`. Datotek v njej ne urejajte ročno, mape ne premikajte in je ne vključite v Git.

### 3. Aktivirajte okolje

=== "Windows PowerShell"

    ```powershell
    .\.venv\Scripts\Activate.ps1
    ```

    Če PowerShell skripto blokira, najprej preglejte pravilnike:

    ```powershell
    Get-ExecutionPolicy -List
    ```

    Na računalniku, ki ga upravljate sami, je najmanj trajen predmetni obhod omejen na trenutni proces:

    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    .\.venv\Scripts\Activate.ps1
    ```

    Nastavitev preneha veljati, ko zaprete ta proces PowerShell. Na računalniku ustanove se ustavite in prosite informatike; trajnih varnostnih pravil ne izklapljajte.

=== "Bash (macOS/Linux/WSL)"

    ```bash
    source .venv/bin/activate
    ```

### 4. Preverite aktivni tolmač in pip

```bash
python --version
python -m pip --version
```

Različica naj bo `Python 3.12.x`, pot do pipa pa naj vsebuje `.venv`.

Za dodatno preverjanje:

```bash
python -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
```

Druga vrstica naj izpiše `True`.

### 5. Preverite ali posodobite pip v okolju

```bash
python -m pip install --upgrade pip
```

Python 3.12 ne vključuje več `setuptools` kot temeljne odvisnosti venv. Orodja za gradnjo namestite samo, če jih zahteva pregledani projekt.

### 6. Okolje deaktivirajte

V PowerShellu ali Bashu:

```bash
deactivate
```

Isto okolje lahko pozneje znova aktivirate; ob vsakem delu ga ni treba znova ustvariti.

## Rezultat

Krajevna `.venv/`, v kateri `python --version` po aktiviranju pokaže Python 3.12.

## Preverite se

- Ali poziv vsebuje `(.venv)`?
- Ali `python -m pip --version` kaže v `.venv/`?
- Ali lahko okolje deaktivirate in znova aktivirate?
- Ali `git status` ne ponuja `.venv/` za potrditev?

## Specifikacija ni mapa

`.venv/` je strojno odvisna in zavržljiva. Ni specifikacija okolja. V Git vključite:

```text
README.md
requirements.txt
.gitignore
```

V README zapišite natančna ukaza za ustvarjanje in aktiviranje na podprti platformi.

## Pogoste pasti

- okolje ustvarite z napačnim tolmačem;
- pakete nameščate pred aktiviranjem;
- uporabite goli `pip` in ne `python -m pip`;
- `.venv/` vključite v Git;
- `.venv/` premaknete in pričakujete, da bo ostala prenosljiva;
- zaradi blokirane skripte trajno izklopite PowerShellov varnostni pravilnik.

## Naloga

V zavržljivi projektni mapi okolje ustvarite, aktivirajte, preverite in deaktivirajte. Natančne ukaze za svojo platformo zapišite v `environment-check.md`.

## Preverjeni viri

Dostopano **23. julija 2026**:

- [Python 3.12: `venv`](https://docs.python.org/3.12/library/venv.html)
- [Python Packaging User Guide: nameščanje paketov in ustvarjanje okolij](https://packaging.python.org/en/latest/tutorials/installing-packages/)

Ustvarjanje, aktiviranje v Bashu, deaktiviranje, preverjanje tolmača in ponovna izdelava so bili preizkušeni s Pythonom 3.12.3 v Ubuntuju 24.04 pod WSL 2. Ukaz za PowerShell izhaja iz dokumentacije Python 3.12 in je bil skladenjsko preverjen v Windows PowerShellu; izvornega Pythona za Windows nismo znova nameščali.
