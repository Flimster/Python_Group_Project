# How to create new problems

The Thinkback system expects your solution to be in a specific format.
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
			results[1] = "Input \"{}\" but got \"{}\"".format(expected, actual)
		return results

	def _correct(self, a, b):
		return a + b
		
```
---
The file you upload must be named **correct.py** and it is important to note that the class name must be **Solution** and it must inherit the ```unittest.TestCase``` class to be able to run the tests.
Every function should have the same name as the example above.
The ```_correct``` function contains your correct implementation of the problem.
