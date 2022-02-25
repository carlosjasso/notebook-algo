import unittest
from datetime import datetime
from src.sorting import Sorting
from helper import print_ruled, print_took
from configuration import Configuration

class Test_Sorting(unittest.TestCase):
    config: Configuration

    @classmethod
    def setUpClass(self):
        self.config = Configuration()

    def test_buble_sort(self):
        print_ruled("Testing bubble sort")
        expected = self.config.int_array.copy()
        expected.sort()
        start = datetime.now()
        actual = Sorting.bubble(self.config.int_array)
        print_took(start)
        self.assertListEqual(actual, expected)
