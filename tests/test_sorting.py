import unittest
from src.sorting import Sorting
from helper import print_ruled, benchmark_start, benchmark_stop
from configuration import Configuration

class Test_Sorting(unittest.TestCase):
    config: Configuration

    @classmethod
    def setUpClass(self):
        self.config = Configuration()

    def test_buble_sort(self):
        print_ruled("Testing bubble sort")
        actual = self.config.int_array
        expected = sorted(actual)
        start = benchmark_start()
        actual = Sorting.bubble(actual)
        benchmark_stop(start)
        self.assertListEqual(actual, expected)
