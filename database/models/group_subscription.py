from datetime import datetime

from sqlalchemy import BigInteger, Column, Integer, ForeignKey, DateTime, Boolean, String, Float
from sqlalchemy.orm import relationship

from database.sql import Base



class GroupSubscription(Base):
    __tablename__ = 'groups_subscriptions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subscription_id = Column(Integer, ForeignKey("subscriptions.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))

    subscription = relationship("Subscription", back_populates="group_subscriptions")
    group = relationship("Group", back_populates="groups_subscriptions")