# thinkback/views/assignments.py
from collections import defaultdict
import os
import sqlite3
import importlib
from ..models import Assignment, Problem
from flask import current_app as app
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, redirect, flash, url_for, g

ALLOWED_EXTENSIONS = set(['py'])

assignment_blueprint = Blueprint('/assignments', __name__)

# Gives the right path to the 'link' coming in, and also gets a right question list

@assignment_blueprint.route('/<link>', methods=['GET'])
def get_assignment_path(link):
    assignment_list = filter_assignments(1)
    problem_list = get_db_problems()
    print(problem_list)
    problems_dict = defaultdict()
    for assignment in assignment_list:
        for problem in problem_list:
            if problem.assignment_id == assignment.id:
                problems_dict[assignment.id] = problem
    print(problems_dict)
    if link == 'active_assignments': 
        return render_template('assignments.html', assignment_list=filter_assignments(1))
    if link == 'past_assignments': 
        return render_template('assignments.html', assignment_list=filter_assignments(0))
    return "Something went wrong"

@assignment_blueprint.route('/<link>/<problem>', methods=['GET'])
def get_problems(link, problem_id):
    problem = get_problem_info(problem_id)
    return render_template('problem.html', link=link, problem=problem)


# @assignment_blueprint.route('/<link>/<problem_id>', methods=['POST'])
# def upload_file(link, problem_id):
#     if request.method == 'POST':
#         # Check if the post request has a file in it
#         file = request.files['file']

#         if file.filename == '':
#             flash("Something went wrong")
#             return redirect(request.url)

#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             path = create_file_path(problem_id)

#             if not os.path.exists(path):
#                 os.makedirs(path)

#             save_file_to_path(path, file, filename)

#             module_path = '.uploads.{}'.format(problem_id)
#             problem_module = get_file_module(module_path, filename)
#             function_name = get_problem_info(problem_id).function_name
#             problem_function = getattr(problem_module, function_name)
#             problem_function(1, 2)
#             return redirect(request.url)

#     # TODO: Return error that something went wrong
#     return ""

def filter_assignments(status):
    filtered_assignment_list = []
    for assignment in get_db_assignments():
        if assignment.active == status:
            filtered_assignment_list.append(assignment)
    return filtered_assignment_list

def get_problem_by_assignment_id(assignment_id):
    print('SADSAJJDSAJDSADSAJ')
    problems = get_db_problems()
    problem_list = []
    for p in problems:
        if p.assignment_id == assignment_id:
            problem_list.append(p)
    return problem_list

def get_problem_info(problem_id):
    assignment = get_assignment_by_problem_id(problem_id)
    for problem in assignment.problem_list:
        if problem.id == problem_id:
            return problem

def get_assignment_by_problem_id(problem_id):
    for assignment in get_db_assignments():
        for problem in assignment.problem_list:
            if problem.id == problem_id:
                return assignment

def get_db_assignments():
    assignment_list = []
    db = get_db()
    cur = db.execute('select * from assignments')
    entries = cur.fetchall()
    for assignment in entries:
        assignment_list.append(Assignment(assignment['a_id'], assignment['a_name'], assignment['a_active']))
    return assignment_list

def get_db_problems():
    problem_list = []
    db = get_db()
    cur = db.execute('select * from problems')
    entries = cur.fetchall()
    for problem in entries:
        problem_list.append(Problem(problem['p_name'], problem['p_desc'], problem['p_solution_name'], problem['a_id']))
    return problem_list#render_template('/', entries=entries)

def connect_db():
    print("""Connects to the specific database.""")
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    print("""Opens a new database connection if there is none yet for the
	current application context.
	""")
    if not hasattr(g, 'thinkback.db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def drop_db():
    db = get_db()
    with app.open_resource('drop.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
