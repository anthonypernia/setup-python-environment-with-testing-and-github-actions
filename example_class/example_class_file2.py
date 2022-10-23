""" EXAMPLE CLASS 2 """


class ExampleClass2:
    """EXAMPLE CLASS 2"""

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
