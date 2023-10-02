import unittest
from new_concepts import Multiply_method


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Multiply_method.multiply(2, 2), 4)
        self.assertEqual(Multiply_method.multiply(4,4),16)
    def test_multiply(self):
        mutiplication =Multiply()