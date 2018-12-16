# How to create new problems

The Thinkback system expectes solutions to be of a specific format
An example for a solution can be found below, this specific problem asks for two numbers **a, b** and returns the sum of those numbers.

---
```python
import unittest
class Solution(unittest.TestCase):
	def __init__(self, func):
		super().__init__()
		self.func = func
		self.values = [[1,2], [12,42], [12,22], [62,236], [123,2234], [1234, 987]]
	
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
			results[1] = "Expected \"{}\" but got \"{}\"".format(expected, actual)
		return results

	def _correct(self, a, b):
		return a + b
		
```
---

It is important to note that the class must inherit ```python unittest.TestCase``` to be able to run the tests.
The class name and functions name must be the same in your upload for the problem.
The ```python _correct function``` contains your correct implementation of the problem.
