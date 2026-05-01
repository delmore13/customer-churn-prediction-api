from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["model_loaded"] is True


def test_predict_endpoint():
    payload = {
        "customer_id": 101,
        "tenure": 4,
        "monthly_charges": 85.5,
        "total_charges": 342.0,
        "contract_type": "month-to-month",
        "payment_method": "electronic_check"
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["customer_id"] == 101
    assert "prediction" in data
    assert "churn_risk" in data
    assert "churn_probability" in data
    assert data["churn_risk"] in ["High", "Low"]
