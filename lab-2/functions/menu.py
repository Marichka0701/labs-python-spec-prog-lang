from functions.display_menu import display_menu
from functions.calculate import calculate
from AppSettings import get_decimal_places
from AppSettings import update_decimal_places

def menu(calculator):
    while True:
        display_menu()  
        user_input = input("Enter the operation: ").strip().lower()
        if user_input == 'exit':
            break
        elif user_input == 'memory':
            calculator.memory_operations()
        elif user_input == 'history':
            calculator.show_history()
        elif user_input == 'settings':
            update_decimal_places() 
        else:
            try:
                operation_result = calculate(calculator, user_input)
                calculator.add_to_history(operation_result)
                print(operation_result)
            except Exception as e:
                print(f"Error: {e}")
