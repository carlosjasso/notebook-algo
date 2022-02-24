from cgi import test
import unittest
from sorting import bubble

class Test_Sorting(unittest.TestCase):
    def test_buble_sort(self):
        data = [123, 4, 456, 2, 456, -9, 0, 234, 7]
        actual = bubble.sort_array(data)
        data.sort()
        self.assertListEqual(actual, data)
