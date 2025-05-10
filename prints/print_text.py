from prints.print import Print

class TextPrint(Print):
    def print(self, a, b, result, operation):
        print(f"{operation}: {a} and {b} => {result}")