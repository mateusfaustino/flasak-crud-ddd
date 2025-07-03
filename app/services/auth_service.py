import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, request, jsonify
from functools import wraps

from ..domain.entities import User
from ..domain.repositories import UserRepositoryInterface


class AuthService:
    """Handle user registration and authentication."""

    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def register(self, username: str, password: str):
        if self.user_repository.get_by_username(username):
            return None
        user = User(username=username, password_hash=generate_password_hash(password))
        self.user_repository.add(user)
        return user

    def authenticate(self, username: str, password: str):
        user = self.user_repository.get_by_username(username)
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
