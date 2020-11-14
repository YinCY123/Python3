import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """test for class employee"""

    def setUp(self):
        """create a employee instance used in all test"""
        self.my_employee = Employee("Yin", "Chunyou", 100000)

    def test_default_raise(self):
        """test for the default raise"""
        self.my_employee.give_raise()
        self.assertEqual(105000, self.my_employee.annual_salary)

    def test_give_custom_raise(self):
        """test for the custom raise"""
        self.my_employee.give_raise(amount=100000)
        self.assertEqual(110000, self.my_employee.annual_salary)

unittest.main()
