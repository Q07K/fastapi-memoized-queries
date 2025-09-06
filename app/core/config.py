"""애플리케이션 설정 관리 모듈."""

from functools import cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """애플리케이션 설정 관리 클래스."""

    app_name: str = "FastAPI Memoized Queries"
    database_url: str = "sqlite+aiosqlite:///./quotes.db"


@cache
def get_settings() -> Settings:
    """설정 인스턴스를 반환합니다."""
    return Settings()
