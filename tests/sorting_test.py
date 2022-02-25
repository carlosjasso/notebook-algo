from cgi import test
import unittest
from src.sorting import Sorting

class Test_Sorting(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self._int_arr = [
            3705, 1321, -1202, 2668, 4474, -123, -1152, 3486, 2324, -773, 2934,
            2541, 1669, -735, 1784, -5, 1166, 3438, 3197, -653, 3912, 3842, 4482,
            4387, 1300, 2363, 2518, 958, -1094, 2909, 3399, 3599, -339, 371, 795,
            1005, 563, 1481, 3511, -1192, 3773, 4769, -651, -68, 3919, -1128, -618,
            4749, 2984, -30, 4183, 2109, 4170, 4072, 2076, 4558, 729, 4169, 1973,
            -81, -767, 3067, 4009, 2207, 1306, -655, 720, -287, 1550, -1183, 764,
            -1140, 3676, 4414, 3843, 1802, 3334, 4545, 208, -3, 1486, 3666, 1459,
            3948, 2101, 2689, 3590, -182, 937, 749, -285, -1010, 2003, 3416, 900,
            1428, 1588, 3233, 2809, 1087, 1974, 990, 175, 1456, 1134, 3751, 3593,
            3911, 1897, 3265, -858, 4635, 3752, 4553, -164, 2493, 2288, -94, 3860,
            2545, 3639, 1455, 941, -757, 2429, 1235, -418, 4584, -354, -272, -603,
            142, -733, 3906, 320, 2528, -339, -861, 2022, 3614, -622, -440, 1728, 4812,
            -152, 757, 1108, 1865, -874, -25, 617, 3176, 1821, 1448, 2520, 3147, 4173,
            3623, 2504, 2183, 316, 2445, 1718, 2860, 3568, 1425, 4051, 4534, 1989,
            1093, 3956, 4372, -403, -516, 761, 343, 2137, 292, 3265, 1550, 4419, -233,
            -987, 1327, 2472, 622, 3209, -221, 2412, 1647, 3498, 2824, 326, 2407, -359,
            3191, 4164, -154, 2456, 1484
        ]

    def test_buble_sort(self):
        actual = Sorting.bubbble_sort(self._int_arr)
        expected = self._int_arr.copy()
        expected.sort()
        self.assertListEqual(actual, expected)
