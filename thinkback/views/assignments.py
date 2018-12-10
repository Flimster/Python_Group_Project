# thinkback/views/assignments.py

from flask import Blueprint
from ..models import Project, Problem

assignments_blueprint = Blueprint('/assignments', __name__)

# Create a project with 10 empty problems
project1 = Project("Verkefni 1")
for i in range(10):
	project1.create_problem("Tmp", "This is description")

@assignments_blueprint.route('/<assignment>', methods=['GET'])
def get_assignments(assignment):
	return "Hello world this is assignment {}".format(assignment)

@assignments_blueprint.route('/createAssignment')
def create_assignment():
	return "Here you create the assignments {}"

@assignments_blueprint.route('/<assignment>/create_problem')
def create_problem(assignment):
	return "Here you create problem for assignment {}".format(assignment)

@assignments_blueprint.route('/<assignment>/<problem>', methods=['GET'])
def problem_description(assignment, problem):
	return "Hello world this is assignment {} and problem {}".format(assignment, problem)