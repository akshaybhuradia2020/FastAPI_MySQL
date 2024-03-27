from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Test Application"}


def test_create_user():
    response = client.post(
        "/signup/",
        json={
            "id": 112,
            "isactive": True,
            "gender": "female",
            "email": "nisha@gmail.com",
            "fullname": "nisha singh",
            "passwd": "123456",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 112,
        "isactive": True,
        "gender": "female",
        "email": "nisha@gmail.com",
        "fullname": "nisha singh",
        "passwd": "123456",
    }
