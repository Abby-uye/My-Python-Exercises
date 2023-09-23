import unittest

from class_work.palindrome_function import palindrome

class MyTestCase(unittest.TestCase):
    def test_something(self):
        the_test = palindrome(12121)
        actual = True
        self.assertEquals(actual,the_test)

