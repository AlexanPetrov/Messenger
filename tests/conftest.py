import pytest
import httpx
from app.main import app
from app.database import async_session as session_factory
from dotenv import load_dotenv
import os
import asyncio
from sqlalchemy import text

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

if not BASE_URL:
    raise EnvironmentError("BASE_URL environment variable is not set in the .env file.")

@pytest.fixture
async def client():
    async with httpx.AsyncClient(app=app, base_url=BASE_URL) as c:
        yield c
            
@pytest.fixture(scope="function")
async def test_session():
    async with session_factory() as session:
        print(f"Creating session with ID: {id(session)}")
        await session.begin_nested()
        try:
            yield session
        finally:
            await session.rollback()
            print(f"Rolling back session with ID: {id(session)}")

@pytest.fixture(scope="session")
def event_loop():
    """Create a session-scoped event loop fixture to share across all tests."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(autouse=True)
async def clean_database():
    async with session_factory() as session:
        await session.execute(text("TRUNCATE TABLE users RESTART IDENTITY CASCADE"))
        await session.commit()
