from datetime import datetime, timedelta
from database.orm import SyncOrm


async def create_payment(user_id: int, months: int):


    address = await SyncOrm.get_free_address()
    user = await SyncOrm.get_user(user_id)

    if not address:
        raise Exception("Нет доступных адресов для оплаты")

    # Помечаем адрес как занятый
    address.is_busy = True
    user.id_address = address.id

    SyncOrm.update_user(user)
    SyncOrm.update_address(address)




    SyncOrm.create_transaction(user.id, address.id, months, 1, 'SOL', )

    payment = Payment(
        user_id=user_id,
        address_id=address.id,
        months=months,
        amount=amount,
        expires_at=datetime.utcnow() + timedelta(minutes=30)
    )

    session.add(payment)
    await session.commit()

    return {"address": address.address, "amount": amount}


async def cancel_payment(user_id: int):
    async with async_session() as session:
        # Находим активный платеж
        result = await session.execute(
            select(Payment).join(User).where(User.tg_id == user_id, Payment.status == "pending")
        )
        payment = result.scalar_one_or_none()

        if payment:
            # Освобождаем адрес
            address = await session.get(PaymentAddress, payment.address_id)
            address.in_use = False
            address.assigned_to = None
            address.assigned_until = None

            payment.status = "canceled"
            await session.commit()
