from flask import Blueprint, jsonify
from models import Curriculum, Lesson

curriculum_blueprint = Blueprint('curriculum', __name__)

# Get all curriculum courses along with their lessons
@curriculum_blueprint.route('/curriculum', methods=['GET'])
def get_curriculum():
    courses = Curriculum.query.all()

    course_list = []
    for course in courses:
        lessons = [
            {
                "lesson": lesson.lesson,
                "content": lesson.content,
                "images": lesson.images
            } for lesson in course.lessons  # Iterate through the associated lessons
        ]

        course_list.append({
            "course_title": course.course_title,
            "course_description": course.course_description,
            "syllabus_url": lessons  # Add the nested lessons here
        })

    return jsonify(course_list), 200
