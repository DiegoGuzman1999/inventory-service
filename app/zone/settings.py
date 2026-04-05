import os
from pydantic_settings import BaseSettings, SettingsConfigDict


def get_env_file() -> str:
    env = os.getenv("APP_ENV", "dev").lower()
    if env == "qa":
        return ".env.qa"
    if env == "prod":
        return ".env.prod"
    return ".env.dev"


class Settings(BaseSettings):
    app_name: str = "inventory-service"
    app_env: str = "dev"
    app_host: str = "127.0.0.1"
    app_port: int = 8002
    log_level: str = "debug"

    model_config = SettingsConfigDict(
        env_file=get_env_file(),
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
