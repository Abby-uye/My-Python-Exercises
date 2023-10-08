import unittest

from  tuple_assignments import unpack_tuple
from tuple_assignments import reverse_tuple


class MyTestCase(unittest.TestCase):
    def test_something(self):

       tuple_list = items_to_unpack = unpack_tuple.unpacking_tuple((15,25,60,50,30,40,45,55))
       expected = (55, 15)
       self.assertEquals(expected, tuple_list)

    def testThatIcanReverseTuple(self):
        tuple_to_reverse = reverse_tuple.reverse_tuple((5,4,3,2,1))
        reversed_tuple = (1,2,3,4,5)
        self.assertEqual(reversed_tuple,tuple_to_reverse)
