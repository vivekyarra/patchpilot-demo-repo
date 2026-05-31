# src/payments.py
def get_plan(user):
    plans = {'basic': 10, 'pro': 50, 'enterprise': 100}
    return plans[user['plan']]