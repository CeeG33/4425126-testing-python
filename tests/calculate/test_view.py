from calculate.view import View
from _pytest.capture import capsys

def test_should_print_result(capsys):
    operation = "2+2"
    result = 4
    expected_output = f"RESULTAT : {operation} = {result}\n"
    View.print_result(operation, result)
    out, err = capsys.readouterr()
    assert out == expected_output
