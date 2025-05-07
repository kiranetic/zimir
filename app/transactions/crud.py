from sqlalchemy.orm import Session
from app.transactions.models import Transaction
from app.transactions.schemas import TransactionCreate
from typing import List, Optional
from datetime import datetime

def create_transaction(db: Session, transaction_data: TransactionCreate, user_id: int) -> Transaction:
    new_transaction = Transaction(**transaction_data.dict(), user_id=user_id)
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

def get_transaction_by_id(db: Session, transaction_id: int) -> Optional[Transaction]:
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def get_all_transactions(db: Session, user_id: int):
    return db.query(Transaction).filter(Transaction.user_id == user_id).order_by(Transaction.transaction_date.desc()).all()
