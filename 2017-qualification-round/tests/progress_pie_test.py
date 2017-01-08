import progress_pie as pp
import unittest


class ProgressPieTest(unittest.TestCase):

    def _helper_assert(self, inputs, expected):
        res = pp.solve(inputs)
        self.assertEqual(expected, res)

    def test_0_55_55_should_be_false2(self):
        inputs = [0, 50, 100]
        self._helper_assert(inputs, False)

    # Sample of Facebook
    def test_0_55_55_should_be_false(self):
        inputs = [0, 55, 55]
        self._helper_assert(inputs, False)

    def test_13_55_55_should_be_true(self):
        inputs = [13, 55, 55]
        self._helper_assert(inputs, True)

    def test_12_55_55_should_be_false(self):
        inputs = [12, 55, 55]
        self._helper_assert(inputs, False)

    def test_99_99_99_should_be_false(self):
        inputs = [99, 99, 99]
        self._helper_assert(inputs, False)

    def test_87_20_40_should_be_True(self):
        inputs = [87, 20, 40]
        self._helper_assert(inputs, True)

    # Test Q1
    def test_0_75_75_should_be_false(self):
        inputs = [0, 75, 75]
        self._helper_assert(inputs, False)

    def test_25_75_75_should_be_true(self):
        inputs = [25, 75, 75]
        self._helper_assert(inputs, True)

    # Test Q2
    def test_25_75_25_should_be_false(self):
        inputs = [25, 75, 25]
        self._helper_assert(inputs, False)

    def test_50_75_25_should_be_true(self):
        inputs = [50, 75, 25]
        self._helper_assert(inputs, True)

    # Test Q3
    def test_50_25_25_should_be_false(self):
        inputs = [25, 25, 25]
        self._helper_assert(inputs, False)

    def test_75_25_25_should_be_true(self):
        inputs = [75, 25, 25]
        self._helper_assert(inputs, True)

    # Test Q4
    def test_75_25_75_should_be_false(self):
        inputs = [75, 25, 75]
        self._helper_assert(inputs, False)

    def test_100_25_75_should_be_true(self):
        inputs = [100, 25, 75]
        self._helper_assert(inputs, True)
