from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    BOT_TAG: str

    ADMINISTRATOR: str

    DB_IP: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    LOG_LEVEL: str




    @property
    def DATABASE_URL(self) -> str:
        return f"sqlite:///{self.DB_NAME}"
        # return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_IP}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"


settings = Settings()

