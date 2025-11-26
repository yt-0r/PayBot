from database.models import User, Referrer

# Функция вычисляющая процент реферала
# Ничего лучше ветвления я не придумал

def referrer_percent(user: User, user_success_transactions, referrer: Referrer, period_month: int) -> float:

    if user.referrer_id is None:
        percent = 0

    # если не первая покупка, и реферал ПАРТНЕР
    elif user_success_transactions and referrer.name != 'default' and period_month != 1000:
        percent = 15
    # если не первая покупка, и реферал НЕ ПАРТНЕР
    elif user_success_transactions and referrer.name == 'default' and period_month != 1000:
        percent = 10
    # если первая покупка, и реферал ПАРТНЕР
    elif not user_success_transactions and referrer.name != 'default' and period_month != 1000 :
        percent = 50
    # если первая покупка и реферал НЕ ПАРТНЕР
    elif not user_success_transactions and referrer.name == 'default' and period_month != 1000:
        percent = 30

    # если покупает навсегда и реферал ПАРТНЕР
    elif referrer.name != 'default' and period_month == 1000:
        percent = 25

    # если покупает навсегда и реферал НЕ ПАРТНЕР
    elif referrer.name == 'default' and period_month == 1000:
        percent = 15

    else:
        percent = 0
        print('yes')


    return percent