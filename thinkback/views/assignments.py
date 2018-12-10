# thinkback/views/assignments.py

from flask import Blueprint
from ..models import Project

assignments_blueprint = Blueprint('/assignments', __name__)

# Create a project with 10 empty problems
project1 = Project()
for i in range(10):
	project1.create_problem()

@assignments_blueprint.route('/<assignment>', methods=['GET'])
def get_assignments(assignment):
	return "Hello world this is assignment {}".format(assignment)


@assignments_blueprint.route('/<assignment>/<problem>', methods=['GET'])
def problem_description(assignment, problem):
	return "Hello world this is assignment {} and problem {}".format(assignment, problem)