import unittest
from list_exercises import sum_elements_of_a_list
from list_exercises import smallest_number_in_a_list
from list_exercises import largest_numbers_in_a_list
from list_exercises import multiplication_of_list_elements
from list_exercises import remove_duplicate_code
from list_exercises import cube_of_items_in_a_list
class MyTestCase(unittest.TestCase):
    def test_something(self):
        sum_of_numbers = sum_elements_of_a_list.sum_of_numbers([10, 20, 30])
        result = 60
        self.assertEqual(sum_of_numbers, result)
    def test_smallest_numbers(self):
        list_of_numbers = smallest_number_in_a_list.smallest_numbers([4,9,8,7])
        smallest_number = 4
        self.assertEqual(smallest_number, list_of_numbers)

    def test_largest_numbers(self):
        list_of_numbers = largest_numbers_in_a_list.largest_numbers([4,9,8,7])
        largest_number = 9
        self.assertEqual(largest_number, list_of_numbers)

    def test_multiplied_numbers(self):
        list_of_numbers = multiplication_of_list_elements.multuply_numbers([4, 9, 8, 7])
        multiplied_result = 784
        self.assertEqual(multiplied_result, list_of_numbers)

    def test_remove_duplicate_code(self):
        list_exercises = remove_duplicate_code.duplicated_list([7, 4, 3, 5, 6, 5, 7, 5, 8])
        removed_duplicate =[7, 4,  3, 5, 6, 8]
        self.assertEqual(removed_duplicate, list_exercises)

    def test_cube_of_numbers(self):
        list_of_numbers = cube_of_items_in_a_list.list_of_numbers_to_cube([3, 7, 2, 6, 5])
        result = [27, 343, 8, 216, 125]
        self.assertEquals(result,list_of_numbers)