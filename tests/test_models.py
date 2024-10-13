import uuid
import pytest
from sqlalchemy.exc import IntegrityError
from app.models import User

@pytest.mark.asyncio
async def test_create_user_model(test_session):
    unique_email = f"testuser_{uuid.uuid4()}@example.com"
    new_user = User(username=f"testmodeluser_{uuid.uuid4()}", email=unique_email)  # Ensure unique username
    
    test_session.add(new_user)
    
    await test_session.commit()
    
    try:
        await test_session.refresh(new_user)
    except Exception as e:
        pytest.fail(f"Failed to refresh user instance: {e}")
    
    assert new_user.id is not None
    assert new_user.email == unique_email

@pytest.mark.asyncio
async def test_unique_constraints(test_session):
    unique_username = f"testuser_{uuid.uuid4()}"
    unique_email = f"testuser_{uuid.uuid4()}@example.com"

    duplicate_user = User(username=unique_username, email=unique_email)
    test_session.add(duplicate_user)
    await test_session.commit()

    duplicate_user_2 = User(username=unique_username, email=unique_email)
    test_session.add(duplicate_user_2)

    with pytest.raises(IntegrityError):
        await test_session.commit()
