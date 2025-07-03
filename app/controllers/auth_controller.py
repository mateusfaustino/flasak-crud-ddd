from flask import Blueprint, request, jsonify, current_app


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    """Create a new user and return a success message.

    Expects ``username`` and ``password`` fields in the JSON body.

    Returns a tuple ``(response, status_code)`` with ``201`` when the user is
    created or ``400`` if the user already exists.
    """
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    user = current_app.auth_service.register(username, password)
    if user:
        return jsonify({'message': 'User created'}), 201
    return jsonify({'message': 'User already exists'}), 400


@auth_bp.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return a JWT token.

    The request body should contain ``username`` and ``password`` fields.

    Returns the generated token in JSON format or ``401`` when credentials are
    invalid.
    """
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    token = current_app.auth_service.authenticate(username, password)
    if token:
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401
