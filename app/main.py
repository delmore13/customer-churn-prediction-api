import logging

import joblib
import pandas as pd
from fastapi import FastAPI
from app.schemas import CustomerData


MODEL_PATH = "models/churn_model.joblib"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


app = FastAPI(
    title="Customer Churn Prediction API",
    description="Production-style API for predicting customer churn risk.",
    version="1.0.0"
)

logger.info("Loading churn prediction model from %s", MODEL_PATH)
model = joblib.load(MODEL_PATH)
logger.info("Model loaded successfully")


@app.get("/")
def home():
    logger.info("Home endpoint accessed")
    return {
        "message": "Customer Churn Prediction API is running",
        "status": "healthy"
    }


@app.get("/health")
def health_check():
    logger.info("Health check endpoint accessed")
    return {
        "status": "ok",
        "model_loaded": True
    }


@app.post("/predict")
def predict_churn(customer: CustomerData):
    logger.info("Prediction request received for customer_id=%s", customer.customer_id)

    input_data = pd.DataFrame([customer.model_dump()])

    prediction = model.predict(input_data)[0]

    probability = None
    if hasattr(model, "predict_proba"):
        probability = float(model.predict_proba(input_data)[0][1])

    churn_risk = "High" if int(prediction) == 1 else "Low"

    logger.info(
        "Prediction completed | customer_id=%s | prediction=%s | churn_risk=%s | probability=%s",
        customer.customer_id,
        int(prediction),
        churn_risk,
        probability
    )

    return {
        "customer_id": customer.customer_id,
        "prediction": int(prediction),
        "churn_risk": churn_risk,
        "churn_probability": probability
    }