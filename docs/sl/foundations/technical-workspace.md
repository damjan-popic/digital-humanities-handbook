---
title: "Tehnično delovno okolje: terminal, WSL, Bash, Git in Python"
description: "Začetnikom prijazna pot od novega računalnika do dokumentiranega in ponovljivega humanističnega projekta."
---

# Tehnično delovno okolje: terminal, WSL, Bash, Git in Python

## Raziskovalni problem

Kako lahko druga raziskovalka ali raziskovalec ponovi računalniško pretvorbo, če uporablja drugačen računalnik, operacijski sistem ali različice paketov? Za ponovljiv projekt ni dovolj skripta: potrebujete pregledno delovno okolje, zgodovino sprememb in okolje, ki ga je mogoče znova ustvariti.

Na tej poti boste temelje zgradili z majhnim humanističnim projektom za vajo, ki ga lahko brez škode zavržete. Pojme bomo ločili od navodil za namestitev, da boste pred zagonom razumeli, kaj ukaz spremeni.

## Učni izidi

Po opravljeni poti boste znali:

- razlikovati med terminalom, lupino, ukazno vrstico, lupino Bash, PowerShellom, WSL in distribucijo Linuxa;
- uporabljati poti, ne da bi zamešali datotečna sistema Windows in Linux;
- pojasniti, kaj beleži Git in kako se razlikuje od GitHuba;
- ustvariti, aktivirati in znova ustvariti virtualno okolje Python 3.12;
- zabeležiti odvisnosti, ne da bi v Git vključili `.venv/`;
- odpraviti običajne napake in se ustaviti pred uničujočimi operacijami;
- izdelati krajevni izdelek preverjanja tehnične pripravljenosti, ki ga lahko pregleda izvajalka ali izvajalec predmeta.

## Kaj potrebujete vsi in kaj velja samo za Windows

| Vsi potrebujete | Če uporabljate Windows, dodatno potrebujete |
| --- | --- |
| Terminal, v katerem teče znana lupina | WSL 2 s podprto distribucijo Ubuntu za skupne vaje v lupini Bash |
| Bash za skupne vaje iz ukazne vrstice | PowerShell za namestitev in upravljanje WSL |
| Git z ustrezno nastavljeno identiteto | Jasno razlikovanje med ukazi pri pozivih `PS C:\>` in `user@host:~$` |
| Tolmač Python 3.12 kot preizkušeno predmetno izhodišče | Zavedanje, da sta `C:\Users\Ime\...` in `/home/ime/...` različna sistema poti |
| Po eno virtualno okolje za vsak projekt | Zavedanje, da so datoteke sistema Windows v WSL dostopne pod `/mnt/c/...` |

Če uporabljate macOS ali Linux, namestitev WSL preskočite. Še vedno opravite korake za Bash, Git in Python.

## Besedišče pred ukazi

| Izraz | Pomen na tej poti |
| --- | --- |
| **Terminal** | Program, ki prikazuje besedilo in sprejema vnos. Primera sta Windows Terminal in Terminal v macOS. |
| **Lupina** | Program, ki bere ukaze. Bash in PowerShell sta različni lupini z različno skladnjo. |
| **Ukazna vrstica** | Besedilni vmesnik, v katerega vnesete ukaz in njegove argumente. To ni ime določene lupine. |
| **Bash** | Lupina, razširjena v sistemih GNU/Linux in dostopna v Ubuntuju pod WSL. Skupne vaje z datotekami in cevovodi uporabljajo Bash. |
| **PowerShell** | Lupina za Windows. Na tej poti jo uporabljate za upravljanje WSL in ukaze za aktiviranje okolja v sistemu Windows. |
| **WSL** | Windows Subsystem for Linux, okolje za poganjanje Linuxa v podprtih sistemih Windows. |
| **Distribucija Linuxa** | Pripravljeno operacijsko okolje Linux, na primer Ubuntu. WSL je platforma, Ubuntu pa distribucija, nameščena vanjo. |
| **Repozitorij** | Projektna mapa, katere zgodovino Git beleži v krajevni mapi `.git/`. |
| **Oddaljeni repozitorij** | Ločeno shranjen repozitorij, iz katerega lahko Git pridobiva spremembe ali vanj pošilja spremembe. GitHub je eden od možnih gostiteljev in ni isto kot Git. |
| **Tolmač Python** | Izvedljivi program, ki bere in izvaja kodo Python. `python`, `python3`, `python3.12` in `py -3.12` lahko izberejo različne tolmače. |
| **Paket** | Programska oprema, ki jo dodate v okolje Python, navadno z `python -m pip`. |
| **Virtualno okolje** | Projektno omejen kontekst tolmača Python in mapa s paketi, navadno `.venv/`. |
| **Projekt** | Človeku razumljiva celota: vprašanje, viri, koda, specifikacija okolja, dokumentacija, rezultati in omejitve. |

