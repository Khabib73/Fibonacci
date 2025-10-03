from fastapi.testclient import TestClient
from src.fibonacci.__main__ import app

client = TestClient(app)


def test_client():
    responce = client.get("/get_fib/30")
    assert responce.status_code == 200
    assert responce.json() == {"status": "success", "fibonacci_number": 832040}


def test_negative_number():
    responce = client.get("/get_fib/-30")
    assert responce.status_code == 400
