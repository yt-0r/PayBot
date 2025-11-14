import traceback

from aiogram import Router, types
from aiogram.filters import CommandStart

from database.orm import SyncOrm
from keyboards.main_kb import main_keyboard
from utils.log_config import bot_logger as logger

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    logger.info(f"{message.from_user.username} {message.from_user.id} start the bot.")
    try:
        args = message.text.split()
        referrer_id = 2058516705
        if len(args) > 1:
            try:
                referrer_id = int(args[1][::-1])
            except ValueError:
                pass
        if referrer_id == message.from_user.id and referrer_id != 2058516705:
            referrer_id = None

        if not SyncOrm.user_exist(message.from_user.id):
            full_name = message.from_user.full_name
            full_name += message.from_user.last_name if message.from_user.last_name else ""

            SyncOrm.add_user(message.from_user.id, message.from_user.username, full_name, referrer_id)

        await message.answer(
            "Добро пожаловать!\nВыберите действие:",
            reply_markup=main_keyboard()
        )

    except Exception as e:
        await message.reply('❌ Произошла ошибка')
        logger.error(f"{message.from_user.username} {message.from_user.id} {str(e)} {traceback.format_exc()}")


