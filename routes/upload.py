from models import User, db
from flask_login import login_required, current_user
from flask import Blueprint, request, jsonify
import os

upload_blueprint = Blueprint('upload', __name__)

# Define the local upload folder for development (this can later be replaced by Azure Blob Storage)
UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the folder exists

@upload_blueprint.route('/upload', methods=['POST'])
@login_required  # Ensure the user is logged in to upload their profile picture
def upload_profile_picture():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400  # Handle case where no file is uploaded

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400  # Handle case where no file is selected
    
    # Save file in the local uploads folder (development purpose)
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    # Update the current user's profile picture URL in the database
    current_user.profile_pic_url = file_path  # Store the file path (or later an Azure Blob URL)
    db.session.commit()

    return jsonify({"file_url": file_path}), 200  # Return the file URL
