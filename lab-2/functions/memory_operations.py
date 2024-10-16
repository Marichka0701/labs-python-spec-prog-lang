from functions.calculate import calculate

def memory_operations(memory, result):
    print(f"Memory: {memory}")
    operation = input("Choose memory operation (ms = store, mr = recall, m+ = add): ").lower()
    if operation == 'ms':
        memory = result
        print(f"Stored in memory: {memory}")
    elif operation == 'mr':
        recalled_value = memory
        print(f"Recalled from memory: {recalled_value}")
        additional_operation = input("Do you want to perform an operation on this value? (yes/no): ").strip().lower()
        if additional_operation == 'yes':
            operator = input("Enter the operator (+, -, *, /): ")
            number = float(input("Enter the number: "))
            if operator in ['+', '-', '*', '/']:
                result = calculate(recalled_value, operator, number)
                print(f"Result after operation: {result}")
            else:
                print("Invalid operator.")
    elif operation == 'm+':
        memory += result
        print(f"Updated memory: {memory}")
    return memory, result