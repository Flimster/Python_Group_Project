import pytest
from impl import sum_two

class TestSum:

	def test_one_two(self):
		f = sum_two(1, 2)
		assert f == 3, "Expected output: 3. Optained output: {}".format(f)

	def test_one_four(self):
		f = sum_two(1, 4)
		assert f == 5, "Expected output: 5. Optained output: {}".format(f)