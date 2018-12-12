import os
import uuid
import json
import importlib
from flask import current_app as app


class Assignment:
	def __init__(self, name, description, active):
		self.name = name
		self.problem_list = []
		self.active = active

	def toJson(self):
		return {"name": self.name, "problem_list": self.problem_list, "active": self.active}

	def create_problem(self, name, desc):
		self.problem_list.append(Problem(name, desc, "sum_two", self.name))


class Problem:
	def __init__(self, name, desc, function_name, assignment_name):
		self.name = name
		self.desc = desc
		self.assignment_name = assignment_name
		self.function_name = function_name
		self.id = str(uuid.uuid4())

	def toJson(self):
		return {"name": self.name, "description": self.desc, "id": self.id}


class UploadedFile:
	def __init__(self, file):
		self.file = file
		self._allowed_extensions = set(['py'])

	def is_empty(self):
		if self.file.filename == '':
			return True
		return False

	def is_allowed(self):
		return '.' in self.file.filename and \
			self.file.filename.rsplit('.', 1)[1].lower() in self._allowed_extensions

	def create_file_path(self, problem_id):
		return os.path.join(app.config['UPLOAD_FOLDER'], ''.join(problem_id))

	def save_file_to_path(self, path, secure_filename):
		self.file.save(os.path.join(path, secure_filename))
		self.file.save(os.path.join(path, '__init__.py'))

	def get_file_module(self, module_path, filename):
		filename = filename.split('.')
		module = importlib.import_module('.{}'.format(filename[0]), package=module_path)
		return module

class TestCase:
	def __init__(self, problem_id):
		self.expected_values_list = []
