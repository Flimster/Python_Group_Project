from .problem import Problem

class Project:
	def __init__(self):
		self.problem_list = []
		self.counter = 0

	def create_problem(self):
		name = str(self.counter)
		self.problem_list.append(Problem(name, "This is a problem"))
		self.counter += 1