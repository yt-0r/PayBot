import asyncio
from datetime import datetime, timedelta

from core.bot_init import bot
from database.orm import SyncOrm
from keyboards.main_kb import main_kb
from utils.kick_user import kick_user

from utils.log_config import bot_logger as logger


async def check_users_subscriptions():
    """Проверяем пользователей на наличие подписки"""
    while True:
            logger.info('Getting users with subscription...')
            users = SyncOrm.get_users_with_subscription()
            for user in users:
                logger.info(f'Check user {user.id}')
                delta = user.subscription_until - datetime.utcnow()

                # Уведомляем пользователя
                if 0 <= delta.days <= 3:
                    try:

                        if delta.days == 0:
                            day = f'осталось {delta.days} дней'

                        elif delta.days == 1:
                            day = f'остался {delta.days} день'

                        elif delta.days == 2 or delta.days == 3:
                            day = f'осталось {delta.days} дня'

                        else:
                            day = f'{delta.days} '

                        await bot.send_message(
                            user.id,
                            f"⚠️ Внимание!\nДо окончания вашей подписки {day}",
                            reply_markup=main_kb()
                        )
                        logger.info(f'user {user.id} {day}')

                    except:
                        pass

                    continue

                # если подписка кончилась - удаляем
                if delta.days < 0:

                    user_subscription = SyncOrm.get_user_subscriptions(user.id)
                    group_ids = SyncOrm.get_groups(user_subscription.subscription_id)

                    await kick_user(user.id, group_ids)


                    old_sub_until = user.subscription_until

                    user.subscription_until = None
                    SyncOrm.update_user(user)

                    SyncOrm.update_user_subscription3(user_subscription.id, user_subscription.subscription_id, user.id,
                                                      old_sub_until)

                    logger.info(f'Kick user {user.id} from {", ".join([x.name for x in group_ids])}')


                    try:
                        await bot.send_message(
                            user.id,
                            f"⚠️ Внимание!\nВаша подписка закончилась",
                            reply_markup=main_kb()
                        )

                    except:
                        pass

            await asyncio.sleep(86400)  # Проверяем раз в сутки
