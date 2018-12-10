class Project:
	def __init__(self, name):
		self.project_name = name
		self.problem_list = []
		self.problem_count = 0

	def create_problem(self, name, description):
		self.problem_list.append(Problem(name, description))
		self.problem_count += 1


class Problem:
	def __init__(self, name, description):
		self.name = name
		self.description = description