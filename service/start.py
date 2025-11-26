from database.orm import SyncOrm


async def start_service(message):
    args = message.text.split()
    referrer_id = None
    if len(args) > 1:
        try:
            referrer_id = int(args[1])
        except ValueError:
            print(referrer_id)
            print(args[1])
            referrer_id = SyncOrm.get_partner_id(args[1])

        if referrer_id == message.from_user.id:
            referrer_id = None

    if not SyncOrm.user_exist(message.from_user.id):
        full_name = message.from_user.full_name
        full_name += message.from_user.last_name if message.from_user.last_name else ""

        SyncOrm.add_user(message.from_user.id, message.from_user.username, full_name, referrer_id)
        SyncOrm.add_referral(message.from_user.id)
