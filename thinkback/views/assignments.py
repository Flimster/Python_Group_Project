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

#Gives the right path to the 'link' coming in, and also gets a right question list
@assignment_blueprint.route('/<link>', methods=['GET'])
def get_assignment_path(link):
    if link == 'active_assignments': 
        return render_template('active_assignments.html', active_assignments=assignment_list)
    if link == 'past_assignments': 
        return render_template('past_assignments.html', past_assignment=assignment_list)
    else: return "Something went wrong"

#Broken, havent been able to pass on the correct assigments list
@assignment_blueprint.route('/<link>/<assignment>', methods=['GET'])
def get_assignment(link, assignment):
    print(assignment)
    find_questions = problems_finder(assignment)
    return render_template('assignment_problems_list.html', assignment=find_questions)

# @assignment_blueprint.route('/<link>/<assignment>/<problem>', methods=['GET'])
# def get_assignment_problems(link, assignment):
#     print('IWAS HERE OKAY-------------------------------------')
#     return render_template('question_list.html', assignment=find_questions)

def problems_finder(assignment_name):
    for assignment in assignment_list:
        if assignment.name == assignment_name:
            print(assignment.problem_list)
            return assignment.problem_list


#   def get_problems_with_assignment(name):
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



#This function is used to look up active or inactive assignments
# def get_assignment(assignment, status, link):
#     for assignment in assignment_list:
#         if status == 'active_assignments':
#             if assignment.active == True:
#                 return assignment
#         if status == 'past_assignments':
#             if assignment.active == False:
#                 return assignment

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