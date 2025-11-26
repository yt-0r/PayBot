from datetime import datetime

from sqlalchemy import BigInteger, Column, Integer, ForeignKey, DateTime, Boolean, String, Float
from sqlalchemy.orm import relationship

from database.sql import Base






class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    name = Column(String)
    period_month = Column(Integer)
    price = Column(Integer)

    transactions = relationship("Transaction", back_populates="subscription")
    coupon = relationship("Coupon", back_populates="subscription")

    group_subscriptions = relationship("GroupSubscription",back_populates="subscription")
    users_subscriptions = relationship("UserSubscription", back_populates="subscription")

