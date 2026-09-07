---
translation_status: machine-assisted draft; requires human language review
---

# Znane težave in omejena negotovost

- Vzorec CLASSLA je namenski, majhen in deloma izbran zaradi zahtevnosti. Mere
  posameznih plasti diagnosticirajo samo ta vzorec in nimajo intervala zaupanja.
- Referenčna anotacija je strojno podprti raziskovalni osnutek, ki čaka na
  strokovni človeški pregled. Drug usposobljeni označevalec se lahko utemeljeno
  odloči drugače, zlasti pri odvisnostnih glavah, razmerjih in zgodovinskih lemah.
- Ponudnikov OCR in zgodovinski referenčni prepis sta dve besedilni različici
  istega odlomka. Primerjava nadaljnjih anotacij pomeša poškodbe prepoznavanja z
  vedenjem označevalnika; ne gre za neodvisna korpusa.
- Natančno ujemanje čustvenih oblik namenoma ne uporablja lematizacije. Majhni
  leksikon ni popoln, kategorija `fear` pa zaradi učnega prikaza skrb namenoma
  združi s strahom.
- Sintetični korpus z dvanajstimi dokumenti je veliko premajhen za utemeljeno
  empirično raziskavo tem. Rezultat o stabilnosti ponazarja le občutljivost in
  ujemanje.
- Identiteto tem NMF določa največje Jaccardovo prekrivanje najpomembnejših besed
  znotraj istega števila sestavin. Majhno prekrivanje in izenačenja ostanejo
  negotovost, ki je ne smete prikriti.
- Različice modelov, datoteke virov in vmesniki se spreminjajo. Zamrznjeni
  rezultat dokumentira eno izvedbo, običajni CI pa ga ne prenaša znova.
- Končne datoteke modelskih virov imajo kontrolne vsote, njihovega časa
  pridobitve pa ni mogoče obnoviti, zato je izrecno označen kot `unknown`.
- Slovenska dokumentacija je strojno podprti osnutek, ki čaka na strokovni
  jezikovni pregled.
