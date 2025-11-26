from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

from config import settings
from database.models.address import Address
from database.models.group import Group
from database.models.subscription import Subscription

from database.sql import Base

engine = create_engine(settings.DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


from database.models import *



Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session() as session:
    session.add(Address(currency="SOL", address="84W4umT7ncLLWucA9TGAV3HxWRZsfqSckaEXHj4nYayc"))
    session.add(Address(currency="SOL", address="CxrVFW52F1w4pAS3MowPFWB6MHnSgbsHCJ6x8RRCsNHy"))

    # 84W4umT7ncLLWucA9TGAV3HxWRZsfqSckaEXHj4nYayc


    session.add(Subscription(name='TRIGGER', period_month=1, price=0.3))
    session.add(Subscription(name='TRIGGER + SOL DAO 2.0', period_month=3, price=0.5))
    session.add(Subscription(name='TRIGGER + SOL DAO 2.0', period_month=1000, price=1))

    session.add(Group(id=-1003281919218, name='TRIGGER'))
    session.add(Group(id=-1003236436475, name='SOL DAO 2.0'))
    session.add(Group(id=-1003407805563, name='ADMINS'))

    # trigger
    session.add(GroupSubscription(group_id=-1003281919218, subscription_id=1))
    session.add(GroupSubscription(group_id=-1003281919218, subscription_id=2))
    session.add(GroupSubscription(group_id=-1003281919218, subscription_id=3))

    #soldao
    session.add(GroupSubscription(group_id=-1003236436475, subscription_id=2))
    session.add(GroupSubscription(group_id=-1003236436475, subscription_id=3))

    #referral
    session.add(Referrer(id=2058516705, name='yt-0r'))


    session.commit()


