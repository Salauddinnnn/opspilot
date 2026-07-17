from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "OpsPilot"
    APP_VERSION: str = "1.0.0"

    model_config = SettingsConfigDict(
        env_file="../",
        env_file_encoding="utf-8",
    )


settings = Settings()