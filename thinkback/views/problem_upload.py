#thinkback/views/problem_upload.py

from flask import Blueprint, render_template

problem_upload_blueprint = Blueprint('problem_upload', __name__)


@problem_upload_blueprint.route('/<assignment_id>', methods=['GET'])
def post_new_problem(assignment_id):
	return render_template('createassignment.html')
