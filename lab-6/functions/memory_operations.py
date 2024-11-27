def memory_operations(memory):
    print(f"Memory: {memory.recall()}")
    operation = input("Choose memory operation (store, recall, clear, add): ").lower()
    return memory.perform_memory_operation(operation)
