import unittest

from Assignments.decimal_to_binary import decimal_to_binary_function,binary_to_decimal_function


class MyTestCase(unittest.TestCase):

    def testThatCanConvertDecimalToBinary(self):
        actual = decimal_to_binary_function(13)
        expected = [1101]
        self.assertEqual(expected, actual)
    def testThatCanConvertBinaryToDecimal(self):
        actual = binary_to_decimal_function([1101])
        expected = 13
        self.assertEqual(expected,actual)


