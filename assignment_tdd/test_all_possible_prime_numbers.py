import unittest

from Assignments.possible_prime_factors import finding_prime_factors


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual = finding_prime_factors(24)
        expected = [3, 8, 4, 2, 2, 2]
        self.assertEqual(expected, actual)
