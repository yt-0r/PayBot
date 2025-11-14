import traceback
from datetime import datetime

from aiogram import Router, types, F

from config import settings
from utils.log_config import bot_logger as logger

router = Router()

@router.message(F.text == "❓ Помощь")
async def txt_referrer(message: types.Message):
    logger.info(f"{message.from_user.username} {message.from_user.id} press button ❓ Помощь")

    await message.answer(
        (f"📞 Поддержка\n"
         f"{settings.ADMINISTRATOR}\n")
    )


