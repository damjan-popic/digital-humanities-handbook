---
title: "Kako zaženem skripto Python iz terminala?"
description: "Napišite in zaženite prvo skripto Python v predvidljivi projektni mapi."
category: "NLP"
difficulty: "začetno"
time: "20–40 min"
tags: [Python, terminal, skripte, začetniki]
---

# Kako zaženem skripto Python iz terminala?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>začetno</span>
<span>20–40 min</span>
</div>

## Kaj želite doseči

Ponovljivi postopki NLP so pogosto skripte in ne zaporedja klikov. Skripta je datoteka `.py`, ki jo lahko znova zaženete z istim vhodom, nastavitvami in lokacijo izhoda.

Vaš cilj je omejen: ustvarite eno skripto, zaženite jo iz korena projekta in preverite eno izhodno datoteko. Uspešen zagon še ne potrdi interpretacije.

!!! quote "V enem stavku"
    Kodo shranite v `scripts/`, zaženite jo iz korena projekta in prepustite skripti, da ustvari izhod.

## Kaj potrebujete

- Python 3.12 in aktivirano virtualno okolje;
- urejevalnik navadnega besedila oziroma kode;
- zavržljivo projektno mapo.

## Postopek

### 1. Ustvarite osnovno zgradbo

```text
nlp-first-steps/
├── data/
├── output/
└── scripts/
```

=== "Windows PowerShell"

    ```powershell
    New-Item -ItemType Directory -Path data, output, scripts
    ```

=== "Bash (macOS/Linux/WSL)"

    ```bash
    mkdir -p data output scripts
    ```

### 2. Ustvarite skripto

V urejevalniku ustvarite `scripts/hello.py`:

```python
from pathlib import Path
import sys

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

message = "Hello from a reproducible Python script."
run_info = f"{message}\nPython: {sys.version}\n"

print(message)
(output_dir / "hello.txt").write_text(run_info, encoding="utf-8")
```

`Path("output")` je relativna pot. Pomeni mapo `output/` glede na trenutno delovno mapo, ne nujno glede na mesto skripte.

### 3. Preverite projektni koren

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

Videti morate `data/`, `output/` in `scripts/`. Ne vstopite v `scripts/`.

### 4. Zaženite skripto

V aktiviranem okolju:

```bash
python scripts/hello.py
```

Ukaz uporablja `python` iz `.venv/` in relativne poti iz projektnega korena.

### 5. Preglejte izhod

=== "Windows PowerShell"

    ```powershell
    Get-Content output\hello.txt
    ```

=== "Bash (macOS/Linux/WSL)"

    ```bash
    cat output/hello.txt
    ```

Datoteka mora vsebovati sporočilo in različico Pythona.

### 6. Preverite ponovljivost izhoda

V zavržljivi mapi `output/` datoteko `hello.txt` odstranite z upravljalnikom datotek, preverite, da ne gre za nenadomestljiv rezultat, nato znova zaženite:

```bash
python scripts/hello.py
```

Skripta mora izhod znova ustvariti. Vhodnih raziskovalnih datotek pri tej vaji ne brišite.

## Rezultat

Delujoča skripta in `output/hello.txt`, ustvarjen s preverjenim ukazom.

## Preverite se

- Ali ste skripto zagnali iz korena projekta?
- Ali je rezultat ustvarila skripta in ne ročno urejanje?
- Ali izhod vsebuje različico Pythona?
- Ali lahko izhod znova ustvarite?
- Ali sta skripta in rezultat kodirana v UTF-8?

## Pogoste pasti

- skripto zaženete iz napačne mape in spremenite pomen relativnih poti;
- datoteko shranite kot `hello.py.txt`;
- urejate eno kopijo in zaženete drugo;
- rezultat ustvarite ročno;
- pred zagonom ne aktivirate `.venv`;
- uspešen zagon zamenjate z vsebinsko veljavnostjo.

## Naloga

Skripto dopolnite tako, da v `output/run-info.txt` zapiše:

- vaše začetnice ali neosebno projektno oznako;
- današnji datum;
- različico Pythona;
- trenutno delovno mapo.

Pred potrditvijo preverite, da absolutna pot ne razkriva občutljivega uporabniškega imena.

## Uporabna diagnostika

```python
from pathlib import Path
print("Current folder:", Path.cwd())
```

Izvorno besedilo hranite v UTF-8, za nenadomestljiv vhod pa imejte ločeno varnostno kopijo. Uspešen zagon pokaže, da so se navodila izvedla; ne podeli pravic do razširjanja vhoda ali izhoda.

## Preverjeni viri

Dostopano **23. julija 2026**:

- [Python 3.12: uporaba tolmača](https://docs.python.org/3.12/tutorial/interpreter.html)
- [Python 3.12: `pathlib`](https://docs.python.org/3.12/library/pathlib.html)

Skripto in ponovno izdelavo izhoda smo preizkusili iz zavržljivega projektnega korena s Pythonom 3.12.3 v Ubuntuju 24.04 pod WSL 2.
