import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add(self):
        self.assertEqual(self.calc.add(4, 6), 10)

    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 9), -7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_modulo(self):
       self.assertEqual(self.calc.modulo(3, 5), 0)
    def test_modulo(self):
       self.assertEqual(self.calc.modulo(10, 6), 4)

if __name__ == '__main__':
    unittest.main()