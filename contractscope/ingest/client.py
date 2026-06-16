import requests
from ..models import Award
from pathlib import Path
import json

class USASpendingClient:
    BASE_URL = "https://api.usaspending.gov/api/v2"

    def __init__(self, timeout: int = 30) -> None:
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "ContractScope/0.1"})

    def search_awards(self, recipient: str, *, limit: int = 100, page: int = 1) -> list[Award]:

        path = self._cache_path(recipient, limit, page)

        if path.exists():
            with open(path, "r") as f:
                data = json.load(f)
            return [Award.from_raw(r) for r in data["results"]]

        body = {
            "filters": {
                "award_type_codes": ["A", "B", "C", "D"],
                "recipient_search_text": [recipient],
                "time_period": [{"start_date": "2023-01-01", "end_date": "2025-12-31"}],
            },
            "fields": [
                "Award ID", "Recipient Name", "Award Amount",
                "Awarding Agency", "Awarding Sub Agency",
                "Start Date", "End Date", "Award Type",
            ],
            "limit": limit,
            "page": page,
        }

        url = f"{self.BASE_URL}/search/spending_by_award/"
        response = self.session.post(url, json=body, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()

        with open(path, "w") as f:
            json.dump(data, f)
        return [Award.from_raw(r) for r in data["results"]]
    
    def _cache_path(seld, recipient: str, limit: int, page: int) -> Path:
        cache_dir = Path("data/cache")
        cache_dir.mkdir(parents=True, exist_ok=True)
        safe_recipient = recipient.lower().replace(" ", "-")
        filename = f"{safe_recipient}_limit{limit}_page{page}.json"
        return cache_dir / filename
    
