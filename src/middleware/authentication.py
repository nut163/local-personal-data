```python
from flask import request, jsonify, g
from src.services.UserService import UserService
from src.utils.encryption import verify_password

def authenticate():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'message': 'Missing token. Please login or register.'}), 401

    try:
        token = auth_header.split(" ")[1]
        user_id = UserService.decode_auth_token(token)
        user = UserService.get_user_by_id(user_id)
        if not user:
            return jsonify({'message': 'User not found.'}), 404

        if not verify_password(user.password, token):
            return jsonify({'message': 'Invalid token. Please login again.'}), 401

        g.user = user
    except Exception as e:
        return jsonify({'message': str(e)}), 500

    return None
```