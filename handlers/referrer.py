import traceback

from aiogram import Router, types, F

from config import settings
from database.orm import SyncOrm
from utils.log_config import bot_logger as logger

router = Router()

@router.message(F.text == "👫 Реферальная система")
async def txt_referrer(message: types.Message):
    logger.info(f"{message.from_user.username} {message.from_user.id} press button 👫Реферальная система")

    try:
        referrer_id = message.from_user.id
        count = SyncOrm.get_invited_count(referrer_id)
        ref_link = f"https://t.me/{settings.BOT_TAG}?start={referrer_id}"

        text = (
            f"💎 <b>Реферальная система</b>\n\n"
            f"👤 Ваша ссылка: <code>{ref_link}</code>\n\n"
            f"📊 Приглашено пользователей: <b>{count}</b>\n\n"
            f"🔹 Отправь ссылку друзьям и получай бонусы!"
        )

        await message.answer(
            text
        )


    except Exception as e:
        await message.reply('❌ Произошла ошибка')
        logger.error(f"{message.from_user.username} {message.from_user.id} {str(e)} {traceback.format_exc()}")


