from functions.display_menu import display_menu
from functions.calculate import calculate
from AppSettings import get_decimal_places
from AppSettings import update_decimal_places

def menu(calculator):
    while True:
        display_menu()  
        user_input = input("Enter the operation: ").strip().lower()
        
        match user_input:
            case 'exit':
                break
            case 'memory':
                calculator.memory_operations()
            case 'history':
                calculator.show_history()
            case 'settings':
                update_decimal_places()
            case _:
                try:
                    operation_result = calculate(calculator, user_input)
                    calculator.add_to_history(operation_result)
                    print(operation_result)
                except Exception as e:
                    print(f"Error: {e}")
