	# thinkback/views/assignments.py

from flask import Blueprint, render_template
from ..models import Assignment

assignment_blueprint = Blueprint('/assignments', __name__)

# TODO: Delete this
# This is used for testing the various routes
assignment_list = []
problem = Assignment("Basics in python")
problem.create_problem("Hello world", "Simply print out hello world")
problem.create_problem("If statements", "Do something simple with if statements")
problem.create_problem("While loops", "Do something simple with while loops")
problem.create_problem("AI", "Use machine learning techniques that you learned to create an AI to determine the probabilty of human destructoin")
problem2 = Assignment("Advance mathematics in python")
assignment_list.append(problem)
assignment_list.append(problem2)


@assignment_blueprint.route('/active_assignments', methods=['GET'])
def get_active_assignments():
    return render_template('assignments.html', user_assignments=assignment_list)


@assignment_blueprint.route('/active_assignments/<assignment>', methods=['GET'])
def get_problems(assignment):
	the_assignment = get_problems_with_assignment(assignment)
	return render_template('problems.html', assignment=the_assignment)


@assignment_blueprint.route('/active_assignments/<assignment>/<problem>', methods=['GET'])
def get_assignment_problem(assignment, problem):
    return render_template('problem.html', problem=problem)

def get_problems_with_assignment(name):
	for assignment in assignment_list:
		if assignment.name == name:
			return assignment