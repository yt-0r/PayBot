from datetime import datetime

from sqlalchemy import BigInteger, Column, Integer, ForeignKey, DateTime, Boolean, String, Float
from sqlalchemy.orm import relationship

from database.sql import Base



class UserSubscription(Base):
    __tablename__ = 'users_subscriptions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subscription_id = Column(Integer, ForeignKey("subscriptions.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    until = Column(DateTime, nullable=True)
    status = Column(String, nullable=True)

    subscription = relationship("Subscription", back_populates="users_subscriptions")
    user = relationship("User", back_populates="users_subscriptions")