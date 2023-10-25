import unittest

from class_work import salary_calculation


class MyTestCase(unittest.TestCase):
    def test_That_Can_calculate_salary(self):
        test_can_calculate = salary_calculation.your_salary("Abby", 78)
        salary = 1560
        self.assertEqual(salary,test_can_calculate)

