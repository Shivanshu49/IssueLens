from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Union
from pydantic import Field, field_validator
import os
import traceback

print(f"Current working directory: {os.getcwd()}")
print(f".env exists: {os.path.exists('.env')}")

try:
    print("Defining Settings class...")
    class Settings(BaseSettings):
        PROJECT_NAME: str = "IssueLens"
        # Removed env_file to test if BaseSettings works at all
        model_config = SettingsConfigDict(extra="ignore")

    print("Attempting to instantiate Settings...")
    settings = Settings()
    print("Settings loaded successfully!")
    print(settings.model_dump())

except Exception:
    print("FATAL ERROR TRACEBACK:")
    traceback.print_exc()
