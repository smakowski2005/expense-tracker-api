from fastapi.testclient import TestClient
from app.main import app
import random

client = TestClient(app)

def test_create_user():
    random_id = random.randint(1, 100000)
    test_email = f"test_{random_id}@example.com"

    response = client.post("/users/",json={"email": test_email, "password": "strongpassword123"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == test_email
    assert "id" in data