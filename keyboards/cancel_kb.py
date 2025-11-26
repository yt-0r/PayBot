from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def cancel_kb():
    return InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="❌ Отменить оплату", callback_data="cancel_payment")]
    ]
)