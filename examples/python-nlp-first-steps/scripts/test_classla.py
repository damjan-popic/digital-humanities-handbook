import classla

nlp = classla.Pipeline("sl", processors="tokenize,pos,lemma")
doc = nlp("To je kratek preizkus slovenskega jezikovnega označevanja.")

for sentence in doc.sentences:
    for word in sentence.words:
        print(word.text, word.lemma, word.upos, sep="\t")
