\# Customer Churn Prediction API



A production-style machine learning API that predicts whether a customer is likely to churn based on customer account and billing information.



This project demonstrates an end-to-end ML deployment workflow using FastAPI, a trained machine learning model, schema validation, automated testing, structured logging, batch prediction, modular service architecture, and Docker support.



\---



\## Project Overview



Customer churn is a major business problem for subscription-based companies. This API allows a business to score individual customers or upload a CSV file for batch churn prediction.



The goal is to show how a machine learning model can be wrapped inside a clean, testable, production-style API.



\---



\## Features



\- Single-customer churn prediction endpoint

\- Batch CSV prediction endpoint

\- FastAPI interactive Swagger documentation

\- Pydantic request and response validation

\- Structured API logging

\- Professional error handling

\- Automated API tests with pytest

\- Docker support for containerized deployment

\- Modular service-layer architecture



\---



\## Tech Stack



\- Python

\- FastAPI

\- Pydantic

\- pandas

\- scikit-learn

\- joblib

\- pytest

\- Uvicorn

\- Docker



\---



\## Project Structure



```text

customer\_churn\_api/

│

├── app/

│   ├── main.py

│   ├── schemas.py

│   └── services/

│       ├── \_\_init\_\_.py

│       └── prediction\_service.py

│

├── models/

│   └── churn\_model.joblib

│

├── tests/

│   ├── conftest.py

│   ├── test\_api.py

│   └── test\_app.py

│

├── sample\_customers.csv

├── requirements.txt

├── Dockerfile

├── .dockerignore

└── README.md

```



\---



\## API Endpoints



| Method | Endpoint         | Description                                          |

| ------ | ---------------- | ---------------------------------------------------- |

| GET    | `/`              | API home/status message                              |

| GET    | `/health`        | Health check endpoint                                |

| POST   | `/predict`       | Predict churn for one customer                       |

| POST   | `/predict/batch` | Predict churn for multiple customers from a CSV file |



\---



\## Example Single Prediction Request



```json

{

&#x20; "customer\_id": 101,

&#x20; "tenure": 4,

&#x20; "monthly\_charges": 85.5,

&#x20; "total\_charges": 342.0,

&#x20; "contract\_type": "month-to-month",

&#x20; "payment\_method": "electronic\_check"

}

```



\## Example Single Prediction Response



```json

{

&#x20; "customer\_id": 101,

&#x20; "prediction": 1,

&#x20; "churn\_risk": "High",

&#x20; "churn\_probability": 0.900737490821496

}

```



\---



\## Batch Prediction CSV Format



The batch endpoint accepts a CSV file with these columns:



```csv

customer\_id,tenure,monthly\_charges,total\_charges,contract\_type,payment\_method

101,4,85.5,342.0,month-to-month,electronic\_check

102,24,65.0,1560.0,one\_year,credit\_card

103,2,95.0,190.0,month-to-month,electronic\_check

```



\---



\## Run Locally



Create and activate a virtual environment:



```powershell

python -m venv venv

.\\venv\\Scripts\\activate

```



Install dependencies:



```powershell

pip install -r requirements.txt

```



Run the API:



```powershell

python -m uvicorn app.main:app --reload

```



Open Swagger docs:



```text

http://127.0.0.1:8000/docs

```



\---



\## Run Tests



```powershell

python -m pytest

```



Expected result:



```text

5 passed

```



\---



\## Run with Docker



Build the Docker image:



```powershell

docker build -t customer-churn-api .

```



Run the container:



```powershell

docker run -p 8000:8000 customer-churn-api

```



Open Swagger docs:



```text

http://127.0.0.1:8000/docs

```



\---



\## What This Project Demonstrates



This project demonstrates core production ML engineering skills:



\- Turning a trained ML model into an API service

\- Designing request and response schemas

\- Validating user input with Pydantic

\- Handling single and batch predictions

\- Writing automated API tests

\- Adding structured logs for observability

\- Separating API routes from prediction logic

\- Preparing an application for containerized deployment



\---



\## Future Improvements



\- Add GitHub Actions CI for automated test runs

\- Add model explainability with SHAP or feature importance

\- Add MLflow experiment tracking

\- Add authentication for protected API access

\- Deploy the API to a cloud platform

