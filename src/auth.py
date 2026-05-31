# src/auth.py
def validate_session(session_data):
    user_id = session_data.get('user')
    if user_id is None:
        return None  # Return None if user_id is missing or explicitly None, indicating an invalid session.
    return user_id.upper()