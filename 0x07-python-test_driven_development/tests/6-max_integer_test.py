#!/usr/bin/python3
""" A test module for 6-max_integer module """


import unittest
max_integer = __import__('6-max_integer').max_integer
class MaxTest(unittest.TestCase):
    """ attributes for testing 6-max_integer module """


    def test_types(self):
        """ check whether type errors are raised """
        self.assertRaises(TypeError, max_integer, (1, 2, 3))
        self.assertRaises(TypeError, max_integer, [1, "d", 3])

    def test_results(self):
        """ Test to confirm that the results are ok """
        self.assertEqual(max_integer([1, 3, 5, 4]), 5)
        self.assertEqual(max_integer([]), None)
