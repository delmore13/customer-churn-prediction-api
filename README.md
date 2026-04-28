# Customer Churn Prediction API

## Project Summary

This project is a production-style machine learning API that predicts whether a customer is likely to churn.

The project demonstrates an end-to-end machine learning workflow, including data preparation, model training, model serialization, API development, input validation, real-time prediction, and automated API testing.

## Business Problem

Customer churn happens when customers stop using a company's product or service. Predicting churn helps a business identify customers who may leave, allowing the company to take action before losing revenue.

This API receives customer information and returns a churn prediction, churn risk label, and churn probability score.

## Tech Stack

* Python
* Pandas
* Scikit-learn
* Joblib
* FastAPI
* Pydantic
* Uvicorn
* Pytest
* HTTPX

## Project Structure

customer\_churn\_api/

* app/

  * **init**.py
  * main.py
  * schemas.py
* data/

  * churn.csv
* models/

  * churn\_model.joblib
* screenshots/

  * project1\_predict\_success.png.jpg
  * project1\_pytest\_success.png
* src/

  * app.py
  * schema.py
  * train.py
* tests/

  * test\_app.py
* README.md
* requirements.txt

## Features

* Trains a machine learning model to predict customer churn
* Saves the trained model as a reusable model artifact
* Loads the trained model inside a FastAPI application
* Validates incoming customer data using Pydantic
* Provides a real-time prediction endpoint
* Returns churn prediction, risk label, and probability score
* Includes a health check endpoint
* Includes automated API tests using Pytest

## API Endpoints

### Home Endpoint

GET /

Returns a basic message confirming the API is running.

### Health Check Endpoint

GET /health

Example response:

{
"status": "ok",
"model\_loaded": true
}

### Prediction Endpoint

POST /predict

Example request:

{
"customer\_id": 101,
"tenure": 4,
"monthly\_charges": 85.5,
"total\_charges": 342.0,
"contract\_type": "month-to-month",
"payment\_method": "electronic\_check"
}

Example response:

{
"customer\_id": 101,
"prediction": 1,
"churn\_risk": "High",
"churn\_probability": 0.900737490821496
}

## How to Run the Project

1. Open the project folder:

cd customer\_churn\_api

2. Activate the virtual environment:

venv\\Scripts\\activate

3. Install dependencies:

pip install -r requirements.txt

4. Train the model:

python src\\train.py

5. Run the API:

uvicorn app.main:app --reload

6. Open the interactive API documentation:

http://127.0.0.1:8000/docs

## Testing

Run automated tests with:

pytest

The test suite verifies that:

* The health check endpoint returns a successful response
* The model-loaded status is returned
* The prediction endpoint accepts valid customer data
* The prediction response includes the expected output fields

Example successful test result:

2 passed

## Screenshots

Prediction response screenshot:

screenshots/project1\_predict\_success.png.jpg

Automated test success screenshot:

screenshots/project1\_pytest\_success.png

## What I Learned

This project helped me understand how to move a machine learning model from a simple training script into a real API service.

I learned how to prepare a dataset, train a classification model, save a trained model with Joblib, load it inside FastAPI, validate incoming API requests with Pydantic, return real-time ML predictions, and test API endpoints with Pytest.

## Why This Project Matters

This project demonstrates the foundation of production machine learning.

Instead of only training a model in a notebook, this project turns the model into a working API that another application, dashboard, or business system could use.

## Future Improvements

* Dockerizing the application
* Adding batch CSV prediction support
* Building a dashboard for non-technical users
* Adding SHAP explainability
* Adding structured logging
* Adding monitoring
* Deploying the API to the cloud
* Adding GitHub Actions for automated testing