## Namestitev ni vsakodnevna uporaba

Namestitev spreminja računalnik: omogoči WSL ali namesti distribucijo, Git oziroma tolmač Python. Zanjo boste morda potrebovali skrbniške pravice ali pomoč ustanove. Pri vsakodnevnem delu odprete pravo lupino, vstopite v projektno mapo, aktivirate `.venv`, preverite `git status`, zaženete skripto in okolje deaktivirate.

Namestitvenih ukazov ne ponavljajte ob vsakem učenju. Če projektni ukaz ne uspe, ne uporabite samodejno `sudo`, ne spreminjajte trajno varnostnih pravil in ne nameščajte vsega znova. Najprej preverite trenutno lupino, pot, dovoljenja in aktivni tolmač.

## Celotna pot

Prvič opravite korake po vrsti. Pozneje se vrnite neposredno k postopku, ki ga potrebujete.

1. **Samo za Windows:** [Namestite WSL in Ubuntu v sistemu Windows](../workflows/foundations/install-wsl-and-ubuntu-on-windows.md).
2. [Premikajte se med datotekami in mapami z lupino Bash](../workflows/foundations/navigate-files-and-directories-with-bash.md).
3. [Uporabite cevovode, preusmerjanje in grep v lupini Bash](../workflows/foundations/use-pipes-redirection-and-grep-in-bash.md).
4. [Namestite in nastavite Git](../workflows/foundations/install-and-configure-git.md).
5. [Sledite manjšemu projektu z Gitom](../workflows/foundations/track-a-small-project-with-git.md).
6. [Namestite Python 3.12 za delo z NLP](../workflows/nlp/install-python-312-for-nlp.md).
7. [Ustvarite virtualno okolje Python 3.12](../workflows/nlp/create-a-python-312-virtual-environment.md).
8. [Namestite pakete Python s pipom](../workflows/nlp/install-python-packages-with-pip.md).
9. [Zaženite skripto Python iz terminala](../workflows/nlp/run-a-python-script-from-terminal.md).
10. [Uredite manjši projekt Python za NLP](../workflows/nlp/structure-a-small-python-nlp-project.md).
11. [Diagnosticirajte težave s Pythonom, venv in pipom](../workflows/nlp/troubleshoot-python-venv-and-pip.md).
12. [Klonirajte, zaženite, spremenite in potrdite projekt priročnika](../workflows/foundations/clone-run-change-and-commit-a-handbook-project.md).

