from config import settings
from database.orm import SyncOrm


async def referrer_callback(callback):
    referrer_id = callback.from_user.id
    referrer = SyncOrm.get_referrer(callback.from_user.id)

    # для ПАРТНЕРОВ уникальное название.
    ref_link = f"https://t.me/{settings.BOT_TAG}?start={referrer_id}" if referrer.name == 'default' \
        else f"https://t.me/{settings.BOT_TAG}?start={referrer.name}"

    # получаем приход реферала
    referrer_income = SyncOrm.get_referrer_income(referrer_id)
    referrer_sum = sum([i[0] * (i[1] / 100) for i in referrer_income])

    # получаем кол-во рефералов
    referrer_count = SyncOrm.get_referrer_count(referrer_id)

    # получаем отход реферала
    referrer_remove = SyncOrm.get_referrer_remove(referrer_id)

    text = (
        f"💎 <b>Реферальная система</b>\n\n"
        f"👤 Ваша ссылка:\n <code>{ref_link}</code>\n\n"
        f"📊 Приглашено пользователей: <b>{referrer_count}</b>\n\n"
        f"💸 Ваш заработок: <b>{(referrer_sum - referrer_remove):.2f}</b> USDT\n\n"
        f"🔹 Отправь ссылку друзьям и получай бонусы!"
    )
    return text
