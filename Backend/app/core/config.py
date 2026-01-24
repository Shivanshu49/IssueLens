from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    PROJECT_NAME: str = "IssueLens"
    API_V1_STR: str = "/api/v1"
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    
    # GitHub
    GITHUB_TOKEN: str = ""
    GITHUB_WEBHOOK_SECRET: str = ""
    
    # AI Service
    OPENAI_API_KEY: str = ""
    AI_MODEL: str = "gpt-4"
    
    # Database (optional for later)
    DATABASE_URL: str = "sqlite:///./issuelens.db"
    
    # Pathway
    PATHWAY_HOST: str = "localhost"
    PATHWAY_PORT: int = 8080
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
