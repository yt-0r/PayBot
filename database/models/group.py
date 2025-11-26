from datetime import datetime

from sqlalchemy import BigInteger, Column, Integer, ForeignKey, DateTime, Boolean, String, Float
from sqlalchemy.orm import relationship

from database.sql import Base






class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    groups_subscriptions = relationship(
        "GroupSubscription",
        back_populates="group"
    )
