from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .services import check_db_connection, get_root_message
from .database import async_session

# Create a router
router = APIRouter()

# Dependency for getting the database session
async def get_db():
    async with async_session() as session:
        yield session

# Route to check the database connection
@router.get("/test-db", summary="Test Database Connection", description="Database check endpoint.")
async def test_db(db: AsyncSession = Depends(get_db)):
    return await check_db_connection(db)

# Root endpoint
@router.get("/", summary="Read Root", description="Root endpoint.")
def read_root():
    return get_root_message()
