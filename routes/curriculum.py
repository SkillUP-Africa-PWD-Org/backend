from flask import Blueprint, jsonify
from models import Curriculum, Lesson
from get_content import getContent
from flasgger import swag_from

curriculum_blueprint = Blueprint('curriculum', __name__)

# Route 1: List all curriculums
@curriculum_blueprint.route('/curriculum', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List all curriculums',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'curriculum_id': {'type': 'integer'},
                        'course_title': {'type': 'string'},
                        'course_description': {'type': 'string'}
                    }
                }
            }
        }
    }
})
def list_curriculums():
    """List all curriculums
    ---
    responses:
      200:
        description: A list of all curriculums
        schema:
          type: array
          items:
            type: object
            properties:
              curriculum_id:
                type: integer
              course_title:
                type: string
              course_description:
                type: string
    """
    curriculums = Curriculum.query.all()
    result = []
    for curriculum in curriculums:
        result.append({
            "curriculum_id": curriculum.id,
            "course_title": curriculum.course_title,
            "course_description": curriculum.course_description
        })
    return jsonify(result), 200


# Route 2: List all lessons for a specific curriculum
@curriculum_blueprint.route('/curriculum/<int:curriculum_id>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'curriculum_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the curriculum'
        }
    ],
    'responses': {
        200: {
            'description': 'List all lessons for a specific curriculum',
            'schema': {
                'type': 'object',
                'properties': {
                    'curriculum_title': {'type': 'string'},
                    'lessons': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'lesson_id': {'type': 'integer'},
                                'lesson_title': {'type': 'string'},
                                'content': {'type': 'string'},
                                'images': {'type': 'string', 'nullable': True}
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Curriculum not found'
        }
    }
})
def list_lessons(curriculum_id):
    """List all lessons for a specific curriculum
    ---
    parameters:
      - name: curriculum_id
        in: path
        type: integer
        required: true
        description: The ID of the curriculum
    responses:
      200:
        description: A list of lessons for the specified curriculum
        schema:
          type: object
          properties:
            curriculum_title:
              type: string
            lessons:
              type: array
              items:
                type: object
                properties:
                  lesson_id:
                    type: integer
                  lesson_title:
                    type: string
                  content:
                    type: string
                  images:
                    type: string
                    nullable: true
      404:
        description: Curriculum not found
    """
    curriculum = Curriculum.query.get(curriculum_id)
    if not curriculum:
        return jsonify({"message": "Curriculum not found"}), 404

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


# Route 3: Get specific lesson(s) by title
@curriculum_blueprint.route('/curriculum/lesson/<string:title>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'title',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'The title of the lesson to search for'
        }
    ],
    'responses': {
        200: {
            'description': 'Search lessons by title',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'lesson_title': {'type': 'string'},
                        'lesson_content': {'type': 'string'},
                        'id': {'type': 'integer'}
                    }
                }
            }
        },
        404: {
            'description': 'No lessons found with the given title'
        }
    }
})
def fetch_course_by_title(title):
    """Search lessons by title
    ---
    parameters:
      - name: title
        in: path
        type: string
        required: true
        description: The title of the lesson to search for
    responses:
      200:
        description: A list of lessons that match the title
        schema:
          type: array
          items:
            type: object
            properties:
              lesson_title:
                type: string
              lesson_content:
                type: string
              id:
                type: integer
      404:
        description: No lessons found with the given title
    """
    lessons = Lesson.query.filter(Lesson.lesson.ilike(f"%{title}%")).all()
    if not lessons:
        return jsonify({"message": "No lessons found with the title"}), 404

    lesson_list = []
    for lesson in lessons:
        blob_name = lesson.content
        lesson_content = getContent(blob_name)
        lesson_list.append({
            "id": lesson.id,
            "lesson_title": lesson.lesson,
            "lesson_content": lesson_content
        })

    return jsonify(lesson_list), 200
