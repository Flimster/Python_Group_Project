import unittest
# Solution for the print out a input
class Solution(unittest.TestCase):
	def __init__(self, func):
		super().__init__()
		self.func = func
		self.values = [1, 2, "fdafd", 3.0, True]
	
	def run_tests(self):
		results = {}
		for index, value in enumerate(self.values):
			expected = self._correct(value)
			actual = self.func(value)				
			try:
				self.assertEquals(expected, actual)
				results[index] = "Correct"
			except AssertionError:
				results[index] = "Input: \"{}\" but got \"{}\" of type {}".format(expected, actual, str(type(actual)))
		return results

	def _correct(self, a):
		return str(a)