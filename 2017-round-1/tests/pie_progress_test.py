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

    def test_6_should_be_2590(self):
        inputs = [21, 6, [
            [821, 740, 847, 533, 817, 883],
            [481, 686, 703, 389, 965, 962],
            [795, 987, 213, 646, 91, 332],
            [918, 899, 378, 152, 163, 832],
            [89, 943, 303, 481, 20, 151],
            [191, 325, 575, 12, 554, 174],
            [27, 986, 686, 314, 49, 319],
            [256, 214, 586, 692, 174, 593],
            [304, 329, 245, 654, 197, 40],
            [795, 252, 670, 393, 312, 760],
            [843, 549, 694, 258, 902, 655],
            [826, 981, 933, 372, 366, 671],
            [382, 83, 932, 984, 286, 224],
            [825, 72, 733, 730, 883, 705],
            [794, 20, 168, 396, 631, 537],
            [525, 647, 321, 992, 656, 468],
            [510, 759, 131, 525, 362, 532],
            [446, 642, 176, 735, 471, 13],
            [266, 163, 560, 637, 462, 811],
            [309, 239, 749, 201, 856, 764],
            [792, 313, 531, 619, 17, 765]]
        ]
        self._helper_assert(inputs, 2590)
