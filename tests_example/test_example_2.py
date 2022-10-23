"""EXAMPLE TEST 2"""
from example_class.example_class_file_second import ExampleClassSecond


class TestExampleClassSecond:
    """EXAMPLE TEST 2"""

    def test_is_palindrome(self):
        """EXAMPLE TEST 2"""
        assert ExampleClassSecond().is_palindrome("racecar") is True

    def test_is_prime(self):
        """EXAMPLE TEST 2"""
        assert ExampleClassSecond().is_prime(7) is True

    def test_is_even(self):
        """EXAMPLE TEST 2"""
        assert ExampleClassSecond().is_even(4) is True
