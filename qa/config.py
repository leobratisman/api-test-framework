from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra='allow',
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.',
    )

    API_BASE_URL: str
    API_AUTH_URL: str
    TIMEOUT: int

    TEST_DATA_DIR: str

    def file_path(self, filename: str) -> str:
        return str(self.TEST_DATA_DIR) + filename
    

settings = Settings()
