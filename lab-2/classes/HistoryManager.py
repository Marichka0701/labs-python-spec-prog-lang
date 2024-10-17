from classes.FileManager import FileManager

class HistoryManager:
    def __init__(self, filename):
        self.file_manager = FileManager(filename)
        self.history = self.file_manager.read_from_file() 

    def add_to_history(self, operation):
        self.history.append(operation)
        self.save_history() 

    def view_history(self):
        print("Calculation history:")
        for entry in self.history:
            print(entry)

    def save_history(self):
        self.file_manager.write_to_file(self.history)
        print("History saved to file.")
