import unittest

from class_work.EvenAndOddNumber import even_odd


class MyTestCase(unittest.TestCase):
    def test_something(self):
        the_test = even_odd([2,5,7,8])
        even = 2
        odd = 2
        self.assertEquals(even,odd,the_test)
