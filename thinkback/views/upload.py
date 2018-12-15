# thinkback/views/upload.py
import os
import sqlite3
import importlib
from flask import current_app as app
from ..models import Problem, ProblemModule
from ..database import database
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, flash, redirect, g


upload_blueprint = Blueprint('upload', __name__)


@upload_blueprint.route('/<link>/<problem_id>', methods=['POST'])
def upload_file(link, problem_id):
	if request.method == 'POST':
		problem = database.get_single_problem(problem_id)

		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)

		file = request.files['file']
		submitted_file = ProblemModule(file)
		
		if file.filename == '':
			flash("No selected file")
			return redirect(request.url)


		elif file and submitted_file.is_allowed():
			filename = secure_filename(file.filename)
			path = submitted_file.create_file_path(problem_id)

			if not os.path.exists(path):
				os.makedirs(path)

			submitted_file.save_files_to_path(path, filename)

			module_path = '.uploads.{}'.format(problem_id)
			solution_path = '.impl.{}'.format(problem_id)

			problem_module = submitted_file.get_file_module(
				module_path, filename)
			function_name = database.get_function_name(problem_id)
			# Try to import the fuction needed for the problem
			try:
				problem_function = getattr(problem_module, function_name)
				solution = importlib.import_module(
					'.correct', package=solution_path)
				tmp = solution.Solution(problem_function)
				results = tmp.run_tests()
				problem = database.get_single_problem(problem_id)
			except AttributeError:
				# If the function did not exists remove the file
				flash("Could not import the correct file name")
				os.remove(os.path.join(path, filename))

	return render_template('problem.html', link=link, problem=problem, results=results)
