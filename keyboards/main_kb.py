
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💳 Купить подписку")],
            [KeyboardButton(text="📅 Статус подписки")],
            [KeyboardButton(text="👫 Реферальная система",)],
            [KeyboardButton(text="❓ Помощь")]
        ],
        resize_keyboard=True
    )
