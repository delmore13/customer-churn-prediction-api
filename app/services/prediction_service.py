import logging
from io import StringIO

import joblib
import pandas as pd
from fastapi import HTTPException, UploadFile

from app.schemas import CustomerData


MODEL_PATH = "models/churn_model.joblib"

logger = logging.getLogger(__name__)

logger.info("Loading churn prediction model from %s", MODEL_PATH)
model = joblib.load(MODEL_PATH)
logger.info("Model loaded successfully")


def predict_single_customer(customer: CustomerData):
    logger.info("Prediction request received for customer_id=%s", customer.customer_id)

    try:
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

    except Exception as error:
        logger.exception(
            "Prediction failed for customer_id=%s | error=%s",
            customer.customer_id,
            str(error)
        )
        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Please check input data or model service."
        )


async def predict_customer_batch(file: UploadFile):
    logger.info("Batch prediction request received | filename=%s", file.filename)

    if not file.filename.endswith(".csv"):
        logger.warning("Invalid batch upload file type | filename=%s", file.filename)
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Please upload a CSV file."
        )

    try:
        contents = await file.read()
        csv_text = contents.decode("utf-8")
        input_data = pd.read_csv(StringIO(csv_text))

        required_columns = {
            "customer_id",
            "tenure",
            "monthly_charges",
            "total_charges",
            "contract_type",
            "payment_method"
        }

        missing_columns = required_columns - set(input_data.columns)

        if missing_columns:
            logger.warning("Batch prediction failed due to missing columns: %s", missing_columns)
            raise HTTPException(
                status_code=400,
                detail=f"Missing required columns: {sorted(missing_columns)}"
            )

        predictions = model.predict(input_data)

        probabilities = None
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(input_data)[:, 1]

        results = []

        for index, row in input_data.iterrows():
            prediction = int(predictions[index])
            probability = float(probabilities[index]) if probabilities is not None else None

            results.append(
                {
                    "customer_id": int(row["customer_id"]),
                    "prediction": prediction,
                    "churn_risk": "High" if prediction == 1 else "Low",
                    "churn_probability": probability
                }
            )

        logger.info("Batch prediction completed | records=%s", len(results))

        return {
            "filename": file.filename,
            "record_count": len(results),
            "predictions": results
        }

    except HTTPException:
        raise

    except Exception as error:
        logger.exception("Batch prediction failed | error=%s", str(error))
        raise HTTPException(
            status_code=500,
            detail="Batch prediction failed. Please check the CSV format or model service."
        )