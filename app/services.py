from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.models import User
from app.schemas import CreateUserSchema

async def check_db_connection(db: AsyncSession):
    try:
        result = await db.execute(text("SELECT 1"))
        return {"status": "Database connection successful", "result": result.scalar()}
    except Exception as e:
        return {"error": str(e)}

def get_root_message():
    return {"message": "Welcome to the Messenger API"}

async def create_user(db: AsyncSession, user: CreateUserSchema) -> User:
    new_user = User(username=user.username, email=user.email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
