import unittest
import main

class TestMain(unittest.TestCase):

    def test_count_numbers(self):
        self.assertEqual(main.count_numbers([3, 4, 5, 6], 1), 0)
        self.assertEqual(main.count_numbers([0, 15, 32, 2000, 15000], 15), 1)
        self.assertEqual(main.count_numbers([1, 1, 10, 32, 41], 42), 2)

        