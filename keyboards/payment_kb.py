from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def subscription_period_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="1 месяц", callback_data="pay_months_1"),
            InlineKeyboardButton(text="3 месяца", callback_data="pay_months_3"),
            InlineKeyboardButton(text="6 месяцев", callback_data="pay_months_6")
        ],
        [InlineKeyboardButton(text="❌ Отмена", callback_data="cancel_payment")]
    ])
