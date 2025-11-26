from aiogram.filters.callback_data import CallbackData


class BuyPlanCallback(CallbackData, prefix="buy"):
    subscription: str

