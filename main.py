from calculators.calculator import Calculator
from arithmetic_operations.addition import Addition
from arithmetic_operations.subtraction import Subtraction
from arithmetic_operations.multiplication import Multiplication
from arithmetic_operations.division import Division
from arithmetic_operations.expression import Expression
from prints.print_text import TextPrint

operations = {
    'add': Addition(),
    'sub': Subtraction(),
    'mul': Multiplication(),
    'div': Division(),
    'expr': Expression()
}

printer = TextPrint()
printer.print_welcome()


while True:
    try:
        operation = input("Enter add, sub, mul, div, expr: ").strip().lower()
        if printer.print_exit(operation):
            break

        if operation == 'expr':
            expression = input("Enter full expression: ")
            if printer.print_exit(expression):
                break
            calc = Calculator(operations[operation])
            result = calc.execute(expression, None)
            print(f"Result: {result}")
            continue

        a = input("Enter first number: ")
        if printer.print_exit(a):
            break
        b = input("Enter second number: ")
        if printer.print_exit(b):
            break
        
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