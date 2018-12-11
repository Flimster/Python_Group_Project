# thinkback/views/assignments.py

from ..models import Assignment
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, redirect, flash, url_for


assignment_blueprint = Blueprint('/assignments', __name__)

# TODO: Delete this
# This is used for testing the various routes
assignment_list = []
assignment1 = Assignment("Basics in python", True)
assignment1.create_problem("Hello world", "Simply print out hello world")
assignment1.create_problem("If statements", "Do something simple with if statements")
assignment1.create_problem("While loops", "Do something simple with while loops")
assignment1.create_problem("AI", "Use machine learning techniques that you learned to create an AI to determine the probabilty of human destructoin")
assignment2 = Assignment("Advance mathematics in python", True)
assignment_list.append(assignment1)
assignment_list.append(assignment2)
#Testing for past assigments
assignment3 = Assignment("Number Lists", False)
assignment3.create_problem("Create an asc. number list", "33% of grade")
assignment3.create_problem("Create a desc. number list", "33% of grade")
assignment3.create_problem("Calculate the std. deviation of all the numbers", "33% of grade")
assignment_list.append(assignment3)

@assignment_blueprint.route('/<status>', methods=['GET'])
def get_assignments(status):
    if status == 'active_assignments': 
        return render_template('active_assignments.html', user_assignments=assignment_list)
    if status == 'past_assignments': 
        return render_template('past_assignments.html', past_assignment=assignment_list)
    else: return "Something went wrong"

@assignment_blueprint.route('/<link>/<assignment>', methods=['GET'])
def get_problem(assignment, status, link):
    specific_assignment = get_assignment(assignment, status, link)
    return render_template('multiple_problems.html', assignment=specific_assignment)


#This function is used to look up active or inactive assignments
@assignment_blueprint.route('/<link>/<assignment>/<assignment_name>')
def get_assignment(assignment, status, link):
    for assignment in assignment_list:
        if status == 'active_assignments':
            if assignment.active == True:
                return assignment
        if status == 'past_assignments':
            if assignment.active == False:
                return assignment

# @assignment_blueprint.route('/active_assignments', methods=['GET'])
# def get_active_assignments():
    

# @assignment_blueprint.route('/active_assignments/<assignment>', methods=['GET'])
# def get_problems(assignment):
#     the_assignment = get_problems_with_assignment(assignment)
#     return render_template('multiple_problems.html', assignment=the_assignment)

# @assignment_blueprint.route('/active_assignments/<assignment>/<problem>', methods=['GET'])
# def get_problem_details(assignment, problem):
#     problem = get_single_problem(assignment, problem)
#     return render_template('single_problem.html', problem=problem)

# @assignment_blueprint.route('/active_assignments/<assignment>/<problem>', methods=['GET'])
# def get_assignment_problem(assignment, problem):
#     return "Your assignment is {} and the problem is {}".format(assignment, problem)

# # @assignment_blueprint.route('/past_assignments', methods=['GET'])
# # def get_past_assigments():
    
# @assignment_blueprint.route('/past_assignments/<assignment>', methods=['GET'])
# def get_past_problems(assignment):
#     assignment = get_past_problems_with_assignments(assignment)
#     return render_template('multiple_problems.html', assignment=assignment)

# @assignment_blueprint.route('/past_assignments/<assignment>/<problem>', methods=['GET'])
# def get_past_assigment_problem(assignment, problem):
#     problem = get_single_past_problem(assignment, problem)
#     return render_template('single_problem.html', assignment=assignment, problem=problem)




# def get_problems_with_assignment(name):
#     for assignment in assignment_list:
#         if assignment.name == name:
#             return assignment

# def get_past_problems_with_assignments(name):
#     for assignment in assignment_list:
#         if assignment.name == name:
#             return assignment

# def get_single_past_problem(assignment, problem_name):
#     assignment = get_past_problems_with_assignments(assignment)
#     for problem in assignment.problem_list:
#         if problem.name == problem_name:
#             return problem

# def get_single_problem(assignment, problem_name):
#     assignment = get_problems_with_assignment(assignment)
#     for problem in assignment.problem_list:
#         if problem.name == problem_name:
#             return problem

