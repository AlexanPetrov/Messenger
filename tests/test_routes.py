import pytest

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Messenger API"}

def test_db_connection(client):
    response = client.get("/test-db")
    print(response.json())
    assert response.status_code == 200

    json_data = response.json()

    if "status" in json_data:
        assert json_data["status"] == "Database connection successful"
    elif "error" in json_data:
        pytest.fail(f"Database connection failed with error: {json_data['error']}")
    else:
        pytest.fail(f"Unexpected response: {json_data}")
