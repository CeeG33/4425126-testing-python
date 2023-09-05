from unittest import TestCase, main
from calculate.view import View
from _pytest.capture import capsys



class TestView(TestCase):
    def test_should_print_menu(self, capsys):
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
        
        self.assertEqual(out.strip(), expected_output.strip())
        
    def test_should_print_end_message(self, capsys):
        View.end_message()
        out, err = capsys.readouterr()
        expected_output = ("=========== GOOD-BYE ===========")
        
        self.assertEqual(out.strip(), expected_output.strip())

    def test_should_print_result(self, capsys):
        operation = "2+2"
        result = 4
        expected_output = f"RESULTAT : {operation} = {result}\n"
        View.print_result(operation, result)
        out, err = capsys.readouterr()
        self.assertEqual(out.strip(), expected_output.strip())
        
    def test_should_print_result_error(self, capsys):
        operation = "2+3"
        result = None
        View.print_result(operation, result)
        out, err = capsys.readouterr()
        expected_output = (f"Votre operation est incorrect ! : {operation}\n")
        self.assertEqual(out.strip(), expected_output.strip())


if __name__ == "__main__":
    main()