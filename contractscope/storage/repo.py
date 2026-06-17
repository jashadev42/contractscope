from .db import SessionLocal
from .schema import AwardRow
import sqlite3
from .db import DB_PATH


from ..models import Award

def save_awards(awards: list[Award]) -> int:
    with SessionLocal() as session:
        for award in awards:
            row = AwardRow.from_award(award)
            session.merge(row)
        session.commit()
    return len(awards)

def load_awards() -> list[Award]:
    with SessionLocal() as session:
        rows = session.query(AwardRow).all()
        return [row.to_award() for row in rows]
    
def total_by_recipient_raw() -> list[tuple[str, float]]:
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.execute(
            "SELECT     recipient_name, SUM(award_amount) "
            "FROM       awards "
            "GROUP BY   recipient_name "
            "ORDER BY SUM(award_amount) DESC"
        )
        return cursor.fetchall()
    finally:
        connection.close()