from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    #defines the database connection URL.
    DATABASE_URL:str


    #configures how application settings are loaded
    model_config=SettingsConfigDict(
        env_file=".env",
        extra="ignore"        
    )

#creates a Settings instance and loads the configuration values.
settings=Settings()
