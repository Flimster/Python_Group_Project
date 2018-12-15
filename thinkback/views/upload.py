# thinkback/views/upload.py
import os
import sqlite3
import importlib
import shutil
from flask import current_app as app
from ..models import Problem
from ..database import database
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, flash, redirect, g


ALLOWED_EXTENSIONS = ['py']

upload_blueprint = Blueprint('upload', __name__)


@upload_blueprint.route('/<link>/<problem_id>', methods=['POST'])
def upload_file(link, problem_id):
    if request.method == 'POST':
        problem = database.get_single_problem(problem_id)

        if 'file' not in request.files:
            flash('No file was submitted')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash("No selected file")
            return redirect(request.url)

        if file and is_allowed(file):
            filename = secure_filename(file.filename)
            path = create_file_path(problem_id)
            save_files_to_path(file, path, filename)

            module_path = '.uploads.{}'.format(problem_id)
            solution_path = '.impl.{}'.format(problem_id)

            # Try to get the problem module from the file uploaded
            # If that does not succed remove it form the server
            try:
                problem_module = get_file_module(module_path, filename)
            except ModuleNotFoundError as e:
                shutil.rmtree(os.path.abspath(path))
                flash(e, 'danger')
                return render_template('problem.html', link=link, problem=problem)

            function_name = database.get_function_name(problem_id)
            # Try to import the fuction needed for the problem
            try:
                problem_function = getattr(problem_module, function_name)
                solution_module = importlib.import_module(
                    '.correct', package=solution_path)
                solution = solution_module.Solution(problem_function)
                results = solution.run_tests()
                for value in results.values():
                    if value == "Correct":
                        flash(value, 'success')
                    else:
                        flash(value, 'warning')
                problem = database.get_single_problem(problem_id)

            except AttributeError or TypeError as e:
                # If the function did not exists remove the file
                flash(e, 'danger')
                os.remove(os.path.join(path, filename))

    return render_template('problem.html', link=link, problem=problem)


def is_empty(self):
    if self.file.filename == '':
        return True
    return False


def is_allowed(file):
    return '.' in file.filename and \
        file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def create_file_path(problem_id):
    return os.path.join(app.config['UPLOAD_FOLDER'], ''.join(problem_id))


def save_files_to_path(file, path, secure_filename):
    if not os.path.exists(path):
        os.makedirs(path)
    file.save(os.path.join(path, secure_filename))
    file.save(os.path.join(path, '__init__.py'))


def get_file_module(module_path, filename):
    filename = filename.split('.')
    module = importlib.import_module(
        '.{}'.format(filename[0]), package=module_path)
    return module
