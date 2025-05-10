from abc import ABC, abstractmethod

class Print(ABC):
    @abstractmethod
    def print(self, a, b, result, operation):
        pass