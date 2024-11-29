from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    VERSION: str
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int


model_config = SettingsConfigDict(
    env_file=".env",
    extra="ignore"
)


Config = Settings()
