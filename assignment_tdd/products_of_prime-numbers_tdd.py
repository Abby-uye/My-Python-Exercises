import unittest

from Assignments.products_of_prime_numbers import lcm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual = lcm(30)
        expected = [2, 3, 5]
        self.assertEqual(expected, actual)
