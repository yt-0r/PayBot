from datetime import datetime

from sqlalchemy import BigInteger, Column, Integer, ForeignKey, DateTime, Boolean, String, Float
from sqlalchemy.orm import relationship
from database.sql import Base

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    currency = Column(String, nullable=False)
    address = Column(String, nullable=False)
    balance = Column(Float, nullable=False, default=0)
    is_busy = Column(Boolean, nullable=False, default=False)

    user = relationship(
        "User",
        back_populates="address",
    )

    transactions = relationship(
        "Transaction",
        back_populates="address"
    )