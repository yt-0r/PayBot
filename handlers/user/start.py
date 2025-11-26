import traceback

from aiogram import Router, types
from aiogram.filters import CommandStart

from database.orm import SyncOrm
from keyboards.main_kb import main_kb
from service.start import start_service
from texts.wellcome_text import text
from utils.log_config import bot_logger as logger

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    logger.info(f"{message.from_user.username} {message.from_user.id} start the bot.")
    try:
        await start_service(message)

        await message.answer(text=text,
            reply_markup=main_kb(), parse_mode='Markdown'
        )

    except Exception as e:
        await message.reply('❌ Произошла ошибка')
        logger.error(f"{message.from_user.username} {message.from_user.id} {str(e)} {traceback.format_exc()}")


