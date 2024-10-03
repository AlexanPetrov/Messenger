from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

async def check_db_connection(db: AsyncSession):
    try:
        result = await db.execute(text("SELECT 1"))
        return {"status": "Database connection successful", "result": result.scalar()}
    except Exception as e:
        return {"error": str(e)}

def get_root_message():
    return {"message": "Welcome to the Messenger API"}
