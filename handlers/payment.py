from aiogram import Router, types, F
from aiogram.types import CallbackQuery
from keyboards.payment_kb import subscription_period_kb
from services.payments import create_payment, cancel_payment

from database.orm import SyncOrm

router = Router()

# Кнопка "Оплатить подписку"
@router.message(F.text == "💳 Оплатить подписку")
async def choose_subscription(message: types.Message):
    await message.answer(
        "Выберите срок подписки:",
        reply_markup=subscription_period_kb()
    )


# Пользователь выбрал срок
@router.callback_query(F.data.startswith("pay_months_"))
async def process_payment_choice(callback: CallbackQuery):
    months = int(callback.data.split("_")[-1])
    user_id = callback.from_user.id

    payment = await SyncOrm.create_transaction(user_id, months)

    await callback.message.edit_text(
        f"🔗 Ваш временный адрес для оплаты ({months} мес):\n\n"
        f"`{payment['address']}`\n\n"
        f"💰 Сумма: {payment['amount']} SOL\n"
        f"⏰ Время действия: 30 минут\n\n"
        f"После оплаты бот автоматически подтвердит вашу подписку.",
        parse_mode="Markdown"
    )


# Отмена
@router.callback_query(F.data == "cancel_payment")
async def cancel_payment_handler(callback: CallbackQuery):
    user_id = callback.from_user.id
    await cancel_payment(user_id)
    await callback.message.edit_text("❌ Оплата отменена.")
