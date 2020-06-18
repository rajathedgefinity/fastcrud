from pydantic import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str
    API_V1_STR: str = "/api/v1"

    class Config:
        case_sensite = True


settings = Settings()
