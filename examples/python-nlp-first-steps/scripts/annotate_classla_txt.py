from pathlib import Path
import classla

input_path = Path("data/raw/sample-sl.txt")
output_path = Path("output/sample-sl.tsv")
output_path.parent.mkdir(exist_ok=True)

text = input_path.read_text(encoding="utf-8")

nlp = classla.Pipeline("sl", processors="tokenize,pos,lemma")
doc = nlp(text)

rows = ["sent_id\tword_id\ttext\tlemma\tupos"]

for sent_id, sentence in enumerate(doc.sentences, start=1):
    for word in sentence.words:
        rows.append(f"{sent_id}\t{word.id}\t{word.text}\t{word.lemma}\t{word.upos}")

output_path.write_text("\n".join(rows) + "\n", encoding="utf-8")
print(f"Wrote {output_path}")
