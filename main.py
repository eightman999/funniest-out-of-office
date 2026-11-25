import os

LINE = (
    "Out of office. My AI agent is covering my inbox, "
    "so replies will be instant, confident, and legally non-binding."
)

output_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "entry.txt"), "w") as f:
    f.write(LINE + "\n")
