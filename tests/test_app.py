import sys
from pathlib import Path

from fastapi.testclient import TestClient


ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["model_loaded"] is True


def test_predict_churn():
    sample_customer = {
        "customer_id": 101,
        "tenure": 4,
        "monthly_charges": 85.5,
        "total_charges": 342.0,
        "contract_type": "month-to-month",
        "payment_method": "electronic_check"
    }

    response = client.post("/predict", json=sample_customer)
    data = response.json()

    assert response.status_code == 200
    assert data["customer_id"] == 101
    assert "prediction" in data
    assert "churn_risk" in data
    assert "churn_probability" in data