from dotenv import load_dotenv, dotenv_values
import os
import traceback

print(f"Current working directory: {os.getcwd()}")
try:
    print("Loading .env using load_dotenv...")
    success = load_dotenv(verbose=True)
    print(f"load_dotenv result: {success}")
    
    print("Loading .env using dotenv_values...")
    config = dotenv_values(".env")
    print(f"dotenv_values result keys: {list(config.keys())}")
    
except Exception:
    traceback.print_exc()
