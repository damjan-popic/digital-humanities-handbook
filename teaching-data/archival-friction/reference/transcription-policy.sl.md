# Pravila referenčnega prepisa

Vzorec obsega vrstico v glavi, naslov in uvodni odstavek na vrhu 1. strani
PDF-ja. Datoteka `source/provider-ocr.txt` ohranja besedilo iz plasti ABBYY
FineReader 9.0 v PDF-ju; strnjeni so le presledki, ki izvirajo iz postavitve.
Datoteka `reference/reference-transcription.txt` je ročno preverjen priročniški
prepis: sledi vidnemu tisku, ohranja zgodovinsko besedišče in ločila, združuje
le besede, deljene ob prelomu vrstice, ter ne posodablja črkovanja.

Prepis je dokumentirana referenca in ne neposredna »temeljna resnica«.
Poravnava znakov uporablja Unicode NFC in upošteva notranje presledke.
Poravnava besed deli besedilo po presledkih Unicode. Če ima več poravnav
enako najnižjo ceno, velja deterministični vrstni red: ujemanje, zamenjava,
izpust in vstavek.

Vzorec je namenoma majhen. CER, WER in podrobni pregled napak opisujejo samo
te vrstice; rezultatov ne smete posplošiti na celo stran, številko, naslov
ali zbirko.
