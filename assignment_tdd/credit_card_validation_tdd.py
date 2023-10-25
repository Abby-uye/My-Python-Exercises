import unittest

from Assignments.credit_card import check_credit_card_type, even_position


class MyTestCase(unittest.TestCase):
    def test_something(self):
        check = check_credit_card_type([4, 5, 3, 2, 7, 6, 5, 8, 4, 3, 5, 8, 7, 9, 8, 7])
        expected = "Visa Card"
        self.assertEqual(expected, check)

    def test_that_can_calculate_even_position(self):
        check = even_position([4, 3, 8, 8, 5, 7, 6, 0, 1, 8, 4, 0, 2, 6, 2, 6])
        expected = 37
        self.assertEqual(expected, check)
