import uuid
import json

class Assignment:
	def __init__(self, name, active):
		self.name = name
		self.problem_list = []
		self.active = True

	def toJson(self):
		 return {"name": self.name, "problem_list": self.problem_list, "active": self.active }

	def create_problem(self, name, description):
		self.problem_list.append(Problem(name, description))


class Problem:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.id = str(uuid.uuid4())
	
	def toJson(self):
		 return {"name": self.name, "description": self.description, "id": self.id}