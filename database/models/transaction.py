from datetime import datetime

from sqlalchemy import BigInteger, Column, Integer, ForeignKey, DateTime, Boolean, String, Float
from sqlalchemy.orm import relationship

from database.sql import Base



class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    id_address = Column(Integer, ForeignKey("addresses.id"), nullable=True)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=True)
    id_subscription = Column(Integer, ForeignKey("subscriptions.id"), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)

    status = Column(String, nullable=True, default="pending")
    referrer_percent = Column(Float, nullable=True, default=0)

    address = relationship("Address", back_populates="transactions")
    user = relationship("User", back_populates="transactions")
    subscription = relationship("Subscription", back_populates="transactions")

