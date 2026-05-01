from pydantic import BaseModel, Field, ConfigDict


class CustomerData(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "customer_id": 101,
                "tenure": 4,
                "monthly_charges": 85.5,
                "total_charges": 342.0,
                "contract_type": "month-to-month",
                "payment_method": "electronic_check"
            }
        }
    )

    customer_id: int = Field(..., ge=1, description="Unique customer identifier")
    tenure: int = Field(..., ge=0, description="Number of months the customer has stayed")
    monthly_charges: float = Field(..., ge=0, description="Customer monthly bill amount")
    total_charges: float = Field(..., ge=0, description="Total amount charged to the customer")
    contract_type: str = Field(..., description="Customer contract type")
    payment_method: str = Field(..., description="Customer payment method")
