from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.transactions.schemas import TransactionCreate, TransactionResponse
from app.transactions.crud import (
    create_transaction,
    get_all_transactions,
    get_transaction_by_id
)

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.post("/", response_model=TransactionResponse)
def create_transaction_endpoint(transaction_data: TransactionCreate, db: Session = Depends(get_db), user_id: int = 1):
    return create_transaction(db, transaction_data, user_id = 1)

@router.get("/", response_model=List[TransactionResponse])
def get_all_transactions_endpoint(db: Session = Depends(get_db), user_id: int = 1):
    return get_all_transactions(db=db, user_id=user_id)

@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_single_transaction_endpoint(transaction_id: int, db: Session = Depends(get_db), user_id: int = 1):
    transaction = get_transaction_by_id(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=400, detail="Transaction not found")
    return transaction
