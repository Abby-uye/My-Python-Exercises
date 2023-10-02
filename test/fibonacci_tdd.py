import unittest

from class_work.fibobacci_series import fibonacci


class MyTestCase(unittest.TestCase):
    def test_something(self,):
        fib = fibonacci(6)
        actual = 8
        self.assertEquals(actual,fib)
