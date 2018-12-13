import uuid
import json

class Assignment:
	def __init__(self, name, description, active):
		self.id = str(uuid.uuid4())
		self.name = name
		self.active = active

class Problem:
	def __init__(self, name, desc, function_name, assignment_name):
		self.id = str(uuid.uuid4())
		self.name = name
		self.desc = desc
		self.assignment_name = assignment_name
		self.function_name = function_name