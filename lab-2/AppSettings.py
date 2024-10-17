decimal_places = 2

def set_decimal_places(places):
    global decimal_places
    if places >= 0:
        decimal_places = places
    else:
        raise ValueError("Decimal places cannot be negative.")

def get_decimal_places():
    return decimal_places

def update_decimal_places():
    try:
        places = int(input("Enter the number of decimal places: "))
        set_decimal_places(places)
        print(f"New number of decimal places set to: {get_decimal_places()}")
    except ValueError:
        print("Please enter a valid integer.")
