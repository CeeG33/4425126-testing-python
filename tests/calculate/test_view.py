from calculate.view import View
from _pytest.capture import capsys

def test_should_print_menu(capsys):
    View.print_menu()
    out, err = capsys.readouterr()
    expected_output = (
        "\n=========== MENU ===========\n"
        "1 - Addition\n"
        "2 - Soustraction\n"
        "3 - Multiplication\n"
        "4 - Division\n"
        "5 - Quitter\n"
        "============================\n")
    
    assert out.strip() == expected_output.strip()
    
def test_should_print_end_message(capsys):
    View.end_message()
    out, err = capsys.readouterr()
    expected_output = ("=========== GOOD-BYE ===========")
    
    assert out.strip() == expected_output.strip()

def test_should_print_result(capsys):
    operation = "2+2"
    result = 4
    expected_output = f"RESULTAT : {operation} = {result}\n"
    View.print_result(operation, result)
    out, err = capsys.readouterr()
    assert out == expected_output
    
def test_should_print_result_error(capsys):
    operation = "2+3"
    result = None
    View.print_result(operation, result)
    out, err = capsys.readouterr()
    expected_output = (f"Votre operation est incorrect ! : {operation}\n")
    assert out == expected_output
