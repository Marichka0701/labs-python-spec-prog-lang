from functions.display_menu import display_menu
from functions.menu import menu

def main():
    memory = 0
    result = 0 
    history = [] 
    decimal_places = 2  
    filename = "calculation_history.txt" 

    running = True
    while running:
        display_menu() 
        user_input = input("Enter the operation: ").strip().lower()

        memory, result, history, decimal_places, running = menu(user_input, memory, result, history, decimal_places, filename)