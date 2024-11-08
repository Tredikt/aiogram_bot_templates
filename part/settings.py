from pydantic.v1 import BaseSettings, Field


class Settings(BaseSettings):
    telegram__token: str = Field(env="TELEGRAM_TOKEN")
    database__url: str = Field(env="DATABASE_URL")

    admin_ids: str = Field(env="ADMIN_IDS")

    class Config:
        env_file = ".env"


env_settings = Settings()
