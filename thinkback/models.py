import uuid
import json

class Assignment:
	def __init__(self, name, active):
		self.name = name
		self.problem_list = []
		self.active = active

	def toJson(self):
		 return {"name": self.name, "problem_list": self.problem_list, "active": self.active }

	def create_problem(self, name, desc):
		self.problem_list.append(Problem(name, desc))


class Problem:
	def __init__(self, name, desc):
		self.name = name
		self.desc = desc
		self.id = str(uuid.uuid4())
	
	def toJson(self):
		 return {"name": self.name, "description": self.desc, "id": self.id}
