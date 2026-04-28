from pydantic import BaseModel, Field


class CustomerData(BaseModel):
    customer_id: int = Field(..., example=101)
    tenure: int = Field(..., ge=0, example=4)
    monthly_charges: float = Field(..., ge=0, example=85.5)
    total_charges: float = Field(..., ge=0, example=342.0)
    contract_type: str = Field(..., example="month-to-month")
    payment_method: str = Field(..., example="electronic_check")