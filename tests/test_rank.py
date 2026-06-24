import pytest

from contractscope.analysis.rank import canonical_recipient

@pytest.mark.parametrize(
    "raw_name, expected",
    [
        ("LEIDOS, INC.", "Leidos"),
        ("LEIDOS SECURITY DETECTION & AUTOMATION, INC.", "Leidos"),
        ("KALEIDOSCOPE AFFECT, LLC", "Other"),
        ("NORTHROP GRUMMAN SYSTEMS CORPO", "Northrop Grumman"),
        ("THE ARC OF BERGEN AND PASSAIC COUNTIES INC", "Other")
    ]
)
def test_canonical_recipient(raw_name, expected):
    assert canonical_recipient(raw_name) == expected