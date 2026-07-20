from pathlib import Path
import pandas as pd
import classla

input_dir = Path("data/raw/texts")
output_path = Path("output/classla-tokens.csv")
output_path.parent.mkdir(exist_ok=True)

if not input_dir.exists():
    raise SystemExit(f"Input folder does not exist: {input_dir}")

txt_files = sorted(input_dir.glob("*.txt"))
if not txt_files:
    raise SystemExit(f"No .txt files found in {input_dir}")

nlp = classla.Pipeline("sl", processors="tokenize,pos,lemma")
rows = []

for txt_path in txt_files:
    doc_id = txt_path.stem
    text = txt_path.read_text(encoding="utf-8")
    doc = nlp(text)

    for sent_id, sentence in enumerate(doc.sentences, start=1):
        for word in sentence.words:
            rows.append({
                "doc_id": doc_id,
                "source_file": txt_path.name,
                "sent_id": sent_id,
                "word_id": word.id,
                "text": word.text,
                "lemma": word.lemma,
                "upos": word.upos,
            })

df = pd.DataFrame(rows)
df.to_csv(output_path, index=False)

lemma_counts = (
    df.groupby(["lemma", "upos"])
    .size()
    .reset_index(name="count")
    .sort_values("count", ascending=False)
)
lemma_counts.to_csv("output/lemma-counts.csv", index=False)

print(f"Processed {len(txt_files)} files")
print(f"Wrote {len(df)} tokens to {output_path}")
print("Wrote output/lemma-counts.csv")
