from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db.base import Base
import enum

class CategoryType(str, enum.Enum):
    EXPENSE = "expense"
    INCOME = "income"

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    type = Column(Enum(CategoryType), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    user = relationship("User", back_populates="categories")

    __table_args__ = (
        UniqueConstraint("user_id", "name", "type", name="unique_user_category"),
    )
