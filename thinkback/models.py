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