def write_to_file(filename, history):
    with open(filename, 'w') as file:
        for entry in history:
            file.write(entry + '\n')
    print(f"Calculation history is recorded in the file: {filename}")