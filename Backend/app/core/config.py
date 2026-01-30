from typing import List, Union
from pydantic_settings import BaseSettings
from pydantic import Field, field_validator


from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    PROJECT_NAME: str = "IssueLens"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = False
    
    # Security
    SECRET_KEY: str = Field(default="change-me-in-production")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8 # 8 days

    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    
    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def parse_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v
    
    # GitHub - Required for production
    GITHUB_TOKEN: str = Field(default="")
    GITHUB_WEBHOOK_SECRET: str = Field(default="")
    
    # AI Service - Required for production
    OPENAI_API_KEY: str = Field(default="")
    AI_MODEL: str = "gpt-4"
    
    # Database
    DATABASE_URL: str = "sqlite:///./issuelens.db"
    
    # Pathway
    PATHWAY_HOST: str = "localhost"
    PATHWAY_PORT: int = 8080
    
    model_config = {
        # "env_file": ".env", # Disabled due to pydantic-settings issue
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
        "extra": "ignore",
    }


settings = Settings()
