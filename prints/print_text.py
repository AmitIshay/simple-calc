from prints.print import Print

class TextPrint(Print):
    def print(self, a, b, result, operation):
        print(f"{operation}: {a} and {b} => {result}")
        
    
    def print_exit(self, result):
        if result == 'exit':
            print("Exiting, bye bye..")
            return True
        return False
    
    def print_welcome(self):
        print("Welcome to the calculator system")
        print("This system can perform addition, subtraction, multiplication, and division")
        print("Please enter two numbers and the operation you want to perform, for exit type 'exit'")
