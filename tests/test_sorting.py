import unittest
from src import sorting
import helper
from configuration import Configuration

class Test_Sorting(unittest.TestCase):
    config: Configuration

    @classmethod
    def setUpClass(self):
        self.config = Configuration()

    def test_buble_sort(self):
        helper.print_ruled("Testing bubble sort")
        actual = self.config.int_array
        expected = sorted(actual)
        start = helper.benchmark_start()
        actual = sorting.bubble(actual)
        helper.benchmark_stop(start)
        self.assertListEqual(actual, expected)

    def test_insert_sort(self):
        helper.print_ruled("Testing insert sort")
        actual = self.config.int_array
        expected = sorted(actual)
        start = helper.benchmark_start()
        actual = sorting.insert(actual)
        helper.benchmark_stop(start)
        self.assertListEqual(actual, expected)
