from calculators.calculator import Calculator
from arithmetic_operations.addition import Addition
from arithmetic_operations.subtraction import Subtraction
from arithmetic_operations.multiplication import Multiplication
from arithmetic_operations.division import Division
from prints.print_text import TextPrint

operations = {
    'add': Addition(),
    'sub': Subtraction(),
    'mul': Multiplication(),
    'div': Division()
}

printer = TextPrint()
print("Welcome to the calculator system")
print("This system can perform addition, subtraction, multiplication, and division")
print("Please enter two numbers and the operation you want to perform, for exit type 'exit'")


while True:
    try:
        a = input("Enter first number: ")
        if a == 'exit':
            print("Exiting, bye bye..")
            break
        b = input("Enter second number: ")
        if b == 'exit':
            print("Exiting, bye bye..")
            break
        operation = input("Enter add, sub, mul, div: ").strip().lower()
        a = float(a)
        b = float(b)
        if operation not in operations:
            print(f"Invalid operation '{operation}'. Please try again.")
            continue

        calc = Calculator(operations[operation])
        result = calc.execute(a, b)
        printer.print(a, b, result, operation)
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")
    
    
# examples = [
#     (10, 5, 'add'),
#     (10, 5, 'sub'),
#     (10, 5, 'mul'),
#     (10, 5, 'div')
# ]

# for a, b, op_key in examples:
#     operation = operations[op_key]
#     calc = Calculator(operation)
#     result = calc.execute(a, b)
#     print.print(a, b, result, op_key)