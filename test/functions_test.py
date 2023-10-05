import unittest

from Assignments import functions
class MyTestCase(unittest.TestCase):
    def test_something(self):
        numbers = [7,8,4,2,]
        self.assertEqual(8,functions.numbers(numbers))

    def test_reverse(self):

        numbers = [5,4,3,2,1]
        self.assertEqual([1,2,3,4,5],functions.reverse_list(numbers))

    def test_if_item_exist(self):
        numbers = [5,7,3,2,9]
        item = 5
        self.assertEqual(True,functions.check_elements(numbers,item))

    def test_odd_index(self):
        numbers = [1,2,3,4]
        oddPosition = [2,4]
        self.assertEqual(oddPosition,functions.numbers(numbers))

    def test_running_total(self):
        numbers = [1,2,3,4,5,6,7,8,9]
        total = 45
        self.assertEquals(total,functions.running_total(numbers))
