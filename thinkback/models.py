import uuid
import json

class Assignment:
	def __init__(self, name, description, active):
		self.name = name
		self.description = description
		self.problem_list = []
		self.active = active

	def toJson(self):
		 return {"name": self.name, "problem_list": self.problem_list, "active": self.active }

	def create_problem(self, name, desc):
		self.problem_list.append(Problem(name, desc, self.name))


class Problem:
	def __init__(self, name, desc, assignment_name):
		self.name = name
		self.desc = desc
		self.assignment_name = assignment_name
		self.id = str(uuid.uuid4())
	
	def toJson(self):
		 return {"name": self.name, "description": self.desc, "id": self.id}
