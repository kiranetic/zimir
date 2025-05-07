from pydantic import BaseModel, Field, condecimal
from typing import Optional
from datetime import datetime
from app.transactions.models import TransactionType

class TransactionBase(BaseModel):
    name: str = Field(..., max_length=50)
    notes: Optional[str] = Field(None, max_length=255)
    amount: condecimal(max_digits=10, decimal_places=2)
    type: TransactionType
    transaction_date: datetime

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
