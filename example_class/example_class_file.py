

class ExampleClass:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def multiplication(self, a: int, b: int) -> int:
        return a * b

    def division(self, a: int, b: int) -> int:
        return a / b

    def addition(self, a: int, b: int) -> int:
        return a + b

    def subtraction(self, a: int, b: int) -> int:
        return a - b
        
