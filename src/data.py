import json
from pathlib import Path

with Path("src/generated.json").open("r") as f:
    OUTPUT = json.load(f)
