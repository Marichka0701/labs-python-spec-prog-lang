from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def calc(self, num1, num2=None):
        pass
    
class Addition(Operation):
    def calc(self, num1, num2):
        return num1 + num2

class Subtraction(Operation):
    def calc(self, num1, num2):
        return num1 - num2

class Multiplication(Operation):
    def calc(self, num1, num2):
        return num1 * num2

class Division(Operation):
    def calc(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Can't divide by zero")
        return num1 / num2

class SquareRoot(Operation):
    def calc(self, num1, num2=None):
        return math.sqrt(num1)