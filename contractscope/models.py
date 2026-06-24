from dataclasses import dataclass

@dataclass
class Award:
    generated_internal_id: str
    award_id: str
    recipient_name: str
    award_amount: float
    awarding_agency: str
    awarding_sub_agency: str
    start_date: str
    end_date: str
    award_type: str | None

    @classmethod
    def from_raw(cls, raw: dict) -> "Award":
        return cls(
            generated_internal_id=raw["generated_internal_id"],
            award_id=raw["Award ID"],
            recipient_name=raw["Recipient Name"],
            award_amount=raw["Award Amount"],
            awarding_agency=raw["Awarding Agency"],
            awarding_sub_agency=raw["Awarding Sub Agency"],
            start_date=raw["Start Date"],
            end_date=raw["End Date"],
            award_type=raw.get("Award Type"),
        )