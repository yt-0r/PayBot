from asyncio import sleep

from config import settings
from core.bot_init import bot


async def kick_user(user_id, groups):
    """Кикаем пользователя, у которого нет подписки"""

    for group in groups:
        await bot.ban_chat_member(
            chat_id=group.id,
            user_id=user_id
        )

        await sleep(1)

        # Сразу разбаниваем, чтобы он мог вступить снова после оплаты
        await bot.unban_chat_member(
            chat_id=group.id,
            user_id=user_id
        )



