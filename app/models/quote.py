"""명언(Quote) Table model 정의."""

from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

# TYPE_CHECKING은 순환 참조(circular import) 오류 없이
# 타입 힌트(Quote)를 사용하기 위해 필요합니다.
if TYPE_CHECKING:
    from .daily_assignment import DailyAssignment


class Quote(Base):
    """명언(Quote) Table model."""

    __tablename__ = "quotes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(String(500), nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)

    daily_assignments: Mapped[list["DailyAssignment"]] = relationship(
        "DailyAssignment",
        back_populates="quote",
        cascade="all, delete-orphan",
    )
