import pytest
from app.services import get_root_message, create_user
from app.schemas import CreateUserSchema
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

def test_get_root_message():
    result = get_root_message()
    assert result == {"message": "Welcome to the Messenger API"}

@pytest.mark.asyncio
async def test_create_user_service(test_session: AsyncSession):
    unique_email = f"testuser_{uuid.uuid4()}@example.com"
    test_user = CreateUserSchema(username="testuser_service", email=unique_email)
    new_user = await create_user(test_session, test_user)

    assert new_user.id is not None
    assert new_user.username == "testuser_service"
    assert new_user.email == unique_email
    