from unittest import TestCase
from class_work import biggest_odd

class Test(TestCase):
    def test_big_numbers(self):
        numbers = "23569"
        expected = 9
        actual = biggest_odd.big_numbers(numbers)
        self.assertEquals(expected,actual)

