from functions.calculate import calculate
from AppSettings import settings
from functions.manage_history import manage_history
from functions.memory_operations import memory_operations
from functions.perform_calculation import perform_calculation

def menu(user_input, memory, result, history, decimal_places, filename):
    match user_input:
        case 'exit':
            return memory, result, history, decimal_places, False
        
        case 'memory':
            memory, result = memory_operations(memory, result)

        case 'history':
            history = manage_history(history, filename)

        case 'mc':
            memory = 0
            print("Memory cleared.")

        case 'settings':
            decimal_places = settings(decimal_places)
        
        case _:
            result, history = perform_calculation(user_input, decimal_places, result, history)

    return memory, result, history, decimal_places, True 