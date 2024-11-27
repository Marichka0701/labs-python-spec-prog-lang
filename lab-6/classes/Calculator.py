import math
from classes.FileManager import FileManager
from classes.HistoryManager import HistoryManager
from classes.Memory import Memory
from classes.Operation import Operation, Addition, Subtraction, Multiplication, Division, SquareRoot
from functions.calculate import calculate
from functions.display_menu import display_menu
from AppSettings import get_decimal_places

class Calculator:
    def __init__(self):
        self.__memory = Memory()
        self.__history_manager = HistoryManager("calculation_history.txt")
        self.__operations = {
            '+': Addition(),
            '-': Subtraction(),
            '*': Multiplication(),
            '/': Division(),
            'sqrt': SquareRoot(),
        }
        self.last_result = None 

    def perform_operation(self, operator, num1, num2=None):
        if operator not in self.__operations:
            raise ValueError("Invalid operator!")
        result = self.__operations[operator].calc(num1, num2)
        self.last_result = result 
        return result

    def memory_operations(self):
        self.__memory.perform_memory_operation(self.last_result)

    def show_history(self):
        self.__history_manager.view_history()

    def add_to_history(self, operation):
        self.__history_manager.add_to_history(operation)

    def get_decimal_places(self):
        return get_decimal_places() 
