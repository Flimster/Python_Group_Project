# thinkback/views/assignments.py

from flask import Blueprint, render_template, url_for
from ..models import Assignment


assignment_blueprint = Blueprint('/assignments', __name__)

# TODO: Delete this
# This is used for testing the various routes
assignment_list = []
problem = Assignment("Basics in python")
problem.create_problem("Hello world", "Simply print out hello world")
problem.create_problem(
    "If statements", "Do something simple with if statements")
problem.create_problem("While loops", "Do something simple with while loops")
problem.create_problem(
    "AI", "Use machine learning techniques that you learned to create an AI to determine the probabilty of human destructoin")
problem2 = Assignment("Advance mathematics in python")
assignment_list.append(problem)
assignment_list.append(problem2)
#Testing for past assigments
past_assignment_list = []
past_problem = Assignment("Number Lists")
past_problem.create_problem("Create an asc. number list", "33% of grade")
past_problem.create_problem("Create a desc. number list", "33% of grade")
past_problem.create_problem("Calculate the std. deviation of all the numbers", "33% of grade")
past_assignment_list.append(past_problem)


@assignment_blueprint.route('/active_assignments', methods=['GET'])
def get_active_assignments():
    return render_template('active_assignments.html', user_assignments=assignment_list)


@assignment_blueprint.route('/active_assignments/<assignment>', methods=['GET'])
def get_problems(assignment):
    the_assignment = get_problems_with_assignment(assignment)
    return render_template('problems.html', assignment=the_assignment)


@assignment_blueprint.route('/active_assignments/<assignment>/<problem>', methods=['GET'])
def get_problem_details(assignment, problem):
    problem = get_single_problem(assignment, problem)
    return render_template('problem.html', problem=problem)

@assignment_blueprint.route('/active_assignments/<assignment>/<problem>', methods=['GET'])
def get_assignment_problem(assignment, problem):
    return "Your assignment is {} and the problem is {}".format(assignment, problem)

@assignment_blueprint.route('/past_assignments', methods=['GET'])
def get_past_assigments():
	return render_template('past_assignmets.html', past_assignment=past_assignment_list)

@assignment_blueprint.route('/past_assignments/<assignment>', methods=['GET'])
def get_past_problems(assignment):
	assignment = get_past_problems_with_assignments(assignment)
	return render_template('problems.html', assignment=assignment)

@assignment_blueprint.route('/past_assignments/<assignment>/<problem>', methods=['GET'])
def get_past_assigment_problem(assignment, problem):
	problem = get_single_past_problem(assignment, problem)
	return render_template('problem.html', problem=problem)

def get_problems_with_assignment(name):
    for assignment in assignment_list:
        if assignment.name == name:
            return assignment

def get_past_problems_with_assignments(name):
	for assignment in past_assignment_list:
		if assignment.name == name:
			return assignment

def get_single_past_problem(assignment, problem_name):
	assignment = get_past_problems_with_assignments(assignment)
	for problem in assignment.problem_list:
		if problem.name == problem_name:
			return problem

def get_single_problem(assignment, problem_name):
    assignment = get_problems_with_assignment(assignment)
    for problem in assignment.problem_list:
        if problem.name == problem_name:
            return problem