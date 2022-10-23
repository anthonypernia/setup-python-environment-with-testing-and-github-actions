"""EXAMPLE TEST 2"""
from example_class.example_class_file2 import ExampleClass2


class TestExampleClass2:
    """EXAMPLE TEST 2"""

    def test_is_palindrome(self):
        """EXAMPLE TEST 2"""
        assert ExampleClass2().is_palindrome("racecar") is True

    def test_is_prime(self):
        """EXAMPLE TEST 2"""
        assert ExampleClass2().is_prime(7) is True

    def test_is_even(self):
        """EXAMPLE TEST 2"""
        assert ExampleClass2().is_even(4) is True
