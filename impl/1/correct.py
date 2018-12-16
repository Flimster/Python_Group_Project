import unittest
# Solution for the hello_world
class Solution(unittest.TestCase):
	def __init__(self, func):
		super().__init__()
		self.func = func
	
	def run_tests(self):
		results = {}
		try:
			actual = self.func()
			expected = self._correct()
		except TypeError as e:
			return e
		try:
			self.assertEquals(expected, actual)
			results[1] = "Correct"
		except AssertionError:
			results[1] = "Input \"{}\" but got \"{}\"".format(expected, actual)
		return results

	def _correct(self):
		return "Hello world!"
