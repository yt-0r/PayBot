from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def coupon_kb():
    return InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🟢 Создать купон", callback_data="adm_add_coupon")],
        [InlineKeyboardButton(text="👁 Просмотреть купоны", callback_data="adm_show_coupon")],
        [InlineKeyboardButton(text="🔴 Удалить купон", callback_data="adm_del_coupon")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="adm_back")],

    ]
)