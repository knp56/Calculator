import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        testdata = CsvReader('/src/subtraction.csv').data
        pprint(testdata)
        for row in testdata:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), row['Result'])
            self.assertEqual(self.calculator.result, row['Result'])

    def test_subtract_method_calculator(self):
        testdata = CsvReader('/src/addition.csv').data
        pprint(testdata)
        for row in testdata:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), row['Result'])
            self.assertEqual(self.calculator.result, row['Result'])

    def test_multiply_method_calculator(self):
        testdata = CsvReader('/src/multiply.csv').data
        pprint(testdata)
        for row in testdata:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), row['Result'])
            self.assertEqual(self.calculator.result, row['Result'])

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(2, 2), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(3,2), 9)
        self.assertEqual(self.calculator.result, 9)

    def test_square_root_method_calculator(self):
        self.assertEqual(2, self.calculator.square_root(4))
        self.assertEqual(self.calculator.result, 2)

if __name__ == '__main__':
    unittest.main()
