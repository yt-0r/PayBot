from datetime import datetime, timedelta
from aiogram import Bot

from config import settings
from core.bot_init import bot

async def create_one_time_invite_link(groups: list):
    """Создаёт одноразовые инвайт-ссылки в Telegram группы."""
    d = {}
    for group in groups:

        expire_time = datetime.now() + timedelta(minutes=30)

        invite_link = await bot.create_chat_invite_link(
            chat_id=group.id,
            expire_date=expire_time,
            member_limit=10  # Одноразовая ссылка
        )

        d[group.name] = invite_link.invite_link

    return d
