#thinkback/views/problem_upload.py

from flask import Blueprint

problem_upload_blueprint = Blueprint('problem_upload', __name__)


@problem_upload_blueprint.route('/<assignment_id>', methods=['POST'])
def post_new_problem(assignment_id):
	return "Here i am"
