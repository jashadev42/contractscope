import requests
from ..models import Award

class USASpendingClient:
    BASE_URL = "https://api.usaspending.gov/api/v2"

    def __init__(self, timeout: int = 30) -> None:
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "ContractScope/0.1"})

    def search_awards(self, recipient: str, *, limit: int = 100, page: int = 1) -> list[Award]:
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
        return [Award.from_raw(r) for r in data["results"]]