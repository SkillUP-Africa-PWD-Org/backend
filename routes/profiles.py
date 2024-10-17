from flask import Blueprint, jsonify
from flask_login import login_required, current_user

profiles_blueprint = Blueprint('profiles', __name__)

@profiles_blueprint.route('/profile', methods=['GET'])
@login_required  # Ensure the user is logged in to view their profile
def get_profile():
    # Return the user's profile details, including the optional profile picture
    profile_data = {
        "username": current_user.username,
        "email": current_user.email,
        "profile_pic_url": current_user.profile_pic_url or None  # Return None if no profile picture is uploaded
    }
    return jsonify(profile_data), 200
