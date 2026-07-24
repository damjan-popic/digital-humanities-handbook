---
title: "Kako namestim in nastavim Git?"
description: "Git namestite po uradni poti za svojo platformo in premišljeno nastavite identiteto za potrditve."
category_id: "foundations"
category: "Osnove"
difficulty: "začetno"
time: "20–40 min"
tags: [Git, nadzor različic, identiteta, namestitev]
---

# Kako namestim in nastavim Git?

<div class="answer-meta" markdown>
<span>Osnove</span>
<span>začetno</span>
<span>20–40 min</span>
</div>

## Kaj želite doseči

Raziskovalni projekt potrebuje sledljiv zapis o tem, kdo je opravil spremembo in kdaj. Git boste namestili v okolje, v katerem delate, ga preverili ter nastavili ime in e-poštni naslov, ki se bosta zapisovala v prihodnje potrditve.

Git beleži krajevno zgodovino. GitHub je ločena storitev za gostovanje; pri tem postopku ne potrebujete računa GitHub ali javnega repozitorija.

## Kaj potrebujete

- dovoljenje za nameščanje programske opreme ali podporo ustanove;
- lupino, v kateri boste opravljali projektno delo;
- pravilo o imenu in e-poštnem naslovu, primerno za akademsko delo.

Če pri predmetu uporabljate WSL, Git namestite in nastavite **v Ubuntuju**, tudi če že imate Git for Windows. Gre za ločeni namestitvi z ločenimi nastavitvenimi datotekami.

## Postopek

### 1. Pred namestitvijo preverite stanje

V projektni lupini zaženite:

```bash
git --version
```

Če se izpiše različica, nadaljujte z nastavitvijo. Programa ne nameščajte znova samo zato, da bi se različica ujemala s sliko v navodilih.

### 2. Izberite pot za svojo platformo

=== "Ubuntu / WSL"

    Ukaza izvedite samo, če `git --version` sporoči, da Git manjka, in sami upravljate to okolje Ubuntu:

    ```bash
    sudo apt update
    sudo apt install git
    ```

    To sta namestitvena ukaza operacijskega sistema. `sudo` pri tem natančno določenem opravilu podeli skrbniške pravice; ni rešitev za poznejše Gitove napake pri dovoljenjih. Na upravljani napravi brez dovoljenja prosite informatike, naj namestijo paket distribucije.

=== "Windows (izvorno)"

    Uporabite vzdrževani namestitveni program **Git for Windows**, ki je povezan z uradne strani Git, ali trenutno pot WinGet z iste strani.

    **PowerShell:**

    ```powershell
    winget install --id Git.Git -e --source winget
    ```

    Po namestitvi odprite nov terminal. Ta izvorna namestitev je ločena od Gita v WSL.

=== "macOS"

    Uradna stran za namestitev Gita navaja Applova orodja ukazne vrstice:

    ```bash
    xcode-select --install
    ```

    Navaja tudi Homebrew, če ga vaša ustanova že podpira:

    ```bash
    brew install git
    ```

    Drugega upravljalnika paketov ne nameščajte samo zato, da bi se izognili zahtevku ustanovi.

### 3. Preverite namestitev

Odprite novo lupino in zaženite:

```bash
git --version
```

Zabeležite natančni izpis. Pri projektih navadno ni potrebno, da imajo vsi študenti isto različico popravka Gita.

### 4. Nastavite identiteto za potrditve

Primera zamenjajte z identiteto, ki jo želite objaviti v metapodatkih potrditev:

```bash
git config --global user.name "Vaše ime"
git config --global user.email "vi@example.edu"
git config --global init.defaultBranch main
```

`--global` zapiše uporabniške nastavitve za repozitorije tega računa operacijskega sistema. S tem ne ustvarite spletnega profila.

V vsako potrditev se zapišeta nastavljeno ime in e-poštni naslov. Če bo repozitorij postal javen, se odločite, ali je primeren naslov ustanove, drug poklicni naslov ali naslov za varovanje zasebnosti, ki ga ponuja gostitelj. Ne izmišljajte si identitete druge osebe. Če se identiteti za ocenjevanje in objavo razlikujeta, vprašajte izvajalko ali izvajalca predmeta.

### 5. Preglejte vrednosti in njihov izvor

```bash
git config --list --show-origin
git config user.name
git config user.email
git config init.defaultBranch
```

`--show-origin` pokaže, iz katere nastavitvene datoteke prihaja vrednost. To je pomembno, kadar se sistemske, uporabniške in repozitorijske nastavitve razlikujejo.

### 6. Po potrebi uporabite repozitorijsko nastavitev

Če v obstoječem repozitoriju izpustite `--global`, zapišete krajevno vrednost:

```bash
git config user.email "course-address@example.edu"
git config --show-origin user.email
```

Krajevne vrednosti v `.git/config` za ta repozitorij preglasijo globalne. Uporabite resnični odobreni naslov; kadar je identiteta metodološko ali institucionalno pomembna, preglasitev pojasnite v projektni dokumentaciji.

## Rezultat

- delujoč ukaz `git`;
- premišljeno izbrana ime in e-poštni naslov za potrditve;
- `main` kot začetna veja novih repozitorijev;
- pregleden zapis o izvoru nastavitev.

## Preverite se

```bash
git --version
git config --list --show-origin
```

Izpis preberite. V javno poročilo ne prilepite dostopnih žetonov, skrivnosti upravljalnika poverilnic ali nepovezanih zasebnih poti.

## Pogoste pasti

- nastavite Git for Windows, vse delo pa opravljate v Ubuntuju pod WSL;
- dobesedno prekopirate nadomestno ime ali e-poštni naslov;
- v projektu uporabljate `sudo git ...` in ustvarite datoteke v lasti uporabnika `root`;
- domnevate, da je Gitova identiteta overjen dokaz avtorstva;
- v repozitoriju, ki bo javen, razkrijete zasebni e-poštni naslov;
- spremenite sistemske nastavitve, čeprav bi zadoščala globalna ali krajevna nastavitev.

## Naloga

V `environment-check.md` zabeležite:

```text
Različica Git:
Okolje izvedljive datoteke Git: WSL Ubuntu / izvorni Windows / macOS / Linux
Ime za potrditve preverjeno:
Zasebnost e-poštnega naslova preverjena: da
Privzeta začetna veja: main
```

E-poštnega naslova ne prekopirajte v dokument, ki bo objavljen, razen če je objava namerna.

## Preverjeni viri

Dostopano **23. julija 2026**:

- [Git: namestitev](https://git-scm.com/install/)
- [Git za Windows](https://git-scm.com/install/windows)
- [Git za macOS](https://git-scm.com/install/mac)
- [Git za Linux](https://git-scm.com/install/linux)
- [Pro Git: prva nastavitev Gita](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

Preverjanje v Ubuntuju in nastavitvene ukaze smo preizkusili z Gitom 2.43 v zavržljivih uporabniških nastavitvah in repozitoriju. Izvorni poti za namestitev v Windows in macOS smo preverili po uradnih straneh, na preglednem gostitelju WSL pa ju nismo izvedli.
