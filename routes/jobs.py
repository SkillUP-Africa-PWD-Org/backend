from flask import Blueprint, jsonify
from models import Job
from flasgger import swag_from

jobs_blueprint = Blueprint('jobs', __name__)

@jobs_blueprint.route('/jobs', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List of available jobs',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'title': {'type': 'string'},
                        'description': {'type': 'string'},
                        'is_available': {'type': 'boolean'}
                    }
                }
            }
        }
    }
})
def get_jobs():
    """Get all available jobs
    ---
    responses:
      200:
        description: List of jobs
        schema:
          type: array
          items:
            type: object
            properties:
              title:
                type: string
              description:
                type: string
              is_available:
                type: boolean
    """
    jobs = Job.query.all()
    jobs_data = [{"title": job.title, "description": job.description, "is_available": job.is_available} for job in jobs]
    return jsonify(jobs_data), 200
