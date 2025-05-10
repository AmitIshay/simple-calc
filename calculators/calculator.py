
# This class is the calculator class based on the strategy pattern
class Calculator:
    def __init__(self,strategy):
        self.strategy = strategy
    
    def execute(self, a, b):
        return self.strategy.calculate(a, b)