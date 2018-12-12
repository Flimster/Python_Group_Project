# thinkback/views/assignments.py

import os
import importlib
from ..models import Assignment
from flask import current_app as app
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, redirect, flash, url_for


ALLOWED_EXTENSIONS = set(['py'])

assignment_blueprint = Blueprint('/assignments', __name__)

# TODO: Delete this
# This is used for testing the various routes
assignment_list = []
assignment1 = Assignment("Basics in python", "People search for this Lorem ipsum dummy copy text using all kinds of names, such as Lorem ipsum, lorem ipsum dolor sit amet, Lorem, dummy text, loren ipsum (yes, spelled wrong)", True)
assignment1.create_problem("Hello world", "Simply print out hello world")
assignment1.create_problem("If statements", "Do something simple with if statements")
assignment1.create_problem("While loops", "Do something simple with while loops")
assignment1.create_problem("AI", "Use machine learning techniques that you learned to create an AI to determine the probabilty of human destructoin")
assignment2 = Assignment("Advance mathematics in python", "I’ve seen several versions of this Lorem ipsum text on the Internet, with various changes; however, this Lorem Ipsum dummy copy text doesn’t have any odd text sneaked in as I’ve seen in some of the others.", True)
assignment2.create_problem("TYLER", "Try to be awesome like him")
assignment2.create_problem("INGI", "The cool kid")
assignment_list.append(assignment1)
assignment_list.append(assignment2)
#Testing for past assigments
assignment3 = Assignment("Number Lists", "There is an unformatted plain text (.txt) version to either copy/paste or to save the .txt file to your computer. Note: it’s unformatted and will stretch across your screen. ",False)
assignment3.create_problem("Create an asc. number list", "33% of grade")
assignment3.create_problem("Create a desc. number list", "33% of grade")
assignment3.create_problem(
    "Calculate the std. deviation of all the numbers", "33% of grade")
assignment_list.append(assignment3)

# Gives the right path to the 'link' coming in, and also gets a right question list


@assignment_blueprint.route('/<link>', methods=['GET'])
def get_assignment_path(link):
    if link == 'active_assignments': 
        return render_template('assignments.html', assignment_list=get_assignment_list(True))
    if link == 'past_assignments': 
        return render_template('assignments.html', assignment_list=get_assignment_list(False))
    return "Something went wrong"

@assignment_blueprint.route('/<problem>', methods=['GET'])
def get_problems(problem):
    problem = get_problem_info(problem)
    return render_template('problem.html', problem=problem)

@assignment_blueprint.route('/<link>/<assignment_name>/<problem_id>', methods=['POST'])
def upload_file(link, assignment_name, problem_id):
    """Uploads a file to the server"""
    if request.method == 'POST':
        # Check if the post request has a file in it
        file = request.files['file']

        if file.filename == '':
            flash("Something went wrong")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = create_file_path(problem_id)

            if not os.path.exists(path):
                os.makedirs(path)

            save_file_to_path(path, file, filename)

            module_path = '.uploads.{}'.format(problem_id)
            problem_module = get_file_module(module_path, filename)
            function_name = get_problem_info(problem_id).function_name
            problem_function = getattr(problem_module, function_name)
            problem_function(1, 2)
            return redirect(request.url)

    # TODO: Return error that something went wrong
    return ""

def get_assignment_list(status):
    filtered_assignment_list = []
    for assignment in assignment_list:
        if assignment.active == status:
            filtered_assignment_list.append(assignment)
    return filtered_assignment_list

def get_problem_info(problem_id):
    assignment = find_problems_with_assignment(problem_id)
    for problem in assignment.problem_list:
        if problem.id == problem_id:
            return problem

def find_problems_with_assignment(assignment_name):
    for assignment in assignment_list:
        if assignment.name == assignment_name:
            return assignment

def get_assignment_by_problem_id(problem_id):
    for assigment in assignment_list:
        for problem in assigment:
            if problem.id == problem_id:
                return problem

def has_file(request):
    if 'file' not in request.files:
        return redirect(request.url)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def create_file_path(problem_id):
    path = os.path.join(app.config['UPLOAD_FOLDER'], ''.join(problem_id))
    return path
def save_file_to_path(path, file, secure_filename):
    file.save(os.path.join(path, secure_filename))
    file.save(os.path.join(path, '__init__.py'))
def get_file_module(module_path, filename):
    print(filename)
    filename = filename.split('.')
    module = importlib.import_module(
        '.{}'.format(filename[0]), package=module_path)
    return module