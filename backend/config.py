from pydantic import BaseSettings, RedisDsn


class Settings(BaseSettings):
    REDIS_URL: RedisDsn

    TURNSTILE_SECRET_KEY: str

    class Config:
        env_file = "./.env"

settings = Settings()