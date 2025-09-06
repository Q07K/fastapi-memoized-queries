"""데이터베이스 세션 관리 모듈."""

from typing import Any, Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import get_settings

settings = get_settings()

engine = create_engine(
    url=settings.database_url,
    connect_args={"check_same_thread": False},
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, Any, None]:
    """데이터베이스 세션을 생성하고 종료하는 제너레이터 함수.

    Yields
    ------
    Generator[Session, Any, None]
        데이터베이스 세션
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
