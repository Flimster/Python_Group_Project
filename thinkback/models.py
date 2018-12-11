import uuid
import json

class Assignment:
	def __init__(self, name):
		self.name = name
		self.problem_list = []
		self.problem_count = 0
		self.active = True

	def toJson(self):
		 return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

	def create_problem(self, name, description):
		self.problem_list.append(Problem(name, description))
		self.problem_count += 1


class Problem:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.id = str(uuid.uuid4())
	
	def toJson(self):
		 return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)