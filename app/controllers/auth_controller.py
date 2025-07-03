from flask import Blueprint, request, jsonify
from ..services.auth_service import AuthService


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    user = AuthService.register(username, password)
    if user:
        return jsonify({'message': 'User created'}), 201
    return jsonify({'message': 'User already exists'}), 400


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    token = AuthService.authenticate(username, password)
    if token:
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401
