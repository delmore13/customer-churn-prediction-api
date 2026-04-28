import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DATA_PATH = "data/churn.csv"
MODEL_PATH = "models/churn_model.joblib"


def train_model():
    df = pd.read_csv(DATA_PATH)

    X = df.drop(columns=["customer_id", "churn"])
    y = df["churn"]

    numeric_features = ["tenure", "monthly_charges", "total_charges"]
    categorical_features = ["contract_type", "payment_method"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ]
    )

    model = LogisticRegression()

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    pipeline.fit(X, y)

    joblib.dump(pipeline, MODEL_PATH)

    print("Model trained successfully.")
    print(f"Saved model to {MODEL_PATH}")


if __name__ == "__main__":
    train_model()