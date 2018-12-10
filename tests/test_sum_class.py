import pytest
import impl

class TestSum:

	def test_one_two(self):
		f = impl.sum(1, 2)
		assert f == 3, "Expected output: 3. Optained output: {}".format(f)

	def test_one_four(self):
		f = impl.sum(1, 4)
		assert f == 5, "Expected output: 5. Optained output: {}".format(f)