
from example_class.example_class_file import ExampleClass


class TestExampleClass:

    def test_multiplication(self):
        assert ExampleClass('example').multiplication(2, 2) == 4

    def test_division(self):
        assert ExampleClass('example').division(2, 2) == 1

    def test_addition(self):
        assert ExampleClass('example').addition(2, 2) == 4

    def test_subtraction(self):
        assert ExampleClass('example').subtraction(2, 2) == 0

    def test_str(self):
        assert str(ExampleClass('example')) == 'example'

    def test_subtraction(self):
        assert ExampleClass('example').subtraction(2, 2) == 5
        

