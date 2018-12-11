class Assignment:
	def __init__(self, name, active):
		self.name = name
		self.problem_list = []
		self.problem_count = 0
		self.active = active

	def create_problem(self, name, desc):
		self.problem_list.append(Problem(name, desc))
		self.problem_count += 1


class Problem:
	def __init__(self, name, desc):
		self.name = name
		self.description = desc
		self.active = True