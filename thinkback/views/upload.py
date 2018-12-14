# thinkback/views/upload.py
import os
import sqlite3
import importlib
from flask import current_app as app
from ..models import Problem, ProblemModule
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, flash, redirect, g


upload_blueprint = Blueprint('upload', __name__)


@upload_blueprint.route('/<link>/<problem_id>', methods=['POST'])
def upload_file(link, problem_id):
    if request.method == 'POST':
        # Check if the post request has a file in it
        file = request.files['file']

        submitted_file = ProblemModule(file)
        if submitted_file.is_empty():
            flash("Something went wrong")
            return redirect(request.url)

        if submitted_file.file and submitted_file.is_allowed():
            filename = secure_filename(file.filename)
            path = submitted_file.create_file_path(problem_id)

            if not os.path.exists(path):
                os.makedirs(path)

            submitted_file.save_files_to_path(path, filename)

            module_path = '.uploads.{}'.format(problem_id)
            solution_path = '.impl.{}'.format(problem_id)

            problem_module = submitted_file.get_file_module(
                module_path, filename)
            function_name = get_function_name(problem_id)
            # Try to import the fuction needed for the problem
            try:
                problem_function = getattr(problem_module, function_name)
                solution = importlib.import_module(
                    '.correct', package=solution_path)
                tmp = solution.Solution(problem_function)
                results = tmp.run_tests()
                problem = get_single_problem(problem_id)
                return render_template('problem.html', link=link, problem=problem, results=results)
            except AttributeError:
                # If the function did not exists remove the file
                os.remove(os.path.join(path, filename))
            return redirect(request.url)

    # TODO: Return error that something went wrong
    return ""

def get_single_problem(problem_id):
	db = get_db()
	cur = db.execute(
		'select * from problems P where P.p_id = {}'.format(problem_id))
	entry = cur.fetchone()
	problem = Problem(entry['p_id'], entry['a_id'], entry['p_name'],
					  entry['p_desc'], entry['p_solution_name'])
	return problem


def get_function_name(problem_id):
	db = get_db()
	cur = db.execute(
		'select P.p_solution_name from Problems P where P.p_id = {}'.format(problem_id))
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
