import pytest
import uuid

@pytest.mark.asyncio
async def test_read_root(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Messenger API"}

@pytest.mark.asyncio
async def test_db_connection(client):
    response = await client.get("/test-db")
    assert response.status_code == 200

    json_data = response.json()

    if "status" in json_data:
        assert json_data["status"] == "Database connection successful"
    elif "error" in json_data:
        pytest.fail(f"Database connection failed with error: {json_data['error']}")
    else:
        pytest.fail(f"Unexpected response: {json_data}")

@pytest.mark.asyncio
async def test_create_user(client):
    test_user = {
    "username": f"testuser_{uuid.uuid4()}",
    "email": f"testuser_{uuid.uuid4()}@example.com"
}

    response = await client.post("/users/", json=test_user)
    assert response.status_code == 201
    user_data = response.json()
    assert user_data["username"].startswith("testuser")
    assert user_data["email"].startswith("testuser_") and user_data["email"].endswith("@example.com")

@pytest.mark.asyncio
async def test_rate_limiter(client):
    # Generate a new user with a unique email using uuid
    base_email = f"testuser_{uuid.uuid4()}@example.com"
    base_user = {"username": f"testuser_{uuid.uuid4()}", "email": base_email}

    # Make 5 successful requests with unique emails to bypass the unique constraint
    for _ in range(5):
        test_user = {
            "username": f"testuser_{uuid.uuid4()}",
            "email": f"testuser_{uuid.uuid4()}@example.com"
        }
        response = await client.post("/users/", json=test_user)
        assert response.status_code == 201

    # The 6th request should fail due to rate limiting, using the base_email and base_user
    response = await client.post("/users/", json=base_user)
    assert response.status_code == 429
    assert response.json() == {"message": "Rate limit exceeded"}
    