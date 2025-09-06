"""일일 할당(DailyAssignment) Table model 정의."""

from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

# TYPE_CHECKING은 순환 참조(circular import) 오류 없이
# 타입 힌트(Quote)를 사용하기 위해 필요합니다.
if TYPE_CHECKING:
    from .quote import Quote


class DailyAssignment(Base):
    """일일 할당(DailyAssignment) Table model."""

    __tablename__ = "daily_assignments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    assigned_date: Mapped[str] = mapped_column(String(100), nullable=False)
    quote_id: Mapped[int] = mapped_column(Integer, nullable=False)

    quote: Mapped["Quote"] = relationship(
        "Quote",
        back_populates="daily_assignments",
    )
