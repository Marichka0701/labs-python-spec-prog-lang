def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readlines()
        return [entry.strip() for entry in data]
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return []