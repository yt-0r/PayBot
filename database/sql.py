from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

from config import settings

Base = declarative_base()

engine = create_engine(settings.DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

