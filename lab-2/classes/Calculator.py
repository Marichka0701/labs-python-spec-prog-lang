import math

class Calculator:
    def __init__(self):
        self.__memory = 0 
        self.__history = []
        self.__decimal_places = 2 

    def get_memory(self):
        return self.__memory

    def add_to_memory(self, value):
        self.__memory += value

    def get_history(self):
        return self.__history

    def add_to_history(self, operation):
        self.__history.append(operation)

    def set_decimal_places(self, places):
        if places >= 0:
            self.__decimal_places = places
        else:
            raise ValueError("Decimal places cannot be negative.")

    def get_decimal_places(self):
        return self.__decimal_places
