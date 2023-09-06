import contextlib

from io import StringIO
from unittest import TestCase, main

from calculate.view import View

class TestView(TestCase):
    def setUp(self):
        self.temp_stdout = StringIO()
    
    def test_should_print_menu(self):
        with contextlib.redirect_stdout(self.temp_stdout):
            View.print_menu()
        
        output = self.temp_stdout.getvalue()
        expected_output = (
            "\n=========== MENU ===========\n"
            "1 - Addition\n"
            "2 - Soustraction\n"
            "3 - Multiplication\n"
            "4 - Division\n"
            "5 - Quitter\n"
            "============================\n")
        
        self.assertEqual(output.strip(), expected_output.strip())
        
    def test_should_print_end_message(self):
        with contextlib.redirect_stdout(self.temp_stdout):
            View.end_message()
        
        output = self.temp_stdout.getvalue()
        expected_output = ("=========== GOOD-BYE ===========")
        
        self.assertEqual(output.strip(), expected_output.strip())

    def test_should_print_result(self):
        operation = "2+2"
        result = 4
        with contextlib.redirect_stdout(self.temp_stdout):
            View.print_result(operation, result)
        
        output = self.temp_stdout.getvalue()
        expected_output = f"RESULTAT : {operation} = {result}\n"
        self.assertEqual(output.strip(), expected_output.strip())
        
    def test_should_print_result_error(self):
        operation = "2+3"
        result = None
        with contextlib.redirect_stdout(self.temp_stdout):
            View.print_result(operation, result)
            
        output = self.temp_stdout.getvalue()
        expected_output = (f"Votre operation est incorrect ! : {operation}\n")
        self.assertEqual(output.strip(), expected_output.strip())


if __name__ == "__main__":
    main()