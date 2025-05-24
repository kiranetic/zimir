from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.auth.dependencies import get_current_user
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
def create_transaction_endpoint(transaction_data: TransactionCreate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    return create_transaction(db, transaction_data, current_user)

@router.get("/", response_model=List[TransactionResponse])
def get_all_transactions_endpoint(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    return get_all_transactions(db, current_user)

@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_single_transaction_endpoint(transaction_id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    transaction = get_transaction_by_id(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=400, detail="Transaction not found")
    return transaction
