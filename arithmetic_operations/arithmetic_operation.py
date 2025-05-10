from abc import ABC, abstractmethod

# This class is the abstract class for arithmetic operations
class ArithmeticOperation(ABC):
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        pass