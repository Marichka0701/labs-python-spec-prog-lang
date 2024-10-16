from classes.FileManager import FileManager

class HistoryManager:
    def __init__(self, filename):
        self.file_manager = FileManager(filename)

    def view_history(self):
        history = self.file_manager.read_from_file()
        print("Calculation history:")
        for entry in history:
            print(entry)

    def save_history(self, history):
        self.file_manager.write_to_file(history)
        print("History saved to file.")
