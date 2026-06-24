import pytest

from contractscope.models import Award
from contractscope.analysis.rank import canonical_recipient

def test_from_raw_maps_all_fields():
    raw = {
    "generated_internal_id": "CONT_AWD_W91WRZ24P0019_9700_-NONE-_-NONE-",
    "Award ID": "W91WRZ24P0019",
    "Recipient Name": "LEIDOS, INC.",
    "Award Amount": 104625.0,
    "Awarding Agency": "Department of Defense",
    "Awarding Sub Agency": "Department of the Army",
    "Start Date": "2024-09-30",
    "End Date": "2026-09-30",
    "Award Type": "DELIVERY ORDER",
    }

    award = Award.from_raw(raw)

    assert award.recipient_name == "LEIDOS, INC."
    assert award.award_id == "W91WRZ24P0019"
    assert award.award_amount == 104625.0

def test_from_raw_handles_missing_award_type():
    raw = {
        "generated_internal_id": "CONT_AWD_W91WRZ24P0019_9700_-NONE-_-NONE-",
        "Award ID": "W91WRZ24P0019",
        "Recipient Name": "LEIDOS, INC.",
        "Award Amount": 104625.0,
        "Awarding Agency": "Department of Defense",
        "Awarding Sub Agency": "Department of the Army",
        "Start Date": "2024-09-30",
        "End Date": "2026-09-30",
    }

    award = Award.from_raw(raw)

    assert award.award_type is None