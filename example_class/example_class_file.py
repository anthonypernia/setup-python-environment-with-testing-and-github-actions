"""EXAMPLE CLASS"""


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
