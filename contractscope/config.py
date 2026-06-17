import json
from pathlib import Path

def load_watchlist(path: str = "watchlist.json") -> list[str]:
    with open(path, "r") as f:
        data = json.load(f)
    return data["contractors"]