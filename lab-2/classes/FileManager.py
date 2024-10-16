class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def read_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                data = file.readlines()
            return [entry.strip() for entry in data]
        except FileNotFoundError:
            print(f"Файл {self.filename} не знайдено.")
            return []

    def write_to_file(self, history):
        with open(self.filename, 'w') as file:
            for entry in history:
                file.write(entry + '\n')
        print(f"Calculation history is recorded in the file: {self.filename}")