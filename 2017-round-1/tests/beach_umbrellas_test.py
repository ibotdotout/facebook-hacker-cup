import beach_umbrellas as bu
import unittest


class ProgressPieTest(unittest.TestCase):

    def _helper_assert(self, inputs, expected):
        n, m, umbrellas = inputs
        res = bu.solve(n, m, umbrellas)
        self.assertEqual(expected, res)

    def test_1_should_be_24(self):
        inputs = [3, 6, [1, 1, 1]]
        self._helper_assert(inputs, 24)

    def test_2_should_be_6(self):
        inputs = [2, 5, [1, 2]]
        self._helper_assert(inputs, 6)

    def test_3_should_be_916295601(self):
        inputs = [3, 2000, [1, 2, 3]]
        self._helper_assert(inputs, 916295601)

    def test_4_should_be_12(self):
        inputs = [5, 22, [1, 2, 3, 4, 5]]
        self._helper_assert(inputs, 12)

    def test_5_should_be_10(self):
        inputs = [1, 10, [50]]
        self._helper_assert(inputs, 10)

    # mytest
    def test_extra1_should_be_20(self):
        inputs = [2, 6, [1, 2]]
        self._helper_assert(inputs, 12)

    def test_extra2_should_be_20(self):
        inputs = [2, 7, [1, 2]]
        self._helper_assert(inputs, 20)
