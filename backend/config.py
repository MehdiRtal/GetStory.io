from pydantic import BaseSettings, RedisDsn


class Settings(BaseSettings):
    SERVER_HOST: str
    SERVER_PORT: int

    REDIS_URL: RedisDsn

    TURNSTILE_SECRET: str

    class Config:
        env_file = "./.env"

settings = Settings()