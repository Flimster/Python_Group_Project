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
        return render_template('active_assignments.html', link=link, active_assignments=assignment_list)
    if link == 'past_assignments': 
        return render_template('past_assignments.html', link=link, past_assignment=assignment_list)
    else: return "Something went wrong"

#Broken, havent been able to pass on the correct assigments list
@assignment_blueprint.route('/<link>/<assignment>', methods=['GET'])
def get_assignment(link, assignment):
    find_questions = problems_finder(assignment)
    return render_template('assignment_problems_list.html', link=link , assignment=find_questions)

@assignment_blueprint.route('/<link>/<assignment>/<problem>', methods=['GET'])
def get_problems(link, assignment, problem):
    print('IWAS HERE OKAY-------------------------------------')
    return render_template('problem.html', problem=problem)

def problems_finder(assignment_name):
    for assignment in assignment_list:
        if assignment.name == assignment_name:
            return assignment