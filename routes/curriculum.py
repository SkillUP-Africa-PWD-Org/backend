from flask import Blueprint, jsonify
from models import Curriculum, Lesson
from get_content import getContent

curriculum_blueprint = Blueprint('curriculum', __name__)

# Route 1: List all curriculums
@curriculum_blueprint.route('/curriculum', methods=['GET'])
def list_curriculums():
    try:
        # Query all curriculums
        curriculums = Curriculum.query.all()
        result = []

        for curriculum in curriculums:
            result.append({
                "curriculum_id": curriculum.id,
                "course_title": curriculum.course_title,
                "course_description": curriculum.course_description
            })

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route 2: List all lessons for a specific curriculum
@curriculum_blueprint.route('/curriculum/<int:curriculum_id>', methods=['GET'])
def list_lessons(curriculum_id):
    try:
        # Fetch the curriculum by id
        curriculum = Curriculum.query.get(curriculum_id)
        if not curriculum:
            return jsonify({"message": "Curriculum not found"}), 404

        # Get all lessons associated with the curriculum
        lessons = [
            {
                "lesson_id": lesson.id,
                "lesson_title": lesson.lesson,
                "content": lesson.content,
                "images": lesson.images
            } for lesson in curriculum.lessons
        ]

        return jsonify({
            "curriculum_title": curriculum.course_title,
            "lessons": lessons
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route 3: Get specific lesson(s) by title
@curriculum_blueprint.route('/curriculum/lesson/<string:title>', methods=['GET'])
def fetch_course_by_title(title):
    try:
        # Fetch lessons that match the given title (partial match)
        lessons = Lesson.query.filter(Lesson.lesson.ilike(f"%{title}%")).all()

        if not lessons:
            return jsonify({"message": "No lessons found with the title"}), 404

        # Prepare response for multiple lessons with similar titles
        lesson_list = []
        for lesson in lessons:
            blob_name = lesson.content  # Assuming 'content' stores the blob name
            lesson_content = getContent(blob_name)
            lesson_list.append({
                "lesson_title": lesson.lesson,
                "lesson_content": lesson_content,
                "id": lesson.id
            })

        return jsonify(lesson_list), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
