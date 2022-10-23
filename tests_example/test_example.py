"""EXAMPLE TEST"""
from example_class.example_class_file import ExampleClass


class TestExampleClass:
    """EXAMPLE TEST"""

    def test_multiplication(self):
        """this is a test docstring"""
        assert ExampleClass("example").multiplication(2, 2) == 4

    def test_addition(self):
        """this is a test docstring"""
        assert ExampleClass("example").addition(2, 2) == 4

    def test_subtraction(self):
        """this is a test docstring"""
        assert ExampleClass("example").subtraction(2, 2) == 0

    def test_is_palindrome(self):
        """EXAMPLE TEST 2"""
        assert ExampleClass("example").is_palindrome("racecar") is True

    def test_is_prime(self):
        """EXAMPLE TEST 2"""
        assert ExampleClass("example").is_prime(7) is True

    def test_is_even(self):
        """EXAMPLE TEST 2"""
        assert ExampleClass("example").is_even(4) is True
