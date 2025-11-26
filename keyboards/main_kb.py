from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from database.orm import SyncOrm
from utils.custom_callback import BuyPlanCallback


def main_kb() -> InlineKeyboardMarkup:


    # subscriptions = SyncOrm.get_prices()
    #
    #
    # keyboard = []
    # for subscription in subscriptions:
    #     keyboard.append([InlineKeyboardButton(text=f'{subscription.name} '
    #                                                f'{subscription.period_month+" мес" if subscription.period_month != 1000 else "Навсегда"} - '
    #                                                f'{subscription.price}$',
    #                                           callback_data=BuyPlanCallback(subscription=f"subscription_{subscription.id}").pack())])
    #
    #
    # keyboard.append([
    #             InlineKeyboardButton(
    #                 text="Реферальная система",
    #                 callback_data="referrer_system"
    #             ),
    #             InlineKeyboardButton(
    #                 text="Статус подписки",
    #                 callback_data="status"
    #             )
    #         ])
    # keyboard.append([
    #             InlineKeyboardButton(
    #                 text="Помощь",
    #                 callback_data="help"
    #             )
    #         ])
    #



    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="TRIGGER 1 мес - 49$",
                # callback_data=BuyPlanCallback(subscription="subscription_1").pack()
                callback_data="subscription_1"
            )
        ],
        [
            InlineKeyboardButton(
                text="TRIGGER 3 мес + SOL DAO 2.0 - 450$",
                # callback_data=BuyPlanCallback(subscription="subscription_2").pack()
                callback_data="subscription_2"

    )
        ],
        [
            InlineKeyboardButton(
                text="TRIGGER Навсегда + SOL DAO 2.0 - 999$",
                # callback_data=BuyPlanCallback(subscription="subscription_3").pack()
                callback_data="subscription_3"

    )
        ],
            [
                InlineKeyboardButton(
                    text="Реферальная система",
                    callback_data="referrer_system"
                ),
                InlineKeyboardButton(
                    text="Статус подписки",
                    callback_data="status"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Помощь",
                    callback_data="help"
                )
            ]
        ]
    )
