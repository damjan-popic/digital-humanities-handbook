---
title: "Kako namestim WSL in Ubuntu v sistemu Windows?"
description: "Namestite podprto okolje WSL 2, ustvarite uporabnika Ubuntu in preverite, kje tečejo ukazi Bash."
category_id: "foundations"
category: "Osnove"
difficulty: "začetno"
time: "20–60 min in ponovni zagon"
tags: [WSL, Ubuntu, Windows, Bash, namestitev]
---

# Kako namestim WSL in Ubuntu v sistemu Windows?

<div class="answer-meta" markdown>
<span>Osnove</span>
<span>začetno</span>
<span>20–60 min in ponovni zagon</span>
</div>

## Kaj želite doseči

Za predmetni projekt, pri katerem se morajo besedila, skripte in preverjanja obnašati predvidljivo, potrebujete skupno okolje Bash. V podprtih sistemih Windows lahko z WSL 2 poganjate distribucijo Ubuntu, ne da bi morali namestiti predogledno različico sistema Windows.

Če uporabljate macOS ali Linux, ta postopek preskočite. Nadaljujte s [premikanjem med datotekami in mapami z lupino Bash](navigate-files-and-directories-with-bash.md).

## Kaj potrebujete

- Windows 11 ali Windows 10, različico 2004 (gradnjo 19041) ali novejšo;
- dovoljenje za omogočanje funkcij sistema Windows in nameščanje programske opreme;
- internetno povezavo in čas za ponovni zagon;
- izbrano uporabniško ime za Linux, ki ni nujno enako računu Windows.

Na računalniku, ki ga upravlja ustanova, se pred začetkom posvetujte z oddelkom za informatiko. Če nimate skrbniških pravic, prosite, naj vam namestijo WSL 2 in podprto distribucijo Ubuntu. Pravil ne obidite z izklapljanjem varnostnih nadzorov ali prenašanjem neuradnih slik.

## Pred ukazom preverite lupino

Namestitveni ukaz izvedete v **PowerShellu s skrbniškimi pravicami**:

```text
PS C:\>
```

Vsakodnevne predmetne ukaze pozneje izvajate v **lupini Bash v Ubuntuju**:

```text
student@computer:~$
```

Poziva, skladnja poti in ukazi niso zamenljivi.

## Postopek

### 1. Odprite PowerShell kot skrbnik

Odprite meni Start, poiščite **PowerShell** ali **Windows Terminal**, kliknite z desno tipko in izberite **Zaženi kot skrbnik**. Okno s povišanimi pravicami uporabite za namestitev WSL, ne za redno projektno delo.

### 2. Namestite podprto privzeto okolje WSL

**PowerShell (skrbnik):**

```powershell
wsl --install
```

Na ustreznem računalniku brez nameščenega WSL ukaz omogoči potrebne komponente sistema Windows, namesti WSL, za nove namestitve izbere WSL 2 in namesti Ubuntu. Ko sistem to zahteva, računalnik znova zaženite.

Če se prikaže pomoč, ker WSL že obstaja, najprej preglejte podprte distribucije:

```powershell
wsl --list --online
```

Nato namestite predmetno distribucijo:

```powershell
wsl --install -d Ubuntu
```

Ne dodajajte `--pre-release`, ne vključujte se v program Insider in ne zamenjajte podprte učne distribucije samo zaradi novejših funkcij.

### 3. Ustvarite uporabnika Linuxa

Po ponovnem zagonu iz menija Start odprite **Ubuntu**. Ob prvem zagonu se distribucija razširi in zahteva:

1. uporabniško ime za Linux;
2. geslo za Linux.

Uporabniško ime in geslo pripadata tej distribuciji Ubuntu, ne računu Windows. Med vnašanjem gesla se ne izpiše nič; to je običajno. Geslo varno shranite. Račun lahko opravlja skrbniška dejanja z `sudo`, vendar zato `sudo` ni vsakdanja predpona ali splošna rešitev za napake pri dovoljenjih.

### 4. V PowerShellu preverite WSL 2

