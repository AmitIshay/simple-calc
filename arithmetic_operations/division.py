from arithmetic_operations.arithmetic_operation import ArithmeticOperation

# This class is the division operation
class Division(ArithmeticOperation):
    
    def calculate(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    