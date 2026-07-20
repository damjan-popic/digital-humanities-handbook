from pathlib import Path
import sys

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

message = "Hello from a reproducible Python script."
run_info = f"{message}\nPython: {sys.version}\n"

print(message)
(output_dir / "hello.txt").write_text(run_info, encoding="utf-8")
