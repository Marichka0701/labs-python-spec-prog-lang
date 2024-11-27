class Memory:
    def __init__(self):
        self.__value = 0

    def store(self, value):
        self.__value = value

    def recall(self):
        return self.__value

    def clear(self):
        self.__value = 0

    def add(self, value):
        self.__value += value

    def perform_memory_operation(self, last_result):
        operation = input("Choose memory operation (store, recall, clear, add): ").strip().lower()
        if operation == 'store':
            value = float(input("Enter value to store: "))
            self.store(value)
            print(f"Stored {value} in memory.")
        elif operation == 'recall':
            print(f"Recalled from memory: {self.recall()}")
        elif operation == 'clear':
            self.clear()
            print("Memory cleared.")
        elif operation == 'add':
            self.add(last_result) 
            print(f"Added last result {last_result} to memory. New memory value: {self.recall()}.")
        else:
            print("Invalid operation.")