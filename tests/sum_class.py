import pytest
import impl

class TestSum:

	def test_one_two(self):
		f = impl.sum(1, 2)
		assert f == 3

	def test_one_three(self):
		f = impl.sum(1, 3)
		assert f == 3