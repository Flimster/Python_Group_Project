import unittest
# Solution for the print out a input
class Solution(unittest.TestCase):
	def __init__(self, func):
		super().__init__()
		self.func = func
		self.values = [1, 2, 3, 10, 12, 15]
	
	def run_tests(self):
		results = {}
		for index, value in enumerate(self.values):
			expected = self._correct(value)
			actual = self.func(value)				
			try:
				self.assertEquals(expected, actual)
				results[index] = "Correct"
			except AssertionError:
				results[index] = "Expected \"{}\" but got \"{}\"".format(expected, actual)
		return results

	def _correct(self, a):
		string_built = '|'
		for i in range(a):
			string_built += str(i) + '|'
		return string_built