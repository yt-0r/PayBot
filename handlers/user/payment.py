import traceback

from aiogram import Router, types, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from config import settings
from database.models import Subscription, User, Referrer, Transaction
from database.orm import SyncOrm
from keyboards.cancel_kb import cancel_kb
from keyboards.main_kb import main_kb
from service.payment import create_payment, cancel_payment
from texts.wellcome_text import text
from utils.custom_callback import BuyPlanCallback
from utils.exceptions import NotFreeAddress, AddressInWork
from utils.log_config import bot_logger as logger
from utils.referrel_percent import referrer_percent

router = Router()


#
# @router.callback_query(BuyPlanCallback.filter())
# async def process_buy_plan(callback: CallbackQuery, callback_data: BuyPlanCallback):
#
#     subscription = callback_data.subscription
#
#     kb = InlineKeyboardMarkup(inline_keyboard=[
#         [
#             InlineKeyboardButton(
#                 text="Готов оплатить",
#                 callback_data=subscription
#             )
#         ],
#         [
#             InlineKeyboardButton(
#                 text="Назад",
#                 callback_data="back"
#             )
#         ]
#     ])
#
#     await callback.message.answer("Продающее сообщение", parse_mode="Markdown", reply_markup=kb)
#     await callback.answer()



@router.callback_query(F.data=="subscription_1")
async def crypto_selected1(callback: CallbackQuery):
    logger.info(f"{callback.from_user.username} {callback.from_user.id} press button {callback.data}")

    user_id = callback.from_user.id
    subscription_id = int(callback.data.split("_")[-1])

    try:
        subscription: Subscription = SyncOrm.get_subscription(subscription_id)
        user: User = SyncOrm.get_user(user_id)
        referrer: Referrer = SyncOrm.get_referrer(user.referrer_id)
        user_success_transactions: Transaction = SyncOrm.get_success_transaction_user(user.id)

        percent = referrer_percent(user, user_success_transactions, referrer, subscription.period_month)
        payment = await create_payment(user_id, subscription.id, subscription.price, percent)

        await callback.message.edit_text(
            f"🔗 Ваш адрес для оплаты USDT (SOL):\n\n"
            f"`{payment['address']}`\n\n"
            f"💰 Сумма: {payment['price']} USDT (SOL)\n\n"
            f"⏰ Адрес действует {settings.PAYMENT_TIME} минут.\n\n"
            f"После оплаты бот автоматически подтвердит подписку.",
            parse_mode="Markdown", reply_markup=cancel_kb()
        )

    except NotFreeAddress as e:
        await callback.message.answer(f"❌ {e}")
        logger.error(f"{callback.from_user.username} {callback.from_user.id} {str(e)} {traceback.format_exc()}")

    except AddressInWork as e:
        await callback.message.answer(f"❌ {e}")
        logger.error(f"{callback.from_user.username} {callback.from_user.id} {str(e)} {traceback.format_exc()}")

    except Exception as e:
        await callback.message.answer(f"❌ Произошла ошибка")
        logger.error(f"{callback.from_user.username} {callback.from_user.id} {str(e)} {traceback.format_exc()}")

    finally:
        await callback.answer()
        logger.info(f"{callback.from_user.username} {callback.from_user.id} create transaction")



