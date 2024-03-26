class MathOperations:
    pi = 5.32

    @staticmethod
    def add(x, y):

        return x + y

    @staticmethod
    def subtract(x, y):

        return x - y

    @staticmethod
    def multiply(x, y):

        return x * y

    @staticmethod
    def divide(x, y):
        return x / y
print("Value of pi:", MathOperations.pi)
print("Addition:", MathOperations.add(5, 3))
print("Subtraction:", MathOperations.subtract(5, 3))
print("Multiplication:", MathOperations.multiply(5, 3))
print("Division:", MathOperations.divide(5, 3))
