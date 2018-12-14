import os
import importlib
import unittest
from flask import current_app as app


class Assignment:
	def __init__(self, id, name, active):
		self.id = id
		self.name = name
		self.active = active
		self.problem_list = []

	def __str__(self):
		return '{} {} {}'.format(self.id, self.name, self.active)

class Problem:
	def __init__(self, id, assignment_id, name, desc, function):
		self.id = id
		self.assignment_id = assignment_id
		self.name = name
		self.desc = desc
		self.function = function
		
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
	
	def get_testing_class(self, module_path):
		module = importlib.import_module('.correct', package=module_path)
		return module
