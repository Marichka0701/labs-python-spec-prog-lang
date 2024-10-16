from functions.file_manager import FileManager

def manage_history(history, filename):
    file_manager = FileManager(filename) 
    print("Choose history operation: (view = view history, save = save history)")
    action = input("Your choice: ").lower()
    
    if action == 'view':
        history = file_manager.read_from_file()
        print("Calculation history:")
        for entry in history:
            print(entry)
    
    elif action == 'save':
        file_manager.write_to_file(history)  
        print("History saved to file.")
    
    return history
