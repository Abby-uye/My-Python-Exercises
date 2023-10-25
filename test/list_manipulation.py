import unittest
from list_exercises.list_manipulations import list_of_numbers,list_of_odd_numbers,doubled_numbers


class MyTestCase(unittest.TestCase):
    def test_something(self):
        list_to_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        numbers = list_of_numbers(list_to_test)
        self.assertEqual(numbers, list_to_test)

    def test_that_odd_numbers(self):
        list_to_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        reduced_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        the_test = list_of_odd_numbers(list_of_numbers(list_to_test))
        self.assertEqual(reduced_list, the_test)

    def test_that_can_double_numbers(self):
        list_to_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        reduced_list = [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
        the_test = doubled_numbers(list_of_odd_numbers(list_of_numbers(list_to_test)))
        self.assertEqual(reduced_list, the_test)
