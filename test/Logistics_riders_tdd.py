import unittest

from Java_assignments.logistics_riders_pay import Logistics


class MyTestCase(unittest.TestCase):
    def test_if_i_have_a_clas(self):
        my_logistic = Logistics()
        self.assertIsNotNone(my_logistic)

    def test_that_something(self):
        my_logistic = Logistics()
        expected = my_logistic.riders_pay(4)
        actual = 5640
        self.assertEqual(expected, actual)

    def test_that_can_pay(self):
        my_logistic = Logistics()
        expected = my_logistic.riders_pay(78)
        actual = 44000
        self.assertEqual(expected, actual)

    def test_that_i_can_pay(self):
        my_logistic = Logistics()
        actual = my_logistic.riders_pay(64)
        expected = 21000
        self.assertEqual(actual, expected)
