# from classes.ConsoleReader import ConsoleReader
# from classes.ConsoleWriter import ConsoleWriter
# from classes.Calculator import Calculator
# from functions.display_menu import display_menu
# from functions.menu import menu

# def main():
#     calculator = Calculator()
#     memory = calculator.get_memory()
#     result = 0
#     history = calculator.get_history()  
#     decimal_places = calculator.get_decimal_places()
#     filename = "calculation_history.txt"

#     running = True
#     while running:
#         display_menu()
#         user_input = ConsoleReader().read_input("Enter the operation: ").strip().lower()

#         memory, result, history, decimal_places, running = menu(user_input, memory, result, history, decimal_places, filename)

# if __name__ == "__main__":
#     main()

from abc import ABC, abstractmethod
import math

# Абстрактний клас для калькулятора
class AbstractCalculator(ABC):
    @abstractmethod
    def perform_calculation(self, operation):
        pass

    @abstractmethod
    def get_memory(self):
        pass

# Основний калькулятор
class Calculator(AbstractCalculator):
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

    def perform_calculation(self, operation):
        # Реалізація базових арифметичних операцій
        try:
            result = eval(operation)  # Використання eval (з обережністю)
            self.add_to_history(f"{operation} = {result}")
            return round(result, self.__decimal_places)
        except Exception as e:
            print(f"Error: {e}")
            return None

# Клас наукового калькулятора
class ScientificCalculator(Calculator):
    def sin(self, angle_degrees):
        # Обчислення синуса
        angle_radians = math.radians(angle_degrees)
        result = math.sin(angle_radians)
        self.add_to_history(f"sin({angle_degrees}) = {result}")
        return round(result, self.get_decimal_places())

# Основна функція
def main():
    calculator = Calculator()
    scientific_calculator = ScientificCalculator()

    # Виконання базових обчислень
    print(calculator.perform_calculation("3 + 5"))
    
    # Використання наукового калькулятора
    angle = 30
    print(f"sin({angle}) = {scientific_calculator.sin(angle)}")

    # Перевірка історії обчислень
    print("Calculation History:")
    for entry in calculator.get_history():
        print(entry)

    print("Scientific Calculation History:")
    for entry in scientific_calculator.get_history():
        print(entry)

if __name__ == "__main__":
    main()
