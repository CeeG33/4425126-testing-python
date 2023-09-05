from calculate.operators import Operators

operator = Operators()

def test_should_make_additions():
    operation = "10 + 20.5"
    expected_value = 30.5
    assert operator.addition(operation) == expected_value

def test_should_make_multiple_additions():
    operation = "10 + 5 + 20.5 + 12.7"
    expected_value = 48.2
    assert operator.addition(operation) == expected_value
    
def test_addition_should_return_none_with_wrong_operator():
    operation = "10 + 10 - 10"
    expected_value = None
    assert operator.addition(operation) == expected_value
    
def test_addition_should_return_none_with_wrong_characters():
    operation = "10 + c - b"
    expected_value = None
    assert operator.addition(operation) == expected_value
    
def test_addition_should_return_none_with_wrong_separator():
    operation = "10 + 20,5"
    expected_value = None
    assert operator.addition(operation) == expected_value
    
def test_addition_should_return_none_with_wrong_space():
    operation = "10e+e20.5"
    expected_value = None
    assert operator.addition(operation) == expected_value
    
def test_should_make_substractions():
    operation = "10 - 20.5"
    expected_value = -10.5
    assert operator.substraction(operation) == expected_value
    
def test_should_make_multiple_substractions():
    operation = "10 - 20.5 - 20.5 - 5"
    expected_value = -36
    assert operator.substraction(operation) == expected_value
    
def test_substraction_should_return_none_with_wrong_operator():
    operation = "10 + 10 - 10"
    expected_value = None
    assert operator.substraction(operation) == expected_value
    
def test_substraction_should_return_none_with_wrong_characters():
    operation = "10 - c - b"
    expected_value = None
    assert operator.substraction(operation) == expected_value
    
def test_substraction_should_return_none_with_wrong_separator():
    operation = "10 - 20,5"
    expected_value = None
    assert operator.substraction(operation) == expected_value
    
def test_substraction_should_return_none_with_wrong_space():
    operation = "10e-e20.5"
    expected_value = None
    assert operator.substraction(operation) == expected_value
    
def test_should_make_multiplications():
    operation = "1 * 2.5"
    expected_value = 2.5
    assert operator.multiplication(operation) == expected_value
    
def test_should_make_multiple_multiplications():
    operation = "1 * 5 * 3 * 2"
    expected_value = 30
    assert operator.multiplication(operation) == expected_value
    
def test_multiplication_should_return_none_with_wrong_operator():
    operation = "10 * 10 - 10"
    expected_value = None
    assert operator.multiplication(operation) == expected_value
    
def test_multiplication_should_return_none_with_wrong_characters():
    operation = "10 * c * b"
    expected_value = None
    assert operator.multiplication(operation) == expected_value
    
def test_multiplication_should_return_none_with_wrong_separator():
    operation = "10 * 20,5"
    expected_value = None
    assert operator.multiplication(operation) == expected_value
    
def test_multiplication_should_return_none_with_wrong_space():
    operation = "10e*e20.5"
    expected_value = None
    assert operator.multiplication(operation) == expected_value
    
def test_should_make_divisions():
    operation = "30 / 2"
    expected_value = 15
    assert operator.division(operation) == expected_value
    
def test_should_make_multiple_divisions():
    operation = "60 / 2 / 2"
    expected_value = 15
    assert operator.division(operation) == expected_value
    
def test_division_should_return_none_with_wrong_operator():
    operation = "10 / 2 - 2"
    expected_value = None
    assert operator.division(operation) == expected_value
    
def test_division_should_return_none_with_wrong_characters():
    operation = "10 / c / b"
    expected_value = None
    assert operator.division(operation) == expected_value
    
def test_division_should_return_none_with_wrong_separator():
    operation = "10 / 2,5"
    expected_value = None
    assert operator.division(operation) == expected_value
    
def test_division_should_return_none_with_wrong_space():
    operation = "10e/e2"
    expected_value = None
    assert operator.division(operation) == expected_value
    
def test_division_should_return_none_with_zero_division():
    operation = "10 / 0"
    expected_value = None
    assert operator.division(operation) == expected_value