from sqlalchemy import Column, BigInteger, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref

from database.sql import Base


class Coupon(Base):
    __tablename__ = "coupons"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_subscription = Column(Integer, ForeignKey("subscriptions.id"))
    name = Column(String)
    expires_at = Column(DateTime)

    subscription = relationship("Subscription", back_populates="coupon")