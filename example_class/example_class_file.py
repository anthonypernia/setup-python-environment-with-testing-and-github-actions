"""EXAMPLE CLASS """


class ExampleClass:
    """This is num_1 docstring for the EXAMPLE"""

    def __init__(self, name: str):
        """This is num_1 docstring for the __init__ method
        Args:
            name (str): The name of the ExampleClass object
        """
        self.name = name

    def multiplication(self, num_1: int, num_2: int) -> int:
        """This is num_1 docstring for the multiplication method

        Args:
            num_1 (int): The first number to multiply
            num_2 (int): The second number to multiply

        Returns:
            int: The product of num_1 and num_2
        """
        return num_1 * num_2

    def addition(self, num_1: int, num_2: int) -> int:
        """This is num_1 docstring for the addition method

        Args:
            num_1 (int): The first number to add
            num_2 (int): The second number to add

        Returns:
            int: The sum of num_1 and num_2
        """
        return num_1 + num_2

    def subtraction(self, num_1: int, num_2: int) -> int:
        """This is num_1 docstring for the subtraction method

        Args:
            num_1 (int): The first number to subtract
            num_2 (int): The second number to subtract

        Returns:
            int: The difference of num_1 and num_2
        """
        return num_1 - num_2

    def is_palindrome(self, word: str) -> bool:
        """Checks if a word is a palindrome
        Args:
            word (str): The word to check
        Returns:
            bool: True if the word is a palindrome, False otherwise
        """
        return word == word[::-1]

    def is_prime(self, number: int) -> bool:
        """Checks if a number is prime

        Args:
            number (int): The number to check

        Returns:
            bool: True if the number is prime, False otherwise
        """
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    return False
                    break
            else:
                return True
        else:
            return False

    def is_even(self, number: int) -> bool:
        """Checks if a number is even

        Args:
            number (int): The number to check

        Returns:
            bool: True if the number is even, False otherwise
        """
        return number % 2 == 0

    def is_odd(self, number: int) -> bool:
        """Checks if a number is odd

        Args:
            number (int): The number to check

        Returns:
            bool: True if the number is odd, False otherwise
        """
        return number % 2 != 0
