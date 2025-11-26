from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def address_kb():
    return InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🟢 Добавить кошелек", callback_data="adm_add_address")],
        [InlineKeyboardButton(text="👁 Просмотреть кошельки", callback_data="adm_show_address")],
        [InlineKeyboardButton(text="🔴 Удалить кошелёк", callback_data="adm_del_address")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="adm_back")],

    ]
)