from flask import Blueprint, request, jsonify
from models import Curriculum, db

curriculum_blueprint = Blueprint('curriculum', __name__)

# Add a new curriculum course
@curriculum_blueprint.route('/curriculum/add', methods=['POST'])
def add_curriculum():
    data = request.json
    new_course = Curriculum(
        course_title=data['course_title'],
        course_description=data['course_description'],
        syllabus_url=data.get('syllabus_url', None)  # Optional file URL
    )
    db.session.add(new_course)
    db.session.commit()
    return jsonify({"message": "Curriculum added successfully"}), 201

# Get all curriculum courses
@curriculum_blueprint.route('/curriculum', methods=['GET'])
def get_curriculum():
    courses = Curriculum.query.all()
    course_list = [
        {
            "course_title": course.course_title,
            "course_description": course.course_description,
            "syllabus_url": course.syllabus_url
        }
        for course in courses
    ]
    return jsonify(course_list), 200
