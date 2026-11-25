import os

LINE = (
    "Out of office until Monday. My agent has my inbox and my full confidence, which is exactly what it will use to invent your deadline."
)

output_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "entry.txt"), "w") as f:
    f.write(LINE + "\n")
