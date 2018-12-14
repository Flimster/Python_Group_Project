# thinkback/views/assignments.py
import os
import sqlite3
import importlib
from ..models import Assignment, Problem, UploadedFile
from flask import current_app as app
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, redirect, flash, url_for, g

ALLOWED_EXTENSIONS = set(['py'])

assignment_blueprint = Blueprint('/assignments', __name__)

# Gives the right path to the 'link' coming in, and also gets a right question list


@assignment_blueprint.route('/<link>', methods=['GET'])
def get_assignment_path(link):
	assignment_list = get_db_assignments()
	problem_list = get_db_problems()
	for assignment in assignment_list:
		for problem in problem_list:
			if problem.assignment_id == assignment.id:
				assignment.problem_list.append(problem)

	if link == 'active_assignments':
		return render_template('assignments.html', assignment_list=filter_assignments(assignment_list, 1))
	if link == 'past_assignments':
		return render_template('assignments.html', assignment_list=filter_assignments(assignment_list, 0))
	return "Something went wrong"


@assignment_blueprint.route('/<link>/<problem_id>', methods=['GET'])
def get_problems(link, problem_id):
	problem = get_single_problem(problem_id)
	return render_template('problem.html', link=link, problem=problem)


@assignment_blueprint.route('/<link>/<problem_id>', methods=['POST'])
def upload_file(link, problem_id):
	if request.method == 'POST':
		# Check if the post request has a file in it
		file = request.files['file']
		submitted_file = UploadedFile(file)

		if submitted_file.is_empty():
			flash("Something went wrong")
			return redirect(request.url)

		if submitted_file.file and submitted_file.is_allowed():
			filename = secure_filename(file.filename)
			path = submitted_file.create_file_path(problem_id)

			if not os.path.exists(path):
				os.makedirs(path)
			
			submitted_file.save_file_to_path(path, filename)
			module_path = '.uploads.{}'.format(problem_id)
			problem_module = submitted_file.get_file_module(module_path, filename)
			function_name = get_function_name(problem_id)
			problem_function = getattr(problem_module, function_name)
			print(problem_function(432))
			return redirect(request.url)

	# TODO: Return error that something went wrong
	return ""

def filter_assignments(assignments, status):
	filtered_assignment_list = []
	for assignment in assignments:
		if assignment.active == status:
			filtered_assignment_list.append(assignment)
	return filtered_assignment_list


def get_db_assignments():
	assignment_list = []
	db = get_db()
	cur = db.execute('select * from assignments')
	entries = cur.fetchall()
	for assignment in entries:
		assignment_list.append(Assignment(
			assignment['a_id'], assignment['a_name'], assignment['a_active']))
	return assignment_list


def get_db_problems():
	problem_list = []
	db = get_db()
	cur = db.execute('select * from problems')
	entries = cur.fetchall()
	for problem in entries:
		problem_list.append(Problem(
			problem['p_id'], problem['a_id'], problem['p_name'], problem['p_desc'], problem['p_solution_name']))
	return problem_list

def get_single_problem(problem_id):
	db = get_db()
	cur = db.execute('select * from problems P where P.p_id = {}'.format(problem_id))
	entry = cur.fetchone()
	problem = Problem(entry['p_id'], entry['a_id'], entry['p_name'], entry['p_desc'], entry['p_solution_name'])
	return problem


def get_function_name(problem_id):
	db = get_db()
	cur = db.execute('select P.p_solution_name from Problems P where P.p_id = {}'.format(problem_id))
	entry = cur.fetchone()
	return entry['p_solution_name']

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
