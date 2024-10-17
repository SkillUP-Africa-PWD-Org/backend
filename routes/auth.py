from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user
from models import User
from werkzeug.security import check_password_hash

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@auth_blueprint.route('/logout')
def logout():
    logout_user()
    return jsonify({"message": "Logged out"}), 200
