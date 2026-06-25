from .db import SessionLocal
from .schema import AwardRow
import sqlite3
from .db import DB_PATH
from sqlalchemy.orm import Session


from ..models import Award

def save_awards(awards: list[Award], session: Session | None = None) -> int:
    own_session = session is None
    if own_session:
        session = SessionLocal()
    try:
        for award in awards:
            row = AwardRow.from_award(award)
            session.merge(row)
        session.commit()
    finally:
        if own_session:
            session.close()
    return len(awards)

def load_awards(session: Session | None = None) -> list[Award]:
    own_session = session is None
    if own_session:
        session = SessionLocal()
    try:
        rows = session.query(AwardRow).all()
    finally:
        if own_session:
            session.close()
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