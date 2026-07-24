---
title: "Kako se z lupino Bash premikam med datotekami in mapami?"
description: "Varno vadite premikanje in delo z datotekami v zavržljivi humanistični mapi."
category_id: "foundations"
category: "Osnove"
difficulty: "začetno"
time: "30–45 min"
tags: [Bash, terminal, poti, datoteke, WSL]
---

# Kako se z lupino Bash premikam med datotekami in mapami?

<div class="answer-meta" markdown>
<span>Osnove</span>
<span>začetno</span>
<span>30–45 min</span>
</div>

## Kaj želite doseči

Pred pretvorbo korpusa morate vedeti, iz katere mape bo ukaz bral in kam bo pisal. Ustvarili boste zavržljivo mapo, se premikali po njej, pregledali majhne datoteke UTF-8 ter vadili popravljive datotečne operacije.

Vse ukaze na tej strani izvedite v **lupini Bash**, ne v PowerShellu.

## Kaj potrebujete

- Bash v macOS, Linuxu ali Ubuntuju pod WSL;
- vadbeno lokacijo brez nenadomestljivih datotek;
- terminal s pozivom, podobnim `student@computer:~$`.

## Postopek

### 1. Preverite, kje ste

```bash
pwd
```

`pwd` izpiše absolutno pot delovne mape. **Absolutna pot** se začne pri `/`, na primer `/home/student`. **Relativna pot** se začne v trenutni mapi, na primer `technical-practice/texts`.

### 2. Ustvarite zavržljivo učno mapo

```bash
mkdir -p ~/technical-practice/texts
cd ~/technical-practice
pwd
```

Vse nadaljnje delo ostane v `~/technical-practice/`. Med učenjem te mape ne zamenjajte z mapo raziskovalnih podatkov.

### 3. Naštejte vidne in skrite vnose

```bash
ls
ls -la
```

`ls` našteje vidne vnose. `ls -a` pokaže tudi imena, ki se začnejo s `.`, zato so po dogovoru skrita. Vnosa `.` in `..` pomenita trenutno in nadrejeno mapo:

```bash
ls .
ls ..
```

### 4. Ustvarite majhne datoteke

```bash
touch "reading notes.txt"
touch texts/poem.txt
printf 'jutro\nmesto\njutro\n' > texts/poem.txt
```

`touch` ustvari prazno datoteko, če še ne obstaja. Zadnji ukaz zapiše tri vrstice v zavržljivo datoteko; `>` nadomesti njeno prejšnjo vsebino. Narekovaji okoli `"reading notes.txt"` ohranijo presledek v enem imenu.

### 5. Preglejte besedilo brez urejanja

```bash
cat texts/poem.txt
head -n 2 texts/poem.txt
tail -n 2 texts/poem.txt
less texts/poem.txt
```

- `cat` izpiše kratko datoteko;
- `head` in `tail` pokažeta začetek in konec;
- z `less` se premikate po daljši datoteki, ne da bi jo spremenili; za izhod pritisnite `q`.

### 6. Vadite popravljivo kopiranje in premikanje

```bash
cp texts/poem.txt "copy of poem.txt"
mv "copy of poem.txt" texts/poem-copy.txt
ls -la texts
```

`cp` ohrani vir in ustvari kopijo. `mv` vnos premakne ali preimenuje. Pred obema ukazoma preverite, ali cilj že obstaja: prepis lahko uniči delo.

### 7. Vadite relativno premikanje

```bash
cd texts
pwd
cd ..
pwd
cd ./texts
cd ..
```

`..` pomeni nadrejeno mapo, `.` pa trenutno. `cd` spremeni delovno mapo lupine, datotek pa ne premakne.

### 8. Uporabite dopolnjevanje in zgodovino

Vnesite `cd te` in pritisnite **Tab**, namesto da bi ime dokončali sami. Bash lahko dopolni nedvoumno pot. S **puščico navzgor** prikličite prejšnji ukaz, ga uredite in pritisnite Enter šele po ponovnem branju.

Zapisane ukaze pregledate z:

```bash
history
```

Zgodovina lahko vsebuje občutljive argumente. Gesel ali žetonov ne vnašajte neposredno v ukaze.

### 9. V WSL prepoznajte poti Windows in Linux

Spodnja imena kažejo na različne lokacije:

```text
Windows: C:\Users\Student\Documents\corpus
WSL:     /mnt/c/Users/Student/Documents/corpus
Linux:   /home/student/projects/corpus
```

V lupini Bash uporabljajte poti Linuxa. Za Git in Python v Linuxu raje izberite `/home/student/projects/...`. Pot do priklopljenega sistema Windows s presledkom zapišite v narekovajih:

```bash
cd "/mnt/c/Users/Student/My Documents"
```

Primer zamenjajte samo, če mapa res obstaja.

## Namerno opozorilo o odstranjevanju

`rm` odstrani datoteke brez namiznega koša. Ni ukaz za razveljavitev; `rm -r` lahko odstrani celotno drevo map. V tem začetnem postopku rekurzivnega odstranjevanja ne uporabljamo.

Šele ko potrdite, da ste v zavržljivi mapi:

```bash
pwd
ls "reading notes.txt"
rm "reading notes.txt"
```

Če `pwd` ne pokaže vaše mape `technical-practice` ali je navedeno ime nepričakovano, se ustavite. Za nenadomestljivo gradivo hranite varnostne kopije.

## Rezultat

```text
technical-practice/
└── texts/
    ├── poem-copy.txt
    └── poem.txt
```

## Preverite se

- Ali prepoznate absolutno pot, ki jo izpiše `pwd`?
- Ali lahko pojasnite `.` in `..`, ne da bi ju imenovali datoteki?
- Ali poti s presledki in narekovaji delujejo?
- Ali lahko datoteko pregledate z `less` in zaprete z `q`?
- Ali pred `cp`, `mv` ali `rm` poznate natančni vir in cilj?

## Pogoste pasti

- pot PowerShella, na primer `C:\...`, neposredno prilepite v Bash;
- ukaze izvajate pod `/mnt/c/...`, ne da bi vedeli, da ste prestopili mejo med datotečnima sistemoma;
- pri imenu s presledki izpustite narekovaje;
- skrito datoteko zamenjate z manjkajočo;
- `rm -r` uporabljate kot bližnjico za pospravljanje, ne da bi preverili cilj.

## Naloga

V `~/technical-practice/` ustvarite `sources/` in `notes/`. Ustvarite eno kratko datoteko UTF-8, jo kopirajte, kopijo preimenujte ter preglejte prvo in zadnjo vrstico. Ukaze zabeležite v `notes/commands.txt`; vanjo ne vključite poverilnic ali zasebnega izvornega besedila.

## Preverjeni viri

Dostopano **23. julija 2026**:

- [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html)
- [priročnik GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [Microsoft Learn: priporočila za shranjevanje datotek v WSL](https://learn.microsoft.com/windows/wsl/setup/environment#file-storage)

Zaporedje, vključno z `rm` za eno datoteko, smo preizkusili v novoustvarjeni zavržljivi mapi z GNU Bash 5.2.21 in GNU coreutils v Ubuntuju 24.04 pod WSL 2.
