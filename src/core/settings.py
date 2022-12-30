from typing import Optional, Dict, Any

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_DB: str

    DATABASE_URI: Optional[str] = None

    @validator("DATABASE_URI", pre=True)
    def assymbly_database_uri(
        cls, v: str, values: Dict[str, Any]
    ) -> str:
        if v:
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values["POSTGRES_USER"],
            password=values["POSTGRES_PASSWORD"],
            host=values["POSTGRES_HOST"],
            path="/" + values["POSTGRES_DB"],
        )


settings = Settings()
