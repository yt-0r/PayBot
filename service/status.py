from datetime import datetime

from database.orm import SyncOrm
from keyboards.main_kb import main_kb


def status_service(callback):
    user_id = callback.from_user.id
    sub_until = SyncOrm.get_sub_until(user_id)

    if len(sub_until) == 0 or sub_until[0] is None or sub_until[0] < datetime.utcnow():
        text = 'У вас нет активной подписки!'

    else:
        text = (f""
                # f"🪄{sub_until[0].name}\n\n"
                f"⌚️ Подписка истекает {sub_until[0].strftime('%d.%m.%Y %H:%M')}")

    return text
