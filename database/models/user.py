from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean, String, Float
from sqlalchemy.orm import relationship

from database.sql import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    referrer_id = Column(Integer, ForeignKey("referrers.id"), nullable=True)
    id_address = Column(Integer, ForeignKey("addresses.id"), nullable=True)

    username = Column(String, index=True)
    fullname = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    subscription_until = Column(DateTime, nullable=True)

    is_active = Column(Boolean, default=True, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)

    referrer = relationship("Referrer", back_populates="users")
    address = relationship(
        "Address",
        back_populates="user",
        uselist=False,
        foreign_keys=[id_address]
    )

    transactions = relationship(
        "Transaction",
        back_populates="user"
    )

    users_subscriptions = relationship('UserSubscription', back_populates="user")