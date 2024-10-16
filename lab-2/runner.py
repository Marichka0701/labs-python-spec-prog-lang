from classes.ConsoleReader import ConsoleReader
from classes.ScientificCalculator import ScientificCalculator
from classes.ConsoleWriter import ConsoleWriter
from functions.display_menu import display_menu
from functions.menu import menu
from classes.HistoryManager import HistoryManager

def main():
    calculator = ScientificCalculator() 
    memory = calculator.get_memory()
    result = 0
    history = calculator.get_history()  
    decimal_places = calculator.get_decimal_places()
    filename = "calculation_history.txt"

    running = True
    while running:
        display_menu()
        user_input = ConsoleReader().read_input("Enter the operation: ").strip().lower()

        if user_input.startswith("sin") or user_input.startswith("cos"):
            try:
                parts = user_input.split()
                if len(parts) != 2:
                    raise ValueError("Invalid input format. Use: <function> <angle>")
                function, angle_str = parts
                angle = float(angle_str)
                if function == "sin":
                    result = calculator.sin(angle)
                elif function == "cos":
                    result = calculator.cos(angle)
                ConsoleWriter().write_output(f"{function}({angle}) = {result}")
                # Оновлюємо історію
                history = calculator.get_history()
            except IndexError:
                ConsoleWriter().write_output("Please provide an angle for the function.")
            except ValueError as ve:
                ConsoleWriter().write_output(f"Invalid input: {ve}")
        else:
            memory, result, history, decimal_places, running = menu(user_input, memory, result, history, decimal_places, filename)

    history_manager = HistoryManager(filename)
    history_manager.save_history(history)

if __name__ == "__main__":
    main()
