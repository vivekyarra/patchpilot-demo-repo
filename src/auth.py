# src/auth.py
def validate_session(session_data):
    user_id = session_data.get('user')
    return user_id.upper()  # BUG: user_id can be None
