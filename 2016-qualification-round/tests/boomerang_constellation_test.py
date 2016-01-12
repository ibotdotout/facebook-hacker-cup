import boomerang_constellation as bc
import unittest


class BoomerangConstellationTest(unittest.TestCase):

    def _helper_assert(self, stars, expected):
        res = bc.count_boomerang_constellation(stars)
        self.assertEqual(expected, res)

    def test_first_night_should_be_0(self):
        stars = [(0, 0), (0, 1), (0, 3)]
        self._helper_assert(stars, 0)

    def test_second_night_should_be_4(self):
        stars = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
        self._helper_assert(stars, 4)

    def test_third_night_should_be_4(self):
        stars = [(0, 0), (0, 100), (100, 0), (100, 100)]
        self._helper_assert(stars, 4)

    def test_fourth_nigh_should_be_3(self):
        stars = [(0, 0), (-3, 4), (0, 5), (-5, 0)]
        self._helper_assert(stars, 3)

    #  @unittest.skip('')
    def test_fifth_nigh_should_be_12(self):
        stars = [(5, 6), (6, 5), (7, 6), (6, 7), (7, 8), (8, 7)]
        self._helper_assert(stars, 12)
