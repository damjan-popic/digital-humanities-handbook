# Pravila referenčnega prepisa

Vzorec obsega vrstico v glavi, naslov in uvodni odstavek na vrhu 1. strani
PDF-ja. Datoteka `source/provider-ocr.txt` je bajtno nespremenjen izvoz TXT iz
dLib: meri 5.710 bajtov, uporablja zaključke vrstic CRLF in ima zgoščeno
vrednost SHA-256
`ab4e9e5464eb349d4c27b3b895c2b98b3a6509f3ce4be76f387b739a1fcee456`.
Gradilnik jo dekodira kot Windows-1250, izbere vrstice 1–4, združi vrstici 1
in 2 kot glavo, ohrani vrstici 3 in 4 kot naslov in odstavek, uporabi
normalizacijo Unicode NFC ter poenoti zaporedne presledne znake v teh treh
vrsticah za primerjavo. Tako nastane izpeljana datoteka UTF-8
`raw/provider-ocr.txt`; odločitev AF-ED-009 dokumentira ta na viru utemeljeni
izbor in normalizacijo.

Datoteka `reference/reference-transcription.txt` je ročno preverjen
priročniški prepis: sledi vidnemu tisku, ohranja zgodovinsko besedišče in
ločila, združuje le besede, deljene ob prelomu vrstice, ter ne posodablja
črkovanja.

Prepis je dokumentirana referenca in ne neposredna »temeljna resnica«.
Poravnava znakov uporablja Unicode NFC in upošteva notranje presledke.
Poravnava besed deli besedilo po preslednih znakih Unicode. Če ima več poravnav
enako najnižjo ceno, velja deterministični vrstni red: ujemanje, zamenjava,
izpust in vstavek.

Vzorec je namenoma majhen. Izračun CER in WER ter podrobni pregled napak se
začnejo po dokumentiranem izboru in normalizaciji presledkov. Zato ne merijo
izpuščenih presledkov postavitve in opisujejo samo te vrstice; rezultatov ne
smete posplošiti na celo stran, številko, naslov ali zbirko.
