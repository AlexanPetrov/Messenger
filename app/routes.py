# Endpoints for application

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import check_db_connection, get_root_message, create_user
from app.schemas import CreateUserSchema, UserResponseSchema
from app.database import async_session


router = APIRouter()

# Dependency for getting the database session
async def get_db():
    async with async_session() as session:
        yield session

# Routes
@router.get("/test-db", summary="Test Database Connection", description="Database check endpoint.")
async def test_db(db: AsyncSession = Depends(get_db)):
    return await check_db_connection(db)

@router.get("/", summary="Read Root", description="Root endpoint.")
def read_root():
    return get_root_message()

@router.post("/users/", response_model=UserResponseSchema, status_code=201)
async def create_user_route(user: CreateUserSchema, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)
