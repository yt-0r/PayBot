import traceback
from datetime import datetime

from aiogram import Router, types, F

from config import settings
from database.orm import SyncOrm
from utils.log_config import bot_logger as logger

router = Router()

@router.message(F.text == "📅 Статус подписки")
async def txt_referrer(message: types.Message):
    logger.info(f"{message.from_user.username} {message.from_user.id} press button 📅 Статус подписки")

    try:
        user_id = message.from_user.id
        sub_until = SyncOrm.get_sub_until(user_id)


        if sub_until is None or sub_until[0] is None or sub_until[0] < datetime.utcnow():
            await message.answer('❌ У вас нет подписки')

        else:
            text = f"⌚️ Подписка истекает {sub_until[0].strftime('%d.%m.%Y %H:%M')}"

            await message.answer(
                text
            )


    except Exception as e:
        await message.reply('❌ Произошла ошибка')
        logger.error(f"{message.from_user.username} {message.from_user.id} {str(e)} {traceback.format_exc()}")


