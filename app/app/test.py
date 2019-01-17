from django.test import TestCase
from app.calc import add, substract


class CalcTest(TestCase):
    def test_add_numbers(self):
        """
        Test that two numbers are added together
        """
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """
        This will substract two numbers and return the result
        """
        self.assertEqual(substract(8, 3), 5)
