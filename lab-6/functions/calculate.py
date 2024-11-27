def calculate(calculator, user_input):
    parts = user_input.split()
    if len(parts) == 1 and parts[0] == 'sqrt':
        num = float(input("Enter the number for square root calculation: "))
        result = calculator.perform_operation('sqrt', num)
        return f"sqrt({num}) = {result:.{calculator.get_decimal_places()}f}"

    if len(parts) == 3:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
        result = calculator.perform_operation(operator, num1, num2)
        return f"{num1} {operator} {num2} = {result:.{calculator.get_decimal_places()}f}"

    raise ValueError("Invalid input. Please enter a valid operation.")