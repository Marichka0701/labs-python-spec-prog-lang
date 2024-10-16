from functions.calculate import calculate

def perform_calculation(user_input, decimal_places, result, history):
    try:
        if user_input.startswith('sqrt'):
            num1 = float(input("Enter the number for square root calculation: "))
            result = calculate(num1, '√', 0)
            result = round(result, decimal_places)
            print(f"Result: {format(result, f'.{decimal_places}f')}")
            history.append(f"√{num1} = {format(result, f'.{decimal_places}f')}")
            return result, history

        parts = user_input.split()
        if len(parts) == 3:
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            result = calculate(num1, operator, num2)
            result = round(result, decimal_places)
            print(f"Result: {format(result, f'.{decimal_places}f')}")
            history.append(f"{num1} {operator} {num2} = {format(result, f'.{decimal_places}f')}")

        return result, history

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    return result, history