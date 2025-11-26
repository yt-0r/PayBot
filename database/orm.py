from datetime import datetime, timedelta

from sqlalchemy import select, func, and_, or_
from sqlalchemy.orm import joinedload

from database.models import User, Address, Transaction, Subscription, Referrer, Group, GroupSubscription, \
    UserSubscription
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
    def get_sub_until1(user_id):
        with Session() as session:
            subscriptions_status = (
                session.query(
                    Subscription.name,
                    Subscription.period_month,
                    UserSubscription.until
                )
                .join(UserSubscription, UserSubscription.subscription_id == Subscription.id)
                .join(User, User.id == UserSubscription.user_id)
                .filter(User.id == user_id)
                .filter(UserSubscription.status == 'Active')
                .filter(UserSubscription.until >= datetime.utcnow())
                .all()
            )
            return subscriptions_status

    @staticmethod
    def get_sub_until(user_id):
        with Session() as session:
            subscriptions_status = session.query(User.subscription_until).filter(User.id == user_id).first()
            return subscriptions_status

    @staticmethod
    def get_free_address():
        with Session() as session:
            address = session.scalar(
                select(Address).where(Address.is_busy == False)
            )
            return address

    @staticmethod
    def get_addresses():
        with Session() as session:
            addresses = session.query(Address).all()
            return addresses

    @staticmethod
    def create_transaction(user_id, address_id, subscription_id,expires_at, percent):
        with Session() as session:
            payment = Transaction(
                id_address=address_id,
                id_user=user_id,
                id_subscription=subscription_id,
                expires_at=expires_at,
                referrer_percent=percent,
            )

            session.add(payment)
            session.commit()

    @staticmethod
    def get_user(user_id):
        with Session() as session:
            return session.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_referrer(referrer_id):
        with Session() as session:
            return session.query(Referrer).filter(Referrer.id == referrer_id).first()


    @staticmethod
    def update_user(user: User):
        with Session() as session:
            session.merge(user)
            session.commit()

    @staticmethod
    def update_address(address: Address):
        with Session() as session:
            session.merge(address)
            session.commit()

    @staticmethod
    def update_transaction(transaction: Transaction):
        with Session() as session:
            session.merge(transaction)
            session.commit()


    @staticmethod
    def get_pending_transaction_for_user(user_id):
        with Session() as session:
            transaction = session.query(Transaction).filter(Transaction.id_user == user_id, Transaction.status == 'pending').first()
            return transaction

    @staticmethod
    def get_address(address_id):
        with Session() as session:
            address = session.query(Address).filter(Address.id == address_id).first()
            return address

    @staticmethod
    def get_address_by_address(address):
        with Session() as session:
            address = session.query(Address).filter(Address.address == address).scalar()
            return address


    @staticmethod
    def get_pending_transactions():
        with Session() as session:
            pending_transactions = (
                session.query(Transaction)
                .options(
                    joinedload(Transaction.user),  # подтянуть User
                    joinedload(Transaction.address),  # подтянуть Address
                    joinedload(Transaction.subscription)  # подтянуть Subscription
                )
                .filter(Transaction.status == "pending")
                .all()
            )
            return pending_transactions

    @staticmethod
    def get_balance(id_address):
        with Session() as session:
            return session.query(Address.balance).filter(Address.id == id_address).scalar()


    @staticmethod
    def get_referrer_income(referrer_id):
        with Session() as session:
            result = (
                session.query(
                    Subscription.price,
                    Transaction.referrer_percent
                )
                .join(Transaction, Transaction.id_subscription == Subscription.id)
                .join(User, User.id == Transaction.id_user)
                .filter(User.referrer_id == referrer_id)
                .filter(User.id != referrer_id)
                .filter(Transaction.status == "paid")
                .all()
            )

            return result


    @staticmethod
    def get_referrer_count(referrer_id):
        with Session() as session:
            count = session.query(User).filter(User.referrer_id == referrer_id).count()
            return count



    @staticmethod
    def get_users_with_subscription():
        with Session() as session:
            users = session.query(User).filter(User.subscription_until != None).all()
            return users


    @staticmethod
    def get_subscription(sub_id: int):
        with Session() as session:
            query = select(Subscription).where(Subscription.id == sub_id)
            sub = session.execute(query).scalar()
            return sub

    @staticmethod
    def get_partner_id(name):
        with Session() as session:
            query = select(Referrer.id).where(Referrer.name == name)
            referrer_id = session.execute(query).scalar()
            return referrer_id


    @staticmethod
    def add_referral(user_id):
        with Session() as session:
            referral = Referrer(id=user_id)
            session.merge(referral)
            session.commit()

    @staticmethod
    def get_success_transaction_user(id_user):
        with Session() as session:
            query = select(Transaction).where(and_(Transaction.id_user == id_user, Transaction.status == 'paid'))
            transactions = session.execute(query).scalars().all()
            return transactions

    @staticmethod
    def get_groups(subscription_id):
        with Session() as session:
            groups = (
                session.query(Group)
                .join(GroupSubscription, Group.id == GroupSubscription.group_id)
                .filter(GroupSubscription.subscription_id == subscription_id)
                .all()
            )

            return groups


    @staticmethod
    def get_user_subscriptions(user_id):
        with Session() as session:
            query = select(UserSubscription).where(and_(UserSubscription.user_id == user_id, UserSubscription.status == 'Active'))
            user_subscription = session.execute(query).scalar()
            return user_subscription

    @staticmethod
    def update_user_subscription(subscription_id, user_id, new_subscription_until):
        with Session() as session:
            session.merge(UserSubscription(subscription_id=subscription_id, user_id=user_id, until=new_subscription_until, status='Active'))
            session.commit()

    @staticmethod
    def update_user_subscription2(id1, subscription_id, user_id, new_subscription_until):
        with Session() as session:
            session.merge(UserSubscription(id=id1, subscription_id=subscription_id, user_id=user_id, until=new_subscription_until, status='Active'))
            session.commit()

    @staticmethod
    def update_user_subscription3(id1, subscription_id, user_id, new_subscription_until):
        with Session() as session:
            session.merge(
                UserSubscription(id=id1, subscription_id=subscription_id, user_id=user_id, until=new_subscription_until, status='Inactive'))
            session.commit()




    @staticmethod
    def get_group_ids(user_id):
        with Session() as session:
            groups = (
                session.query(Group.id)
                .join(GroupSubscription, Group.id == GroupSubscription.group_id)
                .join(UserSubscription, GroupSubscription.subscription_id == UserSubscription.subscription_id)
                .filter(
                    UserSubscription.user_id == user_id,
                    UserSubscription.status == 'Active',
                )
                .all()
            )
            return groups

    @staticmethod
    def get_referrer_remove(referrer_id):
        with Session() as session:
            res = session.query(Referrer.referrer_income).filter(Referrer.id == referrer_id).scalar()
            return res

    @staticmethod
    def get_prices():
        with Session() as session:
            subscriptions = session.query(Subscription).all()
            return subscriptions

    @staticmethod
    def is_admin(user_id: int) -> bool:
        with Session() as session:
            user = session.get(User, user_id)
            return user and user.is_admin

    @staticmethod
    def add_address(addr):
        with Session() as session:
            session.add(Address(address=addr, currency='SOL'))
            session.commit()

    @staticmethod
    def delete_address(addr):
        with Session() as session:
            session.query(Address).filter(Address.address == addr).delete()
            session.commit()





