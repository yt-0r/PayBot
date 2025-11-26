from datetime import datetime
from dateutil.relativedelta import relativedelta

def new_sub_until(subscription_until, months):

    if subscription_until is None or subscription_until < datetime.utcnow():
        return datetime.utcnow() + relativedelta(months=months)

    else:
        return subscription_until + relativedelta(months=months)