[Preverjanje tehnične pripravljenosti pri Digitalni slovenistiki](../learning-paths/digitalna-slovenistika.md#preverjanje-tehnicne-pripravljenosti) te korake poveže v eno pripravljalno nalogo.

## Popravljiva in uničujoča dejanja

| Navadno popravljivo | Najprej se ustavite in preverite |
| --- | --- |
| Z `cd` vstopite v napačno mapo | `rm`, ki datoteke odstrani brez namiznega koša |
| Z `git add` pred potrditvijo dodate napačno datoteko | Rekurzivno odstranjevanje, na primer `rm -r` ali PowerShellov `Remove-Item -Recurse` |
| Ustvarite krajevno potrditev z nepopolnim sporočilom | Prepis datoteke z `>`, kadar vsebuje potrebno delo |
| Ustvarite zavržljivo okolje `.venv/`, ki ga lahko obnovite | Vsiljeno pošiljanje ali prepisovanje skupne zgodovine |
| Premaknete vzorčno datoteko in jo premaknete nazaj | Zagon skrbniškega ukaza, prekopiranega iz nepreverjenega odgovora |

Hranite varnostne kopije gradiva, ki ga ne morete znova pridobiti. Git je uporabna zgodovina, ni pa varnostna kopija, če je edini repozitorij na eni napravi.

## Specifikacija okolja ni `.venv/`

Mape `.venv/` nikoli ne vključite v Git. Vsebuje datoteke, odvisne od računalnika, in absolutne poti ter je namenjena ponovni izdelavi. V repozitorij vključite navodila in specifikacije:

```text
README.md
requirements.txt
.gitignore
```

V kratkem, pregledanem `requirements.txt` lahko navedete neposredne odvisnosti. `python -m pip freeze` zabeleži vse nameščene distribucije v trenutnem okolju; tak posnetek je lahko uporaben pri diagnosticiranju, toda nepregledan surovi izpis ni samodejno najboljša zaklepna datoteka za objavo.

## Meje, pomembne za humanistične podatke

- **Varnostne kopije:** nenadomestljive posnetke, prepise in terenske podatke hranite tudi zunaj Gita.
- **Poti:** imena s presledki zapišite v narekovajih. Če uporabljate orodja Linuxa v WSL, projekte praviloma hranite pod `/home/<uporabnik>/...`; pot `/mnt/c/...` prečka mejo z datotečnim sistemom Windows.
- **Dovoljenja:** napaka pri dovoljenjih je podatek za diagnozo, ne navodilo, naj pred vsak ukaz dodate `sudo`.
- **Konci vrstic:** Windows navadno uporablja CRLF, Linux pa LF. Celotnega korpusa ne spreminjajte samo zato, ker je urejevalnik pretvoril konce vrstic.
- **Kodiranje:** besedila in skripte hranite v UTF-8; pri branju ali pisanju v Pythonu kodiranje navedite.
- **Pravice in zasebnost:** s kloniranjem ali obdelavo vira ne pridobite dovoljenja za objavo. Preglejte README, licenco, pogoje uporabe podatkov in tveganja za osebne podatke.

## Pregled virov in platform

Do vseh spodnjih virov smo dostopali **23. julija 2026**.

| Platforma ali skupina ukazov | Preverjeni uradni vir | Sklep pregleda |
| --- | --- | --- |
| Namestitev WSL, nastavitev Ubuntuja in meja med datotečnima sistemoma | [Microsoft Learn: namestitev WSL](https://learn.microsoft.com/windows/wsl/install); [nastavitev razvojnega okolja WSL](https://learn.microsoft.com/windows/wsl/setup/environment) | `wsl --install` je podprta privzeta pot v ustreznih sistemih Windows 10/11; nove namestitve privzeto uporabljajo WSL 2, `wsl --list --verbose` pa preveri distribucijo in različico. WSL na preglednem računalniku nismo znova nameščali. |
| Skladnja lupine Bash, cevovodi, preusmerjanje, narekovaji, vzorci in zgodovina | [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html) | Skupni primeri uporabljajo skladnjo Bash; izvedli smo jih v GNU Bash 5.2.21 pod WSL 2. |
| Datotečni in besedilni pripomočki | [priročnik GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html); [priročnik GNU Grep](https://www.gnu.org/software/grep/manual/grep.html) | Primere za datoteke, štetje, razvrščanje in filtriranje smo izvedli samo v zavržljivi mapi. |
| Namestitev Gita in ukazi Git | [strani za namestitev Gita](https://git-scm.com/install/); [Pro Git](https://git-scm.com/book/en/v2) | Pot za WSL/Linux in vse krajevne vaje z repozitorijem smo preizkusili z Gitom 2.43. Izvorna navodila za Windows in macOS smo pregledali, namestitvenih programov pa nismo zagnali. |
| Python 3.12 in virtualna okolja | [prenosi Python](https://www.python.org/downloads/); [Python 3.12: `venv`](https://docs.python.org/3.12/library/venv.html) | Repozitorij in CI uporabljata Python 3.12 kot preizkušeno predmetno izhodišče. Ustvarjanje, aktiviranje, deaktiviranje in obnovo smo preizkusili s Pythonom 3.12.3 v Ubuntuju 24.04 pod WSL 2. |
| Nameščanje paketov | [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/) | Pot uporablja aktivirano okolje in `python -m pip`; ne uporablja `sudo pip`. Namestitev iz datoteke z zahtevami smo preizkusili v zavržljivem okolju. |

## Preverjanje pripravljenosti

Pripravljeni ste, ko lahko pojasnite in ne le prekopirate ukaz, ki:

- pokaže trenutno mapo in lupino;
- pokaže različici Gita in Pythona;
- aktivira projektno okolje;
- namesti dokumentirane zahteve;
- zažene kratko skripto;
- prikaže spremembo pred potrditvijo.

Shranite nastali `environment-check.md`. To je dokaz o enem uspešnem okolju, ne trditev, da so bile preizkušene vse platforme.
