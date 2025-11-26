from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def cancel_kb_adm():
    return InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="❌ Отмена", callback_data="admin_cancel")]
    ]
)