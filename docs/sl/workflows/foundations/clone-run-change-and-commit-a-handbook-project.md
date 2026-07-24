---
title: "Kako kloniram, zaženem, spremenim in potrdim projekt priročnika?"
description: "Povežite Git in Python v majhnem repozitoriju pripravljenosti, ki ga zagotovi izvajalec predmeta."
category_id: "foundations"
category: "Osnove"
difficulty: "začetno"
time: "45–75 min"
tags: [Git, Python, venv, kloniranje, pripravljenost]
---

# Kako kloniram, zaženem, spremenim in potrdim projekt priročnika?

<div class="answer-meta" markdown>
<span>Osnove</span>
<span>začetno</span>
<span>45–75 min</span>
</div>

## Kaj želite doseči

Dokazati želite, da lahko manjši humanistični izračun prenesete iz dokumentiranega repozitorija do uspešnega krajevnega zagona in pregledne spremembe. Postopek poveže že pridobljene spretnosti; ne uvaja javnega prispevanja.

Uporabite URL majhnega začetnega repozitorija ali pot ustanove, ki vam jo posreduje izvajalka oziroma izvajalec predmeta. Javni repozitorij GitHub ni potreben. Pred odprtjem zahtevka za vključitev se ustavite, razen če vam izvajalec izrecno naroči drugače.

## Pogodba začetnega projekta

Posredovani repozitorij naj vsebuje vsaj:

```text
technical-readiness/
├── README.md
├── environment-check.md
├── hello.py
├── requirements.txt
└── output/
```

Licenca naj bo zapisana v `LICENSE` ali jasno navedena v `README.md`, `.venv/` pa naj bo prezrta. Skripta naj vsebuje eno neškodljivo oznako, ki jo po navodilu README lahko spremenite.

## Postopek

### 1. Klonirajte, ne inicializirajte

Celotno nadomestilo zamenjajte z naslovom HTTPS ali odobreno krajevno potjo, ki jo posreduje izvajalec.

**Bash:**

```bash
cd ~/projects
git clone "<starter-repository-url>" technical-readiness
cd technical-readiness
```

**PowerShell (izvorni projekt Windows):**

```powershell
Set-Location "$HOME\Projects"
git clone "<starter-repository-url>" technical-readiness
Set-Location technical-readiness
```

V kloniranem repozitoriju ne zaženite `git init`. `git clone` je že ustvaril krajevni repozitorij in njegov izvor zabeležil kot oddaljeni naslov.

### 2. Pred izvajanjem preglejte

```bash
git status
git remote -v
ls -la
less README.md
```

Preglejte licenčno datoteko, ki jo navaja README, na primer:

```bash
less LICENSE
```

Za izhod iz `less` pritisnite `q`. Licenca opisuje dovoljenja in pogoje; ne razveljavi zasebnosti, varstva podatkov, soglasja ali pravic tretjih oseb.

Pred zagonom preberite `hello.py` in `requirements.txt`:

```bash
cat hello.py
cat requirements.txt
```

Če sta izvor repozitorija ali odvisnosti nepričakovana, se ustavite in vprašajte izvajalko ali izvajalca.

### 3. Preverite, da je `.venv/` prezrta

```bash
git check-ignore -v .venv/
```

Če ukaz ne pokaže pravila, dodajte `.venv/` v `.gitignore` in spremembo pred nadaljevanjem preglejte. `.venv/` nikoli ne vključite v Git.

### 4. Ustvarite preizkušeno predmetno okolje

=== "Bash (WSL/macOS/Linux)"

    ```bash
    python3.12 -m venv .venv
    source .venv/bin/activate
    ```

