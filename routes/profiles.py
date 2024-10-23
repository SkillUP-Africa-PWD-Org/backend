from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from flasgger import swag_from

profiles_blueprint = Blueprint('profiles', __name__)

@profiles_blueprint.route('/profile', methods=['GET'])
@login_required
@swag_from({
    'responses': {
        200: {
            'description': 'Retrieve the current user profile',
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string'},
                    'email': {'type': 'string'},
                    'profile_pic_url': {'type': 'string', 'nullable': True}
                }
            }
        }
    }
})
def get_profile():
    """Get the current user's profile
    ---
    responses:
      200:
        description: Get the current user's profile
        schema:
          type: object
          properties:
            username:
              type: string
            email:
              type: string
            profile_pic_url:
              type: string
              nullable: true
    """
    profile_data = {
        "username": current_user.username,
        "email": current_user.email,
        "profile_pic_url": current_user.profile_pic_url or None
    }
    return jsonify(profile_data), 200
