import unittest

from new_concepts.regius_portus_app import Regius_portus


class MyTestCase(unittest.TestCase):
    def test_that_user_have_name(self):
        user_uye = Regius_portus()
        first_name = user_uye.user_name(self)
        user_first_name = "Abigail"
        assertEqual("Abigail",first_name)



