# python -m unittest test_three_unittest.py
# python -m unittest discover

import unittest
import three_unittest

class Three_unittestTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(three_unittest.add(4, 5), 9)
        self.assertEqual(three_unittest.add(-1, 4), 3)
    def test_subtract(self):
        self.assertEqual(three_unittest.subtract(5, 0), 5)
    def test_multiply(self):
        self.assertEqual(three_unittest.multiply(4, 5), 20)
        self.assertEqual(three_unittest.multiply(7, 0), 0)
    def test_division(self):
        self.assertEqual(three_unittest.division(30, 5), 6)
        self.assertRaises(ZeroDivisionError, three_unittest.division, 4, 0)


if __name__ == '__main__':
    unittest.main()

