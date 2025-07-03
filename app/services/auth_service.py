import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, request, jsonify
from functools import wraps

from ..adapters.sqlalchemy.models import User
from ..domain.repositories import UserRepository


class AuthService:
    @staticmethod
    def register(username: str, password: str):
        if UserRepository.get_by_username(username):
            return None
        user = User(username=username, password_hash=generate_password_hash(password))
        UserRepository.add(user)
        return user

    @staticmethod
    def authenticate(username: str, password: str):
        user = UserRepository.get_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            payload = {
                'sub': user.id,
                'exp': datetime.utcnow() + timedelta(hours=1)
            }
            token = jwt.encode(payload, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')
            return token
        return None


def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message': 'Missing token'}), 401
        try:
            token = auth_header.split()[1]
            payload = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
            request.user_id = payload['sub']
        except Exception:
            return jsonify({'message': 'Invalid token'}), 401
        return f(*args, **kwargs)
    return decorated
