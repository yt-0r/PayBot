from datetime import datetime

from sqlalchemy import BigInteger, Column, Integer, ForeignKey, DateTime, Boolean, String
from sqlalchemy.orm import relationship

from database.sql import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, unique=True, index=True)
    referrer_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    id_address = Column(Integer, ForeignKey("addresses.id"), nullable=True)


    username = Column(String, index=True)
    fullname = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    subscription_until = Column(DateTime, nullable=True)

    is_active = Column(Boolean, default=True, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)

    referral_income = Column(Integer, nullable=True, default=0)

    referrer = relationship("User", remote_side=[id])
    address = relationship("Address", back_populates="users")

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(BigInteger, primary_key=True, unique=True, index=True, autoincrement=True)
    currency = Column(String, nullable=False)
    address = Column(String, nullable=False)

    is_busy = Column(Boolean, nullable=False, default=False)
    id_user = Column(BigInteger, ForeignKey("users.id"), nullable=True)

    user = relationship("User", back_populates="addresses")

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(BigInteger, primary_key=True, unique=True, index=True, autoincrement=True)
    id_address = Column(Integer, ForeignKey("addresses.id"), nullable=True)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=True)

    currency = Column(String, nullable=True)
    amount = Column(BigInteger, nullable=True)
    months = Column(Integer, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)

    status = Column(String, nullable=True, default="pending")

    address = relationship("Address", back_populates="transactions")
    user = relationship("User", back_populates="transactions")
