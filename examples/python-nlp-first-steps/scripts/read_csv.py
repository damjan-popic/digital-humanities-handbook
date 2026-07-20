from pathlib import Path
import pandas as pd

input_path = Path("data/documents.csv")
output_path = Path("output/documents-cleaned.csv")
output_path.parent.mkdir(exist_ok=True)

df = pd.read_csv(input_path, dtype={"id": "string"})

print("Columns:", list(df.columns))
print("Rows:", len(df))
print(df.head())

df["text_length"] = df["text"].str.len()
df["has_year"] = df["year"].notna()
df["word_count"] = df["text"].str.split().str.len()

df.to_csv(output_path, index=False)
print(f"Wrote {output_path}")
