from calculate.operators import Operators

def test_should_make_multiple_additions():
    sut = Operators()
    operation = "10 + 5 + 20.5 + 12.7"
    expected_value = 48.2
    assert sut.addition(operation) == expected_value