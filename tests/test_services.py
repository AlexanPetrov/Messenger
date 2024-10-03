import pytest
from app.services import get_root_message

def test_get_root_message():
    result = get_root_message()
    assert result == {"message": "Welcome to the Messenger API"}
