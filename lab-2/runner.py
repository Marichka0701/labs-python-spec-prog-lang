from classes.ConsoleReader import ConsoleReader
from classes.ConsoleWriter import ConsoleWriter
from classes.Calculator import Calculator
from functions.display_menu import display_menu
from functions.menu import menu

def main():
    calculator = Calculator()
    memory = 0
    result = 0
    history = []
    decimal_places = 2
    filename = "calculation_history.txt"

    running = True
    while running:
        display_menu()
        user_input = ConsoleReader.read_input("Enter the operation: ").strip().lower()

        memory, result, history, decimal_places, running = menu(user_input, memory, result, history, decimal_places, filename)

if __name__ == "__main__":
    main()
