import traceback

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery

from config import settings
from database.orm import SyncOrm
from service.referrer import referrer_callback
from utils.log_config import bot_logger as logger

router = Router()

@router.callback_query(F.data == "referrer_system")
async def txt_referrer(callback: CallbackQuery):
    logger.info(f"{callback.from_user.username} {callback.from_user.id} press button Реферальная система")
    try:
        text = await referrer_callback(callback)

        await callback.message.answer(
            text
        )

    except Exception as e:
        await callback.message.reply('❌ Произошла ошибка')
        logger.error(f"{callback.from_user.username} {callback.from_user.id} {str(e)} {traceback.format_exc()}")

    finally:
        await callback.answer()


@router.message(Command('refs'))
async def cmd_start(message: types.Message):
    logger.info(f"{message.from_user.username} {message.from_user.id} press button Реферальная система")
    try:
        text = await referrer_callback(message)

        await message.answer(
            text
        )

    except Exception as e:
        await message.reply('❌ Произошла ошибка')
        logger.error(f"{message.from_user.username} {message.from_user.id} {str(e)} {traceback.format_exc()}")




