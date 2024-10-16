from functions.write_to_file import write_to_file
from functions.read_from_file import read_from_file

def manage_history(history, filename):
    print("Choose history operation: (view = view history, save = save history)")
    action = input("Your choice: ").lower()
    if action == 'view':
        history = read_from_file(filename)
        print("Calculation history:")
        for entry in history:
            print(entry)
    elif action == 'save':
        write_to_file(filename, history)
        print("History saved to file.")
    return history