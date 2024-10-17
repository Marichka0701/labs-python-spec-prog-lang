from classes.ConsoleReader import ConsoleReader
from classes.ConsoleWriter import ConsoleWriter
from functions.display_menu import display_menu
from functions.menu import menu
from classes.HistoryManager import HistoryManager
from classes.Calculator import Calculator

def main():
    calculator = Calculator() 
    memory = calculator.get_memory()
    result = 0
    history = calculator.get_history()  
    decimal_places = calculator.get_decimal_places()
    filename = "calculation_history.txt"

    running = True
    while running:
        display_menu()
        user_input = ConsoleReader().read_input("Enter the operation: ").strip().lower()

        memory, result, history, decimal_places, running = menu(user_input, memory, result, history, decimal_places, filename)

    history_manager = HistoryManager(filename)
    history_manager.save_history(history)

if __name__ == "__main__":
    main()
