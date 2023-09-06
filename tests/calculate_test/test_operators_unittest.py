from unittest import TestCase, main

from calculate.operators import Operators

operator = Operators()
class TestOperators(TestCase):
    
    def test_should_make_additions(self):
        operation = "10 + 20.5"
        expected_value = 30.5
        self.assertEqual(operator.addition(operation), expected_value)

    def test_should_make_multiple_additions(self):
        operation = "10 + 5 + 20.5 + 12.7"
        expected_value = 48.2
        self.assertEqual(operator.addition(operation), expected_value)
        
    def test_addition_should_return_none_with_wrong_operator(self):
        operation = "10 + 10 - 10"
        expected_value = None
        self.assertEqual(operator.addition(operation), expected_value)
        
    def test_addition_should_return_none_with_wrong_characters(self):
        operation = "10 + c - b"
        expected_value = None
        self.assertEqual(operator.addition(operation), expected_value)
        
    def test_addition_should_return_none_with_wrong_separator(self):
        operation = "10 + 20,5"
        expected_value = None
        self.assertEqual(operator.addition(operation), expected_value)
        
    def test_addition_should_return_none_with_wrong_space(self):
        operation = "10e+e20.5"
        expected_value = None
        self.assertEqual(operator.addition(operation), expected_value)
        
    def test_should_make_substractions(self):
        operation = "10 - 20.5"
        expected_value = -10.5
        self.assertEqual(operator.substraction(operation), expected_value)
        
    def test_should_make_multiple_substractions(self):
        operation = "10 - 20.5 - 20.5 - 5"
        expected_value = -36
        self.assertEqual(operator.substraction(operation), expected_value)
        
    def test_substraction_should_return_none_with_wrong_operator(self):
        operation = "10 + 10 - 10"
        expected_value = None
        self.assertEqual(operator.substraction(operation), expected_value)
        
    def test_substraction_should_return_none_with_wrong_characters(self):
        operation = "10 - c - b"
        expected_value = None
        self.assertEqual(operator.substraction(operation), expected_value)
        
    def test_substraction_should_return_none_with_wrong_separator(self):
        operation = "10 - 20,5"
        expected_value = None
        self.assertEqual(operator.substraction(operation), expected_value)
        
    def test_substraction_should_return_none_with_wrong_space(self):
        operation = "10e-e20.5"
        expected_value = None
        self.assertEqual(operator.substraction(operation), expected_value)
        
    def test_should_make_multiplications(self):
        operation = "1 * 2.5"
        expected_value = 2.5
        self.assertEqual(operator.multiplication(operation), expected_value)
        
    def test_should_make_multiple_multiplications(self):
        operation = "1 * 5 * 3 * 2"
        expected_value = 30
        self.assertEqual(operator.multiplication(operation), expected_value)
        
    def test_multiplication_should_return_none_with_wrong_operator(self):
        operation = "10 * 10 - 10"
        expected_value = None
        self.assertEqual(operator.multiplication(operation), expected_value)
        
    def test_multiplication_should_return_none_with_wrong_characters(self):
        operation = "10 * c * b"
        expected_value = None
        self.assertEqual(operator.multiplication(operation), expected_value)
        
    def test_multiplication_should_return_none_with_wrong_separator(self):
        operation = "10 * 20,5"
        expected_value = None
        self.assertEqual(operator.multiplication(operation), expected_value)
        
    def test_multiplication_should_return_none_with_wrong_space(self):
        operation = "10e*e20.5"
        expected_value = None
        self.assertEqual(operator.multiplication(operation), expected_value)
        
    def test_should_make_divisions(self):
        operation = "30 / 2"
        expected_value = 15
        self.assertEqual(operator.division(operation), expected_value)
        
    def test_should_make_multiple_divisions(self):
        operation = "60 / 2 / 2"
        expected_value = 15
        self.assertEqual(operator.division(operation), expected_value)
        
    def test_division_should_return_none_with_wrong_operator(self):
        operation = "10 / 2 - 2"
        expected_value = None
        self.assertEqual(operator.division(operation), expected_value)
        
    def test_division_should_return_none_with_wrong_characters(self):
        operation = "10 / c / b"
        expected_value = None
        self.assertEqual(operator.division(operation), expected_value)
        
    def test_division_should_return_none_with_wrong_separator(self):
        operation = "10 / 2,5"
        expected_value = None
        self.assertEqual(operator.division(operation), expected_value)
        
    def test_division_should_return_none_with_wrong_space(self):
        operation = "10e/e2"
        expected_value = None
        self.assertEqual(operator.division(operation), expected_value)
        
    def test_division_should_return_none_with_zero_division(self):
        operation = "10 / 0"
        expected_value = None
        self.assertEqual(operator.division(operation), expected_value)
        

if __name__ == "__main__":
    main()