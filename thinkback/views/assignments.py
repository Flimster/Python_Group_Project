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
assignment1 = Assignment("Basics in python", True)
assignment1.create_problem("Hello world", "Simply print out hello world")
assignment1.create_problem(
    "If statements", "Do something simple with if statements")
assignment1.create_problem(
    "While loops", "Do something simple with while loops")
assignment1.create_problem(
    "AI", "Use machine learning techniques that you learned to create an AI to determine the probabilty of human destructoin")
assignment2 = Assignment("Advance mathematics in python", True)
assignment_list.append(assignment1)
assignment_list.append(assignment2)
# Testing for past assigments
assignment3 = Assignment("Number Lists", False)
assignment3.create_problem("Create an asc. number list", "33% of grade")
assignment3.create_problem("Create a desc. number list", "33% of grade")
assignment3.create_problem(
    "Calculate the std. deviation of all the numbers", "33% of grade")
assignment_list.append(assignment3)

# Gives the right path to the 'link' coming in, and also gets a right question list


@assignment_blueprint.route('/<link>', methods=['GET'])
def get_assignment_path(link):
    if link == 'active_assignments':
        return render_template('active_assignments.html', link=link, active_assignments=assignment_list)
    if link == 'past_assignments':
        return render_template('past_assignments.html', link=link, past_assignment=assignment_list)
    else:
        return "Something went wrong"

# Broken, havent been able to pass on the correct assigments list


@assignment_blueprint.route('/<link>/<assignment>', methods=['GET'])
def get_assignment(link, assignment):
    find_questions = find_problems_with_assignment(assignment)
    return render_template('assignment_problems_list.html', link=link, assignment=find_questions)


@assignment_blueprint.route('/<link>/<assignment>/<problem>', methods=['GET'])
def get_problems(link, assignment, problem):
    problem = get_problem_info(assignment, problem)
    return render_template('problem.html', link=link, assignment_name=assignment, problem=problem)


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
            function_name = get_problem_info(assignment_name, problem_id).function_name
            problem_function = getattr(problem_module, function_name)
            problem_function(1, 2)
            return redirect(request.url)

    # TODO: Return error that something went wrong
    return ""


def find_problems_with_assignment(assignment_name):
    for assignment in assignment_list:
        if assignment.name == assignment_name:
            return assignment


def get_problem_info(assignment, problem_id):
    assignment = find_problems_with_assignment(assignment)
    for problem in assignment.problem_list:
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
    filename = filename.split('.')
    module = importlib.import_module(
        '.{}'.format(filename[0]), package=module_path)
    return module
