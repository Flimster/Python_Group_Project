import unittest
# Solution for the sum_two problem
class Solution(unittest.TestCase):
	def __init__(self, func):
		super().__init__()
		self.func = func
		self.values = [[1,2], [12,42], [12,22], [62,236], [123,2234], [1234, 987]]
	
	def run_tests(self):
		results = {}
		for index, value in enumerate(self.values):
			expected = self._correct(value[0], value[1])
			actual = self.func(value[0], value[1])				
			try:
				self.assertEquals(expected, actual)
				results[index] = "Correct"
			except AssertionError:
				results[index] = "Input {} but got \"{}\"".format(value, actual)
		return results

	def _correct(self, a, b):
		return a + b