from contractscope.storage.repo import save_awards
from contractscope.storage.schema import AwardRow
from contractscope.models import Award

def test_save_awards_is_idempotent(db_session):
    awards = [
        Award(generated_internal_id="TEST_001", award_id="A001", recipient_name="N001", award_amount=1, awarding_agency="AA001", awarding_sub_agency="ASA001", start_date="2026-09-03", end_date="2026-09-04", award_type="AT001"),
        Award(generated_internal_id="TEST_002", award_id="A002", recipient_name="N002", award_amount=2, awarding_agency="AA002", awarding_sub_agency="ASA002", start_date="2026-09-03", end_date="2026-09-04", award_type="AT002"),
    ]

    save_awards(awards, session=db_session)
    save_awards(awards, session=db_session)

    count = db_session.query(AwardRow).count()
    assert count == 2