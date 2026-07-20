from pathlib import Path

input_path = Path("data/sample.txt")
output_path = Path("output/sample-cleaned.txt")
output_path.parent.mkdir(exist_ok=True)

text = input_path.read_text(encoding="utf-8")
lines = [line.strip() for line in text.splitlines() if line.strip()]
cleaned = "\n".join(lines)

output_path.write_text(cleaned + "\n", encoding="utf-8")
print(f"Read {input_path}")
print(f"Wrote {output_path}")
