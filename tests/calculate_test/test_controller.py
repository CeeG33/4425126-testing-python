from calculate.operators import Operators
from calculate import view
from calculate.controller import Controller


sut = Controller()

def test_quit(mocker):
    mock = mocker.patch("calculate.view.View.get_user_input", return_value = 5)
    
def test_addition(mocker):
    expected_value = 1.0
    mock = mocker.patch("calculate.view.View.get_user_input")
    mock.side_effect = ["1", "10+10", "5"]
    mocker.patch("calculate.operators.Operators.addition", return_value = expected_value)
    mocker.patch("calculate.view.View.continue_message")
    
    sut.run()
    assert sut.result == expected_value
    
def test_substraction(mocker):
    expected_value = 1.0
    mock = mocker.patch("calculate.view.View.get_user_input")
    mock.side_effect = ["2", "10-10", "5"]
    mocker.patch("calculate.operators.Operators.substraction", return_value = expected_value)
    mocker.patch("calculate.view.View.continue_message")
    
    sut.run()
    assert sut.result == expected_value
    
def test_multiplication(mocker):
    expected_value = 6.0
    mock = mocker.patch("calculate.view.View.get_user_input")
    mock.side_effect = ["3", "10*10", "5"]
    mocker.patch("calculate.operators.Operators.multiplication", return_value = expected_value)
    mocker.patch("calculate.view.View.continue_message")
    
    sut.run()
    assert sut.result == expected_value
    
def test_division(mocker):
    expected_value = 6.0
    mock = mocker.patch("calculate.view.View.get_user_input")
    mock.side_effect = ["4", "12/2", "5"]
    mocker.patch("calculate.operators.Operators.division", return_value = expected_value)
    mocker.patch("calculate.view.View.continue_message")
    
    sut.run()
    assert sut.result == expected_value