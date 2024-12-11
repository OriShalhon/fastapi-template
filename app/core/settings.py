from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_expiration_time_minutes: int
    testing_database_url: str

    class config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
