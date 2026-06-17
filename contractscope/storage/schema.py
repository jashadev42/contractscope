from sqlalchemy import String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..models import Award

class Base(DeclarativeBase):
    pass

class AwardRow(Base):
    __tablename__ = "awards"

    generated_internal_id: Mapped[str] = mapped_column(primary_key=True)
    award_id: Mapped[str] = mapped_column(String)
    recipient_name: Mapped[str] = mapped_column(String)
    award_amount: Mapped[float] = mapped_column(Float)
    awarding_agency: Mapped[str] = mapped_column(String)
    awarding_sub_agency: Mapped[str] = mapped_column(String)
    start_date: Mapped[str] = mapped_column(String)
    end_date: Mapped[str] = mapped_column(String)
    award_type: Mapped[str | None] = mapped_column(String, nullable=True)

    @classmethod
    def from_award(cls, award: "Award") -> "AwardRow":
        return cls(
            generated_internal_id=award.generated_internal_id,
            award_id=award.award_id,
            recipient_name=award.recipient_name,
            award_amount=award.award_amount,
            awarding_agency=award.awarding_agency,
            awarding_sub_agency=award.awarding_sub_agency,
            start_date=award.start_date,
            end_date=award.end_date,
            award_type=award.award_type
        )
    
    def to_award(self) -> "Award":
        from ..models import Award
        return Award(
            generated_internal_id=self.generated_internal_id,
            award_id=self.award_id,
            recipient_name=self.recipient_name,
            award_amount=self.award_amount,
            awarding_agency=self.awarding_agency,
            awarding_sub_agency=self.awarding_sub_agency,
            start_date=self.start_date,
            end_date=self.end_date,
            award_type=self.award_type
        )