import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Settings:
    # For current use in the code
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    
    # Test database settings
    TEST_DATABASE_URL: str = os.getenv("TEST_DATABASE_URL")
    
    # These are currently used by Docker Compose but could be useful later in the code
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")

settings = Settings()
