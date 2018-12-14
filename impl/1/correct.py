import unittest
import json

class HelloWorld(unittest.TestCase):

	def __init__(self, submitted_func):
		super().__init__()
		self.values = [1, 2, 3, 4, 5, 6, 7]
		self.submitted_func = submitted_func

	def run_tests(self):
		results = {}
		for value in self.values:
			expected_value = self._correct(value)
			actual_value = self.submitted_func(value)
			try:
				self.assertEqual(expected_value, actual_value)
				results[value] = "Correct"
			except AssertionError:
				results[value] = "Expected {} but got {}".format(expected_value, actual_value)
		results = json.dumps(results)
		return json.loads(results)
	
	def _correct(self, a):
		return a