import unittest
# Solution for the hello_world
class Solution(unittest.TestCase):
	def __init__(self, func):
		super().__init__()
		self.func = func
	
	def run_tests(self):
		results = {}
		expected = self._correct()
		actual = self.func()
		try:
			self.assertEquals(expected, actual)
			results[1] = "Correct"
		except AssertionError:
			results[1] = "Expected \"{}\" but got \"{}\"".format(expected, actual)
		return results

	def _correct(self):
		return "Hello world!"
