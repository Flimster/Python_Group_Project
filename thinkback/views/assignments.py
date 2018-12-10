# thinkback/views/assignments.py

from flask import Blueprint

assignments_blueprint = Blueprint('/assignments', __name__)

@assignments_blueprint.route('/assignments')
def tmp():
	return "Hello world"