Zaprite Ubuntu ali odprite ločen navaden zavihek PowerShell.

**PowerShell:**

```powershell
wsl --list --verbose
```

Pričakovana oblika:

```text
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

Ime distribucije lahko vsebuje številko različice. Pomemben dokaz je vnos Ubuntu z vrednostjo `2` v stolpcu `VERSION`.

### 5. Preverite lupino v Ubuntuju

Znova odprite Ubuntu.

**Ubuntu Bash:**

```bash
whoami
printf '%s\n' "$SHELL"
pwd
cat /etc/os-release
```

Videti morate uporabniško ime za Linux, pot do lupine Bash, na primer `/bin/bash`, domačo mapo, na primer `/home/student`, in podatke o različici Ubuntuja.

### 6. Predmetno delo ustvarite v datotečnem sistemu Linuxa

**Ubuntu Bash:**

```bash
mkdir -p ~/projects
cd ~/projects
pwd
```

Microsoft priporoča, da projekte hranite v istem datotečnem sistemu kot orodja, ki jih uporabljajo. Za to pot z Bashom in Pythonom uporabite `/home/<uporabnik>/projects/...`. Datoteke sistema Windows so dostopne pod `/mnt/c/...`, vendar je ponavljajoče poganjanje paketnih ali Gitovih operacij čez to mejo lahko počasnejše, poti, dovoljenja in konce vrstic pa je teže razumeti.

## Rezultat

- podprta distribucija Ubuntu v okolju WSL 2;
- uporabnik Linuxa, ki ni `root`;
- domača mapa Bash in mapa `~/projects/`;
- izpis terminala z distribucijo, različico WSL in lupino.

## Preverite se

- Ali `wsl --list --verbose` pokaže Ubuntu z različico 2?
- Ali poziv Ubuntu uporablja poti v obliki Linuxa?
- Ali `printf '%s\n' "$SHELL"` pokaže Bash?
- Ali lahko pojasnite razliko med `C:\Users\Ime\Project` in `/home/ime/projects/project`?

## Pogoste pasti

| Znak | Varen naslednji korak |
| --- | --- |
| Windows sporoči, da ukaz ni podprt | Zabeležite različico sistema Windows in se obrnite na informatike; Microsoftov dokumentirani ročni postopek uporabite samo z dovoljenjem ustanove. |
| Nimate skrbniškega dovoljenja | Ustavite se in zahtevajte namestitev. Upravljanja naprave ne obidite. |
| Virtualizacija ni dostopna ali je blokirana | Zabeležite celotno sporočilo in informatike vprašajte, ali naprava podpira potrebne funkcije virtualizacije. |
| Ubuntu zahteva geslo, vendar ne pokaže znakov | Nadaljujte z vnosom in pritisnite Enter; vnos gesla v Linuxu namenoma ni viden. |
| Distribucija kaže WSL 1 | Pred spreminjanjem upravljanega računalnika vprašajte izvajalko, izvajalca ali informatike; izpis shranite kot dokaz. |

## Naloga

Pozneje v projektu pripravljenosti v `environment-check.md` zabeležite:

```text
Operacijski sistem: Windows … z Ubuntujem … pod WSL 2
Lupina: /bin/bash
Lokacija projekta: /home/…/projects/…
```

Ne zapisujte gesla, žetona računa Windows ali drugih poverilnic.

## Preverjeni viri

Dostopano **23. julija 2026**:

- [Microsoft Learn: namestitev Linuxa v sistemu Windows z WSL](https://learn.microsoft.com/windows/wsl/install)
- [Microsoft Learn: nastavitev razvojnega okolja WSL](https://learn.microsoft.com/windows/wsl/setup/environment)
- [Microsoft Learn: osnovni ukazi WSL](https://learn.microsoft.com/windows/wsl/basic-commands)

Namestitev in pozivi ob prvem zagonu so vezani na platformo; pri tej spremembi smo jih preverili po virih, namestitve pa nismo ponovili. Ukaze za preverjanje in Bash smo preizkusili v Ubuntuju 24.04 pod WSL 2.
