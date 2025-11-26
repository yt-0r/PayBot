# keyboards/admin_inline.py
from aiogram.utils.keyboard import InlineKeyboardBuilder

def admin_menu_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="💳 Адреса", callback_data="adm_address")
    kb.button(text="🎁 Купоны", callback_data="adm_coupon")
    # kb.button(text="📄 Список адресов", callback_data="admin_list_addresses")
    kb.adjust(1)
    return kb.as_markup()
