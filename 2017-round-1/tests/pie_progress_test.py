import pie_progress as pp
import unittest


class PieProgressTest(unittest.TestCase):

    def _helper_assert(self, inputs, expected):
        n, m, prices = inputs
        res = pp.solve(n, m, prices)
        self.assertEqual(expected, res)

    def test_1_should_be_107(self):
        inputs = [3, 2, [[1, 1], [100, 100], [10000, 10000]]]
        self._helper_assert(inputs, 107)

    def test_2_should_be_20(self):
        inputs = [5, 1, [[1], [2], [3], [4], [5]]]
        self._helper_assert(inputs, 20)

    def test_3_should_be_10(self):
        inputs = [5, 5, [
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 1],
            [3, 4, 5, 1, 2],
            [4, 5, 1, 2, 3],
            [5, 1, 2, 3, 4]]]
        self._helper_assert(inputs, 10)

    def test_4_should_be_18(self):
        inputs = [5, 5, [
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5]]]
        self._helper_assert(inputs, 18)

    def test_5_should_be_79(self):
        inputs = [10, 4, [
            [7, 15, 12, 6],
            [15, 3, 19, 18],
            [10, 9, 10, 14],
            [12, 14, 8, 8],
            [5, 3, 5, 11],
            [9, 14, 19, 11],
            [12, 6, 20, 9],
            [18, 13, 12, 15],
            [14, 14, 10, 20],
            [11, 19, 12, 11]]
        ]
        self._helper_assert(inputs, 79)
