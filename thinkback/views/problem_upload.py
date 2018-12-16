# thinkback/views/problem_upload.py
import os
from ..database import database
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, flash, redirect, url_for

problem_upload_blueprint = Blueprint('problem_upload', __name__)


@problem_upload_blueprint.route('/<assignment_id>', methods=['POST'])
def upload(assignment_id):
	name = request.form['problem_name']
	desc = request.form['problem_desc']
	func_name = request.form['function_name']

	if 'file' not in request.files:
		flash('No file was submitted')
		return redirect(request.url)

	file = request.files['file']
	filename = secure_filename(file.filename)

	if filename != 'correct.py':
		flash('The filename has to be correct.py')
		return redirect(request.url)

	path = os.path.join('./impl', str(database.get_max_problem_id() + 1))

	if not os.path.exists(path):
		os.makedirs(path)
		file.save(os.path.join(path, filename))
		file.save(os.path.join(path, '__init__.py'))
	
	database.insert_problem(assignment_id, name, desc, func_name)

	return redirect(url_for('/assignments.get_assignment_path', link='active_assignments'))
