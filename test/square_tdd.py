import unittest

from new_concepts.Square_of_numbers import SquareOfNumbers


class MyTestCase(unittest.TestCase):
    def test_that_i_can_multiply(self):
        square_of_numbers = SquareOfNumbers()
        expected = square_of_numbers.square_of_numbers()
        actual = 25
        self.assertEquals(expected,actual)

