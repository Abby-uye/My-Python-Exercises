import unittest
from list_exercises import sum_elements_of_a_list


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sum_of_numbers = sum_elements_of_a_list.sum_of_numbers([10, 20, 30])
        result = 60
        self.assertEqual(sum_of_numbers, result)
        # self.assertEqual(60, sum_elements_of_a_list.sum_of_numbers([10, 20, 30]))
