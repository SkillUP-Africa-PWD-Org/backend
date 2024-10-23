from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user
from models import User
from werkzeug.security import check_password_hash
from flasgger import swag_from

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'username',
            'in': 'body',
            'required': True,
            'description': 'The user\'s username',
            'schema': {'type': 'string'}
        },
        {
            'name': 'password',
            'in': 'body',
            'required': True,
            'description': 'The user\'s password',
            'schema': {'type': 'string'}
        }
    ],
    'responses': {
        200: {
            'description': 'Login successful'
        },
        401: {
            'description': 'Invalid credentials'
        }
    }
})
def login():
    """User login
    ---
    parameters:
      - name: username
        in: body
        type: string
        required: true
        description: The user's username
      - name: password
        in: body
        type: string
        required: true
        description: The user's password
    responses:
      200:
        description: Login successful
      401:
        description: Invalid credentials
    """
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@auth_blueprint.route('/logout', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'User logged out successfully'
        }
    }
})
def logout():
    """User logout
    ---
    responses:
      200:
        description: User logged out successfully
    """
    logout_user()
    return jsonify({"message": "Logged out"}), 200