@router.callback_query(F.data=="subscription_2")
async def crypto_selected2(callback: CallbackQuery):
    logger.info(f"{callback.from_user.username} {callback.from_user.id} press button {callback.data}")
    user_id = callback.from_user.id
    subscription_id = int(callback.data.split("_")[-1])

    try:
        subscription: Subscription = SyncOrm.get_subscription(subscription_id)
        user: User = SyncOrm.get_user(user_id)
        referrer: Referrer = SyncOrm.get_referrer(user.referrer_id)
        user_success_transactions: Transaction = SyncOrm.get_success_transaction_user(user.id)

        percent = referrer_percent(user, user_success_transactions, referrer, subscription.period_month)
        payment = await create_payment(user_id, subscription.id, subscription.price, percent)

        await callback.message.edit_text(
            f"🔗 Ваш адрес для оплаты USDT (SOL):\n\n"
            f"`{payment['address']}`\n\n"
            f"💰 Сумма: {payment['price']} USDT (SOL)\n\n"
            f"⏰ Адрес действует {settings.PAYMENT_TIME} минут.\n\n"
            f"После оплаты бот автоматически подтвердит подписку.",
            parse_mode="Markdown", reply_markup=cancel_kb()
        )

    except NotFreeAddress as e:
        await callback.message.answer(f"❌ {e}")
        logger.error(f"{callback.from_user.username} {callback.from_user.id} {str(e)} {traceback.format_exc()}")

    except AddressInWork as e:
        await callback.message.answer(f"❌ {e}")
        logger.error(f"{callback.from_user.username} {callback.from_user.id} {str(e)} {traceback.format_exc()}")

    except Exception as e:
        await callback.message.answer(f"❌ Произошла ошибка")
        logger.error(f"{callback.from_user.username} {callback.from_user.id} {str(e)} {traceback.format_exc()}")

    finally:
        await callback.answer()
        logger.info(f"{callback.from_user.username} {callback.from_user.id} create transaction")


@router.callback_query(F.data=="subscription_3")
async def crypto_selected3(callback: CallbackQuery):
    logger.info(f"{callback.from_user.username} {callback.from_user.id} press button {callback.data}")

    user_id = callback.from_user.id
    subscription_id = int(callback.data.split("_")[-1])

    try:
        subscription: Subscription = SyncOrm.get_subscription(subscription_id)
        user: User = SyncOrm.get_user(user_id)
        referrer: Referrer = SyncOrm.get_referrer(user.referrer_id)
        user_success_transactions: Transaction = SyncOrm.get_success_transaction_user(user.id)

        percent = referrer_percent(user, user_success_transactions, referrer, subscription.period_month)
        payment = await create_payment(user_id, subscription.id, subscription.price, percent)

        await callback.message.edit_text(
            f"🔗 Ваш адрес для оплаты USDT (SOL):\n\n"
            f"`{payment['address']}`\n\n"
            f"💰 Сумма: {payment['price']} USDT (SOL)\n\n"
            f"⏰ Адрес действует {settings.PAYMENT_TIME} минут.\n\n"
            f"После оплаты бот автоматически подтвердит подписку.",
            parse_mode="Markdown", reply_markup=cancel_kb()
        )

    except NotFreeAddress as e:
        await callback.message.answer(f"❌ {e}")
        logger.error(f"{callback.from_user.username} {callback.from_user.id} {str(e)} {traceback.format_exc()}")

    except AddressInWork as e:
        await callback.message.answer(f"❌ {e}")
        logger.error(f"{callback.from_user.username} {callback.from_user.id} {str(e)} {traceback.format_exc()}")

    except Exception as e:
        await callback.message.answer(f"❌ Произошла ошибка")
        logger.error(f"{callback.from_user.username} {callback.from_user.id} {str(e)} {traceback.format_exc()}")

    finally:
        await callback.answer()
        logger.info(f"{callback.from_user.username} {callback.from_user.id} create transaction")


# Отмена выбора
@router.callback_query(F.data == "cancel_payment")
async def cancel_payment_handler(callback: CallbackQuery):
    logger.info(f"{callback.from_user.username} {callback.from_user.id} press button cancel_payment")
    user_id = callback.from_user.id
    await cancel_payment(user_id)
    await callback.message.edit_text("❌ Оплата отменена.")
    logger.info(f"{callback.from_user.username} {callback.from_user.id} cancelled transaction")



# кнопка назад
@router.callback_query(F.data == "back")
async def cancel_payment_handler(callback: CallbackQuery):
    await callback.message.answer(text=text, reply_markup=main_kb())
    await callback.answer()

@router.callback_query(F.data == "retry")
async def retry_payment(callback: CallbackQuery):
    await callback.message.answer(text=text, reply_markup=main_kb())
    await callback.answer()






