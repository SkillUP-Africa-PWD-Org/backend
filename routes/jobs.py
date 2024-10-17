from flask import Blueprint, jsonify
from models import Job

jobs_blueprint = Blueprint('jobs', __name__)

@jobs_blueprint.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    jobs_data = [{"title": job.title, "description": job.description, "is_available": job.is_available} for job in jobs]
    return jsonify(jobs_data), 200
