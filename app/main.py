from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from .database import async_session

app = FastAPI()

async def get_db():
    async with async_session() as session:
        yield session

@app.get("/test-db", summary="Test Database Connection", description="Database check endpoint.")
async def test_db(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 1"))
        return {"status": "Database connection successful", "result": result.scalar()}
    except Exception as e:
        return {"error": str(e)}

@app.get("/", summary="Read Root", description="Root endpoint.")
def read_root():
    return {"message": "Welcome to the Messenger API"}
