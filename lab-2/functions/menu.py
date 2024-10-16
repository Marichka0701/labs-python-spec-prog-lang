from classes.HistoryManager import HistoryManager
from functions.memory_operations import memory_operations
from functions.perform_calculation import perform_calculation
from AppSettings import settings

def menu(user_input, memory, result, history, decimal_places, filename):
    history_manager = HistoryManager(filename)

    match user_input:
        case 'exit':
            return memory, result, history, decimal_places, False
        
        case 'memory':
            memory, result = memory_operations(memory, result)

        case 'history':
            print("Choose history operation: (view = view history, save = save history)")
            action = input("Your choice: ").lower()
            if action == 'view':
                history_manager.view_history()
            elif action == 'save':
                history_manager.save_history(history)

        case 'mc':
            memory = 0
            print("Memory cleared.")

        case 'settings':
            decimal_places = settings(decimal_places)
        
        case _:
            result, history = perform_calculation(user_input, decimal_places, result, history)

    return memory, result, history, decimal_places, True
