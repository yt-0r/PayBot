
from aiogram import Router, types, F
from aiogram.types import CallbackQuery
from aiogram.filters import Command

from config import settings
from utils.log_config import bot_logger as logger

router = Router()

@router.callback_query(F.data == "help")
async def help_window(callback: CallbackQuery):
    logger.info(f"{callback.from_user.username} {callback.from_user.id} press button Помощь")

    await callback.message.answer(
        text = f"_Возникли вопросы или проблемы с оплатой ?\n\n"
         f"Пишите нашему менеджеру {settings.ADMINISTRATOR}_", parse_mode="Markdown")

    await callback.answer()



@router.message(Command('help'))
async def cmd_start(message: types.Message):
    logger.info(f"{message.from_user.username} {message.from_user.id} press button Помощь")

    await message.answer(
        text = f"_Возникли вопросы или проблемы с оплатой ?\n\n"
         f"Пишите нашему менеджеру {settings.ADMINISTRATOR}_", parse_mode="Markdown")

