---
title: "Kako namestim Python 3.12 za delo z NLP?"
description: "Namestite in preverite Python 3.12 kot preizkušeno izhodišče začetnih postopkov NLP."
category: "NLP"
difficulty: "začetno"
time: "20–40 min"
tags: [Python, Python 3.12, namestitev, NLP, začetniki]
---

# Kako namestim Python 3.12 za delo z NLP?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>začetno</span>
<span>20–40 min</span>
</div>

## Kaj želite doseči

Za manjše projekte NLP potrebujete predvidljivo namestitev Pythona. Na tej poti uporabljajte **Python 3.12.x** kot preizkušeno predmetno izhodišče.

To je odločitev zaradi ponovljivosti in ne trditev, da so novejše različice Pythona same po sebi neuporabne. Druge različice lahko delujejo, vendar so repozitorij, primeri in predmetna preverjanja usmerjeni v 3.12. Python 3.12 je zdaj v obdobju zgolj varnostnih popravkov, zato naj izvajalci izhodišče preverijo pred vsakim semestrom.

!!! quote "V enem stavku"
    Namestite Python 3.12, preverite, kateri ukaz ga zažene, in šele nato za vsak projekt ustvarite ločeno virtualno okolje.

## Kaj potrebujete

- računalnik, na katerem smete namestiti programsko opremo;
- PowerShell v izvornem sistemu Windows ali Bash v WSL/macOS/Linux;
- projektno mapo za varno vajo;
- pomoč informatika, če napravo upravlja ustanova.

## Različni ukazi niso sopomenke

| Ukaz | Običajni pomen |
| --- | --- |
| `py -3.12` | V sistemu Windows izrecno izbere Python 3.12 prek upravljalnika namestitev ali starejšega zaganjalnika. |
| `python3.12` | V podprtih okoljih macOS/Linux/WSL izrecno izbere Python 3.12. |
| `python3` | Izbere privzeti Python 3 distribucije, ki ni nujno 3.12. |
| `python` | Zunaj virtualnega okolja lahko izbere drug tolmač; po aktiviranju naj kaže na tolmač v `.venv/`. |

## Postopek

### 1. Namestite Python 3.12

=== "Windows"

    1. Z uradne strani [Python downloads](https://www.python.org/downloads/) ali iz trgovine Microsoft Store pridobite trenutni **Python install manager** in sledite [uradnim navodilom za Windows](https://docs.python.org/3/using/windows.html).
    2. V novem oknu PowerShell preglejte dostopno izvajalno okolje 3.12:

        ```powershell
        py list --online 3.12
        ```

    3. Namestite izbrano različico 3.12:

        ```powershell
        py install 3.12
        ```

    4. Starejši podpisani namestitveni program 3.12.10 ostaja na [uradni strani izdaje 3.12.10](https://www.python.org/downloads/release/python-31210/) za upravljana okolja, ki še ne uporabljajo upravljalnika. O poti se posvetujte z informatiki.

=== "macOS"

    Uporabite podpisani namestitveni program universal2 z uradne [strani izdaje Python 3.12.10](https://www.python.org/downloads/release/python-31210/). To je zadnja izdaja 3.12 z binarnimi namestitvenimi programi; poznejše varnostne izdaje 3.12 so samo izvorne. Po namestitvi odprite novo okno Terminala.

    Če ustanova Python že upravlja s Homebrew, je platformna možnost:

    ```bash
    brew install python@3.12
    ```

    Zabeležite ponudnika. Drugega upravljalnika paketov ne nameščajte samo zaradi teh navodil.

=== "Ubuntu / WSL"

    Uporabite vzdrževane pakete distribucije. Ubuntu 24.04, ki je preizkušeno okolje repozitorija, vsebuje Python 3.12:

    ```bash
    sudo apt update
    sudo apt install python3.12 python3.12-venv
    ```

    To sta namestitvena ukaza operacijskega sistema za okolje Ubuntu, ki ga smete upravljati, ne splošna rešitev za dovoljenja. V preizkušenih repozitorijih Ubuntu 24.04 ni paketa `python3.12-pip`; `python3.12-venv` pip pripravi znotraj vsakega novega okolja. Pri drugih distribucijah uporabite njihovo uradno dokumentacijo.

### 2. Preverite različico in pot

=== "Windows PowerShell"

    ```powershell
    py -3.12 --version
    py list
    ```

    Prvi ukaz naj izpiše `Python 3.12.x`. Drugi pokaže izvajalna okolja, ki jih pozna trenutni upravljalnik Python. Starejši zaganjalniki poznajo tudi `py -0p`.

=== "Bash (macOS/Linux/WSL)"

    ```bash
    python3.12 --version
    command -v python3.12
    ```

    Različica naj se začne s `Python 3.12`, drugi ukaz pa naj izpiše pot do izvedljive datoteke.

### 3. Ustvarite projektno mapo

=== "Windows PowerShell"

    ```powershell
    New-Item -ItemType Directory -Name nlp-first-steps
    Set-Location nlp-first-steps
    ```

=== "Bash (macOS/Linux/WSL)"

    ```bash
    mkdir nlp-first-steps
    cd nlp-first-steps
    ```

V tej mapi bodo pozneje virtualno okolje, skripte, vhodni podatki in rezultati.

### 4. Paketov NLP še ne nameščajte

Na tej stopnji samo potrdite, da Python 3.12 obstaja. Pakete boste namestili pozneje, v virtualnem okolju. Ne uporabljajte globalnega ali `sudo pip` kot bližnjice.

## Rezultat

Delujoč Python 3.12 in čista projektna mapa, pripravljena za virtualno okolje.

## Preverite se

- Ali `py -3.12 --version` oziroma `python3.12 --version` pokaže 3.12?
- Ali po odprtju novega terminala dobite isti rezultat?
- Ali veste, kateri ukaz na vašem računalniku izrecno izbere 3.12?
- Ali delate v projektni in ne v sistemski mapi?

## Pogoste pasti

- predmetno izhodišče 3.12 razlagate kot dokaz, da vse novejše različice ne delujejo;
- pakete namestite globalno pred ustvarjanjem virtualnega okolja;
- imate več različic, vendar ne preverite izbranega tolmača;
- ukaze PowerShella kopirate v Bash ali obratno;
- pri težavi z okoljem uporabite `sudo` ali globalni pip;
- po namestitvi ne odprete novega terminala.

## Naloga

Ustvarite `nlp-first-steps/` in v `README.md` zapišite:

```markdown
# NLP first steps

Course baseline: Python 3.12.x
Python command on this computer: python3.12
Exact version checked: …
```

Ukaz prilagodite svoji platformi.

## Preverjeni viri

Dostopano **23. julija 2026**:

- [prenosi Python in stanje aktivnih izdaj](https://www.python.org/downloads/)
- [izdaja Python 3.12.10 in podpisani namestitveni programi](https://www.python.org/downloads/release/python-31210/)
- [uporaba Pythona v sistemu Windows](https://docs.python.org/3/using/windows.html)
- [uporaba Pythona v macOS](https://docs.python.org/3.12/using/mac.html)
- [dokumentacija Python 3.12 za `venv`](https://docs.python.org/3.12/library/venv.html)

Pot Linux/WSL smo preizkusili v Ubuntuju 24.04.4 LTS z vzdrževanim paketom Python 3.12.3. Izvorni poti za Windows in macOS smo preverili po uradnih virih, na preglednem gostitelju WSL pa ju nismo izvedli.
