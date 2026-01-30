from fastapi.testclient import TestClient
from app.main import app
from app.db.session import SessionLocal
from app.models.user import User

client = TestClient(app)

def test_signup():
    response = client.post(
        "/api/v1/auth/signup",
        json={"email": "debug_user@example.com", "password": "password123"},
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    test_signup()
