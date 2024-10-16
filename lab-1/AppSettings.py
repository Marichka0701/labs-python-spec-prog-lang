def settings(decimal_places):
    try:
        decimal_places = int(input("Enter the number of decimal places: "))
        print(f"New number of decimal places: {decimal_places}")
    except ValueError:
        print("Please enter a valid integer.")
    return decimal_places