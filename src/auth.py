# src/auth.py
def validate_session(session_data):
    user_id = session_data.get('user')
    if user_id is not None:
        return user_id.upper()
    return None