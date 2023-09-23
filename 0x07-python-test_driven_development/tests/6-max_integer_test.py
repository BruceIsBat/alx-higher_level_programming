#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """ This class of the test
    """
    def test_max(self):
        """This is the function for test

        Args:
            self: self call
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([202, 4, 5, 9, 10]), 202)


if __name__ == '__main__':
    import unittest
    unittest.main()
