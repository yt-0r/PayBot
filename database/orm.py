from datetime import datetime, timedelta

from sqlalchemy import select

from database.models import User, Address, Transaction
from database.sql import Session


class SyncOrm:

    @staticmethod
    def add_user(user_id, username, fullname, referrer_id):
        with Session() as session:
            user = User(id=user_id, username=username,fullname=fullname, referrer_id=referrer_id)
            session.add(user)
            session.commit()

    @staticmethod
    def get_invited_count(referrer_id):
        with Session() as session:
            count = session.query(User).filter(User.referrer_id == referrer_id).count()
            return count

    @staticmethod
    def user_exist(user_id):
        with Session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            return user


    @staticmethod
    def get_sub_until(user_id):
        with Session() as session:
            subscription_until = session.query(User.subscription_until).filter(User.id == user_id).first()
            return subscription_until


    @staticmethod
    def get_free_address():
        with Session() as session:
            address = session.scalar(
                select(Address).where(Address.is_busy == False)
            )
            return address

    @staticmethod
    def create_transaction(user_id, address_id, currency, amount, months):
        with Session() as session:
            payment = Transaction(
                id_address=address_id,
                id_user=user_id,
                currency=currency,
                amount=amount,
                months=months,
                expires_at=datetime.utcnow() + timedelta(minutes=30)
            )

            session.add(payment)
            session.commit()

    @staticmethod
    def get_user(user_id):
        with Session() as session:
            return session.query(User).filter(User.id == user_id).first()

    @staticmethod
    def update_user(user: User):
        with Session() as session:
            session.commit()
            session.refresh(user)
            session.commit()

    @staticmethod
    def update_address(address: Address):
        with Session() as session:
            session.commit()
            session.refresh(address)
            session.commit()




