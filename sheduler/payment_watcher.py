import asyncio
from datetime import datetime

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import settings
from core.bot_init import bot
from database.orm import SyncOrm
from utils.payment_checker import get_balance
from utils.invite_link import create_one_time_invite_link
from utils.subscription import new_sub_until
from utils.log_config import bot_logger as logger


async def check_pending_payments():
    """Проверяет только новые поступления на адреса, а не общий баланс."""
    while True:
            logger.info('Getting transactions...')
            transactions = SyncOrm.get_pending_transactions()
            for i, transaction in enumerate(transactions):
                logger.info(f'Check transaction {transaction.id}')

                # Получаем адрес
                address = transaction.address

                # Получаем пользователя
                user = transaction.user

                # получаем подписку
                subscription = transaction.subscription

                # Баланс кошелька на момент создания заявки на оплату (транзакции)
                database_balance = SyncOrm.get_balance(address.id)

                # Текущий баланс кошелька
                current_balance = get_balance(address.address)

                # Сколько поступило после начала оплаты
                received = current_balance - database_balance

                # Успешная оплата
                if received >= subscription.price:
                    logger.info(f'Transaction {transaction.id} was paid')

                    # если пользователь покупает первый раз - отправляем ссылку
                    if user.subscription_until is None:
                        # получаем группы
                        group_ids = SyncOrm.get_groups(transaction.subscription.id)
                        links = await create_one_time_invite_link(group_ids)

                        inline_keyboard = []

                        for name, link in links.items():
                            inline_keyboard.append([InlineKeyboardButton(text=f"Вступить в {name}", url=link)])

                        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


                        await bot.send_message(
                            user.id,
                            text=f"Велком мессадж от Дани\n\n",
                            reply_markup=keyboard,
                        )
                        await bot.send_message(settings.ADMIN_GROUP,
                                               text=f"user {user.username} paid {subscription.price}$ for {subscription.name} {subscription.period_month} months")

                    else:
                        await bot.send_message(user.id, f"Оплата получена!\nПодписка продлена")
                        await bot.send_message(settings.ADMIN_GROUP,
                                               text=f"user {user.username} paid {subscription.price}$ for {subscription.name} {subscription.period_month} months")


                    transaction.status = "paid"

                    # Освобождаем адрес
                    address.is_busy = False
                    user.id_address = None

                    SyncOrm.update_address(address)
                    SyncOrm.update_transaction(transaction)

                    # Продляем подписку
                    new_subscription_until = new_sub_until(user.subscription_until, subscription.period_month)
                    user.subscription_until = new_subscription_until
                    SyncOrm.update_user(user)

                    user_subscription = SyncOrm.get_user_subscriptions(user.id)
                    if user_subscription is None:
                        SyncOrm.update_user_subscription(subscription.id, user.id, new_subscription_until)
                    else:
                        SyncOrm.update_user_subscription2(user_subscription.id, subscription.id, user.id, new_subscription_until)
                    # SyncOrm.update_user_subscription(subscription.id, user.id, new_subscription_until)




                # Если время вышло — просрочка
                if datetime.utcnow() > transaction.expires_at:
                # if 1:
                    logger.info(f'Transaction {transaction.id} expired')

                    transaction.status = "expired"
                    address.is_busy = False
                    user.id_address = None

                    SyncOrm.update_user(user)
                    SyncOrm.update_address(address)
                    SyncOrm.update_transaction(transaction)

                    try:
                        await bot.send_message(
                            user.id,
                            f"_Ваша заявка отменена, время на оплату вышло!_", parse_mode='Markdown',
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Повторить попытку', callback_data='retry')]])
                        )
                    except:
                        pass
                else:
                    logger.info(f'Transaction {transaction.id} not paid')

            await asyncio.sleep(60)  # Проверяем
