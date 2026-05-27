# src/payments.py
def get_plan(user):
    plans = {'basic': 10, 'pro': 50}
    return plans[user['plan']]  # BUG: key might not exist