=== "Windows PowerShell"

    ```powershell
    py -3.12 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

Če PowerShell blokira aktivacijsko skripto, uporabite diagnostiko za trenutno sejo iz [postopka za virtualno okolje](../nlp/create-a-python-312-virtual-environment.md). Varoval pravil izvajanja ne izklopite trajno.

### 5. Preverite in namestite navedene zahteve

```bash
python --version
python -m pip --version
python -m pip install -r requirements.txt
```

Različica Pythona se mora začeti s `3.12`, pot do pipa pa mora biti znotraj `.venv`. Nameščanje paketov uporablja omrežje in izvaja namestitvena orodja; uporabite samo pregledano predmetno datoteko.

### 6. Zaženite nespremenjeno skripto

```bash
python hello.py
```

Preglejte dokumentirani izhod:

```bash
ls -la output
```

Uspešni ukaz in lokacijo izhoda zabeležite v `environment-check.md`.

### 7. Ustvarite vejo in spremenite neškodljivo vrednost

```bash
git switch -c readiness-practice
git status
```

`hello.py` odprite v urejevalniku navadnega besedila. Spremenite samo oznako, določeno v README, na primer projektno oznako `technical readiness` nadomestite s kratko oznako predmeta. Ne spreminjajte izvornih podatkov, poti, različic paketov ali licenčnega besedila.

Zaženite in preglejte:

```bash
python hello.py
git diff -- hello.py
git status
```

Razlika naj vsebuje samo nameravano spremembo oznake.

### 8. Dopolnite zapis o okolju

V `environment-check.md` zabeležite:

```text
Operacijski sistem:
Lupina:
Različica Git:
Različica Python:
Ukaz za aktiviranje:
Uspešni ukaz za skripto:
Izhod preverjen:
```

Ne zapisujte uporabniških imen, žetonov, gesel ali občutljivih absolutnih poti. Spremembo preglejte:

```bash
git diff -- environment-check.md
```

### 9. Pripravite in krajevno potrdite

```bash
git add hello.py environment-check.md
git diff --staged
git commit -m "Complete the technical-readiness run"
git status
git log --oneline --decorate --max-count=3
```

Če se `.venv/` v `git status` pojavi kot pripravljena ali sledena, se ustavite in pred potrditvijo popravite `.gitignore`.

### 10. Ustavite se pred javnim prispevanjem

Ne zaženite `git push`, ne ustvarite javne izpeljanke in ne odprite zahtevka za vključitev, razen če je izvajalka ali izvajalec izrecno opredelil naslednjo dejavnost ter njene pogoje zasebnosti in licenciranja. Pripravljenost lahko pregledate krajevno ali oddate po odobrenem sistemu ustanove.

Okolje deaktivirajte:

```bash
deactivate
```

## Rezultat

- zahtevani izdelek `technical-readiness/`;
- znova ustvarjena `.venv/`, izključena iz Gita;
- en uspešen izhod skripte;
- ena veja in krajevna potrditev, ki vsebujeta samo neškodljivo oznako ter zapis o okolju.

## Preverite se

```bash
git status
git log --oneline --decorate --all
git ls-files .venv
```

`git ls-files .venv` ne sme izpisati ničesar.

## Pogoste pasti

| Znak | Varen naslednji korak |
| --- | --- |
| Kloniranje nepričakovano zahteva poverilnice | Preverite natančni naslov izvajalca; žetona ne prilepite v klepet ali zgodovino lupine. |
| README ali licenca manjka | Ustavite se in zahtevajte popoln začetni projekt; dovoljenja za ponovno uporabo ne ugibajte. |
| Python ni različice 3.12 | Okolje deaktivirajte in `.venv/` znova ustvarite z ukazom 3.12 za svojo platformo. |
| Namestitev paketa ne uspe | Ohranite celotno napako, različici Pythona in pipa ter platformo; ne uporabite `sudo pip`. |
| Skripta piše zunaj `output/` | Ustavite se, preglejte kodo in pred ponovnim zagonom sporočite neskladje. |
| Razlika vsebuje veliko datotek ali spremembe koncev vrstic | Ničesar ne pripravite; preverite kodiranje in nastavitve koncev vrstic v urejevalniku. |

## Preverjeni viri

Dostopano **23. julija 2026**:

- [Pro Git: pridobitev repozitorija Git](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
- [dokumentacija Python 3.12 za `venv`](https://docs.python.org/3.12/library/venv.html)
- [Python Packaging User Guide: nameščanje paketov](https://packaging.python.org/en/latest/tutorials/installing-packages/)

Povezano zaporedje kloniranja, veje, virtualnega okolja, namestitve, zagona in potrditve smo preizkusili z zavržljivim krajevnim začetnim projektom in golim oddaljenim repozitorijem v Ubuntuju 24.04 pod WSL 2. Naslov izvajalca, izvorno aktiviranje v Windows in okolje macOS ostajajo odvisni od platforme oziroma predmeta; na tem gostitelju jih nismo izvedli.
