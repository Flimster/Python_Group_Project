import uuid

class Assignment:
	def __init__(self, name):
		self.name = name
		self.problem_list = []
		self.problem_count = 0
		self.active = True

	def create_problem(self, name, description):
		self.problem_list.append(Problem(name, description))
		self.problem_count += 1


class Problem:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.id = str(uuid.uuid4())