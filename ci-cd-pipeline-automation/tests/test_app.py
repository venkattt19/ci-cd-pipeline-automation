from app.app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "UP"

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "CI/CD Pipeline Automation demo" in response.get_json()["message"]
