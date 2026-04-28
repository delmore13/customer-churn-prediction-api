import joblib
import pandas as pd
from fastapi import FastAPI
from app.schemas import CustomerData


MODEL_PATH = "models/churn_model.joblib"

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Production-style API for predicting customer churn risk.",
    version="1.0.0"
)

model = joblib.load(MODEL_PATH)


@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running",
        "status": "healthy"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "model_loaded": True
    }


@app.post("/predict")
def predict_churn(customer: CustomerData):
    input_data = pd.DataFrame([customer.model_dump()])

    prediction = model.predict(input_data)[0]

    probability = None
    if hasattr(model, "predict_proba"):
        probability = float(model.predict_proba(input_data)[0][1])

    churn_risk = "High" if int(prediction) == 1 else "Low"

    return {
        "customer_id": customer.customer_id,
        "prediction": int(prediction),
        "churn_risk": churn_risk,
        "churn_probability": probability
    }