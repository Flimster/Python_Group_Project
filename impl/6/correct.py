import unittest
# Solution for the print out a input
class Solution(unittest.TestCase):
	def __init__(self, func):
		super().__init__()
		self.func = func
		self.values = [1, 2, 3, 4 ,5, 6, 0, -32, -1 ,2, 143, -324, -0]
	
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
		if 0 <= a:
			return True
		return False