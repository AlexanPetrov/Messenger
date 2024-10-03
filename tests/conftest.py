import sys
import os
import pytest
from fastapi.testclient import TestClient

# Project root directory added to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app

# Fixture to create a test client for FastAPI
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
