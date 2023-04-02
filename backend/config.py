from pydantic import BaseSettings, RedisDsn


class Settings(BaseSettings):
    REDIS_URL: RedisDsn

    TURNSTILE_SECRET: str

    class Config:
        env_file = "./.env"

settings = Settings()