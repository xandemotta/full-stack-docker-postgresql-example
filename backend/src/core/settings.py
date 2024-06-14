# from typing import Optional, Dict, Any

# from pydantic import BaseSettings, PostgresDsn, validator


# class Settings(BaseSettings):
#     POSTGRES_USER: str
#     POSTGRES_PASSWORD: str
#     POSTGRES_HOST: str
#     POSTGRES_DB: str

#     DATABASE_URI: Optional[str] = None
    
#     class Config:
#         arbitrary_types_allowed = True

#     @validator("DATABASE_URI", pre=True)
#     def assymbly_database_uri(
#         cls, v: str, values: Dict[str, Any]
#     ) -> str:
#         if v:
#             return v
#         return PostgresDsn.build(
#             scheme="postgresql+asyncpg",
#             user=values["POSTGRES_USER"],
#             password=values["POSTGRES_PASSWORD"],
#             host=values["POSTGRES_HOST"],
#             path="/" + values["POSTGRES_DB"],
#         )


# settings = Settings()


from typing import Optional, Dict, Any

from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_DB: str

    DATABASE_URI: Optional[str] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_database_uri(
        cls, v: Optional[str], values: Dict[str, Any]
    ) -> str:
        if v is not None:
            return v
        return f"postgresql+asyncpg://{values['POSTGRES_USER']}:{values['POSTGRES_PASSWORD']}@{values['POSTGRES_HOST']}/{values['POSTGRES_DB']}"


settings = Settings()
