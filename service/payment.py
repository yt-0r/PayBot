from datetime import datetime, timedelta

from config import settings
from database.models import Transaction
from database.orm import SyncOrm
from utils.payment_checker import get_balance
from utils.exceptions import NotFreeAddress, AddressInWork


async def create_payment(user_id: int, subscription_id: int, price: int, percent: float):

    transaction: Transaction = SyncOrm.get_pending_transaction_for_user(user_id)

    if transaction:
        raise AddressInWork('У вас уже есть заявка на оплату в работе')

    address =  SyncOrm.get_free_address()
    user =  SyncOrm.get_user(user_id)

    if not address:
        raise NotFreeAddress("Нет доступных адресов для оплаты")

    # ФИКСИРУЕМ БАЛАНС
    address_balance = get_balance(address.address)

    address.is_busy = True
    address.balance = address_balance
    user.id_address = address.id

    SyncOrm.update_user(user)
    SyncOrm.update_address(address)


    payment_time = datetime.utcnow() + timedelta(minutes=settings.PAYMENT_TIME)
    SyncOrm.create_transaction(user_id=user.id, address_id=address.id, subscription_id=subscription_id, expires_at=payment_time, percent=percent)
    return {"address": address.address, "price": price}


async def cancel_payment(user_id: int):
    user = SyncOrm.get_user(user_id)
    if user:
        address = SyncOrm.get_address(user.id_address)
        if address:
            address.is_busy = False
            SyncOrm.update_address(address)
        user.id_address = None
        SyncOrm.update_user(user)

    transaction = SyncOrm.get_pending_transaction_for_user(user_id)
    if transaction:
        transaction.status = 'cancelled'
        SyncOrm.update_transaction(transaction)

    return True


