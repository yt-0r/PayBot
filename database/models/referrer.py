from datetime import datetime

from sqlalchemy import BigInteger, Column, Integer, ForeignKey, DateTime, Boolean, String, Float
from sqlalchemy.orm import relationship

from database.sql import Base





class Referrer(Base):
    __tablename__ = 'referrers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, default='default')
    referrer_income = Column(Float, nullable=False, default=0)

    users = relationship("User", back_populates="referrer")
