from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise EnvironmentError("DATABASE_URL environment variable is not set in the .env file.")

# Manage db connections & execute SQL queries asynchronously with SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True)

# Interact w/ db asynchronously (e.g., to perform CRUD operations)
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)
