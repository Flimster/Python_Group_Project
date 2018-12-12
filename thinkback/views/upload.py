import os
import json
from flask import current_app as app
from werkzeug.utils import secure_filename
from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
import re


UPLOAD_FOLDER = './uploads/python'
ALLOWED_EXTENSIONS = set(['py'])

upload = Blueprint('/upload', __name__)


@upload.route('/upload/<assignment_name>/<problem_id>', methods=['POST'])
def upload_file(assignment_name, problem_id):
	if request.method == 'POST':
		# Check if the post request has a file in it
		file = request.files['file'] 

		if file.filename == '':
				flash('No selected file')
				return redirect(request.url)

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			path = create_file_path(problem_id)
			if not os.path.exists(path):
				os.makedirs(path)
			save_file_to_path(path, file, filename)
			return redirect(url_for('/assignments.get_past_assigment_problem', assignment=assignment_name, problem=problem_id))

	# TODO: Return error that something went wrong
	return ""


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
