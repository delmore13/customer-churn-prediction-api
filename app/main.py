import logging

from fastapi import FastAPI, File, UploadFile

from app.schemas import CustomerData, PredictionResponse
from app.services.prediction_service import (
    predict_customer_batch,
    predict_single_customer,
)


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


@app.post("/predict", response_model=PredictionResponse)
def predict_churn(customer: CustomerData):
    return predict_single_customer(customer)


@app.post("/predict/batch")
async def predict_batch(file: UploadFile = File(...)):
    return await predict_customer_batch(file)